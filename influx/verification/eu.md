# EU-sources verification: `safety-risk-factors.md`

*Written 2026-09-27 by the EU-sources verifier, a Claude instance. The integrating agent reads it first; Joseph may read it later for the evidence behind a change. Scope: the AI Act, the GPAI Code of Practice (Safety & Security chapter), the Chairs' statement, CSET's Code piece, and Hacker et al. I also covered the CSET crosswalk column, whose values turn out to describe a different CSET document (see §2.4).*

**How I read.** I read the Code whole (all 43 pp.). I read the AI Act provisions the report leans on in full: Art. 3(2), 3(49), 3(63)–(65), Art. 5(1)(a), Arts. 51, 52, 55, 56, 113, Annex XIII, and recitals 110–116. I read Hacker et al. whole (v2 = FAccT '26), CSET-2025 whole, CSET-2021 whole, and §§1–2.3 and §5 of the Commission's GPAI Guidelines. Every quote below was copied from local text extractions of these files; none comes from memory. Where I rely on a secondary source I say so.

**Page numbers.** "p." means the PDF page of the copy filed in relata. The Code's official Commission PDF has 43 pages; the marinacastellaneta.it mirror has 40, so its page numbers do not match these. Section numbers (Measure / Appendix) are the stable pinpoint.

---

## 0. The short version: what most needs changing

1. **"Mandates" / "the mandatory floor" misstates the Code's legal status.**
   - The Code is a voluntary instrument. Signatories *commit* to it, and adhering to it is one way of *demonstrating* compliance with AI Act Art. 55. It is not law.
   - The Code itself says adherence "does not constitute conclusive evidence of compliance".
   - The Commission's Guidelines say that, unlike harmonised standards, adherence to a code does **not** give a presumption of conformity.
   - Both CSET-2025 and Hacker et al. make the opposite ("presumption of conformity") error, which is probably where the report's framing came from.
   - Details in §1.
2. **The Code's organizational content is entirely *mitigation*, never a *risk source*.**
   - The Code's own glossary classes Commitments 1 and 7–10 (including Commitment 8) as "governance mitigations".
   - Its risk-source taxonomy (App. 1.3: 14 + 10 + 13 items) contains no organizational source at all.
   - So the exec summary's "turns organizational factors into commitments" should be recast. The accurate statement actually *strengthens* the report's gap thesis (C15): the most detailed instrument regulates how a developer is organized, but never names the organization as a source of risk. See §3.1.
3. **"The only primary instrument that turns organizational factors into commitments" is false.**
   - California SB 53 (signed 29 Sep 2025) requires large frontier developers to write, implement and publish a frontier AI framework covering "internal governance practices", and it adds whistleblower protections to the Labor Code.
   - The defensible claim is "the most granular". See §2.1.
4. **Recommendation 3 (the Measure 1.3 hook) leans on the weakest reading.**
   - Example ground (1) is about "how the Signatories develop models". It is also conditional: the change must be one that "can be reasonably foreseen to lead to the systemic risks … not being acceptable".
   - The Measure's headline trigger fits better: reasonable grounds that "adherence thereto has been or will be materially undermined". The Framework-adherence assessment and the remediation-plan requirement that follow it fit too.
   - Three further hooks name organisational complexity or scale with headcount: Measure 8.1 ("organisational complexity"), App. 4.3(1) (six-monthly access re-authorisation) and App. 4.4(1) (background checks).
   - Details in §2.9.
5. **Loss of control is pooled across at least four different scales in these sources.** This is exactly Joseph's worry. They range from an operator failing to intervene in a deployed system (CSET-2021), through a reportable self-exfiltration incident (Code Measure 9.3(2)), to a scale-free inability to "reliably direct, modify, or shut down" a model (Code App. 1.4(2)), to a catastrophe-bounded ">50 deaths / >$1B, single incident" definition (SB 53). See §4.2.
6. **Factual fixes:**
   - The CSET Code piece is by Mia Hoffmann and dated **30 Jul 2025**, not 19 Dec 2025.
   - The 10^25 FLOP presumption is in **Art. 51(2)**, not Annex XIII. Annex XIII lists designation criteria and has its own 10,000-business-user reach presumption.
   - The A18 "AI welfare" EU-CoP cell rests on "non-human welfare", which is undefined in the Code and is read by commentators as *animal* welfare.
   - A8 and A13 have no Safety & Security chapter support.
   - B10 misreads App. 1.2.2(3) ("high velocity" is how fast a *risk* materialises, not deployment velocity).
   - §5.6 contrasts the Code with "RAND's actor-based threat model", but the Code is also actor-based: its Measure 6.1 and glossary define a sized "non-state external threat".
7. **The CSET column holds CSET-2021 (Arnold & Toner) values, and it undercounts them.** CSET-2021 explicitly names *competitive pressure* as a risk factor (C1). It also names system complexity and "systems with many instances" (C12), and over-reliance by users (A11). None of these is in the report.
8. **The AI Act has since been amended.**
   - Regulation (EU) 2026/1744 (the "Digital Omnibus on AI") has been in force since 27 Jul 2026, per secondary sources.
   - As summarized by FLI's explorer, it reportedly leaves Arts. 3(63)–(65), 51–56, 101 and Annex XIII unchanged. I did **not** obtain the OJ text; the Publications Office CELEX URL returned 404.
   - Separately, the Commission's GPAI fining powers under Art. 101 have applied since 2 Aug 2026. As of today, the Code's commitments therefore sit under live enforcement.

---

## 1. Binding status, and factor vs mitigation (the coordinator's lens)

This comes straight from the texts. "Commits / will" is the Code's own verb for what signatories undertake. "Examples … and/or" marks illustrative lists.

| What the report leans on | Status | Factor or mitigation? | Evidence (verbatim) |
| --- | --- | --- | --- |
| AI Act Art. 55(1)(a)–(d) (evaluate, assess & mitigate, report incidents, cybersecurity) | **Law.** Binding on GPAISR providers from 2 Aug 2025 (Art. 113(b)). Commission fines (Art. 101) from **2 Aug 2026**. | Obligations (mitigation duties) | Art. 55(1), p.86. Fining date: GPAI Guidelines ¶106, p.29: "impose fines of up to 3% of global annual turnover or EUR 15 million … starting on 2 August 2026." |
| The Code as a whole | **Voluntary.** Binding only as a signatory's commitment, and a means of *demonstrating* Art. 55 compliance. | — | Code, Objective A, p.2: "to serve as a guiding document for demonstrating compliance … while recognising that adherence to the Code does not constitute conclusive evidence of compliance". AI Act Art. 55(2), p.86: providers "may rely on codes of practice … to demonstrate compliance … until a harmonised standard is published". GPAI Guidelines ¶100, p.27: "A code of practice is a temporary tool … As opposed to adherence to a code of practice, compliance with harmonised standards grants a presumption of conformity". Commission CoP page: the Commission and AI Board "have confirmed that the code is an adequate voluntary tool". |
| Who is bound | Signatories as listed by the Commission (page updated 31 Jul 2026): Amazon, Anthropic, Google, IBM, Microsoft, Mistral AI, OpenAI and others. **xAI signed only the Safety & Security chapter.** Meta is not on the list. | — | digital-strategy.ec.europa.eu/en/policies/contents-code-gpai (fetched 2026-09-27) |
| App. 1.4 specified systemic risks (CBRN, loss of control, cyber offence, harmful manipulation) | **Committed** (for signatories). They must always be *identified*, and they must get capability-defined risk tiers: non-tier criteria are allowed only if "the systemic risk is not a specified systemic risk". | Hazards | Measure 2.1(2), p.11: Signatories "will identify … (2) the specified systemic risks in Appendix 1.4." Measure 4.1(1)(b), p.15. |
| App. 1.1 risk types and examples (non-human welfare, concentration of power, etc.) | Five types are the frame. The examples are ones signatories "will draw upon when compiling the list". **Considered, not mandated as systemic risks.** | Hazards | App. 1.1, p.34 |
| App. 1.2.2 contributing characteristics | Considerations that "inform systemic risk identification" | Properties of risks (neither factor nor mitigation) | App. 1.2, p.34–35 |
| App. 1.3 sources (14 / 10 / 13) | "treated as **non-exhaustive, potential** systemic risk sources for the purpose of systemic risk identification" | **Factors** (the Code's only factor taxonomy) | App. 1.3, p.35 |
| Measure 1.3 Framework assessment | **Committed.** Trigger: "reasonable grounds" or 12 months. The three grounds are "**Examples** of such grounds". | Mitigation (governance) | p.9 |
| Commitment 8 / Measure 8.1 responsibilities | Defining responsibilities is **committed**. The four-part structure, including "must not also be responsible for … core business", sits inside a **presumption-of-fulfilment (safe-harbour) paragraph**: "This Measure is presumed to be fulfilled, if Signatories … adhere to all of the following". | **Mitigation** (governance) | p.23–24 |
| Measure 8.2 resources | **Committed:** "The allocation of such resources will include: (1) human … (4) computational" | Mitigation | p.24 |
| Measure 8.3 risk culture | Promoting a healthy risk culture is **committed**. The seven items are "**Examples** of indicators … and/or". | Mitigation | p.25 |
| Glossary definitions (insider threats, deception, …) | Binding interpretive definitions within the Code | Definitions. "Insider threats" defines a threat-actor class. | p.29–33 |
| Glossary: "systemic risk mitigations" | — | Classifies Commitment 8 as mitigation | p.32: "comprise safety mitigations (pursuant to Commitment 5), security mitigations (pursuant to Commitment 6), and **governance mitigations (pursuant to Commitments 1 and 7 to 10)** for systemic risk." |
| Commitment 6 open-weight exemption | **Committed scope rule** | — | p.18 |
| App. 4 security measures, including **App. 4.3(4)** | Point (a) of each item is the default measure. Signatories may deviate if they "implement alternative security mitigations that achieve the respective mitigation objectives" (Measure 6.2). Implementation "may be staged". **No numeric limit anywhere.** | Mitigation (security) | Measure 6.2, p.18. App. 4.3(4), p.42: "(4) reduction of the risk of insider threats or compromised accounts, through (a) limiting the number of people who have non-hardened interface-access to model parameters." |
| App. 3.4(3), "20 business days" | **Illustrative benchmark**, not a requirement: "For example, a period of at least 20 business days is appropriate for most systemic risks and model evaluation methods" | Mitigation (evaluation resourcing) | p.40 |
| Measure 9.3 deadlines | **Committed** "save in exceptional circumstances" | Mitigation (reporting) | p.26–27 |
| Recital (g), Precautionary Principle | Recital: "The Signatories recognise…" (interpretive) | Principle | p.4 |
| Chairs' statement (100 staff) | **No normative status.** The Chairs' own opinion, published alongside the Code, not part of it. | Recommendation | code-of-practice.ai / artificialintelligenceact.eu |
| CSET-2025, Hacker et al. | Commentary / scholarship | — | — |

**Consequence for §4 of the report.** The "Named?" column counts Commitment 8 and the Measures as evidence that a *factor* is named. By the Code's own taxonomy, the Code names **no organizational risk sources**. It names organizational **mitigations** (Commitment 8, App. 4) and one organizational **threat class** (insider threats, defined in the glossary).

The closest things in App. 1.3 to organizational sources are provider *decisions* and states:
- 1.3.3(3) "release and distribution strategies";
- 1.3.3(7) "lack of appropriate infrastructure security";
- 1.3.3(13) "inappropriate use of the model".

I'd restructure §4 into two columns: "named as a risk source/factor" and "addressed by a mitigation". On that split, safety culture becomes "mitigation: yes (Measure 8.3); factor: no (EU)". It stays a factor for CAIS ("Weak Safety Culture") and for CSET-2021, whose "competitive pressure" is a named risk factor.

---

## 2. Item-by-item corrections

Format: **Current** → **Source says** → **Proposed** → *confidence*.

### 2.1 Executive Summary, first bullet

**(a) Current:** "The EU General-Purpose AI Code of Practice (July 2025) is the most complete authoritative risk-factor list. It mandates four 'specified systemic risks'…"

- **Source:** See §1. Measure 2.1(2) requires *identification* of the App. 1.4 risks. The Code is voluntary (Objective A, p.2).
- **Proposed:** "…It commits signatories to always identify and assess four 'specified systemic risks' (App. 1.4; Measure 2.1(2)), each with capability-defined risk tiers (Measure 4.1(1)). The Code is voluntary: signing it is the Commission-endorsed way of demonstrating compliance with the binding AI Act Art. 55. Commission fines for Art. 55 breaches apply from 2 Aug 2026."
- *Confidence: high.*

**(b) Current:** "It lists 37 systemic-risk sources: 14 capabilities, 10 propensities and 13 affordances or contextual factors."

- **Source:** The counts are correct (App. 1.3.1 items (1)–(14), 1.3.2 (1)–(10), 1.3.3 (1)–(13); p.35–36). The list is "non-exhaustive, potential systemic risk sources".
- **Proposed:** add "non-exhaustive".
- *Confidence: high.*

**(c) Current:** "It is the only primary instrument that turns *organizational* factors into commitments. Its Commitment 8 covers responsibility allocation, resourcing and 'healthy risk culture,' and it defines insider threats in its glossary."

- **Source 1, uniqueness.** California SB 53, Bus. & Prof. Code §22757.12(a): "A large frontier developer shall write, implement, comply with, and clearly and conspicuously publish … a frontier AI framework … [that] describes how the large frontier developer approaches all of the following: … (9) Instituting internal governance practices to ensure implementation of these processes. (10) Assessing and managing catastrophic risk resulting from the internal use of its frontier models, including risks resulting from a frontier model circumventing oversight mechanisms." SB 53 also adds Labor Code ch. 5.1 (§1107 ff.) whistleblower protections. It was approved and filed on 29 Sep 2025 (leginfo). The AI Act itself anticipates the same thing: recital 114, p.30, "putting in place risk-management policies, such as accountability and governance processes".
- **Source 2, "factors".** The glossary classes Commitment 8 as a "governance mitigation" (p.32).
- **Proposed:** "It is the most granular primary instrument on how a frontier developer must *organize* itself. Commitment 8 covers responsibility allocation across four organizational levels, resourcing (human, financial, information, compute) and 'healthy risk culture'. The glossary defines 'insider threats' to include senior management and model self-exfiltration. The Code treats all of this as *mitigation*, though: its own list of systemic-risk *sources* (App. 1.3, 37 items) contains no organizational source. California's SB 53 (Sep 2025) also makes internal governance a published-framework obligation, at far lower granularity."
- *Confidence: high on the text. Medium that "most granular" survives a full survey. SB 53 belongs to the US verifier's lane; I only read the provisions quoted.*

### 2.2 §1 Source documents table

- **EU-CoP row**
  - Current: link to artificialintelligenceact.eu, tag P.
  - Source: that site is run by the **Future of Life Institute** ("This resource is provided by the Future of Life Institute and is not associated with the European Union"). FLI also appears in this report as a rater (FLI Safety Index).
  - Proposed link: the Commission's official PDF, https://ec.europa.eu/newsroom/dae/redirection/document/118119 (landing page https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai). Date "10 Jul 2025". Tag P.
  - *High.*
- **EU-Act row**
  - "OJ 12 Jul 2024; in force 1 Aug 2024" is correct: OJ L 2024/1689 of 12.7.2024; Art. 113, "twentieth day following that of its publication".
  - Proposed addition: "GPAI obligations apply from 2 Aug 2025; Commission fining powers from 2 Aug 2026 (Art. 113(b), Art. 101). Amended by Reg. (EU) 2026/1744 (Digital Omnibus on AI, in force 27 Jul 2026 [S]; the GPAI chapter is reportedly unchanged [S])."
  - *High on dates. Low/secondary on the Omnibus.*
- **CSET-CoP row**
  - Current: "Dec 19, 2025 | CSET-CoP | CSET, 'AI Safety under the EU AI Code of Practice'".
  - Source: the page byline reads "Mia Hoffmann · July 30, 2025", and the full title is "AI Safety under the EU AI Code of Practice — A New Global Standard?"
  - Proposed: "Jul 30, 2025 | CSET-CoP | Hoffmann (CSET blog), 'AI Safety under the EU AI Code of Practice — A New Global Standard?'". Move the row accordingly.
  - *High.*
- **CSET row (Jul 2021, tag U)**
  - Now verified. Arnold & Toner, *AI Accidents: An Emerging Threat*, CSET Policy Brief, July 2021, DOI 10.51593/20200072 (the DOI is in the relata entry another agent created).
  - Proposed tag: P.
- **Hacker row:** see §2.8.

### 2.3 §2(a) crosswalk, EU-CoP column

Verified cells I agree with:
- A1–A4 are **E** (App. 1.4(1)–(4), p.37).
- A5 **E**: App. 1.1, "illegal, violent, hateful, radicalising, or false content, including risks from child sexual abuse material (CSAM) and non-consensual intimate images (NCII)". Fraud and deepfakes are not named.
- A6 **E**: App. 1.3.2(4) "tendency to 'hallucinate'…", (6) "lack of performance reliability"; App. 1.1 "risks of major accidents".
- A7 **E**: App. 1.1 "critical sectors or infrastructure"; App. 1.4(3); Measure 9.3(1).
- A9 **E**: App. 1.1 "concentration of power".
- A12 **E**: App. 1.1 "privacy and the protection of personal data".
- A14 **E**: App. 1.1 "non-discrimination"; 1.3.2(5) "discriminatory bias".
- A15 **E**: App. 1.1 "the environment".
- A17 **E**: App. 1.3.2(9) "'colluding' with other AI models/systems", (10) "mis-coordination or conflict", 1.3.3(12) "interactions with other AI models and/or AI systems".
- A10 and A16 "—" are correct: there is no "military", "divide" or equivalent anywhere in the chapter.

Changes:

| Cell | Current | Source | Proposed | Conf. |
| --- | --- | --- | --- | --- |
| A8 Labour market | P | The chapter has no labour/labor/employ/job content. The only economic item is App. 1.1 "economic security" (p.34). | **—** (or P with a note: "'economic security' only; not labour-market") | high |
| A11 Autonomy/over-reliance/psych harm | E✓ | App. 1.1 "public mental health" (p.34); Measure 9.3(4) "serious harm to a person's health (mental and/or physical)" (p.27). Nothing on over-reliance, dependence or skill erosion. | **E** for psychological harm only. Footnote: "over-reliance/autonomy not addressed" | high |
| A13 IP | P | 0 hits for copyright/intellectual in the Safety & Security chapter. Copyright is handled by the Code's *separate* Copyright chapter as a compliance duty (Art. 53(1)(c)), not as a systemic risk. | **—** for the Safety & Security chapter. Optional note: "Copyright chapter treats it as compliance, not systemic risk" | high |
| A18 AI welfare | P✓ | App. 1.1 lists "non-human welfare" among examples of risks the model may pose (p.34). The Code does not define it. Secondary commentary reads it as animals (e.g. EA Forum, "Addressing the nonhuman gap in intergovernmental AI governance frameworks": "Animals were included in the voluntary Code of Practice … which refers to risks to 'non-human welfare'…" [S/W, not verified further]). As a risk *to* welfare caused *by* the model, it is structurally not about the model's own moral status. | **—**, with a footnote: "'non-human welfare' (App. 1.1) is undefined; read as animal welfare in commentary; not AI moral status." This also resolves the §6 inconsistency: §6 already lists AI welfare as single-source (MIT). | high on the text; medium on the reading |

### 2.4 The CSET column: which document is it?

The column's values (A3 P, A6 E, A7 P, the rest "—") match **CSET-2021 (Arnold & Toner)**, not CSET-2025. CSET-2025 restates the Code's four specified risks and would score A1–A4 E. The report never says which document the column holds. Since the §1 table lists both, I'd make it explicit.

**Rating CSET-2021 against the text:**

- **A6 E ✓.** p.6: "three basic types of AI failures—robustness failures, specification failures, and assurance failures".
- **A3 P → D, with a definitional flag.** p.6: "Failures of assurance: the system cannot be adequately monitored or controlled during operation." p.15: "An AI system might even actively resist being controlled, whether by design or as a strategy 'learned' by the system itself during training." This is a named category, but at the scale of deployed-system accidents (an autopilot scenario), not frontier loss of control. See §4.2; pooling this with EU-CoP A3 is exactly the problem Joseph described.
- **A7 P → D.** Hospital routing, driverless taxis and missile defence scenarios (pp.7–15). p.3: "critical, real-world systems, from cars and planes to financial markets, power plants, hospitals, and weapons platforms".
- **A10 — → P.** "Phantom missile launches" scenario (p.7–8). It is an accident in a military system, not strategic instability as such.
- **A11 — → E.** Named risk factor, p.17: "**Untrained or distracted users.** … Untrained users may trust the system too much". Also p.14: "many come to trust them implicitly … they stop carefully monitoring the systems".
- **A14 — → P.** p.4: "unexpected racial and gender discrimination by machine learning software"; p.16: biased hospital algorithm.
- **§2(c) C1: add CSET-2021 as E.** p.16: "**Competitive pressure.** When not using AI could mean falling behind competitors or losing profits, companies, militaries, and governments are more likely to deploy buggy AI systems, use them in reckless ways, or cut corners on testing and operator training." This is one of the earliest explicit statements of the C1 mechanism in the report's corpus.
- **§2(c) C12: add CSET-2021 as E.** p.17: "**System complexity.** … 'ripple effects' throughout the system" and "**Systems with many instances.** When a single AI model is used in many different real-world settings at once, a single error can create havoc on a much larger scale."
- Also named but not in the report's taxonomy: "Systems that operate too quickly for human intervention" (p.17).

*Confidence: high. I read the whole brief.*

CSET-2021 is also a better anchor than CSET-2025 for C6/C9. It is primary and older, whereas CSET-2025 is only a secondary restatement of the Code.

### 2.5 §2(b) Drivers table, EU-CoP pinpoints

| Row | Current | Check | Proposed | Conf. |
| --- | --- | --- | --- | --- |
| B1 | "EU-CoP App. 1.3.1 (14 items)" | Correct. Items include (5) operate autonomously, (7) long-horizon planning, (8) self-reasoning, (10) self-replicate/self-improve, (11) automate AI R&D, (13) tool use incl. computer use, (14) control physical systems (p.35). | keep | high |
| B2 | "EU-CoP App. 1.3.2 (10 items)" | Correct (p.36). Note that "deception" and "sandbagging" in the row label are not App. 1.3.2 items. Deception is a *capability* (1.3.1(4)) and a glossary term. Sandbagging appears in App. 3.2(2) as "model deception during model evaluations (e.g. sandbagging)". | keep; optionally add "glossary 'deception'; App. 3.2(2)" | high |
| B3 | "EU-CoP App. 1.3.3(4)" | Correct: "level of human oversight (e.g. degree of model autonomy)" | keep | high |
| B5 | "EU-CoP App. 3 (resourcing, time)" | App. 3 also covers under-elicitation and test-awareness directly. App. 3.2 (p.39): "minimise the risk of under-elicitation; and (2) minimise the risk of model deception during model evaluations (e.g. sandbagging)". App. 1.3.1(8): "its ability to know if it is being evaluated". Glossary "deception": "a model's detecting that it is being evaluated and under-performing or otherwise undermining oversight". Measure 4.1 safety margin: "under-elicitation of model evaluations". | "EU-CoP App. 1.3.1(8); App. 3.2 (under-elicitation, sandbagging); App. 3.4 (resourcing, time); glossary 'deception'". EU-CoP is then a primary source for all three sub-items, not just resourcing. | high |
| B6 | "EU-CoP App. 1.3.3(5)" | Correct: "vulnerability to adversarial removal of guardrails". Also Measure 5.1 "sufficiently robust under adversarial pressure (e.g. fine-tuning attacks or jailbreaking)". | keep; optionally add Measure 5.1 | high |
| B7 | "EU-CoP Commitment 6, App. 1.3.3(6–7)" | Correct (p.18, p.36) | keep | high |
| B8 | "EU-CoP glossary and App. 4.4" | Correct. Glossary (p.30): "'insider threats' hostile operations by humans, AI models, and/or AI systems (e.g. senior management, a senior member of the organisation's research team, other disgruntled employees, perpetrators of industrial espionage operations that have infiltrated their target, and/or model self-exfiltration) with access to sensitive organisational resources, and/or accidental model leakage." Also Measure 6.1: the Security Goal must include "insider threats". | keep | high |
| B9 | "EU-CoP Commitment 6 exemption" | The exemption is a *scope rule* that references open weights; it does not name proliferation as a risk. The Code's risk-source hook is App. 1.3.3(3) "release and distribution strategies". AI Act recital 112 flags open-source release: "after the open-source model release, necessary measures to ensure compliance … may be more difficult to implement." | "EU-CoP App. 1.3.3(3) (release strategy as risk source); Commitment 6 open-weight exemption (scope); AI Act recital 112" | high |
| B10 | "EU-CoP App. 1.2.2(2–3), 1.3.3(2, 8)" | 1.2.2(3) is "High velocity: **The risk** can materialise rapidly, potentially outpacing mitigations." That is the speed of risk materialisation, not deployment velocity. 1.2.2(2) reach-dependent ✓; 1.3.3(2) scalability ✓; 1.3.3(8) user numbers ✓. | "EU-CoP App. 1.2.2(2), 1.3.3(2, 3, 8)". If "velocity" is kept, cite 1.2.2(3) separately as "risk materialisation speed". | high |
| B12 | "EU-CoP App. 1.3.3(9)" | Correct: "offence-defence balance, including the potential number, capacity, and motivation of malicious actors to misuse the model" | keep | high |
| B13 | "EU-CoP App. 1.3.3(11)" | 1.3.3(11) is "lack of appropriate model explainability or transparency", i.e. model opacity. It covers *information asymmetry* (developer vs public/regulator) only loosely. | keep for "opacity"; the asymmetry sub-item needs another source | high |

### 2.6 §2(c) Structural/organizational table, EU-CoP pinpoints

- **C1:** add CSET-2021 (E, quoted in §2.4). CSET-2025 is a secondary echo: "It is easy to see how commercial interests might get in the way of caution."
- **C5, "EU-CoP Chairs":** fine as a pointer. Note that the Chairs' text is about the *regulator's* capacity (see §2.7).
- **C6, "EU-CoP Measure 8.3; CSET":**
  - The Measure 8.3 pinpoint is correct.
  - Relabel as mitigation (§1).
  - The CSET quote in fn 24 is verified: "providers are also expected to foster a healthy risk culture in the organization, for example by periodically informing employees about the whistleblower protection policy…" (CSET-2025).
  - Consider CSET-2021 "competitive pressure" as the primary *factor* source instead.
- **C7, "EU-CoP Measure 8.1":** correct pinpoint; it is a mitigation.
- **C8, "EU-CoP Measure 8.2 … and App. 3":** correct. App. 3.4(4) lists "(b) adequate staffing".
- **C9, "EU-CoP Measure 8.3(4–6)":** should be **8.3(4)–(7)**. Item (7) is the non-retaliation item and is the most on-point: "not retaliating in any form … against any person publishing or providing information … to competent authorities about systemic risks". Recital (d) also ties Measure 8.3 to the Whistleblower Directive (EU) 2019/1937. *High.*
- **C12, "EU-CoP App. 1.2.2(4–6)":**
  - Only 1.2.2(4) "Compounding or cascading: The risk can trigger other systemic risks or chain reactions" fits.
  - (5) is irreversibility and (6) is asymmetric impact; neither is about correlated failure.
  - Add App. 1.3.3(12) "interactions with other AI models and/or AI systems".
  - Add AI Act recital 110: "risk that a particular event could lead to a chain reaction with considerable negative effects that could affect up to an entire city, an entire domain activity or an entire community".
  - Add Hacker et al. "multi-model systemic risks" (§4, p.5): "correlated failures when multiple models fail in synchronized, or connected, ways".
  - Add CSET-2021 ("systems with many instances").
  - *High.*
- **C13, "EU-CoP Precautionary Principle recital":** pinpoint is **recital (g)**, p.4: "particularly for systemic risks for which the lack or quality of scientific data does not yet permit a complete assessment. Accordingly … the extrapolation of current adoption rates and research and development trajectories of models should be taken into account". This is a fair analogue of the evidence dilemma. *High.*

### 2.7 §3 "EU AI Act and Code: definitions and the mandatory floor (verified)"

**Heading.**
- Proposed: "EU AI Act and Code: definitions, obligations and signatory commitments".
- The word "verified" was only partly earned in the original (Annex XIII was marked "not text-verified"). Everything below now is verified.

**Bullet "AI Act definitions".**
- **Current:** "Art. 3(64) defines 'high-impact capabilities' and Art. 3(65) defines 'systemic risk.' Art. 51 and Annex XIII set the 10^25 FLOP presumption; Art. 55 sets obligations. (Annex XIII detail not text-verified.)"
- **Source:**
  - Art. 51(2), p.83: "A general-purpose AI model shall be presumed to have high impact capabilities pursuant to paragraph 1, point (a), when the cumulative amount of computation used for its training measured in floating point operations is greater than 10^25."
  - Annex XIII, p.144, is the list of criteria for Commission *designation* under Art. 51(1)(b): "(a) the number of parameters … (c) the amount of computation used for training … (e) … its level of autonomy and scalability, the tools it has access to; (f) whether it has a high impact on the internal market due to its reach, which shall be presumed when it has been made available to at least 10 000 registered business users established in the Union; (g) the number of registered end-users."
- **Proposed:** "Art. 3(64) defines 'high-impact capabilities' ('capabilities that match or exceed the capabilities recorded in the most advanced general-purpose AI models'). Art. 3(65) defines 'systemic risk'. Art. 51(2) presumes high-impact capabilities above 10^25 training FLOP. Annex XIII lists the criteria for Commission designation (parameters, data, compute, modalities, benchmarks/autonomy/tools, reach — presumed at ≥10,000 registered EU business users — and end-users). Art. 55(1) sets four obligations: evaluation incl. adversarial testing; assess and mitigate systemic risks 'including their sources'; serious-incident reporting; cybersecurity."
- *High.*

**Bullet "Types and nature of risk".** Correct as written (App. 1.1, p.34; App. 1.2.2, p.35). Keep, noting that App. 1.1's items are *examples*.

**Bullet "Sources of risk".** Correct. Add "non-exhaustive, potential".

**Bullet "The mandatory floor".**
- Proposed: "**The specified risks.** App. 1.4 lists four specified systemic risks that signatories must always identify (Measure 2.1(2)) and must manage with capability-defined risk tiers (Measure 4.1(1)): CBRN, loss of control, cyber offence and harmful manipulation."
- Put the App. 1.4 definitions inline, since they are the Code's operational meaning of each hazard. Verbatim text is in §4.1.

**Bullet "Measure 8.1 requires…".**
- **Current:** "requires that the executive-level systemic-risk support role 'must not also be responsible for the Signatory's core business activities' such as research and product."
- **Source,** p.24, inside the presumption paragraph: "(3) Systemic risk support and monitoring: The responsibility … has been assigned to at least one member of the management body in its executive function (e.g. a Chief Risk Officer or a Vice President, Safety & Security Framework). This member(s) must not also be responsible for the Signatory's core business activities that may produce systemic risk (e.g. research and product development)." Contrast item (2): "Systemic risk ownership … assigned to suitable members of the management body in its executive function **who are also responsible for** relevant Signatory core business activities that may give rise to systemic risk, such as research and product development (e.g. Head of Research or Head of Product)."
- **Proposed:** "Measure 8.1's safe-harbour structure (the Measure 'is presumed to be fulfilled' if followed) separates duties. Risk *ownership* sits with the executives who run research and product. Risk *support and monitoring* sits with at least one executive (e.g. a CRO) who 'must not also be responsible for the Signatory's core business activities that may produce systemic risk'. Assurance reports to the board. Responsibilities are allocated 'as suitable for the Signatories' governance structure and organisational complexity'."
- The last clause is the only place the Code names organisational complexity, and it matters for C15.
- *High.*

**Bullet "Measure 8.3".** Accurate. Add that these are "Examples of indicators", listed with "and/or". Item (3), verbatim: "setting incentives and affording sufficient independence of staff involved in systemic risk assessment and mitigation to discourage excessive systemic-risk-taking and encourage an unbiased assessment". Also add (7), non-retaliation.

**Bullet "Reassessment trigger (Measure 1.3)".**
- **Current:** "Signatories reassess their Framework when there are reasonable grounds to believe its adequacy or adherence will be materially undermined. Examples include material change in how models are developed, serious incidents or near misses, and materially changed risks. Otherwise reassessment happens every 12 months."
- **Source,** p.9: "Signatories will conduct an appropriate Framework assessment, if they have reasonable grounds to believe that the adequacy of their Framework and/or their adherence thereto has been or will be materially undermined, or every 12 months starting from their placing of the model on the market, whichever is sooner. Examples of such grounds are: (1) how the Signatories develop models will change materially, **which can be reasonably foreseen to lead to the systemic risks stemming from at least one of their models not being acceptable**; (2) serious incidents and/or near misses involving their models or similar models that are likely to indicate that the systemic risks … are not acceptable have occurred; and/or (3) the systemic risks … have changed or are likely to change materially…"
- **Proposed:** keep the text, but add the foreseeability condition to example (1), and replace "Otherwise" with "and in any case at least every 12 months ('whichever is sooner')".
- *High.*

**Bullet "Security (Commitment 6)".**
- **Current:** "Exempts models weaker than at least one open-weight model. The security goal must cover insider threats. App. 4.3(4) limits the number of people with non-hardened interface access to parameters."
- **Source:** p.18: "A model is exempt from this Commitment if the model's capabilities are inferior to the capabilities of at least one model for which the parameters are publicly available for download." Measure 6.1: "including non-state external threats, insider threats, and other expected threat actors". App. 4.3(4) is quoted in §1.
- **Proposed:** "…App. 4.3(4) lists 'limiting the number of people who have non-hardened interface-access to model parameters' as the default measure for reducing insider-threat and compromised-account risk. No number is set, and equivalent alternatives are allowed (Measure 6.2). App. 4.3(1) also requires access authorisations to be 'checked on a regular basis of at least every six months'. App. 4.4(1) requires background checks on employees and contractors who 'have or might reasonably obtain read or write access to unreleased model parameters'. App. 4.5(4) requires 'periodic personnel integrity testing'."
- Those last three are exactly where headcount growth bites, operationally.
- *High.*

**Bullet "Incident reporting (Measure 9.3)".**
- Numbers are correct. Tighten wording: the 2-day deadline is for "a serious and **irreversible** disruption of the management or operation of critical infrastructure". These deadlines are for the *initial* report. Intermediate reports follow at least every four weeks; the final report is due within 60 days of resolution (p.26–27).
- The GPAI Guidelines ¶103 (p.28) confirm that the AI Office treats "(self-)exfiltration of model parameters and cyberattacks" as serious incidents under the Act itself.
- *High.*

**Bullet "Regulator capacity".**
- **Source** (the Chairs' statement, on code-of-practice.ai p.3 and artificialintelligenceact.eu): "On quantity, we share the view recently put forward by a group of AI experts that the AI Safety unit (DG CNECT A3) should be scaled up to 100 staff, with the full implementation team of the AI Act expanding to 200." The "group of AI experts" hyperlink points to https://thefuturesociety.org/wp-content/uploads/2025/06/ProtectingGPAIRules.pdf (not fetched).
- **Proposed:** "The Chairs, in a statement published with the Code but not part of it, endorsed an expert proposal to scale the AI Office's AI Safety unit (DG CNECT A3) to 100 staff and the AI Act implementation team to 200."
- *High.*
- **Worth Joseph's attention for the AISI EOI (adjacent).** The same statement holds UK AISI up as the model for regulator recruitment: "The United Kingdom's AI Security Institute (AISI) – which does not even have regulation to enforce – showed how this can be done. With an in-house, head-hunting team that proactively approaches leading talent …, significantly higher-than-usual government pay for technical talent, and a dramatically sped-up recruitment process, UK AISI has been able to recruit world-leading technical experts from places like OpenAI, Anthropic, and Google DeepMind."
- It also makes a regulator-side absorptive-capacity observation that directly supports Recommendation 4: "the AI Office employs exceptional staff. But they are not many, and the expectations and incentives they face in the Office are such that they constantly have to meet urgent deadlines. This means that it is nobody's job to scan what is happening at the frontier of AI development".

### 2.8 §5 "Where organizations disagree"

**§5.1, first sub-bullet.**
- **Current:** "The EU uses a legal definition tied to high-impact capabilities and EU-market reach."
- **Source,** Art. 3(65): "'systemic risk' means a risk that is specific to the high-impact capabilities of general-purpose AI models, having a significant impact on the Union market due to their reach, **or** due to actual or reasonably foreseeable negative effects on public health, safety, public security, fundamental rights, or the society as a whole, that can be propagated at scale across the value chain".
- **Proposed:** "The AI Act ties systemic risk to (i) high-impact (frontier) capabilities, (ii) significant Union-market impact, via reach *or* via negative effects on health, safety, security, fundamental rights or society, and (iii) propagation at scale across the value chain (Art. 3(65))."
- *High.*

**§5.1, Hacker sub-bullet.**
- **Current:** "Hacker et al. argue the AI Act concept is too narrow and would miss 'discrimination at scale, and large-scale hallucinations.'"
- **Source (v2 = FAccT '26):**
  - The report's quote is verbatim from the v2 abstract (p.1): "Our framework identifies systemic risks overlooked by the DSA and AI Act — including multi-agent interactions, discrimination at scale, and large-scale hallucinations".
  - The arXiv abstract hedges: "may not fall under current legal definitions".
  - On their own close reading of the Act, they conclude: discrimination at scale **does** qualify (§8.1, p.13: "we conclude that large-scale discrimination does count as systemic risk"); hallucinations have "a narrow road to the recognition of hallucination under the systemic risk framework, at best" (§8.2, p.14); environmental harms qualify (§8.3, p.15).
  - Their core critiques are the "most advanced models" restriction (the "moving target problem", p.9) and the "Union market" restriction (§6.3.3). They also argue "The DSA … actually does a better job at identifying systemic risk than the more recent AI Act."
- **Proposed:** "Hacker, Edwards & Kasirzadeh (FAccT 2026) argue that the Act's definition is too narrow because it is tied to 'the most advanced' models and to 'Union market' impact, and that the DSA's enumerative approach does better. They flag multi-agent interactions, discrimination at scale and large-scale hallucinations as risks the definitions may miss. Their own legal analysis concludes that large-scale discrimination still qualifies, while hallucinations do so only on 'a narrow road … at best'."
- *High.*

**§5.2, "Loss of control. Mandatory in the EU Code".** Replace "Mandatory" with "a specified systemic risk" (see §1). The definitional divergence belongs here; see §4.2.

**§5.3, "Manipulation. Mandatory in the EU Code".** Same fix. Also note the AI Act *prohibits* manipulative AI systems in Art. 5(1)(a), a different, individual-scale notion (§4.3).

**§5.6, "Open weights".**
- **Current:** "The EU Code exempts models weaker than the best open-weight model from Commitment 6. That resets the security baseline in a way RAND's actor-based threat model does not."
- **Source:** The exemption text is in §2.7. The Code is itself actor-based. Measure 6.1: the "Security Goal … specifies the threat actors that their security mitigations are intended to protect against". The glossary (p.31) sizes one class: "'non-state external threats' hostile operations conducted by non-state actors that: (1) are roughly comparable to ten experienced, professional individuals in cybersecurity; (2) spend several months with a total budget of up to EUR 1 million on the specific operation; and (3) have major pre-existing cyberattack infrastructure but no pre-existing access to the target organisation."
- **Proposed:** "The Code's security commitment is actor-based like RAND's: its Security Goal must name threat actors, and it sizes the minimum 'non-state external threat' at roughly ten professionals, several months and ≤EUR 1M. But it switches off entirely for any model whose capabilities are inferior to those of at least one open-weight model. RAND's model has no such relative exemption [RAND side: the RAND verifier's call]."
- A possible cross-walk for the RAND verifier: the Code's sized actor resembles one of RAND's operational-capacity (OC) tiers. That is my impression, not something I checked.
- *High on the Code side.*

### 2.9 §6 Single-source items, §7 priorities, Recommendations

**§6.**
- **Current:** "'Lawlessness' and 'non-human welfare' (EU-CoP)".
  - Lawlessness is correct and defined in App. 1.3.2(7): "lawlessness, i.e. acting without reasonable regard to legal duties that would be imposed on similarly situated persons, or without reasonable regard to the legally protected interests of affected persons".
  - For non-human welfare, see A18: it is undefined.
  - *High.*
- **Current:** "Two sources: Multi-agent collusion (EU-CoP, MIT; GDM 'structural')".
  - That entry lists three sources, and with Hacker et al. there are four: v2 abstract, "the possibility of systemic failures arising from the interaction of multiple AI agents"; §4 "multi-model systemic risks".
  - Move it to "three or more".
  - *High.*

**§7, EU row.**
- **Current:** "EU AI Office | CBRN, loss of control, cyber offence, harmful manipulation (mandatory)".
- **Proposed:** "EU (Code of Practice; drafted by independent Chairs, assessed adequate by the Commission and AI Board) | CBRN, loss of control, cyber offence, harmful manipulation (specified risks signatories must always assess)".
- The AI Office did not itself issue a ranking. App. 1.4 says the list takes "into account international approaches pursuant to Article 56(1) and recital 110 AI Act".
- *High.*

**Recommendation 1, anchors.**
- "EU-CoP Commitment 8 and App. 4.3–4.4" are fine as anchors *for mitigations*.
- Add that the Code's App. 1.3 contains no organizational risk source. That absence is the cleanest documentary support for the gap the paper claims.
- Add the Measure 8.1 "organisational complexity" clause.
- *High.*

**Recommendation 2, indicators.**
- "Year-on-year growth in privileged-access headcount (EU-CoP App. 4.3(4); RAND SL3)". App. 4.3(4) is narrower: it covers "non-hardened interface-access to model parameters". The adjacent scope is App. 4.4(1): staff who "have or might reasonably obtain read or write access to unreleased model parameters or systems that manage the access".
  - Proposed: "growth in headcount with (non-hardened) access to unreleased parameters (EU-CoP App. 4.3(4), 4.4(1)); churn in the six-monthly access re-authorisation (App. 4.3(1))".
- "Tenure of risk-owning staff (Measure 8.1)". Measure 8.1 says nothing about tenure; this is the paper's own proposed indicator, anchored to 8.1's role structure. Mark it as proposal.
- "Trends in anonymous-survey indicators (Measure 8.3)": fine, noting it is an *example* indicator (8.3(4)).
- *High.*

**Recommendation 3, the regulatory hook.**
- **Current:** "Use Measure 1.3 as the regulatory hook. A material change in how models are developed includes rapid organizational change, which is a reasonable-grounds trigger for Framework reassessment."
- **Assessment:**
  - Example (1) is about "how the Signatories develop models". The natural reading covers methods, architectures and AI-automated R&D, which is the same family as Measure 7.5's "novel architectures", "training techniques". Whether organizational change counts is an argument, not a reading.
  - Example (1) is also conditional on it being "reasonably foreseen to lead to the systemic risks … not being acceptable".
  - The stronger hook is the Measure's **headline trigger**: "reasonable grounds to believe that … their adherence thereto has been or will be materially undermined". Rapid growth plausibly threatens *adherence*: role dilution under Measure 8.1, access-control churn under App. 4.3/4.4, culture indicators under Measure 8.3.
  - The **Framework adherence assessment** then *requires* remediation planning (p.10): "(2) Framework adherence: An assessment focused on the Signatories' adherence to the Framework, including: (a) any instances of, and reasons for, non-adherence … and (b) any measures … that need to be implemented to ensure continued adherence to the Framework. If point(s) (a) and/or (b) give rise to risks of future non-adherence, Signatories will make remediation plans as part of their Framework assessment."
  - A secondary hook: Measure 7.2(2) requires Model Reports to state "the reasonably foreseeable conditions under which the justification … would no longer hold". A growth-rate condition could be one of them, and its materialisation triggers a Model Report update under Measure 7.6(1).
- **Proposed:** "Use Measure 1.3's adherence prong as the hook. Rapid organizational growth can give 'reasonable grounds to believe that … adherence [to the Framework] … will be materially undermined'. That triggers a Framework assessment, which must include remediation plans for 'risks of future non-adherence'. A growth condition could also be named among the Model Report's 'reasonably foreseeable conditions under which the justification … would no longer hold' (Measure 7.2(2)), which would feed Measure 7.6's update trigger. Example ground (1), material change in 'how the Signatories develop models', is a weaker fit, because it is aimed at development methods and conditional on foreseeable unacceptability."
- *Confidence: high on the text. Medium on which argument would persuade the AI Office; that is interpretation.*

**Recommendation 4.**
- Accurate in substance. Replace with the precise figures (100 in DG CNECT A3; 200 in total).
- Add the Chairs' own absorptive-capacity observation quoted in §2.7. It makes the regulator–developer analogy the Chairs' *own* reasoning, not merely an extension.
- *High.*

### 2.10 Footnotes owned by this lane

**fn 1**

> \[P] Regulation (EU) 2024/1689 (Artificial Intelligence Act), OJ L, 2024/1689, 12.7.2024. ELI: http://data.europa.eu/eli/reg/2024/1689/oj (EUR-Lex: https://eur-lex.europa.eu/eli/reg/2024/1689/oj). Relata: `eu-2024-ai-act`.
>
> Art. 3(65), p.50: "'systemic risk' means a risk that is specific to the high-impact capabilities of general-purpose AI models, having a significant impact on the Union market due to their reach, or due to actual or reasonably foreseeable negative effects on public health, safety, public security, fundamental rights, or the society as a whole, that can be propagated at scale across the value chain".
>
> Art. 51(2), p.83: presumption above 10^25 FLOP. Annex XIII, p.144: designation criteria. Art. 113, p.123: in force on the 20th day after publication; Chapter V applies from 2 Aug 2025, except Art. 101.
>
> Amended by Reg. (EU) 2026/1744 (Digital Omnibus on AI), in force 27 Jul 2026 [S: FLI AI Act Explorer summary; OJ text not retrieved].

The ELI link is correct. EUR-Lex serves a bot challenge to scripts, so it could not be machine-checked. I retrieved the same OJ PDF via publications.europa.eu/resource/celex/32024R1689.

**fn 2**

> \[P] General-Purpose AI Code of Practice, Safety and Security Chapter, published 10 Jul 2025. European Commission official PDF: https://ec.europa.eu/newsroom/dae/redirection/document/118119 (landing page https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai). Relata: `eu-cop-2025-safety-security`. Pages refer to the official 43-page PDF.
>
> Measure 8.1 (p.24): "This member(s) must not also be responsible for the Signatory's core business activities that may produce systemic risk (e.g. research and product development)."

The mirror (marinacastellaneta.it) is word-for-word identical in substance. I checked with a word-level diff: only hyphenation and pagination differ.

**fn 3**

> \[P, unofficial host] "Statement from the Chairs and Vice-Chairs", published with the final Code, Jul 2025. Hosted at https://code-of-practice.ai/?section=safety-security and https://artificialintelligenceact.eu/ai-act-explorer/cop-safety/ (FLI). Relata: `eu-cop-chairs-2025-statement` (browser print; statement on pp.2–3).
>
> "we share the view recently put forward by a group of AI experts that the AI Safety unit (DG CNECT A3) should be scaled up to 100 staff, with the full implementation team of the AI Act expanding to 200."

I found no copy of the statement on a Commission site.

**fn 24** (retitle and re-date)

> \[S] Hoffmann, M., "AI Safety under the EU AI Code of Practice — A New Global Standard?", CSET blog, 30 Jul 2025. https://cset.georgetown.edu/article/eu-ai-code-safety/. Relata: `hoffmann-2025-eu-code-safety` (created by another agent).
>
> "providers are also expected to foster a healthy risk culture in the organization, for example by periodically informing employees about the whistleblower protection policy, allowing internal challenges of decisions concerning systemic risk management, and committing to not retaliating against employees who disclose concerns about systemic risks to oversight authorities."
>
> Caution: the piece says the Code offers a "presumption of conformity". The Commission's GPAI Guidelines ¶100 say the opposite.

**fn 29**

> \[P] Hacker, P., Edwards, L., & Kasirzadeh, A. (2026). "AI, Digital Platforms, and the New Systemic Risk." FAccT '26, 25–28 June 2026, Montréal. https://doi.org/10.1145/3805689.3806506. Preprint arXiv 2509.17878 (v1 22 Sep 2025; v2 23 May 2026 = FAccT version). Relata: `hacker-2026-digital` (the arXiv v2 PDF is attached to the published-version entry; `relata audit` may flag the version mismatch).
>
> Abstract (v2): "Our framework identifies systemic risks overlooked by the DSA and AI Act — including multi-agent interactions, discrimination at scale, and large-scale hallucinations — which can destabilize institutions despite falling outside current definitions."
>
> §8.1, p.13: "we conclude that large-scale discrimination does count as systemic risk".
>
> Also note: §6.2 says Code signatories "benefit from a presumption of conformity", which contradicts GPAI Guidelines ¶100.

**fn 23** (CSET-2021)

> \[P] Arnold, Z. & Toner, H., *AI Accidents: An Emerging Threat*, CSET Policy Brief, Jul 2021, doi:10.51593/20200072. Relata: `arnold-2021-ai-accidents`.
>
> p.16: "Competitive pressure. When not using AI could mean falling behind competitors or losing profits, companies, militaries, and governments are more likely to deploy buggy AI systems, use them in reckless ways, or cut corners on testing and operator training."

---

## 3. Framing issues (beyond details)

### 3.1 The Code regulates the organization but never names it as a risk source

This is the most useful finding for Joseph's positioning, and it is stronger than what the report says.

The Code defines a "systemic risk source" as "a factor which alone or in combination with other factors might give rise to systemic risk" (glossary, p.33). It then enumerates sources in App. 1.3 exclusively as *model* capabilities, *model* propensities, and *model* affordances and deployment context. It regulates the developer's organization heavily, in Commitment 8 and App. 4.4–4.5, but only under the heading of "governance mitigations".

So the organization appears only as a lever, never as something that can itself raise risk. This is a structural feature of the instrument, not a gap in coverage that more reading might close.

"None models growth rate" is true. The deeper point is that the Code has no *category* in which organizational dynamics could be listed as a factor. The closest openings are:
- the non-exhaustiveness of App. 1.3;
- 1.3.3(7) "lack of appropriate infrastructure security";
- Measure 8.1's "organisational complexity".

*Confidence: high on the text. The inference ("no category") is mine and marked as such.*

### 3.2 Two secondaries on which the report leans share one legal error

CSET-2025 and Hacker et al. both describe Code adherence as giving a "presumption of conformity". The Commission's Guidelines ¶100 reserve that for harmonised standards. This is probably the origin of the report's "mandates / mandatory floor" framing. It is worth one line in the Caveats.

### 3.3 The host of the report's Code link is an interested party

artificialintelligenceact.eu is run by FLI, whose AI Safety Index the report also cites as a rater. The content I checked there (the Chairs' statement) matches code-of-practice.ai verbatim, so this is a provenance note, not an accuracy problem.

### 3.4 Timing

The report calls §3 "the mandatory floor" without dates. As of Sep 2026:
- Art. 55 has applied for over a year.
- Fines have been possible since 2 Aug 2026.
- Models placed on the market before 2 Aug 2025 have until **2 Aug 2027** (Art. 111(3); Guidelines ¶109).

For an AISI EOI written now, "live enforcement since last month" is a materially different posture from "a code published last summer".

---

## 4. Definitions record (raw, verbatim; not reconciled)

### 4.1 EU instruments

**AI Act (Reg. 2024/1689; `eu-2024-ai-act`)**

- **Art. 3(2), p.46.** "'risk' means the combination of the probability of an occurrence of harm and the severity of that harm".
- **Art. 3(49), p.49.** "'serious incident' means an incident or malfunctioning of an AI system that directly or indirectly leads to any of the following: (a) the death of a person, or serious harm to a person's health; (b) a serious and irreversible disruption of the management or operation of critical infrastructure; (c) the infringement of obligations under Union law intended to protect fundamental rights; (d) serious harm to property or the environment".
  - The GPAI Guidelines ¶103 extend this to GPAI *models*, and treat "(self-)exfiltration of model parameters and cyberattacks" as covered.
- **Art. 3(63), p.50.** "'general-purpose AI model' means an AI model, including where such an AI model is trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks …"
  - The GPAI Guidelines add an indicative criterion of 10^23 FLOP.
- **Art. 3(64).** "'high-impact capabilities' means capabilities that match or exceed the capabilities recorded in the most advanced general-purpose AI models".
  - Guidelines ¶38, p.14: "the Commission does not consider it to refer to a fixed level of capabilities".
- **Art. 3(65).** Systemic risk: quoted in §2.10, fn 1.
- **Recital 110, p.28–29. The Act's closest language to loss of control and misalignment.** Note that it says "issues of control relating to alignment", not "loss of control".
  - "Systemic risks should be understood to increase with model capabilities and model reach, can arise along the entire lifecycle of the model, and are influenced by conditions of misuse, model reliability, model fairness and model security, the level of autonomy of the model, its access to tools, novel or combined modalities, release and distribution strategies, the potential to remove guardrails and other factors."
  - "In particular, international approaches have so far identified the need to pay attention to risks from potential intentional misuse or unintended issues of control relating to alignment with human intent; … risks from models of making copies of themselves or 'self-replicating' or training other models; … risk that a particular event could lead to a chain reaction with considerable negative effects that could affect up to an entire city, an entire domain activity or an entire community."
- **Art. 5(1)(a), p.51. A system-level, individual-harm notion of manipulation (prohibited practice).** It is distinct from the Code's population-scale "harmful manipulation". "the placing on the market, the putting into service or the use of an AI system that deploys subliminal techniques beyond a person's consciousness or purposefully manipulative or deceptive techniques, with the objective, or the effect of materially distorting the behaviour of a person or a group of persons by appreciably impairing their ability to make an informed decision, thereby causing them to take a decision that they would not have otherwise taken in a manner that causes or is reasonably likely to cause that person, another person or group of persons significant harm".
- **Used without definition in the Act:** "misalignment" (only "alignment with human intent", recital 110), "loss of control" (absent), "manipulation" as a *systemic* risk.

**GPAI Code, Safety & Security chapter (`eu-cop-2025-safety-security`)**

- **App. 1.4(2) Loss of control, p.37.** "Risks from humans losing the ability to reliably direct, modify, or shut down a model. Such risks may emerge from misalignment with human intent or values, self-reasoning, self-replication, self-improvement, deception, resistance to goal modification, power-seeking behaviour, or autonomously creating or improving AI models or AI systems."
  - **No scale, duration or harm threshold.** Scale enters only through the systemic-risk definition: the App. 1.2.1 essential characteristics, "significant impact on the Union market", "propagated at scale".
  - "Reliably" carries most of the weight: an episodic escape arguably demonstrates the lack of *reliable* control.
- **App. 1.4(4) Harmful manipulation, p.37.** "Risks from enabling the strategic distortion of human behaviour or beliefs by targeting large populations or high-stakes decision-makers through persuasion, deception, or personalised targeting. This includes significantly enhancing capabilities for persuasion, deception, and personalised targeting, particularly through multi-turn interactions and where individuals are unaware of or cannot reasonably detect such influence. Such capabilities could undermine democratic processes and fundamental rights, including exploitation based on protected characteristics."
- **App. 1.4(1) CBRN.** "Risks from enabling chemical, biological, radiological, and nuclear (CBRN) attacks or accidents. This includes significantly lowering the barriers to entry for malicious actors, or significantly increasing the potential impact achieved, in the design, development, acquisition, release, distribution, and use of related weapons or materials."
- **App. 1.4(3) Cyber offence.** "Risks from enabling large-scale sophisticated cyber-attacks, including on critical systems (e.g. critical infrastructure). This includes significantly lowering the barriers to entry for malicious actors, or significantly increasing the potential impact achieved in offensive cyber operations, e.g. through automated vulnerability discovery, exploit generation, operational use, and attack scaling."
- **Glossary, p.29–33:**
  - **'deception':** "model behaviours that systematically produce false beliefs in others, including model behaviours to achieve goals that involve evading oversight, such as a model's detecting that it is being evaluated and under-performing or otherwise undermining oversight."
  - **'insider threats':** quoted in §2.5, row B8.
  - **'non-state external threats':** quoted in §2.8.
  - **'(self-)exfiltration of model weights':** "access or transfer of weights or associated assets of a model from their secure storage by the model itself and/or an unauthorised actor."
  - **'near miss':** "a situation in which a serious incident could have, but ultimately did not, materialise."
  - **'systemic risk source':** "a factor which alone or in combination with other factors might give rise to systemic risk."
  - **'systemic risk mitigations':** quoted in §1.
  - **'state of the art':** "the forefront of relevant research, governance, and technology that goes beyond best practice."
  - **'best practice':** "accepted amongst providers of general-purpose AI models with systemic risk as the processes, measures, methodologies, methods, and techniques that best assess and mitigate systemic risks at any given point in time."
  - **'model elicitation':** "technical work to systematically enhance a model's capabilities, propensities, affordances, and/or effects, thereby facilitating an accurate measurement of the full range of its capabilities, propensities, affordances, and/or effects that can likely be attained."
  - **'management body':** "a corporate organ appointed pursuant to national law and empowered to perform: (1) an executive function … and (2) a supervisory function by overseeing and monitoring executive decision-making."
- **App. 1.3.2(7) lawlessness:** quoted in §2.9.
- **App. 1.3.2, propensities,** "which encompass inclinations or tendencies of a model to exhibit some behaviours or patterns".
- **App. 1.2.2 contributing characteristics:** verbatim in the Code, p.35. "High velocity: The risk can materialise rapidly, potentially outpacing mitigations." "Asymmetric impact: A small number of actors or events can trigger the materialisation of the risk, causing disproportionate impact relative to the number of actors or events."
- **Used but NOT defined in the Code:**
  - "misalignment with human intent" / "with human values" (1.3.2(1)–(2); only exemplified: "e.g. disregard for fundamental rights");
  - "power-seeking" and "goal-pursuing" (in scare quotes, 1.3.2(8));
  - "colluding" (1.3.2(9));
  - "healthy risk culture" (Measure 8.3; indicators only);
  - "concentration of power" and "non-human welfare" (App. 1.1);
  - "sabotage" (App. 4.4);
  - "manipulate, persuade, or deceive" as a *capability* (1.3.1(4)); only the risk "harmful manipulation" and the behaviour "deception" are defined.

**Commission GPAI Guidelines (`ec-2025-gpai-guidelines`)**

- ¶5, p.4, paraphrase of systemic risk: "risks which, are specific to the most advanced general-purpose AI models and can have a significant impact on the Union market". This drops the Act's "due to … negative effects" alternative, a telling compression.
- ¶23: "lifecycle" begins "at the start of the large pre-training run".

**Chairs' statement (`eu-cop-chairs-2025-statement`)**

- "the core component of the AI Act's definition of systemic risk is about the risk being specific to capabilities that match or exceed the capabilities of the most advanced general-purpose AI models". The Chairs drafted "assuming only about 5-15 providers" would be in scope.

### 4.2 Loss of control: the scales in play

Joseph's illustration, put against the texts, from smallest to largest scale:

| Scale | Source | Operative words |
| --- | --- | --- |
| Operator-level, deployed system, accidental | CSET-2021 p.6, 15 | "Failures of assurance: the system cannot be adequately monitored or controlled during operation"; "An AI system might even actively resist being controlled, whether by design or as a strategy 'learned'". Example: an autopilot overriding pilots. |
| Reportable incident, no harm threshold | Code Measure 9.3(2); glossary "(self-)exfiltration" | "a serious cybersecurity breach, including the (self-)exfiltration of model weights", with a 5-day initial report |
| Incident with harm / demonstrated subversion | SB 53 "critical safety incident" (§22757.11(d)) | "(3) Loss of control of a frontier model causing death or bodily injury. (4) A frontier model that uses deceptive techniques against the frontier developer to subvert the controls or monitoring of its frontier developer outside of the context of an evaluation designed to elicit this behavior and in a manner that demonstrates materially increased catastrophic risk." |
| Risk category, scale-free (scale only via "systemic") | Code App. 1.4(2) | "humans losing the ability to reliably direct, modify, or shut down a model" |
| Risk category, alignment-framed | AI Act recital 110 | "unintended issues of control relating to alignment with human intent"; "making copies of themselves or 'self-replicating' or training other models" |
| Catastrophe-bounded | SB 53 "catastrophic risk" | "a foreseeable and material risk that … will materially contribute to the death of, or serious injury to, more than 50 people or more than one billion dollars ($1,000,000,000) in damage to, or loss of, property arising from a single incident involving a frontier model doing any of the following: … (C) Evading the control of its frontier developer or user." |

The report's A3 row ("Humans lose the ability to reliably direct, modify or shut down AI") is the Code's wording nearly verbatim. It pools cells from sources operating at every one of these scales. The CSET cell in particular is a different phenomenon, an operator-level accident. The SB 53 material is from a US source I read only for this record; the US verifier may want to check it.

### 4.3 Systemic risk, and manipulation

- **Systemic risk, AI Act:** capability-specific + Union-market + value-chain propagation (Art. 3(65)).
- **Systemic risk, Hacker et al.:**
  - Four criteria (§4, p.5): "Scale and scope of harm", "Simple aggregation vs. collective harms", "Potentially irreversible", "Complexity" (cascading).
  - Four levels: single-model (monoculture), multi-model (correlated), model-platform integration, model-institution integration.
  - Three readings of "specific to high-impact capabilities" (§6.3.2, p.8–9): risk *category*; marginal *risk level* (their preferred operative reading); capabilities merely *present in* frontier models.
  - Table 1 (p.21) collects finance and complexity definitions, e.g. Kaufman & Scott: "The risk or probability of breakdowns in an entire system, as opposed to breakdowns in individual parts or components"; Helbing: "interdependent, so-called 'cascading' failures in a network".
  - The DSA (Art. 34) uses an *enumerative* approach with no definition (per Hacker, p.6).
  - These are close to the Code's App. 1.2.2 characteristics, but the Code treats them as *contributing*, not *essential*.
- **Manipulation:** EU uses at least two notions.
  - The AI Act Art. 5(1)(a) prohibition: an individual/group decision distorted, causing "significant harm".
  - The Code's "harmful manipulation": the *strategic* distortion of "large populations or high-stakes decision-makers".
  - The report's A4 row ("at scale or of key decision-makers") matches the Code. IASR's "little evidence of … manipulating people at scale" (§5.3) may be measuring a third thing. That is for the UK/IASR verifier.
- **Hallucination, Hacker et al. p.13:** "outputs that contain factually false or misleading information".
- **AI accident, CSET-2021:** unintended failures, distinguished from intentional misuse (p.4). Three failure types: robustness, specification, assurance (p.6).

---

## 5. New references worth adding

| Ref | Why | Relata |
| --- | --- | --- |
| European Commission, *Guidelines on the scope of the obligations for providers of general-purpose AI models*, C(2025) 5045 final, 18 Jul 2025 | Authoritative on Code status (¶94–100), fines date (¶106), the serious-incident reading (¶103), "high-impact capabilities" not fixed (¶38), and the 10^23 GPAI indicator | `ec-2025-gpai-guidelines` |
| California SB 53 (TFAIA), ch. 138, Stats. 2025 | Counterexample to "only instrument"; scale-bounded loss-of-control and catastrophic-risk definitions; internal-use risk (§22757.12(a)(10)). Lane: US verifier | `california-2025-sb53` |
| CSET-2021 (Arnold & Toner) as a C1/C12/A11 source | Names competitive pressure, complexity, many instances and over-reliance as risk factors | `arnold-2021-ai-accidents` (existing) |
| Reg. (EU) 2026/1744, Digital Omnibus on AI | Amends the AI Act. Reportedly adds prohibitions on AI-generated NCII/CSAM from 2 Dec 2026 (bears on A5) and new AI Office powers | not filed; OJ text not retrieved. [S] via FLI Explorer and law-firm alerts (White & Case, K&L Gates) |
| The Future Society, "Protecting GPAI Rules" (Jun 2025) | The source of the 100/200 staffing figure the Chairs endorsed | not fetched: https://thefuturesociety.org/wp-content/uploads/2025/06/ProtectingGPAIRules.pdf |

---

## 6. Bibkeys

**I created:**
- `eu-2024-ai-act`: AI Act OJ PDF, 144 pp.
- `eu-cop-2025-safety-security`: Code S&S chapter, official Commission PDF, 43 pp.
- `eu-cop-chairs-2025-statement`: Chairs' statement. **Secondary host**: browser print of code-of-practice.ai; statement on pp.2–3.
- `ec-2025-gpai-guidelines`: Commission GPAI Guidelines.
- `hacker-2026-digital`: auto-created by `relata ingest` from the DOI; FAccT '26 entry with arXiv v2 PDF attached.
- `california-2025-sb53`: SB 53 chaptered text, browser print from leginfo.

**Already present (created by other agents; I used them and did not duplicate):**
- `hoffmann-2025-eu-code-safety`: CSET-2025.
- `arnold-2021-ai-accidents`: CSET-2021. Its attached PDF has the same sha256 as my download (b8d5d649…).

Nothing of mine is left in `relata pending`. No entry carries verification events yet; I did not run `relata verify`.

---

## 7. Feedback

**On the brief.** It worked well for me. Two things helped most:
- Naming the coordinator as first reader, with Joseph as a later evidence-reader. It told me to put evidence *next to* each proposed change.
- Joseph's scale illustration for loss of control. It turned the definitions record from a glossary into an analysis (§4.2).

The one ambiguity was "the CSET column": the report has two CSET sources and the column doesn't say which it holds.

**On the process.**
- relata's `add` reads BibTeX from stdin. In zsh, `</dev/stdin <<'EOF'` concatenates both inputs (MULTIOS) and hangs a non-TTY caller. I lost a few minutes to this. Plain `<<'EOF'`, or running under bash, works.
- The dry-run output of `relata ingest` says "staged … → ingest/" even though "nothing was written". That was briefly alarming.

**Adjacent, for Joseph's EOI.** The Chairs' statement explicitly holds UK AISI up as the recruitment model the EU should copy (quote in §2.7). The same statement says the AI Office lacks anyone whose job is to scan the frontier. Both might be useful context for why AISI matters and what it is known for.

I'm staying on the line for follow-ups.
