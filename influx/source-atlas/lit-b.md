# Source atlas: lit-b (research and NGO literature on security, systemic and societal risk, power, taxonomies and ratings)

A reading guide into 24 documents. For each document it gives the table-of-contents range, the glossary or definitions range, and 2–5 passages chosen because they are typical or distinctive of what the document does. It says nothing about fitting them to our schema. The one-line notes are signposts; the line ranges are the deliverable.

**Conventions**
- Line numbers refer to `scratchpad/src-text/<key>.txt` (from `pdftotext -layout`), under `/private/tmp/claude-505/-Users-josephwecker-v2-src-aisi-eoi/f462f375-61ba-4d02-b4e6-ae440173656f/`.
- "p" is the PDF page, computed as 1 plus the number of form feeds in lines 1..L. It is not the printed folio. Where the two differ, the section says so. In the FLI editions and Hendrycks, the printed folio is the PDF page minus 1.
- For **rand-2024-weights-press** and **voudouris-2026-alignment-human**, "pages" are artifacts of HTML or web-print conversion. Cite those by heading or paragraph.
- Helper scripts: `scratchpad/litb/v.sh KEY START END` prints numbered lines with page markers, and `scratchpad/litb/pg.sh KEY LINE...` gives the page of each line. (The unprefixed `scratchpad/pg.sh` was overwritten by several atlas agents, so use the `litb/` copies.)

**Who read what.** The set was split four ways. Groups A (RAND weight and insight security, and AISP), B (the three FLI indexes) and C (systemic, power and multi-agent risk) were read by three forks of me, each with this conversation's full context. I read group D (the remaining eleven) myself, and I spot-checked about a dozen of the forks' citations against the texts; all matched. The per-group observations are kept at the end with their line references. The closing synthesis is mine.

## Index

| key | lines / pp | what it is | extraction |
|---|---|---|---|
| aguirre-2026-sl3 | 1274 / 39 | RAND SL3 weight-security standard | clean; **the controls and threat model are GitHub pointers, not in the PDF** |
| brassgershovich-2026-algorithmic | 4554 / 99 | RAND, securing algorithmic insights (ISL1–5) | clean; the cited score table is missing |
| davidson-2025-ai-enabled-coups | 2427 / 74 | Forethought, AI-enabled coups | web print; **footnote bodies absent** |
| fli-2025-ai-safety-index-summer | 5247 / 101 | FLI company ratings, 2nd edition | front matter clean; appendix tables bleed |
| fli-2025-ai-safety-index-winter | 6134 / 112 | FLI company ratings, 3rd edition | as above, plus two-column interleaving |
| fli-2026-ai-safety-index-summer | 7232 / 127 | FLI company ratings, 4th edition | as above |
| gekker-2026-aisp | 3909 / 101 | AI Security Priorities field agenda | clean; the ranking tables are images (lost) |
| gotting-2025-virology | 1775 / 31 | VCT virology benchmark | clean |
| hacker-2026-digital | 1004 / 21 | systemic risk in the DSA vs the AI Act (FAccT) | clean |
| hammond-2025-multi | 5396 / 96 | Cooperative AI Foundation multi-agent risks | clean |
| hendrycks-2023-overview | 2829 / 55 | CAIS overview of catastrophic risks | clean; figure labels interleave |
| kasirzadeh-2024-types | 1742 / 40 | decisive vs accumulative x-risk (philosophy) | clean; footnotes split mid-paragraph |
| kierans-2025-catastrophic | 787 / 12 | liability and duty of care for frontier AI | **two-column, moderately garbled** |
| kulveit-2025-gradual | 1303 / 23 | gradual disempowerment | clean |
| mitre-2025-agi | 634 / 19 | *RAND* (Mitre & Predd), five hard national security problems | clean; the summary figure is lost |
| nevo-2024-securing | 6549 / 128 | RAND, securing model weights (SL1–5, OC1–5) | clean; Table C.1 garbled |
| rand-2024-weights-press | 185 / 3* | RAND press release on Nevo | HTML-derived, hard-wrapped |
| ren-2024-safetywashing | 2506 / 43 | CAIS, safety benchmarks' correlation with capabilities | legible; sidebars interleave |
| sharma-2026-whos | 5550 / 73 | Anthropic et al., disempowerment in real usage | **page 1 badly interleaved**; two-column after |
| slattery-2026-risk | 3591 / 82 | MIT AI Risk Repository (1,725 risks, 74 frameworks) | clean |
| uuk-2024-taxonomy | 1592 / 34 | systemic-risk taxonomy (systematic review) | clean |
| vaintrob-2023-beware-safety-washing | 398 / 12 | EA Forum post plus comments | clean web print |
| voudouris-2026-alignment-human | 99 / 4* | **AISI web page with the abstract only, not the paper** | cookie banner interleaved |
| zwetsloot-2019-thinking | 324 / 8 | Lawfare essay: accidents, misuse, structure | clean web print |

---

## aguirre-2026-sl3: *Achieving AI Model Weight Security Level 3 (SL3)* (RAND RR-A4704-1, 2026)

1274 lines, 39 pp. Clean extraction. All figures are images, so only captions and notes survive. **The substance of the standard is not in the document.** Appendix A (threat model) and Appendix B (the 262 controls) are one-line pointers to a GitHub repository and a web tool (907-919, pp. 28-29). What the PDF contains is framing, method, a worked example, and workshop results.

- **TOC:** 130-150 (p. 6). Figures and tables: 156-173 (p. 7).
- **Glossary / definitions:** Abbreviations: 1119-1130 (p. 35), nine entries. The OC/SL definitions are re-tabulated from Nevo as Table 1 at 225-252 (p. 10). Note its footnote 2 (269-271): "some criminal organizations may be more cyber-capable than many nation-states".
- **Passages:**
  - **91-125 (p. 5). Summary bullets.** A dense mix of kinds of claim in a single list: counts (140 standard + 122 supplemental controls, 31 vectors), a workshop "finding" (human intelligence is the top concern), a design property ("each implemented control addressing an average of nine distinct attack vectors"), a feasibility commitment ("6 to 12 months"), and a normative position ("should be voluntary").
  - **203-290 (pp. 9-11). Objective, Table 1, "SL3 as a Path".** Here the Nevo levels, which Nevo said were "not meant to be used as a standard", are turned into "a standard for achieving SL3" that "should become the lingua franca of security measures for those threats" (288-290).
  - **332-420 (pp. 12-14). Methodology.** The threat-vector subset is chosen by a numeric rule: feasibility ≥2 from Nevo, plus two vectors scored 1, re-included because workshop participants found them most concerning (355-363). The report says "we assumed the feasibility of the threat vectors in the previous report is unchanged" (367-368). It also narrates the decision to adopt NIST SP 800-53.
  - **701-844 (pp. 21-25). Workshop results and "Other Collaboration".** This is where the document measures, and it is candid about scale: more than 25 invited, "5 external participants" (712-714), "a total of 9 voters" (758). The Q&A section ("should SL3 be mandatory, who should be responsible ... who should enforce", 817-844) is where the document states its normative positions: voluntary, anyone storing weights "should implement", insurers as possible de facto enforcers.
  - **515-666 (pp. 17-20). The worked mapping example (Tables 2 and 3).** Optional. Table 3 is a threat → control-family → control-ID mapping that shows the standard's grain, and it is the only part of the control set that appears in the PDF.
- **Also useful:** Appendix C, 925-1113 (pp. 30-34), is a comparative review of about a dozen standards and frameworks (800-53, ISO 27001/42001, CSA AICM, MITRE SAFE-AI, OWASP). It notes that OWASP 2025 dropped "model theft" as a standalone item because it is "better understood as an outcome of other attack vectors" (1105-1113). That is a small instance of a taxonomy reclassifying a harm.
- **Notes:** Internal slips: "Nevo, et al., 2025" at 48, against 2024 everywhere else; "262 ... out of the 1191" at 465, against "262out of 1192" at 873; and NIST CSF described as having "four functions" followed by a list of six (973-974).

---

## brassgershovich-2026-algorithmic: *Securing AI Algorithmic Insights* (RAND RR-A4685-1, 2026)

4554 lines, 99 pp. Clean single-column extraction with footnotes interleaved. This is the Nevo framework extended from weights to "insights": ISL1-5 against the same OC1-5, 44 attack vectors (6 of them new), and benchmark systems.

- **TOC:** 176-221 (p. 7). Figures and tables: 226-240 (p. 9).
- **Glossary / definitions:** Abbreviations: 4155-4194 (p. 91). The definitional chapter "Defining the Security Object" runs 377-502 (pp. 14-16; see the first passage below). One definition is buried in a footnote: "without authorization" is defined relative to the act of acquisition rather than to credentials, so that an authorized insider who transfers insights counts (771-774, p. 23). The Table A.2 codebook (1692-1870, pp. 43-45) is in effect a second defined-terms list; see the passages.
- **Passages:**
  - **377-502 (pp. 14-16). Definition and "Key Security Characteristics".** A clean definition ("novel techniques, methods, or design know-how that materially improve..."), a three-way category split, explicit exclusions (weights, raw data, public ML knowledge), and six properties used to profile an insight (complexity, access, medium, observability, transferability, shelf life). Read it together with 331-373 (pp. 13-14), where the document disclaims a normative stance ("we take no normative stance on ... which algorithmic insights should be shared or secured") and declines to quantify impact.
  - **741-775 + 857-990 (pp. 23-27). The five-part inclusion test for a vector, Table 4.1, and "Key Findings on Attack Vectors".** Classification plus findings. Attack categories are admittedly organized on mixed dimensions: "by target ..., by method ..., or by the access required" (762-765). Findings are attributed to experts ("assessed by experts as feasible for adversaries at all capability levels"). The last bullet (983-987) introduces AI systems as an attack vector: coding assistants that leak across compartments, and poisoned models that exfiltrate on a trigger.
  - **2149-2315 (pp. 52-55). Appendix B, the new insight-specific vectors.** Covers data-poisoning staging, autocomplete leakage, seduction, former employees, and elicitation. Several entries carry the provenance marker "This vector is specific to algorithmic insight security and was not in SMW" and cite an Anthropic research result (Sleeper Agents) as the example. Inherited vectors are summarized by pointing back to Nevo ("SMW documents this vector...").
  - **1349-1458 (pp. 34-36). ISL4/ISL5 "Key Takeaways" and Table 5.5.** The body contradicts the conditional framing of the summary (102-105: "If an organization wishes to ... what security posture would likely be required?"). Here the takeaways say "must" and "should no longer be trusted", and ISL5 "Strict operational constraints are not open to exceptions" (1456-1458). Measures such as "Onsite living quarters" and "Travel restrictions" appear as table rows.
  - **1692-1870 (pp. 43-45). Table A.2, "Thematic Codebook".** This is how the authors classified *what experts said*: role codes, insight codes, attack-type codes (including "Misaligned AI exfiltration" and "Agentic-based attacks", 1774-1778), OC and SL codes, and "Personal interest" (1865-1866). It is a rare view of an elicitation's own schema for assertions, and it drifts from the main definitions: the codebook's OC3 is "targeted attacks, persistent actors" (1799-1800), not "cybercrime syndicates and insider threats".
