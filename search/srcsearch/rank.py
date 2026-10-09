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

Every ranking factor is a hypothesis about relevance, registered in
search/RANKING.md with its impetus, its encoding, how it is checked and its
status. A factor without a register entry doesn't belong here. When a result
looks wrong, find which hypothesis's term is mis-specified (--explain) and test
that hypothesis; don't add a special case (Joseph, 2026-10-09: "it becomes
spaghetti really quickly"). RANKING.md §3 proposes replacing the fusion and
multipliers below with one log-odds model; until then this is the model in use.
"""
import math, os, re, tomllib
from collections import defaultdict

from . import SEARCH, match
from .text import fold, norm_term, sentences, words
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


def _forms(conn, word, w, keys):
    """{passage id: BM25} for a query word's longer forms (DESIGN §6.2, §7.1): the
    forms `lexical` would match ("hazards", "hazardous"; "capabilities" for
    "capability"), the word itself excluded, scored as one term. They stand in for
    Postgres's stems, which also merge words that share only a stem ("developer",
    "development") and hide which form matched."""
    if len(word) < 2 or not re.fullmatch(r"[a-z0-9]+", word):
        return {}
    if len(word) > 2 and word[-1] == 'e':
        stem, rx = word[:-1], re.escape(word[:-1]) + '(e|(?=[ie]))'
    elif len(word) > 2 and word[-1] == 'y' and word[-2] not in 'aeiouy':
        stem, rx = word[:-1], re.escape(word[:-1]) + '(y|ie)'
    else:
        stem, rx = word, re.escape(word)
    rx = '^' + rx + '[a-z]{0,%d}$' % match.CAP
    st = _stats(conn)
    rows = conn.execute(
        """select p.id, p.nwords, sum(coalesce(array_length(x.positions, 1), 1)) tf
           from src.passages p, unnest(p.tsv_exact) x
           where p.tsv_exact @@ to_tsquery('simple', %(pre)s) and x.lexeme ~ %(rx)s and x.lexeme <> %(w)s
             and (%(keys)s::text[] is null or p.doc_key = any(%(keys)s))
           group by p.id, p.nwords""", dict(pre=stem + ':*', rx=rx, w=word, keys=keys)).fetchall()
    if not rows:
        return {}
    # df over the whole corpus, as for the other terms, not just the scope
    n = len(rows) if keys is None else conn.execute(
        """select count(distinct p.id) from src.passages p, unnest(p.tsv_exact) x
           where p.tsv_exact @@ to_tsquery('simple', %s) and x.lexeme ~ %s and x.lexeme <> %s""",
        (stem + ':*', rx, word)).fetchone()[0]
    idf = math.log(1 + (st['n'] - n + 0.5) / (n + 0.5))
    k1, b = w['k1'], w['b']
    return {i: idf * tf * (k1 + 1) / (tf + k1 * (1 - b + b * nw / st['avg'])) for i, nw, tf in rows}


_TOK = re.compile(r"[^\W_]+")


def _positions(text):
    """[(word, sentence, paragraph)] for proximity: memorata's _tokenize_positions,
    with this index's sentence splitter."""
    out = []
    for p_i, para in enumerate(text.split('\n\n')):
        for s_i, (a, b) in enumerate(sentences(para)):
            for m in _TOK.finditer(para[a:b]):
                out.append((m.group(0).lower(), (p_i, s_i), p_i))
    return out


