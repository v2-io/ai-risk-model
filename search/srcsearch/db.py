"""Reconcile the database with the inputs (DESIGN §4).

A run computes every document's fingerprints from the inputs and brings the
database to match: new or changed text is re-chunked, changed metadata updates the
document row, keys that left the catalog are deleted. Running it twice changes
nothing the second time.

Three fingerprints per document:
- text_fp: the canonical file's bytes and the chunker's own source. A changed
  chunker re-chunks everything; hashing its source, not a version number, means a
  forgotten version bump can't leave stale passages (memorata's lesson);
- meta_fp: its bib entry and catalog row. The title goes into each passage's
  embedding input, so a changed title re-chunks the document too;
- fidelity_fp: pages.json's fidelity section.
"""
import hashlib, json, os, time

import psycopg

from . import SEARCH, catalog, chunk
from .text import words

DB = os.environ.get('AIRISK_SOURCES_DB', 'airisk_sources')
SCHEMA = os.path.join(SEARCH, 'schema.sql')
CHUNKER_FILES = ('text.py', 'chunk.py', 'defs.py', 'db.py')


def file_sha(*paths):
    h = hashlib.sha256()
    for p in paths:
        h.update(open(p, 'rb').read())
    return h.hexdigest()


def chunker_sha():
    here = os.path.dirname(os.path.abspath(__file__))
    return file_sha(*(os.path.join(here, f) for f in CHUNKER_FILES))


def schema_sha():
    return file_sha(SCHEMA)


def connect(db=DB, create=False):
    try:
        return psycopg.connect(dbname=db)
    except psycopg.OperationalError as e:
        if not create or 'does not exist' not in str(e):
            raise
    with psycopg.connect(dbname='postgres', autocommit=True) as c:
        c.execute(f'create database "{db}"')
    return psycopg.connect(dbname=db)


CACHE_SQL = os.path.join(SEARCH, 'cache.sql')


def ensure_cache(conn):
    """Create the cache tables beyond the embeddings if missing (search/cache.sql)."""
    with conn.transaction():
        conn.execute(open(CACHE_SQL, encoding='utf-8').read())


def ensure_schema(conn, rebuild=False):
    """Create schema src if missing, or drop and recreate it with rebuild. Returns
    a message if the database was built from a different schema.sql."""
    with conn.transaction():
        has = conn.execute("select 1 from information_schema.schemata where schema_name = 'src'").fetchone()
        if has and rebuild:
            conn.execute('drop schema src cascade')
            has = None
        if not has:
            conn.execute(open(SCHEMA, encoding='utf-8').read())
            conn.execute("insert into src.meta values ('schema_sha', %s)", (schema_sha(),))
            conn.execute(open(CACHE_SQL, encoding='utf-8').read())
            return None
        built = conn.execute("select value from src.meta where name = 'schema_sha'").fetchone()
        if not built or built[0] != schema_sha():
            return 'search/schema.sql has changed since this database was built: run bin/source-index --rebuild'
    return None


def embed_input(doc, p):
    """The text a passage's embedding is made from: the document's title and the
    passage's heading path, then its text (DESIGN §5.4). A bare clause like
    '(c) "Catastrophic risk" means …' is then findable as SB 53's."""
    head = ' › '.join(p['path']) if p['path'] else (
        '(text restored from the PDF\'s text layer)' if p['section'] == 'restored' else '')
    return f"{doc.get('title') or doc['key']}\n{head}\n\n{p['text']}"


def _doc_row(d, text_fp, n):
    cols = ('key', 'status', 'active_key', 'subsumed_by', 'no_canon', 'has_text', 'section', 'code', 'group_label',
            'influence', 'cat_date', 'cat_kind', 'cat_document', 'title', 'authors', 'org', 'year', 'url', 'bib_type',
            'fidelity_mark', 'pages_to_check')
    row = {c: d[c] for c in cols}
    row.update(text_fp=text_fp, meta_fp=d['meta_fp'], fidelity_fp=d['fidelity_fp'], n_passages=n)
    return row


def _upsert_doc(conn, row):
    cols = list(row)
    conn.execute(
        f"insert into src.documents ({', '.join(cols)}, indexed_at) values ({', '.join('%(' + c + ')s' for c in cols)}, now()) "
        f"on conflict (key) do update set {', '.join(f'{c} = excluded.{c}' for c in cols if c != 'key')}, indexed_at = now()",
        row)


