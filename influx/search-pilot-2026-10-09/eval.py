"""Score rankings against gold-draft.json (search pilot, 2026-10-09).

    python3 eval.py [--models m1,m2] [--modes sem,lex,mix,mix+p] [--target 1200] [--input ctx] [--per-query]

An expected item counts as found at the rank of the first passage, from its
key, whose text contains its quote (letters and digits, casefolded). Metrics per
query: nDCG@10 (gain 2^grade - 1, each expected item credited once), recall of
grade>=2 items in the top 10 and top 30, and the rank of the first grade-3 item.
"""
import json, math, os, re, sys
sys.dont_write_bytecode = True
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import embed, search  # noqa: E402

def letters(s):
    return re.sub(r'[^0-9a-z]', '', search.fold(s))

def load_gold():
    return json.load(open(os.path.join(HERE, 'gold-draft.json')))['queries']

def matches(ix, gold):
    """for each query, for each expected item, the set of passage indices that hold it"""
    L = [letters(p['text']) for p in ix.ps]
    out = []
    for g in gold:
        per = []
        for e in g['expect']:
            q = letters(e['quote'])
            per.append({i for i, p in enumerate(ix.ps) if p['key'] == e['key'] and q in L[i]})
        out.append(per)
    return out

def units(expect, hold):
    """Expected items that one passage satisfies together (SB 53's (c)(1) and (c)(2) share a
    passage) are scored as one unit at their highest grade, so nDCG stays within [0, 1]."""
    us = []
    for e, h in zip(expect, hold):
        for u in us:
            if u['hold'] & h:
                u['hold'] |= h
                u['grade'] = max(u['grade'], e['grade'])
                break
        else:
            us.append(dict(grade=e['grade'], hold=set(h)))
    return [dict(grade=u['grade']) for u in us], [u['hold'] for u in us]

def score(order, expect, hold, k=10):
    expect, hold = units(expect, hold)
    pos = {int(i): r for r, i in enumerate(order[:2000], 1)}
    ranks = []
    for e, h in zip(expect, hold):
        rr = [pos[i] for i in h if i in pos]
        ranks.append(min(rr) if rr else None)
    # nDCG@k: each expected item once, at its best rank
    dcg = sum((2 ** e['grade'] - 1) / math.log2(r + 1) for e, r in zip(expect, ranks) if r and r <= k)
    ideal = sorted((2 ** e['grade'] - 1 for e in expect), reverse=True)
    idcg = sum(g / math.log2(i + 2) for i, g in enumerate(ideal[:k]))
    strong = [r for e, r in zip(expect, ranks) if e['grade'] >= 2]
    first3 = min([r for e, r in zip(expect, ranks) if e['grade'] == 3 and r] or [9999])
    return dict(ndcg=dcg / idcg if idcg else 0, r10=sum(1 for r in strong if r and r <= 10) / max(1, len(strong)),
                r30=sum(1 for r in strong if r and r <= 30) / max(1, len(strong)), first3=first3, ranks=ranks)

def qvecs(model):
    have = embed.save_queries(model)
    return {q: np.array(v, dtype=np.float32) for q, v in have.items()}

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--models', default='bge-m3')
    ap.add_argument('--modes', default='sem,lex,lex+p,mix,mix+p,rrf+p')
    ap.add_argument('--target', type=int, default=1200)
    ap.add_argument('--input', default='ctx')
    ap.add_argument('--per-query', action='store_true')
    ap.add_argument('--json')
    ap.add_argument('--qrels', help='judgments JSON {query: {pid: grade}} (comma-separated files merge); replaces gold-draft expectations')
    a = ap.parse_args()
    gold = load_gold()
    ix = search.Index(a.target)
    if a.qrels:
        # judged pool: each judged passage (grade > 0) is its own expected item
        qr = {}
        for f in a.qrels.split(','):
            for q, d in json.load(open(f)).items():
                qr.setdefault(q, {}).update(d)
        pid = {p['id']: i for i, p in enumerate(ix.ps)}
        for g in gold:
            g['expect'] = [dict(key=k.split('#')[0], quote='', grade=int(v), pid=k) for k, v in qr.get(g['q'], {}).items() if int(v) > 0]
        hold = [[{pid[e['pid']]} for e in g['expect']] for g in gold]
    else:
        hold = matches(ix, gold)
    missing = [(g['q'], e['key'], e['quote'][:50]) for g, hs in zip(gold, hold) for e, h in zip(g['expect'], hs) if not h]
    for m in missing:
        print('NOT IN ANY PASSAGE (chunk boundary or quote error):', m)
    rows = []
    for model in a.models.split(','):
        qv = None
        for mode in a.modes.split(','):
            if not mode.startswith('lex') and qv is None:
                qv = qvecs(model)
            res = []
            for g, hs in zip(gold, hold):
                order, _ = ix.rank(g['q'], model, mode, inp=a.input, qvec=None if mode.startswith('lex') else qv[g['q']])
                s = score(order, g['expect'], hs)
                res.append(s)
                if a.per_query:
                    print(f'  {model:<26} {mode:<6} {g["q"][:40]:<40} ndcg {s["ndcg"]:.2f} first3 {s["first3"]:>4} ranks {s["ranks"]}')
            term = [s for g, s in zip(gold, res) if g['kind'] == 'term']
            nl = [s for g, s in zip(gold, res) if g['kind'] == 'nl']
            row = dict(model=model if not mode.startswith('lex') else '-', mode=mode, target=a.target, input=a.input,
                       gold='qrels' if a.qrels else 'draft',
                       ndcg=np.mean([s['ndcg'] for s in res]), ndcg_term=np.mean([s['ndcg'] for s in term]),
                       ndcg_nl=np.mean([s['ndcg'] for s in nl]), r10=np.mean([s['r10'] for s in res]),
                       r30=np.mean([s['r30'] for s in res]),
                       first3_top3=sum(1 for s in res if s['first3'] <= 3) / len(res),
                       per_query={g['q']: dict(ndcg=round(s['ndcg'], 3), first3=s['first3'], ranks=s['ranks']) for g, s in zip(gold, res)})
            rows.append(row)
            print(f'{row["model"]:<26} {mode:<6} t{a.target} {a.input:<3}  nDCG@10 {row["ndcg"]:.3f} (term {row["ndcg_term"]:.3f}, nl {row["ndcg_nl"]:.3f})  '
                  f'R@10 {row["r10"]:.2f}  R@30 {row["r30"]:.2f}  grade-3 in top 3: {row["first3_top3"]:.2f}', flush=True)
    if a.json:
        prev = json.load(open(a.json)) if os.path.exists(a.json) else []
        json.dump(prev + rows, open(a.json, 'w'), indent=1, default=float)

if __name__ == '__main__':
    main()
