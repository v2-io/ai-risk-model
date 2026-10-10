"""fit_lr.py's model fitted on all 12 queries x 5 docs (in-sample) as a ceiling, and a variant weighting
each passage by its stretch's gain over the stretch's passage count (the spike's proposed fix, item 8)."""
from dn import *
import fit_lr as FL
from sklearn.linear_model import LogisticRegression
X, y, w, meta = FL.matrix(FL.ALL)
m = LogisticRegression(C=1.0, max_iter=3000).fit(X, y, sample_weight=w)
s = dict(zip([(q, i) for q, i, _ in meta], m.decision_function(X)))
print(f'in-sample LR (passage weights 3/1): AUC {FL.mean_auc(s):.3f} flagged {FL.flagged(s):.3f}')
# stretch-normalised weights: a passage's weight = sum over stretches it is in of gain/len(stretch)
w2 = []
for q, i, _ in meta:
    r = T[q]['rows'][i]
    ko = (r['key'], r['ord'])
    ww = sum(st['gain'] / len(st['ps']) for st in T[q]['stretches'] if ko in set(map(tuple, st['ps'])))
    w2.append(ww if ww > 0 else 1.0)
w2 = np.array(w2)
pos = y == 1
w2[pos] *= w[pos].sum() / w2[pos].sum()
m2 = LogisticRegression(C=1.0, max_iter=3000).fit(X, y, sample_weight=w2)
s2 = dict(zip([(q, i) for q, i, _ in meta], m2.decision_function(X)))
print(f'in-sample LR (stretch-normalised weights): AUC {FL.mean_auc(s2):.3f} flagged {FL.flagged(s2):.3f}')
# held out by query with stretch-normalised weights
groups = [q for q, _, _ in meta]; sc = {}
for g in sorted(set(groups)):
    tr = np.array([x != g for x in groups])
    mm = LogisticRegression(C=1.0, max_iter=3000).fit(X[tr], y[tr], sample_weight=w2[tr])
    for (q, i, _), v in zip([mm_ for mm_, t in zip(meta, tr) if not t], mm.decision_function(X[~tr])): sc[(q, i)] = v
print(f'LOQO LR (stretch-normalised weights): AUC {FL.mean_auc(sc):.3f} flagged {FL.flagged(sc):.3f}')
