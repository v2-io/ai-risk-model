#!/usr/bin/env python3
"""For each unflagged stretch (cut 188), structural relations to flagged passages:
  sect   a passage with the same heading path (same outline node) is flagged
  adj    a passage within 2 positions in the document is flagged
  dup    a passage with bge-m3 cosine >= 0.92 to one of the stretch's passages is flagged (near-copies)
  parent a passage under the parent heading (path minus its last element) is flagged
Gain-weighted shares of all judged gain, so they compare with the 0.248 unflagged."""
import os, pickle, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from common import SPIKE, QUERIES
z = np.load(os.path.join(SPIKE, 'cache', 'bge-m3-full.npz')); ids = [int(i) for i in z['ids']]; V = z['V']; pos = {i: n for n, i in enumerate(ids)}
D = pickle.load(open(os.path.join(SPIKE, 'runs', 'table.pkl'), 'rb')); T, P = D['table'], D['P']
CUT = 188
tot = 0; acc = dict(un=0, sect=0, adj=0, dup=0, parent=0, any=0, none=0)
per = []
for q in QUERIES:
    rows = T[q]['rows']; ko = {(r['key'], r['ord']): i for i, r in rows.items()}
    fl = {i for i, r in rows.items() if r['hrank'] and r['hrank'] <= CUT}
    flv = V[[pos[i] for i in fl]]
    for st in T[q]['stretches']:
        g = st['gain']; tot += g
        S = [ko[k] for k in st['ps']]
        if S and set(S) & fl: continue
        acc['un'] += g
        sect = any(tuple(P[j]['path']) == tuple(P[i]['path']) and P[j]['key'] == P[i]['key'] for i in S for j in fl)
        parent = any(P[j]['key'] == P[i]['key'] and len(P[i]['path']) > 0 and tuple(P[j]['path'][:len(P[i]['path']) - 1]) == tuple(P[i]['path'][:-1]) for i in S for j in fl)
        adj = any(P[j]['key'] == P[i]['key'] and abs(P[j]['ord'] - P[i]['ord']) <= 2 for i in S for j in fl)
        dup = bool(len(fl)) and float((V[[pos[i] for i in S]] @ flv.T).max()) >= 0.92
        for k, v in dict(sect=sect, adj=adj, dup=dup, parent=parent).items(): acc[k] += g * v
        a = sect or adj or dup
        acc['any'] += g * a; acc['none'] += g * (not a)
        per.append((q, st['sid'], st['grade'], sect, adj, dup, parent))
print(f'total judged gain {tot}; unflagged {acc["un"]/tot:.3f}')
for k in ('sect', 'parent', 'adj', 'dup', 'any', 'none'):
    print(f'  {k:7} {acc[k]/tot:.3f} of all  ({acc[k]/acc["un"]:.0%} of unflagged)')
pickle.dump(per, open(os.path.join(SPIKE, 'runs', 'structure.pkl'), 'wb'))
