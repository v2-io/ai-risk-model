"""Where a block of a canonical text defines a term (DESIGN §5.3).

Detection rests on structure as well as wording, and errs toward recall with a
confidence, because a false positive is visible in `--defs` (its evidence is
shown) and its pattern can then be fixed, while a miss is invisible.

What the pilot measured (influx/search-pilot-2026-10-09/REPORT.md §5), on which
these patterns were built and with which they should be re-checked:
- statutory definitions: all 68 of the AI Act's Art. 3 and all 18 of SB 53's,
  including the scoped "'subject', for the purpose of real-world testing, means";
- IASR 2026's glossary, which has no heading: 179 of 179 entries, as a run of
  `**Term:**` paragraphs in alphabetical order;
- the EU Code's glossary table, whose rows wrap across rows and pages;
- heading-based flags alone caught about a third of the judge's grade-3
  definitions; most of the rest were prose definitions, so prose patterns matter
  ("the notion of 'X'", "X scenarios are scenarios in which", "By 'X' … we mean").

Each detection is a dict: term (as written), kind, conf, evidence, and `at`, the
offset in the canonical file where the defining words start (for anchors).
"""
import re

from .text import clean, norm_term

QT = r'["“‘\']([^"”’\'\n]{2,80}?)["”’\']'

# (c) (1) "Catastrophic risk" means … ; (58) 'subject', for the purpose of real-world testing, means …
STAT_RE = re.compile(r'^\s*(?:[-*+]\s*)?(?:<span[^>]*>\s*</span>\s*)?(?:\(\w{1,4}\)\s*)+' + QT +
                     r'(?:,[^,\n]{1,90},)?\s+(?:means|shall mean|has the (?:same )?meaning|includes|is defined)\b')
# **Term:** text   and   **Term**: text
BOLD_LEAD_RE = re.compile(r'^\s*(?:[-*+]\s*(?:\(\w{1,4}\)\s*)?)?(?:\(\w{1,4}\)\s*)?\*\*([^*\n]{2,90}?)(?::\*\*|\*\*:)\s*\S')
# Labels that aren't terms: "Figure 2.1", "Box 2.6: AI companions", "Note", "Sources". Whole-label
# matches only: "Source code" is a term (IASR 2026's glossary has it).
PLAIN_LEAD_RE = re.compile(r'^\s*(?:[-*+]\s*)?([A-Z][\w ()/’\'&.-]{1,70}?):\s+\S')
NOT_A_TERM = re.compile(r'^(?:(?:figure|fig\.|table|box|exhibit|chart)\s*[\dA-Z]'
                        r'|(?:note|notes|claim|example|examples|source|sources|step|question|answer|recommendation|'
                        r'finding|summary|context|background|why|what|how|key)(?:\s+(?-i:[\dA-Z])[\w.-]*)?$)', re.I)

INLINE = [
    # By 'severe harm' in this document, we mean …  (OpenAI PF, footnote 1)
    ('inline-we-mean', 0.9, re.compile(r'\bby\s+' + QT + r',?\s+(?:(?:in|throughout) (?:this|the) [a-z]+,?\s+)?we (?:mean|refer to)\b', re.I)),
    ('inline-quoted', 0.8, re.compile(QT + r',?\s+(?:means|shall mean|refers to|is defined as|denotes|is used to mean|is understood as)\b', re.I)),
    # the notion of 'deployer' (AI Act recitals). "The term 'X'" and "the concept of 'X'" often
    # introduce a definition and sometimes only mention the word ("The term 'proceeding'"), so less sure.
    ('notion-of', 0.8, re.compile(r'\bthe notion of ' + QT, re.I)),
    ('term-of', 0.6, re.compile(r'\bthe (?:concept|term) (?:of )?' + QT, re.I)),
    ('inline-we-define', 0.8, re.compile(r'\bwe define\s+\*?["“‘\']?([A-Za-z][\w\s-]{1,50}?)["”’\']?\*?\s+(?:as|to mean|to refer to)\b', re.I)),
    # "we use X as" is usually not a definition ("We use topical classifiers … as"); with the
    # word quoted or named as a term, or with "to mean / to refer to", it is
    ('inline-we-use', 0.8, re.compile(r'\bwe use\s+(?:the (?:term|word|phrase)\s+\*?["“‘\']?([A-Za-z][\w\s-]{1,50}?)["”’\']?\*?\s+(?:as|to mean|to refer to|for)'
                                     r'|\*?["“‘\']([A-Za-z][\w\s-]{1,50}?)["”’\']\*?\s+(?:as|to mean|to refer to)'
                                     r'|([A-Za-z][\w\s-]{1,50}?)\s+(?:to mean|to refer to))\b', re.I)),
    ('inline-which-we-define', 0.8, re.compile(r'\*([A-Za-z][^*\n]{1,50})\*,?\s+(?:which|that) we define as', re.I)),
    ('inline-emph-refers', 0.7, re.compile(r'\*\*?([A-Za-z][^*\n]{1,50})\*?\*\s+(?:refers to|means|is defined as|denotes)\b', re.I)),
    ('inline-defined-as', 0.5, re.compile(r'\b(?:we )?defined?\s+([a-z][a-z -]{1,40}?)\s+as\s+(?:the|a|an|any)\b', re.I)),
]
# Loss of control scenarios are scenarios in which …; In this report, systemic risks are risks that …
REPEATED_HEAD = re.compile(r'(?:^|[.:;]\s+|\n|,\s+)(?:-\s*)?((?:[A-Za-z][\w-]*\s+){0,4}?([A-Za-z][\w-]*?)s?)\s+(?:is|are)\s+(?:an?\s+)?(\2s?)\b\s+(?:that|which|in which|where|when|whose)\b')
SKIP_LEAD = re.compile(r'^(?:by|in|a|an|the|these|this|that|its|their|our|such|other|some|any|all|each|it|they|we)\b', re.I)


