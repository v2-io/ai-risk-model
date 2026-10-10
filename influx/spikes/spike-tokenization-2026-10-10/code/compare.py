"""Per-query differences between two variants' eval outputs (runs/LABEL-*.txt).
    python3 code/compare.py D0 W
For outline-check: the budget-60 'flagged' and 'opened' reached scores per query and
pooled scope; for pilot-check: nDCG@10 per query."""
import re, sys
a, b = sys.argv[1:3]

def outline(label, which):
    out = {}
    for line in open(f'runs/{label}-outline-{which}.txt'):
        m = re.match(r'^(\S+)\s+(.{40}) B=(\d+)\s+opened ([\d.]+)/([\d.]+)\s+flagged ([\d.]+)/', line)
        if m:
            out[(m[1], m[2].strip(), int(m[3]))] = (float(m[4]), float(m[6]))
    return out

def pilot(label):
    out = {}
    for line in open(f'runs/{label}-pilot-check.txt'):
        m = re.match(r'^([\d.]+)\s+judged\s+[\d/]+\s+(.+?)\s*$', line)
        if m and not line.startswith('mean'):
            out[m[2]] = float(m[1])
    return out

for which in ('judges', 'experts'):
    A, B = outline(a, which), outline(b, which)
    diffs = [(k, A[k], B[k]) for k in A if k in B and A[k] != B[k]]
    print(f'== outline-check, {which}: {len(diffs)} of {len(A)} (scope, query, budget) rows differ')
    for k, x, y in sorted(diffs, key=lambda d: -abs(d[2][1] - d[1][1]) - abs(d[2][0] - d[1][0]))[:15]:
        print(f'  {k[0][:28]:28} {k[1][:40]:40} B={k[2]:<4} opened {x[0]:.2f}->{y[0]:.2f}  flagged {x[1]:.2f}->{y[1]:.2f}')
A, B = pilot(a), pilot(b)
diffs = [(k, A[k], B[k]) for k in A if k in B and A[k] != B[k]]
print(f'== pilot-check: {len(diffs)} of {len(A)} queries differ')
for k, x, y in diffs:
    print(f'  {k[:60]:60} {x:.3f} -> {y:.3f}')
