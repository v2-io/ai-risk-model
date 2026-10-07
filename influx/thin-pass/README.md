# influx/thin-pass/: the G1b thin pass

*Phase G1b of `MODEL-GAMMA-METHODOLOGY-AND-PLAN.md`: one source and one competency question carried end to end in rough form, to find out which terms and record fields bear weight before refinement time is spent on them. Done 2026-10-07 by Claude (Opus 5.5). **Everything here is disposable.** Nothing is adopted into `def/` or the plan except by a later decision.*

**The source:** California SB 53, at full depth. The four documents that carry its ">50 people or $1B" bar (RAISE S.8828, xAI FAIF 2025, Anthropic FCF v2, OpenAI FGF) are covered at their passages.

**The question:** candidate Q1, "For a single incident with 60 deaths, which sources would call it catastrophic, severe or systemic, under what conditions, and through how many independent lineages?"

## Read in this order

| File | What it is | Who it's for |
|---|---|---|
| `debrief.md` | What happened, what it means for where refinement goes, and what I'm unsure of | Joseph, after his plan review; then the G2 and G3 agents |
| `answer.md` | Q1's answer, checkable against quoted passages, then the computed tables | Anyone checking the answer against SB 53 |
| `weight-and-defects.md` | G1b's done-test: terms and record fields ranked by how much the answer leaned on them, and the defects found (D- ids) | Joseph, to place refinement passes; the G2, G3 and G1(e) authors |
| `proposed-changes.md` | Changes to the plan and the competency questions, each pointing to its defect | Joseph |
| `records/` | The records the answer is computed from (below) | Verifiers; whoever drafts G1(e) |
| `tools/` | The checker and the answer computation | Verifiers |

## The records

All are YAML. Each file's header says what its rough format is and where it broke.

| File | Holds |
|---|---|
| `records/passages.yaml` | documents, scopes, and 53 anchored passages (page, lines, exact quote) |
| `records/translation.yaml` | translation rows (`T-`) and definition frames (`F-`) with evaluable tests |
| `records/resolutions.yaml` | resolution records (`R-`) |
| `records/assertions.yaml` | assertion records (`A-`) |
| `records/lineage.yaml` | lineage records (`L-`) |
| `records/scenarios.yaml` | Q1 under open- and closed-world readings, plus three variants used as probes |
| `records/terms-thin.yaml` | the throwaway `thin:` terms the answer forced, with their weights |

## Re-running

```sh
bin/extract-text california-2025-sb53 ny-2026-raise-s8828 xai-2025-faif xai-2026-faif xai-2025-rmf \
  anthropic-2026-frontier-compliance-framework-v2 openai-2026-frontier-governance-framework \
  openai-2025-preparedness-framework-v2          # from the repo root, into .extract/
cd influx/thin-pass
python3 -I tools/check.py              # every quote, page and id; reports quotes that match more than once
python3 -I tools/answer.py             # the answer and weights; --write refreshes answer.md's tables
```

The tools need PyYAML. Line numbers match only with the same poppler version; pages and quotes survive any version.
