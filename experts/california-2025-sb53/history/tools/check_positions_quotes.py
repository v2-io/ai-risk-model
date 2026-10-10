"""Check every «verbatim» span in POSITIONS.md against the line it cites.

Usage (from history/):  python3 -I tools/check_positions_quotes.py [--canonical DIR]

POSITIONS.md sets verbatim text in «guillemets», followed by a citation such as
(PCP1 483), (SCONC 150–199), (ATF 17) or (`versions/04…` line 122). For each span
this script finds the first citation after it, takes the cited lines (±2), and checks
that every fragment of the span (split at "[…]") occurs there. Before comparing it
normalizes curly and prime quotes, pandoc's backslash escapes, <sup>/<u> tags,
and * and ~ markup.

ATF is ref/canonical/anthropic-2025-transparency-framework.md, which is git-ignored and
built by bin/canonicalize. By default it is looked for under the repo root (four levels
above history/). Pass --canonical to point elsewhere (e.g. the main checkout's
ref/canonical). If it is missing, ATF citations are reported as skipped.

A MISS is not always an error. Each MISS line lists the other files that contain the
text ("found-in"). Expected misses (as of 2026-10-09) fall into four kinds:
  - the span is cited by a group reference just before it, not after;
  - the citation names two lines and the span is on the second;
  - the span quotes 07-15a (not scanned; same line numbers as 07-15b), actions.md,
    the main repo's source-catalog.md, or the web fetch in POSITIONS §5.1, none of
    which is in the scan set;
  - a list name cited after a group of names.
Anything else is worth a look.
"""
import os, re, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # history/
A = os.path.join(HERE, 'analyses')
V = os.path.join(HERE, 'versions')

CODES = {
    'SGO': '2025-03-20-senate-gov-org-cmte-on-02-27-text.md',
    'SJUD': '2025-04-04-senate-judiciary-cmte-on-03-27-text.md',
    'SFLR': '2025-05-27-senate-floor-third-reading-on-05-23-text.md',
    'AJUD': '2025-06-28-assembly-judiciary-cmte-on-05-23-text.md',
    'PCP1': '2025-07-15b-assembly-pcp-cmte-on-07-08-text.md',
    'AAPP': '2025-08-18-assembly-approps-cmte-on-07-17-text.md',
    'AFL1': '2025-09-03-assembly-floor-on-09-02-text.md',
    'AFL2': '2025-09-08-assembly-floor-on-09-05-text.md',
    'PCP2': '2025-09-10-assembly-pcp-cmte-rule-77.2-on-09-05-text.md',
    'AFL3': '2025-09-11-assembly-floor-on-09-05-text.md',
    'SCONC': '2026-07-21-senate-floor-unfinished-business-concurrence.md',
}


def norm(t):
    t = t.replace('\\$', '$').replace('\\[', '[').replace('\\]', ']').replace('\\', '')
    for a, b in [('″', '"'), ('′', "'"), ('“', '"'), ('”', '"'), ('’', "'"), ('‘', "'")]:
        t = t.replace(a, b)
    t = re.sub(r'<sup>|</sup>|<u>|</u>', '', t).replace('*', '').replace('~', '')
    return re.sub(r'\s+', ' ', t).strip()


def main(argv):
    canon = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(HERE))), 'ref', 'canonical')
    if '--canonical' in argv:
        canon = argv[argv.index('--canonical') + 1]
    paths = {k: os.path.join(A, v) for k, v in CODES.items()}
    atf = os.path.join(canon, 'anthropic-2025-transparency-framework.md')
    if os.path.exists(atf):
        paths['ATF'] = atf
    for f in os.listdir(V):
        paths['V' + f[:2]] = os.path.join(V, f)
    lines = {k: open(p, encoding='utf-8').read().split('\n') for k, p in paths.items()}
    whole = {k: norm(' '.join(v)) for k, v in lines.items()}
    doc = open(os.path.join(HERE, 'POSITIONS.md'), encoding='utf-8').read()
    cite = re.compile(r'\b(SGO|SJUD|SFLR|AJUD|PCP1|PCP2|AAPP|AFL1|AFL2|AFL3|SCONC|ATF) (\d+)(?:–(\d+))?'
                      r'|`versions/(0\d)…` lines? (\d+)')
    n = miss = nocite = skipped = 0
    for m in re.finditer(r'«(.*?)»', doc, flags=re.S):
        q = m.group(1)
        n += 1
        c = cite.search(doc, m.end(), m.end() + 400)
        if not c:
            nocite += 1
            continue
        if c.group(1):
            k, a = c.group(1), int(c.group(2))
            b = int(c.group(3) or a)
        else:
            k, a = 'V' + c.group(4), int(c.group(5))
            b = a
        if k not in lines:
            skipped += 1
            print(f'SKIP {k}: no file for this code (ATF needs --canonical): «{q[:60]}»')
            continue
        window = norm(' '.join(lines[k][max(0, a - 3):b + 2]))
        frags = [norm(f) for f in re.split(r'\[…\]', q) if norm(f)]
        missing = [f for f in frags if f not in window]
        if missing:
            miss += 1
            found = [kk for kk in whole if all(f in whole[kk] for f in missing)]
            print(f'MISS {k} {a}-{b}: «{q[:70]}» found-in: {found[:5]}')
    print(f'{n} spans; {miss} miss; {nocite} with no citation within 400 chars after; {skipped} skipped')


if __name__ == '__main__':
    main(sys.argv[1:])
