"""The documents to index, and what the index needs to know about each.

The catalog decides what is indexed, not the directory: a key that leaves the
catalog keeps its old canonical text on disk (DESIGN §2). Every catalog key is a
document; `subsumed-by` keys (copies of another key's text) and keys without a
canonical text carry metadata only. `superseded-by` keys are indexed and marked
inactive, with the active version their chain ends at.

Metadata comes from three places: the catalog (section, Code, Influence, Date and
Kind from the main table; the family heading and group label from *The rest of
the corpus*), bib/refs.bib (title, authors, year, URL), and the canonical text's
pages.json (its fidelity mark).
"""
import hashlib, json, os, re

from . import CANON, REPO
import corpus

BIB = os.path.join(REPO, 'bib', 'refs.bib')


# ------------------------------------------------------------------ the catalog
def _main_table_rows(path):
    """{key: {column: cell}} for the keys in the main table, read by header name
    (corpus.read_catalog takes only the Code)."""
    out, header = {}, None
    for line in open(path, encoding='utf-8'):
        if line.startswith('## ') and header:
            break                                  # the main table ends at the next section
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.rstrip('\n').strip().strip('|').split('|')]
        if header is None:
            if 'relata' in cells and 'Influence' in cells:
                header = cells
            continue
        if set(''.join(cells)) <= set('-: '):
            continue
        row = dict(zip(header, cells))
        for m in corpus.CAT_ITEM.finditer(row.get('relata', '')):
            out.setdefault(m.group('key'), row)
    return out


def _corpus_groups(path):
    """{key: group label} for keys listed under a bold label in *The rest of the corpus*
    ("- **Anthropic (with Karnofsky's post on RSP v3)** (7): `@…`")."""
    out = {}
    for line in open(path, encoding='utf-8'):
        m = re.match(r'^- \*\*(.+?)\*\*', line)
        if not m:
            continue
        for k in corpus.CAT_ITEM.finditer(line):
            out.setdefault(k.group('key'), m.group(1).strip())
    return out


# ------------------------------------------------------------------------ bib
def _bib_entries(path=BIB):
    """{key: (fields, entry text)} from refs.bib. Values are brace- or quote-delimited;
    braces nest. Enough for relata's output, not a general BibTeX parser."""
    text = open(path, encoding='utf-8').read()
    out = {}
    for m in re.finditer(r'^@(\w+)\{([^,\s]+),', text, re.M):
        i, depth = m.end(), 1
        while i < len(text) and depth:
            depth += {'{': 1, '}': -1}.get(text[i], 0)
            i += 1
        body = text[m.end():i - 1]
        fields, j = {'_type': m.group(1).lower()}, 0
        for f in re.finditer(r'(\w+)\s*=\s*', body):
            if f.start() < j:
                continue
            k, j = f.group(1).lower(), f.end()
            if j < len(body) and body[j] == '{':
                d, s = 0, j
                while j < len(body):
                    d += {'{': 1, '}': -1}.get(body[j], 0)
                    j += 1
                    if d == 0:
                        break
                fields[k] = body[s + 1:j - 1]
            elif j < len(body) and body[j] == '"':
                e = body.index('"', j + 1)
                fields[k] = body[j + 1:e]; j = e + 1
            else:
                e = re.search(r'[,\n]', body[j:])
                fields[k] = body[j:j + e.start()] if e else body[j:]; j += e.start() if e else len(body)
        out[m.group(2)] = (fields, text[m.start():i])
    return out


def _unbrace(s):
    s = re.sub(r'\\([&%$#_])', r'\1', s or '')          # LaTeX escapes: NIST CAISI's "\&"
    return re.sub(r'\s+', ' ', re.sub(r'[{}]', '', s)).strip() or None


def _org(fields):
    """The authoring organisation, where the bib names one ({{OpenAI}}), else the
    first author's surname. Recency is measured within it (DESIGN §6.2)."""
    a = fields.get('author') or fields.get('editor') or ''
    m = re.match(r'\s*\{([^{}]+)\}', a)
    if m:
        return _unbrace(m.group(1))
    first = a.split(' and ')[0].strip()
    return _unbrace(first.split(',')[0]) if first else None


# ------------------------------------------------------------------ documents
def sha(*parts):
    h = hashlib.sha256()
    for p in parts:
        h.update(p if isinstance(p, bytes) else str(p).encode('utf-8'))
        h.update(b'\0')
    return h.hexdigest()


def documents():
    """(docs, warnings): one dict per catalog key, in catalog order."""
    order, entries, errors = corpus.read_catalog()
    warnings = [f'catalog: {e}' for e in errors]
    table = _main_table_rows(corpus.CATALOG)
    groups = _corpus_groups(corpus.CATALOG)
    bib = _bib_entries() if os.path.exists(BIB) else {}
    if not bib:
        warnings.append('bib/refs.bib missing: titles and authors are empty (run `relata emit bib`)')
    docs, no_text = [], []
    for key in order:
        e = entries[key]
        tags = e['tags']
        row = table.get(key, {})
        fields, bibtext = bib.get(key, ({}, ''))
        if bib and not fields:
            warnings.append(f'{key}: not in bib/refs.bib')
        canon = os.path.join(CANON, key + '.md')
        has_text = corpus.in_scope(e) and os.path.exists(canon)
        if corpus.in_scope(e) and not os.path.exists(canon):
            no_text.append(key)
        pages_json = os.path.join(CANON, 'msc', key, 'pages.json')
        fidelity = None
        if has_text and os.path.exists(pages_json):
            fidelity = json.load(open(pages_json, encoding='utf-8')).get('fidelity')
        status = ('subsumed' if 'subsumed-by' in tags else
                  'superseded' if 'superseded-by' in tags else 'active')
        year = fields.get('year')
        d = dict(
            key=key, status=status, active_key=e['active'],
            subsumed_by=tags.get('subsumed-by'), no_canon=tags.get('no-canon'),
            has_text=has_text, canon_path=canon if has_text else None,
            section=e['section'], code=row.get('Code') or e['code'] or None, group_label=groups.get(key),
            influence=(row.get('Influence') or ('corpus' if key not in table else None)),
            cat_date=row.get('Date'), cat_kind=row.get('Kind'), cat_document=row.get('Document'),
            title=_unbrace(fields.get('title')), authors=_unbrace(fields.get('author') or fields.get('editor')),
            org=_org(fields), year=int(year) if year and year.isdigit() else None,
            url=fields.get('url'), bib_type=fields.get('_type'),
            fidelity_mark=(fidelity or {}).get('mark'),
            pages_to_check=(fidelity or {}).get('pages_to_check') or [],
        )
        catrow = {k: d[k] for k in ('status', 'active_key', 'subsumed_by', 'no_canon', 'section', 'code',
                                    'group_label', 'influence', 'cat_date', 'cat_kind', 'cat_document')}
        d['meta_fp'] = sha(bibtext, json.dumps(catrow, sort_keys=True))
        d['fidelity_fp'] = sha(json.dumps(fidelity, sort_keys=True)) if fidelity else None
        d['text_sha'] = sha(open(canon, 'rb').read()) if has_text else None
        docs.append(d)
    if no_text:
        # mostly relata's conversion queue; ref/canonical/skipped.json says why each is missing
        warnings.append(f'{len(no_text)} keys in scope have no canonical text yet (ref/canonical/skipped.json)')
    return docs, warnings
