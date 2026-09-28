# Source atlas: EU and international instruments

*Family: the EU AI Act and its amendment, the GPAI Code of Practice (Safety and Security chapter) and its chairs' statement, Commission guidelines and the serious-incident template, commentary on the Code; international and consensus documents (G7 Hiroshima, OECD, Singapore Consensus 2025 and 2026, UN advisory body), Canada's and Japan's safety institutes and code.*

*Compiled 2026-09-28 by a guide agent for the schema redesign. Line numbers refer to the `pdftotext -layout` files at `/private/tmp/claude-505/-Users-josephwecker-v2-src-aisi-eoi/f462f375-61ba-4d02-b4e6-ae440173656f/scratchpad/src-text/<key>.txt`. A citation like "cop 1530" in cross-references means line 1530 of that document's file. The short aliases are: act = eu-2024-ai-act, omnibus = eu-2026-digital-omnibus-ai, guidelines = ec-2025-gpai-guidelines, cop = eu-cop-2025-safety-security, chairs = eu-cop-chairs-2025-statement, template = ec-2025-gpai-serious-incident-template, tfs, g7, oecd = oecd-2024-future-ai-risks, perset, sg2025 / sg2026 = the two Singapore Consensus files, un = unhlab-2024-governing, jaisi. "p" numbers are PDF pages counted by form-feed (the first line of a page is the line that carries the `\f`), not the page numbers printed in the document; where the two differ I say so. One-liners after each range are signposts, marked as my reading.*

*Global extraction note: superscripts collapse in this family. `1023 FLOP` in the text means 10^23, `1025` means 10^25, `109` is 10^9. Footnote markers likewise fuse onto the preceding word ("developingFootnote 1", "Report 20255"). Keep this in mind anywhere a number sits next to a unit.*

---

## At a glance

| key | what it is | lines / PDF pp | extraction | TOC | glossary |
|---|---|---|---|---|---|
| eu-2024-ai-act | Regulation (EU) 2024/1689 | 9196 / 144 | clean | none (map given) | Art. 3, 3132–3435 |
| eu-2026-digital-omnibus-ai | Reg. (EU) 2026/1744, amends the Act | 2700 / 41 | clean | none (map given) | amends Art. 3, 953–973 |
| ec-2025-gpai-guidelines | Commission GPAI scope guidelines | 1487 / 36 | clean; numbering drift in source | 29–66 | none (inline notions) |
| eu-cop-2025-safety-security | Code of Practice, S&S chapter (PDF) | 1826 / 43 | clean; figures lost | none (map given) | 1136–1375 |
| eu-cop-chairs-2025-statement | chairs' statement **plus a second copy of the chapter** | 2183 / 52 | noisy inline numbers; one textual divergence | none | 1375–1653 |
| ec-2025-gpai-serious-incident-template | reporting form | 68 / 2 | clean | none | none |
| hoffmann-2025-eu-code-safety | CSET commentary | 452 / 10 | double-spaced | none | none |
| tfs-2025-protecting-gpai | open letter | 173 / 4 | clean | none | none |
| g7-2023-hiroshima-code-of-conduct | G7 voluntary code | 348 / 8 | clean | none | none |
| oecd-2026-haip-reporting-v2 | reporting questionnaire | 616 / 9 | top-level Q numbers lost | none | roles, 10–24 |
| oecd-2024-future-ai-risks | OECD Expert Group foresight | 3632 / 69 | clean; **ranking charts lost** | 100–172 | none |
| perset-2025-how-managing-risks | OECD synthesis of HAIP reports | 1613 / 36 | clean; ragged table | 145–171 | 1404–1522 |
| ecosystem-2025-singapore | Singapore Consensus 2025 | 1839 / 40 | contributor grid scrambled | 5–37 | 338–395 |
| ecosystem-2026-2026 | Singapore Consensus 2026 **plus Agentic companion** | 4812 / 99 | clean body | 7–58 | 667–736 |
| unhlab-2024-governing | UN HLAB final report | 6064 / 101 | **two columns interleaved** | 60–114 | abbreviations only |
| ised-2023-voluntary-code-genai | Canada voluntary code (web) | 250 / 4 | web chrome | none | footnotes 193–202 |
| caisi-ca-2026-landing | CAISI landing page (web) | 160 / 4 | web chrome | none | none |
| caisi-ca-2026-evaluators-share | CAISI blog on evaluation reporting | 337 / 7 | web chrome | none | none |
| jaisi-2025-national-status | J-AISI status report (translated) | 933 / 25 | chapter numbers lost; translation | 15–57 | "AI Safety" box, 72–79 |

Where a document reads well whole, I say so rather than choosing passages.

---

# EU instruments

## eu-2024-ai-act

**Regulation (EU) 2024/1689 (Artificial Intelligence Act), Official Journal L, 12.7.2024.** 9,196 lines, 144 PDF pages. PDF page equals the printed "N/144" page throughout. Clean extraction: single column, with an OJ running header and footer on every page (`ELI: http://data.europa.eu/eli/...`, `OJ L, 12.7.2024`), and footnotes inline at page bottoms.

**TOC:** none; the Official Journal prints no contents page. A structural map, from the headings:
- Citations and recitals (1) to (180): lines 17–3015 (p1–44). Recitals (97)–(117) on GPAI models are at 1733–2057 (p26–31).
- Chapter I, general provisions (Art. 1–4): 3016 (p44). Chapter II, prohibited practices (Art. 5): 3450 (p51). Chapter III, high-risk systems (Art. 6–49): 3615 (p53). Chapter IV, transparency (Art. 50): 5579 (p82). **Chapter V, general-purpose AI models (Art. 51–56): 5641 (p83).** Chapters VI–XIII: 5965, 6451, 6770, 6811, 7656, 7739, 7794, 7988. GPAI enforcement powers (Art. 88–94) are at 7486–7661 (p110–113); GPAI fines (Art. 101) at 7947 (p117).
- Annexes I–XIII: 8328–9196 (p124–144). Annex XI (GPAI technical documentation) at 9069; Annex XII (information to downstream providers) at 9138; Annex XIII (designation criteria) at 9171.

A one-line article index can be regenerated by matching lines of the form `Article N` followed by the title line.

**Glossary:** Article 3, "Definitions", lines **3132–3435 (p46–50)**: 68 numbered definitions. Of note for the schema: (2) `risk` (3142), (3) `provider` (3144), (4) `deployer` (3148), (49) `serious incident` (3331), (63) `general-purpose AI model` (3411), (64) `high-impact capabilities`, (65) `systemic risk`, (66) `general-purpose AI system`, (68) `downstream provider` (3432). There is no definition of "developer", "AI model" (bare), "incident" (bare), "safety", "alignment" or "control"; "provider" is defined as the one who "develops … or that has … developed and places it on the market". Several more terms are defined in passing in recitals, e.g. recital (97) on models versus systems.

**Passages**
1. **Lines 1912–2031 (p28–30), recitals (110)–(115).** The Act's causal and risk-descriptive voice. Recital (110) is the only place the Act gestures at loss of control ("unintended issues of control relating to alignment with human intent"), and it reuses the G7 Hiroshima risk list nearly word for word, including "self-replicating" and a "chain reaction … up to an entire city". Recital (111) explains *why* compute is a proxy. Recitals are non-binding interpretive text, which is a status distinct from the articles.
2. **Lines 5641–5961 (p83–87), Articles 51–56.** The binding core for frontier models: classification by presumption (10^25 FLOP) or designation, notification and rebuttal, the four Art. 55 duties (evaluate, assess and mitigate, report serious incidents, cybersecurity), and codes of practice as a route to showing compliance. It shows the legal-conditional register: "shall", "may", "presumed", "until a harmonised standard is published".
3. **Lines 3456–3614 (p51–53), Article 5, prohibited practices.** A different mode from everything else in the family: outright bans defined by purpose and effect ("materially distorting the behaviour … appreciably impairing their ability to make an informed decision"), each with carve-outs. Worth seeing because "manipulation" appears here as a prohibited use of a *system*, whereas the Code treats "harmful manipulation" as a systemic risk of a *model*.
4. **Lines 3796–3878 (p56–57) with 4083–4143 (p60–61), Articles 9 and 14.** The high-risk-system template of risk management ("residual risk … judged to be acceptable", risks "which may be reasonably mitigated or eliminated through … design") and human oversight ("automation bias", a "'stop' button … to come to a halt in a safe state"). This is the Act's system-level safety vocabulary, which the GPAI chapter does not reuse.
5. **Lines 9138–9191 (p143–144), Annexes XII–XIII.** Enumerated criteria: what documentation downstream providers get, and the designation criteria (parameters, data, compute or its proxies, modalities, benchmarks, "level of autonomy and scalability, the tools it has access to", and 10,000 registered business users as a presumption of reach). The classification-by-indicator mode in its barest form.

