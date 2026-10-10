#!/usr/bin/env python3
"""Run search/eval/outline-check's own scoring (pooled Au5, budgets 60/120/200) with rank.search's
scores replaced by a remedy's, in this process only. Both the outline and the list baselines then use
the new ranking. Rows and explain fields come from today's rank.search; passages it didn't return
(non-candidates) are added with empty explain.

usage: outline_with.py today | exp | tags | exp+tags
"""
import os, pickle, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import OC, rank, connect, AU5, SPIKE
from rescore import today, QUERIES, T

which = sys.argv[1]
S = pickle.load(open(os.path.join(SPIKE, 'runs', 'tags-scores.pkl'), 'rb'))
E = pickle.load(open(os.path.join(SPIKE, 'runs', 'expansion-scores.pkl'), 'rb'))
SC = dict(today=today(), exp=E['R+N|2.0'], tags=S['tags-both|1.0'], **{'exp+tags': S['exp+tags+exp-on-tags b1.0|1.0']})[which]
orig = rank.search


def patched(conn, query, n=10, model='bge-m3', fusion=None, keys=None, qvec=None, w=None):
    if query not in SC or sorted(keys or []) != sorted(AU5):
        return orig(conn, query, n=n, model=model, fusion=fusion, keys=keys, qvec=qvec, w=w)
    res, pq = orig(conn, query, n=10 ** 9, model=model, keys=keys, qvec=qvec, w=w)
    have = {r[0]: (r, ex) for r, _s, ex in res}
    sc = SC[query]
    rows = rank.details(conn, [i for i in sc if i not in have])
    out = []
    seen = set()
    for i in sorted(sc, key=lambda i: -sc[i]):
        r, ex = have.get(i, (rows.get(i), {}))
        if r is None or r[11] in seen:        # verbatim copies collapsed, as rank.search does
            continue
        seen.add(r[11])
        out.append((r, sc[i], ex))
    return out[:n], pq


rank.search = patched
conn = connect()
grades, keys = OC.judged_grades(OC.os.path.join(OC.REPO, 'search', 'eval', 'outline-judgments'))
C = OC.Corpus(conn, keys)
tot = OC.score_scope(conn, C, grades, keys, [60, 120, 200], 'bge-m3', False, None)
OC.print_table(tot, [60, 120, 200], f'pooled, ranking = {which}')
