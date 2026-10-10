#!/usr/bin/env python3
"""What blind query expansion recovers (an estimate of H-Q8's ceiling and of model-written rewrites).

Each expansion phrase e gets today's lexical scoring (rank.lexical over Au5) and a bge-m3 semantic
ranking (pool 400). They are fused with the query's own rankings in one RRF:

  s(p) = M(p) * [ 1/(k + sr_q) + 1/(k + lr_q) + (alpha/|E|) * sum_e (1/(k + sr_e) + 1/(k + lr_e)) ]

M(p) is today's multipliers. alpha = 1 means the expansions together weigh as much as the query.
One ranking, one fixed cut (188), so a longer list can't win by volume alone.
Lists: R (rephrasings), N (neighbours), R+N; and R without the phrasings CLAUDE.md quotes (the
expander flagged them as not strictly blind). The chemical/biological query has no expansion (left
out on purpose), so it scores as today in every row.
"""
import json, os, pickle, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
from rescore import *
import rescore
from common import connect, qvec, AU5
from srcsearch import rank

EXP = json.load(open(os.path.join(SPIKE, 'runs', 'blind-expansions.json')))['queries']
NOT_BLIND = {'reliably direct, modify, or shut down', 'death of, or serious injury to, more than 50 people',
             'more than one billion dollars in damage'}
CACHE = os.path.join(SPIKE, 'cache', 'phrase-qvec-bge-m3.json')
k = 60




def main():
    from srcsearch import embed
    conn = connect()
    W = rank.weights()['lexical']
    ids, V = (lambda z: (z['ids'], z['V']))(np.load(os.path.join(SPIKE, 'cache', 'bge-m3-full.npz')))
    try:
        cache = json.load(open(CACHE))
    except (OSError, ValueError):
        cache = {}
    lexc, semc = {}, {}
    phrases = {p for d in EXP.values() for p in d['rephrasings'] + d['neighbours']}
    for p in sorted(phrases):
        if p not in cache:
            cache[p] = embed.embed_query('bge-m3', p)
        v = np.array(cache[p], dtype=np.float32); v /= np.linalg.norm(v)
        s = V @ v
        order = np.argsort(-s)[:400]
        semc[p] = {int(ids[j]): n + 1 for n, j in enumerate(order)}
        lx, *_ = rank.lexical(conn, rank.parse(p), W, AU5)
        lexc[p] = {i: n + 1 for n, i in enumerate(sorted((i for i in lx if lx[i] > 0), key=lambda i: -lx[i]))}
    json.dump(cache, open(CACHE, 'w'))
    base_today = today()

    def run(lists, alpha, drop=frozenset()):
        S = {}
        for q in QUERIES:
            h = hybrid(q)                      # today's s(p), multipliers included
            E = [] if q not in EXP else [p for L in lists for p in EXP[q][L] if p not in drop]
            if not E:
                S[q] = h
                continue
            M = rescore._M[q]
            S[q] = {i: h[i] + M[i] * (alpha / len(E)) * sum(1 / (k + semc[e].get(i, NBIG)) + 1 / (k + lexc[e].get(i, NBIG))
                                                          for e in E) for i in h}
        return S

    print(f'today: flagged {flagged(base_today):.3f}, must {flagged(base_today, must_only=True):.3f}\n')
    rows = []
    for name, lists, drop in (('R', ['rephrasings'], frozenset()), ('R, blind only', ['rephrasings'], NOT_BLIND),
                              ('N', ['neighbours'], frozenset()), ('R+N', ['rephrasings', 'neighbours'], frozenset()),
                              ('R+N, blind only', ['rephrasings', 'neighbours'], NOT_BLIND)):
        for alpha in (0.5, 1.0, 2.0):
            S = run(lists, alpha, drop)
            d = boot(base_today, S)
            tot, pq = flagged(S, per_query=True)
            print(f'{name:16} alpha {alpha:<3}: flagged {tot:.3f} ({d[0]:+.3f}, {d[1]:+.3f} to {d[2]:+.3f})  '
                  f'must {flagged(S, must_only=True):.3f}')
            rows.append((name, alpha, pq))
    keep = {f'{n}|{a}': run(l, a, d) for n, l, d, a in (('R', ['rephrasings'], frozenset(), 2.0), ('N', ['neighbours'], frozenset(), 2.0),
                                                     ('R+N', ['rephrasings', 'neighbours'], frozenset(), 2.0),
                                                     ('R+N', ['rephrasings', 'neighbours'], frozenset(), 1.0))}
    pickle.dump(keep, open(os.path.join(SPIKE, 'runs', 'expansion-scores.pkl'), 'wb'))
    _, pq0 = flagged(base_today, per_query=True)
    print('\nper query, alpha 1 (today -> R / N / R+N):')
    sel = {(n, a): pq for n, a, pq in rows if a == 1.0}
    for q in QUERIES:
        print(f'  {q[:48]:48} {pq0[q]:.2f} -> {sel[("R", 1.0)][q]:.2f} / {sel[("N", 1.0)][q]:.2f} / {sel[("R+N", 1.0)][q]:.2f}')


if __name__ == '__main__':
    main()