def _ok_term(t):
    t = t.strip()
    return (2 <= len(t) <= 90 and len(t.split()) <= 8 and not t.endswith(',')
            and not SKIP_LEAD.match(t) and re.search(r'[A-Za-z]', t))


def detect(raw, block, section):
    """Definitions in one block. `block` has start, end, kind; section is its section kind."""
    out = []
    if block['kind'] not in ('item', 'para', 'restored'):
        return out
    first_end = raw.find('\n', block['start'], block['end'])
    first = raw[block['start']:first_end if first_end != -1 else block['end']]

    m = STAT_RE.match(first)
    if m:
        out.append(dict(term=m.group(1), kind='statutory-means', conf=0.95,
                        evidence='"X" means, in a lettered or numbered item', at=block['start'] + m.start(1) - 1))
    m = BOLD_LEAD_RE.match(first)
    if m and not NOT_A_TERM.match(m.group(1).strip()) and _ok_term(m.group(1)):
        block['bold_lead'] = re.sub(r'^[●•▪◦·]\s*', '', m.group(1).strip())
        block['bold_lead_at'] = block['start'] + m.start(1)
        block['numbered'] = bool(re.match(r'^\s*(?:[-*+]\s*)?\(\w{1,4}\)', first))
        if section == 'glossary' and not out:
            out.append(dict(term=block['bold_lead'], kind='glossary-entry', conf=0.9,
                            evidence='**Term:** in a glossary section', at=block['bold_lead_at']))

    # In a glossary section, "Term: definition" without bold: OCR loses the bold (AISI's
    # Frontier AI Trends Report: "Agent:", "Cyber range:", "Wet lab:").
    if section == 'glossary' and not out and 'bold_lead' not in block:
        m = PLAIN_LEAD_RE.match(first)
        if m and _ok_term(m.group(1)) and not NOT_A_TERM.match(m.group(1)):
            out.append(dict(term=m.group(1).strip(), kind='glossary-entry', conf=0.8,
                            evidence='Term: in a glossary section (not bold)', at=block['start'] + m.start(1)))

    body = clean(raw, block['start'], block['end'], emphasis=True)
    footnote = bool(re.match(r'\s*(?:<span[^>]*>\s*</span>\s*)?<sup>', raw[block['start']:block['start'] + 80]))
    seen = {norm_term(d['term']) for d in out}
    for kind, conf, rx in INLINE:
        for mm in rx.finditer(body.s):
            g = next(k for k in range(1, (rx.groups or 1) + 1) if mm.group(k))
            t = mm.group(g).strip().strip('*').strip()
            n = norm_term(t)
            if not _ok_term(t) or not n or n in seen:
                continue
            seen.add(n)
            out.append(dict(term=t, kind=('footnote-' + kind) if footnote else kind, conf=conf,
                            evidence=mm.group(0)[:90], at=body.span(mm.start(), mm.end())[0]))
    for mm in REPEATED_HEAD.finditer(body.s):
        t = re.sub(r'^(?:in this \w+\s+)', '', mm.group(1).strip(), flags=re.I)
        n = norm_term(t)
        if not _ok_term(t) or not n or n in seen or len(n.split()) < 2:
            continue
        seen.add(n)
        out.append(dict(term=t, kind='repeated-head', conf=0.7, evidence=mm.group(0).strip()[:90],
                        at=body.span(mm.start(1), mm.end(1))[0]))
    return out