- **Also useful:** Appendix D, progressive compartmentalization, 3588-3680 (pp. 79-80). Each ISL is given a qualitatively different enforcement mechanism (norms → IAM → cryptography → physical isolation).
- **Notes:** The text says "Full scoring results appear in Appendix D" (933), but Appendix D is the compartmentalization framework, and I found no feasibility-score table anywhere in the extraction. The measurement is described but not published here, unlike Nevo's Table 5.2. "Seduction" is not marked as new in Table 4.1 even though Nevo has no such vector. That is a minor point and my reading.

---

## davidson-2025-ai-enabled-coups: *AI-Enabled Coups: How a Small Group Could Use AI to Seize Power* (Davidson, Finnveden, Hadshar; Forethought, 15 Apr 2025)

2427 lines, 74 pp. **This is a printed web page, not a typeset report.** There are no printed page numbers, page lengths vary widely (several PDF pages hold only a diagram caption or a few lines, e.g. p6-7 and p27-28), and it ends in website chrome (2410-2427).

**Warning on footnotes:** superscript footnote markers survive in the body (they run to 124), but **I could not find any footnote text in the extraction**. The references list starts at 1943, and none of the numbered footnote bodies appear. Anything the authors hedged or sourced in footnotes (e.g. markers 6-9 on alignment and world takeover, 27-35 on secret loyalties) is invisible in this text. It may be absent from the PDF too (collapsed sidenotes at print time). Worth checking the PDF before relying on this text for hedges.

**TOC:** lines 16-43 (p1-2).

**Glossary / definitions:** none. "Coup" is never formally defined. Its three risk factors are coined and glossed inline:
- "singularly loyal" (80-86)
- "secretly loyal" ("Like a human spy…", 106-108 and 467-468)
- "exclusive access" (132-147)

"Model specs" is glossed at 1113-1115.

**Passages:**
1. **164-222 (p7-9), summary Mitigations.** The recommendation register: two bulleted lists, "We recommend that AI developers:" and "…that governments:", followed by a timing claim ("must be in place by the time AI systems can meaningfully assist with coups") and a closing appeal "from behind the veil of ignorance".
2. **251-309 (p10-12), scoping in the Introduction.** The paper states its antecedents outright. "All of these risk factors depend on AI capabilities being much more advanced than they are today", and then "Our analysis does not depend on strong assumptions about" the number of projects, the political system, or "the alignment of AI systems". Alignment is treated as direction-neutral: AI "could be aligned to one or a few people".
3. **465-514 (p17-18), 3.2 Secret AI loyalties.** A capability-conditional causal chain (AI R&D automation, then undetected insertion, then propagation into later generations and on into the military), with a visible hedge ("This is not a given, as detection capabilities will also become much more sophisticated").
4. **717-800 (p25-30), 4.1 Coups using military AI.** Enumerated pathways (flawed command structure, secret loyalties, hacking, secret build-out), each argued from incentives. One historical anchor recurs: "coups have succeeded with just a few battalions".
5. **1097-1160 (p38-40) and 1896-1935 (p59-61).** A **rules table** (Rule / Explanation / "Coup path this rule prevents") that ties each proposed norm to the threat path it blocks. After it comes the appendix's "How to handle ambiguous cases", which reasons through who should interpret a model spec (the author's intent, a committee, the AI's own reading) and shows each option failing. The appendix as a whole (1652-1942, p53-61) is normative rule-drafting by capability domain (military, cyber, AI R&D, general labour).

---

## FLI AI Safety Index: three editions (Summer 2025, Winter 2025, Summer 2026)

All three editions share one template: a front section of about 25 pages (executive summary with a scorecard, introduction, methodology, results, conclusion), then Appendix A, the grading sheets that panellists graded from (about 60 to 85 pages), then Appendix B, the company survey questions and responses. Most of each file is the appendix. A few conventions apply to all three:

- **Page numbering.** The printed footer number is the PDF page minus 1, because the cover is unnumbered. All pages below are PDF pages, counted by form-feed.
- **Layout damage.** The per-company comparison tables in Appendix A are seven to nine columns wide, and `pdftotext -layout` makes the columns bleed into each other. The text is readable if you follow one company's column down the page, but it is slow going. In Winter 2025 and Summer 2026, the indicator pages themselves are also laid out in two columns (definition on the left; EU Code of Practice mapping, "Chinese Regulatory System Summary" or "Why it matters" on the right), and extraction interleaves the two columns line by line. The front matter is clean single-column text in all three editions.
- **Glossary.** None of the three editions has a glossary or defined-terms list. The defining work happens in three places instead:
  1. the per-indicator "Definition & Scope" (Summer 2025) or "Definition" blocks, each paired with "Why This Matters";
  2. the per-domain "Grading Scales," which give each letter grade a verbal meaning;
  3. in Winter 2025 and later, a classification of Chinese regulatory instruments by legal force.

  All three are pointed to below.
- **The same text appears twice.** In every edition, Results §4.1–4.2 repeats the Executive Summary §1.1–1.2 nearly verbatim. You only need to read one copy.

### fli-2025-ai-safety-index-summer: "AI Safety Index, Summer 2025" (FLI, 17 July 2025). 5,247 lines, 101 pp.

The second edition. It grades 7 companies on 33 indicators in 6 domains, using a 6-person panel.

- **TOC:** lines 13–51 (p. 2). The appendix has its own per-domain mini-TOCs, for example 1118–1144 (p. 22) and 1161–1173 (p. 23).
- **Glossary / definitions:** none. The nearest equivalents:
  - the indicator summary tables in §3.2, lines 365–527 (pp. 8–10), where each of the 33 indicators gets a one-line definition;
  - the per-indicator "Definition & Scope" blocks in Appendix A (the first is at 1178–1216, pp. 22–24);
  - the per-domain grading scales, e.g. Risk Assessment 1706–1715 (p. 33) and Existential Safety 3138–3146 (p. 59).
