from dn import *
conn = ro_conn()
d = json.load(open(os.path.join(SP, 'runs', 'blind-expansions.json')))['queries']
n = hit = 0; long_hits = []
for q, v in d.items():
    for p in v['rephrasings'] + v['neighbours']:
        n += 1
        docs = conn.execute("select array_agg(distinct doc_key) from src.passages where doc_key = any(%s) and layer='canonical' "
                            "and tsv_exact @@ phraseto_tsquery('simple', %s)", (CM.AU5, p)).fetchone()[0]
        if docs:
            hit += 1
            if len(p.split()) >= 4: long_hits.append((p, [x[:12] for x in docs]))
print(f'{hit}/{n} expansion phrases occur verbatim (as a phrase) in Au5')
for p, ds in long_hits: print('  ', p, ds)