## eu-2026-digital-omnibus-ai

**Regulation (EU) 2026/1744 (Digital Omnibus on AI), amending the AI Act, OJ L, 24.7.2026.** 2,700 lines, 41 PDF pages. The PDF page equals the printed "N/41". Clean single-column OJ layout, like the Act.

**What kind of document this is:** almost every operative sentence is an *edit instruction* against another text ("in Article 56, paragraph 6 is replaced by the following: '…'"). The quoted replacement text is what becomes law; the surrounding sentence is a pointer. So its assertions are deltas on eu-2024-ai-act, and reading the Act alone after July 2026 gives a partly superseded picture. Most of it concerns high-risk systems, sandboxes, conformity assessment and dates; "general-purpose AI model" occurs only seven times. The GPAI chapter (Art. 51–55) is essentially untouched. Art. 56(6) moves the adequacy assessment of codes of practice from "the AI Office and the Board" to "the Commission, taking utmost account of the opinion of the Board".

**TOC:** none. Map: recitals (1)–(47) at lines 44–880 (p1–15); "HAVE ADOPTED THIS REGULATION" at 883; Article 1 (amendments to the AI Act, numbered points (1)–(43)) at 888–2499 (p15–38); Articles 2–3 amend aviation (2018/1139) and machinery (2023/1230) rules, 2500–2675; Article 4 (entry into force) at 2676.

**Glossary:** no standalone section. It amends the Act's Art. 3 at lines **953–973 (p16)**: a redefined `safety component` (now keyed to "intended purpose"), plus new `SME` and `SMC`. Recital (7), lines 129–142 (p3), explains the redefinition.

**Passages**
1. **Lines 200–307 (p4–6), recitals (10)–(13), the new prohibition on non-consensual intimate material and CSAM.** For your purposes this is the densest specification of what a "safeguard" is anywhere in my set. It lists technical measures ("data cleaning, refusal training, safe prompt design and output controls, runtime prompt guardrails, content classification and filtering mechanisms, … abuse detection …"), sets an adequacy standard ("align with the state-of-the-art … demonstrably prevent or sufficiently reduce … likelihood"), and splits provider from deployer liability. It also uses "providers retaining effective control over AI systems", which is "control" in the sense of provider control over a deployed system. Carve-outs are drawn with unusual anatomical and legal precision.
2. **Lines 1072–1133 (p18), the binding text of the same amendment (Art. 5(1)(ba)–(bb), 1a, 1b) and new Art. 6(1a)–(1c).** Read this against passage 1 to see how a recital's reasoning becomes a two-limb legal test ("intended purpose" *or* "reasonably foreseeable and reproducible outcome … without requiring significant technical modification, and … does not have reasonable and adequate technical safety measures").
3. **Lines 552–597 (p10) with 1679–1777 (p26–28), recitals (31)–(32) and amended Art. 75.** The AI Office gains exclusive competence over *systems* built on GPAI models where model and system come from "the same provider, or … providers forming part of the same undertaking", and over AI in very large online platforms. This is where the model/system and provider/undertaking lines get redrawn, which bears directly on "developer".
4. **Lines 717–753 (p12–13), recitals (40)–(41).** The justificatory voice of an amending act: delays attributed to late standards and authorities, and new dates. Recital (41) states that codes of practice under Art. 56(6) "have limited legal effect, and in particular do not grant a presumption of conformity". That sentence contradicts hoffmann-2025-eu-code-safety (see its entry).
5. *(Optional)* **Lines 2346–2495 (p36–38), new Annex XIV.** AIP/AIB/AIH codes, a "multi-dimensional typology of AI systems" built for notified-body scoping: a regulator-made classification with its own code namespace. The technology axis (2430–2486) ends with AIH 0301 "generative AI systems, including AI systems based on general-purpose AI models" and AIH 0401 "other emerging AI technologies … including Agentic AI". As far as I noticed, this is the only place in the EU legal texts of my set where "agentic" appears.

## ec-2025-gpai-guidelines

**Commission Guidelines on the scope of the obligations for general-purpose AI models established by Regulation (EU) 2024/1689, Annex to C(2025) 5045 final, 18.7.2025.** 1,487 lines, 36 PDF pages. The printed page number is one less than the PDF page (the cover is unnumbered), so printed p.3 is PDF p4. Clean extraction. Paragraphs are numbered (1)–(144), which makes a better anchor than pages.

**Extraction and source quirks:** exponents are flattened (`1023 FLOP` is 10^23, `1025` is 10^25). In the source itself, a bullet inside the worked-examples box received a paragraph number, "(21)" at line 326. Every internal cross-reference after that point appears to be off by one: para (63) sets the modifier threshold but para (67) calls it "the criterion set out in paragraph 60", and para (71) points to "paragraph 31" for notification contents that are in (32). The Model D figure is 1.6·10^23 in the list (1428) but 1.663·10^23 in the worked calculation (1465). These are small, but relevant if anyone anchors by paragraph number.

**TOC:** lines **29–66 (p2–3)**.

**Glossary:** none as a section. It re-quotes the Act's definitions where it uses them (GPAI model at 175, systemic risk at 403, provider / placing on the market at 660–672) and adds the Commission's own working notions: "lifecycle" begins at "the start of the large pre-training run" (para 23, lines 352–365, with a footnote defining "large pre-training run" at 388–391); "training compute" versus "cumulative training compute" (para 118, lines 1306–1312); "access / usage / modification / distribution" for open-source licences (paras 79–82, lines 969–990); what counts as "monetisation" (paras 85–89).

**Passages**
1. **Lines 162–340 (p6–9), §2.1, "When is a model a general-purpose AI model?"** This shows the document's signature move. The statutory definition is admitted to be uncheckable (para 13); an *indicative criterion* is set (10^23 FLOP plus language, text-to-image or text-to-video output) with a stated rationale ("an imperfect proxy"); either direction is rebuttable "exceptionally"; then a box of worked in-scope and out-of-scope examples, each resolved by applying the criterion. It is classification by presumption plus exemplars, in the Commission's self-described interpretive voice (see para 9 at 131–139: "not binding … only the CJEU … Nevertheless … on which it will base its enforcement action").
2. **Lines 499–607 (p13–15), §2.3.3, contesting classification.** The burden-of-proof and evidential side: what arguments a provider may make ("forecasted benchmark results (for example based on scaling analyses)"), that "high-impact capabilities" is a moving target (para 38: "does not consider it to refer to a fixed level"), and para 40: mitigations "are not suitable grounds" to escape classification, because the model "still poses systemic risks". That sentence separates *risk posed* from *risk remaining after mitigation*, a distinction the schema will need.
3. **Lines 777–858 (p19–21), §3.2, downstream modifiers.** When fine-tuning makes you a "provider": the one-third-of-original-compute criterion, with a causal justification ("the original provider cannot reasonably foresee the change in systemic risk posed by such modifications"). Footnote 12 (lines 790–793) makes "who has the control over the model's weights" the test of who counts as the modifier. This is the richest treatment of the role question behind "developer" in my set.
4. **Lines 1149–1210 (p28–29), §5.2, supervision and enforcement.** Para (103), lines 1169–1178, states the AI Office's reading that "serious incident" for GPAI covers "serious cybersecurity breaches … including the (self-)exfiltration of model parameters". The Act's own serious-incident definition (Art. 3(49)) has no such limb. The Code of Practice carries the same extension (eu-cop-2025-safety-security line 1055, and a definition of "(self-)exfiltration" at 1315), so this is the Commission and the Code reading a machine-agency case into a system-harm definition. The powers list and fine ceiling follow.
5. **Lines 1288–1370 (p32–33), Annex A.1–A.2.** Measurement as definition: what compute counts (synthetic-data generation including discarded samples; merged weights) and what does not (evaluations and red-teaming, failed experiments, teacher models in distillation, reward models). There is a tolerance: "accurate within an overall error margin of 30%". Worth seeing for how a quantity gets operationalised in a legal document.

