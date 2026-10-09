"""Scopes: which documents a search covers (search/DESIGN.md §7.2).

A scope is a list of selectors, given after the query on the command line or in a
named set (`catalog/sets/NAME.yaml`). Selectors, unioned:
- a relata key:                    california-2025-sb53
- a key glob:                      'anthropic-*'
- a set:                           Au5   (or set:Au5)
- a catalog field:                 org:anthropic   influence:anchor,major   year:2025..2026
- several fields that must all hold, joined by '+':   org:anthropic+influence:major

Fields, from the catalog as the index holds it (src.documents):
  key, code, org, section, group, influence, status, kind, year, title.
Text fields match a case-insensitive substring; key, code, influence and status
match whole values (case-insensitive; a code ignores spaces); a value list
separated by commas matches any of them. year takes N, N..M, >=N or <=N.

A set file:
    description: one line on what the set is for and who named it
    select: [selectors]
    exclude: [selectors]          # optional

A set name that is also a key is an error, as is a selector that matches nothing.
"""
import fnmatch, glob, os, re

import yaml

from . import REPO

SETS_DIR = os.path.join(REPO, 'catalog', 'sets')
FIELDS = dict(key='key', code='code', org='org', section='section', group='group_label', influence='influence',
              status='status', kind='cat_kind', year='year', title='title')
WHOLE = {'key', 'code', 'influence', 'status'}


class ScopeError(Exception):
    pass


def documents(conn):
    cols = ['key'] + [c for f, c in FIELDS.items() if f != 'key'] + ['has_text']
    rows = conn.execute(f"select {', '.join(cols)} from src.documents").fetchall()
    return [dict(zip(cols, r)) for r in rows]


def load_sets(keys=()):
    """{name: dict(description, select, exclude, path)} from catalog/sets/."""
    out, lower_keys = {}, {k.lower() for k in keys}
    for p in sorted(glob.glob(os.path.join(SETS_DIR, '*.yaml'))):
        name = os.path.splitext(os.path.basename(p))[0]
        if name.lower() in lower_keys:
            raise ScopeError(f'set {name!r} ({p}) has the same name as a relata key; rename the set')
        if re.search(r'[:*?+,]', name):
            raise ScopeError(f'set {name!r} ({p}): a set name cannot hold ":", "*", "?", "+" or ","')
        d = yaml.safe_load(open(p, encoding='utf-8')) or {}
        out[name] = dict(description=d.get('description', ''), select=list(d.get('select') or []),
                         exclude=list(d.get('exclude') or []), path=os.path.relpath(p, REPO))
    return out


def _norm_code(s):
    return re.sub(r'\s+', '', s or '').lower()


def _year_ok(y, v):
    if y is None:
        return False
    m = re.fullmatch(r'(\d{4})\.\.(\d{4})', v)
    if m:
        return int(m[1]) <= y <= int(m[2])
    m = re.fullmatch(r'(>=|<=|>|<)?(\d{4})', v)
    if not m:
        raise ScopeError(f'year:{v} — use N, N..M, >=N or <=N')
    op, n = m[1] or '=', int(m[2])
    return dict(zip(('=', '>=', '<=', '>', '<'), (y == n, y >= n, y <= n, y > n, y < n)))[op]


def _field_ok(doc, field, values):
    col = FIELDS[field]
    v = doc.get(col)
    for val in values:
        if field == 'year':
            if _year_ok(v, val):
                return True
        elif field == 'code':
            if v and _norm_code(v) == _norm_code(val):
                return True
        elif field in WHOLE:
            if v and str(v).lower() == val.lower():
                return True
        elif v and val.lower() in str(v).lower():
            return True
    return False


def _select(sel, docs, sets, seen):
    """The keys one selector picks out."""
    sel = sel.strip()
    if sel.startswith('set:'):
        return _set_keys(sel[4:], docs, sets, seen)
    if ':' in sel:
        parts = sel.split('+')
        conds = []
        for part in parts:
            field, _, vals = part.partition(':')
            field = field.strip().lower()
            if field not in FIELDS:
                raise ScopeError(f'{sel!r}: no field {field!r}; fields are {", ".join(FIELDS)}')
            conds.append((field, [x.strip() for x in vals.split(',') if x.strip()]))
        return {d['key'] for d in docs if all(_field_ok(d, f, vs) for f, vs in conds)}
    if any(c in sel for c in '*?['):
        return {d['key'] for d in docs if fnmatch.fnmatchcase(d['key'], sel)}
    by_key = {d['key'] for d in docs}
    if sel in by_key:
        return {sel}
    hit = [n for n in sets if n.lower() == sel.lower()]
    if hit:
        return _set_keys(hit[0], docs, sets, seen)
    return set()


def _set_keys(name, docs, sets, seen):
    hit = [n for n in sets if n.lower() == name.lower()]
    if not hit:
        raise ScopeError(f'no set {name!r}; sets: {", ".join(sorted(sets)) or "none"} (catalog/sets/)')
    name = hit[0]
    if name in seen:
        raise ScopeError(f'set {name!r} includes itself (through {" → ".join(seen)})')
    s = sets[name]
    seen = seen + [name]
    keys = set()
    for sel in s['select']:
        got = _select(str(sel), docs, sets, seen)
        if not got:
            raise ScopeError(f'set {name!r} ({s["path"]}): {sel!r} matches no document in the index')
        keys |= got
    for sel in s['exclude']:
        keys -= _select(str(sel), docs, sets, seen)
    return keys


def resolve(conn, specs):
    """Sorted keys the scope selects, or None for no scope (everything indexed)."""
    if not specs:
        return None
    docs = documents(conn)
    sets = load_sets(d['key'] for d in docs)
    keys = set()
    for sel in specs:
        got = _select(sel, docs, sets, [])
        if not got:
            raise ScopeError(f'{sel!r} matches no document: not a relata key in the index, a key glob, '
                             f'a set ({", ".join(sorted(sets)) or "none defined"}) or a field selector (field:value)')
        keys |= got
    return sorted(keys)


def describe(conn):
    """For `source-search help scopes`: the sets, and each field's values with counts."""
    docs = documents(conn)
    sets = load_sets(d['key'] for d in docs)
    out = dict(sets={}, fields={})
    for n, s in sets.items():
        try:
            k = _set_keys(n, docs, sets, [])
            out['sets'][n] = dict(description=s['description'], documents=len(k), path=s['path'])
        except ScopeError as e:
            out['sets'][n] = dict(description=s['description'], error=str(e), path=s['path'])
    for f in ('influence', 'status', 'section', 'group'):
        counts = {}
        for d in docs:
            v = d.get(FIELDS[f])
            if v:
                counts[v] = counts.get(v, 0) + 1
        out['fields'][f] = dict(sorted(counts.items(), key=lambda x: -x[1]))
    return out