def proximity_density(text, terms, form_rx):
    """(proximity or None, density), ported from memorata (memorata3/search.py
    proximity_score and keyword_density, read 2026-10-09), with a word's longer forms
    taken from the literal matcher instead of a bare prefix:
    - proximity, in [0,1], or None for a one-word query or a passage holding fewer
      than two of the query's words: coverage × exactness × (0.4 + 0.6 × closeness),
      where a longer form counts 0.55 as exact, and closeness is 1 − 0.03 per extra
      word in the tightest window − 0.25 per sentence − 0.6 per paragraph it spans,
      × 0.75 out of the query's order;
    - density, in [0,1]: half a saturating count (log, 8 = full) and half the rate
      (one word in ten = full)."""
    toks = _positions(text)
    if not toks or not terms:
        return None, 0.0
    pos = {i: [] for i in range(len(terms))}
    hits = 0
    for wi, (wd, s, p) in enumerate(toks):
        hit = False
        for ti, t in enumerate(terms):
            if wd == t:
                pos[ti].append((wi, s, p, True)); hit = True
            elif form_rx[ti] is not None and form_rx[ti].fullmatch(wd):
                pos[ti].append((wi, s, p, False)); hit = True
        hits += hit
    count_sig = math.log(1 + hits) / math.log(1 + 8)
    rate_sig = (hits / len(toks)) / 0.10
    density = min(1.0, 0.5 * min(1.0, count_sig) + 0.5 * min(1.0, rate_sig)) if hits else 0.0
    present = [ti for ti in pos if pos[ti]]
    if len(terms) < 2 or len(present) < 2:
        return None, round(density, 4)
    coverage = len(present) / len(terms)
    exactness = sum(1.0 if any(e for *_, e in pos[ti]) else 0.55 for ti in present) / len(present)
    rarest = min(present, key=lambda ti: len(pos[ti]))
    best = 0.0
    for anchor_ in pos[rarest]:
        chosen = [(ti, min(pos[ti], key=lambda x: abs(x[0] - anchor_[0]))) for ti in present]
        idx = [c[1][0] for c in chosen]
        span = max(idx) - min(idx)
        sents, paras = len({c[1][1] for c in chosen}), len({c[1][2] for c in chosen})
        order = [ti for ti, _ in sorted(chosen, key=lambda c: c[1][0])]
        gap = max(0, span - (len(present) - 1))
        prox = max(0.0, 1.0 - (0.03 * gap + 0.25 * (sents - 1) + 0.6 * (paras - 1)))
        best = max(best, prox * (1.0 if order == present else 0.75))
    return round(coverage * exactness * (0.4 + 0.6 * best), 4), round(density, 4)


def _form_rx(word):
    if len(word) < 2 or word in match.FUNCTION_WORDS:
        return None
    return re.compile(match.word_rx(match.Term(word), 'loose').replace(f'(?<!{match.WORD_CH})', '').replace(
        f'(?!{match.WORD_CH})', ''))


def lexical(conn, pq, w, keys):
    """{passage id: lexical score}, the phrase hits, the heading hits, and each scored
    passage's (proximity, density). The score is BM25 on exact word forms, plus a
    second leg at lower weight (DESIGN §6.2): Postgres's English stems, or, with
    `forms_weight`, each word's longer forms; then the phrase, heading, proximity
    and density factors."""
    text = ' '.join(pq['words'])
    exact = _bm25(conn, 'tsv_exact', 'simple', _lexemes(conn, 'simple', text), w, keys)
    score = defaultdict(float)
    for i, s in exact.items():
        score[i] += s
    if w.get('forms_weight'):
        for word in dict.fromkeys(pq['words']):
            for i, s in _forms(conn, word, w, keys).items():
                score[i] += w['forms_weight'] * s
    if w.get('stem_weight'):
        stem = _bm25(conn, 'tsv_stem', 'english', _lexemes(conn, 'english', text), w, keys)
        for i, s in stem.items():
            score[i] += w['stem_weight'] * s
    if not score:
        return {}, set(), set(), {}
    ids = list(score)
    phrase, heading = set(), set()
    if w.get('phrase') in ('literal', 'forms'):
        # the query's own words, function words included ("loss of control"), by the
        # literal matcher: Joseph's case rule, word boundaries, any separators; with
        # 'forms', each word may also take its longer forms ("information hazards")
        term = pq['term']
        mode = 'loose-phrase' if w['phrase'] == 'forms' else 'phrase'
        if len(match.terms(term, mode)) > 1:
            pats = match.prefilter(term, mode)
            where = ' and '.join(['text ~* %s'] * len(pats))
            for i, t in conn.execute(f"select id, text from src.passages where id = any(%s) and {where}", (ids, *pats)):
                if match.finditer(term, mode, t):
                    phrase.add(i)
    elif len(pq['words']) > 1:
        phrase = {r[0] for r in conn.execute(
            "select id from src.passages where id = any(%s) and tsv_exact @@ phraseto_tsquery('simple', %s)",
            (ids, text))}
    heading = {r[0] for r in conn.execute(
        "select id from src.passages where id = any(%s) and tsv_head @@ plainto_tsquery('simple', %s)", (ids, text))}
    for i in phrase:
        score[i] *= w['phrase_factor']
    for i in heading:
        score[i] *= w['heading_factor']
    sig = {}
    pb, db_ = w.get('proximity_boost', 0), w.get('density_boost', 0)
    if pb or db_:
        # only the head of the lexical ranking: past a few hundred, RRF's 1/(k + rank)
        # barely moves, and reading every passage holding "risk" would cost seconds
        head = sorted(score, key=lambda i: -score[i])[:w.get('signal_pool', 500)]
        terms = list(dict.fromkeys(pq['words']))
        frx = [_form_rx(t) for t in terms]
        for i, t in conn.execute("select id, text from src.passages where id = any(%s)", (head,)):
            sig[i] = proximity_density(t, terms, frx)
        if w.get('signals', 'lexical') == 'lexical':
            for i, (pr, de) in sig.items():
                score[i] *= (1 + pb * pr if pr is not None else 1.0) * (1 + db_ * de)
    return dict(score), phrase, heading, sig


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