## eu-cop-2025-safety-security

**Code of Practice for General-Purpose AI Models: Safety and Security Chapter (final, July 2025).** 1,826 lines, 43 PDF pages. The printed page equals the PDF page. Clean single-column extraction. The four process figures (Figures 1–4) survive only as captions, e.g. line 186 ("The text of the Commitments and Measures takes precedence").

**Register:** three distinct speech acts, each with its own grammar, which the schema may want to keep apart.
- Recitals (a)–(j): "The Signatories **recognise** that …", i.e. shared premises and interpretive principles.
- Commitments: "Signatories **commit to** …".
- Measures: "Signatories **will** …". It is neither the statute's "shall" nor the soft-law "should".

Each Commitment is headed "LEGAL TEXT: Article 55(1) … AI Act", an explicit pointer from commitment to obligation. Several Measures carry safe harbours ("This Measure is presumed to be fulfilled, if …", line 914).

**TOC:** none. Map: Objectives 21–41 (p2); Recitals 43–160 (p3–5); Commitments 1–10 at 166 / 331 / 380 / 532 / 603 / 637 / 672 / 877 / 988 / 1090; Glossary 1136; Appendices 1–4 at 1380–1821 (p34–43).

**Glossary:** lines **1136–1375 (p29–33)**, 35 terms in a two-column table that extracts cleanly. It states precedence: Art. 3 AI Act definitions "prevail". Entries that bear on your contested terms:
- `deception` (1159), which folds in "evading oversight … detecting that it is being evaluated and under-performing";
- `insider threats` (1192): "hostile operations by humans, AI models, and/or AI systems … and/or model self-exfiltration", so a model can be an insider;
- `model` (1230): means "a general-purpose AI model with systemic risk", with a version-aggregation rule;
- `model elicitation`, `near miss`;
- `non-state external threats` (1273), which is quantified ("roughly comparable to ten experienced, professional individuals … up to EUR 1 million");
- `(self-)exfiltration` (1315), `state of the art` versus `best practice`, `systemic risk source`, `systemic risk tiers`;
- even `including` (1180), defined as a non-exhaustive minimum.

**Passages**
1. **Lines 43–160 (p3–5), Recitals (a)–(j).** Principles as premises the signatories "recognise": lifecycle, contextual assessment (system architecture and inference compute count even though the chapter is "not [about] AI systems"), proportionality, a *Precautionary Principle* ("extrapolation of current adoption rates and research and development trajectories … should be taken into account"), purposive interpretation, and "reporting of a serious incident is not an admission of wrongdoing". This is how the Code frames its own epistemic stance.
2. **Lines 166–330 (p6–10), Commitment 1, Safety and Security Framework.** The loop: identify, analyse, determine acceptability, mitigate, re-assess. There are "trigger points", forecasts of when a model will exceed the highest tier reached ("may consist of time ranges or probability distributions", 211–216), 12-month reassessment, and triggers including a model that "has developed or is likely to develop materially changed capabilities and/or propensities". Commitments that require a forecast, not just a measurement.
3. **Lines 532–632 (p15–17), Commitments 4–5, acceptance and safety mitigations.** Tiers "defined in terms of model capabilities … measurable … at least one … not been reached"; a *safety margin* against under-elicitation and mitigations "being circumvented, deactivated, or subverted"; the go/no-go rule ("will only proceed … if … acceptable"); then the mitigation examples, ending with "defending against a model's ability to subvert its other safety mitigations". Mitigation that assumes the mitigated object may act against it.
4. **Lines 1380–1546 (p34–37), Appendix 1, the taxonomy.** Types (five), nature (essential versus contributing characteristics: velocity, cascading, irreversibility, asymmetry), sources split into **capabilities / propensities / affordances**, and the four "specified systemic risks", including the definition of **Loss of control** (1530–1533): "humans losing the ability to reliably direct, modify, or shut down a model". The propensities list (1477–1490) names "misalignment with human intent", "lawlessness", "power-seeking", "colluding". This is the most explicit risk-classification scheme in the EU texts.
5. **Lines 988–1085 (p25–27), Commitment 9, serious incident reporting.** The nine report fields (the same ones as the template), tiered deadlines by harm type (2 days for critical infrastructure, 5 for cybersecurity breach including self-exfiltration, 10 for death, 15 otherwise), and a causal-attribution standard: "establish or suspect with reasonable likelihood such a causal relationship between their model and the …". The incident model in legal form.

Also distinctive if you have time: **Appendix 2, lines 1548–1600 (p37–38)**, "similarly safe or safer models". Safety as a *comparison* to a reference model on benchmarks "within a negligible margin of error", used to unlock exemptions. And **Measure 3.5's external-evaluator access terms, 486–525 (p14–15)**: access to "helpful-only" versions and chains-of-thought, a non-retaliation clause, and a 30-business-day cap on blocking publication.

## eu-cop-chairs-2025-statement

**"Statement from the Chairs and Vice-Chairs" plus the full Safety & Security chapter, as captured from the Code's website (header: "FINAL VERSION · 10/07/2025").** 2,183 lines, 52 PDF pages (the last form feed falls at p53).

**This file is not only the chairs' statement.** Lines 33–140 (p1–4) are the statement. Everything from line 145 to the end is a second rendering of the whole Safety & Security chapter, the same text as eu-cop-2025-safety-security. The recitals are numbered (1)–(10) instead of (a)–(j), and every glossary-linked term carries its glossary index number inline ("models 12", "including 7", "state of the art 25", "independent external 8"). Those numbers are hyperlink residue, not footnotes. They make the prose here noisier to read or quote than the PDF, but they do show which words the site treats as defined terms.

**The two renderings are not identical.** A word-sequence comparison (my check, after stripping the inline numbers) matches about 98.6%. Most differences are omissions: the PDF's "LEGAL TEXT" citation lines and figure captions are absent here. One difference is substantive, in Appendix 2.2 (similarly safe or safer models):
- This file (lines 1896–1907) requires benchmarks "that measure (a) general capabilities and (b) systemic-risk-specific capabilities", and point (3) compares "capabilities, propensities, and safety mitigations".
- The PDF (eu-cop-2025-safety-security lines 1574–1583) has no (a)/(b) clause, and its point (3) compares "characteristics such as relevant architectural details, capabilities, propensities, affordances, and safety mitigations".

It also says "this Code" where the PDF says "this Chapter" (1921). I can't tell from the texts which is later. If the schema ever quotes Appendix 2.2, it should say which rendering it quotes.

**TOC:** none.

**Glossary:** lines **1375–1653 (p34–39)**, the same 35 terms as the PDF, numbered 1–35 (the numbers match the inline markers throughout).

**Passages**
1. **Lines 33–140 (p1–4), the statement itself. Read it whole; it is the only content unique to this file.** A different voice from the Code: first-person-plural advocacy by the drafters ("we believe the Safety and Security Chapter is the best framework of its kind in the world"). It makes empirical forecasts without citations ("estimates suggesting that there will be hundreds of such models within a few years"), states a drafting assumption ("assuming only about 5–15 providers will be subject to the systemic risk obligations"), and gives institutional recommendations (a two-year review cadence, emergency updates, a whistleblower channel, 100/200 staffing, a "foresight unit"). The staffing figure is attributed to "a group of AI experts", and its sentence is nearly verbatim from tfs-2025-protecting-gpai lines 93–94 ("The AI Safety unit (DG CNECT A3) should be scaled up to 100 staff, with the full implementation team expanding to 200"). It also offers an interpretive claim about the Act: GPAISR obligations should be read as "only applying to risks that are specific to the frontier of capabilities".
2. **Lines 1888–1926 (p45–46), Appendix 2.2 in this rendering.** Only worth opening side by side with the PDF's 1569–1599, for the divergence described above.

