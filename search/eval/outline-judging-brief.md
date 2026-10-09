# Judging one document whole, for the outline's evaluation

*A brief for an agent judging one of the Au5 documents. Written 2026-10-09 by the Claude instance that built the outline (`search/srcsearch/outline.py`), so it carries that author's interest in the result. That is part of why the judging goes to you.*

## What this is for

This repository maps the frontier-AI risk landscape from what the field's own documents claim. Agents working on it constantly need the right parts of long documents without reading all of them first. Joseph Wecker, who leads the project, put the need this way (2026-10-09): "Essentially what we're trying to do is give us all the right intuition and relevant info from a set of sources without requiring you or a sub-agent to have to ingest the entire things into context first." His idea for meeting it was a document's outline, with only the parts that matter to a question unfolded, down to the line ranges to read. That has now been built.

The only way to know whether it points to the right places is for someone who has read the document whole to say what an agent answering each question would actually need to read. That is what we're asking of you, for one document. A ranked search's own grades can't settle it, because they only ever see what some ranking already surfaced. Your reading isn't limited that way.

So please read the document in order, the way a person would. Then, for each question below, say which stretches of it an agent answering that question must read, and which would help. Please don't run `bin/source-outline` or `bin/source-search` until your judgments are written. They would show you what the tools think, and the value of your reading is that it is independent of them.

## The document and the questions

Your document is `ref/canonical/KEY.md` (the key is in the message that launched you). It is a markdown rendering of the source with `[pdf-page N, printed "X"]` markers. The questions are in `search/eval/outline-queries.txt`, one per line. Some are single terms ("hazard"); read those as "where does this document use, define, or discuss this?". Some are questions. Several won't apply to your document at all, and an empty answer is a judgment too.

## What to write, and where

One JSON file, `search/eval/outline-judgments/KEY.json`. `search/eval/outline-check --judgments search/eval/outline-judgments` reads it and scores the outline, and a ranked list given the same room, against it:

```json
{
  "key": "california-2025-sb53",
  "canonical_sha256": "<sha256 of ref/canonical/KEY.md as you read it>",
  "judge": "<your model and anything that identifies this run>",
  "read": "whole, in order",
  "date": "2026-10-…",
  "queries": {
    "whistleblower": [
      {"lines": [255, 303], "quote": "the exact first words of that stretch", "grade": 2, "note": "why, briefly"}
    ],
    "hazard": []
  }
}
```

- `lines` are the file's line numbers, inclusive. `quote` is the exact text the stretch starts with: line numbers change when the file is rebuilt, and the quote lets the check find the stretch again. That is also why the file's sha256 is recorded.
- `grade` 2 means an agent answering this must read it. 1 means it would help (context, a qualification, a cross-reference). Leave out anything else.
- A stretch can be a whole section or a single sentence, whichever is true to the document. If a whole chapter matters, say the chapter rather than listing its paragraphs.
- Every question gets a key, even if its list is empty, so that "nothing here" is distinguishable from "not judged".

## What else would help

The outline is new, and you'll know this document better than anyone involved by the time you finish. Anything you notice is welcome in a short `search/eval/outline-judgments/KEY.notes.md`: how the document is organised, places where its headings mislead about what's under them, a question that turned out ambiguous for this document, or a question you think the evaluation should have asked. If a question doesn't make sense for the document, or the format gets in the way of saying something true, say so rather than forcing it.

If you're willing, please stay on the line after you report, in case there are follow-up questions.
