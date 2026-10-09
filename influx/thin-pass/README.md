# influx/thin-pass/: the G1b thin pass

> [!NOTE]
> **Line and page references here predate `ref/canonical/`.** They were taken from `pdftotext -layout` extractions of the relata PDFs (the `bin/extract-text` script), before the canonical page-marked texts existed. Page numbers are the PDF's physical pages as pdftotext counted them (by form feeds). For the 84 catalog PDFs that count was checked and holds; for other documents a PDF with stray form feeds would shift it, so check before relying on a page. Line numbers ("L…") are lines of those layout extractions, so they won't match `ref/canonical/`: to re-find a passage, search for its quoted words, or regenerate the layout text with `pdftotext -layout`. References marked "md" are lines of `ref/iasr-2026-full.md`, which is unchanged.

*Phase G1b of `MODEL-GAMMA-METHODOLOGY-AND-PLAN.md`: one source and one competency question carried end to end in rough form, to find out which terms and record fields bear weight before refinement time is spent on them. Done 2026-10-07 by Claude (Opus 5.5); audited by an independent verifier and repaired the same day. **Everything here is disposable.** Nothing is adopted into `def/` or the plan except by a later decision.*

**The source:** California SB 53, at full depth. The four documents that carry its ">50 people or $1B" bar are covered at their passages:
- RAISE S.8828;
- xAI FAIF 2025;
- Anthropic FCF v2;
- OpenAI FGF.

There are also single passages from xAI's 2025 RMF and 2026 FAIF, OpenAI's PF v2, Anthropic's RSP v3.4 and the EU AI Act.

**The question:** candidate Q1, "For a single incident with 60 deaths, which sources would call it catastrophic, severe or systemic, under what conditions, and through how many independent lineages?"

**Why Q1.** The coordinator chose it. The plan's G1b text suggested Q4 or Q20, and SB 53's catastrophic-risk definition is acceptance test 1's first case. Q1 turned out to be a good test of the record formats and a poor test of term weight. It stipulates two facts, so most clauses can only be named, not weighed (`weight-and-defects.md` §1). It also never touches the actor vocabulary that Joseph named as his priority.

**The main result, corrected.** The slice can't rank lexicon terms for refinement. The first version said it could; `response-to-de-novo-feedback-1.md` explains why that was withdrawn.

## Read in this order

| File | What it is | Who it's for |
|---|---|---|
| `debrief.md` | What happened, the correction, what it means for refinement, and what I'm unsure of | Joseph, after his plan review; then the G2 and G3 agents |
| `answer.md` | Q1's answer, checkable against quoted passages, then the computed tables | Anyone checking the answer against the sources |
| `weight-and-defects.md` | G1b's done-test: what the computation can and cannot say about weight, the record fields used, and the defects found (D- ids) | Joseph; the G2, G3 and G1(e) authors |
| `proposed-changes.md` | Changes to the plan and the competency questions, each pointing to its defect. Change 2 is a decision for Joseph | Joseph |
| `de-novo-feedback-1.md` | The independent verifier's audit of the first version | Anyone weighing this pass |
| `response-to-de-novo-feedback-1.md` | What was accepted, changed and contested, with where each finding was checked | Joseph; the coordinator |
| `notation/` | The same slice rewritten in the namespaced notation Joseph sketched on 2026-10-07, with notes on where it fit and strained. Start at `notation/README.md` | Joseph |
| `records/` | The records the answer is computed from (below) | Verifiers; whoever drafts G1(e) |
| `tools/` | The checker, the answer computation, and the shared-wording comparison | Verifiers |

## The records

All are YAML. Each file's header says what its rough format is and where it broke.

| File | Holds |
|---|---|
| `records/passages.yaml` | documents, scopes, and 65 anchored passages (page, lines, exact quote) |
| `records/translation.yaml` | translation rows (`T-`) and definition frames (`F-`) with evaluable tests |
| `records/resolutions.yaml` | resolution records (`R-`), each saying whether its candidates are encoded |
| `records/assertions.yaml` | assertion records (`A-`) |
| `records/lineage.yaml` | lineage records (`L-`), including a shared FCF/FGF template node |
| `records/scenarios.yaml` | Q1 under open- and closed-world readings, plus three variants used as probes |
| `records/terms-thin.yaml` | the throwaway `thin:` terms the answer used, each with how much it weighed and whether that was computed or judged |

## Re-running

```sh
bin/extract-text california-2025-sb53 ny-2026-raise-s8828 xai-2025-faif xai-2026-faif xai-2025-rmf \
  anthropic-2026-frontier-compliance-framework-v2 openai-2026-frontier-governance-framework \
  openai-2025-preparedness-framework-v2 anthropic-2026-rsp-v3-4 eu-2024-ai-act \
  eu-cop-2025-safety-security                    # from the repo root, into .extract/
cd influx/thin-pass
python3 -I tools/check.py              # every quote, page and id; reports quotes that match more than once
python3 -I tools/answer.py             # the answer and row-level weights; --write refreshes answer.md's tables
python3 -I tools/shared_runs.py ../../.extract/A.txt ../../.extract/B.txt   # shared verbatim runs (lineage)
```

The tools need PyYAML. Line numbers match only with the same poppler version; pages and quotes survive any version. The EU Code is used only by the shared-wording comparison.
