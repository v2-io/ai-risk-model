"""--defs and --all as the design describes them, over the pilot passages (2026-10-09).

    python3 defs.py --defs developer
    python3 defs.py --all hazard

--defs: every detected definition whose term is the query or contains it as
whole words, grouped by source, with its evidence and an anchor.
--all: every occurrence of any word form containing the query (so 'infohazard'
and 'biohazards' are caught), counted by source and form, with indexed text
(link targets and IASR's tooltips removed) and the references section counted
apart.
"""
import collections, os, re, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import chunk, embed, search  # noqa: E402

def defs(query, target=1200):
    ps = embed.passages_for(target)
    qn = chunk.norm_term(query)
    by = collections.defaultdict(list)
    for p in ps:
        for d in p['defs']:
            n = d.get('norm') or chunk.norm_term(d['term'])
            if n == qn or re.search(r'\b' + re.escape(qn) + r'\b', n):
                by[p['key']].append((p, d))
    for k in embed.KEYS:
        if k not in by:
            continue
        print(f'== {k}')
        for p, d in by[k]:
            a = search.anchor(p, d['term'])
            print(f'  {d["term"]!r:<40} {d["kind"]:<26} conf {d["conf"]:.2f}   {search.fmt_anchor(a)[:200]}')

def concordance(query, target=1200):
    ps = embed.passages_for(target)
    q = query.lower()
    tot = collections.Counter()
    for k in embed.KEYS:
        body, refs = collections.Counter(), collections.Counter()
        for p in ps:
            if p['key'] != k:
                continue
            c = refs if p['section'] in ('references',) else body
            if ' ' in q:
                c[q] += len(re.findall(r'\b' + r'\W+'.join(map(re.escape, q.split())) + r'\b', search.fold(p['text'])))
            else:
                for w in search.words(p['text']):
                    if q in w:
                        c[w] += 1
        if sum(body.values()) or sum(refs.values()):
            print(f'{k:<40} body {sum(body.values()):>4}  {dict(body.most_common())}'
                  + (f'   references {sum(refs.values())}' if refs else ''))
            tot.update(body)
    print(f'forms matched across the pilot: {dict(tot.most_common())}')

if __name__ == '__main__':
    mode, query = sys.argv[1], ' '.join(sys.argv[2:])
    (defs if mode == '--defs' else concordance)(query)
