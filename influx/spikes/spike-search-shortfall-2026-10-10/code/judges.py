#!/usr/bin/env python3
"""SB 53 has two blind judges (Claude, Gemini). Score today's pooled-Au5 hybrid ranking against each,
and ask: of the stretches one judge marked that the ranking misses, how many did the other judge mark at all?"""
import os, pickle, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import *  # noqa
T = pickle.load(open(os.path.join(SPIKE, 'runs', 'table.pkl'), 'rb'))['table']
KEY = 'california-2025-sb53'
conn = connect()
dirs = dict(claude=JUDG, gemini=os.path.join(REPO, 'search', 'eval', 'outline-judgments-gemini'))
J = {}
for name, d in dirs.items():
    import glob, json, shutil, tempfile
    tmp = tempfile.mkdtemp()
    shutil.copy(os.path.join(d, KEY + '.json'), tmp)
    g, keys = OC.judged_grades(tmp)
    C = OC.Corpus(conn, [KEY])
    J[name] = {q: [dict(it, ps=C.resolve(it)['ps']) for it in its] for q, its in g.items()}
def lines(it): return set(range(it['lines'][0], it['lines'][1] + 1))
for cut in (188,):
    for a, b in (('claude', 'gemini'), ('gemini', 'claude')):
        mx = fl = un_other = un_none = 0; must_un = 0
        for q in QUERIES:
            rows = T[q]['rows']; ko = {(r['key'], r['ord']): i for i, r in rows.items()}
            for it in J[a].get(q, []):
                g = 2 ** it['grade'] - 1; mx += g
                hr = [rows[ko[k]]['hrank'] for k in it['ps'] if rows[ko[k]]['hrank']]
                if hr and min(hr) <= cut: fl += g; continue
                other = any(lines(it) & lines(o) for o in J[b].get(q, []))
                if other: un_other += g
                else: un_none += g
        print(f'judge {a}: max {mx}, flagged {fl/mx:.3f}; unflagged {1-fl/mx:.3f} = also marked by {b} {un_other/mx:.3f} + marked by {a} alone {un_none/mx:.3f}')
