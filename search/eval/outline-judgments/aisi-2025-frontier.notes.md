# Notes on aisi-2025-frontier (UK AISI, *Frontier AI Trends Report*, 2025)

Judged 2026-10-09 by Claude Opus 5.5. I read the whole document in order, then grepped it for words in the queries. I did not run `bin/source-outline` or `bin/source-search`.

## What kind of document it is

This is an empirical trends report. It contains no obligations, thresholds, definitions of risk or decision procedures. It reports what AISI's evaluations found, domain by domain. So four of the twelve queries are nearly empty, and that is the correct result: whistleblower, serious incident, what a developer must publish before deploying, and how severity or acceptability is decided. What I graded for them are the near-misses, all at grade 1, with notes explaining that.

The order is: executive summary (lines 56–82) → key milestones (86–110) → contents table → 01 Introduction, covering the testing approach and how to read the report (133–180) → 02 Agents (184–222) → 03 Capabilities & risks, split into 3.1 Chem/Bio (242–320) and 3.2 Cyber (324–366) → 04 Safeguards (370–466) → 05 Loss of control, split into 5.1 Self-replication (482–508) and 5.2 Sandbagging (512–550) → 06 Societal impacts (556–678) → 07 Open-source (684–718) → 08 Conclusion (724–732) → Appendix: limitations, data presentation, uncertainty (736–761) → References → Glossary (812–870).

## Where headings mislead, or are missing

- **The heading levels follow the conversion, not the document.** "Capabilities & risks in key domains", "04 Safeguards", "Loss of control risks" and "Conclusion" are `#`. "Introduction", "02 Agents", "Societal impacts" and "Open-source models" are `##`. 6.3 is `###` while 6.1 and 6.2 are `##`. Some chapter numbers are left on their own: "## 05" (468) and "## 06" (552) are empty headings sitting just before their chapters, and "01", "03", "07" and "08" are bare lines at the end of the previous chapter. An outline built from heading depth will nest these wrongly. For example, "Loss of control risks" comes out as a top-level sibling of "Executive summary", with an empty "## 05" above it.
- **Figure titles have become headings.** Examples are line 310 ("## Multimodal AI models can now provide PhD-level troubleshooting advice…"), line 360 ("## AI models are improving at cyber range challenges…") and line 452 (a `####` heading that has swallowed the figure's axis labels and tick values). Meanwhile, many of the report's own claim-headers are plain paragraphs, for example lines 328, 336, 354, 516, 522, 584 and 630. So the real sub-structure of each section is mostly invisible to a heading outline.
- **One headline number sits in an unexpected chapter.** The cyber result most often quoted from this report (task length doubling about every eight months, an estimated upper bound) is in **02 Agents** at line 204, not in 3.2 Cyber. An outline that opens only "3.2 Cyber" for a cyber question will miss it.
- **Figure content is almost entirely missing.** Most figures are images only. Captions survive only for Figures 1.3, 9, 11, 12, 14 and 15. Fragments of the captions for Figures 18, 20 and 23 are stranded in the text at lines 578, 604 and 678. Several numbers in the prose refer to figures that can't be read here. pdf-page 8 has no text (probably a full-page graphic), and nor do pdf-pages 50–51.
- Small conversion leftovers: "AlSI" at line 88 was not corrected, there is a literal `\n` at line 746, and "sustems" (372) and "safequards" (374) are misspelt, either in the source or by OCR.

## How the queries fit this document

- **chemical and biological weapons uplift.** The report almost never says "weapons". It says it once, in Safeguards (372, "aid in weapons development"). The chem/bio section talks instead of "dual-use", "misuse", "harmful intentions" and "risky research" (234), and of "uplift" only as a method (169, 832). That makes it a good test of retrieval that is not lexical: everything that matters is in 3.1, and the word is not.
- **humans can no longer shut down or correct the AI system.** The report never puts loss of control in terms of shutting down or correcting a system. Its wording is "evade human control" (72, 154, 476) and "reliably directed towards human goals" (74). That last phrase is close to the EU Code's "reliably direct, modify, or shut down" but leaves out the modify and shut-down parts. That may interest the lineage work in `MODEL-GAMMA-…` §1.3. I haven't checked whether it is derived from the Code.
- **misalignment.** The word never appears. "Deliberative Alignment" (386) is the name of an OpenAI technique, and I left it out. The nearest concept is at line 474, "risks that emerge from models themselves behaving in unintended or unforeseen ways", which the report sets against misuse.
- **catastrophic risk.** "Catastrophic" appears once, at 476, and qualifies loss of control.
- **hazard.** The word appears twice, in two different senses: "hazardous capabilities" (110) and the glossary's lab "'wet' hazards" (870).

## How I divided the stretches, and a scoring interaction worth knowing

`outline-check` credits a stretch if *any* passage overlapping its line range is read. A stretch the size of a whole chapter is therefore fully credited when any one passage in it is opened. I divided 3.1, 3.2 and 5.2 into the report's own claim-units, because each one carries a separate finding that an agent would need: for example, the 4.7x non-expert uplift study at 278–288 is a different finding from the QA scores at 242–254. I kept 5.1 and 5.2 whole for the broad "loss of control" query, where the chapter really is the unit. If whole-chapter credit is what you intend, that's fine. If not, consider crediting a stretch by the fraction of its passages that are read.

Also, the docstring of `outline-check` says that judged passages with "grade 2 or more" count. The code in `judged_grades` keeps grade ≥ 1 and weights it 2^g − 1, so grade 1 counts as 1 and grade 2 as 3. Under this brief's scale, grade-1 items are therefore scored. That seems reasonable to me, but the docstring and the code disagree.

## Questions this evaluation could add for this kind of document

- "self-replication": section 5.1, and the autonomy figure at 110.
- "evaluation awareness / models can tell testing from deployment": 518 and 546. It is scattered and short, so it is a good test of finding small things.
- "open-weight models and removal of safeguards": 412–414, 440, 520, and all of chapter 07. It cuts across chapters.
- "limitations of these evaluations": 176–180, 338–340, 506, 548, and the Appendix. The material is spread across the whole document.
