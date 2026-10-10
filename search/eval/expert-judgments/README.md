# Source experts' judgments of what search should return

*Round 1, 2026-10-10, coordinated by ai-risk-model-61. Each source expert (`experts/README.md`) was forked and asked to judge the outline's 12 queries plus questions of its own, in two stages: blind first, committed before it saw any search output; then against what `hybrid -n 20` and `outline --lines 60` actually returned over its source. The briefs are in `experts/fork-briefs/`.*

## Files, per source key

- `KEY.json`: stage 1, in the whole-document judges' format (`../outline-judging-brief.md`). `outline-check --judgments` and `--agree` read it.
- `KEY.reorder.json`: stage 2, keyed by the tool's own passages (`src.passages` ord, with line ranges and first words). Per query and tool, it gives the order the results should have come in, what was missed (`shown_rank: null`), and the noise. Outline entries carry `opened` instead of ranks.
- `KEY.notes.md`: what the expert found, by mechanism, and what got in the way.
- `KEY.inputs/`: the expert's ideal orderings and build script. The scripts read raw search runs from each fork's temporary directory, which hasn't been kept, so they won't rerun. The `.reorder.json` files are complete without them.
- `california-2025-sb53.agreement.md`: the SB 53 expert's reading of where it, the Claude judge and Gemini disagree, its own errors included.

## What to know before using them

- **Four of five sources.** The IASR expert's fork was stopped twice by a safety classifier, after turns that only checked a hash and ran a keyword search, so the cause is most likely the biological section in its context. It stopped itself (2026-10-10). Its one judged query ("hazard", stage 1) is in `partial/`, which the scorer doesn't read: a one-query file here would add IASR to the pooled scope and shift every document's cut. IASR has only its whole-document judge, which read the canonical text whole without a stop.
- **The chemical and biological query** was left out for the Risk Report and AISI, after a classifier stop of another fork in that territory. SB 53 and the EU Code judged it with anchors and grades only.
- **The AISI expert had read the earlier Opus AISI expert's notes** before judging (its notes say so), so its stage 1 isn't wholly unprimed.
- **Questions the source can't answer in its own words** ("hazard" in a statute, say) were judged differently: some judges left them empty, while the experts mapped them to the source's nearest terms. That's a policy choice the evaluation hasn't made yet (EU Code and SB 53 notes).
- **Agreement with each document's whole-document judge** on the queries both judged (`outline-check --agree`, marked or not): AISI 0.84, SB 53 0.83, EU Code 0.65 (against Grok), Risk Report 0.61 (its judge marked chapter-sized stretches). The SB 53 expert's advice for fitting: trust grade 2, treat grade 1 as soft, and match passages by overlap with a judged stretch, not by its exact edges.
- **Search ran at commits `f1c93eb` (SB 53) and `e0e7025` (the others),** before any change to ranking.
