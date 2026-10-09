"""A folded outline of documents for a query (search/DESIGN.md §12).

Joseph's idea, 2026-10-09: "looking for line ranges within documents that the agent
who uses it will want to look at most carefully and probably ingest. Like a very
smart index/ToC table", a document's outline with only the relevant branches
unfolded, down to line ranges. He called it the "aspectus-like (in spirit) ToC
contextual hybrid".

What it borrows from aspectus is its rule that a fold is never silent. Every
section of a document stays on the page. One that isn't opened is a single line
with what it holds (its line range, its passages, how many of them the ranking
found relevant), so a section the ranking misjudges is still visible, as a folded
line the reader can open. A ranked list would just leave it out.

How it is built:
- the tree is the passages' heading paths (src.passages.path), which are fuller
  than the headings table: a statute's "§22757.12" is a path element without a
  heading of its own;
- every passage in scope is scored by the hybrid ranking (rank.search: RRF of the
  semantic and lexical rankings, times the priors), and a verbatim copy gets its
  original's score;
- the passages are cut into tiers relative to the scope: "top" is the best 2%
  (at least 10), "near" the next, to 10% (at least 40). The rest count as no hit.
  The tiers are ranks, not a judgment of relevance: a query nothing in scope
  answers still has a top 2%. The outline says so when no passage holds any of the
  query's words, so every hit is by meaning alone (an off-topic query's nearest
  passages come about as close as a real query's: 2026-10-09, over all texts, the
  nearest passage to 15 off-topic queries was at cosine distance 0.405 or more,
  and the median pilot query's tenth-nearest at 0.401);
- passages are opened best first, each opening its ancestors (whose children
  then show, folded), until the output reaches its line budget, the way
  `aspectus --lines` works. Adjacent opened passages merge into one range;
- an opened section's subsections that hold no top passage are counted on its
  own line ("+9 sections not shown (5 near)") rather than given lines, and any
  lines left once the passages are chosen go back to naming them (QUIET below);
- each opened range carries both a line range in ref/canonical/KEY.md, for reading
  now, and the usual anchor (key, PDF page, quote), for citing. Line numbers change
  whenever bin/canonicalize rebuilds a file; the anchor doesn't.

The tier sizes and the heat thresholds are starting guesses; search/eval/outline-check
is how they get measured.
"""
import bisect, math

from . import anchor, rank

STRONG_SHARE, STRONG_MIN = 0.02, 10
WEAK_SHARE, WEAK_MIN = 0.10, 40
# A section's heat is the rank of its best passage among all passages in scope:
# in the top 1%, 2%, 5% or 10%. Ranks rather than scores, because RRF compresses
# scores differently for a one-word query and for a question.
HEAT = ((0.01, '█'), (0.02, '▓'), (0.05, '▒'), (0.10, '░'))
# Opening order: passages open in order of score / cost**COST_POWER, where cost is
# the lines opening one adds (its unopened ancestors' children, plus its own range
# line). 0 is plain score order. Measured on the pilot's grades (outline-check,
# 2026-10-09, with QUIET 'runs'): opened recall at 120 / 200 lines was 0.85 / 0.92
# at 0, 0.79 / 0.90 at 0.5, 0.67 / 0.88 at 1, 0.66 / 0.80 at 1.5. Valuing cheap
# passages opens neighbours of what is already open rather than what is best. I had
# set 0.5 from one example ("hazard" at 60 lines) before measuring.
COST_POWER = 0.0
GIVE_UP = 40                              # consecutive passages that didn't fit
# Where an opened section's folded subsections go:
# - 'runs': every one has a line, except that runs of two or more with no hits
#   share one;
# - 'census': those with no hits are counted on the section's own line, as aspectus
#   counts leftover files on their directory's line ([+ md×5]);
# - 'strong': so are those with only weak hits;
# - 'auto' (the default): passages are chosen under 'strong', then any lines left
#   over go back to structure, 'runs' if it fits, else 'census'.
# Measured on the pilot's grades (search/eval/outline-check, 2026-10-09), a
# subsection's own line is what the budget runs out on: opened recall at 60 lines
# was 0.32 under 'runs', 0.71 under 'census' and 0.90 under 'strong' (a ranked list
# in the same 60 lines: 0.72).
QUIET = 'auto'
TITLE_W = 72
QUOTE_W = 110


