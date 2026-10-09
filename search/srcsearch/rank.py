"""Ranked search, definitions and the concordance (DESIGN §6, §7).

Ranked search fuses two rankings, then multiplies in query-independent priors:
- lexical: BM25 on exact word forms plus half-weight BM25 on English stems, with
  a phrase factor and a heading factor, computed in Postgres over every passage
  that holds a query word;
- semantic: cosine distance between the query's embedding and each passage's,
  the nearest `semantic_pool`;
- fusion: RRF by default (Joseph's choice, 2026-10-09), or memorata's mix;
- priors: the definition boost, section kind, superseded status, Influence and
  recency (search/weights.toml, each with its reason).

Verbatim copies are shown once, with where else they occur (DESIGN §6.3): copying
is evidence here, so it is surfaced, not discarded.
"""
import math, os, re, tomllib
from collections import defaultdict

from . import SEARCH
from .text import fold, norm_term, words
import corpus

WEIGHTS_PATH = os.path.join(SEARCH, 'weights.toml')
STOP = set('a an and are as at be by for from has have in is it its of on or that the this to was were will with '
           'which we our what how does do'.split())
DEF_INTENT = re.compile(r'^\s*(?:(?:the\s+)?(?:definitions?|meaning|sense)s?\s+of|what\s+(?:is|are)(?:\s+an?)?|'
                        r'define|definition:)\s+', re.I)


def weights():
    return tomllib.load(open(WEIGHTS_PATH, 'rb'))


def parse(query):
    """The query with OCR's "Al" corrected, the term it asks about ("definition of X"
    asks about X), and its content words."""
    q = corpus.fix_ocr_ai(query)[0].strip()
    term = DEF_INTENT.sub('', q).strip(' ?"\'“”‘’')
    ws = [w for w in words(term) if w not in STOP] or words(term)
    return dict(query=q, term=term, norm=norm_term(term), words=ws)


# ------------------------------------------------------------------- filters
def doc_filter(conn, specs):
    """Keys matching --in specs: a key, a catalog Code, an organisation, a catalog
    section or group label. None when there are no specs."""
    if not specs:
        return None
    keys = set()
    for s in specs:
        rows = conn.execute(
            "select key from src.documents where key = %(s)s or lower(replace(code, ' ', '')) = lower(replace(%(s)s, ' ', '')) "
            "or org ilike %(p)s or section ilike %(p)s or group_label ilike %(p)s or key like %(k)s",
            dict(s=s, p=f'%{s}%', k=s.rstrip('*') + '%' if s.endswith('*') else s)).fetchall()
        if not rows:
            raise SystemExit(f'--in {s!r} matches no document (a key, a catalog Code, an organisation or a catalog section)')
        keys.update(r[0] for r in rows)
    return sorted(keys)


# ------------------------------------------------------------------- lexical
_STATS = {}


def _stats(conn):
    if not _STATS:
        n, avg = conn.execute("select count(*), avg(nwords) from src.passages where layer = 'canonical'").fetchone()
        _STATS.update(n=n, avg=float(avg or 1))
    return _STATS


def _lexemes(conn, cfg, text):
    return [r[0] for r in conn.execute(f"select lexeme from unnest(to_tsvector('{cfg}', %s))", (text,))]


def _bm25(conn, col, cfg, lexemes, w, keys):
    """{passage id: BM25} over passages holding any of lexemes, in column col."""
    if not lexemes:
        return {}
    st = _stats(conn)
    rows = conn.execute(
        # df is materialised: inlined, Postgres re-ran its count for every joined row (51 s for "catastrophic risk")
        f"""with q(lex) as (select unnest(%(lex)s::text[])),
               df as materialized (select lex, (select count(*) from src.passages p
                                   where p.{col} @@ quote_literal(q.lex)::tsquery) n from q),
               orq as (select string_agg(quote_literal(lex), ' | ')::tsquery t from q)
           select p.id, sum(ln(1 + (%(N)s - df.n + 0.5) / (df.n + 0.5))
                            * x.tf * (%(k1)s + 1) / (x.tf + %(k1)s * (1 - %(b)s + %(b)s * p.nwords / %(avg)s)))
           from src.passages p, orq,
                lateral (select lexeme, coalesce(array_length(positions, 1), 1) tf from unnest(p.{col})) x
           join df on df.lex = x.lexeme
           where p.{col} @@ orq.t and (%(keys)s::text[] is null or p.doc_key = any(%(keys)s))
           group by p.id""",
        dict(lex=lexemes, N=st['n'], avg=st['avg'], k1=w['k1'], b=w['b'], keys=keys)).fetchall()
    return {i: float(s) for i, s in rows}


