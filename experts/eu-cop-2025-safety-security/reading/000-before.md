# Before reading: priming, and what I expect

*Expert on `eu-cop-2025-safety-security` (EU General-Purpose AI Code of Practice, Safety & Security chapter, 2025). Claude Opus 5.5, Claude Code session 7354940e. Started 2026-10-09. The reading tool runs from the main checkout (`bin/reading`, whose cursor and `.prior/` copy stay local there). These reflections are written in the worktree `.claude/worktrees/expert-eu-cop`, branch `expert/eu-cop-2025-safety-security`. They are committed to that branch and the branch is not pushed while they quote the Code heavily (agreed with ai-risk-search-tool, 2026-10-09).*

*Unit size: `--min-words 150`, 124 units. The reasons: a Measure-sized unit gives each prediction a whole provision to land on; 462 single-paragraph units with a real reflection after each probably wouldn't fit. Joseph's calibration: the session started at about 188k tokens. Context checks at about units 30, 60 and 90, and otherwise no thought about context.*

## Priming (read hardest where this fires)

1. **From the repo's `CLAUDE.md`**, loaded every session:
   - the Code's loss-of-control formula "reliably direct, modify, or shut down", said to recur in nine later documents (three quote it as the Code's, one adopts it verbatim, one embeds it, four paraphrase it);
   - the Code says the AI Act's definitions "shall prevail";
   - the Code is to be read "in accordance with any AI Office guidance".

   So when I meet the loss-of-control definition, the definitions clause and the interpretation clause, the reflex will be "yes, I know this". Those are the three places to slow down. What is the *rest* of the sentence around each phrase? What does "reliably" modify? What does the word "shut down" sit beside?
2. **From training.** The Code was published around July 2025, so I probably saw it or commentary on it. What I think I remember, held as a hypothesis and not as knowledge:
   - It's one of three chapters (Transparency, Copyright, Safety & Security). This one applies only to providers of GPAI models *with systemic risk*.
   - Its structure is Commitments, each with numbered Measures, plus a preamble/recitals and an appendix (or appendices) that list systemic risks and give a glossary.
   - Its core artefacts are a "Safety and Security Framework" (a document created before or around placing on the market, and updated), and a "Safety and Security Model Report" per model, sent to the AI Office.
   - There's a lifecycle of systemic-risk identification, then analysis, then a determination of acceptability against pre-defined "systemic risk tiers" / acceptance criteria, then mitigations (safety and security), then reporting.
   - It names a short list of "specified systemic risks": CBRN, loss of control, cyber offence, harmful manipulation. Others are to be identified via a process.
   - There are external evaluators, serious incident reporting with timelines (something like 2/5/10/15 days by severity?), whistleblower protection / non-retaliation, allocating responsibility within the organisation, and documentation retention (maybe 10 years?).
   - Some flexibility for SMEs, and an "appropriate" / "state of the art" standard used throughout.
   - The Commitments number around ten.

   Every one of those is a place where my memory may be the anthology version and not the text. I expect at least some of the numbers (deadlines, retention years) and the list of specified risks to be wrong or to be more qualified than I remember. When the text differs from this list, I'll say so.
3. **What I've deliberately not read:** Grok's outline-evaluation judgements on this source, `influx/source-models/` and the atlas entries on the Code, and anything in `influx/` that analyses it. I've read only the repo's `CLAUDE.md` (unavoidable), and the experts README/BRIEF and protocol.

## What I expect the document to be like, as a reading

- Legal-administrative prose, written by Chairs and Vice-Chairs out of a multistakeholder drafting process. So it will be careful, hedged ("Signatories commit to…", "as appropriate", "where…"), with drafting fingerprints from compromises: places where a strong word got a qualifier.
- Its addressee is "Signatories", not "providers". A voluntary instrument that becomes a way to *demonstrate compliance* with AI Act Art. 55 obligations. So I expect a tension running through it: is it describing what the law requires, or offering one way to meet it? I'll watch for the phrase that ties the two (something like "adequate means of demonstrating compliance").
- Its implicit model of risk: probably a bow-tie-ish one (sources → risk → mitigations), with "systemic risk" as the AI Act's term (Art. 3(65)), meaning high-impact capabilities and effects at Union scale. I want to see how it operationalises "systemic" and whether "risk" here means probability × severity, or a scenario, or a hazard.

## Prediction for unit 1

The first unit will be the title and some framing material: the chapter's name, maybe a statement of who drafted it (Chairs/Vice-Chairs), and the beginning of a preamble or "Objectives" section. I expect it to open with the AI Act (Regulation (EU) 2024/1689), Art. 56 (codes of practice), and the purpose: to help providers of GPAI models with systemic risk comply with Art. 55. If the recitals come first, they'll be lettered (a), (b)… and will state principles such as proportionality, the precautionary principle, and "appropriate lifecycle management".