def _write_text(conn, d, passages, headings):
    """Replace a document's passages, definitions and headings."""
    conn.execute('delete from src.passages where doc_key = %s', (d['key'],))
    conn.execute('delete from src.headings where doc_key = %s', (d['key'],))
    conn.execute('delete from src.definitions where doc_key = %s', (d['key'],))
    with conn.cursor() as cur:
        cur.executemany(
            'insert into src.headings (doc_key, ord, start_off, end_off, level, text, title, path, page, printed) '
            'values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            [(d['key'], k, h['start'], h['end'], h['level'], h['text'], h.get('title'), h['path'], h['page'], h['printed'])
             for k, h in enumerate(headings)])
        cur.executemany(
            'insert into src.passages (doc_key, ord, start_off, end_off, page, printed, page_last, printed_last, pages, '
            'not_in_pdf, path, heading, section, kinds, text, nwords, norm_sha, embed_sha) '
            'values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) returning id',
            [(d['key'], p['ord'], p['start'], p['end'], p['page'], p['printed'], p['page_last'], p['printed_last'],
              p['pages'] if p['pages'] != [None] else None, p['not_in_pdf'], p['path'], ' › '.join(p['path']),
              p['section'], p['kinds'],
              p['text'], len(words(p['text'])), p['norm_sha'], hashlib.sha256(embed_input(d, p).encode()).hexdigest())
             for p in passages], returning=True)
        ids = []
        while passages:
            ids.append(cur.fetchone()[0])
            if not cur.nextset():
                break
        pages = chunk.Pages(open(d['canon_path'], encoding='utf-8').read())
        defs = []
        for pid, p in zip(ids, passages):
            for x in p['defs']:
                pg, pr, _ = pages.at(x['at'])
                defs.append((pid, d['key'], x['term'], x['norm'], x['kind'], x['conf'], x['evidence'], x['at'], pg, pr))
        cur.executemany(
            'insert into src.definitions (passage_id, doc_key, term, norm, kind, conf, evidence, at_off, page, printed) '
            'values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', defs)
    return len(defs)


def reconcile(conn, dry_run=False, log=print):
    """Bring the database to the inputs. Returns the run's counts."""
    t0 = time.time()
    docs, warnings = catalog.documents()
    csha = chunker_sha()
    have = {r[0]: r[1:] for r in conn.execute(
        'select key, text_fp, meta_fp, fidelity_fp, title from src.documents')}
    counts = dict(added=0, rechunked=0, metadata=0, fidelity=0, unchanged=0, removed=0, passages=0, definitions=0)
    run_id = None
    if not dry_run:
        run_id = conn.execute('insert into src.runs (chunker_sha) values (%s) returning id', (csha,)).fetchone()[0]
        conn.commit()
    for d in docs:
        text_fp = catalog.sha(d['text_sha'], csha) if d['has_text'] else None
        old = have.get(d['key'])
        if old is None:
            what = 'added'
        elif old[0] != text_fp or (old[1] != d['meta_fp'] and old[3] != d['title']):
            what = 'rechunked'
        elif old[1] != d['meta_fp']:
            what = 'metadata'
        elif old[2] != d['fidelity_fp']:
            what = 'fidelity'
        else:
            counts['unchanged'] += 1
            continue
        counts[what] += 1
        if dry_run:
            log(f'  would {dict(added="add", rechunked="re-chunk", metadata="update metadata of", fidelity="update fidelity of")[what]}: {d["key"]}')
            continue
        with conn.transaction():
            if what in ('added', 'rechunked') and d['has_text']:
                raw = open(d['canon_path'], encoding='utf-8').read()
                ps, hs = chunk.passages(raw)
                _upsert_doc(conn, _doc_row(d, text_fp, len(ps)))
                counts['definitions'] += _write_text(conn, d, ps, hs)
                counts['passages'] += len(ps)
            elif what in ('added', 'rechunked'):
                _upsert_doc(conn, _doc_row(d, text_fp, 0))
                conn.execute('delete from src.passages where doc_key = %s', (d['key'],))
                conn.execute('delete from src.headings where doc_key = %s', (d['key'],))
            else:
                n = conn.execute('select n_passages from src.documents where key = %s', (d['key'],)).fetchone()[0]
                _upsert_doc(conn, _doc_row(d, text_fp, n))
    gone = sorted(set(have) - {d['key'] for d in docs})
    counts['removed'] = len(gone)
    if gone and not dry_run:
        with conn.transaction():
            conn.execute('delete from src.documents where key = any(%s)', (gone,))
    for k in gone:
        log(f'  {"would remove" if dry_run else "removed"}: {k}')
    counts['seconds'] = round(time.time() - t0, 1)
    if not dry_run:
        with conn.transaction():
            conn.execute('update src.runs set finished = now(), counts = %s, warnings = %s where id = %s',
                         (json.dumps(counts), warnings, run_id))
    return counts, warnings
