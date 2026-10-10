#!/usr/bin/env python3
"""Decompose the outline's unflagged share, stretch by stretch.

A stretch is "flagged" (as outline-check's 'flagged reached') when any passage overlapping it is
in the outline's tiers: hybrid rank <= 10% of the scope (188 of 1,872 for Au5). Gain 3 for must, 1 for helps.

For each unflagged stretch, which of these holds:
  NC   no passage in it is a candidate at all (H-C1: lexical hit, 400-nearest, or definition)
  CL   some passage is a candidate, but the best is ranked past the cut
and, independently, what other single signals would have done:
  semF  the best full-scan cosine rank of its passages is within the cut
  lexF  the best lexical-only rank within the cut
  words whether any passage holds any query content word (rank.parse's words, exact token)
"""
import os, pickle, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from common import SPIKE, QUERIES

T = pickle.load(open(os.path.join(SPIKE, 'runs', 'table.pkl'), 'rb'))['table']
CUT = int(sys.argv[1]) if len(sys.argv) > 1 else 188


def best(rows, ids, f):
    vals = [rows[i][f] for i in ids if rows[i][f] is not None]
    return min(vals) if vals else None


def main():
    tot = defaultdict(float)
    print(f'cut = {CUT} (hybrid rank); gain-weighted shares of each query\'s judged stretches\n')
    print(f'{"query":42} {"max":>4} {"flag":>5} {"NC":>5} {"CL":>5} | of unflagged: {"semF":>5} {"lexF":>5} {"noW":>5}')
    detail = []
    for q in QUERIES:
        d = T[q]
        rows = d['rows']
        ko = {(r['key'], r['ord']): i for i, r in rows.items()}
        mx = fl = nc = cl = semf = lexf = now = 0
        for st in d['stretches']:
            ids = [ko[k] for k in st['ps']]
            g = st['gain']
            mx += g
            h = best(rows, ids, 'hrank')
            if h is not None and h <= CUT:
                fl += g
                continue
            if not any(rows[i]['cand'] for i in ids):
                nc += g
                kind = 'NC'
            else:
                cl += g
                kind = 'CL'
            sf = best(rows, ids, 'sem_full')
            lr = best(rows, ids, 'lex_rank')
            w = max(rows[i]['qwords_present'] for i in ids)
            semf += g * (sf <= CUT)
            lexf += g * (lr is not None and lr <= CUT)
            now += g * (w == 0)
            detail.append(dict(q=q, kind=kind, sid=st['sid'], key=st['key'], grade=st['grade'], lines=st['lines'],
                               hrank=h, sem_full=sf, lex_rank=lr, words=w, nps=len(ids), quote=st['quote'][:90],
                               note=st['note'][:160]))
        for k, v in dict(max=mx, fl=fl, nc=nc, cl=cl, semf=semf, lexf=lexf, now=now).items():
            tot[k] += v
        un = (mx - fl) or 1
        print(f'{q[:42]:42} {mx:>4} {fl / mx:>5.2f} {nc / mx:>5.2f} {cl / mx:>5.2f} | {"":14}{semf / un:>5.2f} {lexf / un:>5.2f} {now / un:>5.2f}')
    mx, un = tot['max'], tot['max'] - tot['fl']
    print(f'{"POOLED":42} {mx:>4.0f} {tot["fl"] / mx:>5.2f} {tot["nc"] / mx:>5.2f} {tot["cl"] / mx:>5.2f} | {"":14}'
          f'{tot["semf"] / un:>5.2f} {tot["lexf"] / un:>5.2f} {tot["now"] / un:>5.2f}')
    pickle.dump(detail, open(os.path.join(SPIKE, 'runs', f'unflagged-{CUT}.pkl'), 'wb'))
    return detail


if __name__ == '__main__':
    main()
