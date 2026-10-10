#!/usr/bin/env python3
"""Flagged recall (gain-weighted 'reached') as a function of the cut, for today's hybrid and for
single-signal rankings, and where the unflagged stretches' best ranks sit."""
import os, pickle, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from common import SPIKE, QUERIES
T = pickle.load(open(os.path.join(SPIKE, 'runs', 'table.pkl'), 'rb'))['table']
N = 1872

def stretch_best(q, rankf):
    d = T[q]; rows = d['rows']; ko = {(r['key'], r['ord']): i for i, r in rows.items()}
    out = []
    for st in d['stretches']:
        rs = [rankf(rows[ko[k]]) for k in st['ps']]
        rs = [r for r in rs if r is not None]
        out.append((st['gain'], min(rs) if rs else N + 1, st['must']))
    return out

def recall(rankf, cut, must_only=False):
    num = den = 0
    for q in QUERIES:
        for g, r, m in stretch_best(q, rankf):
            if must_only and not m: continue
            den += g; num += g * (r <= cut)
    return num / den

R = dict(hybrid=lambda r: r['hrank'], semantic_full=lambda r: r['sem_full'], lexical=lambda r: r['lex_rank'])
cuts = [38, 94, 188, 282, 374, 562, 936, 1872]
print('gain-weighted share of judged stretches with a passage within the cut (cut as share of 1,872 Au5 passages)')
print(f'{"cut":>6} ' + ' '.join(f'{c:>6}' for c in cuts))
print(f'{"share":>6} ' + ' '.join(f'{c/N:>6.0%}' for c in cuts))
for name, f in R.items():
    print(f'{name[:14]:>14} ' + ' '.join(f'{recall(f, c):>6.3f}' for c in cuts))
print('must-read only:')
for name, f in R.items():
    print(f'{name[:14]:>14} ' + ' '.join(f'{recall(f, c, True):>6.3f}' for c in cuts))

# random baseline: expected recall if passages ranked at random
rng = np.random.default_rng(0)
vals = []
for t in range(50):
    perm = {}
    for q in QUERIES:
        ids = list(T[q]['rows']); rng.shuffle(ids)
        perm[q] = {i: k + 1 for k, i in enumerate(ids)}
    num = den = 0
    for q in QUERIES:
        d = T[q]; rows = d['rows']; ko = {(r['key'], r['ord']): i for i, r in rows.items()}
        for st in d['stretches']:
            b = min(perm[q][ko[k]] for k in st['ps'])
            den += st['gain']; num += st['gain'] * (b <= 188)
    vals.append(num / den)
print(f'random ranking, cut 188: {np.mean(vals):.3f}')
