# Source atlas: US federal and state

Line numbers refer to `…/scratchpad/src-text/<key>.txt` (pdftotext `-layout`). "p" is the physical page, counted by form feeds (`\f`). A line that *begins* with `\f` belongs to the new page. Ranges are inclusive. The one-line notes are signposts: they say what drew me to a passage, not what it means.

**Two caveats before you open anything.**

1. **About half of this set is not an agency PDF.** Eighteen of the 36 keys are web pages. Seventeen of them (NIST news items, CAISI blog posts, the Commerce press release, the NSPM-11 text) were rendered to text and then to PDF by an earlier agent, and each starts with a `PROVENANCE` block, or a `Source:` block, giving the URL and retrieval date. The eighteenth is SB 53, rendered from the leginfo web page. For these, "p" is a page of that rendering, not of any official document, so **cite them by line**. Two of them (`commerce-2025-caisi`, `nist-2025-caisi-deepseek`) are hard-wrapped at 80 characters, with words split across lines ("Com / merce"), which makes phrase search unreliable. Tables on the web pages are flattened to one cell per line.
2. **How much I read.** I read the short documents (under about 500 lines) whole. For the long ones I read the TOC, the glossary and the sections cited below, and skimmed the heading structure elsewhere. I did not read them end to end. Where I say "typical", it is typical of what I sampled.

Documents are grouped by genre. Search for `### key` to jump to one. Every key in the set is here.

---

## A. Statutes and binding or quasi-binding instruments

### california-2025-sb53: SB 53, Transparency in Frontier Artificial Intelligence Act (TFAIA), Stats. 2025 ch. 138 (approved 29 Sep 2025). 762 lines, 12 pp

