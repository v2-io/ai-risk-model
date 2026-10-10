"""decompose.py's 'no query content word' share, recomputed with stems (Postgres english config) and with
prefix matching, to see how much of the 50% is morphology rather than absence."""
from dn import *
conn = ro_conn()
CUT = 188
tot_un = tot_now_exact = tot_now_stem = tot_now_pref = 0
per = []
for q in QUERIES:
    rows = T[q]['rows']; ko = {(r['key'], r['ord']): i for i, r in rows.items()}
    ws = T[q]['pq']['words']
    for st in T[q]['stretches']:
        ids = [ko[k] for k in st['ps']]
        h = [rows[i]['hrank'] for i in ids if rows[i]['hrank']]
        if h and min(h) <= CUT: continue
        g = st['gain']; tot_un += g
        exact = max(rows[i]['qwords_present'] for i in ids)
        stem = conn.execute("select count(*) from src.passages where id = any(%s) and to_tsvector('english', text) @@ "
                            "to_tsquery('english', %s)", (ids, ' | '.join(ws))).fetchone()[0]
        pref = conn.execute("select count(*) from src.passages where id = any(%s) and to_tsvector('simple', text) @@ "
                            "to_tsquery('simple', %s)", (ids, ' | '.join(w[:5] + ':*' for w in ws))).fetchone()[0]
        tot_now_exact += g * (exact == 0); tot_now_stem += g * (stem == 0); tot_now_pref += g * (pref == 0)
        if exact == 0 and stem > 0: per.append((q, st['sid'], 'stem hit'))
print(f'unflagged gain {tot_un}; no word exact {tot_now_exact / tot_un:.2f}, no word by english stem {tot_now_stem / tot_un:.2f}, '
      f'no 5-letter prefix {tot_now_pref / tot_un:.2f}')
from collections import Counter
print(Counter(p[0][:40] for p in per))
