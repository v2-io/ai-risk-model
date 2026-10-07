#!/usr/bin/env python3
"""Check the thin pass's records against the source extractions.

    python3 -I tools/check.py [--extract-dir DIR]        check every record
    python3 -I tools/check.py --locate KEY "some quote"  print page/line/match count

Extractions are `pdftotext -layout` text, one file per relata key, as
`bin/extract-text KEY...` writes them (default: the repo's .extract/).

For each passage in records/passages.yaml it checks that:
  - the quote occurs inside the recorded line range (after normalization);
  - the recorded page equals the page of the range's first line (form feeds + 1);
and it reports the quote's match count in the whole document. An anchor
intends exactly one match (plan §3.5); more than one is reported, not hidden.

It also checks that every passage id, record id and `thin:` term used anywhere
in records/*.yaml is defined. Disposable, like everything in this directory.
"""
import re
import sys
import pathlib
import argparse

import yaml

HERE = pathlib.Path(__file__).resolve().parent.parent
REPO = HERE.parent.parent


def norm(s):
    s = s.replace("​", "").replace("­", "").replace("\f", " ")
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def load_lines(extract_dir, key, strip_bill_numbers=False):
    raw = (extract_dir / f"{key}.txt").read_text()
    lines = raw.split("\n")
    if strip_bill_numbers:
        # NY bill text prints its own line numbers (1-55) in a left column.
        lines = [re.sub(r"^\s{0,3}\d{1,2}(\s{2,}|\s(?=\S))", " ", ln) for ln in lines]
        # It also hyphenates words across its line breaks ("inju- ry"). Move the
        # rest of the word up a line, keeping the line count. This would wrongly
        # join a compound split at its own hyphen; anchors avoid those.
        text = re.sub(r"([a-z])-[ \t]*\n([ \t]*)([a-z]\S*)",
                      lambda m: m.group(1) + m.group(3) + "\n" + m.group(2), "\n".join(lines))
        lines = text.split("\n")
    return lines


def page_of(lines, lineno):
    # pdftotext puts the form feed at the start of a new page's first line,
    # so a line's own leading form feed counts toward its page.
    return sum(ln.count("\f") for ln in lines[:lineno]) + 1


def count(hay, needle):
    n, i = 0, hay.find(needle)
    while i != -1:
        n += 1
        i = hay.find(needle, i + 1)
    return n


def locate(extract_dir, key, quote, strip):
    lines = load_lines(extract_dir, key, strip)
    q = norm(quote)
    whole = norm("\n".join(lines))
    print(f"matches in document: {count(whole, q)}")
    # Tightest spans: for each end line where the quote first completes,
    # move the start forward as far as it still contains the quote.
    end = 1
    while end <= len(lines):
        if q in norm("\n".join(lines[max(0, end - 60) : end])):
            start = max(1, end - 59)
            while q in norm("\n".join(lines[start : end])):
                start += 1
            print(f"L{start}-{end}  p{page_of(lines, start)}")
            end += 60
        else:
            end += 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--extract-dir", default=str(REPO / ".extract"))
    ap.add_argument("--locate", nargs=2, metavar=("KEY", "QUOTE"))
    ap.add_argument("--bill-numbers", action="store_true")
    a = ap.parse_args()
    xd = pathlib.Path(a.extract_dir)
    if a.locate:
        locate(xd, a.locate[0], a.locate[1], a.bill_numbers)
        return 0

    rec = {p.stem: yaml.safe_load(p.read_text()) for p in sorted((HERE / "records").glob("*.yaml"))}
    docs = {d["key"]: d for d in rec["passages"]["documents"]}
    passages = {p["id"]: p for p in rec["passages"]["passages"]}
    problems, notes = [], []

    for pid, p in passages.items():
        d = docs.get(p["doc"])
        if d is None:
            problems.append(f"{pid}: unknown document {p['doc']}")
            continue
        path = xd / f"{p['doc']}.txt"
        if not path.exists():
            problems.append(f"{pid}: no extraction {path} (run bin/extract-text {p['doc']})")
            continue
        lines = load_lines(xd, p["doc"], d.get("bill_line_numbers", False))
        a_, b_ = (int(x) for x in str(p["lines"]).split("-")) if "-" in str(p["lines"]) else (int(p["lines"]),) * 2
        span = norm("\n".join(lines[a_ - 1 : b_]))
        q = norm(p["quote"])
        if q not in span:
            problems.append(f"{pid}: quote not found in {p['doc']} L{p['lines']}")
        pg = page_of(lines, a_)
        if pg != p["page"]:
            problems.append(f"{pid}: page recorded {p['page']}, extraction says {pg}")
        m = count(norm("\n".join(lines)), q)
        if m != 1:
            notes.append(f"{pid}: quote matches {m} times in {p['doc']}; the line range disambiguates")

    # Referential integrity: P-, R-, A-, L-, D-, T- ids and thin: terms.
    defined = set(passages)
    for name, body in rec.items():
        for k, v in (body or {}).items() if isinstance(body, dict) else []:
            if isinstance(v, list):
                for item in v:
                    if isinstance(item, dict) and "id" in item:
                        defined.add(item["id"])
    # Defects are defined as headings "#### D-..." in weight-and-defects.md.
    wd = HERE / "weight-and-defects.md"
    if wd.exists():
        defined |= set(re.findall(r"^#+ (D-[a-z0-9-]+)", wd.read_text(), re.M))
    terms = {t["id"] for t in rec["terms-thin"]["terms"]}
    text = "\n".join((HERE / "records" / f"{n}.yaml").read_text() for n in rec)
    text_md = "\n".join(p.read_text() for p in HERE.glob("*.md"))
    for ref in sorted(set(re.findall(r"\b([PRALDTFS]-[a-z0-9][a-z0-9.-]*[a-z0-9])\b", text + text_md))):
        if ref not in defined:
            problems.append(f"undefined id referenced: {ref}")
    for t in sorted(set(re.findall(r"\bthin:[a-z][a-z0-9.-]*[a-z0-9]", text + text_md))):
        if t not in terms:
            problems.append(f"undefined term referenced: {t}")

    for n in notes:
        print("note:", n)
    for pr in problems:
        print("PROBLEM:", pr)
    print(f"{len(passages)} passages, {len(defined)} ids, {len(terms)} thin terms; {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
