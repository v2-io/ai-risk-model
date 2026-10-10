"""Re-score today's hybrid with parts swapped, from the table (runs/table.pkl).

hybrid(q, sem=None, lex=None, pool=400): RRF(k=60) of a semantic ranking and a lexical ranking, times
today's multipliers (definition, section, document priors, proximity), as rank.search does.
- sem: {id: similarity} for all Au5 passages (default: today's full-scan bge-m3 cosine);
- pool: how many nearest count as semantic candidates (today 400 over the scope; None = all);
- lex: {id: lexical score} (default: today's), 0 or missing = no lexical hit.
Missing ranks get 1/(60 + 61,560), as today.

The multipliers come from the table: for a candidate, today's score / today's base; for a non-candidate,
its section weight times its document's priors (taken from any candidate of the same document).
"""
import math, os, pickle, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from common import SPIKE, QUERIES
from srcsearch import rank

T = pickle.load(open(os.path.join(SPIKE, 'runs', 'table.pkl'), 'rb'))['table']
W = rank.weights()
NBIG = 61560
CUT = 188


def multipliers(q):
    rows = T[q]['rows']
    docf = {}
    for r in rows.values():
        if r['cand'] and r['base']:
            m = r['score'] / r['base']
            # divide out the passage-level parts to get the document-level priors
            prox = 1 + W['lexical']['proximity_boost'] * r['proximity'] if r['proximity'] is not None else 1.0
            docf.setdefault(r['key'], m / (r['f_def'] * r['f_section'] * prox))
    out = {}
    for i, r in rows.items():
        if r['cand'] and r['base']:
            out[i] = r['score'] / r['base']
        else:
            out[i] = W['section'].get(r['section'], 1.0) * docf.get(r['key'], 1.0)
    return out


_M = {}


def hybrid(q, sem=None, lex=None, pool=400, k=60, mult=True, lex_weight=1.0, sem_weight=1.0):
    rows = T[q]['rows']
    if q not in _M:
        _M[q] = multipliers(q)
    M = _M[q]
    sem = sem or {i: r['cos'] for i, r in rows.items()}
    lex = lex if lex is not None else {i: r['lexical'] for i, r in rows.items()}
    sr = {i: n + 1 for n, i in enumerate(sorted(sem, key=lambda i: -sem[i]))}
    if pool:
        sr = {i: v for i, v in sr.items() if v <= pool}
    lr = {i: n + 1 for n, i in enumerate(sorted((i for i in lex if lex[i] > 0), key=lambda i: (-lex[i], -sem.get(i, 0))))}
    out = {}
    for i in rows:
        b = sem_weight / (k + sr.get(i, NBIG)) + lex_weight / (k + lr.get(i, NBIG))
        out[i] = b * (M[i] if mult else 1.0)
    return out


def flagged(scores_by_q, cut=CUT, must_only=False, per_query=False):
    num = den = 0
    pq = {}
    for q in scores_by_q:
        s = scores_by_q[q]
        rows = T[q]['rows']
        rk = {i: n + 1 for n, i in enumerate(sorted(rows, key=lambda i: -s[i]))}
        ko = {(r['key'], r['ord']): i for i, r in rows.items()}
        a = b = 0
        for st in T[q]['stretches']:
            if must_only and not st['must']:
                continue
            best = min(rk[ko[k]] for k in st['ps'])
            a += st['gain'] * (best <= cut)
            b += st['gain']
        num += a
        den += b
        pq[q] = a / b if b else None
    return (num / den, pq) if per_query else num / den


def boot(scores_a, scores_b, n=2000, cut=CUT, seed=0):
    """Paired bootstrap over queries of flagged(b) - flagged(a): (mean diff, 2.5%, 97.5%)."""
    rng = np.random.default_rng(seed)
    qs = list(scores_a)
    per = {}
    for name, S in (('a', scores_a), ('b', scores_b)):
        for q in qs:
            s = S[q]
            rows = T[q]['rows']
            rk = {i: m + 1 for m, i in enumerate(sorted(rows, key=lambda i: -s[i]))}
            ko = {(r['key'], r['ord']): i for i, r in rows.items()}
            num = sum(st['gain'] * (min(rk[ko[k]] for k in st['ps']) <= cut) for st in T[q]['stretches'])
            den = sum(st['gain'] for st in T[q]['stretches'])
            per[(name, q)] = (num, den)
    diffs = []
    for _ in range(n):
        smp = rng.choice(qs, len(qs))
        na = sum(per[('a', q)][0] for q in smp); da = sum(per[('a', q)][1] for q in smp)
        nb = sum(per[('b', q)][0] for q in smp); db = sum(per[('b', q)][1] for q in smp)
        diffs.append(nb / db - na / da)
    point = flagged(scores_b, cut) - flagged(scores_a, cut)
    return point, np.percentile(diffs, 2.5), np.percentile(diffs, 97.5)


def today():
    return {q: {i: (r['score'] if r['score'] else 0.0) for i, r in T[q]['rows'].items()} for q in QUERIES}