- **What it is:** the chaptered bill text from leginfo.legislature.ca.gov, rendered from the web page (the site's nav bar is at line 1). Clean single-column extraction.
- **TOC:** none. The **Legislative Counsel's Digest, 30–108 (p1–2)**, is the bill's own summary of itself. It is useful as a map, but it is not operative text.
- **Glossary:** there are two definition sections, and they are **not identical**:
  - **179–257 (p3–5)**, Bus. & Prof. Code §22757.11: *affiliate, AI model, catastrophic risk, critical safety incident, deploy, foundation model, frontier AI framework, frontier developer, frontier model* (10^26 operations), *large frontier developer* ($500M revenue), *model weight, property*.
  - **596–643 (p10)**, Labor Code §1107 (whistleblower chapter). Here *catastrophic risk* and *critical safety incident* are defined over **foundation** models, not frontier models. The weights-exfiltration incident also covers "damage to, or loss of, property" (627–628), which the §22757.11 version does not. *Covered employee* is defined at 622–623.
- **Passages:**
  1. **113–170 (p2–3).** Legislative findings. Causal and justificatory claims in a legislative voice: "there is concern that advanced artificial intelligence systems could have capabilities that pose catastrophic risks from both malicious uses and malfunctions, including artificial intelligence-enabled hacking, biological attacks, and loss of control" (142–144). Also a forecast: "foundation models developed by smaller companies or that are behind the frontier may pose significant catastrophic risk" (161–162).
  2. **179–257 (p3–5).** The definitions. Look at the structure of *catastrophic risk* (187–209): a threshold (more than 50 people or $1B), then three pathways (CBRN expert-level assistance; autonomous conduct that "would constitute the crime of murder, assault, extortion, or theft" if done by a human; "Evading the control of its frontier developer or user"), then three exclusions. The fourth kind of *critical safety incident* (220–222) is deceptive subversion of the developer's controls "outside of the context of an evaluation designed to elicit this behavior".
  3. **259–361 (p5–6).** The obligations. The frontier-AI-framework contents are a ten-item list of things the developer must *describe how it approaches* (disclosure of process, not a performance standard). There is a transparency-report "deemed in compliance" rule (a model card counts, 332–334), a false-statement prohibition with a good-faith safe harbor (344–351), and redaction with a duty to describe the redaction (353–361).
  4. **453–487 (p8).** §22757.14, a **definition-maintenance clause**. The Department of Technology must recommend annually whether and how to update *frontier model*, *frontier developer* and *large frontier developer*. The criteria are: alignment with federal definitions; whether a person can tell *before training* that they are covered; simplicity; and "external verifiability … by parties other than the frontier developer" (483–484). The statute states what a good definition must do.
  5. **644–696 (p10–11).** Whistleblower protections: a "reasonable cause to believe" trigger, a burden shift to "clear and convincing evidence" (692–696), and an anonymous internal channel with monthly status updates.
- **Other:** §22757.13(c) sets a **15-day** reporting clock (382–384; compare RAISE's 72 hours below). Sec. 5(d) (743–744) disapplies the act where it "strictly conflicts with the terms of a contract between a federal government entity and a frontier developer".

### ny-2026-raise-s8828: NY Senate Bill S.8828, RAISE Act chapter amendment (introduced 8 Jan 2026). 502 lines, 9 pp

- **What it is:** the bill as printed. It **repeals and re-adds** Article 44-B of the General Business Law, which was enacted in 2025 via S.6953-B/A.6453-B (74–78).
- **Extraction warning:** line-numbered bill print (1–56 per page). The header says new matter is in italics (underscored) and deleted matter in [brackets] (48–49). **The italics are lost**, so this text cannot distinguish new from old wording, except for bracketed deletions such as 487. "10º26" at 156 is an extraction artifact for 10^26.
- **TOC:** the section list 83–92 (p2).
- **Glossary:** §1420, **93–179 (p2–4)**. It is textually near-identical to SB 53 §22757.11 (same catastrophic-risk structure, 102–124), plus *Department*, *Office* (within DFS), *Person*, *Superintendent*.
- **Passages:**
  1. **25–73 (p1–2).** Legislative findings. These are largely SB 53's findings re-used, with New York substituted and some findings dropped: there is no "loss of control" enumeration here, which SB 53 has at (j).
  2. **180–265 (p4–5).** Transparency requirements, parallel to SB 53 §22757.12.
  3. **266–385 (p5–7).** Reporting. **72-hour** incident reporting (290–296). Confidential quarterly summaries of *internal-use* risk (275–285). There is also a federal-equivalence "deeming" mechanism (349–385) identical in shape to SB 53's.
  4. **405–482 (p8–9).** Violations ($1M first, $3M subsequent, 405–414). Then the provision SB 53 lacks: §1428, the large-frontier-developer **disclosure statement** (filing, 5% beneficial owners, fee assessment to fund the office, $1,000/day penalty).
- **Why it matters for the schema:** SB 53 and RAISE are the cleanest case in this set of *the same words in two instruments with different operative consequences*: 15 days vs 72 hours, penalty scale, regulator, a registration regime. A quote-level model will need to say "same text, different instrument".

### caag-2025-openai-mou: California Attorney General / OpenAI Memorandum of Understanding on the recapitalization (27 Oct 2025). 260 lines, 6 pp

- **TOC / glossary:** none. Defined terms are introduced inline in quotation marks ("NFP", "PBC", "Recapitalization", "Information", "Representations", "SSC", "Mission").
- **Read it whole (260 lines).** If you only want part of it:
  1. **1–49 (p1–2).** Recitals. "WHEREAS OpenAI is committed to creating jobs…" (21–35) are promotional claims *recited as* agreed premises. The AG's position is "formed in reliance upon, and contingent upon the accuracy of" OpenAI's information (36–39). Odd structure: the heading "Representations:" (47) is followed directly by "It is therefore agreed:" (49). The numbered items that follow serve both as OpenAI's representations and as the agreed terms.
  2. **96–124 (p3).** The safety-governance core. The PBC board may consider "only the Mission (and may not consider the pecuniary interests of stockholders …)" on safety and security (96–103). The Safety and Security Committee sits in the nonprofit, not the PBC. "The SSC has and will continue to have the authority to require mitigation measures—up to and including halting the release of models or AI systems—even … where the applicable risk thresholds would otherwise permit release" (120–124).
  3. **195–234 (p5–6).** The conditional non-objection: "the Attorney General shall not object" subject to three conditions (204–211). Then "RELIANCE: The Attorney General is unaware of any facts contrary to the foregoing Representations, and is expressly and solely relying upon" them (231–234).
- **Why it's distinctive:** the operative claims are **third-party representations adopted under a reliance clause**. The state commits to nothing about their truth. That is an assertion type in its own right, and it isn't on your list.

### eo-2025-14365: Executive Order 14365, "Ensuring a National Policy Framework for Artificial Intelligence" (11 Dec 2025; 90 FR 58499). 186 lines, 3 pp

- **What it is:** the Federal Register print. The text sits in a right-hand column behind about 100 spaces of indentation, and the FR slug lines ("VerDate…", "khammond on DSK…") interrupt it. Otherwise it is clean.
- **TOC / glossary:** none.
- **Passages** (it is short enough to read whole):
  1. **14–49 (p1).** Purpose. Causal and normative claims asserted without hedging: a state patchwork "by definition creates" compliance burden; state laws are "increasingly responsible for requiring entities to embed ideological bias"; Colorado's law "may even force AI models to produce false results" (32–35).
  2. **73–132 (p2).** Directives with 30- and 90-day clocks. Commerce is to identify state laws "that require AI models to alter their truthful outputs" (82–85). There is a BEAD funding condition, an FCC proceeding on a preemptive disclosure standard, and an FTC policy statement on preemption. The document introduces the concept of *truthful outputs* but never defines it.
  3. **138–150 (p3).** Carve-outs the legislative recommendation "shall not propose preempting": child safety, compute/data-center infrastructure, state procurement, and "other topics as shall be determined".
- **Genre note:** an EO asserts almost nothing about the world. It *allocates tasks* to named officials with deadlines, and the claims in its purpose section are the justification for those tasks.

### eo-2026-14409: Executive Order 14409, "Promoting Advanced Artificial Intelligence Innovation and Security" (2 Jun 2026; 91 FR 34565). 172 lines, 3 pp

- **TOC / glossary:** none. It uses definitions by reference, e.g. "National Security Systems, as defined in 44 U.S.C. 3552(b)(6)(A)" (41–42).
- **Passages** (read whole):
  1. **17–38 (p1).** Purpose. "Advanced AI capabilities make our Nation stronger, but also introduce new national security considerations" (25–27).
  2. **89–133 (p2).** "Secure Frontier Model Deployment". **Covered frontier model** is defined by procedure: "a classified benchmarking process to assess the advanced cyber capabilities of AI models and determine the threshold" (97–99), with the determination made by the Director of NSA. There is a voluntary framework for up to 30 days' pre-release government access "before they plan to release such models to other trusted partners" (109–113). Then (c): "Nothing in this section shall be construed to authorize … a mandatory governmental licensing, preclearance, or permitting requirement" (117–120).
- **Why it's distinctive:** the key term's content is **secret by design**. The definition exists as a process and an office, not as text.

### whitehouse-2026-nspm-11: National Security Presidential Memorandum NSPM-11, "Artificial Intelligence in the National Security Enterprise" (5 Jun 2026), plus White House fact sheet. 291 lines, 5 pp

- **Provenance:** the text comes from a globalsecurity.org mirror, "not compared against whitehouse.gov" (1–13). Two parts: the memorandum (17–228) and the fact sheet (230–291).
- **TOC:** none.
- **Glossary:** Sec. 6, **195–218 (p4)**. *AI* (by reference to 15 U.S.C. 9401(3)), *AI incident response*, *AI security*, *AI technology stack*, *chain of command*, **controllability** ("the ability to monitor the operation and outcomes of a system and take corrective action as needed"), *national security enterprise*, *reliability*, *robustness*, **steerability** ("the ability to shape the internal behavior of a system to pursue a given set of objectives").
- **Passages:**
  1. **39–93 (p1–2).** Purpose and the four pillars (Adoption, Adaptation, Assurance, Accountability). Under Assurance, "controllable" is paired with a quite different control claim: "no commercial entity or adversary possesses the capability to prevent use of, disable or degrade, or materially modify without Federal Government knowledge and approval, an AI system" (80–83). That is control **of the vendor's influence over the system**, not control of the system.
  2. **94–130 (p2–3).** Directives. Update DoD Directive 3000.09 on autonomy in weapons. **Terminate contracts** with companies "that have repeatedly demonstrated a pattern of conduct that is inconsistent with" the policy (105–108). There is a classified annex, and it rescinds NSM-25.
  3. **231–291 (p4–5).** Fact sheet. The same content in a promotional register ("Civil liberties and Constitutional protections are non-negotiable", 267–268), with political history ("an outdated document that burdened American AI adoption with ideological mandates", 256–257). It is a useful side-by-side of one policy in two voices.

### whitehouse-2026-legislative-framework: "National Policy Framework for Artificial Intelligence: Legislative Recommendations" (White House, Mar 2026). 205 lines, 4 pp

- **Extraction warning:** a two-column layout where the section title sits in a left sidebar. The title words are **interleaved into the first lines of each section's lead sentence** (53–57, 84–87, 114–117, 129–132, 149–152, 168–174). The bullets themselves are clean.
- **TOC / glossary:** none.
- **Read it whole (205 lines).** Seven sections, each a normative headline followed by "Congress should…" bullets. Most distinctive:
  - **84–109 (p3).** An explicitly marked government *belief* plus an acknowledged contrary view: "Although the Administration believes that training of AI models on copyrighted material does not violate copyright laws, it acknowledges arguments to the contrary exist and therefore supports allowing the Courts to resolve this issue" (88–90).
  - **168–205 (p4).** Preemption. "States should not be permitted to regulate AI development, because it is an inherently interstate phenomenon with key foreign policy and national security implications" (197–199). A causal claim used as a jurisdictional premise.

---

## B. White House policy

### whitehouse-2025-action-plan: "Winning the Race: America's AI Action Plan" (July 2025). 1175 lines, 28 pp

- **TOC:** 37–76 (p3).
- **Glossary:** none.
- **Structure:** three pillars. Each subsection is a short argumentative preamble followed by "Recommended Policy Actions" bullets that name a lead agency. There are 30+ instances of that heading (e.g. 186, 232, 259, 517, 545).
- **Passages:**
  1. **86–149 (p4–5).** Introduction. A race framing and three cross-cutting principles. "our AI systems must be free from ideological bias and be designed to pursue objective truth rather than social engineering agendas" (139–140). "monitor for emerging and unforeseen risks from AI" (143–145) is the only general risk sentence.
  2. **226–265 (p7).** Free speech: "revise the NIST AI Risk Management Framework to eliminate references to misinformation, Diversity, Equity, and Inclusion, and climate change" (233–236). CAISI is tasked to evaluate PRC models "for alignment with Chinese Communist Party talking points and censorship" (240–243). Then open-weight models: "the decision of whether and how to release an open or closed model is fundamentally up to the developer" (256–258).
  3. **509–562 (p12–13).** Interpretability, control, and robustness ("the inner workings of frontier AI systems are poorly understood", 510, which is a rare epistemic-humility sentence), then the evaluations ecosystem.
  4. **1105–1153 (p25–26).** The national-security-risk and biosecurity sections. The chief forecast: "the risks present in American frontier models are likely to be a preview for what foreign adversaries will possess in the near future" (1110–1111). Biosecurity asks for *mandatory* screening "rather than relying on voluntary attestation" (1146–1147), which is unusual in a deregulatory document.
- **Also:** incident response, 959–1010 (p22–23).

---

## C. NIST frameworks, guidance and taxonomies

### nist-2023-ai-rmf: NIST AI 100-1, AI Risk Management Framework 1.0 (Jan 2023). 1947 lines, 48 pp

- **TOC:** 58–123 (p4–5), including lists of tables and figures.
- **Glossary:** none as a section (NIST points to a separate online glossary). Definitions appear **inline, many quoted from ISO/OECD with "(Source: …)" or "(Adapted from: …)" tags**: *AI system* (142–146, p6); *social responsibility / sustainability / professional responsibility* (180–191, p7); *risk* (272–283, p9); *validation, reliability, accuracy, robustness, safe, resilient, secure* (653–747, p18–20). **Appendix A, 1584–1660 (p40–41)**, works as a role glossary (AI actor task categories).
- **Passages:**
  1. **262–330 (p9–10).** Risk defined as "the composite measure of an event's probability of occurring and the magnitude or degree of the consequences" (272–274). Then an epistemic claim about measurement: "The inability to appropriately measure AI risks does not imply that an AI system necessarily poses either a high or low risk" (324–325).
  2. **640–760 (p18–20).** The trustworthiness characteristics, each defined by an imported standard. The tradeoff box (641–650) is a claim that the characteristics trade off against each other. "Safe" is ISO's "not under defined conditions, lead to a state in which human life, health, property, or the environment is endangered" (701–702).
  3. **987–1060 (p26–28).** GOVERN and Table 1. This is the Core's genre: outcome statements in the passive present ("Legal and regulatory requirements … are understood, managed, and documented"). They are neither obligations nor recommendations. The table's two columns partly interleave.
  4. **1584–1660 (p40–41).** AI actor categories. "developers" appears among AI Development actors, "software developers" among Deployment actors, and "product developers" among Operation and Monitoring actors. The word shows up in three different roles.
  5. **1721–1790 (p43–44).** "How AI risks differ from traditional software risks": a list of comparative claims.
- **Note:** this is the document the Action Plan (226–236 above) orders revised. The VCAT slides say a "Revised NIST AI RMF" is forthcoming (`nist-2026-vcat-ai-update` 413).

### nationalinstituteofstandardsandtechnologyus-2024-artificial: NIST AI 600-1, AI RMF Generative AI Profile (Jul 2024). 3097 lines, 64 pp

- **Extraction warning:** "fi" and "ff" are ligature characters (ﬁ, ﬀ) throughout, so searches for "define", "fine-tuning", "effect" and the like will miss. **The suggested-action tables (Section 3, from 616 through about 2550) are three-column and interleave badly.** The action text, risk tags and IDs are scrambled across lines (see 659–665).
- **TOC:** 72–81 (p4).
- **Glossary:** none. The text says one "will be developed and hosted" on the AIRC (130–132, p6). Footnoted definitions (EO 14110's *Generative AI* and *dual-use foundation model*) are at 108–113 (p5). **The twelve named risks at 216–278 (p8–9) are in effect this document's defined-terms list.**
- **Passages:**
  1. **138–213 (p6–7).** How GAI risk "can vary": along lifecycle stage, scope, source and time scale. Then an explicit **evidential scope rule**: "This document focuses on risks for which there is an existing empirical evidence base … speculative risks that may potentially arise in more advanced, future GAI systems are not considered" (191–194). Footnote 5 (205–213) offers an alternative three-way grouping derived from the UK International Scientific Report.
  2. **216–278 (p8–9).** The twelve risks, each a one-sentence definition (CBRN, Confabulation, … Value Chain). Footnote 6 (249–251) records that "hallucination" was rejected because it anthropomorphizes. Footnote 8 (257–262) gives a definition of *harm* by counterfactual baseline.
  3. **281–330 (p9–10).** CBRN and Confabulation. The CBRN section contains a dated empirical finding ("LLM outputs regarding biological threat creation … provided minimal assistance beyond traditional search engine queries", 289–292), followed by a forecast framed by capability ("may augment design capabilities … beyond what text-based LLMs are able to provide", 297–299).
  4. **616–700 (p16–18).** How the action tables work (Action ID, GAI Risks, AI Actor Tasks), then the first tables. Look at how garbled they are before deciding whether to rely on this extraction for Section 3.
  5. **2629–2655 (p52–53)** and **2798–2831 (p56–57).** Pre-deployment testing limits, and incident disclosure. The latter gives a definition of *AI incident* in quotation marks, with no source named in the lines I read (2801–2807), and an observation about the incident ecosystem: databases "track by amount of media coverage" (2811–2812).

### nist-2025-managing: NIST AI 800-1 2pd, "Managing Misuse Risk for Dual-Use Foundation Models" (second public draft, U.S. AISI, Jan 2025). 3308 lines, 69 pp

- **Extraction note:** draft line numbers (1–40) are printed at the start of every line, and running headers repeat on every page. The appendix tables are wide.
- **TOC:** 97–114 (p4).
- **Glossary:** Appendix A, **1027–1102 (p27–28)**: *AI, AI red-teaming, distribution channel, dual-use foundation model (EO 14110 text, including "permitting the evasion of human control or oversight through means of deception or obfuscation", 1055–1056), fine-tuning,* **margin of safety***, misuse risk, model flaws, model performance, unauthorized access, proxy models,* **threat profile***.*
- **Passages:**
  1. **174–256 (p6–7).** Scope and actors. It applies only to "the additional or novel misuse risk that a model introduces (i.e., the marginal risk)" (182–183). Its focus is on "**initial developers**" (191–201). Then a supply-chain role list: compute providers, model hosting platforms, "downstream model adapters, application developers, and deployers", distribution platforms. Footnote vii (206–208): the document "does not cover risks from accidental AI harms".
  2. **300–360 (p9–10).** "Key challenges": seven numbered epistemic claims about why misuse risk is hard to know. "Safeguards … are often underdeveloped and brittle" (353–359).
  3. **673–781 (p18–21).** Objective 4 (measure) and Practice 4.2 (red-team safeguards). This is the characteristic three-part unit: Practice → Recommendations → Documentation. Note the adversary-parity reasoning ("Compare the red team's expertise, resources, and time available to those of a relevant threat actor", 744–749).
  4. **1538–1612 (p37–39).** Appendix D (chem/bio). Threat-actor categories (state versus three illustrative non-state profiles), threat scenarios, and **technical, operational and motivational barriers**. A classification of how uplift could happen.
  5. **1198–1260 (p31–32).** Appendix C, measurement environments: a typology running from Q&A to physical environment, with examples.
- **Also:** Appendix E (cyber), 2267–3308 (p52–69), has the same D-shaped structure; its subsection headings are at 2277–2835.

### nist-2026-ai-800-2-ipd: NIST AI 800-2 ipd, "Practices for Automated Benchmark Evaluations of Language Models" (CAISI, Jan 2026). 1642 lines, 39 pp

- **Extraction note:** draft line numbers at line starts. "Terms defined in the Glossary are underlined" (183), but **the underlining is lost** in extraction.
- **TOC:** 115–130 (p5).
- **Glossary:** Appendix A, **1525–1642 (p37–39)**: *baseline, behavior, benchmark, capability, content validity, evaluation objective, evaluation protocol (+ settings), external validity, metric,* **measurement construct / measurement criterion / measurement instrument / measurement validity***, proxy task, robustness, scaffolding, task, test item, trial.* The construct/criterion distinction is borrowed from measurement theory.
- **Passages:**
  1. **147–219 (p6–7).** Scope and audience, and Table I.1: when automated benchmarks fit and when they don't (structured vs open-ended, time-invariant vs dynamic, and so on). Practices are labelled "[Emerging Practice]" where they are less mature (153–154), which is a built-in maturity marker.
  2. **314–400 (p9–11).** Practices 1.1–1.2: define the measurement target and select benchmarks, with preregistration-like documentation "before conducting the evaluation" (356–357).
  3. **1367–1411 (p32–33).** **Practice 3.3, "Report qualified claims."** Read this one. It is NIST telling evaluators to "Differentiate observations, inferences, predictions, and normative statements" (1378–1379), to report the evidence linking a benchmark to its construct, and to flag evaluation awareness as a threat to external validity (1402–1404). It is, near enough, a schema for the kind of claim-tagging you are designing, written by a source.

### nist-2026-ai-800-4: NIST AI 800-4, "Challenges to the Monitoring of Deployed AI Systems" (CAISI, Mar 2026). 2085 lines, 49 pp

- **TOC:** 116–171 (p5–6), including lists of tables and figures.
- **Glossary:** none as a section. The terms *post-deployment* and *monitoring* are defined at **335–351 (p11)**. **Table 1, 408–446 (p13)**, defines the six monitoring categories, each as a question plus a "Measuring …" definition. **Appendix C codebook, 1582–1645 (p39–41).**
- **Passages:**
  1. **335–399 (p11–12).** Definitions, then method (23 → 87 papers, three workshops, inductive thematic coding by two reviewers). Then the contribution statement: "the primary contributions … are the identification and documentation of monitoring challenges, and **reporting of views expressed by experts** in the field" (396–398).
  2. **679–730 (p19–20).** "Gap: Immature information sharing ecosystem". The genre in full: an anonymous attendee quotation, then a literature quotation, then another attendee quotation, all under a Gap/Barrier label. It notes "the term 'AI incident' as 'a relatively new term' that lacks clear definition" (703–704).
  3. **1032–1135 (p26–28).** Human factors and security monitoring. It quotes attendees on "sycophancy" and "anthropomorphization" (1074–1075), and quotes the literature on models that "deliberately present themselves as aligned … when monitored" (1125–1127). An attendee asks "Is the model agentically attempting to subvert the monitoring setup it is under, i.e., scheming?" (1129–1130).
  4. **1274–1330 (p32–33).** Open questions (who, what, when, why), almost entirely in the form of attendees' questions.
- **Why it's distinctive:** most of its content is **attributed speech coded into categories**. NIST asserts that people said X, and asserts the coding. It does not assert X.

### vassilev-2025-adversarial: NIST AI 100-2e2025, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations" (Mar 2025). 5977 lines, 127 pp

- **Size note:** the References run from **3355 to 5627** (p74–120). That is about 38% of the file, so the prose body is about 3000 lines.
- **TOC:** 144–222 (p5–7). **Taxonomy index with IDs: 297–362 (p10–11)** (NISTAML.01 … .05 and their children, e.g. "Misaligned Outputs (ID: NISTAML.027)" at 345).
- **Glossary:** Appendix A, **5628–5977 (p120–127)**. In the source PDF, glossary terms appear in SMALL CAPS; in this extraction they appear in ALL CAPS in the body text (e.g. "AVAILABILITY BREAKDOWN", 2345).
- **Passages:**
  1. **373–439 (p12–13).** Executive summary. It classifies attacks along five axes (400–404). It defines risk as "a measure of the extent to which an entity … is threatened by a potential circumstance … and the severity of the outcome" (406–409), which differs from the RMF's probability × magnitude. It declines to address risk tolerance (409–411) and excludes non-adversarial flaws (424–427).
  2. **2341–2418 (p52–54).** GenAI attacker objectives: availability, integrity, privacy, and the GenAI-specific **misuse enablement**, which "circumvent[s] technical restrictions imposed by the GenAI system's owner", where those restrictions include "RLHF for safety alignment" (2371–2382). Then attacker capabilities (training-data, query, resource, and model control).
  3. **2507–2545 (p56–57).** Direct prompting and the definition of **jailbreak** (2520–2522).
  4. **2918–2931 (p64)**, NISTAML.027. "Misaligned outputs" here means outputs that "align with adversarial objectives" via indirect injection: an integrity violation, not a values failure.
  5. **3129–3180 (p69–70)** and **3294–3330 (p72–73).** Theoretical limits. Detection of adversarial examples "is equivalent to robust classification" (3138–3140). "so long as a model has any probability of exhibiting an undesired behavior, there exist prompts that can trigger that behavior, implying that any alignment process that attenuates but does not remove an unwanted behavior will remain vulnerable" (3317–3320). Compare `nist-2026-vassilev-proof`.

---

## D. CAISI evaluation reports

### caisi-2025-deepseek-eval: "Evaluation of DeepSeek AI Models" (CAISI, Sep 2025). 2323 lines, 69 pp

- **TOC:** 64–97 (p3).
- **Glossary:** none. The **operational definitions are embedded in the methods**: *benchmark contamination* (footnote, 152–154, p4); **"hijacked" = attempted the malicious task, whether or not it succeeded** (1496–1509, p46); the *CCP alignment score* (1739–1745, p53); the *expense-performance curve* (1346–1350, p42).
- **Passages:**
  1. **10–58 (p2).** Executive summary. Six bolded findings, each a measurement framed comparatively (U.S. vs PRC). A normative-risk conclusion: "the expanding use of these models may pose a risk to application developers, to consumers, and to U.S. national security" (56–58).
  2. **103–178 (p4–5).** The mandate as the report's own justification ("As directed by President Trump's AI Action Plan…"). A self-characterization: "an objective, reliable perspective" (119–120). A scope exclusion: "does not investigate how these models were developed … or the possibility that they were trained on distilled data" (129–131). The deployment choice matters: open weights self-hosted, "CAISI did not query DeepSeek's API" (168–176).
  3. **1431–1543 (p45–48).** Agent hijacking. Task choices, a disclosed methodological intervention (an added anti-injection paragraph in the system prompt, 1487–1490), and a disclosed non-adaptivity: "This is not an adaptive evaluation … an imperfect proxy assessment" (1482–1485).
  4. **1700–1760 (p53–54).** The censorship evaluation. Its dataset comes from Department of State SMEs, with "narrative flags" defined as statements "identified as narratives used by the CCP" (1719–1722), and it is scored by LLM-as-judge. "Alignment" here means agreement with a narrative.
  5. **1929–1950 (p61).** The disclaimer: "findings should be considered preliminary … should not be interpreted as a certification or endorsement". Read it against the executive summary; the two registers sit 1,900 lines apart.
- **Also:** benchmark-selection rationale, which is mostly about contamination, 2217–2279 (p67–68); CAISI results vs self-reported results, 2283–2318 (p68–69).

### caisi-2026-glm52: "Assessment of Z.ai's GLM-5.2" (CAISI, 8 Jul 2026). 519 lines, 21 pp

- **TOC:** 41–63 (p3).
- **Glossary:** none. There are operational definitions: "coding" as used by the developer is glossed as "defined to include software engineering and cyber tasks" (98–99). **"Frontier models are defined as those with a greater latent capability level than any previous model released by developers from that country"** (514–516, p21). *Weighted tokens* is defined at 483–484.
- **Passages:**
  1. **13–38 (p2).** Executive summary, with calibrated hedge words: "was **probably** the most capable open-weight AI model" (17), "appears **potentially** more robust" (27). An important caveat: "safeguards for open-weight models can be circumvented when self-hosted" (29–31).
  2. **85–101 (p5).** The **four-voice unit** that recurs in every section: "CAISI Overall Assessment" / "CAISI Results" / "Developer's Self-Reported Results" (quoted) / "CAISI Comment" (disputing the developer's claim). The report explicitly weighs the developer's claims against its own. See also 124–136, 158–169 and 195–222.
  3. **195–222 (p11).** Safeguards. The model refuses overtly malicious cyber queries but "did not refuse any" agentic exploit-development tasks (211–212). Results are a "lower bound" because abliteration is available (205–207).
  4. **439–469 (p19).** Safeguards configuration. U.S. closed models were tested with "system-level safeguards disabled" for capability, and with safeguards enabled for safeguard tests. The distinction between system-level and model-level safeguards is made explicit (459–469).
  5. **491–519 (p21).** IRT method, the "frontier" definition, and a Working–Hotelling band: "any linear trend that exits the shaded region … is rejected at the 95% confidence level" (518–519).

### CAISI evaluation web posts (read whole; each under 300 lines)

These are shorter versions of the report genre. They show how a finding is compressed for publication, and how the evaluation series builds its own comparison baseline over time.

- **nist-2025-caisi-deepseek**: news release for the DeepSeek report (30 Sep 2025). 118 lines. **Hard-wrapped at 80 characters, with words split mid-line.** 29–41: the Secretary's quote ("The report is clear that American AI dominates, with DeepSeek trailing far behind. This weakness isn't just technical") wraps the findings at 78–113. Two voices in one document.
- **nist-2025-caisi-kimi-k2**: "CAISI Evaluation of Kimi K2 Thinking" (12 Dec 2025). 153 lines. Findings at 30–55. The table at 56–133 is flattened to one number per line, with model order given at 59–65. 145–151: a methodology caveat that scores "are not directly comparable" with the earlier report's.
- **nist-2026-caisi-deepseek-v4**: "CAISI Evaluation of DeepSeek V4 Pro" (1 May 2026). 260 lines, p1–5. 30–53: "lags behind the frontier by about 8 months" (a capability gap stated in time units). There is a self-report vs independent-report contrast, and 180–190 says CAISI "pre-committed to its overall benchmark suite, i.e. did not select benchmarks on the basis of results" (a methodological honesty claim). IRT appendix: 221–258.
- **nist-2026-aisi-caisi-kimi-k3**: UK AISI / CAISI "Preliminary Assessment of Kimi K3's Cyber Capabilities" (23 Jul 2026). 141 lines. The **capability claim plus realism caveat** at 128–137: "capable of autonomously attacking small, weakly defended and vulnerable enterprise systems … However, TLO differs from real-world environments" (no active defenders, no alert penalty, an intentional attack path). Also 134–137: "Solves of TLO are no longer exclusive to a small set of models."
- **nist-2026-caisi-glm53**: "CAISI's Assessment of Z.ai's GLM-5.3 Cyber Capabilities" (17 Sep 2026). 178 lines. 63–70 defines "U.S. frontier best", "including both trusted-access releases and full public releases", and excludes unreleased models "which could have stronger capabilities". 136–175 gives the IRT/Elo explanation with a worked odds example.

---

## E. CAISI / NIST institutional announcements and other items (read whole)

Most of these are short web pages. As a class they are **institutional self-description**: what CAISI is for, whom it works with, what it has done. That matters for modelling the actors behind the evaluation claims.

- **commerce-2025-caisi**: Secretary Lutnick's statement transforming the U.S. AISI into CAISI (3 Jun 2025). 117 lines. **Hard-wrapped at 80 characters, words split** (Wayback snapshot; the live site returned 403). 30–37: "For far too long, censorship and regulations have been used under the guise of national security." 42–75: the CAISI mandate list (the source of the "primary point of contact" and "demonstrable risks, such as cybersecurity, biosecurity, and chemical weapons" phrasings used across the later documents).
- **nist-2025-caisi-openai-anthropic**: "CAISI Works with OpenAI and Anthropic to Promote Secure AI Innovation" (25 Sep 2025). 50 lines. The content is 31–48. It asserts that improvements were made by the companies and points to the companies' own blog posts as the evidence (37–44).
- **nist-2026-caisi-agreements**: "CAISI Signs Agreements … With Google DeepMind, Microsoft and xAI" (5 May 2026). 61 lines. **Provenance: the live URL has returned 404 since 8 May 2026 (the page was withdrawn); the text is from Wayback** (2–6). 38–52: more than 40 evaluations completed, including unreleased models. "developers frequently provide CAISI with models that have reduced or removed safeguards" (46–47). Classified-environment testing. The TRAINS Taskforce.
- **nist-2026-agent-standards**: "AI Agent Standards Initiative" (17 Feb 2026). 71 lines. 31–63. Adoption and interoperability framing. Security appears as a precondition for adoption, not as a risk in its own right. Three pillars.
- **nist-2026-ai-consortium**: AISIC renamed to the NIST AI Consortium (29 May 2026). 134 lines. 30–122. A **renaming as a signal of changed scope** ("Formerly known as the AI Safety Institute Consortium", 45–52). Six task groups, including a restarted Chem/Bio group (107–110).
- **nist-2026-caisi-careers**: "Careers at CAISI" (updated 27 Aug 2026). 111 lines. 20–107. Team descriptions work as an inventory of what CAISI measures (agent security including "reward hacking" at 47; frontier assessment; chem/bio; cyber). "acts as a startup within government" (21–22). Every team is "not hiring". Line 107 contains the source's own typo, "is hiring not hiring".
- **nist-2026-intl-network**: International Network publishes consensus areas (13 Feb 2026). 61 lines. 34–57. The network's membership (38–40). CAISI's participation is framed as a way to "counter authoritarian influence" (44–45) and "advocate for U.S. interests" (55–56).
- **nist-2026-caisi-redteam**: CAISI blog, "Insights into AI Agent Security from a Large-Scale Red-Teaming Competition" (23 Mar 2026). 108 lines. 32–98. A definition of agent hijacking as "also known as indirect prompt injection" (40–45). Findings: at least one successful attack against every one of 13 models; robustness "did not correlate uniformly with model capability" (74–77); attacks transfer asymmetrically from robust to less robust models (78–83).
- **nist-2026-caisi-transcripts**: CAISI blog, "Analyzing Transcripts from AI Agent Evaluations" (18 Feb 2026). 66 lines. 32–57. It points to an earlier post on "how AI models can cheat on agentic evaluations" (32–35) and to transcript review as a measurement-validity tool.
- **nist-2026-ai-800-4-release**: news item for NIST AI 800-4 (9 Mar 2026). 117 lines. 30–112. The six categories and a sample of the challenges, in table form flattened to lines. The report's methods reduced to one paragraph.
- **nist-2026-vassilev-proof**: "NIST Mathematical Proof Supports Transition to a Continuous-Monitor-and-Update Security Model for AI Systems" (9 Jun 2026). 133 lines. 35–117. **An impossibility claim relayed through a press release**: "there is no finite set of guardrails that is universally robust against adversarial prompts" (64–65). The Gödel analogy, a quote with a hedge ("in AI you likely can't patch", 108), and an economic-equilibrium goal (107–113). The underlying paper is "Robust AI Security and Alignment: A Sisyphean Endeavor?" (114–117). Compare `vassilev-2025-adversarial` 3314–3320.
- **nist-2026-vcat-ai-update**: "NIST Artificial Intelligence Update", a slide deck for NIST's Visiting Committee on Advanced Technology (27 Mar 2026). 435 lines, 28 slides. **Multi-column slides interleave badly (for example 80–102 and 225–233).** Most informative:
  - **168–186 (p12).** CAISI partnership types. The MOU capabilities include "Waiver of terms of service in order to jailbreak and probe for security issues" (178–179).
  - **187–205 (p13).** TRAINS taskforce membership and goals.
  - **207–233 (p14).** The ART system: "Security benchmarks often overestimate models' robustness against adaptive attackers" (221–222).
  - **80–102 (p7).** Action Plan items mapped to NIST. Garbled, but it includes the RMF-revision item.
- **nist-2026-rfi-agents**: Federal Register RFI, "Security Considerations for Artificial Intelligence Agents" (CAISI, 91 FR 698, 8 Jan 2026). 364 lines, p1–4. **Badly garbled:** three-column FR layout, interleaved line by line. The file also **contains unrelated notices on the same FR pages**: countervailing duties on oil-country tubular goods (1–90) and an AbilityOne procurement-list addition (269–364). The RFI itself runs from about 57 (column 3 of p1) to about 327. Worth untangling: the Background, which defines *AI agent systems* ("at least one generative AI model and scaffolding software that equips the model with tools…", roughly 148–164, column 2). It also names three risk categories, including "the risk that the behavior of uncompromised models may nonetheless pose a threat … (e.g., models that exhibit specification gaming or otherwise pursue misaligned objectives)" (roughly 104–132, column 3). The question list follows (Sections 1–5, roughly 182–345). I'd suggest a non-`-layout` re-extraction of just this document before anyone quotes from it.

---

## F. DHS and CISA

### dhs-2024-ai-roles-framework: DHS, "Roles and Responsibilities Framework for Artificial Intelligence in Critical Infrastructure" (14 Nov 2024). 1452 lines, 35 pp

- **TOC:** 11–51 (p2).
- **Glossary:** Appendix B, **1215–1289 (p31–32)**. It opens with a disclaimer: "Many terms in this document have various definitions across laws and guidance … [we] defer to entities to use the definitions most appropriate to their activities" (1216–1218). Look at **AI DEPLOYERS**: "They may enable access to AI, **develop the models themselves**, or create software tools…" (1232–1235). So the deployer definition overlaps the developer role. **AI PLATFORM**: "a subcategory of developers" (1244). *Foundation model* is quoted from EO 14110 but stops at "high levels of performance at tasks" (1276–1278), without the risk clause.
- **Passages:**
  1. **316–390 (p10–11).** Risks. Three attack-vector categories (attacks using AI, attacks targeting AI, design and implementation failures). Then **four scale-ordered risk categories** (asset, sector, systemic/cross-sector, nationally significant), adapted from NSM-22, with a compounding claim (383–386). The Figure 1 sidebar garbles 338–362.
  2. **396–464 (p12–13).** Roles, and the key-terms definitions of *entity, roles, responsibilities*: "AI developers include model developers as well as application developers" (447–448). It notes that "entities may play more than one role" (421–429).
  3. **592–700 (p17–19).** The AI Developers role. It aggregates "developers of AI models, platforms, and applications—into a single category" (602–604). Responsibilities are "should" statements, among them "**Ensure alignment with human-centric values**", defined as reflecting "human values and goals … helpful, accurate, unbiased, and transparent" (669–673). The overview grid at 611–633 is garbled.
- **Also:** Appendix A matrix, 1158–1214 (p30). A wide table, readable only in a wide window.
- **Context:** the letter from the Secretary (57–115) and the board membership list (121–158, including the CEOs of OpenAI, Anthropic, NVIDIA, Microsoft and Alphabet) are the provenance of the "consultation".

### cisa-2026-insider-threat-guide: CISA "Insider Threat Mitigation Guide" (Sep 2026). 5295 lines, 113 pp

- **What it is:** a general (not AI-specific) insider-threat program guide for critical infrastructure. **Only one section addresses AI** (1643–1692). **Two-column layout throughout, interleaved line by line in most prose** (e.g. 70–87, 142–174). Open it in a wide window, or expect to reassemble sentences.
- **TOC:** 9–69 (p2–3).
- **Glossary:** Appendix B, "Terms and Acronyms", **5051–5295 (p109–113)**.
- **Passages:**
  1. **382–470 (p11–12).** Definitions of *insider* and *insider threat*, followed by an explicit **license to redefine**: "A best practice is for an organization to define the insider threat in a way that addresses the unique nature of its operating environment" (405–412). Types: unintentional (negligent/accidental) vs intentional.
  2. **661–760 (p17–18).** The six-stage "pathway to intended violence" (grievance → preparation → exploration → experimentation → execution → escape; FBI-adapted). This is a **staged behavioral process model** with explicit non-determinism ("does not guarantee", "may skip certain steps", 691–698).
  3. **810–860 (p20).** The first case study, "When an Insider Becomes an Insider Threat". It is an incident account coded into Stressors / Personal Predispositions / Concerning Behaviors / How It Was Disrupted. Other case studies begin at 980, 2573, 3263, 3945, 4691 and 4742.
  4. **1643–1692 (p37).** "Artificial Intelligence and Insider Threat Mitigation Considerations". Insiders as vectors against AI (data poisoning, "model tampering"), and AI as a vector against insiders (deepfake social engineering). The AI system itself is never treated as an insider.
- **Why it might matter:** EO 14409 (110) and NSPM-11 (147–148) both use "insider-risk" and "personnel vetting" language for frontier-model access. This guide is the government's worked-out vocabulary for that frame, but it frames insiders as humans only.

---

## Across the set: how these documents make their claims

**1. The genre determines the speech act, more than the topic does.** Across this set, I would expect a schema to need at least these distinct kinds of assertion, several of them beyond your current list:

- **Tasking / allocation** (EOs, NSPM-11, Action Plan): "Within 90 days, [official] shall …". This is neither a commitment nor a recommendation. It assigns a duty to a named office, with a clock. The claims about the world in these documents sit in the purpose section and serve as justification.
- **Definition by procedure or by secret** (EO 14409 "covered frontier model"): the term is defined as the output of a classified process run by a named official. The schema would need to be able to say "defined, content not public".
- **Definition-maintenance clauses** (SB 53 §22757.14): criteria a definition must satisfy (verifiable by third parties, determinable before training), plus a duty to revisit it. This is a claim about definitions, not about AI.
- **Exclusions, carve-outs and savings clauses**: "does not include", "Nothing … shall be construed to authorize … licensing", the preemption carve-outs, "shall not apply to the extent that it strictly conflicts with … a contract between a federal government entity and a frontier developer". Much of the *meaning* of the statutes and EOs lives here.
- **Deeming and equivalence**: "shall be deemed in compliance" (model card = transparency report; federal-standard designation in both SB 53 and RAISE).
- **Adopted third-party representations under reliance** (CA AG MOU): the government records a counterparty's claims and makes its own position contingent on their truth.
- **Reported speech coded into categories** (AI 800-4): attributed, usually anonymous, quotations, sorted into Gap / Barrier / Open question. The agency asserts the *coding*, not the content.
- **Questions as content** (RFI; AI 800-4 open questions; the VCAT feedback slide): these frame what the agency thinks is unknown.
- **Multi-voice evaluation** (GLM-5.2 especially): "CAISI Overall Assessment" vs "CAISI Results" vs quoted "Developer's Self-Reported Results" vs "CAISI Comment". A single report explicitly disputes a developer's claim.
- **Impossibility or theoretical-limit claims** (AI 100-2 4.1.2 and 4.2.5; the Vassilev proof release): the claim is that no mitigation of a certain form can be complete.
- **Process and stage models** (CISA's six-step pathway), and **case studies** coded to indicators.
- **Explicit maturity markers** ("[Emerging Practice]" in AI 800-2; "preliminary" in the CAISI posts; "second public draft").

**2. Hedging registers differ sharply, and they sort cleanly by genre.** CAISI evaluations hedge like a measurement lab: calibrated words ("probably", "appears potentially"), confidence intervals, disclosed deviations and a separate disclaimer. The GLM-5.2 and DeepSeek V4 posts also state methodological commitments ("pre-committed to its overall benchmark suite"). NIST frameworks hedge through *modality and voluntariness* ("can", "may consider", "voluntary", "not intended to supersede"). Statutes hedge through *legal standards* ("foreseeable and material", "reasonable cause to believe", "good faith and … reasonable under the circumstances"). White House documents (EOs, the Action Plan, the fact sheet) and the Commerce statement don't hedge at all ("tremendous", "dangerous", "by definition"). The one clear exception is the legislative framework's "the Administration believes … acknowledges arguments to the contrary exist" on copyright. Several documents carry **two registers under one key**. In the DeepSeek release, the Secretary's quote wraps the lab findings. The NSPM-11 file holds both the memorandum and its fact sheet. The DeepSeek report's executive summary and its disclaimer sit 1,900 lines apart. So a schema probably needs a *speaker* per assertion, not per document.

**3. Term collisions I saw inside this set** (I've pointed to lines; the interpretation is mine):

- **developer**: SB 53 and RAISE use a compute-threshold role ("trained, or initiated the training of") and a revenue-threshold tier (*large*). AI 800-1 distinguishes "initial developers" from "downstream model adapters, application developers, and deployers". DHS merges model, platform and application developers into one role, while its glossary's *deployer* "may … develop the models themselves". The RMF puts "developers" in three different actor categories.
- **alignment**: (a) agreement with a narrative (the "CCP alignment score"; the Action Plan's "alignment with Chinese Communist Party talking points"); (b) "alignment with human-centric values" as a developer responsibility (DHS 669–673); (c) "safety alignment" as a *technical restriction* that attackers circumvent (AI 100-2 2377); (d) "misaligned outputs" as outputs aligned with an **attacker's** objective (AI 100-2 NISTAML.027); (e) "pursue misaligned objectives" as a security risk of *uncompromised* models (RFI); (f) the Vassilev paper title, "Robust AI Security and Alignment". NSPM-11 avoids the word and uses *steerability* and *controllability* instead.
- **control / loss of control**: "Evading the control of its frontier developer or user" and "Loss of control of a frontier model causing death or bodily injury" (SB 53 / RAISE). "permitting the evasion of human control or oversight through means of deception or obfuscation" (EO 14110, via AI 800-1 and DHS). *Controllability* = "monitor … and take corrective action" (NSPM-11 Sec. 6). NSPM-11's Assurance pillar uses control in the sense of *a vendor's ability to disable or modify a system the government depends on*. The Action Plan's "AI control systems" is a research program.
- **safeguard**: CAISI distinguishes system-level from model-level safeguards and routinely disables the former for capability measurement (GLM-5.2 459–469; Kimi K3 59–61). Developers "frequently provide CAISI with models that have reduced or removed safeguards" (agreements 46–47). The same idea appears as "guardrails" (Vassilev release), "technical restrictions" (AI 100-2), and as terms of service waived "in order to jailbreak" (VCAT 178).
- **risk**: probability × magnitude (RMF, AI 600-1, AI 800-1); the extent to which an entity is threatened × severity (AI 100-2); a thresholded legal construct (SB 53 *catastrophic risk*); marginal risk (AI 800-1); four scale-ordered categories (DHS).
- **frontier**: a 10^26-operations threshold (SB 53 / RAISE); "greater latent capability level than any previous model … from that country" (GLM-5.2 514–516); "U.S. frontier best" including trusted-access releases (GLM-5.3 63–67); "covered frontier model" set by a classified cyber threshold (EO 14409).
- **incident**: SB 53's four-type *critical safety incident*; AI 600-1's quoted *AI incident*; NSPM-11's *AI incident response*. AI 800-4 records that practitioners find "AI incident" undefined.

**4. Near-duplicate texts are a structural feature here.** SB 53 and RAISE share most of their definitions and obligations word for word, with different clocks, penalties and regulators, and one registration regime. The CAISI posts reuse one IRT paragraph with small variations (400 points = 10x odds vs 200 points = 3x). Commerce's June 2025 mandate list reappears nearly verbatim in the DeepSeek report, the DeepSeek release, the careers page and the agreements page. A quote-level model will run into "same sentence, many sources" often, and it may want a way to point to the originating instance.

**5. Extraction and provenance issues worth carrying forward:**

- `nist-2026-rfi-agents`: three-column garble plus unrelated notices. Re-extract before quoting.
- `nationalinstituteofstandardsandtechnologyus-2024-artificial`: ligatures break search, and the action tables are scrambled.
- `ny-2026-raise-s8828`: italics (new matter) lost, so old and new text can't be distinguished. Also "10º26".
- `commerce-2025-caisi` and `nist-2025-caisi-deepseek`: words split by 80-column wrapping.
- `whitehouse-2026-nspm-11`: taken from a mirror, not checked against whitehouse.gov.
- `nist-2026-caisi-agreements`: withdrawn from nist.gov (404 since 2026-05-08).
- `cisa-2026-insider-threat-guide` and `whitehouse-2026-legislative-framework`: two-column interleaving.

---

## Notes on the brief and the process

- **Scratchpad collision.** The scratchpad directory is shared by all ten atlas agents. I wrote two small helpers named `pl.sh` and `pg.sh` at the scratchpad root, and at least one other agent wrote scripts with the same names, so we overwrote each other. My page numbers were recomputed at the end with a helper in `scratchpad/usgov-atlas/`, so they are consistent. But another agent may have run my version of `pg.sh` or `pl.sh` without noticing. For future fan-outs, a per-agent subdirectory would avoid this. I also left `out1.txt`, `out2.txt` and `out3.txt` (plain text dumps) at the scratchpad root.
- **Pages for web renderings.** For the 18 web-page keys, the "PDF page" is a page of an agent-made rendering, so it won't survive a re-render any better than a line number would. Line numbers are the better anchor for those.
