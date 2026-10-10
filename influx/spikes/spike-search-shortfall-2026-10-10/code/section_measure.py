#!/usr/bin/env python3
"""Flagged at three granularities, for today's ranking and for a random one:
  passage  a passage of the stretch is in the top 188 (outline-check's 'flagged')
  near     ... or a passage within 2 positions of it is
  section  ... or a passage with the same heading path is
The random baseline says how much each widening gives for free."""
import os, pickle, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from common import SPIKE, QUERIES
D = pickle.load(open(os.path.join(SPIKE, 'runs', 'table.pkl'), 'rb')); T, P = D['table'], D['P']
def measure(rank_of, cut=188):
    out = dict(passage=[0, 0], near=[0, 0], section=[0, 0])
    for q in QUERIES:
        rows = T[q]['rows']; ko = {(r['key'], r['ord']): i for i, r in rows.items()}
        fl = {i for i in rows if rank_of[q].get(i, 10**9) <= cut}
        flsec = {(P[j]['key'], tuple(P[j]['path'])) for j in fl}
        flpos = {(P[j]['key'], P[j]['ord']) for j in fl}
        for st in T[q]['stretches']:
            S = [ko[k] for k in st['ps']]; g = st['gain']
            a = bool(set(S) & fl)
            b = a or any((P[i]['key'], P[i]['ord'] + d) in flpos for i in S for d in (-2, -1, 1, 2))
            c = a or any((P[i]['key'], tuple(P[i]['path'])) in flsec for i in S)
            for k, v in (('passage', a), ('near', b), ('section', c)):
                out[k][0] += g * v; out[k][1] += g
    return {k: v[0] / v[1] for k, v in out.items()}
today = {q: {i: r['hrank'] for i, r in T[q]['rows'].items() if r['hrank']} for q in QUERIES}
print('today ', {k: round(v, 3) for k, v in measure(today).items()})
rng = np.random.default_rng(1); acc = []
for t in range(30):
    rr = {}
    for q in QUERIES:
        ids = list(T[q]['rows']); rng.shuffle(ids); rr[q] = {i: n + 1 for n, i in enumerate(ids)}
    acc.append(measure(rr))
print('random', {k: round(np.mean([a[k] for a in acc]), 3) for k in acc[0]})
