#!/usr/bin/env python3
"""Build the per-query, per-passage table: today's hybrid features and rank, full-scan cosine,
and the judges' labels. Writes runs/table.pkl (git-ignored size is small; kept for the other scripts).

A passage's label is the highest grade of any judged stretch it overlaps (0 if none).
"""
import math, os, pickle, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from common import *  # noqa
from srcsearch.text import words


def main():
    conn = connect()
    P = passages(conn)
    S, C = stretches(conn)
    ko2id = {(p['key'], p['ord']): i for i, p in P.items()}
    N = len(P)
    ids = sorted(P)
    M = np.stack([P[i]['vec'] for i in ids])
    table = {}
    for q in QUERIES:
        v = np.array(qvec(q), dtype=np.float32)
        v /= np.linalg.norm(v)
        cos = M @ v
        sem_full = {ids[j]: r + 1 for r, j in enumerate(np.argsort(-cos))}
        out, pq, by_sha = hybrid(conn, q, qvec(q))
        out = with_copies(P, out, by_sha)
        ranked = sorted((i for i in out if i in P), key=lambda i: -out[i][0])
        hrank = {i: r + 1 for r, i in enumerate(ranked)}
        label = {i: 0 for i in P}
        sids = {i: [] for i in P}
        for st in S.get(q, []):
            for ko in st['ps']:
                i = ko2id[ko]
                label[i] = max(label[i], st['grade'])
                sids[i].append(st['sid'])
        qw = set(pq['words'])
        rows = {}
        for j, i in enumerate(ids):
            p = P[i]
            pw = set(words(p['text']))
            s, ex = out.get(i, (None, {}))
            rows[i] = dict(id=i, key=p['key'], ord=p['ord'], section=p['section'], nwords=p['nwords'],
                           label=label[i], sids=sids[i], cos=float(cos[j]), sem_full=sem_full[i],
                           cand=i in out, hrank=hrank.get(i), score=s,
                           lexical=ex.get('lexical') or 0.0, lex_rank=ex.get('lex_rank'), sem_pool_rank=ex.get('sem_rank'),
                           phrase=bool(ex.get('phrase')), heading=bool(ex.get('heading')),
                           f_def=ex.get('f_def', 1.0), f_section=ex.get('f_section', 1.0),
                           proximity=ex.get('proximity'), base=ex.get('base'),
                           qwords_present=len(qw & pw), qwords_n=len(qw))
        table[q] = dict(rows=rows, stretches=S.get(q, []), pq=pq, N=N)
        print(f'{q[:50]:50} cands={len(out):5} judged stretches={len(S.get(q, [])):3} '
              f'relevant passages={sum(1 for r in rows.values() if r["label"]):4}')
    pickle.dump(dict(table=table, P={i: {k: v for k, v in p.items() if k != 'vec'} for i, p in P.items()}),
                open(os.path.join(SPIKE, 'runs', 'table.pkl'), 'wb'))


if __name__ == '__main__':
    main()