def lexical(conn, pq, w, keys):
    text = ' '.join(pq['words'])
    exact = _bm25(conn, 'tsv_exact', 'simple', _lexemes(conn, 'simple', text), w, keys)
    stem = _bm25(conn, 'tsv_stem', 'english', _lexemes(conn, 'english', text), w, keys)
    score = defaultdict(float)
    for i, s in exact.items():
        score[i] += s
    for i, s in stem.items():
        score[i] += w['stem_weight'] * s
    if not score:
        return {}, set(), set()
    ids = list(score)
    phrase, heading = set(), set()
    if len(pq['words']) > 1:
        phrase = {r[0] for r in conn.execute(
            "select id from src.passages where id = any(%s) and tsv_exact @@ phraseto_tsquery('simple', %s)",
            (ids, text))}
    heading = {r[0] for r in conn.execute(
        "select id from src.passages where id = any(%s) and tsv_head @@ plainto_tsquery('simple', %s)", (ids, text))}
    for i in phrase:
        score[i] *= w['phrase_factor']
    for i in heading:
        score[i] *= w['heading_factor']
    return dict(score), phrase, heading


# ------------------------------------------------------------------ semantic
def semantic(conn, qvec, model, pool, keys):
    """{passage id: cosine distance} for the `pool` nearest passages. An exact scan:
    at tens of thousands of passages it takes well under a second."""
    v = '[' + ','.join(f'{x:.6g}' for x in qvec) + ']'
    rows = conn.execute(
        """select p.id, e.vec <=> %(v)s::halfvec d from src.passages p
           join cache.embeddings e on e.model = %(m)s and e.input_sha = p.embed_sha
           where (%(keys)s::text[] is null or p.doc_key = any(%(keys)s))
           order by d limit %(n)s""", dict(v=v, m=model, n=pool, keys=keys)).fetchall()
    return {i: float(d) for i, d in rows}


def has_vectors(conn, model):
    return conn.execute('select exists (select 1 from cache.embeddings where model = %s)', (model,)).fetchone()[0]


# -------------------------------------------------------------------- priors
def definition_matches(conn, pq, w, ids=None, keys=None):
    """{passage id: (match × confidence, the definition)} for passages defining the
    query's term (exact), or a narrower term containing it. A broader term gets
    nothing (weights.toml [defines])."""
    qn = pq['norm']
    if not qn:
        return {}
    rows = conn.execute(
        """select passage_id, term, norm, kind, conf, evidence, at_off from src.definitions
           where (norm = %(q)s or norm ~ ('(^| )' || %(re)s || '( |$)'))
             and (%(ids)s::bigint[] is null or passage_id = any(%(ids)s))
             and (%(keys)s::text[] is null or doc_key = any(%(keys)s))""",
        dict(q=qn, re=re.escape(qn), ids=ids, keys=keys)).fetchall()
    out = {}
    for pid, term, norm, kind, conf, ev, at in rows:
        m = (w['exact'] if norm == qn else w['narrower']) * conf
        if m > out.get(pid, (0,))[0]:
            out[pid] = (m, dict(term=term, kind=kind, conf=conf, evidence=ev, at=at, exact=norm == qn))
    return out


def _recency(conn):
    """{key: 0..1}, a document's place among its organisation's documents by year."""
    by = defaultdict(list)
    for key, org, year in conn.execute('select key, org, year from src.documents where has_text'):
        by[org or key].append((year or 0, key))
    out = {}
    for docs in by.values():
        years = sorted({y for y, _ in docs})
        for y, k in docs:
            out[k] = years.index(y) / (len(years) - 1) if len(years) > 1 else 0.5
    return out


# --------------------------------------------------------------------- search
def search(conn, query, n=10, model='bge-m3', fusion=None, keys=None, qvec=None, w=None):
    """[(passage row, score, explain)] best first, verbatim copies collapsed."""
    W = w or weights()
    pq = parse(query)
    fusion = fusion or W['fusion']['method']
    lex, phrase, heading = lexical(conn, pq, W['lexical'], keys)
    sem = {}
    if qvec is not None:
        sem = semantic(conn, qvec, model, W['fusion']['semantic_pool'], keys)
    defs = definition_matches(conn, pq, W['defines'], keys=keys)
    ids = set(lex) | set(sem) | set(defs)
    if not ids:
        return [], pq
    N = _stats(conn)['n']
    sem_rank = {i: r for r, i in enumerate(sorted(sem, key=lambda i: sem[i]), 1)}
    # lexical ties (all the zeros) broken by semantic distance
    lex_rank = {i: r for r, i in enumerate(sorted(lex, key=lambda i: (-lex[i], sem.get(i, 9))), 1)}
    rows = {r[0]: r for r in conn.execute(
        """select p.id, p.doc_key, p.ord, p.start_off, p.end_off, p.page, p.printed, p.page_last, p.section, p.path,
                  p.text, p.norm_sha, p.not_in_pdf, d.status, d.influence, d.title, d.code, d.fidelity_mark,
                  d.pages_to_check, d.active_key
           from src.passages p join src.documents d on d.key = p.doc_key where p.id = any(%s)""", (list(ids),))}
    rec = _recency(conn)
    k = W['fusion']['k']
    out = []
    for i in ids:
        if i not in rows:           # re-chunked by a concurrent bin/source-index run
            continue
        sr, lr = sem_rank.get(i, N + 1), lex_rank.get(i, N + 1)
        if fusion == 'mix':
            base = 1 / math.sqrt(sr * lr)
        elif fusion == 'lexical':
            base = lex.get(i, 0)
        elif fusion == 'semantic':
            base = 1 - sem.get(i, 2)
        else:
            base = (1 / (k + sr) if sem else 0) + 1 / (k + lr)
        r = rows[i]
        dm = defs.get(i)
        f_def = 1 + W['defines']['boost'] * dm[0] if dm else 1.0
        f_sec = W['section'].get(r[8], 1.0)
        f_status = W['status']['superseded'] if r[13] == 'superseded' else 1.0
        f_inf = W['influence'].get(r[14] or 'corpus', 1.0)
        f_rec = 1 + W['recency']['weight'] * rec.get(r[1], 0.5)
        score = base * f_def * f_sec * f_status * f_inf * f_rec
        out.append((r, score, dict(base=base, sem_rank=sr if i in sem_rank else None, lex_rank=lr if i in lex_rank else None,
                                   lexical=lex.get(i), distance=sem.get(i), phrase=i in phrase, heading=i in heading,
                                   defines=dm[1] if dm else None, f_def=f_def, f_section=f_sec, f_status=f_status,
                                   f_influence=f_inf, f_recency=round(f_rec, 3))))
    out.sort(key=lambda x: -x[1])
    # collapse verbatim copies: keep the best, list the others
    seen, results = {}, []
    for r, score, ex in out:
        h = r[11]
        if h in seen:
            seen[h][2].setdefault('copies', []).append((r[1], r[5]))
            continue
        seen[h] = (r, score, ex)
        results.append(seen[h])
    return results[:n], pq


