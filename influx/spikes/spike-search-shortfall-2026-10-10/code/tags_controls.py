#!/usr/bin/env python3
"""Controls for the tags result (tags-both, beta 1, no expansion):
  bridge   only tags sharing no content word with the passage's text or heading path
  echo     only tags that do share one
  tfidf    no model knowledge: each passage's own top-n TF-IDF words (n = its tag count), as tags
Each is indexed the same way (BM25 over tags + bge-m3 embedding of the joined tags) and fused at beta 1."""
import collections, math, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import tags_eval as te
from rescore import *
import rescore
from common import connect, passages
conn = connect(); P = passages(conn); tags = te.load_tags()
STOP = te.rank.STOP | set('also more such other their these those into than been being which while within'.split())
def cw(s): return {w for w in te.toks(s) if w not in STOP and len(w) > 2}
ptoks = {i: cw(P[i]['text'] + ' ' + ' '.join(P[i]['path'])) for i in P}
bridge = {i: [t for t in tags[i] if not (cw(t) & ptoks[i])] for i in P}
echo = {i: [t for t in tags[i] if cw(t) & ptoks[i]] for i in P}
df = collections.Counter(w for i in P for w in set(te.toks(P[i]['text'])) if w not in STOP and len(w) > 2)
N = len(P)
tfidf = {}
for i in P:
    c = collections.Counter(w for w in te.toks(P[i]['text']) if w not in STOP and len(w) > 2 and not w.isdigit())
    tfidf[i] = [w for w, _ in sorted(c.items(), key=lambda x: -x[1] * math.log(N / df[x[0]]))[:len(tags[i])]]
nb = sum(map(len, bridge.values())); ne = sum(map(len, echo.values()))
print(f'tags: {nb} bridge, {ne} echo ({nb / (nb + ne):.0%} bridge)')
ids = sorted(P)
base = today()
qvs = {q: (lambda v: v / np.linalg.norm(v))(np.array(te.qvec(q), dtype=np.float32)) for q in QUERIES}
for name, T_ in (('all tags', tags), ('bridge only', bridge), ('echo only', echo), ('tfidf control', tfidf)):
    bm = te.BM25(T_)
    V = te.embed_many({i: '; '.join(T_[i]) or '(none)' for i in P}, os.path.join(te.CACHE, f'bge-m3-tags-{name.replace(" ", "_")}.npz'))
    Vm = np.stack([V[i] for i in ids])
    S = {}
    for q in QUERIES:
        M = rescore._M.setdefault(q, rescore.multipliers(q))
        tl = te.ranks(bm.score(q)); ts = te.ranks(dict(zip(ids, (Vm @ qvs[q]).tolist())), 400)
        S[q] = {i: base[q][i] + M[i] * (1 / (60 + tl.get(i, NBIG)) + 1 / (60 + ts.get(i, NBIG))) for i in base[q]}
    d = boot(base, S)
    print(f'{name:14} flagged {flagged(S):.3f} ({d[0]:+.3f}, {d[1]:+.3f} to {d[2]:+.3f}) must {flagged(S, must_only=True):.3f}')
