#!/usr/bin/env python3
"""Longest shared verbatim runs between two extractions (8-token shingles).

    python3 -I tools/shared_runs.py A.txt B.txt [N]

Used for the lineage records: shared text shows a relation, not its direction.
Added in the repair after de-novo-feedback-1 (the verifier ran the same kind of
comparison). Disposable.
"""
import re,sys
def toks(p):
    s=open(p).read().replace('​','').replace('’',"'").replace('“','"').replace('”','"')
    return re.findall(r"[A-Za-z0-9$>']+|[.,;:()]",s)
a,b=toks(sys.argv[1]),toks(sys.argv[2]); n=8
idx={}
for i in range(len(b)-n+1): idx.setdefault(tuple(b[i:i+n]),[]).append(i)
runs=[];i=0
while i<len(a)-n+1:
    k=tuple(a[i:i+n])
    if k in idx:
        best=0
        for j in idx[k]:
            L=n
            while i+L<len(a) and j+L<len(b) and a[i+L]==b[j+L]: L+=1
            best=max(best,L)
        runs.append((best,' '.join(a[i:i+best]))); i+=best
    else: i+=1
for L,t in sorted(runs,reverse=True)[:int(sys.argv[3]) if len(sys.argv)>3 else 8]: print(L, t[:260])