def answerability(conn, query, qvec, model='bge-m3', keys=None, w=None):
    """Whether anything in scope seems to answer the query (a cue, not a gate; see
    weights.toml [answerable]): the nearest passage's cosine distance, how many
    passages hold all the query's content words, and `likely_unanswered` when none
    do and the nearest passage is at least the threshold away."""
    W = (w or weights())['answerable']
    pq = parse(query)
    near = None
    if qvec is not None:
        v = '[' + ','.join(f'{x:.6g}' for x in qvec) + ']'
        near = conn.execute(
            """select min(e.vec <=> %(v)s::halfvec) from src.passages p
               join cache.embeddings e on e.model = %(m)s and e.input_sha = p.embed_sha
               where (%(keys)s::text[] is null or p.doc_key = any(%(keys)s))""", dict(v=v, m=model, keys=keys)).fetchone()[0]
    n_all = conn.execute(
        """select count(*) from src.passages where tsv_exact @@ plainto_tsquery('simple', %s)
           and (%s::text[] is null or doc_key = any(%s))""", (' '.join(pq['words']), keys, keys)).fetchone()[0] if pq['words'] else 0
    unanswered = near is not None and n_all == 0 and near >= W['distance']
    return dict(nearest_distance=None if near is None else round(float(near), 4), passages_with_all_words=n_all,
                likely_unanswered=unanswered, threshold=W['distance'])


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
ROW_SQL = """select p.id, p.doc_key, p.ord, p.start_off, p.end_off, p.page, p.printed, p.page_last, p.section, p.path,
                    p.text, p.norm_sha, p.not_in_pdf, d.status, d.influence, d.title, d.code, d.fidelity_mark,
                    d.pages_to_check, d.active_key
             from src.passages p join src.documents d on d.key = p.doc_key where p.id = any(%s)"""


def details(conn, ids):
    """{passage id: row} for ids, in the row shape search() returns."""
    return {r[0]: r for r in conn.execute(ROW_SQL, (list(ids),))}


def _collapse(out, n):
    """Verbatim copies shown once, with where else they occur (§6.3)."""
    seen, results = {}, []
    for r, score, ex in out:
        h = r[11]
        if h in seen:
            seen[h][2].setdefault('copies', []).append((r[1], r[5]))
            continue
        seen[h] = (r, score, ex)
        results.append(seen[h])
    return results[:n]


def semantic_search(conn, query, qvec, n=10, model='bge-m3', keys=None, exclude=None):
    """[(passage row, score, explain)] by cosine similarity alone (DESIGN §7: the
    `semantic` verb): the whole corpus, none of the weights, verbatim copies
    collapsed. exclude(text) -> bool drops a passage (`--without-phrase`). Score is
    1 - cosine distance."""
    pq = parse(query)
    v = '[' + ','.join(f'{x:.6g}' for x in qvec) + ']'
    out, offset, batch = [], 0, max(4 * n, 200)
    while True:
        hits = conn.execute(
            """select p.id, e.vec <=> %(v)s::halfvec d from src.passages p
               join cache.embeddings e on e.model = %(m)s and e.input_sha = p.embed_sha
               where (%(keys)s::text[] is null or p.doc_key = any(%(keys)s))
               order by d limit %(n)s offset %(o)s""", dict(v=v, m=model, n=batch, o=offset, keys=keys)).fetchall()
        if not hits:
            break
        rows = details(conn, [i for i, _ in hits])
        for i, d in hits:
            r = rows.get(i)
            if r is None or (exclude and exclude(r)):
                continue
            out.append((r, 1 - float(d), dict(distance=float(d))))
        if len({r[11] for r, _, _ in out}) >= n:      # enough once copies are collapsed
            break
        offset += batch
    for k, (r, score, ex) in enumerate(out, 1):
        ex['sem_rank'] = k
    return _collapse(out, n), pq


