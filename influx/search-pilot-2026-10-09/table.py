"""Markdown tables from eval rows (search pilot, 2026-10-09).

    python3 table.py RESULTS.json [--gold draft|qrels] [--target 1200] [--input ctx]
"""
import json, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import embed  # noqa: E402

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('results')
    ap.add_argument('--gold', default='draft')
    ap.add_argument('--target', type=int, default=1200)
    ap.add_argument('--input', default='ctx')
    a = ap.parse_args()
    rows = [r for r in json.load(open(a.results)) if r.get('gold', 'draft') == a.gold
            and r['target'] == a.target and r['input'] == a.input]
    last = {}
    for r in rows:
        last[(r['model'], r['mode'])] = r
    models = list(dict.fromkeys(m for m, _ in last if m != '-'))
    modes = ['sem', 'mix+p', 'rrf+p']
    def timing(m):
        name = m.replace(':', '_')
        f = os.path.join(embed.SCRATCH, 'emb', f'{name}__t{a.target}__{a.input}.json')
        if os.path.exists(f):
            j = json.load(open(f))
            return f'{j["seconds"]:.0f}', str(j.get('dims', ''))
        return '', ''
    print('| model | dims | embed s (3,714 passages) | ' + ' | '.join(f'nDCG@10 {m}' for m in modes) + ' | sem: term / nl |')
    print('|---|---|---|' + '---|' * len(modes) + '---|')
    order = sorted(models, key=lambda m: -last.get((m, 'sem'), {}).get('ndcg', 0))
    for m in order:
        s, d = timing(m)
        cells = [f'{last[(m, md)]["ndcg"]:.3f}' if (m, md) in last else '' for md in modes]
        sem = last.get((m, 'sem'))
        tn = f'{sem["ndcg_term"]:.2f} / {sem["ndcg_nl"]:.2f}' if sem else ''
        print(f'| {m} | {d} | {s} | ' + ' | '.join(cells) + f' | {tn} |')
    for md in ('lex', 'lex+p'):
        if ('-', md) in last:
            r = last[('-', md)]
            print(f'| (lexical only, {md}) | | | {r["ndcg"]:.3f} | | | {r["ndcg_term"]:.2f} / {r["ndcg_nl"]:.2f} |')

if __name__ == '__main__':
    main()
