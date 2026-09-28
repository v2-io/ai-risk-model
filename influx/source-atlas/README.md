# Source atlas

Written 2026-09-28 by ten parallel agents, one per family of sources, for the schema relitigation with Joseph. Each file gives, for each document, its table of contents, its glossary or definition ranges, and 2–6 representative passages, with a one-line note on each saying what drew the agent to it. The notes are signposts, not summaries. `SCHEMA-READING-NOTES.md` holds the coordinator's notes from reading the passages, with line references.

**What the line numbers refer to.** Each document's PDF in relata, extracted with:

```
pdftotext -layout "$(relata show <key> | awk '/^pdf:/{print $2; exit}')" <key>.txt
```

The extractions lived in a session scratchpad and weren't kept. Re-running the command gives the same lines on the same poppler version. Pages are PDF pages counted by form feeds, and they survive a re-extraction. For web pages rendered to PDF by earlier agents, pages are rendering artefacts, so cite by heading. Exceptions:
- IASR 2026 cites `influx/iasr-2026-full.md`;
- `anthropic-autonomous-dev` cites `influx/anthropic-autonomous-dev.md`.

**Coverage.** There are 212 documents: every relata key cited in `model/` or `influx/verification/`, minus six misfiled entries recorded in `influx/verification/relata-bugs.md`, plus the two in-repo markdown sources. Each file says what its agent read whole and what it sampled. Long reports are sampled thinly.

**Extraction problems** (garbled columns, image-only tables, OCR) are noted per document. Several agents flagged documents that aren't what their key or title suggests; check the per-document header before relying on one.