class Node:
    def __init__(self, path):
        self.path = path                  # tuple of heading titles
        self.children = []                # in document order; a title can recur (IASR's many "Key information" boxes)
        self.direct = []                  # passages whose path is exactly this node's
        self.head_off = None              # where its heading starts, when the headings table has it
        self.last_ord = -1
        self.parent = None

    @property
    def title(self):
        return self.path[-1] if self.path else ''

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()


def _load(conn, keys):
    if keys is None:
        keys = [r[0] for r in conn.execute('select key from src.documents where has_text order by key')]
    docs = {r[0]: dict(key=r[0], code=r[1], title=r[2], status=r[3], active_key=r[4], fidelity=r[5], ptc=r[6])
            for r in conn.execute('select key, code, title, status, active_key, fidelity_mark, pages_to_check '
                                  'from src.documents where key = any(%s) and has_text', (keys,))}
    ps = [dict(id=r[0], key=r[1], ord=r[2], start=r[3], end=r[4], page=r[5], page_last=r[6], printed=r[7],
               path=tuple(r[8] or ()), section=r[9], norm_sha=r[10])
          for r in conn.execute('select id, doc_key, ord, start_off, end_off, page, page_last, printed, path, section, norm_sha '
                                "from src.passages where doc_key = any(%s) and layer = 'canonical' order by doc_key, ord",
                                (list(docs),))]
    heads = {}
    for key, path, off in conn.execute('select doc_key, path, start_off from src.headings where doc_key = any(%s) '
                                       'order by start_off', (list(docs),)):
        heads.setdefault((key, tuple(path)), []).append(off)
    return docs, ps, heads


def _score(conn, query, keys, qvec, ps, model):
    """{passage id: (score, explain)} for every passage the hybrid ranking reached."""
    res, pq = rank.search(conn, query, n=10 ** 9, model=model, keys=keys, qvec=qvec)
    by_sha = {}
    out = {}
    for r, s, ex in res:
        out[r[0]] = (s, ex)
        by_sha.setdefault(r[11], (s, ex))
    for p in ps:                          # verbatim copies, collapsed by rank.search, take their original's score
        if p['id'] not in out and p['norm_sha'] in by_sha:
            s, ex = by_sha[p['norm_sha']]
            out[p['id']] = (s, dict(ex, copy_of=True))
    return out, pq


