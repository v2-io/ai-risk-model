#!/usr/bin/env python3
"""Fable's measurement (RANKING §8.7): a logistic regression on the features today's --explain
prints, over the whole-document judgments, held out by document (LODO) and by query (LOQO).

Unit: (query, passage) over all 1,872 Au5 passages x 12 queries. Label: overlaps any judged stretch.
Features are standardised within each query (RANKING §3.3). Ridge (L2) towards zero.

Reported: per-query passage AUC (mean), and the outline's flagged measure (gain-weighted share of
stretches with a passage in the top 188), for the fitted ranking against today's hybrid rank.
Passages with no candidate get feature values as if absent (lexical 0, etc.) but keep their cosine,
since the fit may use the full-scan cosine; a variant 'pool' restricts to today's candidates.
"""
import math, os, pickle, sys
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
sys.path.insert(0, os.path.dirname(__file__))
from common import SPIKE, QUERIES, AU5

T = pickle.load(open(os.path.join(SPIKE, 'runs', 'table.pkl'), 'rb'))['table']
CUT = 188
SECTIONS = ['references', 'glossary', 'annex', 'figure', 'toc', 'restored']


def feats(r, which):
    f = {}
    f['cos'] = r['cos']
    f['log_sem_rank'] = -math.log(r['sem_full'])
    f['lex'] = math.log1p(r['lexical'])
    f['has_lex'] = float(r['lexical'] > 0)
    f['phrase'] = float(r['phrase'])
    f['heading'] = float(r['heading'])
    f['prox'] = r['proximity'] or 0.0
    f['defines'] = math.log(r['f_def'])
    f['coverage'] = r['qwords_present'] / max(1, r['qwords_n'])
    f['log_nwords'] = math.log(1 + r['nwords'])
    for s in SECTIONS:
        f['sec_' + s] = float(r['section'] == s)
    f['hybrid'] = math.log(r['score']) if r['score'] else math.log(1e-6)
    return {k: f[k] for k in which}


ALL = ['cos', 'log_sem_rank', 'lex', 'has_lex', 'phrase', 'heading', 'prox', 'defines', 'coverage', 'log_nwords'] + \
      ['sec_' + s for s in SECTIONS]
SETS = {
    'today-features': ALL,
    'cos+lex only': ['cos', 'lex'],
    'cos only': ['cos'],
    'hybrid score only': ['hybrid'],
}


def matrix(which):
    X, y, w, meta = [], [], [], []
    for q in QUERIES:
        rows = T[q]['rows']
        ids = sorted(rows)
        F = np.array([[feats(rows[i], which)[k] for k in which] for i in ids], dtype=float)
        sd = F.std(0)
        sd[sd == 0] = 1
        F = (F - F.mean(0)) / sd
        for j, i in enumerate(ids):
            r = rows[i]
            X.append(F[j])
            y.append(int(r['label'] > 0))
            w.append(3.0 if r['label'] == 2 else 1.0)
            meta.append((q, i, r['key']))
    return np.array(X), np.array(y), np.array(w), meta


def flagged(score_of):
    num = den = 0
    for q in QUERIES:
        rows = T[q]['rows']
        ranked = sorted(rows, key=lambda i: -score_of[(q, i)])
        rk = {i: k + 1 for k, i in enumerate(ranked)}
        ko = {(r['key'], r['ord']): i for i, r in rows.items()}
        for st in T[q]['stretches']:
            b = min(rk[ko[k]] for k in st['ps'])
            den += st['gain']
            num += st['gain'] * (b <= CUT)
    return num / den


def mean_auc(score_of):
    a = []
    for q in QUERIES:
        rows = T[q]['rows']
        y = [int(rows[i]['label'] > 0) for i in sorted(rows)]
        s = [score_of[(q, i)] for i in sorted(rows)]
        a.append(roc_auc_score(y, s))
    return np.mean(a)


def heldout(which, by, C=1.0):
    X, y, w, meta = matrix(which)
    groups = [m[2] if by == 'doc' else m[0] for m in meta]
    score, coefs = {}, []
    for g in sorted(set(groups)):
        tr = np.array([x != g for x in groups])
        m = LogisticRegression(C=C, max_iter=2000)
        m.fit(X[tr], y[tr], sample_weight=w[tr])
        coefs.append(m.coef_[0])
        p = m.decision_function(X[~tr])
        for (q, i, _), s in zip([mm for mm, t in zip(meta, tr) if not t], p):
            score[(q, i)] = s
    return score, np.array(coefs)


def main():
    base = {(q, i): (r['score'] if r['score'] else -1) for q in QUERIES for i, r in T[q]['rows'].items()}
    print(f"today's hybrid:            AUC {mean_auc(base):.3f}   flagged@188 {flagged(base):.3f}")
    cos = {(q, i): r['cos'] for q in QUERIES for i, r in T[q]['rows'].items()}
    print(f"cosine alone (full scan):  AUC {mean_auc(cos):.3f}   flagged@188 {flagged(cos):.3f}")
    for name, which in SETS.items():
        for by in ('doc', 'query'):
            s, co = heldout(which, by)
            print(f'LR {name:18} held out by {by:5}: AUC {mean_auc(s):.3f}   flagged@188 {flagged(s):.3f}')
            if name == 'today-features':
                print('    coefficient (mean, min, max over folds; standardised features):')
                for k, col in zip(which, co.T):
                    flip = ' SIGN FLIPS' if col.min() < 0 < col.max() else ''
                    print(f'      {k:14} {col.mean():+.3f}  [{col.min():+.3f}, {col.max():+.3f}]{flip}')


if __name__ == '__main__':
    main()
