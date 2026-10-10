#!/usr/bin/env python3
"""Which categories of unflagged stretch (runs/classification.tsv) each remedy recovers at cut 188,
and what it costs: stretches flagged today that it loses."""
import os, pickle, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
from rescore import *
C = dict(l.rstrip('\n').split('\t') for l in open(os.path.join(SPIKE, 'runs', 'classification.tsv')) if not l.startswith(('#', 'sid')))
def status(S):
    out = {}
    for q in QUERIES:
        rows = T[q]['rows']; s = S[q]
        rk = {i: n + 1 for n, i in enumerate(sorted(rows, key=lambda i: -s[i]))}
        ko = {(r['key'], r['ord']): i for i, r in rows.items()}
        for st in T[q]['stretches']:
            out[st['sid']] = (min(rk[ko[k]] for k in st['ps']) <= CUT, st['gain'], q)
    return out
base = status(today())
def report(name, S):
    st = status(S); won = collections.Counter(); lost = 0
    for sid, (f, g, q) in st.items():
        f0 = base[sid][0]
        if f and not f0: won[C.get(sid, 'BIO' if q.startswith('chemical') else '?')] += g
        if f0 and not f: lost += g
    tot = sum(g for _, g, _ in st.values())
    print(f'{name:28} won ' + ', '.join(f'{c} {g}' for c, g in won.most_common()) + f'  | lost {lost}  | net {(sum(won.values()) - lost) / tot:+.3f}')
if __name__ == '__main__':
    E = pickle.load(open(os.path.join(SPIKE, 'runs', 'expansion-scores.pkl'), 'rb'))
    for k, S in E.items():
        report('expansion ' + k, S)
    import emb_variants as ev
    for m in ('embeddinggemma:300m', 'snowflake-arctic-embed2'):
        from reembed import call, MODELS
        Sm = ev.sims(m, 'full', lambda q, m=m: call(m, [MODELS[m][0] + q])[0])
        report('embedder ' + m, {q: hybrid(q, sem=Sm[q]) for q in QUERIES})
        call(m, ['x'], keep=0)