# ------------------------------------------------------------------ definitions
def definitions(conn, query, keys=None, narrower=True):
    """Every definition of the term (and, if narrower, of terms containing it),
    grouped by document, active documents first."""
    pq = parse(query)
    qn = pq['norm']
    rows = conn.execute(
        """select d.doc_key, d.term, d.norm, d.kind, d.conf, d.evidence, d.at_off, d.page, d.printed,
                  p.start_off, p.end_off, doc.status, doc.influence, doc.title, doc.code, doc.year, doc.fidelity_mark,
                  doc.pages_to_check, doc.active_key
           from src.definitions d join src.passages p on p.id = d.passage_id join src.documents doc on doc.key = d.doc_key
           where (d.norm = %(q)s or (%(nar)s and d.norm ~ ('(^| )' || %(re)s || '( |$)')))
             and (%(keys)s::text[] is null or d.doc_key = any(%(keys)s))
           order by d.doc_key, d.at_off""", dict(q=qn, re=re.escape(qn), nar=narrower, keys=keys)).fetchall()
    seen, by = set(), defaultdict(list)
    for r in rows:
        if (r[0], r[6]) in seen:          # one definition in two overlapping pieces
            continue
        seen.add((r[0], r[6]))
        by[r[0]].append(r)
    rank = dict(anchor=0, major=1, supporting=2, context=3, corpus=4)
    order = sorted(by, key=lambda k: (by[k][0][11] != 'active', rank.get(by[k][0][12] or 'corpus', 5),
                                      -(by[k][0][15] or 0), k))
    return [(k, by[k]) for k in order], pq


# ------------------------------------------------------------------ concordance
def concordance_rows(conn, query, keys=None, exact=False):
    """Passages and headings holding a word form that contains the query (by
    substring, so "infohazard" and "biohazards" count for "hazard"), or, for a
    phrase, the words in order. With exact, the word or phrase itself only, as
    whole words: an acronym such as "AI" otherwise matches inside "rail" and
    "faith"."""
    pq = parse(query)
    ws = words(pq['term']) or words(query)
    if exact:
        pg = r'\m' + r'[^[:alnum:]]+'.join(re.escape(w) for w in ws) + r'\M'
        py = re.compile(r'(?<![^\W_])' + r'[\W_]+'.join(re.escape(w) for w in ws) + r'(?![^\W_])', re.I)
    elif len(ws) == 1:
        pg = r'[[:alnum:]]*' + re.escape(ws[0]) + r'[[:alnum:]]*'
        py = re.compile(r'[^\W_]*' + re.escape(ws[0]) + r'[^\W_]*', re.I)
    else:
        pg = r'\m' + r'[^[:alnum:]]+'.join(re.escape(w) for w in ws) + r'[[:alnum:]]*'
        py = re.compile(r'\b' + r'[\W_]+'.join(re.escape(w) for w in ws) + r'[^\W_]*', re.I)
    ps = conn.execute(
        """select p.id, p.doc_key, p.section, p.start_off, p.end_off, p.text from src.passages p
           where p.text ~* %(re)s and (%(keys)s::text[] is null or p.doc_key = any(%(keys)s))
           order by p.doc_key, p.start_off""", dict(re=pg, keys=keys)).fetchall()
    hs = conn.execute(
        """select h.doc_key, h.start_off, h.text, h.title, h.page, h.printed from src.headings h
           where (h.text || ' ' || coalesce(h.title, '')) ~* %(re)s and (%(keys)s::text[] is null or h.doc_key = any(%(keys)s))
           order by h.doc_key, h.start_off""", dict(re=pg, keys=keys)).fetchall()
    return pq, py, ps, hs
