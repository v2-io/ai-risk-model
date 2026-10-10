#!/usr/bin/env python3
"""Assemble the stage-1 (blind) judgments for bengio-2026-international from per-query fragments.

Each fragment is stage1/NN-<slug>.json = {"query": "...", "stretches": [{"lines": [a, b], "quote": "...", "grade": 2, "note": "..."}]}.
Fragments whose query is a line of search/eval/outline-queries.txt go under "queries"; any other fragment
(the expert's own questions) goes under "own_questions", so the scored set stays exactly the outline's queries.
Every quote is checked against the canonical text (the line at lines[0] must start with it); mismatches are printed.

usage (from anywhere):
  build_stage1_all.py [--extra DIR ...] [--canon FILE] [--dest FILE]
    --extra  another directory of fragments (repeatable), e.g. the earlier fork's stage1/ with 01-hazard.json
    --canon  the canonical text (default: <repo>/ref/canonical/bengio-2026-international.md; ref/ is git-ignored, so a
             worktree needs the main checkout's copy passed here)
    --dest   output file (default: <repo>/search/eval/expert-judgments/partial/bengio-2026-international.complete.json)
"""
import argparse, datetime, glob, hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE  # partial/<key>.inputs -> partial -> expert-judgments -> eval -> search -> repo root
for _ in range(5):
    ROOT = os.path.dirname(ROOT)
KEY = "bengio-2026-international"

ap = argparse.ArgumentParser()
ap.add_argument("--extra", action="append", default=[])
ap.add_argument("--canon", default=os.path.join(ROOT, "ref", "canonical", KEY + ".md"))
ap.add_argument("--dest", default=os.path.join(ROOT, "search", "eval", "expert-judgments", "partial", KEY + ".complete.json"))
ap.add_argument("--queries", default=os.path.join(ROOT, "search", "eval", "outline-queries.txt"))
a = ap.parse_args()

text = open(a.canon, encoding="utf-8").read()
lines = text.split("\n")
sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
queries = [q.strip() for q in open(a.queries, encoding="utf-8") if q.strip()]

frags, own, seen_files = {}, {}, []
for d in [os.path.join(HERE, "stage1")] + a.extra:
    for f in sorted(glob.glob(os.path.join(d, "*.json"))):
        j = json.load(open(f, encoding="utf-8"))
        seen_files.append(f)
        (frags if j["query"] in queries else own)[j["query"]] = j["stretches"]

bad = 0
for group in (frags, own):
    for q, st in group.items():
        for s in st:
            first = lines[s["lines"][0] - 1]
            if not first.startswith(s["quote"]):
                bad += 1
                print("QUOTE MISMATCH", q, s["lines"], repr(first[:90]), "!=", repr(s["quote"][:90]))

out = {
    "key": KEY,
    "canonical_sha256": sha,
    "judge": "Claude Sonnet 5.5, the IASR source expert's fork (experiential reading of the whole source, units 1-340 of 481; reference list not read); stage 1, blind, written before any source-search run",
    "read": "whole, in order, except the reference list ('Notes', lines 3137-7704)",
    "date": str(datetime.date.today()),
    "queries": {q: frags[q] for q in queries if q in frags},
    "not_judged_this_round": [q for q in queries if q not in frags],
    "own_questions": own,
}
os.makedirs(os.path.dirname(a.dest), exist_ok=True)
json.dump(out, open(a.dest, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("wrote", a.dest)
print("outline queries judged:", len(out["queries"]), "not judged:", len(out["not_judged_this_round"]), "own questions:", len(own),
      "quote mismatches:", bad, "sha", sha[:12], "fragments read:", len(seen_files))