Otherwise, use eu-cop-2025-safety-security for the Code text; its line references are cleaner.

## ec-2025-gpai-serious-incident-template

**"Report for Serious Incidents under the AI Act (General-Purpose AI Models with Systemic Risk)", the Commission's reporting template.** 68 lines, 2 PDF pages. **Read it whole (lines 1–68).** No TOC or glossary.

It is a form, and its assertions are field definitions. Lines 11–52 give ten numbered fields: dates, harm and victim, "chain of events that (directly or indirectly) led to", model involved, evidence, response, recommendation to authorities, root-cause analysis including "failures or circumventions of systemic risk mitigations", and post-market patterns "such as … near misses". Fields 1–9 reproduce Code Measure 9.2 almost word for word (eu-cop-2025-safety-security lines 1020–1034). The header (lines 3–5) explicitly ties the template to "Article 55(1), point (c)" and "Commitment 9". One small divergence: the Code's item (5) reads "a description of material available", the template's reads "a description of evidence available". Field 10 (submitter; lines 55–63) offers "☐ Provider ☐ Authorised representative ☐ Other", which is the only role taxonomy in the document.

---

## hoffmann-2025-eu-code-safety

**Mia Hoffmann (CSET), "AI Safety under the EU AI Code of Practice — A New Global Standard?", blog post, 30 July 2025.** 452 lines, 10 PDF pages. The extraction double-spaces every line (a blank line between each text line), so the real content is about 200 lines. Lines 395–452 are author and related-links boilerplate. **Read it whole (lines 1–392).** No TOC or glossary.

What it does: explanatory commentary that restates the Code in plain words, then evaluates it ("goes far beyond current industry practices", "Unfortunately, the chapter does not offer much transparency") and predicts its global effect. Two places where it recasts the primary texts, worth knowing before anyone quotes it as a source of fact:
- **Lines 76–83 (p2–3):** "Providers of GPAI models, defined as those models whose training compute is above 10^23" presents the Guidelines' *indicative, rebuttable* criterion (ec-2025-gpai-guidelines para 17 and para 20) as the definition. The Act's definition (Art. 3(63)) is functional.
- **Lines 105–115 (p3):** it says the Code offers a "presumption of conformity", meaning regulators "will assume that adherence … demonstrates compliance". The Code itself says adherence "does not constitute conclusive evidence of compliance" (eu-cop-2025-safety-security lines 30–32). The Guidelines (para 100, lines 1139–1143) and the Omnibus (recital 41, lines 743–746) both say codes do *not* grant a presumption of conformity; only harmonised standards do.

