"""Shared loading for the shortfall spike. Reads search/ code and the database; writes nothing there.

- judged stretches, resolved to passages exactly as search/eval/outline-check resolves them;
- every Au5 passage with its text, section, path and bge-m3 vector (from cache.embeddings);
- per query, today's hybrid explain fields for every candidate (rank.search over Au5).
"""
import importlib.machinery, importlib.util, json, os, sys

sys.dont_write_bytecode = True
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'search'))
sys.path.insert(0, os.path.join(REPO, 'bin'))
import numpy as np  # noqa: E402
from srcsearch import db, rank, outline  # noqa: E402

SPIKE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
JUDG = os.path.join(REPO, 'search', 'eval', 'outline-judgments')
AU5 = ['bengio-2026-international', 'eu-cop-2025-safety-security', 'california-2025-sb53',
       'anthropic-2026-risk-report-aug', 'aisi-2025-frontier']
QUERIES = [l.strip() for l in open(os.path.join(REPO, 'search', 'eval', 'outline-queries.txt')) if l.strip()]


def _load_check():
    path = os.path.join(REPO, 'search', 'eval', 'outline-check')
    loader = importlib.machinery.SourceFileLoader('outline_check', path)
    spec = importlib.util.spec_from_loader('outline_check', loader)
    m = importlib.util.module_from_spec(spec)
    loader.exec_module(m)
    return m


OC = _load_check()


def connect():
    return db.connect()


def passages(conn):
    """{id: dict} for every Au5 passage, with its bge-m3 vector as a unit numpy array."""
    rows = conn.execute(
        """select p.id, p.doc_key, p.ord, p.start_off, p.end_off, p.section, p.path, p.heading, p.text, p.nwords, p.norm_sha,
                  e.vec::text
           from src.passages p left join cache.embeddings e on e.model = 'bge-m3' and e.input_sha = p.embed_sha
           where p.doc_key = any(%s) and p.layer = 'canonical' order by p.doc_key, p.ord""", (AU5,)).fetchall()
    out = {}
    for i, k, o, s, e, sec, path, head, text, nw, sha, vec in rows:
        v = np.array(json.loads(vec), dtype=np.float32) if vec else None
        if v is not None:
            v /= np.linalg.norm(v)
        out[i] = dict(id=i, key=k, ord=o, start=s, end=e, section=sec, path=list(path or ()), heading=head,
                      text=text, nwords=nw, norm_sha=sha, vec=v)
    return out


def stretches(conn):
    """{query: [stretch]} with each stretch's gain, grade, key, lines, quote, and passage (key, ord) set."""
    grades, keys = OC.judged_grades(JUDG)
    C = OC.Corpus(conn, keys)
    out = {}
    for q, items in grades.items():
        for n, it in enumerate(items):
            s = C.resolve(it)
            if not s or not s['ps']:
                continue
            out.setdefault(q, []).append(dict(sid=f"{q[:12]}|{it['key'][:8]}|{n}", key=it['key'], grade=it['grade'],
                                              gain=2 ** it['grade'] - 1, must=it['grade'] >= 2,
                                              lines=it['lines'], quote=it.get('quote', ''), note=it.get('note', ''),
                                              ps=sorted(s['ps']), size=s['size'], lo=s['lo'], hi=s['hi']))
    return out, C


def qvec(query, model='bge-m3'):
    return OC.qvec(model, query)


def hybrid(conn, query, v):
    """{passage id: (score, explain)} for every candidate, from today's rank.search over Au5.
    Verbatim copies collapsed by rank.search get their original's score, as outline._score does."""
    res, pq = rank.search(conn, query, n=10 ** 9, keys=AU5, qvec=v)
    out, by_sha = {}, {}
    for r, s, ex in res:
        out[r[0]] = (s, ex)
        by_sha.setdefault(r[11], (s, ex))
    return out, pq, by_sha


def with_copies(P, out, by_sha):
    for i, p in P.items():
        if i not in out and p['norm_sha'] in by_sha:
            s, ex = by_sha[p['norm_sha']]
            out[i] = (s, dict(ex, copy_of=True))
    return out
