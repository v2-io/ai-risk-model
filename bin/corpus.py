"""The two contracts the repo's source tools share, so they can't disagree.

1. The catalog: which documents are listed, and each one's status.
   `source-catalog.md` lists a document with `@key`; status tags follow the
   key's closing backtick. The parsing contract is
   influx/catalog-update-proposal-2026-10-08.md §2. read_catalog() reads it
   and checks its rules; in_scope() says whether a key is canonicalized.

2. The canonical text's format, as bin/canonicalize writes ref/canonical/KEY.md:
   a marker line where each physical PDF page begins (MARK, or MARK_PRINTED
   when the page's printed number is established), NOT_IN_PDF before text
   that matches nothing in the PDF, and text restored from the PDF's text
   layer fenced between SUPP_OPEN and SUPP_CLOSE. MARK_RE matches a marker
   line: group 1 is the physical page (None for not-in-pdf), group 2 the
   printed label (None if not established).

Used by bin/canonicalize; meant to be imported by any other tool that reads
the catalog or the canonical texts (sys.path.insert(0, <repo>/bin); import corpus).
"""
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(REPO, 'source-catalog.md')

# ----------------------------------------------------- the canonical text
MARK = '----------[pdf-page {}]----------'
MARK_PRINTED = '----------[pdf-page {}, printed "{}"]----------'
NOT_IN_PDF = '----------[not in pdf]----------'
MARK_RE = re.compile(r'^----------\[(?:pdf-page (\d+)(?:, printed "([^"]*)")?|not in pdf)\]----------$')
SUPP_OPEN, SUPP_CLOSE = '```pdf-text', '```'
SUPP_RE = re.compile(r'\n*^```pdf-text\n.*?\n```$\n*', re.S | re.M)

# --------------------------------------------------------------- the catalog
#
# The parsing contract is influx/catalog-update-proposal-2026-10-08.md §2: any
# `@key` in source-catalog.md lists that document; status tags follow the key's
# closing backtick.

CAT_KEY = r'[A-Za-z0-9_](?:[\w:.#$%&+?<>~/-]*[\w])?'
CAT_TAG = r'\[(?:no-canon|subsumed-by|superseded-by|canon-text):[^\]\n]*\]'
CAT_ITEM = re.compile(r'(?<![\w@])@(?P<key>' + CAT_KEY + r')`?(?P<tags>(?:[ \t]*' + CAT_TAG + r')*)')
CAT_TAGS = re.compile(r'\[(?P<status>no-canon|subsumed-by|superseded-by|canon-text):[ \t]*(?P<arg>[^\]\n]*)\]')

def read_catalog(path=None):
    """(keys in order of first listing, {key: entry}, errors). An entry has
    the catalog section it is first listed under, its Code if it is in the main
    table, its tags, and for an earlier version the active one its chain ends at."""
    text = open(path or CATALOG, encoding='utf-8').read()
    order, entries, errors = [], {}, []
    section = 'Main sources'
    for line in text.split('\n'):
        if line.startswith('## ') or line.startswith('### '):
            section = line.lstrip('#').strip()
            continue
        code = None
        if line.startswith('|'):
            cells = [c.strip() for c in line.split('|')]
            if len(cells) > 3 and cells[2] not in ('Code', '---'):
                code = cells[2]
        for m in CAT_ITEM.finditer(line):
            key, tags = m.group('key'), {}
            for t in CAT_TAGS.finditer(m.group('tags')):
                st, arg = t.group('status'), t.group('arg').strip()
                if st in ('subsumed-by', 'superseded-by'):
                    arg = arg.lstrip('@').strip().strip('`')
                if st in tags and tags[st] != arg:
                    errors.append(f'{key}: two [{st}] tags')
                tags[st] = arg
            if key not in entries:
                entries[key] = dict(key=key, section=section, code=code, tags=tags)
                order.append(key)
            elif tags:
                if entries[key]['tags'] and entries[key]['tags'] != tags:
                    errors.append(f'{key}: tagged differently in two places')
                entries[key]['tags'] = entries[key]['tags'] or tags
    for key, e in entries.items():
        t = e['tags']
        if 'subsumed-by' in t and len(t) > 1:
            errors.append(f'{key}: subsumed-by stands alone, but has {sorted(t)}')
        if 'canon-text' in t and 'no-canon' in t:
            errors.append(f'{key}: canon-text and no-canon contradict each other')
        for st in ('subsumed-by', 'superseded-by'):
            if st in t and t[st] not in entries:
                errors.append(f'{key}: [{st}: @{t[st]}] names a key the catalog does not list')
        if 'subsumed-by' in t and 'subsumed-by' in entries.get(t['subsumed-by'], {}).get('tags', {}):
            errors.append(f'{key}: subsumed-by @{t["subsumed-by"]}, which is itself subsumed')
        seen, cur = [key], key
        while 'superseded-by' in entries.get(cur, {}).get('tags', {}):
            cur = entries[cur]['tags']['superseded-by']
            if cur in seen:
                errors.append(f'{key}: superseded-by chain loops ({" → ".join(seen + [cur])})')
                break
            seen.append(cur)
        e['active'] = cur if cur != key else None
    return order, entries, errors

def in_scope(e):
    return not ({'no-canon', 'subsumed-by'} & set(e['tags']))