def search(conn, query, n=10, model='bge-m3', fusion=None, keys=None, qvec=None, w=None):
    """[(passage row, score, explain)] best first, verbatim copies collapsed."""
    W = w or weights()
    pq = parse(query)
    fusion = fusion or W['fusion']['method']
    lex, phrase, heading, sig = lexical(conn, pq, W['lexical'], keys)
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
    rows = details(conn, ids)
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
        pr, de = sig.get(i, (None, 0.0))
        f_sig = 1.0
        if W['lexical'].get('signals') == 'post':
            f_sig = (1 + W['lexical'].get('proximity_boost', 0) * pr if pr is not None else 1.0) * \
                    (1 + W['lexical'].get('density_boost', 0) * de)
        score = base * f_def * f_sec * f_status * f_inf * f_rec * f_sig
        out.append((r, score, dict(base=base, sem_rank=sr if i in sem_rank else None, lex_rank=lr if i in lex_rank else None,
                                   lexical=lex.get(i), distance=sem.get(i), phrase=i in phrase, heading=i in heading,
                                   defines=dm[1] if dm else None, f_def=f_def, f_section=f_sec, f_status=f_status,
                                   f_influence=f_inf, f_recency=round(f_rec, 3), proximity=pr, density=de,
                                   f_signals=round(f_sig, 3))))
    out.sort(key=lambda x: -x[1])
    return _collapse(out, n), pq


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
def literal_patterns(term):
    """A literal search term as (Postgres ARE, Python regex), by Joseph's convention
    (2026-10-09): a lowercase letter matches either case and an uppercase letter only
    itself; words have implicit boundaries, and a '*' matches any letters or digits,
    so it removes the boundary on its side. 'ai' finds "AI" and "ai" but not "rail";
    'AI' finds only "AI"; '*ai*' finds "rail"; 'hazard*' finds "hazards" and
    "hazardous"; '*hazard' finds "infohazard". The words of a phrase are separated by
    any run of non-alphanumerics (spaces, line breaks, hyphens)."""
    pg_toks, py_toks = [], []
    for tok in term.split():
        pg, py = [], []
        for c in tok:
            if c == '*':
                pg.append('[[:alnum:]]*')
                py.append(r'[^\W_]*')
            elif c.islower() and len(c.upper()) == 1 and c.upper() != c:
                pg.append(f'[{c}{c.upper()}]')
                py.append(f'[{c}{c.upper()}]')
            else:
                pg.append(re.escape(c))
                py.append(re.escape(c))
        pg_toks.append(''.join(pg))
        py_toks.append(''.join(py))
    pg = '[^[:alnum:]]+'.join(pg_toks)
    py = r'[\W_]+'.join(py_toks)
    t = term.strip()
    if not t.startswith('*'):
        pg, py = '(?<![[:alnum:]])' + pg, r'(?<![^\W_])' + py
    if not t.endswith('*'):
        pg, py = pg + '(?![[:alnum:]])', py + r'(?![^\W_])'
    return pg, re.compile(py)


def wildcard_term(term):
    """The term with a '*' on each side that has a boundary: what it would match
    with no boundaries at all."""
    t = term.strip()
    return ('' if t.startswith('*') else '*') + t + ('' if t.endswith('*') else '*')


def concordance_rows(conn, query, keys=None, term=None):
    """Passages and headings holding the term, matched literally by
    literal_patterns' convention."""
    pq = parse(query)
    term = term or pq['term']
    pg, py = literal_patterns(term)
    ps = conn.execute(
        """select p.id, p.doc_key, p.section, p.start_off, p.end_off, p.text from src.passages p
           where p.text ~ %(re)s and (%(keys)s::text[] is null or p.doc_key = any(%(keys)s))
           order by p.doc_key, p.start_off""", dict(re=pg, keys=keys)).fetchall()
    hs = conn.execute(
        """select h.doc_key, h.start_off, h.text, h.title, h.page, h.printed from src.headings h
           where (h.text || ' ' || coalesce(h.title, '')) ~ %(re)s and (%(keys)s::text[] is null or h.doc_key = any(%(keys)s))
           order by h.doc_key, h.start_off""", dict(re=pg, keys=keys)).fetchall()
    return pq, py, ps, hs
