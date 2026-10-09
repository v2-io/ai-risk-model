# Source atlas

> [!NOTE]
> **Line and page references here predate `ref/canonical/`.** They were taken from `pdftotext -layout` extractions of the relata PDFs (the `bin/extract-text` script), before the canonical page-marked texts existed. Page numbers are the PDF's physical pages and still hold. Line numbers ("L…") are lines of those layout extractions, so they won't match `ref/canonical/`: to re-find a passage, search for its quoted words, or regenerate the layout text with `pdftotext -layout`. References marked "md" are lines of `ref/iasr-2026-full.md`, which is unchanged.

Written 2026-09-28 by ten parallel agents, one per family of sources, for the schema relitigation with Joseph. Each file gives, for each document, its table of contents, its glossary or definition ranges, and 2–6 representative passages, with a one-line note on each saying what drew the agent to it. The notes are signposts, not summaries. `SCHEMA-READING-NOTES.md` holds the coordinator's notes from reading the passages, with line references.

**What the line numbers refer to.** Each document's PDF in relata, extracted with:

```
pdftotext -layout "$(relata show <key> | awk '/^pdf:/{print $2; exit}')" <key>.txt
```

The extractions lived in a session scratchpad and weren't kept. To regenerate one, run `pdftotext -layout` on the PDF path that `relata show <key>` prints; the same poppler version gives the same lines. Pages are PDF pages counted by form feeds, and they survive a re-extraction. For web pages rendered to PDF by earlier agents, pages are rendering artefacts, so cite by heading. Exceptions:
- IASR 2026 cites `ref/iasr-2026-full.md` (a local-only copy; see `ref/.gitignore`);
- `anthropic-autonomous-dev` cites `ref/anthropic-autonomous-dev.md`.

**Coverage.** There are 212 documents: every relata key cited in `model/` (now `influx/model-beta/`) or `influx/verification/`, minus six misfiled entries recorded in `influx/verification/relata-bugs.md`, plus the two in-repo markdown sources. Each file says what its agent read whole and what it sampled. Long reports are sampled thinly.

**Extraction problems** (garbled columns, image-only tables, OCR) are noted per document. Several agents flagged documents that aren't what their key or title suggests; check the per-document header before relying on one.
