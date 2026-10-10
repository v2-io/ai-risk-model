#!/usr/bin/env python3
"""Embedding-input variants (title+path+text as today, path+text, text alone), bge-m3, over Au5:
semantic-only flagged@188 and AUC, and hybrid with the variant's cosine swapped in."""
import os, sys
import numpy as np
from sklearn.metrics import roc_auc_score
sys.path.insert(0, os.path.dirname(__file__))
from rescore import *
from common import qvec

def load(model, v):
    z = np.load(os.path.join(SPIKE, 'cache', f'{model.replace(":", "_")}-{v}.npz'))
    return z['ids'], z['V']

def sims(model, v, qv_of):
    ids, V = load(model, v)
    out = {}
    for q in QUERIES:
        qv = np.array(qv_of(q), dtype=np.float32); qv /= np.linalg.norm(qv)
        s = V @ qv
        out[q] = {int(i): float(x) for i, x in zip(ids, s)}
    return out

def auc(S):
    return np.mean([roc_auc_score([int(T[q]['rows'][i]['label'] > 0) for i in sorted(S[q])], [S[q][i] for i in sorted(S[q])]) for q in QUERIES])

if __name__ == '__main__':
    base = today()
    model = sys.argv[1] if len(sys.argv) > 1 else 'bge-m3'
    qv_of = (lambda q: qvec(q)) if model == 'bge-m3' else None
    if qv_of is None:
        from reembed import call, MODELS
        qv_of = lambda q, m=model: call(m, [MODELS[m][0] + q])[0]
    for v in ('full', 'path', 'text'):
        try:
            S = sims(model, v, qv_of)
        except FileNotFoundError:
            continue
        H = {q: hybrid(q, sem=S[q]) for q in QUERIES}
        d = boot(base, H)
        print(f'{model} {v:5}: semantic alone flagged {flagged(S):.3f} AUC {auc(S):.3f} | hybrid flagged {flagged(H):.3f} '
              f'(vs today {d[0]:+.3f}, {d[1]:+.3f} to {d[2]:+.3f}) must {flagged(H, must_only=True):.3f}')