If you want a passage rather than the whole: **lines 143–320 (p4–7)**. This is the restatement-plus-evaluation core: the four specified risks, the pipeline, "pre-defined risk tiers" (with the author's gloss on why pre-commitment matters, 234–242), and the transparency criticism.

---

## tfs-2025-protecting-gpai

**Open letter to Commission President von der Leyen, "Ensuring GPAI Rules Serve the Interests of European Businesses and Citizens", 25 June 2025.** The key suggests The Future Society as the originator. The text itself only lists it among the organisational signatories, alongside individuals including Acemoglu, Hinton and Russell. 173 lines, 4 PDF pages. **Read it whole (lines 1–111); lines 112–173 are the signatory list.** No TOC or glossary.

What it does: advocacy. It makes causal and empirical claims backed by footnoted press and model-card citations ("recent releases … showcasing new dangerous capabilities related to cyber, biological, radiological and nuclear threats" (24–26); "major GPAI model providers have drastically scaled back transparency and the rigour of safety-testing" (28–29)), an efficiency argument ("Mitigating risks at the upstream model level once … is far more efficient than doing so potentially thousands of times downstream", 69–70), and three numbered demands (76–97: mandatory third-party testing, review and emergency-update mechanisms, 100/200 AI Office staff). Footnote numbers are fused onto words ("Report 20255" is footnote 5). Two notes for cross-reading:
- Its characterisation of the Code's commitments as "overlapping with risk management practices already carried out by most large GPAI providers" (33–35) is the opposite emphasis from Hoffmann's "goes far beyond current industry practices".
- Its staffing demand reappears nearly verbatim in the chairs' statement.

# International instruments and consensus documents

## g7-2023-hiroshima-code-of-conduct

**Hiroshima Process International Code of Conduct for Organizations Developing Advanced AI Systems (G7, October 2023).** 348 lines, 8 PDF pages; printed page equals PDF page. Clean. **Read it whole.** No TOC or glossary. The only definitional move is the parenthetical "(henceforth 'advanced AI systems')" at lines 7–12, which covers "the most advanced foundation models and generative AI systems".

Voice: soft-law commitments in a graded modal register. Within one short text there are four grades:
- "Organizations **should**" (the default);
- "organizations **commit to**" (lines 91, 124, 284: stronger, first-person-of-signatory);
- "Organizations **are encouraged to**" (141, 270, 317);
- "States **must**", used once (61), and only for states' human-rights obligations.

It also opens with "Different jurisdictions may take their own unique approaches to implementing these actions" (34–35) and lists eleven numbered actions.

If you want passages rather than the whole:
1. **Lines 1–68 (p1–2), preamble.** Scope, "risk-based approach", "living document", and the one categorical prohibition in the text (56–58: "should not develop or deploy … in ways that … pose substantial risks … and are thus not acceptable").
2. **Lines 72–131 (p2–3), Action 1 with its risk list.** CBRN "lower barriers to entry", offensive cyber (with a note that such capabilities "could also have useful defensive applications"), "Risks from models of making copies of themselves or 'self-replicating' or training other models", and a "chain reaction … up to an entire city". **This list reappears nearly word for word in AI Act recital (110)** (eu-2024-ai-act lines 1922–1932), which then feeds the Code's Appendix 1. It is a traceable lineage of risk language from G7 to EU law.

---

## oecd-2026-haip-reporting-v2

**Hiroshima AI Process Voluntary Reporting Framework v2.0 (OECD), the questionnaire organisations fill in to report against the G7 Code.** 616 lines, 9 PDF pages. **Read it whole; it is a form, and most of its content is answer options.**

**Extraction artifacts:** the top-level question numbers were lost. Each main question appears as an unnumbered indented line, e.g. 33 ("How does your organization define and/or classify different types of risks…"), and only sub-questions keep labels (1A, 2.A, 3A…). "Recommended for: (and others where relevant)" has lost its role names, which were probably icons. Checkbox glyphs (☐) survive.

What it asserts: almost nothing directly. Its *answer options are an implicit taxonomy of practices*, which is a mode of assertion none of your listed categories quite covers: the form presupposes what kinds of things an organisation might do. Each section header maps back to G7 Actions (e.g. line 30, "Section 1: RISK IDENTIFICATION AND EVALUATION (Actions 1, 4, 6, 10)").

**Glossary:** none formally. **Lines 10–24 (p1)** define the respondent roles ("Model developer (/provider)", "Application developers (/providers)", "Deployer"), with a one-sentence GPAI definition credited to "(OECD, 2023)". This is a third role vocabulary alongside the AI Act's provider/deployer and Canada's developer/manager, and it treats "developer" and "provider" as slash-synonyms.

Passages, if not read whole:
1. **Lines 10–95 (p1–2).** Roles; Q1 on risk taxonomies (with "dangerous capability thresholds … CBRN, cybersecurity attacks, dangerous advanced autonomy capabilities"); 1A on how thresholds of "unreasonable" risk are defined; Q2's list of evaluation practices, including "Assessment of risks arising from interactions among multiple AI agents" and whether "national AI safety / security institutes of the AISI network" are involved.
2. **Lines 355–378 (p5–6).** Post-deployment monitoring, including "Monitoring and emergency controls specific to agentic AI systems (e.g. ability to interrupt autonomous action sequences, override tool-use permissions, or revoke delegated authority)", and Q14 on agentic controls ("Constraints on the agent's action space", "interruptibility"). This is where "control" appears operationally, as a checklist of controls.

## oecd-2024-future-ai-risks

**OECD, "Assessing Potential Future Artificial Intelligence Risks, Benefits and Policy Imperatives", OECD AI Papers No. 27, November 2024 (OECD Expert Group on AI Futures).** 3,632 lines, 69 PDF pages; printed page equals PDF page. Clean single-column extraction with a running header on each page. The reference list (lines 2123–3390, p45–65) and endnotes (3391–end, p66–69) are about 40% of the file.

**Extraction loss worth knowing:** Annex B's three ranking charts, including **Figure B.2, "Experts identified and ranked 38 potential future AI risks"**, are images and came through as captions only (lines 2041–2072, p41–43). The full 38-item risk list, and the chart where the text says disagreement about loss of control is visible ("red in Annex B, Figure B.2", line 924), are **not in the text file**. Only the 66 policy actions survive, as Table B.1 (2080–2112, p44). If anyone needs the 38 risks, it will have to be the PDF.

**TOC:** lines **100–172 (p4–5)**.

**Glossary:** none. It gives one-sentence working definitions inline, e.g. AGI "refers to hypothetical future AI systems with human-level or greater intelligence across a broad spectrum of contexts" (928–929, and again at 244–245), and misalignment as "the degree of difference between an AI system's actions in seeking to achieve the explicit objective and the intents or values of humans" (1060–1062).

**What kind of document:** a foresight synthesis. Its authority comes from an *expert-survey ranking* (explicitly "not designed to be a scientific instrument", 1954), and its voice is heavily attributive: "some experts suggest", "Some believe", "others argue". Each of the ten risks is split into two sub-headed halves, one present-tense (what is "already" happening, with citations) and one future (what "could" happen). The report states its own epistemic status up front: "many of the future-oriented aspects of its contents are necessarily speculative" (24–25).

**Passages**
1. **Lines 891–1136 (p19–23), Chapter 3 opening through Risk 5.** The key messages, the note on disagreement over "humans losing control of artificial general intelligence (AGI)" (925–937), then Risks 1–5, each in the already/future two-part structure. Risk 4 (1051–1087) is the OECD's framing of alignment (goals of "self-preservation, self-improvement and resource acquisition" attributed to "some experts"). Risk 5 carries power concentration "potentially facilitating wide-scale subjugation and/or authoritarianism".
2. **Lines 1927–2031 (p38–40), Annex A, methodology.** How the list was made: about 250 sources, then 17/36/68 initial items, then a survey (53 of 61 members, rated 0–10 on "importance" and "actionability", with the rating scale reproduced in Box A.1, 1982–2030), then consolidation into 21/38/66. It is the one place in my set where a risk list's own provenance is documented. Note that the initial count (36 risks) and the final count (38) differ.
3. **Lines 288–405 (p8–10), Chapter 1, "desirable AI futures".** A mode not on your list: *normative scenario* statements in the conditional ("Benefits from AI would be widely distributed", "Decisions … would be decentralised where possible"). They describe a target state, not a forecast.
4. **Lines 1306–1330 and 1500–1560 (p26, p30–31).** Policy-gap assessment ("There is less recognition of harms resulting from inadequate AI alignment methods, at least under some conceptions of alignment") and Policy Actions 1–2 (liability; "red lines", including "self-replicate autonomously"). This shows the recommendation register and how the report maps each recommendation to existing instruments ("Recent and emerging public policy efforts").
5. *(Optional)* **Lines 2080–2112 (p44), Table B.1.** The 66 policy actions as terse labels, ranging from "Liability rules" (1) to "Advanced AI R&D moratorium" (65) and "Ban advanced AI" (66). The layout is three-column; it reads row-wise but the item numbers keep it usable.

## perset-2025-how-managing-risks

**Karine Perset and Sara Fialho Esposito (OECD), "How are AI developers managing risks? Insights from responses to the reporting framework of the Hiroshima AI Process Code of Conduct", OECD AI Papers No. 45, September 2025.** 1,613 lines, 36 PDF pages. The printed page is one less than the PDF page (printed "3" is PDF p4). Clean extraction except the glossary table (see below). References run 1532 to the end.

**What kind of document:** a *second-order synthesis of self-reports*. Nearly every assertion has the form "organisations report X", quantified by vague frequency words ("most", "many", "several", "a few", "at least five") and illustrated with named companies. Nothing is verified; the report says so ("The examples included are illustrative and do not represent a comprehensive overview", 402–404). The respondent pool is 20 organisations. It includes Anthropic, Google, Microsoft and OpenAI, but also a preparatory school, consultancies and telecoms (acknowledgements, 112–116). The title's "AI developers" therefore covers far more than the frontier-developer sense. Each findings section opens with a box quoting the G7 Code Actions it reports against, so the report links practice claims back to commitments.

**TOC:** lines **145–171 (p6)**.

**Glossary:** **Annex B, "Glossary of key terms", lines 1404–1522 (p33–34)**, 24 terms. The two-column table extracts with the explanation column ragged right, and sometimes split across the term's line, but every entry is legible. It includes the **OECD definition of "AI incident"** (1423–1430): "an event, circumstance or series of events where the development, use or malfunction of one or more AI systems directly or indirectly leads to" harm to health, critical infrastructure, human-rights or legal obligations "intended to protect fundamental, labour and intellectual property rights", or "harm to property, communities or the environment". That is a close parallel to AI Act Art. 3(49), but it is not the same list. The glossary also carries the OECD AI-system definition, the lifecycle phases, "capability thresholds" (after Schuett et al., 2025), "foundation models" and "open-weight models". Several entries are marked "for the purpose of this report, based on organisations' submissions".

**Passages**
1. **Lines 181–275 (p7–8), executive summary.** The whole report compressed into generalisations about populations of organisations ("Larger technology firms tend to focus on systemic risks"; "A few organisations are exploring security concerns related to artificial general intelligence (AGI)"). It shows the "reported-practice" register at its most compressed.
2. **Lines 409–538 (p12–14), Section I, risk identification and evaluation.** The richest findings section. It includes companies' *own* risk classification schemes, quoted as data: NTT's three levels (unacceptable/high/limited), SoftBank's four tiers, KYP.ai's "unreasonable" versus "predictable" risks, and frontier frameworks with "capability thresholds that trigger enhanced safeguards". A source reporting other sources' taxonomies is a layering the schema will probably meet often.
3. **Lines 765–877 (p19–21), Section IV, governance and incident management.** Board oversight, incident teams, and the Frontier Model Forum information-sharing arrangement ("limited to FMF members", 860–864). Useful to see how "incident" is operationalised in self-description, against the Code's legal version.

## ecosystem-2025-singapore

**"The Singapore Consensus on Global AI Safety Research Priorities: Building a Trustworthy, Reliable and Secure AI Ecosystem", 8 May 2025 (following the 26 April 2025 Singapore Conference on AI).** 1,839 lines, 40 PDF pages. The printed page is one less than the PDF page (printed "2" is PDF p3). The body text is clean. **The contributor list, lines 43–171 (p3–4), is a four-column name grid that extraction has scrambled** (names and affiliations interleave across columns). Running section headers show letter-spacing artifacts ("Secu r e and Reliab le"). References start at about line 1500 and use short keys ("IAISR", "Anthropic-C", "Bengio-B"), not numbers.

**TOC:** lines **5–37 (p2)**.

**Glossary:** **Table 1, lines 338–395 (p9)**, 16 terms, including `AI agent`, `AI model`, `AI system`, `Control`, `Alignment` ("Creating/modifying AI to meet intended behaviour, goals, and values (current emphasis tends to be on behaviour)"), `Intelligence` ("Ability to accomplish goals"), `AGI`, and `ASI`. It comes with an unusually explicit disclaimer (256–261, restated at 391–395): "the definitions … simply specify how we use various terms in this report … we make no claims whatsoever to these being better than other alternative definitions". A longer alignment/assurance/robustness gloss sits in a box at **716–733 (p17)**.

**What kind of document:** a research-priorities consensus. Its characteristic assertion is "X is an open problem / a research frontier", backed by a brief evidential sketch with citations. It is structured by a stated model: *defence-in-depth* with three areas, Risk Assessment, Development, and Control. Each area is tagged "Associated with IAISR chapter …", which ties it to the International AI Safety Report. It also marks some topics as "areas of mutual interest" (217–228, 445, 1474), i.e. where competitors have incentive to share. That is a classification of research by its cooperation incentives.

**Passages**
1. **Lines 176–395 (p5–9), Introduction through Table 1.** Goals, consensus process (100+ participants, 11 countries, "points of broad consensus"), scope (the term "AI systems" is stipulated to mean general-purpose systems, "Importantly, it includes general-purpose agents"), the three-area structure, and the glossary. Figure 1's caption (322–328) tries to explain the model/system boundary using an external bioweapons filter. As printed it assigns the filter to "Area 2" or "Area 1" depending on where the system boundary is drawn, where the surrounding text implies Areas 3 and 2. I take that as a slip in the source, and a live example of the boundary problem it describes.
2. **Lines 570–657 (p13–15), §1.5–1.7.** Metrology (internal, external and construct validity; "actuarial" methods and their limits), dangerous *capability versus propensity* assessment, and **§1.7 Loss-of-control risk assessment**. Here LoC is defined as scenarios where systems "come to operate outside of human control, with no clear path to regaining control", covering both "passively ceding control" and "actively undermining control measures". It lists "control-undermining capabilities", quotes the International AI Safety Report on the lack of expert consensus, and cites the CAIS extinction statement. Compare the Code's LoC definition (eu-cop-2025-safety-security 1530–1533), which is about "the ability to reliably direct, modify, or shut down".
3. **Lines 709–809 (p17–19), the "Relationship to other concepts" box and §2.1.1.** Alignment defined twice, as a common definition and as the de facto working one ("ensuring that AI behaves as intended"). Then evidential anecdotes presented as research motivation: pandering, "let's hack", "learned to obfuscate its deceptive plans", and systems "placing more value on their own existence than on human well-being". This is incident-like evidence carried inside a research agenda.
4. **Lines 1287–1393 (p29–31), §3.1.2–3.1.3, intervention and the "AGI and ASI control problem".** Off-switches, override protocols, a call to measure "to what numerical degree a system is under the meaningful control of human operators", scalable oversight, corrigibility, containment, "Scientist AI", "AI control" setups, and Ashby's Law. This is the most technical treatment of "control" in my set, and it uses the engineering sense that the report defines at 311–313.

## ecosystem-2026-2026

**"The 2026 Singapore Consensus on Global AI Safety Research Priorities", July 2026, with a bundled "Companion Report on Agentic Risk Management".** 4,812 lines, 99 PDF pages. The printed page is two less than the PDF page (printed "2" is PDF p4; the Main Report's printed p.11 is PDF p13). Body text is clean. Running headers carry letter-spacing artifacts ("2 De veloping Tr ust worthy", "Companion R eport"). The contributor grids at lines 62–181 (p3–4) are multi-column and partly scrambled, less badly than in the 2025 edition. **Two documents in one file:**
- Main Report: lines 186–2466, references 2467–3061 (p55–64).
- Companion Report on Agentic Risk Management: 3062–4488, references 4489–4812 (p94–99).

**TOC:** lines **7–58 (p2)**, covering both reports.

**Glossary:** **Table 1, lines 667–736 (p17–18)**. It is the 2025 glossary almost verbatim, with the same "we make no claims" disclaimer, plus a new entry `Open-weight AI model` ("can be used and modified in unrestricted ways by downstream users"). The Companion Report adopts an external agent definition instead: "the four-capability model of Perception, Planning, Memory, and Execution [ITU-T F.748.46]" (3135–3138).

**What changed from 2025, visibly in the text** (useful if the schema needs to track a source's own revisions):
- A fourth pillar, "Societal Resilience", was added because "harm prevention efforts alone are insufficient" (243–251, 650–653).
- Every subsection now opens with an **"Updates: / Advantages: / Challenges:" box** (21 of them; e.g. 845–856). The source is summarising its own change since the previous edition.
- Scope: 2025's "Importantly, it includes general-purpose agents" is gone, and "Narrow systems such as self-driving cars are therefore out of scope" is added (604–613).
- The backing-government count for the International AI Safety Report changed from 33 (2025, line 206 of that file) to 29 (541).
- A citation "Bucknall et al, 2005" (234, 561, 566) appears to be a typo for 2025.

**Passages**
1. **Lines 186–354 (p5–8), executive summary.** Measurement-style claims with no inline citation: "Revenues from frontier models have grown by over 400%", misuse capabilities have "surpassed PhD-level experts on some benchmarks", cyber capabilities "increased the number of real-world vulnerabilities found in some critical software by over 1000%", open-weight models "3 to 12 months behind the frontier". Also the key updates and the companion report's ten principles. It shows how a research-priorities document now opens with a landscape assessment.
2. **Lines 363–500 (p9–12), "Research Priorities by Policy Area".** This is new: a policymaker translation organised by harm domain (cyber, bio/chem, child safety, mental health, agents in the economy, open-weight, "Loss of control and oversight of automated frontier AI development"). Each has "What is at stake" plus priorities with section cross-references. It opens by asserting "a scientific consensus … not a policy document", then does policy translation anyway.
3. **Lines 1102–1166 (p26–27), §1.4 Loss-of-control risk assessment.** The same LoC definition as 2025, extended. It adds "precursor capabilities" (autonomous replication, shutdown resistance, self-proliferation), a second pathway ("deliberate decisions by humans to release highly agentic AI systems"), named 2026 events as evidence ("Conway and Moltbook … earning money via cryptocurrency transfers to keep themselves running"; "Claude Mythos (Anthropic, 2026)"), a vivid claim ("credible fears … that some AI systems may soon become goal-oriented invasive species in cyberspace"), and a third, gradual pathway (gradual disempowerment, Kulveit et al.). Loss of control appears here as three distinct causal pathways.
4. **Lines 3062–3290 (p64–68), Companion Report introduction, method and hazard-principle table.** An explicit hazard → mitigating principle → example practice mapping (3210–3287), and a method that treats *convergence across sources* as evidence ("signals of convergence", 3163–3165). It also carries unusually frank self-limitation ("should therefore be seen as exploratory … rather than constituting a definitive framework", 3182–3184).
5. **Lines 4125–4210 (p86–87), Principle 8: Interruptibility.** Shows the per-principle template: "What is it" (definition); "Practical guidance" split **by role** (agent developers / deployers / "Shared responsibilities: whoever controls the execution environment", a role defined by *control over the environment*, which bears on "developer"); "Governance context" (restating the EU AI Act Art. 14 and China's TC260 framework); and "Illustrative Cases" naming company practices (Huawei, OpenAI, IBM, Anthropic, Google). Its paraphrase of Art. 14 ("mandates … must have the ability") is stronger in register than the Act's "enabled, as appropriate and proportionate" (eu-2024-ai-act 4108–4131). It is a small example of secondary restatement drifting from a primary.
6. *(Short, and worth it for scope)* **Lines 4408–4470 (p92–93), Companion conclusion and "Future Work".** Includes an explicit scope exclusion: "The controls mapped here address agents that are compromised, misused, or malfunctioning. The effective pursuit of misaligned goals by agents functioning exactly as engineered presents a broader systemic risk that is not addressed in this companion report" (4436–4439). It also says "no single actor controls the full stack" (4424).

## unhlab-2024-governing

**UN High-level Advisory Body on AI, "Governing AI for Humanity: Final Report", September 2024.** 6,064 lines, 101 PDF pages. The printed page equals the PDF page from the executive summary on (printed "7" is PDF p7).

**Badly garbled in the running prose; read those parts in the PDF if you can.** The body is set in two columns, and `pdftotext -layout` interleaves them *line by line*: a line of the left column, then a line of the right, often mid-sentence (e.g. lines 121–191, 1290–1333, 4204–4302). It is decipherable only because paragraphs are numbered: roman numerals i–lxiii in the executive summary, arabic 1–~215 in the body. The two columns can be followed by tracking those numbers down the page. **Full-width boxes and recommendation boxes extract cleanly** (e.g. Box 3 at 1450–1485, Box 4 at 1501–1542, Recommendation 1 at 370–387). Figures are mixed: Figure 2 (1354–1408) keeps its category labels and percentage bars as loose numbers, while Figure 3 (1600ff.) is glyph noise. Annex E's survey charts (4673–5526, p83–92) are partly numeric residue.

**TOC:** lines **60–114 (p5–6)**.

**Glossary:** none; only **Annex G, List of abbreviations**, 5971 to the end (p99–100). The report defines by stance rather than by term: it declines to list risks ("Putting together a comprehensive list of AI risks for all time is a fool's errand", para 20, around 1307–1316, interleaved) and instead **categorises risks by who is vulnerable** (Box 4).

**Epistemic status, stated up front (lines 40–54, p4):** "This report represents a majority consensus; no member is expected to endorse every single point … broad, but not unilateral, agreement". This consensus hedge differs from Singapore's "points of broad consensus".

**Passages**
1. **Lines 1290–1545 (p28–31), §1.D–E "Risks and challenges / Risks of AI".** The vulnerability-based framing (para 17: "We conceptualize AI-related risks in relation to vulnerabilities"). Figure 2, the AI Risk Global Pulse Check: 348 experts, 14 harm areas, with shares "concerned" (e.g. item e, "Unintended autonomous actions by AI systems … loss of human control over autonomous agents", at 1399–1401, drew *less* concern than most). Box 3 on security (clean; "kill decisions should not be automated through AI"; "120 Member States support a new treaty on autonomous weapons"). **Box 4 (1501–1542), the vulnerability taxonomy**: Individuals / Politics and society / Economy / Environment, with examples. Paras 21–26 are interleaved; the boxes are clean.
2. **Lines 4204–4330 (p73–75), §4.E "Reflections on institutional models: An international AI agency?"** A mode missing from your list: **argument by analogy and historical precedent** (chemical and biological weapons regimes, the 1975 recombinant-DNA limits, IAEA's "grand bargain", CERN, ICAO/IMO, FSB/FATF), each with its stated "limits of the analogy" (para 201). It ends in **conditional triggers** for future institution-building (para 207: "the prospect of uncontrollable or uncontainable AI systems … systems that are unable to be traced back to human, corporate or State actors … qualities that suggest the emergence of 'superintelligence', although this is not present in today's AI systems"). Two columns, interleaved.
3. **Lines 360–390 (p10) and the other recommendation boxes (461, 550, 656, 731, 806, 926; p12–20).** The seven recommendations in clean full-width boxes. Institutional proposals phrased as mandates for bodies that don't exist yet ("We recommend the creation of an independent international scientific panel on AI … its mandate would include: a) Issuing an annual report …").
4. *(If you want the survey itself)* **Lines 4673–4700 (p83), Annex E introduction**, describing the Pulse Check method (fielded 13–25 May 2024, snowball invitation, "More than 340 respondents"). What follows is chart residue.

# National institutes and codes (Canada, Japan)

## ised-2023-voluntary-code-genai

**Innovation, Science and Economic Development Canada, "Voluntary Code of Conduct on the Responsible Development and Management of Advanced Generative AI Systems", September 2023 (web page; "Date modified: 2026-06-04").** 250 lines, 4 PDF pages. The page is a Canada.ca web capture: navigation chrome at lines 1–24 and footer at 206–250. **Read lines 25–204 whole.** No TOC.

**Glossary:** effectively **footnotes 1 and 2, lines 193–202 (p3)**, which define the two roles by activity. *Development* "includes methodology selection, collection and processing of datasets, model building, and testing"; *managing the operations* "includes putting a system into operation, controlling the parameters of its operation, controlling access, and monitoring its operation". So "developer" versus "manager" here is roughly, but not exactly, the AI Act's provider versus deployer.

The distinctive passage is **lines 130–190 (p3), the "Measures" matrix**: principle × measure × four columns (developers or managers × all advanced generative systems or systems "available for public use") with Yes/No cells. It is an explicit *applicability* assertion: who must do what, conditional on role and on public availability. The layout survives but is ragged; cells sit on the line below each measure's first line. Example: "Employ multiple lines of defence, including conducting third-party audits prior to release" is Yes only for developers of publicly available systems (143–145). The six outcome-principles (61–70) are each stated as a *state of affairs* ("Safety – Systems are subject to risk assessments…"), not as an action.

---

## caisi-ca-2026-landing

**Canadian AI Safety Institute landing page, Canada.ca ("Date modified: 2026-07-08").** 160 lines, 4 PDF pages. Web capture with chrome. **Read lines 26–114 if at all.** It is a mission statement. Its one substantive framing (lines 30–36) defines CAISI's risk scope as "risks posed by synthetic content, including impersonation and fraud, as well as risks posed by the development or deployment of systems that may be dangerous or hinder human oversight". Otherwise it lists institutional structure and partners. There is no glossary, and there are no passages beyond that.

---

## caisi-ca-2026-evaluators-share

**CAISI blog post, "What information should AI evaluators share?", 8 July 2026, part of a series by members of the "Network for Advanced AI Measurement, Evaluation, and Science (AAIMES Network)".** 337 lines, 7 PDF pages. Canada.ca chrome at 1–25 and 293–337. **Read lines 26–291 whole**; it is short. No TOC or glossary, though it glosses "construct validity" and "external validity" in passing (lines 130–134).

Voice: normative best-practice guidance about *measurement reporting*, i.e. assertions about how other assertions (evaluation results) should be made. Modal mix: "should", "we propose", and occasionally "must" ("Evaluators must provide enough information about the context of use…", 123–125). It is useful for the schema as a statement, from a government evaluator, of what metadata an evaluation claim needs in order to be interpretable: intent, context of use, methodology, model/system configuration, uncertainty (confidence intervals), and conflicts of interest. It also sets out what may be *withheld* and to whom, in three disclosure tiers (lines 213–221).

If passages: **lines 173–206 (p4–5)** on confidence intervals, benchmark saturation, LLM-as-judge error, and conflicts of interest, with a worked number (83% on 100 questions gives a 95% CI of 74–89%). And **lines 255–271 (p6)** on data contamination ("contamination risk can only be substantially reduced by withholding a large proportion of the test sets").

A small internal inconsistency: the network's acronym is "AAIMES" at line 28 and "NAAIMES" at line 290. J-AISI's report calls the same body the "International Network for Advanced AI Measurement, Evaluation and Science", the renamed International Network of AI Safety Institutes (jaisi-2025-national-status lines 442–444).

---

## jaisi-2025-national-status

**Japan AI Safety Institute (J-AISI), "National Status Report on AI Safety in Japan 2025", dated 31 March 2026.** 933 lines, 25 PDF pages. Printed page numbers start at "1" on PDF p4 (cover, then two TOC pages, i–ii), so printed page N is PDF page N+3. Line 1 reads "Please refer to the original text for accuracy". This is a translation, and it reads like one, with some sentences garbled ("J-AISI will both address risks and drive innovation", "an international consensus will be established by collaborating").

**TOC:** lines **15–57 (p2–3)**. The chapter numbers "1" and "2" were lost in extraction; the chapter headings appear without numbers at lines 18 and 44.

**Glossary:** none, but one boxed definition that matters: **"AI Safety", lines 72–79 (p4)**, defined as *a state* ("A state which based on a human-centric approach, safety and fairness are maintained to reduce societal risks* … privacy is protected … security is ensured … transparency is maintained"), with a footnote: "Societal risks include physical, psychological, and economic risks". Of the definitions of safety in my set, this is the one most unlike the risk-management framing.

What the document does: an institutional activity report. It asserts events, outputs, organisational facts and self-assessed challenges, not claims about AI risk itself. Some measurements of the institution itself: staff about 30 versus US CAISI about 60, UK AISI about 200, EU AI Office about 60 (lines 778–784); 12 ministries plus 5 organisations (709–726). There is a name collision to be aware of: Japan's own "AI Act" (the Act on Promotion of Research and Development, and Utilization of AI-related Technology, lines 833–842) is not the EU AI Act.

Passages:
1. **Lines 62–143 (p4–5), §1.1.** The definition of AI Safety, objectives, and "AISI's Unique Situation": the institute describing the epistemic predicament ("thinking as we run") and comparing governance structures across jurisdictions.
2. **Lines 145–315 (p6–10), §1.2(1).** The catalogue of evaluation guides, red-teaming methodology, open-source evaluation tool, "AI Incident Response Approach Book" (which "assumes that AI incidents are possible", 244–251), and "Known Attacks and Their Impacts on AI Systems". This is what a national AISI actually produces, in its own description.
3. **Lines 788–852 (p22–24), §1.5 and §2.1.** Challenges (staffing, "virtual organization", multi-layered governance), a citation of the OECD's ten future risks including that "governance mechanisms and organizations will not be able to keep up" (817–821), and the new legal basis at home.

---

## Across the set: how these documents make their claims

These are my observations, from reading this family. Each has a pointer so it can be checked.

**1. Text travels between documents verbatim, so apparent agreement is sometimes one sentence copied.** Traceable chains I verified:
- The G7 risk list (g7 91–121: "self-replicating", "chain reaction … up to an entire city") reappears in AI Act recital (110) (act 1922–1932), which the Code cites as its "ADDITIONAL LEGAL TEXT" for Appendix 1 (cop 1393).
- Code Measure 9.2 (cop 1020–1034) becomes the Commission's incident template (template 11–52) with one word changed ("material" becomes "evidence").
- The Future Society letter's staffing sentence (tfs 93–94) reappears in the chairs' statement (chairs 100–102).
- The 2025 Singapore glossary is carried into 2026 almost unchanged.

If the schema records assertions, a *derivation / quotation-of* relation between assertions in different sources would stop several echoes of one sentence from counting as independent corroboration.

**2. The deontic register is fine-grained and it carries meaning.** Within this family:
- the Act's "shall / may / is presumed";
- the Code's "recognise / commit to / will", with safe-harbour "presumed to be fulfilled, if";
- G7's four grades in eight pages ("should / commit / are encouraged / must", the last only for states);
- the Guidelines' "the Commission considers / understands", explicitly non-binding yet the declared basis for enforcement (guidelines 131–139);
- CAISI's "should / we propose / must".

A single "commitment" or "recommendation" type would flatten distinctions the sources draw deliberately.

**3. Kinds of assertion I met that the working list (definitions, causal claims, measurements, incidents, commitments, recommendations, classifications/taxonomies) doesn't obviously hold:**
- **Rebuttable presumptions and indicative criteria.** Classification plus an allocated burden of proof (Act Art. 51(2)/52(2); Guidelines' 10^23 FLOP and one-third-of-compute tests, each with "exceptionally" escape clauses).
- **Worked examples as a defining device** (Guidelines 258–339; Omnibus recital 12's carve-outs).
- **Forms whose answer options are an implicit taxonomy** (HAIP questionnaire; incident template).
- **Scope stipulations and explicit exclusions.** "'AI systems' … should be understood to refer to general-purpose AI" (sg2025 267–269). The Companion Report excludes "misaligned goals by agents functioning exactly as engineered" (sg2026 4436–4439). The Code says it is "not [about] AI systems" but must consider system architecture (cop 62–68).
- **Conditional triggers**: if X then reassess, update, or build an institution (Code 1.3 and 7.6 grounds; UN para 207).
- **Forecasts required as the content of a commitment** (Code Measure 1.1(2)(c): timelines "may consist of time ranges or probability distributions").
- **Argument by analogy and precedent** (UN 4204–4330).
- **Amendments and version deltas.** The Omnibus is almost entirely edit instructions; Singapore 2026's "Updates / Advantages / Challenges" boxes summarise its own change since 2025.
- **Aggregated self-report** ("organisations report …", Perset throughout).
- **Document-level epistemic status statements** that qualify everything else:
  - OECD: "necessarily speculative" (oecd 24–25);
  - UN: "majority consensus; no member is expected to endorse every single point" (un 49–52);
  - Singapore: "we make no claims whatsoever to these being better than other alternative definitions";
  - the Code: adherence is not "conclusive evidence of compliance" (cop 30–32).

**4. The contested terms, as this family uses them.**
- **Loss of control**, five framings:
  - AI Act recital 110: "unintended issues of control relating to alignment with human intent";
  - Code: "humans losing the ability to reliably direct, modify, or shut down a model" (cop 1530);
  - Singapore: "operate outside of human control, with no clear path to regaining control", including "passively ceding control"; 2026 adds deliberate human release and gradual disempowerment (sg2026 1147–1165);
  - OECD: "humans losing control of artificial general intelligence", singled out as drawing "particularly diverging views" among its experts (oecd 925–927);
  - UN: an *example* under "unintended autonomous actions by AI systems" (un 1399–1401).
- **"Control" itself** has at least four senses:
  - engineering feedback control (sg2025 311–313);
  - a provider "retaining effective control" over a deployed system (omnibus 253);
  - control over the weights as the test of who is a modifier/provider (guidelines 790–793);
  - control of the execution environment as the basis of responsibility (sg2026 4145–4147).
  The Code also uses "free from the Signatory's control" to define independence (cop 1185).
- **Developer**: the Act has no "developer", only a provider who "develops … or has … developed and places it on the market". Canada splits developers and managers by activity. HAIP has "Model developer (/provider)", "Application developers (/providers)" and "Deployer". Perset's "AI developers" includes a preparatory school. Singapore 2026 assigns duties to agent developers, deployers and platform providers.
- **Serious incident**: the Act's is system-level (act 3331). The Guidelines and Code extend it for GPAI to "(self-)exfiltration" (guidelines 1169–1178; cop 1055, 1315). The Code adds deadlines keyed to harm type and a "reasonable likelihood" causal standard. The OECD "AI incident" (perset 1423–1430) is a parallel but different harm list.
- **Safety**: J-AISI defines "AI Safety" as a *state* (jaisi 72–79). The Omnibus defines a "safety function" by the provider's intended purpose (omnibus 959–962). The Code separates safety mitigations from security mitigations.

**5. Commentary sometimes contradicts its primaries.** Hoffmann says the Code gives a "presumption of conformity"; the Code, the Guidelines and the Omnibus all say it does not (see her entry). Hoffmann says the Code "goes far beyond current industry practices"; the TFS letter says it overlaps with practices "already carried out by most large GPAI providers". Singapore 2026's paraphrase of AI Act Art. 14 is stronger in register than the article. If commentary enters the compilation, its restatements of primaries probably need to be checked against them, not just attributed.

**6. File is not the same as document, and one text can exist in several renderings.**
- eu-cop-chairs-2025-statement contains a second rendering of the Code chapter, which differs from the PDF in Appendix 2.2.
- ecosystem-2026-2026 contains two reports.
- The Omnibus changes the Act's text by reference.
- For legal and quasi-legal texts, article, paragraph, Measure and recital numbers are more stable anchors than lines or pages (with the caveat of the Guidelines' own numbering drift).

**7. What extraction loses, and where it matters:** flattened exponents everywhere; the OECD's 38-risk ranking chart (only captions survive); the Code's process figures; the UN body text (column interleave); top-level question numbers in the HAIP form; the Singapore contributor grids.

---

## Notes on the brief

- Line plus PDF page worked well. For the legal texts I have added article, recital or paragraph numbers where they help, since those survive re-extraction and re-pagination better than either.
- "Representative passage" was hard to keep separate from "passage that bears on the contested terms", because you named those terms. Where I leaned toward the latter I have tried to say so in the one-liner. In the long, uniform documents (the Act, the Code, the Singapore reports) I preferred passages that show a *kind* of assertion over ones that merely restate a term.
- I did not open the PDFs, so anything that depends on figures (OECD Figure B.2, UN Figure 3, the Code's Figures 1–4) is unexamined.

