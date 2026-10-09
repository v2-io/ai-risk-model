# Notes on judging eu-cop-2025-safety-security

Read whole, in order, 2026-10-09. Canonical sha256 `d2968247a71d1cb372aa050f42af0459ce4249ccbc56983ceb76f194ac79370f`. Judgments in the sibling `.json`. I did not run `bin/source-outline` or `bin/source-search`.

## How the document is organised

This file is only the Safety and Security Chapter of the Code of Practice, not the whole Code. After Objectives and Recitals (a)–(j), it is ten Commitments, each with Measures, then a Glossary, then four Appendices. Appendix 1 is the risk taxonomy the Commitments keep pointing at; Appendix 3 specifies the evaluations Measure 3.2 requires; Appendix 4 specifies the security mitigations Measure 6.2 requires. The Glossary says that where a term is defined in Article 3 of the AI Act, that definition prevails.

Most of the load-bearing content is in the Measures and Appendices, not the Commitment chapeaux. Recitals (i) and (j) are exceptions: they are reading rules, not throat-clearing.

## Headings that mislead, or split oddly

- **`# The safety margin will:`** (line 325) is a top-level heading sitting between Measure 4.1 and Measure 4.2. In substance it is part of 4.1 (the acceptance determination “incorporating a safety margin (as specified in the following paragraph)”). An outline that treats it as its own section, or that folds it away when 4.1 is opened, will hide the only place the Code says what the margin must take into account.
- **Measure 8.3** is titled “Promotion of a healthy risk culture”. The whistleblower policy and the non-retaliation rule live here as two of seven *examples of indicators*, not as standalone duties with their own heading.
- **Commitment 6** is “Security mitigations” and is about cybersecurity *of* the model (theft, unauthorised access, unreleased weights). **Appendix 1.4 (3) “Cyber offence”** is about the model’s own offensive cyber capabilities. Same root, opposite direction. I did not grade Commitment 6 under “cyber capabilities of frontier models”.
- **Appendix 1.1 “Types of risks”** is five EU-Act buckets (health, safety, public security, fundamental rights, society as a whole). The CBRN / loss of control / cyber offence / harmful manipulation list is **Appendix 1.4**, “Specified systemic risks”. A heading search for “types of risks” will miss the specified list.
- Several glossary rows are split across page-break table fragments (`'internal validity'`, `'resolved' (serious incident)`, `'systemic risk acceptance criteria'`). The definition continues on the next row, sometimes after a page marker.

## The two empty queries

**hazard.** The word does not appear. The Code talks in “risk”, “systemic risk”, and “types of risks” (Appendix 1.1 includes “Risks to safety”). I left the list empty rather than mapping those over, so absence stays visible.

**catastrophic risk.** Also never used. The nearest analogue is Appendix 1.4’s specified systemic risks, plus Article 3(65) “systemic risk” quoted at line 725. Same choice: empty in the JSON, analogue named here.

## Questions that were awkward for this document

**“what must a developer publish or report before deploying a frontier model”.** The Code’s parties are Signatories / providers of general-purpose AI models with systemic risk; the act is *placing on the market*, not deploying; “frontier model” is not a defined term (the only “frontier” is “the frontier of model capabilities” in Appendix 1.2.2). What the question is after, in this document, is the Framework (Measure 1.1, confirmed no later than two weeks before placing on the market, notified under 1.4) and the Model Report (Commitment 7, before placing on the market). Public *publication* is Measure 10.2, and it is conditional (“if and insofar as necessary”), not a hard pre-market duty. Measure 10.1 is documentation for the AI Office *upon request*. Recital (h) and line 398 qualify all of this for SMEs/SMCs.

**“evidence that models can sabotage, sandbag or evade oversight”.** This Chapter is a code of practice. It defines deception (including detecting evaluation and under-performing), requires elicitation that minimises sandbagging, lists “capabilities to evade human oversight”, and requires protections against sabotage *carried out by models*. It presents no empirical evidence that models can do those things. The grade-2 stretches are the places an agent has to read in order to report that.

**“chemical and biological weapons uplift”.** “Uplift” appears only in “human uplift studies” as an evaluation method (line 235). The CBRN specified risk talks instead of “significantly lowering the barriers to entry for malicious actors”. That is the Code’s form of the idea.

**“serious incident”.** Used throughout and given a whole Commitment, but *not defined in this Chapter*. The Glossary defines “near miss” and “resolved” (serious incident) only. Measure 9.3 lists harm types that set reporting clocks (critical infrastructure, cybersecurity breach including (self-)exfiltration, death, serious harm to health/rights/property/environment). The definition is left to the AI Act.

**“loss of control” / “humans can no longer shut down or correct the AI system”.** These collapse onto the same sentence in Appendix 1.4 (2): “humans losing the ability to reliably direct, modify, or shut down a model.” That formula is the one later documents copy. I graded the same sentence 2 for both queries, and the capability/propensity sources 1.

## A question the evaluation could usefully add

**“systemic risk”** itself — definition (Art. 3(65) at line 725), how it is identified (Commitment 2 + Appendix 1), and how it relates to “risk” in Art. 3(2) (recital (i)). Several of the present queries are downstream of that, and the empty “hazard” / “catastrophic risk” answers are mostly “this document says systemic risk instead.”

Also useful: **“placing on the market”** versus **“use”**, and **“similarly safe or safer model”** (Appendix 2), which is the main exemption from evaluations, reporting, and public summaries.

## Small fidelity notes for anyone matching quotes

- Line 829 has “selfreasoning” without a hyphen, as in the conversion.
- Line 725 has “generalpurpose” without a hyphen, in the Art. 3(65) quote.
- Recital (d) is one long paragraph: whistleblowers share the line with confidentiality, Article 78, and international standards.