def table_row(raw, cells_first, start, section):
    """A glossary table row: a quoted or bold term in its first cell, perhaps with a
    qualifier after it ("'process' (noun; in the context of systemic risk management)")."""
    if section != 'glossary':
        return []
    c = ' '.join(clean(cells_first).s.split())
    m = re.match(r'^["“‘\']?([^"”’\'|\n]{2,80}?)["”’\']?\s*(\([^)]{1,120}\))?$', c)
    if not m or not _ok_term(m.group(1)) or NOT_A_TERM.match(m.group(1)):
        return []
    quoted = bool(re.match(r'^(?:\*\*)?["“‘\']', cells_first.strip()))
    ev = 'term in the first cell of a glossary table' + (f', qualified {m.group(2)}' if m.group(2) else '')
    return [dict(term=m.group(1).strip(), kind='glossary-table-row', conf=0.9 if quoted else 0.75, evidence=ev, at=start)]


def elect_bold_runs(blocks, raw=None):
    """A glossary without a heading: a run of five or more `**Term:**` paragraphs in
    alphabetical order (IASR 2026's). A shorter or unordered run is a set of labelled
    items, such as a key-information box or a list of risks; its labels are recorded
    as weak definitions, a numbered one less weakly.

    A plain "Term: definition" paragraph between two bold ones belongs to their run:
    IASR's entry "Reinforcement learning with verifiable rewards (RLVR):" lost its
    bold, and so was filed under the heading before the glossary ("Conclusion › The
    value of shared understanding"), and the glossary split in two around it."""
    if raw is not None:
        for k in range(1, len(blocks) - 1):
            b = blocks[k]
            if (b.get('bold_lead') is None and b['kind'] in ('para', 'item')
                    and blocks[k - 1].get('bold_lead') is not None and blocks[k + 1].get('bold_lead') is not None):
                first = raw[b['start']:b['end']].split('\n', 1)[0]
                m = PLAIN_LEAD_RE.match(first)
                if m and _ok_term(m.group(1)) and not NOT_A_TERM.match(m.group(1)):
                    b['bold_lead'] = m.group(1).strip()
                    b['bold_lead_at'] = b['start'] + m.start(1)
                    b['plain_lead'] = True
                    b['path'] = blocks[k - 1]['path']
                    b['section'] = blocks[k - 1]['section']
    i = 0
    while i < len(blocks):
        if blocks[i].get('bold_lead') is None:
            i += 1
            continue
        j = i
        while j < len(blocks) and blocks[j].get('bold_lead') is not None:
            j += 1
        run = blocks[i:j]
        terms = [norm_term(b['bold_lead']) for b in run]
        asc = sum(1 for a, c in zip(terms, terms[1:]) if a <= c) / max(1, len(terms) - 1)
        if len(run) >= 5 and asc >= 0.85:
            for b in run:
                if b['section'] in ('body', 'annex', 'front'):
                    b['section'] = 'glossary'
                    b['path'] = b['path'][:1] + ['Glossary (no heading in the source)']
                if not any(d['kind'] == 'glossary-entry' for d in b['defs']):
                    b['defs'].insert(0, dict(term=b['bold_lead'], kind='glossary-entry', conf=0.85,
                                             evidence=f'alphabetical run of {len(run)} **Term:** paragraphs'
                                                      + (' (this one not bold)' if b.get('plain_lead') else ''),
                                             at=b['bold_lead_at']))
        elif len(run) >= 2:
            for b in run:
                if not any(norm_term(d['term']) == norm_term(b['bold_lead']) for d in b['defs']):
                    b['defs'].append(dict(term=b['bold_lead'], kind='bold-lead', conf=0.5 if b.get('numbered') else 0.35,
                                          evidence=f'a run of {len(run)} **Label:** paragraphs', at=b['bold_lead_at']))
        i = j
