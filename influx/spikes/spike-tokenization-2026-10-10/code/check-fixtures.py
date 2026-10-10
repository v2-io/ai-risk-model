#!/usr/bin/env python3
"""Check fixtures/tokenization.json against an index and a query path.

    code/check-fixtures.py                     search/'s code, database $AIRISK_SOURCES_DB (default airisk_sources)
    python3 code/patched.py code/check-fixtures.py     the patched code (run with AIRISK_SOURCES_DB=airisk_tokspike)

Read-only. 'forms': the lexemes Postgres gives the string as the index would see it
(through src.index_form when the database has it, else raw, as today). 'findable': the
query's lexemes by the ranking code's own path (rank.parse, then rank._lexemes on what
rank.lexical passes it), each looked up in the stored tsv_exact of every passage of the
document holding the quote. Run from the repository root.
"""
import json, os, re, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, *['..'] * 4))
if 'srcsearch' not in sys.modules:
    sys.path.insert(0, os.path.join(REPO, 'search'))
from srcsearch import db, rank  # noqa: E402

FIX = json.load(open(os.path.join(HERE, '..', 'fixtures', 'tokenization.json')))
conn = db.connect()
dbname = conn.info.dbname
has_form = conn.execute("select exists (select 1 from pg_proc p join pg_namespace n on n.oid = p.pronamespace "
                        "where n.nspname = 'src' and p.proname = 'index_form')").fetchone()[0]
patched = 'PATCHED' in open(rank.__file__).read()
print(f'database {dbname}; index form: {"src.index_form" if has_form else "none (raw text)"}; '
      f'ranking code: {"patched" if patched else "search/srcsearch"}')


def query_text(pq):
    # what rank.lexical hands to _lexemes
    return pq['term'] if patched else ' '.join(pq['words'])


fails = 0
print('\nforms')
for f in FIX['forms']:
    sql = "select array_agg(lexeme order by lexeme) from unnest(to_tsvector('simple', " + \
          ("src.index_form(%s)" if has_form else "%s") + "))"
    got = set(conn.execute(sql, (f['text'],)).fetchone()[0] or [])
    want = set(f['lexemes'])
    ok = got == want
    fails += not ok
    extra = f"   got {sorted(got)}" if not ok else ''
    print(f"  {'ok  ' if ok else 'FAIL'} {f['text']!r:42} {f['class']}{extra}")

print('\nfindable')
for f in FIX['findable']:
    pq = rank.parse(f['query'])
    lex = rank._lexemes(conn, 'simple', query_text(pq))
    rows = conn.execute("select id, text, tsv_exact::text from src.passages where doc_key = %s", (f['doc'],)).fetchall()
    norm = lambda s: re.sub(r'\s+', ' ', s)
    held = [(i, t) for i, _, t in [(r[0], r[1], r[2]) for r in rows if norm(f['quote']) in norm(r[1])]]
    if not held:
        print(f"  ???? {f['query']!r:30} quote not found in {f['doc']}")
        fails += 1
        continue
    worst = None
    for i, tsv in held:
        have = set(re.findall(r"'((?:[^']|'')*)'", tsv))
        have = {h.replace("''", "'") for h in have}
        missing = [x for x in lex if x not in have]
        if worst is None or len(missing) > len(worst[1]):
            worst = (i, missing)
    ok = not worst[1]
    fails += not ok
    detail = f"   query lexemes {lex}; passage {worst[0]} lacks {worst[1]}" if not ok else f"   ({len(held)} passage{'s' if len(held) > 1 else ''})"
    print(f"  {'ok  ' if ok else 'FAIL'} {f['query']!r:30} {f['doc']:38} {f['class']}{detail}")

n = len(FIX['forms']) + len(FIX['findable'])
print(f'\n{n - fails} of {n} pass')
