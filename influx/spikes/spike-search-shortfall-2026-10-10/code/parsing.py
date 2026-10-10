#!/usr/bin/env python3
"""Query parsing variants on the lexical side only (the semantic side and multipliers as today):
  stop+   rank.STOP plus modal/negation/question words (can could no not must should would may might
          before after longer whether decided)
  df10    drop content words in more than 10% of the corpus's passages (unless that leaves none)
  df5     the same at 5%
Lexical scores recomputed with today's rank.lexical over Au5."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from rescore import *
from common import connect, AU5
from srcsearch import rank
conn = connect()
W = rank.weights()['lexical']
N = conn.execute('select count(*) from src.passages').fetchone()[0]
df = {}
def dfr(w):
    if w not in df:
        df[w] = conn.execute("select count(*) from src.passages where tsv_exact @@ to_tsquery('simple', %s)", (w,)).fetchone()[0] / N
    return df[w]
EXTRA = set('can could no not must should would may might before after longer whether decided'.split())
def variant(fn):
    S = {}
    for q in QUERIES:
        pq = rank.parse(q)
        ws = fn(pq['words']) or pq['words']
        lx, *_ = rank.lexical(conn, dict(pq, words=ws), W, AU5)
        S[q] = hybrid(q, lex={i: lx.get(i, 0.0) for i in T[q]['rows']})
        if ws != pq['words']:
            print(f'   {q[:45]:45} words {ws}', file=sys.stderr)
    return S
base = today()
for name, fn in (('stop+', lambda ws: [w for w in ws if w not in EXTRA]),
                 ('df10', lambda ws: [w for w in ws if dfr(w) <= 0.10]),
                 ('df5', lambda ws: [w for w in ws if dfr(w) <= 0.05])):
    S = variant(fn)
    d = boot(base, S)
    tot, pq = flagged(S, per_query=True)
    print(f'{name:6} flagged {tot:.3f} ({d[0]:+.3f}, {d[1]:+.3f} to {d[2]:+.3f}) must {flagged(S, must_only=True):.3f}  '
          f'shutdown-query {pq[QUERIES[3]]:.2f}')