class Outline:
    def __init__(self, conn, query, keys=None, qvec=None, model='bge-m3', budget=200, quiet=None, answer=None):
        self.query, self.budget, self.answer = query, budget, answer
        self.mode = quiet or QUIET
        self.quiet = 'strong' if self.mode == 'auto' else self.mode
        self.docs, self.ps, heads = _load(conn, keys)
        self.scores, self.pq = _score(conn, query, keys, qvec, self.ps, model)
        self.by_id = {p['id']: p for p in self.ps}
        # tiers
        ranked = sorted((pid for pid in self.scores if pid in self.by_id), key=lambda i: -self.scores[i][0])
        N = len(self.ps)
        ns = max(STRONG_MIN, math.ceil(STRONG_SHARE * N))
        nw = max(WEAK_MIN, math.ceil(WEAK_SHARE * N))
        self.tier = {}
        for k, pid in enumerate(ranked[:nw]):
            self.tier[pid] = 'strong' if k < ns else 'weak'
        for pid in ranked:                # a definition of the queried term itself is always strong
            d = self.scores[pid][1].get('defines')
            if d and d.get('exact'):
                self.tier[pid] = 'strong'
        self.order = [pid for pid in ranked if pid in self.tier]
        self.lexical_hits = sum(1 for pid in ranked if self.scores[pid][1].get('lex_rank') is not None
                                and self.scores[pid][1].get('lexical'))
        self.rank_of = {pid: k + 1 for k, pid in enumerate(ranked)}
        # trees and line maps
        self.roots, self.nl, self.node_of = {}, {}, {}
        prev, cur = {}, {}
        for p in self.ps:
            key = p['key']
            root = self.roots.setdefault(key, Node(()))
            if p['section'] in ('restored', 'figure') and not p['path']:
                # text restored from the PDF's text layer, prose or figure, sits at the end
                # of its page's section and has no heading of its own (DESIGN §2): it goes
                # with the passage before it, and doesn't break that section's continuity
                cur.get(key, root).direct.append(p)
                self.node_of[p['id']] = cur.get(key, root)
                continue
            node = root
            for i in range(len(p['path'])):
                # continue the last child only: a heading path that recurs after
                # another section is a new section of the same name, not the old one
                t = p['path'][i]
                last = node.children[-1] if node.children else None
                if not (last and last.title == t and last.last_ord == prev.get(key)):
                    last = Node(p['path'][:i + 1])
                    # its heading is the last one with this path before its first passage
                    offs = [o for o in heads.get((key, p['path'][:i + 1]), ()) if o <= p['start']]
                    last.head_off = offs[-1] if offs else None
                    node.children.append(last)
                last.parent = node
                node = last
                node.last_ord = p['ord']
            node.direct.append(p)
            self.node_of[p['id']] = node
            prev[key], cur[key] = p['ord'], node
        for key in self.roots:
            raw = anchor.raw_of(key)
            self.nl[key] = [i for i, c in enumerate(raw) if c == '\n']
            self._stats(self.roots[key], key)
        self.sel = set()
        self._choose()
        if self.mode == 'auto':
            for q in ('runs', 'census'):
                self.quiet = q
                if self.count() <= self.budget:
                    break
            else:
                self.quiet = 'strong'

    # ---------------------------------------------------------------- numbers
    def line(self, key, off):
        return bisect.bisect_left(self.nl[key], off) + 1

    def _stats(self, n, key):
        ps = list(n.direct)
        for c in n.children:
            self._stats(c, key)
            ps.extend(c.all)
        n.all = ps
        n.key = key
        starts = [p['start'] for p in ps] + ([n.head_off] if n.head_off is not None else [])
        n.start, n.end = min(starts), max(p['end'] for p in ps)
        pages = [x for p in ps for x in (p['page'], p['page_last']) if x is not None]
        n.pages = (min(pages), max(pages)) if pages else (None, None)
        n.strong = sum(self.tier.get(p['id']) == 'strong' for p in ps)
        n.weak = sum(self.tier.get(p['id']) == 'weak' for p in ps)
        n.best = max((self.scores[p['id']][0] for p in ps if p['id'] in self.tier), default=0.0)
        n.best_rank = min((self.rank_of[p['id']] for p in ps if p['id'] in self.tier), default=None)

    def heat(self, best_rank):
        if not best_rank:
            return ' '
        share = best_rank / len(self.ps)
        return next((g for t, g in HEAT if share <= t), ' ')

    # --------------------------------------------------------------- choosing
    def _open(self, n):
        """A node is open when it holds a selected passage; a document's root is
        open when the document has any hit."""
        return any(p['id'] in self.sel for p in n.all) or (not n.path and (n.strong or n.weak))

    def _cost(self, pid):
        """About how many lines opening this passage adds."""
        n, c = self.node_of[pid], 1
        p = self.by_id[pid]
        if any(q['id'] in self.sel and abs(q['ord'] - p['ord']) == 1 for q in n.direct):
            c = 0                             # it joins a range already shown
        while n is not None and not self._open(n):
            if n not in self._width:
                self._width[n] = len(self._items(n))
            c += self._width[n]
            n = n.parent
        return max(c, 1)

    def _choose(self):
        """Open passages, the best value per line first, while the outline fits its
        line budget. A definition of the queried term itself goes first."""
        self._width = {}
        todo = set(self.order)
        firsts = [pid for pid in self.order
                  if (self.scores[pid][1].get('defines') or {}).get('exact')]
        misses = 0
        while todo and misses < GIVE_UP:
            if firsts:
                pid = firsts.pop(0)
            else:
                pid = max(todo, key=lambda i: self.scores[i][0] / self._cost(i) ** COST_POWER)
            todo.discard(pid)
            self.sel.add(pid)
            if self.count() > self.budget:
                self.sel.discard(pid)
                misses += 1
            else:
                misses = 0

    def count(self):
        return len(self.render(lines_only=True))

    # -------------------------------------------------------------- rendering
    def _items(self, n):
        """The open node's children in document order: child nodes, ranges of its
        selected passages (adjacent ones merged), and runs of hitless folded
        sections folded together."""
        items = [('node', c.start, c) for c in n.children]
        run = []
        for p in n.direct:
            if p['id'] in self.sel:
                if run and run[-1]['ord'] == p['ord'] - 1:
                    run.append(p)
                else:
                    if run:
                        items.append(('range', run[0]['start'], run))
                    run = [p]
        if run:
            items.append(('range', run[0]['start'], run))
        items.sort(key=lambda x: x[1])
        if self.quiet in ('census', 'strong'):
            return [it for it in items if not (it[0] == 'node' and self._quiet(it[2]))]
        out, quiet = [], []
        for it in items + [None]:
            if it and it[0] == 'node' and self._hitless(it[2]):
                quiet.append(it[2])
                continue
            if len(quiet) >= 2:
                out.append(('quiet', quiet[0].start, quiet))
            elif quiet:
                out.append(('node', quiet[0].start, quiet[0]))
            quiet = []
            if it:
                out.append(it)
        return out

    def _hitless(self, n):
        return not self._open(n) and not (n.strong or n.weak)

    def _quiet(self, n):
        """Folded into its parent's census rather than given a line: in 'census' mode a
        folded section with no hits, in 'strong' mode one with no strong hit."""
        return not self._open(n) and not n.strong and (self.quiet == 'strong' or not n.weak)

    def render(self, lines_only=False):
        out = []
        hits = [k for k in self.roots if self.roots[k].strong or self.roots[k].weak]
        none = [k for k in self.roots if k not in hits]
        hits.sort(key=lambda k: -self.roots[k].best)
        out.append(dict(kind='top'))
        for k in hits:
            self._doc(k, out, lines_only)
        if none:
            out.append(dict(kind='nohits', keys=sorted(none)))
        return out

    def _doc(self, key, out, lines_only):
        root = self.roots[key]
        out.append(dict(kind='doc', key=key, node=root))
        if self._open(root):
            self._children(root, '', out, lines_only)

    def _children(self, n, prefix, out, lines_only):
        items = self._items(n)
        for i, (kind, _, x) in enumerate(items):
            last = i == len(items) - 1
            conn = '└── ' if last else '├── '
            ext = '    ' if last else '│   '
            if kind == 'node':
                out.append(dict(kind='node', node=x, prefix=prefix + conn, open=self._open(x)))
                if self._open(x):
                    self._children(x, prefix + ext, out, lines_only)
            elif kind == 'quiet':
                out.append(dict(kind='quiet', nodes=x, prefix=prefix + conn))
            else:
                r = dict(kind='range', passages=x, prefix=prefix + conn)
                if not lines_only:
                    r['anchor'] = self._anchor(x)
                out.append(r)

    def _anchor(self, ps):
        best = max(ps, key=lambda p: self.scores[p['id']][0])
        d = self.docs[best['key']]
        ex = self.scores[best['id']][1]
        at = ex['defines']['at'] if ex.get('defines') else None
        return anchor.make(best['key'], best['start'], best['end'], self.pq['words'], at=at,
                           fidelity=d['fidelity'], pages_to_check=d['ptc'])

    # ------------------------------------------------------------------- text
    def text(self, rows=None):
        rows = rows or self.render()
        shown = sum(1 for r in rows if r['kind'] == 'range')
        lines = []
        for r in rows:
            k = r['kind']
            if k == 'top':
                lines.append(self._top_line(shown, len(rows)))
            elif k == 'doc':
                lines.append(self._doc_line(r['node']))
            elif k == 'node':
                lines.append(self._node_line(r))
            elif k == 'quiet':
                ns = r['nodes']
                a, b = self.line(ns[0].key, ns[0].start), self.line(ns[0].key, max(n.end for n in ns) - 1)
                lines.append(f"  {r['prefix']}⋯ {len(ns)} sections with no hits, L{a}–{b}, "
                             f"{sum(len(n.all) for n in ns)} passages")
            elif k == 'range':
                lines.append(self._range_line(r))
            else:
                ks = r['keys']
                lines.append(f"{len(ks)} document{'s' if len(ks) != 1 else ''} in scope with no hits: "
                             + ', '.join(ks[:8]) + (f', and {len(ks) - 8} more' if len(ks) > 8 else ''))
        return '\n'.join(lines)

    def _top_line(self, shown, n):
        s = (f'"{self.query}": {len(self.roots)} document{"s" if len(self.roots) != 1 else ""}, '
             f'{len(self.ps)} passages; {shown} ranges opened in {n} of {self.budget} lines (L = lines of '
             f'ref/canonical/KEY.md). "top": among the best 2% of passages in scope; "near": the next, to 10%. '
             f'█▓▒░: a section\'s best passage is in the best 1%, 2%, 5% or 10%.')
        if self.tier and not self.sel:
            s += (f'\nThe budget of {self.budget} lines is too small to open anything: the outline\'s skeleton alone '
                  f'takes {n}. About {self.lines_to_open_best()} would open the best passage (--lines).')
        a = self.answer
        if a and a.get('likely_unanswered'):
            # rank.answerability: a cue, not a gate (weights.toml [answerable])
            s += (f"\nNothing in scope seems to answer this: no passage holds all of the query's words, and the "
                  f"nearest passage by meaning is at cosine distance {a['nearest_distance']} (off-topic test queries "
                  f"fell at {a['threshold']} or more). What follows is the nearest material, ranked relative to itself.")
        elif not self.lexical_hits:
            s += ('\nNo passage in scope holds any of the query\'s words, so every hit is by meaning alone, and '
                  'the ranks are relative: an off-topic query gets a top 2% too.')
        return s

    def lines_to_open_best(self):
        """How many lines the outline would take with its best passage opened: the
        budget to ask for when the skeleton alone has used it up."""
        if not self.order:
            return None
        keep = set(self.sel)
        self.sel.add(self.order[0])
        try:
            return self.count()
        finally:
            self.sel = keep

    def _doc_line(self, n):
        d = self.docs[n.key]
        st = '' if d['status'] == 'active' else f"  [{d['status']}" + (f", active {d['active_key']}]" if d['active_key'] else ']')
        q = [c for c in n.children if self._quiet(c)] if self.quiet in ('census', 'strong') and self._open(n) else []
        qs = (f" · +{len(q)} section{'s' if len(q) != 1 else ''} not shown"
              + (f" ({sum(c.weak for c in q)} near)" if any(c.weak for c in q) else ' (no hits)')) if q else ''
        return (f"{self.heat(n.best_rank)} {n.key}  {d['code'] or ''}  {len(self.nl[n.key]) + 1} lines · {len(n.all)} passages"
                f" · {n.strong} top · {n.weak} near{qs}{st}")

    def _census(self, n, open_):
        bits = [f'{len(n.all)} passage{"s" if len(n.all) != 1 else ""}']
        if n.strong:
            bits.append(f'{n.strong} top')
        if n.weak:
            bits.append(f'{n.weak} near')
        if open_:
            hidden = sum(1 for p in n.direct if p['id'] not in self.sel)
            if hidden and n.children or hidden and any(p['id'] in self.sel for p in n.direct):
                bits.append(f'+{hidden} of its own not shown')
            if self.quiet in ('census', 'strong'):
                q = [c for c in n.children if self._quiet(c)]
                qw = sum(c.weak for c in q)
                if q:
                    bits.append(f'+{len(q)} section{"s" if len(q) != 1 else ""} not shown'
                                + (f' ({qw} near)' if qw else ' (no hits)'))
        return '[' + ' · '.join(bits) + ']'

    def _node_line(self, r):
        n = r['node']
        a, b = self.line(n.key, n.start), self.line(n.key, n.end - 1)
        t = n.title if len(n.title) <= TITLE_W else n.title[:TITLE_W - 1] + '…'
        pg = f'p.{n.pages[0]}' + (f'–{n.pages[1]}' if n.pages[1] != n.pages[0] else '') if n.pages[0] is not None else ''
        return f"{self.heat(n.best_rank)} {r['prefix']}{t}  L{a}–{b} {pg}  {self._census(n, r['open'])}"

    def _range_line(self, r):
        ps = r['passages']
        key = ps[0]['key']
        a, b = self.line(key, ps[0]['start']), self.line(key, ps[-1]['end'] - 1)
        best = min((self.rank_of[p['id']] for p in ps if p['id'] in self.rank_of), default=None)
        an = r['anchor']
        tags = []
        for p in ps:
            d = self.scores[p['id']][1].get('defines')
            if d:
                tags.append(f"defines {d['term']!r}")
                break
        if any(p['section'] not in ('body', 'restored') for p in ps):
            tags.append('/'.join(sorted({p['section'] for p in ps})))
        # cut short, the quote stays verbatim inside the marks and the '…' goes outside
        # them: inside, bin/check-quote would read it as a gap in the quote
        q, cut = (an['quote'], '') if len(an['quote']) <= QUOTE_W else (an['quote'][:QUOTE_W - 1].rstrip(), '…')
        pr = f' ("{an["printed"]}")' if an.get('printed') else ''
        label = an.get('page_label') or ('not in the PDF' if an.get('not_in_pdf') else
                                         'page not yet confirmed' if an.get('check_pdf') else None)
        flag = f' [{label}]' if label else ''
        return (f"{self.heat(best)} {r['prefix']}▸ L{a}–{b}  p.{an['page']}{pr}{flag}"
                + (f"  {'; '.join(tags)}" if tags else '') + f'  {anchor.show_quote(q)}{cut}')

    # ------------------------------------------------------------------- json
    def as_json(self, rows=None):
        rows = rows or self.render()
        docs, stack = [], []
        for r in rows:
            k = r['kind']
            if k == 'doc':
                n = r['node']
                docs.append(dict(self._node_json(n, True), key=n.key, code=self.docs[n.key]['code'],
                                 status=self.docs[n.key]['status'], lines_total=len(self.nl[n.key]) + 1, items=[]))
                stack = [(0, docs[-1])]
            elif k in ('node', 'quiet', 'range'):
                depth = len(r['prefix']) // 4
                while stack and stack[-1][0] >= depth + 1:
                    stack.pop()
                parent = stack[-1][1]
                if k == 'node':
                    item = dict(self._node_json(r['node'], r['open']), items=[])
                    parent['items'].append(item)
                    stack.append((depth + 1, item))
                elif k == 'quiet':
                    ns = r['nodes']
                    parent['items'].append(dict(folded_sections=[n.title for n in ns],
                                                lines=[self.line(ns[0].key, ns[0].start), self.line(ns[0].key, max(n.end for n in ns) - 1)],
                                                passages=sum(len(n.all) for n in ns)))
                else:
                    ps = r['passages']
                    key = ps[0]['key']
                    parent['items'].append(dict(
                        lines=[self.line(key, ps[0]['start']), self.line(key, ps[-1]['end'] - 1)],
                        pages=[ps[0]['page'], ps[-1]['page_last']], passages=[f"{key}#{p['ord']}" for p in ps],
                        score=round(max(self.scores[p['id']][0] for p in ps), 6),
                        tier=sorted({dict(strong='top', weak='near')[self.tier[p['id']]] for p in ps if p['id'] in self.tier}),
                        defines=next((self.scores[p['id']][1]['defines'] for p in ps if self.scores[p['id']][1].get('defines')), None),
                        anchor=r['anchor']))
        none = next((r['keys'] for r in rows if r['kind'] == 'nohits'), [])
        too_small = bool(self.tier) and not self.sel
        return dict(query=self.query, term=self.pq['term'], budget=self.budget, lines_used=len(rows),
                    hits=len(self.tier), budget_too_small=too_small,
                    lines_to_open_best=self.lines_to_open_best() if too_small else None,
                    tiers=dict(top='among the best 2% of passages in scope', near='the next, to 10%'),
                    answerability=self.answer,
                    passages_with_query_words=self.lexical_hits, documents=docs, no_hits=none)

    def _node_json(self, n, open_):
        return dict(path=list(n.path), lines=[self.line(n.key, n.start), self.line(n.key, n.end - 1)],
                    pages=list(n.pages), passages=len(n.all), top=n.strong, near=n.weak,
                    best=round(n.best, 6), open=bool(open_))

    def opened(self):
        """The passages shown in opened ranges, as (key, ord): what an agent reading
        the outline's ranges would read. For search/eval/outline-check."""
        return {(self.by_id[i]['key'], self.by_id[i]['ord']) for i in self.sel}

    def opened_lines(self):
        """How many lines of source the opened ranges cover."""
        tot = 0
        for r in self.render(lines_only=True):
            if r['kind'] == 'range':
                ps = r['passages']
                tot += self.line(ps[0]['key'], ps[-1]['end'] - 1) - self.line(ps[0]['key'], ps[0]['start']) + 1
        return tot
