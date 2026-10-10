#!/usr/bin/env python3
"""Assemble stage-1 judgments (blind) for bengio-2026-international from per-query fragments.
Each fragment: stage1/NN-<slug>.json = {"query": "...", "stretches": [{"lines":[a,b],"quote":"...","grade":2,"note":"..."}]}
Run from the repo root. Verifies each quote against the canonical text and prints mismatches."""
import json, glob, hashlib, os, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
KEY = "bengio-2026-international"
canon = os.path.join(ROOT, "ref/canonical", KEY + ".md")
text = open(canon, encoding="utf-8").read()
lines = text.split("\n")
sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
queries = [q.strip() for q in open(os.path.join(ROOT, "search/eval/outline-queries.txt")) if q.strip()]
frags = {}
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "stage1", "*.json"))):
    d = json.load(open(f))
    frags[d["query"]] = d["stretches"]
bad = 0
for q, st in frags.items():
    for s in st:
        a, b = s["lines"]
        first = lines[a - 1]
        if not first.startswith(s["quote"]):
            bad += 1
            print("QUOTE MISMATCH", q, a, repr(first[:90]), "!=", repr(s["quote"][:90]))
out = {
    "key": KEY,
    "canonical_sha256": sha,
    "judge": "Claude Sonnet 5.5, the IASR source expert's fork (experiential reading of the whole source, units 1-340 of 481; reference list not read); stage 1, blind, written before any source-search run",
    "read": "whole, in order, except the reference list ('Notes', lines 3137-7704)",
    "date": str(datetime.date.today()),
    "queries": {q: frags.get(q) for q in queries if q in frags},
    "not_judged_this_round": [q for q in queries if q not in frags],
}
dst = os.path.join(ROOT, "search/eval/expert-judgments", KEY + ".json")
json.dump(out, open(dst, "w"), indent=1, ensure_ascii=False)
print("wrote", dst, "queries:", len(out["queries"]), "mismatches:", bad, "sha", sha[:12])