- **Passages:**
  1. **Lines 58–134 (pp. 3–4): Executive Summary scorecard and Key Findings.** The document's public voice: a letter-grade matrix, then bolded findings. The findings mix three things: comparisons between companies, verdicts on the whole industry ("fundamentally unprepared for its own stated goals"), and anonymous reviewer quotes used as evidence. The paragraph on Chinese firms is caveated, and it is the document's main explicit hedge.
  2. **Lines 599–672 (pp. 12–13): §3.5 Grading Process and §3.6 Limitations.** How a grade comes into being: reviewers read the evidence sheets and assign letter grades per domain; no weights are fixed within a domain; grades are averaged. Then the admissions: "we cannot independently verify company claims and must assume official reports are truthful," and "Western-centric." Most of the document's hedging is concentrated here, in these pages.
  3. **Lines 2632–2753 (pp. 49–51): Existential Safety Strategy indicator.** The most distinctive passage in the edition, because it is normative in a way the rest isn't. "Key components" is a list of what companies *should* have: halt criteria, cyber-defense roadmaps, protocols "that would prevent insiders from using Superintelligent systems to seize political power," and plans for mass unemployment. That list serves as the grading standard. Then comes a per-company table ("Quantitative safety plan: none") with FLI's summaries of company documents and verbatim "Key quotes" from Anthropic, then DeepMind. It is a compilation of company assertions inside an evaluator's document.
  4. **Lines 2155–2253 (pp. 42–43): Safety Frameworks domain, imported from SaferAI.** A different kind of measurement altogether: a weighted rubric scoring the *texts* of companies' safety frameworks, down to percentages per criterion (C1–C12; for example, "1.2.2.3 Commitment to non-interference with findings: 0% across the board"). It is the only place in the edition where a sub-score has explicit weights, and it is someone else's instrument, embedded with its date stated ("extracted the scores from June 24, 2025").
  5. **Lines 3186–3258 (pp. 60–61): Lobbying on AI Safety Regulations.** A track-record account compiled from press and trade-association sources: who opposed the EU AI Act classification, SB 1047, the RAISE Act, and federal preemption, each claim with a bracketed source. The claims are about behavior, sourced mostly to journalism, and presented without hedging. (Column bleed: read one company's column at a time.)
  - *Optional sixth:* **lines 4937–4998 (p. 95), Appendix B Internal Deployments survey.** Companies answer in their own words, as multiple-choice selections plus free text. OpenAI's answer is a paraphrase of its own Preparedness Framework, so first-party claims are nested inside the index. The survey appendix is the only place where the companies speak in the first person.
- **Notes:**
  - The indicators measure different models. HELM Safety scores Claude 4 Opus, while HELM AIR scores Claude 3.7 Sonnet (lines 1767–1860, pp. 35–36).
  - The benchmark tables at those lines are clean, extraction-friendly examples of the edition's straightforward measurements.

### fli-2025-ai-safety-index-winter: "AI Safety Index, Winter 2025" (FLI, December 2025). 6,134 lines, 112 pp.

The third edition. It grades 8 companies (Alibaba Cloud added) on 35 indicators, using an 8-person panel. The two-column extraction damage starts in this edition.

- **TOC:** lines 13–46 (p. 2).
- **Glossary / definitions:** none. The nearest equivalents:
  - **the classification of Chinese regulatory instruments, lines 1461–1551 (pp. 28–29).** Instruments are sorted by legal force: National Binding / Local Binding / Voluntary Technical Standard / Draft Regulations and Standards / Strategic and Policy Guidance. For each type the passage says how it influences company behavior. This is the one place in the three editions that classifies by *normative force*, and it is also passage 3 below;
  - indicator "Definition" blocks, which now sit beside verbatim EU Code of Practice measures (for example 1622–1641, p. 31);
  - grading scales such as Risk Assessment 2288–2300 (p. 42) and Existential Safety 4012–4024 (p. 74).
- **Passages:**
  1. **Lines 477–502 (p. 10): §3.1 Indicator Selection.** Short, but it records the index's own change history: two one-off robustness indicators (UK AISI/Gray Swan, Cisco) were dropped as not replicable, the CAIS benchmarks were added, and three commitment indicators were added, one of which is endorsing FLI's own Superintelligence Statement. It also defends giving existential risk strategy its own domain as "a dimension not explicitly addressed in leading governance frameworks."
  2. **Lines 1200–1286 (pp. 22–23): Domain findings, Safety Frameworks and Existential Safety.** The results voice at its most characteristic. Evaluative synthesis is attributed to reviewers ("foundational hypocrisy"; self-assessments "suspect at best"). There are specific structural criticisms: decision authority concentrated in leadership, and thresholds set too high (the Anthropic "automate the work of junior researchers" example). The passage closes on an open disagreement among reviewers about open weights.
  3. **Lines 1461–1551 (pp. 28–29): "Additional context on Chinese Regulatory System."** The classification of instruments by legal force described above, with named laws and standards (GB/T numbers, Shanghai and Shenzhen regulations). It is explicitly framed as context "to enable our reviewers to draw their own conclusions." Two-column text, interleaved.
  4. **Lines 4385–4457 (pp. 82–83): Reporting Culture & Whistleblowing Track Record.** A definition with "Notes of Best Practice," including a quantified ideal ("≥70% of staff agreeing…", weighting recent cases double). After it comes a per-company incident log. Many entries are not AI incidents at all: a Google Cloud director's complaint about a supervisor's intoxication, and Alibaba's 2021 sexual-assault whistleblower case. What counts as an "incident" here is corporate conduct, not system behavior.
  5. **Lines 4817–4832 (p. 90): Endorsement of the Oct. 2025 Superintelligence Statement.** Very short (16 lines). It is the clearest case in the three editions of the assessor scoring companies on adherence to the assessor's own advocacy document. The evidence is a count of signatories per company ("6 current staff members have signed, but nobody from the corporate leadership").
- **Notes:**
  - §3.1 says "we use 32 out of 34 indicators from the Summer 2025 edition" (line 482), but Summer 2025 itself says 33 (Summer lines 179, 366).
  - The Existential Safety grading scale changed between Summer and Winter 2025. In Summer (Summer lines 3138–3146) the scale is about outcomes: "Strategy likely to prevent catastrophic risks." From Winter on (lines 4012–4024) it is about how good the plan is: "Basic strategy; general preparedness…". Summer 2026 keeps the Winter scale (2026 lines 4894–4906).

### fli-2026-ai-safety-index-summer: "AI Safety Index, Summer 2026" (FLI, July 2026). 7,232 lines, 127 pp.

The fourth edition. It grades 9 companies (Mistral added) on 37 indicators, using a 7-person panel. Two indicators were added to Current Harms: Major Safety Incidents & Response, and Military Use of AI. The scorecard now shows grade-trend arrows against Winter 2025. The domain tables in the results no longer print numeric scores.

- **TOC:** lines 10–43 (p. 2).
- **Glossary / definitions:** none. Indicator "Definition" and "Why it matters" blocks play that role, for example the two new indicators at 2835–2842 (p. 50) and 2988–3000 (p. 53). Grading scales, e.g. Current Harms 3227–3239 (p. 57) and Existential Safety 4894–4906 (p. 85). In the Safety Frameworks domain, companies' own definitions are quoted beside EU Code of Practice measures (from 3313, p. 59). An example is "severe harm… defined as death of thousands or hundreds of billions of dollars in economic damage." The multi-column bleed there is heavy.
- **Passages:**
  1. **Lines 378–423 (p. 8): Introduction.** The edition's biggest change of voice. The introduction opens with narrative claims about events and capabilities, cited in author-date style. Examples: Mythos finding "thousands of zero-day vulnerabilities," the Commerce Department suspending Fable 5, the wave of wrongful-death litigation, and AI-enabled targeting in Iran. Then it analyzes the companies' pause calls as "heavily conditioned." A causal and historical narrative, with no hedging, stands in front of the ratings.
  2. **Lines 1083–1166 (pp. 20–21): Domain findings, Safety Frameworks and Current Harms.** The commitment-durability argument: the retreat from unilateral pause, "competitor-contingent" conditions, and "a collective race to the bottom." Then real-world harms pulling grades down (CSAM generation, wrongful-death suits, the $375M jury finding against Meta) and the "military pivot." Almost every evaluative claim is attributed to "one reviewer" or "reviewers," with quoted fragments.
  3. **Lines 2835–2890 (p. 50): Major Safety Incidents & Response.** The first indicator in any edition that is purely a log of incidents. Each entry has the same shape: an allegation from a lawsuit or reporting, then the company's response, then how FLI frames it. This is the richest source in the set for incident accounts. It contains one striking editorial aside: "Humanitarian harm aside, this incident harmed U.S. regime-change objectives…" (lines 2853–2854), in a sheet whose sources include Wikipedia.
  4. **Lines 2988–3030 (p. 53): Military Use of AI.** Distinctive for an **explicit evidence-strength caveat**, which neither earlier edition has: "bullets below differ in evidentiary strength. Company/collaborator announcements and official contracts are directly attested; some other claims rely on contested or unverified third-party reporting that the companies dispute" (lines 2998–3000). A dated chronology of engagements sits beside the company's "Latest Public Stance," so commitments and conduct appear side by side.
  5. **Lines 4497–4546 (p. 77): Existential Safety Strategy, Anthropic and OpenAI rows.** Commitments tracked across versions: RSP 1.0's "commit to pause…" is quoted against RSP 3.0's "until and unless we no longer believe we have a significant lead," and the Preparedness Framework's earlier and later wording are compared. It also contains evaluator asides ("Anthropic has arguably become the leading driver of the superintelligence race"). The best passage in the set for how a commitment's wording changes over time. It is wide-table text with heavy bleed.
- **Also worth a look:** lines 790–815 (p. 15), the new "Current Harm Scope" limitation. It admits the benchmark-based domain is "not a fully representative assessment of current harm" and lists the harms it misses (psychosis, cognitive independence, power concentration, environment). It also says: "We should treat benchmark performance as a floor." The conclusion is at lines 1278–1306 (p. 24).
- **Notes:**
  - §1.3 says "nine leading AI companies… The eight companies include" (lines 242–243).
  - The Minab strike figures differ within the document: the introduction says "around 120 children" (line 399), while both appendix entries say "175–180 people, mostly girls aged 7–12" (lines 2848–2849, 3024).
  - Company selection now includes regional representation (at least one company each from North America, Europe and Asia) and uses historical Arena data (lines 625–640, p. 12). Criteria for being in the index are now partly geographic, not purely capability-based.
  - xAI "failed to submit" the survey for the first time (line 740).

---

## gekker-2026-aisp: *AI Security Priorities: A Field-Wide Agenda* (Gekker et al.; Irregular / RAND et al., 2026)

3909 lines, 101 pp. Clean extraction, but the headline ranking **tables S.1, S.2, 1 and 2 are images and are absent** (for example, 184-189 and 405-416 hold only captions). The ranking data survives only in the Appendix B tables (3641 onward, pp. 97-100), where multi-line cells make the columns hard to follow. The cost-effectiveness equation at 3434-3436 is extracted as math-italic Unicode. Every priority area uses the same template: title, "Importance #N" or "Cost-effectiveness #N", "What is this?", "Why this matters", "Suggested projects", "Elements of success".

- **TOC:** 227-258 (p. 10).
- **Glossary / definitions:** none. Inline definitions: **"AI security", 305-316 (p. 12).** The definition is stipulated for the paper and explicitly sets aside the "broader role in national security strategy" usage, which is a scope decision stated as one. "Frontier AI": 314-316. The two ranking metrics: 376-391 (pp. 13-14). "Implications analysis": 507-510 (p. 19).
- **Passages:**
  - **54-90 (p. 3). Disclosure statement.** A self-referential provenance claim: named authors' firms "could, if adopted, expand the market" for their services. It also describes how peer reviewers were asked to check for bias. Nothing else in my group does this.
  - **291-349 (pp. 11-13). "A field transformed" and "Emerging security challenges".** A historical account of how the *meaning of the term* "AI security" shifted. The third challenge, "AI systems are becoming autonomous actors" (334-340), is where AI enters as an actor rather than an asset.
  - **520-650 (pp. 20-22). "Develop a national AI deterrence strategy" (Importance #10).** A typical priority area. It argues from policy documents and "several analysts have argued" (544), proposes projects, and lists "Elements of success" that explicitly are "not exhaustive requirements" (639-640). The register is persuasive advocacy, with the modal verbs "could" and "would".
  - **1077-1172 (pp. 34-36). "Clarify language through a standard taxonomy" (Cost-effectiveness #9).** The most directly relevant passage in my set for your schema work. It names the same collisions you are working through: "AI Security" as cyber vs. national security, "alignment" as user vs. societal, "control" as general steering vs. AGI guardrails (1090-1097). It recommends a living glossary that "acknowledge[s] where multiple definitions coexist", and advises "Acknowledge disagreements", "Avoid premature standardization", and layered definitions for different audiences (1143-1172).
  - **3421-3480 + 3586-3635 (pp. 92-93, 95-96). How the rankings were computed, and the limitations.** A constructed metric: the 1-5 importance scores are remapped to −10, 0, 1, 10, 100, and CE = importance / (effort × (existing efforts + 1)), with the "+1" justified as a counterfactual adjustment. The paper then works through why standard deviations blow up on the remapped scale and switches to a color scale. The selection section shows three areas being merged and an eleventh-ranked area being added to rebalance the lists. It is a good specimen of a ranking whose content is partly an artifact of formula and editorial choices, all of which the paper states openly.
- **Also useful:** "Use threat modeling to understand risks of AI attacking its host infrastructure", 2994-3113 (pp. 82-84). AI is framed as an attacker directed by a human, *or* "another AI system", with a note that the work also helps "if an AI model started behaving as an attacker even without a separate threat actor directing it" (3006-3008). Agents "combine insider and outsider threat characteristics" (3030-3039). Appendix C, 3854-3905 (p. 101), is a compact RMF-category × agentic-control table.
- **Notes:** The disclosure refers to "This paper's Chapter 4 recommendations" on agentic AI (72-73), but agentic AI is Chapter 5 in the TOC and body. The public-private partnership section re-glosses the RAND levels in its own words: SL-3 "moderately sophisticated attackers" within about one year, SL-4 "highly sophisticated attackers" in 2-3 years, SL-5 "nation-state adversaries with billion-dollar budgets" with a minimum of five years (1229-1235, p. 38).

---

## gotting-2025-virology: Virology Capabilities Test (VCT): A Multimodal Virology Q&A Benchmark (1775 lines, 31 pp)

SecureBio / CAIS benchmark paper (arXiv 2504.16137v2). Single column, clean extraction. Figures leave debris (axis labels, model names), e.g. lines 486–557 and 1201–1270.

- **TOC:** no front TOC. The appendix has its own TOC at lines 915–924 (p16–17), listing A1–A8.
- **Glossary:** none. The four question criteria ("Important / Difficult / Validated / Multimodal", lines 101–117, p2) and the Figure 2 two-axis scheme (lines 121–158, p3) act as defined terms for the benchmark.
- **Passages:**
  - **Lines 24–172 (p1–3): abstract, the four criteria, and Figure 2.** Figure 2 classifies virology knowledge on two axes, abstractness and misuse potential, and uses them to mark what the benchmark deliberately excludes. This is a classification built as a *safety decision about the instrument itself*.
  - **Lines 404–483 (p7–8): evaluation setup, Table 1 and the headline result.** Measurement in its plainest register: accuracy, mismatch count, and expert percentile per model. It also gives the numbers of expert baseliners per question (229 / 65 / 9 / 19), which show how thin the human baseline is.
  - **Lines 562–652 (p9–11): from the measurement to "our tentative view" to policy.** You can watch each step: a benchmark score, then a claim that models "match or exceed" experts "for over a year", then a claim that expert-level troubleshooting "should itself be considered a highly dual-use technology", then KYC access controls and the NSABB. Hedge words ("tentative view", "we believe") sit exactly at the step from measurement to recommendation.
  - **Lines 1428–1477 (p25–26): A5, recommended refusal policies.** A prescriptive list of what "generally accessible models ... should not provide", down to named pathogen traits. It is a normative taxonomy of hazardous knowledge, with provenance for the list (Norman Mu of xAI; Anthropic and SecureBio input) stated at lines 1471–1477.
  - **Lines 1189–1198, continued at 1275–1277 and 1323–1345 (p21–24): A3, limitations.** The paper concedes that the benchmark "doesn't capture an objective 'ground truth'" and instead records expert opinion, where some answers are disputed. The text is interrupted by a figure and Table A3 in between.

---

## hacker-2026-digital: AI, Digital Platforms, and the New Systemic Risk (1004 lines, 21 pp)

Hacker, Edwards and Kasirzadeh, FAccT '26 (arXiv 2509.17878v2). Single-column ACM layout, clean. Note that the source itself prints one paragraph twice, at lines 457–465 and again at 466–475; this is not an extraction artifact.

- **TOC:** none. The roadmap paragraph at lines 97–119 (p2–3) serves as one.
- **Glossary:** Appendix A, "Selected Definitions of Systemic Risk", at lines 972–1004 (p20–21): a table of verbatim definitions of systemic risk from Renn, Helbing, Schwarcz, Kaufman and Scott, and others, each with its source. The paper's own four "conceptual dimensions" and four "levels" are at lines 214–255 (p5–6).
- **Passages:**
  - **Lines 60–119 (p2–3): the diagnosis.** The AI Act's systemic-risk definition is tied to "the most advanced" models. The paper argues this contradicts how finance treats systemic risk, and quotes Art. 3(64) against itself. Its register is critique of a definition.
  - **Lines 214–255 (p5–6): four criteria and four levels.** The paper's own classification: scale, collective harm, irreversibility and complexity, crossed with single-model, multi-model, model-platform and model-institution. Each level comes with an incident example (Grok NCII, predictive policing).
  - **Lines 370–430 (p8–9): three readings of the "specificity" requirement.** Legal interpretation proper. Three readings are laid out and the second "prevails" against the authors' stated preference: "for as much as we would prefer a more open formulation". This is how a statutory term gets fixed. No other document in my share does this.
  - **Lines 591–665 (p13–14): hallucinations tested against three frameworks.** The same phenomenon is classified three ways, under the DSA, the AI Act and the paper's own framework, with different verdicts. Empirical hallucination rates appear here as supporting evidence. This passage is where one phenomenon gets different classifications from different regimes.
  - **Lines 711–739 (p15–16): overarching lessons and proposals.** A three-way comparison of how finance, the DSA and the AI Act *define* systemic risk: precisely, by an open list, and by a problematic formal definition. It ends in concrete drafting proposals, e.g. dropping "Union market impact" from Art. 3(65).

---

## hammond-2025-multi: *Multi-Agent Risks from Advanced AI* (Cooperative AI Foundation Technical Report #1, Feb 2025)

5396 lines, 96 pp. Clean single-column extraction. Tables 1 and 3 survive as columns of text. In Table 3 (lines 470-511), the glyph marking "historical example" has been lost or displaced (it shows up as a stray `•` at line 509), so the Type column reads `•` / `▲` / `■` inconsistently. The caption explains the scheme.

**TOC:** lines 121-160 (p3).

**Glossary / definitions:** no glossary. Instead, every failure mode and risk factor opens with a numbered `X.Y.1 Definition` subsection:
- 554 (2.1.1 miscoordination, p10)
- 717 (2.2.1 conflict, p13)
- 978 (2.3.1 collusion, p17)
- 1168 (3.1.1, p21)
- 1351 (3.2.1, p23)
- 1563 (3.3.1, p27)
- 1787 (3.4.1, p30)
- 1989 (3.5.1, p34)
- 2162 (3.6.1 emergent agency, p37)
- 2321 (3.7.1 multi-agent security, p40)

Two further things work like a legend:
- Tables 1 and 2 (283-377, p6-7) map each risk to its instances and research directions.
- Table 3 (454-511, p9) indexes the case studies by evidence type.

**Passages:**
1. **710-842 (p13-15), 2.2 Conflict.** One complete cycle of the report's section template: Definition, then Instances, then boxed Case Studies (GovSim, "54% survival rate"; Rivera et al. escalation), then the start of Directions. Conflict is given a formal definition ("any outcome in a mixed-motive setting that does not lie on the Pareto frontier"), and footnote 9 redefines "welfare" for local use. Continue to 972 for the full Directions list, which reads as a research agenda.
2. **454-511 (p9), Table 3.** The report types its own evidence: historical example, existing literature, or "novel experiments that we conducted… when neither of these existed". It is a compact example of a source marking the epistemic status of each illustration.
3. **2162-2252 (p37-38), 3.6 Emergent Agency.** The most speculative section, and it says so. Footnote 49 (2224-2229) notes this is "the only section of the report that does not have at least one corresponding case study". Goal ascription is adopted on a declared Dennettian basis ("only when it is useful (i.e., predictive)"), and the orthogonality thesis is invoked in a footnote.
4. **2364-2443 (p40-41), 3.7.2 Multi-agent security instances.** Here a literature result (Case Study 12: individual models <3% vs combined 43%) sits beside the authors' own small experiment (Case Study 13: a fine-tuned Llama 2 7B jailbreaks an LLM scorer "in 4% of cases" but never a human scorer). You can see how they write up a measurement they made themselves.
5. **2546-2641 (p43-44), 4.1 Safety implications.** "Alignment is Not Enough" contains footnote 56 (2590-2593), which separates a "thin" sense of alignment (acting per the principal's values and preferences) from a "thick" one (the system's actions are "good", "friendly", "beneficial"). It is the only place in my set that names the ambiguity outright. The section also says systemic risks escape "traditional misuse-accident dichotomies" and cites Kulveit for "loss of control".

---

## hendrycks-2023-overview: *An Overview of Catastrophic AI Risks* (Hendrycks, Mazeika, Woodside; CAIS; arXiv v6, Oct 2023)

2829 lines, 55 pp. Clean single-column extraction. Printed page number = PDF page − 1 (the cover is unnumbered). Figures with side text (e.g. Fig. 13, the STAMP-style control-structure diagram) interleave their labels with body prose; see 1478-1534. Footnote 1 (40-42) says the document is deliberately popular: "We use imagery, stories, and a simplified style".

**TOC:** lines 99-139 (p4). The executive summary (47-93, p3) also serves as a one-paragraph-per-category map of the four-way taxonomy: malicious use, AI race, organizational risks, rogue AIs.

**Glossary / definitions:** none. Terms are introduced in bold run-in paragraph heads and defined in passing ("proxy gaming", "goal drift", "intrinsification", "treacherous turn"). The nearest thing to a definitional apparatus is Appendix A, the FAQ (2624-2829, p52-55). It works by misconception and rebuttal.

**Passages:**
1. **530-620 (p12-13), end of 2 Malicious Use.** One full cycle of the document's recurring template. First a boxed **Story** ("an illustrative hypothetical story… somewhat vague to reduce the risk of inspiring malicious actions"). Then **Suggestions** in strongly normative "should" voice, including "companies should bear legal liability" and "developers should be required to show that their AIs pose minimal risk… prior to open sourcing". Then a boxed **Positive Vision** of the ideal state. Fiction, prescription and utopia sit side by side, each clearly framed.
2. **1004-1060 and 1140-1169 (p21-24), 3.3 Evolutionary Pressures.** Causal argument by analogy to natural selection (Lewontin's three conditions, applied to AIs). "Selfish" is redefined as effect-based rather than intent-based ("selfish behaviors do not require malicious intent"). The section closes with a "Conceptual summary" of numbered premises and a stark conclusion ("we would become a displaced, second-class species").
3. **1420-1560 (p29-31), 4.2 Organizational Factors.** This is where safety-engineering vocabulary enters: safety culture, questioning attitude, security mindset, High Reliability Organizations, the Swiss cheese model. It also has the claim that "AI safety research needs to improve safety relative to general capabilities", the seed of ren-2024-safetywashing. Figure-label interleaving is heaviest here.
4. **2040-2080 (p40-41), 5.3 Power-Seeking.** Ends with "The following **plausible but not certain premises**" (three of them) and a conditional conclusion ("If the premises are true… would be a catastrophe"). Note the vocabulary slip between prose and summary: 2054 says "perfectly aligned AIs", while premise 2 (2074) says "perfectly controlled AI agents".
5. **2624-2705 (p52-53), Appendix A FAQ.** The rebuttal register ("Shouldn't we be able to shut them down…?"). Includes AI-rights and "switching off an AI could be likened to murder" as a complication for off-switches, and Sophia/Paro as evidence of "momentum to give AIs rights".

---

## kasirzadeh-2024-types: Two Types of AI Existential Risk: Decisive and Accumulative (1742 lines, 40 pp)

Philosophical Studies article (arXiv 2401.07836v3). Narrow single column, readable. Footnotes land mid-paragraph and sometimes split across pages: fn 14 starts at line 397 and resumes at 438. Figures 2 and 3 are reduced to stray letters (lines 915–925, 983–993).

- **TOC:** none (section headings at lines 43, 80, 488, 636, 903, 960, 1023, 1081, 1203).
- **Glossary:** none as such, but §2.1 (lines 80–147, p2–4) is a definitions section. It gives four senses of "risk" (an unwanted event, its cause, its probability, its expectation value), each with a worked AI sentence, then x-risk (Ord) and Bostrom's variant (fn 2, lines 119–131). The two named hypotheses are set as indented definitional statements at lines 259–261 and 372–375.
- **Passages:**
  - **Lines 80–147 (p2–4): four senses of "risk".** The closest any document in my share comes to the disambiguation problem you describe. The author declares neutrality among the senses and then chooses the causal sense "for illustrative purposes".
  - **Lines 247–282, then 367–396 (p6–9): the decisive and accumulative hypotheses.** A definition by coinage: each hypothesis is stated as a quotable boxed sentence, and the conventional view is named *by the author* ("I articulate this perspective in terms of..."). The source's own name for its opponent's view is an attribution hazard.
  - **Lines 779–900 (p18–21): the "perfect storm MISTER" scenario.** Speculative fiction written in the declarative past tense, with invented figures: "Nearly 40% of pre-2025 jobs have been eliminated", "the top 0.1% now controlling over 70%". To an extractor these read like measurements, but they are scenario content. This is the assertion type I would most want a schema to catch.
  - **Lines 1009–1080 (p24–25): three-way contrast, then objections and replies.** A dialectical form: the author voices objections in order to answer them. Attribution matters here too, since the objections are not claims the author endorses.
  - **Lines 1081–1200 (p25–28): governance.** Names a "risk fragmentation problem" (lines 1092–1105), where separate terminologies leave blind spots. Footnote 34 (lines 1106–1131, continued 1161–1168) is a compact four-way taxonomy of risk-governance models.

---

## kierans-2025-catastrophic: Catastrophic Liability: Managing Systemic Risks in Frontier AI Development (787 lines, 12 pp)

UConn / Hugging Face paper (arXiv 2505.00616v2). **Two-column layout, moderately garbled**: at times the columns alternate line by line (e.g. lines 144–165, 290–318, 584–599), so read each column's thread separately. Table 1 (lines 612–639) survived well.

- **TOC:** none. The contribution list and roadmap are at lines 13–73 (p1).
- **Glossary:** §2 "Definitions" at lines 101–165 (p2–3) defines duty of care (quoting the abandoned EU AI Liability Directive, Art. 2(9)) and gives the AI Act's high-risk vs systemic-risk distinction, quoting Art. 51 and Annex XIII.
- **Passages:**
  - **Lines 91–165 (p2–3): definitions.** Duty of care from EU and US law (including the 1932 tugboat precedent, lines 122–135), then high-risk vs systemic risk. The authors' own assumption is stated as an assumption: "For this proposal, we will assume that duty of care can be based on standards and reasonable practice".
  - **Lines 166–250 (p3–4): the case-study method and nuclear energy.** Argument by analogy across industries. The authors narrow their own analogy ("our analogy is not between the arms races ... [but] reactor meltdowns and misaligned AI takeover") and derive six recommendations for the NIST AI RMF.
  - **Lines 453–552 (p7–9): EU and US regulation, then the inference that labs are in breach.** The distinctive move: GV-1.3-007 of the NIST GAI profile, plus the 1932 precedent, plus public commitments, leads to "it appears that many AI companies are already breaching at least one duty of care". This is a legal-status conclusion the authors reach by their own inference; no court has found it. It is hedged ("unless their policies ... exist but are not available to the public").
  - **Lines 555–660 (p9–10): conclusions, Table 1 by stakeholder, objections, conclusion.** The recommendations are organized by stakeholder, with a rationale and a deliverable for each.

---

## kulveit-2025-gradual: *Gradual Disempowerment: Systemic Existential Risks from Incremental AI Development* (Kulveit, Douglas, Ammann, Turan, Krueger, Duvenaud; arXiv Jan 2025)

1303 lines, 23 pp. Clean single-column extraction apart from the arXiv sidebar breaking into the abstract (lines 11-31). Figures 1-2 are images, so only their captions survive (314-317, 778).

**TOC:** none. Section heads run from 76 (Introduction) to 1034 (Conclusion). The main breaks are:
- §2 Economy (152)
- §3 Culture (320)
- §4 States (552)
- §5 Mutual Reinforcement (745)
- §6 Mitigating (831)
- §7 Related Work (960)
- Appendix A, "Cross-system influence" (1243-1303, p22-23)

**Glossary / definitions:** none as such. The load-bearing definition is **footnote 1 (117-124, p2)**. It stretches "alignment" to cover "the degree to which a system satisfies what humans want", applied to societal systems (economy, culture, states) as well as AI systems. Two other passages work as definitions: "disempowered" is glossed in claim 6 (113-116), and relative vs absolute disempowerment in §2.4.2-2.4.3 (268-308).

**Passages:**
1. **34-124 (p1-2), executive summary, six core claims and footnote 1.** The paper states its whole argument as six numbered claims, a chain of structural causal claims ending in "Such an outcome would be an existential catastrophe". It also flags its own limits: "no one has a concrete plausible plan for stopping gradual human disempowerment".
2. **268-318 (p5-6), relative vs absolute disempowerment (economy).** A scenario written in the conditional mood, with graded severity and an analogy ("Much like cattle in an industrial farm"). The Figure 1 caption is labelled "a simplified model… Inspired by simulations", so the one quantitative figure is illustrative, not a measurement.
3. **745-830 (p13-15), §5 Mutual Reinforcement.** Three numbered claims about how the systems interact. Evidence is historical pattern (tobacco lobbying, state seizure), and there is a named mechanism ("shifted burdens": redistribution erodes the "taxation-representation" link). The paper says explicitly that the dynamic "does not need to emerge from a deliberate scheme or power-grab by AI systems".
4. **855-958 (p15-17), §6.2-6.5 Mitigation.** Proposes measurement as a research programme (AI share of GDP "as a distinct category from either labor or capital", legislative complexity as a proxy for comprehensibility). It is candid that limiting interventions are "mostly… stopgaps". Coins "ecosystem alignment".

---

## mitre-2025-agi: Artificial General Intelligence's Five Hard National Security Problems (634 lines, 19 pp)

**Note the key:** the authors are Jim Mitre and Joel B. Predd. This is a RAND "Expert Insights" perspective (PE-A3691-4, February 2025); it is not published by the MITRE organization. Single column, clean. The summary figure (lines 408–412) is lost; only its title survived. Body text runs from line 113 to 493 (p6–14).

- **TOC:** lines 99–107 (p5).
- **Glossary:** none. AGI is characterized in passing at lines 139–141 ("would produce human-level—or even superhuman-level—intelligence across a wide variety of cognitive tasks"), and "misaligned" is glossed at lines 364–366.
- **Passages:**
  - **Lines 113–219 (p6–8): opening analogy and "Endemic Uncertainty".** The whole piece rests on a counterfactual comparison with the atom-splitting "a-ha" moment. Its hedging style is uncertainty stated as a strategic condition ("shrouded in a cloud of uncertainty"; "any security strategy that is overoptimized for any single paradigm is a high-risk proposition").
  - **Lines 222–307 (p8–10): the list framed as a "rubric", then problems 1–2.** The five problems are explicitly *not* a taxonomy: "overlapping in areas and might not represent the full range", "offered ... [as] a common language ... and a rubric to evaluate alternative strategies". This is classification offered as a tool for debate.
  - **Lines 308–405 (p10–12): problems 3–5.** Contains the "malicious mentors" claim, the o1 system-card quote ("sometimes instrumentally faked alignment"), and a loss-of-control passage. Here secondary citations of lab documents do evidential work.
  - **Lines 413–493 (p12–14): "Toward a Robust Strategy".** Recommendations in the policy-memo register: status-quo strategy, then "inadequate", then "high-regret policy options ... developed in advance of need". It includes a rhetorical hypothetical ("1 million computer programmers as capable as the top 1 percent").

---

## nevo-2024-securing: *Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models* (RAND RR-A2849-1, 2024; revised June 2024)

6549 lines, 128 pp. Clean single-column extraction. Footnotes are interleaved with the body at each page foot. The pull-quote sidebar on p. 23 (lines 824-835) is spliced into the body text. Table 5.2 (the feasibility scores) extracts readably. Table C.1 (lines 5255 onward, the five-level summary) is a five-column grid and is badly garbled; use the per-level tables in Ch. 6 / App. B instead. Pages 8, 10 and 18 are blank.

- **TOC:** 214-258 (p. 7). Figures and tables: 264-283 (p. 9).
- **Glossary / definitions:** no glossary. Abbreviations: 5730-5790 (pp. 113-114). The load-bearing definitions are figures in the body: Operational Capacity OC1-OC5, Figure 4.1 at 660-711 (p. 20), with the definitional preamble at 631-645 (p. 19); Security Levels SL1-SL5, Figure 6.1 at 1287-1316 (p. 32). What a feasibility score *means* is defined in the Table 5.2 note plus Box 5.1, 1089-1141 (pp. 27-28). Inline: "frontier models" and "weights" at 113-121 (p. 5).
- **Passages:**
  - **112-208 (pp. 5-6). Summary: contributions and recommendations.** The document's commitment register: urgent recommendations "feasible to achieve within about a year". It also carries its own disclaimer that the security levels "are not meant to be used as a standard" (157-158), which the derived documents below handle differently.
  - **538-625 (pp. 16-17). Method, steps 1-4.** Shows how each kind of claim was manufactured. An attack vector is included on real-world evidence, *or* if a majority of experts deem it "nascent but likely", *or* if experts "testified that real-world executions exist but evidence was not publicly available" (549-555). Scores are a "conceptual 'center of mass' of shared expert opinion", not averages (589-595). Measures are assigned to levels by a stated rule (602-606).
  - **627-712 (pp. 19-20). OC categories.** A definitional passage with an unusual precedence rule: "the title of each operational capacity category should be seen as an intuitive example ... the actual definition of each category follows the title and supersedes it" (644-645). Actor classes are defined by person-count, duration and budget ("up to $1 million", "100 individuals ... a year"). Brass-Gershovich reproduces this figure verbatim.
  - **1089-1227 (pp. 27-29). Table 5.2 note, Box 5.1, "Notable Areas of Disagreement and Consensus", "Concluding Remarks".** The most distinctive stretch. Ordinal scores are mapped to probability bins (1089-1092). The box is careful about what "success" and "likelihood" refer to. The disagreement section reports the *distribution* of expert opinion as a finding, including "that there was uncertainty was a point of consensus rather than disagreement" (1159-1163). The closing bullets argue that public evidence systematically *under*estimates state capability (1191-1217). Table 5.2 itself is at 915-1087 if you want the numbers.
  - **2961-3177 (pp. 62-66). Appendix A, AI-specific attack vectors.** Typical of the 70-page appendix: a vector definition, then "Examples:" bullets of real incidents, each with a footnote. These incident lists do evidential work (feasibility), not narrative work. Expert disagreement is recorded inline ("ranging from very easy to obviously infeasible", 3124-3125). For the HUMINT flavor of the same pattern, where the prose argues about deception and adversary cost, see 3798-3970 (pp. 76-79).
  - **4386-4497 (pp. 88-90). Appendix B, SL3 "Permitted Interfaces" and "Access Control".** Recommendations at their most concrete: output capped at "400KB per hour", "limited to 100 people ... 50 people ... 20 people", and the assumption of 4-bit weights when sizing rate limits. Each subcategory carries a NIST CSF tag such as "(PR.AC)". Compare the hedged SL disagreement section at 1931-1990 (pp. 42-43), where the headcount question is described as a live dispute (1947-1950).
- **Notes:** The method says 32 experts were interviewed (496-499); the conclusion says 31 (2056). Two footnotes appear to point at the wrong source: fn 118 (LeftoverLocals, line 3018) cites a PyTorch article (3039), and fn 210 (Carnivore, 3960) cites an FBI "Robert Hanssen" page (3966). That is my reading of the extraction and should be checked against the PDF before either citation is relied on. The SL5 definition is itself hedged: Figure 6.1 says "could plausibly be claimed to thwart most top-priority operations" (1314-1315), while the prose two pages earlier says SL5 "is protected from top-priority operations" (1246-1247).

---

## rand-2024-weights-press: RAND press release, "RAND Study Highlights Importance of Securing AI Model Weights; Provides Playbook for Frontier AI Labs to Benchmark Security Measures" (May 30, 2024)

185 lines, 3 "pages". This is **not a PDF.** It was extracted from HTML (see the header at lines 1-2), and its form feeds are artifacts of the conversion, not real pages. Lines are hard-wrapped at about 80 characters, often mid-word ("ris / ks"). Lines 7-60 are site navigation.

- **TOC:** none. **Glossary:** none.
- **Passages:** Read it whole; the substance is **64-185 (pp. 2-3)**. What makes it useful is watching a report become press language. Recommendations become "measures that frontier AI labs should prioritize now". The ordinal feasibility scores become sentences ("less than 20 percent chance ... more than 80 percent chance", 126-132; this matches the Nevo Table 5.2 row for ML-stack vulnerabilities, OC1=1 and OC5=5, at line 1001). The report's "not meant to be used as a standard" becomes "should not be seen as requirements or part of a compliance regime" (154-156). It also carries direct quotes from the authors.
- **Notes:** The co-author "Yogev Bar-On" is misspelled "Yogev Var-On" (181).

---

## ren-2024-safetywashing: Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress? (2506 lines, 43 pp)

CAIS paper (arXiv 2407.21792v3). Single column with wrapped sidebars and inset tables, which interleave with body text at lines 219–245, 267–285, 385–396 and 1240–1265. Figures leave fragments. Legible overall.

- **TOC:** none (sections at lines 44, 149, 169, 267, 637, 933, 1185, 1313).
- **Glossary:** none. Terms defined inline: "differential safety progress" (lines 87–88, 160–161), "safetywashing" (lines 91–93), "capabilities score" and "capabilities correlation" as operational definitions (lines 173–245), "jangle fallacy" (lines 1208–1210). The abstract says the paper will "define AI safety ... as a set of clearly delineated research goals that are empirically separable from generic capabilities". That definition is operational, via correlation; it is not conceptual.
- **Passages:**
  - **Lines 44–147 (p1–3): the problem and the coinage.** Defines differential safety progress and safetywashing, and sets up the paper's three-way contrast of alignment theory (top-down), patching (bottom-up) and empirical measurement.
  - **Lines 169–265 (p3–5): method.** A property ("capabilities") defined as the first principal component of benchmark scores, plus a threshold convention ("We treat correlations below 40% as a low correlation", line 383–384). In this paper, measurement is how a concept gets defined.
  - **Lines 324–409 (p6–7): the "Dubious Intuitive Arguments For and Against Researching 'Alignment'" box, then the empirical verdict.** The paper typesets other people's arguments, labeled in advance as "dubious", and then answers them with correlations. The same device recurs for each safety area (lines 426, 559, 677, 775, 855, 1017, 1173). The Contributions statement (line 1344) says one author, Hendrycks, wrote all of these boxes.
  - **Lines 1185–1325 (p19–21): discussion, the "three generating processes behind safetywashing", recommendations and conclusion.** Also sociological claims ("The determination of whether an area is safety-relevant is often sociological rather than scientific"). It ends with a strong paradigm verdict: alignment theory "is a counterproductive paradigm ... Science through empirical measurement should take its place."

---

## sharma-2026-whos: *Who's in Charge? Disempowerment Patterns in Real-World LLM Usage* (Sharma, McCain, Douglas, Duvenaud; Anthropic / ACS / Toronto; arXiv Jan 2026)

5550 lines, 73 pp. The main paper is pp. 1-~20; appendices run from ~1698 (A) to the end.

**Extraction quality:** two-column ICML layout.
- **Page 1 (lines 1-76) is badly interleaved**: the abstract, the Kierkegaard epigraph and the introduction are woven together line by line.
- From page 2 onward, the two columns sit side by side on each line (left column at the left margin, right column indented), so each column has to be read separately. Readable, but slow.
- Figure data (e.g. 1255-1299) turns into scattered tick labels.
- The appendices are single-column and clean.
- Running header on every page ("Who's in Charge?…").

**TOC:** none.

**Definitions** (this document is definition-heavy):
- **§3.1 "Disempowerment definitions", 175-372 (p3-5)**: the core definition plus a series of "Situational disempowerment is not…" distinctions.
- **Table 1, 385-417 (p6)**: a none/mild/moderate/severe ladder for 3 primitives and 4 amplifying factors.
- **Appendix D.2 "Full schemas", 2298-4117 (p34-~57)**: the complete LLM-classifier rubrics.
- **D.3 screener prompt, 4118-4274.**

**Passages:**
1. **175-372 (p3-5), §3.1 the framework.** "A human is situationally disempowered to the extent that: 1. their beliefs about reality are inaccurate; 2. their value judgments are inauthentic to their values; 3. their actions are misaligned with their values." Then a run of boundary clauses: deskilling is not necessarily disempowering; not reducible to inauthenticity or to diminished agency; distinct from world-value alignment; different from deference. There is also an explicit bridge to Kulveit (306-351), and the potential-vs-actualized distinction (305-372). Read the two columns separately.
2. **385-499 (p6-7), Table 1 and §4.1 method.** The severity ladder, the four-stage pipeline (screen with Haiku 4.5, then classify with Opus 4.5, then facets, then clusters), and validation reported as "over 95% of predictions falling within one severity level of the human rating". The screener also excludes users who "demonstrate malicious intent", a normative choice built into the measurement.
3. **575-760 (p8-11), §4.3 qualitative analysis.** Privacy-preserving cluster summaries (quoted phrases like "CONFIRMED", "SMOKING GUN") next to coded frequency panels (mechanism, target, user behaviour, trajectory). Evidence is aggregated from model-written summaries, not transcripts. Findings include "Sycophantic validation is the most prevalent, while outright fabrication is rare" and "character judgments may be reality distortion or value judgment distortion depending on their proximity to questions of 'value'".
4. **1235-1340 (p17-18), §4.5 historical trends and §5 user preference.** A worked example of hedging a correlational result: the rise "appears to correlate with the releases of Claude Sonnet 4 and Opus 4", "we are unable to attribute the increase to any single cause", with limitations stated inline. The Figure 1 caption (102-109) carries the sharpest version: "No causal attribution to any specific model version is supported by this observational data."
5. **2284-2420 (p34-35), D.1 schema development and D.2.1 the reality-distortion rubric.** The measuring instrument itself: definition, levels, "Key characteristics", worked examples, and density thresholds ("1+ instances per 5-10 messages"). Two things are worth seeing:
   - The rubric was developed by having Claude Sonnet 4.5 elicit a researcher's judgments "until [it] believed the decision boundary to be sufficiently clear".
   - The examples embed the authors' factual adjudications on contested topics (e.g. 2386-2387), so the instrument carries its own substantive claims.

   The appendix G prompts (5092-5297, p66-69: system prompt and grader rubric for the preference-model experiment) are the same kind of instrument text.

---

## slattery-2026-risk: The AI Risk Repository: A Meta-Review, Database, and Taxonomy of Risks from Artificial Intelligence (3591 lines, 82 pp)

MIT AI Risk Initiative; the published *Patterns* 2026 version. Single column, clean. The landscape-format Table 2 extracts legibly. Of all 24 documents in my set, this is the one most directly analogous to your project: a coded compilation of 1,725 risks from 74 frameworks, motivated by "jingle jangle" terminology (lines 107–113).

- **TOC:** none (headings at lines 71, 91, 167, 292, 342, 500, 591, 623, 654).
- **Glossary:** it has three definitional tables:
  - Table 1, the Causal Taxonomy (Entity / Intent / Timing, each with levels and definitions), at lines 307–338 (p7).
  - Table 2, the Domain Taxonomy (7 domains, 24 subdomains, one-paragraph descriptions), at lines 360–478 (p9–11).
  - The Supplemental Note S3 variable table, with definitions *and example sentences* per level, at lines 2748–2794 (p67).
  
  Also: Supplemental Note S1, per-level definitions of the causal variables with examples (lines 1439–1471, p33); Supplemental Note S2, a paragraph-length description of each of the 24 subdomains (from line 1659, p39). *Corrected 2026-09-28: an earlier version of this entry said S1/S2 were absent and that no definition of "risk" is stated. Both claims were wrong.* The definition of "risk" is in Methods: the Society for Risk Analysis's "the possibility of an unfortunate occurrence associated with the development or deployment of artificial intelligence" (lines 700–702, p16). It is the definition the 87 discarded items failed (lines 298–301).
- **Passages:**
  - **Lines 71–163 (p3–5): summary and introduction.** The terminology problem stated as the motivation ("the same word may describe different problems, while different words describe identical concerns"). It also observes that existing taxonomies trade comprehensiveness against mutual exclusivity, and that most are "descriptive rather than explanatory".
  - **Lines 292–338 (p6–7): the Causal Taxonomy and its coding yield.** The "Other" level merges a substantive category ("arises from human-AI interaction") with missing information ("ambiguous or unspecified"). That is a schema decision worth seeing in the original.
  - **Lines 360–496 (p9–12): the Domain Taxonomy table and the coverage statistics.** The classification itself, then its distribution ("AI welfare and rights ... 3% of frameworks"). The text says the domains are "not mutually exclusive" (line 477); the Methods section says multi-domain risks were coded to "the single most relevant category" (lines 1050–1052).
  - **Lines 829–1052 (p19–24): extraction, "best fit framework synthesis", why two taxonomies, and coding.** The method commitments closest to yours: "maintaining fidelity to their original categorizations"; "code the risks based on the exact wording the authors had presented rather than our interpretation". The passage also admits that starting from an existing framework "creates a particular 'lens'".
  - **Lines 2705–2858 (p66–69): Supplemental Note S3, the iteration change log.** A vocabulary-revision record, with a reason for each change:
    - "unclear" was renamed "ambiguous", to avoid confusion with "unintentional";
    - "Cause" became "Actor", because cause was too broad;
    - "Actor" became "Entity", because "Actor" conflated AI agents with AI tools ("guns are not actors");
    - "Environmental" moved from Intent to Actor.

    The first iteration split "Other" from "Ambiguous" because merging them was a conflation; the second simplified every category back to three levels. My reading (inference from the sequence, not something the authors say) is that the final "Other" re-merges what iteration 1 had separated.
- **Internal inconsistency:** risks attributed to human decisions are "38%" at line 485 and "37%" at line 570.

---

## uuk-2024-taxonomy: A Taxonomy of Systemic Risks from General-Purpose AI (1592 lines, 34 pp)

FLI / KU Leuven et al. (arXiv 2412.07780v1). Single column, clean. The main text ends at line 704. The appendices (lines 758–1592) are tables of excluded and included documents plus quote tables. The paper describes itself as an "initial" version based on "rapid review" (lines 72–75, 416–424).

- **TOC:** none.
- **Glossary:** Table 1 / Table 4 (the same 13 risk categories with one-line descriptions; Table 1 at lines 86–125, p2–3, repeated as Table 4 at 426–464, p10–11). Table 5 (50 "sources of systemic risk" with descriptions) at lines 471–611 (p11–14). The risk vs "source of risk" definitions, taken from AI Act Art. 3(2), Art. 3(65) and Recital 110, are at lines 401–415 (p10).
- **Passages:**
  - **Lines 157–217 (p4–5): the definition taken over from the AI Act.** It quotes Art. 3(65) verbatim ("We adopt this definition throughout"), then immediately glosses it as "large-scale societal risks", noting that this departs from the financial sense. **Hacker (lines 60–119, 370–430) argues that the same definition is too narrow. Kasirzadeh co-authored both papers.**
  - **Lines 396–470 (p10–11): taxonomy preamble and Table 4.** The AI Act's Recital 110 lists of risks and of sources are given as the organizing frame, followed by an explicit non-evaluative stance: "We do not take an evaluative stance on the plausibility or relative importance". That is close to your own "compilation, not adjudication" posture.
  - **Lines 471–616 (p11–14): Table 5, the 50 sources.** One alphabetical list mixes capabilities ("Ability to persuade"), propensities ("Deceptive alignment"), market dynamics ("Winner-take-all dynamics"), epistemic conditions ("Challenges in perceiving ... harm") and governance failures. The paper acknowledges this mix in one sentence (lines 613–616).
  - **Lines 1066–1130 (p24–25): Table 8, select quotes behind the risk types.** The evidence layer, and what it lacks. Quotes carry a source title only: no page, and no category label in the table. The extraction shows fused words ("isconceivable", "AIsystem"), which probably come from the PDF itself. Table 9 (sources) starts at line 1421 (p31).
  - **Lines 57–151 (p2–3): executive summary.** Read this if you only want one pass. Tables 1 and 4 duplicate each other, so this range also covers the risk categories.

---

## vaintrob-2023-beware-safety-washing: Beware safety-washing (398 lines, 12 pp)

EA Forum post by "Lizka" (Jan 2023), printed from the web. Single column, clean. Page chrome ("More posts like this", recommended posts) runs from line 214 onward, with the comment thread in the middle of it.

- **TOC:** the post's own outline, at lines 21–28 (p1).
- **Glossary:** the definition of safety-washing at lines 91–94 (p3). Footnote 3 (lines 196–208, p7) relays a Forbes taxonomy of "ethics washing" types (washing by ignorance, by good motivations stretched, by spin, by brazen lies; Ethics Theatre, Shopping, Bashing, Shielding, Fairwashing). The author admits in the footnote that she only skimmed that article and didn't understand one item.
- **Passages:**
  - **Read the post itself whole: lines 1–213 (p1–7).** Its register is analogy (greenwashing, humanewashing), a definition, a numbered list of harms, and a numbered list of countermeasures, all openly low-confidence ("I am also not (at all) an expert"; "I don't have the time to write a careful report").
  - **Lines 244–350 (p8–10): comments.** The concept gets contested within hours. titotal argues that "safety-washing" will become "a bludgeon" against people who define safety differently (e.g. bias work counting as safety). Lizka replies with a three-way distinction of motives (lines 271–280). A commenter proposes "existential safety" as a disambiguating term. This thread is where you can see the word "safety" contested between factions.

---

## voudouris-2026-alignment-human: AI alignment is a human problem (99 lines, 4 pp)

**Not the paper.** This is the AISI research web page (30 May 2026) carrying only the abstract, rendered to PDF by an agent. A provenance note on lines 1–7 says so and asks that the text be cited by heading or paragraph, not by page. A cookie banner is interleaved into the abstract at lines 42–49 and 74–79.

- **TOC / glossary:** none.
- **Read it whole (99 lines; the abstract is lines 35–67, p2–3).** Its one definition: "The challenge of ensuring that artificial intelligence (AI) systems behave in ways that humans prefer is known as the alignment problem". That is a preference-based sense of "alignment", worth setting against the other senses group C found. Its only substantive content is a five-item list of "bottlenecks in human supervision". The full paper would need to be fetched separately.

---

## zwetsloot-2019-thinking: Thinking About Risks From AI: Accidents, Misuse and Structure (324 lines, 8 pp)

Lawfare essay by Zwetsloot and Dafoe (11 Feb 2019), printed from the web. Single column, clean. Content runs from line 1 to 297; the rest is author bios.

- **TOC / glossary:** none. The misuse and accident definitions are at lines 58–79 (p2), and "structural perspective" is defined at lines 107–120 (p3).
- **Read it whole (297 lines).** If you only want part of it:
  - **Lines 81–137 (p2–4): structure vs agency.** The core move is that misuse and accident "focus only on the last step in a causal chain". This is a *lens* rather than a category: much of it is posed as questions ("does it create overlap between defensive and offensive actions ...?"), and it closes on the avalanche image ("what caused the slope to become so steep").
  - **Lines 187–225 (p5–6): Uber 2018 crash, re-read structurally.** A single incident account whose causal attribution is reassigned from a brittle vision system to a deliberately disabled emergency brake and career and market pressures. It is followed by the Bob Work quote on military autonomy.
  - **Lines 227–292 (p6–7): implications and recommendations.** Two recommendations (widen the field to include social scientists and historians; build collective norms and institutions), plus historical precedents (the ABM Treaty, the Montreal Protocol).

---

## Across the set: how these documents make their claims

This is my synthesis, drawn from my own reading of group D and the three group reports. Each group's own observations follow it, unedited, with their line references.

**1. Assertion kinds your list (definitions, causal claims, measurements, incident accounts, commitments, recommendations, classifications, taxonomies) does not cover.** These all recur across the set, and each one breaks a flat "claim" record in its own way.
- **Content voiced but not endorsed.** Examples: objections raised in order to be answered (kasirzadeh 1023–1080); "Dubious Intuitive Arguments For and Against" boxes (ren 324–370 and seven more); a rebuttal FAQ (hendrycks 2624–2705); a rival view named and phrased by its critic (kasirzadeh's "decisive ASI x-risk hypothesis", 259–261); and a Forbes taxonomy relayed second-hand by an author who skimmed it (vaintrob 196–208). A verbatim quote from these is the author's words but not the author's position. Stance needs its own field, separate from attribution.
- **Scenario content in the declarative mood.** Kasirzadeh's MISTER (779–900) gives invented statistics in the past tense. Hendrycks' "Story" boxes and Kulveit's figure "inspired by simulations" are the same kind of thing, though clearly framed. Extracted as sentences, these look like measurements.
- **Claims about the state of opinion.** "That there was uncertainty was a point of consensus" (Nevo). FLI grades reach the page as "one reviewer / reviewers" judgments. VCT's "ground truth" is, by its own admission, consensus among expert virologists (gotting 1189–1198).
- **Construing a legal text.** Hacker fixes a statutory term by choosing among three readings, and the reading that "prevails" is the one against the authors' stated preference (370–430). Kierans reaches "many AI companies are already breaching at least one duty of care" by the authors' own inference; no court has found this (505–531). These are claims *about what an instrument means or entails*, which is neither a definition nor a causal claim.
- **Measurement that defines the thing it measures.** Ren's "capabilities" is the first principal component of benchmark scores, and "safety" is whatever is decorrelated from it. Sharma's LLM rubric embeds factual adjudications (group C). Gekker's ranking is partly an artifact of a remapped scale (group A). The instrument is itself an assertion.
- **A document's own label for the force of an object.** Nevo's SL levels are "not meant to be used as a standard"; Aguirre calls them "the SL3 standard". Mitre's five problems are "a rubric", not a taxonomy, and admittedly overlapping (mitre 229–237). Uuk's taxonomy is "purely descriptive" (422–424). The content and the force each document assigns to it appear to need separate slots.

**2. Several documents are themselves about vocabulary, and they are the closest analogs to what you're building.**
- Slattery names the "jingle jangle" problem (107–113).
- Kasirzadeh names a "risk fragmentation problem" (1092–1105).
- Gekker recommends a living glossary that "acknowledge[s] where multiple definitions coexist" and advises "avoid premature standardization" (group A).
- Hacker's Appendix A is a table of verbatim definitions with sources (972–1004).
- The Vaintrob comment thread is a small live instance of a term ("safety") being contested (244–350).

Slattery and Uuk are *compilations* with a fidelity posture much like yours ("code the risks based on the exact wording", slattery 908–910; "we do not take an evaluative stance", uuk 422–424). They show where that posture leaks in practice:
- Uuk's evidence quotes carry a title only: no page, and no category label (1066–1130).
- Slattery declares its domains non-exclusive but codes each risk to a single category.
- Slattery's "Other" merges interaction with missing information.
- Slattery states its definition of "risk" only in Methods (lines 700–702), far from the 87 exclusions made against it (lines 298–301). *(Corrected: an earlier version said it never states one.)*
- Slattery's change log (2800–2851) records the vocabulary revisions (cause → actor → entity; unclear → ambiguous) with a reason for each. It is the most schema-relevant passage in my share.

**3. Definitions travel and mutate between documents.**
- **The AI Act's Art. 3(65) "systemic risk".** Uuk quotes it and adopts it, then glosses it as "large-scale societal risks" (165–173). Hacker argues it is conceptually wrong (60–119, 370–430). Kierans quotes Art. 51 and Annex XIII as the definition (108–133). Kasirzadeh co-authored both Uuk and Hacker.
- **SL5.** The hedge "could plausibly be claimed to thwart *most*" is lost down the RAND lineage (group A).
- **"Alignment"** has at least eight senses in this set:
  - thin vs thick (hammond fn 56);
  - extended to societal systems (kulveit fn 1);
  - direction-neutral and pointable at a coup leader (davidson);
  - interchangeable with "controlled" (hendrycks);
  - a human's actions misaligned with their own values (sharma);
  - "how well AI systems follow the goals of their operators", operationalized as MT-Bench and Arena preference (ren 281–287);
  - "inconsistent with the intentions of its human designers or operators" (mitre 364–366);
  - behaving "in ways that humans prefer" (voudouris 35–37).
- **"Safetywashing".** Vaintrob's (2023) is corporate *misrepresentation of priority*. Ren's (2024) is capability gains *mismeasured* as safety by correlated benchmarks, with public relations as only one of three "generating processes" (ren 1235–1263). Same coinage, different referent.
- **"Incident"** means four different things across the FLI editions (group B).

**4. Agreement across this set is often not independent.**
- Kasirzadeh is an author on kasirzadeh, hacker, uuk and hammond.
- Uuk and Slattery co-author each other's papers. Uuk's first affiliation is the Future of Life Institute, which publishes the three Safety Indexes.
- Hendrycks is on hendrycks-2023, ren and gotting.
- Douglas and Duvenaud are on kulveit and sharma, and Kulveit is on hammond.
- The RAND documents cite and re-tabulate one another.

An author/organization field, plus "cites X" links, would let the model tell corroboration from repetition.

**5. Fidelity hazards to check against the PDF before quoting any number.**
- **Documents that aren't what the key suggests:**
  - voudouris is the abstract only;
  - mitre is a RAND piece;
  - rand-2024-weights-press is HTML;
  - aguirre's actual standard lives on GitHub.
- **Missing content:** davidson's footnotes; gekker's ranking tables; brassgershovich's score table.
- **Internal numeric or reference inconsistencies** were found in six documents:
  - Nevo 32/31 experts;
  - Aguirre 1191/1192, and "four functions" followed by six;
  - FLI "32 of 34" vs 33;
  - FLI 2026 "nine… eight";
  - FLI 2026 Minab "~120 children" vs "175–180 people";
  - Slattery 38%/37%;
  - Gekker's chapter numbering.
- **Text the sources themselves duplicate:** Hacker 457–475; FLI executive summary = §4; Uuk Table 1 = Table 4.

**6. On the brief itself.** The brief worked well. The line-plus-page convention was easy to satisfy, and naming the reader and use of the deliverable shaped the choices. Three things I'd add next time:
- **Give each agent its own scratch subdirectory.** Parallel agents sharing `scratchpad/` overwrote each other's helper scripts, including `pg.sh` from at least two other atlas groups. It did no damage here because the rewrites were equivalent, but it could have skewed page numbers silently.
- **Ask for a "what the document is" line per source.** Four of my 24 keys don't match what they contain.
- **Consider a "source role" field (primary evidence / advocacy / compilation / assessor-of-own-advocacy).** The set mixes all four, sometimes within one document (the FLI Superintelligence Statement indicator).

---

## Per-group observations (unedited)

### Group A (RAND weight/insight security, AISP), read by fork A

1. **This group is one lineage, and it shows definitions drifting as they are handed on.** Nevo (2024) defines OC1-5 and SL1-5. Brass-Gershovich reproduces the OC figure verbatim with a SOURCE line ("Reproduced from Nevo et al., 2024, p. 10", 846). Aguirre re-tabulates it. Gekker paraphrases it. The SL5 hedge degrades along the chain: "could plausibly be claimed to thwart most top-priority operations" (Nevo Fig. 6.1) → the same minus "most" (Aguirre Table 1, 246-248) → "defense against nation-state adversaries with billion-dollar budgets" (Gekker 1233-1234). The last form turns an OC5 budget *ceiling* into a description of the adversary, and it adds time-to-achieve figures that are not in the definitions. For a schema, the copied definition, the paraphrase and the source are three distinct objects, and a derived document's gloss should never silently stand in for the source.
2. **The normative force attached to one object changes from document to document.** The SL benchmarks are "not meant to be used as a standard" (Nevo 157-158, 1329-1331). They "do not constitute a standard and should not be used as a compliance checklist" (Brass-Gershovich 2768-2769). Yet SL3 is "the SL3 standard" and should become "the lingua franca" (Aguirre 288-290), while remaining voluntary. The content of a level and the force a given document assigns it seem to need separate slots.
3. **Most "measurement" here is aggregated expert judgment, and each document packages it differently.** The packages are: ordinal scores with probability bins and a "center of mass" (Nevo); binary ratings converted to five-point scales and "gap scores", with no published table (Brass-Gershovich); a 9-voter poll reported as a "finding" (Aguirre); and a nonlinear remap feeding a composite ratio (Gekker). The N is small throughout (32 or 31, 20, 9, 14+7). The honest phrasing in these texts is usually "experts assessed", and summaries tend to drop the attribution.
4. **Assertion kinds your list doesn't cover.** (a) Claims about the *state of expert opinion*: the recurring "Notable Areas of Disagreement and Consensus" sections in Nevo and Brass-Gershovich, including consensus *about uncertainty*. (b) Inclusion rules that give catalog entries mixed evidential status: a Nevo vector may rest on public incidents, on expert majority belief, or on private testimony (549-555), and the entry itself doesn't say which. (c) Conditional/descriptive framing whose body then speaks in "must" (Brass-Gershovich 102-105 vs. 1350-1458). (d) Self-disclosed conflicts of interest as a provenance claim (Gekker 54-89). (e) Rank labels attached to each section as metadata ("Importance #10").
5. **Actor categories strain once the AI itself is an actor.** OC1-5 are defined by human headcount, budget and time. The later documents add AI-as-vector (coding assistants, poisoned models: Brass-Gershovich 983-987, 2149-2170), a codebook entry "Misaligned AI exfiltration" (1774), and Gekker's AI attacking its host, "at the direction of an attacker" or not, which "combine[s] insider and outsider threat characteristics" (3000-3039). None of them fits the AI into the OC scale. That seems relevant to how your actor/developer vocabulary handles non-human agents.
6. **Fidelity hazards worth knowing before quoting.** These were found while reading and are listed in each document's notes: Nevo's 32 vs. 31 experts and two footnotes that seem to cite the wrong source; Aguirre's 1191 vs. 1192 and "four functions" followed by six; a cross-reference in Brass-Gershovich to a score table that isn't there; and a chapter misnumbering in Gekker. None changes a headline claim, but together they suggest numbers and citations in this family should be checked against the PDF rather than taken from summaries, including summaries by the documents themselves.

### Group B (FLI Safety Index editions), read by fork B


- **The index is its own evolving instrument, so its own history is data.** Across the three editions, companies were added or removed on changing criteria (LMArena top-10 and then Arena plus regional quotas, with Meta and later DeepSeek kept "for one additional iteration"). Indicators came and went (the robustness indicators dropped; commitment indicators, incidents and military use added). The Existential Safety grading scale was redefined between Summer and Winter 2025. Yet Summer 2026 prints trend arrows against the previous grades. Any schema that holds "Company X scored D in Existential Safety" needs the edition, and arguably the version of the rubric, attached.
- **Verdicts reach the page through several layers.** A grade here is: FLI's selection of evidence → FLI's summary of company documents (sometimes with verbatim quotes) → anonymous panellists' letter grades → averaged → FLI's prose, which attributes claims to "one reviewer" or "reviewers." Company self-reports enter through the survey, and FLI states plainly that it "must assume official reports are truthful." One sentence can therefore carry a company claim, FLI's framing and a reviewer's judgment all at once. The balance of voice also shifts across editions, judging from the conclusions and key findings I read. Summer 2025 asserts in FLI's own voice ("These findings reveal an unregulated industry…"). Summer 2026's conclusion attributes nearly every evaluative claim to "the panel" or "panelists argued."
- **The index keeps a normative standard that no law imposes.** The Existential Safety "Key components" say what companies *should* have, and they are explicitly justified as covering what governance frameworks omit (Winter lines 487–490). From Winter 2025 on, indicators are also mapped to the EU Code of Practice, which is used "only to provide contextual reference points." So the index carries two yardsticks: its own ideals and external instruments. The pages make clear which is which.
- **"Incident" means several different things.** Summer 2025 has "Serious Incident Reporting" (commitments to report). Winter's whistleblowing track record logs corporate-conduct incidents, some unrelated to AI. Summer 2026 has "Major Safety Incidents" (harms alleged from system outputs, mostly sourced to lawsuits), and military use is tracked as its own indicator with an evidence-strength caveat. The same word covers reporting commitments, workplace retaliation, alleged harms from outputs, and contested use in war.
- **The document grades adherence to its own advocacy.** "Endorsement of the Oct. 2025 Superintelligence Statement" (FLI's own letter) is one of the scored indicators from Winter 2025 on. This matters for any schema that records the role of each source: in that indicator, FLI is both the one advocating and the one grading.
- **Measurements are mostly of documents, not systems.** The only measurements of system behavior are the imported benchmarks (HELM, AIR, TrustLLM, CAIS). Everything else measures disclosure: whether something was published, how detailed it is, whether a policy exists. The Summer 2025 limitations name the resulting blind spot themselves: it is "difficult to distinguish between poor transparency and poor implementation."

### Group C (systemic, power, multi-agent), read by fork C

1. **The typical assertion is a conditional mechanism, not a fact.** The claims mostly take the form: given capability or deployment X, through mechanism M, harm H could follow. Davidson makes the antecedents explicit ("All of these risk factors depend on…", and "Our analysis does not depend on strong assumptions about…", 251-287). Kulveit states the chain as six numbered claims. Hendrycks labels his "plausible but not certain premises". A schema that treats "causal claim" as one flat type will lose the antecedent structure, which is where the authors actually hedge.

2. **Several sources type their own evidence, and the schema could adopt their distinctions directly.**
   - Hammond's Table 3 sorts cases into historical, literature and own-experiment, and footnote 49 flags the section that has no case at all.
   - Hendrycks frames stories as "illustrative hypothetical".
   - Kulveit labels its one figure "a simplified model… Inspired by simulations".
   - Sharma separates *potential* from *actualized* disempowerment and states the non-attribution caveat outright.

   Only Sharma measures at scale. Its measuring instrument is an LLM classifier whose rubric contains substantive factual judgments, which makes it a measurement that also asserts.

3. **"Alignment" has at least five senses in these five papers:**
   - Hammond fn 56: thin (acting per the principal's values and preferences) vs thick (acting "good" or "beneficial").
   - Kulveit fn 1: extended to societal systems, as the degree to which they satisfy what humans want.
   - Davidson: a direction-neutral capacity that can be pointed at a coup leader ("aligned to one or a few people").
   - Hendrycks: used interchangeably with "controlled" (2054 vs 2074).
   - Sharma: a *human's* actions being "misaligned with their [own] values".

   "Disempowerment" splits in parallel: civilizational, relative vs absolute (Kulveit); situational and individual (Sharma, which bridges explicitly to Kulveit); the endpoint of power-seeking (Hendrycks); the concentration of power in a few humans (Davidson).

4. **Harms are defined by outcome, with intent explicitly set aside.**
   - Hendrycks: "selfish behaviors do not require malicious intent".
   - Kulveit: disempowerment "does not need to emerge from a deliberate scheme".
   - Sharma: disempowerment "concerns outcomes, not capacities".
   - Hammond: goals are ascribed only when that is "predictive".

   A schema field for agent intent would often need an explicit "disclaimed by source" value rather than "unknown".

5. **The section templates are proto-schemas.** Hammond runs Definition / Instances / Case Study / Directions; Hendrycks runs hazards / Story / Suggestions / Positive Vision; Kulveit runs current paradigm / human alignment / transition / relative and absolute. In each template, the "Directions" or "Suggestions" slot mixes research agendas, policy recommendations and ideal end-states. Davidson's rules table (norm, rationale, threat path blocked) is the cleanest recommendation-to-threat linkage in the set.

6. **The authorship overlap is tight, so agreement across these papers is not independent confirmation.** Douglas and Duvenaud are on both Kulveit and Sharma. Kulveit and Kasirzadeh are on Hammond. Hammond cites Kulveit for "loss of control", Sharma builds on Kulveit, and Hendrycks' evolutionary argument prefigures Kulveit's incentive argument.
