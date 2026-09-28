# Company frameworks: xAI, NAVER, G42, Cohere, NVIDIA, Magic, and newcomers

*Written 2026-09-27 by a fork of the company-frameworks agent, for that agent to fold into `company-frameworks.md` and then into `influx/safety-risk-factors.md`. The report itself was not edited. Sibling forks cover OpenAI, Google DeepMind, and Meta/Microsoft/Amazon; the parent covers Anthropic.*

**What I read.**
- **Read whole:**
  - xAI's current *Frontier Artificial Intelligence Framework* (FAIF, effective 30 Jun 2026) and its predecessor (30 Dec 2025).
  - NAVER ASF 2.0 (7 Jul 2026) and the 2024 ASF page.
  - G42 (Feb 2025).
  - Magic (Jul 2024; the live page).
- **Read by the parts relevant to the report:** xAI's Aug 2025 RMF (diffed against Dec 2025, since the two are nearly identical), Cohere (§§1–3), and NVIDIA (risk process and hazard list).
- **Shanghai AI Lab / Concordia framework:** Executive Summary and §1 only.

Page numbers are **PDF page indices** of the copy in relata unless marked "printed". Every provider PDF was either downloaded live today or taken from the hash-pinned corpus of Zhu (2026, `zhu-2026-silent`). Where both exist, the SHA-256 hashes match; they are recorded in each footnote.

---

## 0. Headlines

1. **xAI's current framework is a quiet rewrite.** The rewrite runs from a California-compliance document to an EU-Code-shaped one, and it has no revision account.
   - **Removed** from the 30 Jun 2026 FAIF, relative to 30 Dec 2025:
     - the statement "This FAIF complies with California's Transparency in Frontier Artificial Intelligence Act";
     - the TFAIA definition of catastrophic risk (the word "catastrophic" now occurs **0** times, against 8);
     - both quantitative deployment criteria: a restricted-query answer rate "less than 1 out of 20", and MASK dishonesty "less than 1 out of 2";
     - the named benchmarks;
     - the anonymous non-adherence reporting "with protections from retaliation";
     - the whistleblower sentence;
     - the transparency and third-party-review section;
     - "(for example, safety culture)" as a post-mortem focus.
   - **Added:**
     - the EU Code's four specified risks, including a verbatim EU definition of loss of control;
     - an annual "full systemic risk assessment" with four reassessment triggers;
     - a "Security Goal" covering insider threats, reviewed yearly;
     - incident reporting to authorities "when reportable";
     - a systemic-risk "acceptance determination" as a precondition of release.
   - **The PDF's own metadata title is "Privileged/Confidential DRAFT working FRAMEWORK DOC"** (pdfinfo, file SHA-256 2c3c6313).
   - Zhu codes xAI's four revisions as the only ones in the corpus with **no account of any kind** (Table 7). Zhu also records the Dec 2025 → Jun 2026 pair as 45 material changes, 27 of them weakenings. The Midas Project logged the rewrite on 11 Jul 2026 as "Major Change, Not Disclosed" [F].
   - **Consequence for the report's force codes.** Only a developer's own TFAIA framework carries California's penalty for "fail[ing] to comply with its own frontier AI framework" (§22757.15(a), civil penalty up to $1M per violation). It is now unclear, from xAI's documents, which document plays that role. The Dec 2025 one said so explicitly; the Jun 2026 one is silent. I found no other xAI TFAIA document; x.ai blocks automated access, so its site was not checked directly.
2. **NAVER's ASF 2.0 no longer names catastrophic hazards.** The 2024 ASF ("ASF Beta") had two risk categories:
   - "loss of control", defined as "AI systems causing severe disempowerment of the human species";
   - misuse, with "biochemical weapons" as the example.

   It also set a frontier-AI evaluation cycle of "every 3 months, or when performance increases by 6x". ASF 2.0 (7 Jul 2026) is service-centred. It sets three protected values (life and physical safety, economic value, non-discrimination) across three protected subjects, and uses an impact matrix keyed to the Korean AI Basic Act's "High-Impact AI". The English and Korean texts contain no occurrence of "control"/통제, "weapon"/무기, "cyber"/사이버, "biolog"/생물 or "catastroph". The periodic, capability-indexed trigger is gone. The governance side is *strengthened*: a dedicated AI Safety Center (est. March 2026, inside the CRO organization) and a three-layer structure ending at the Board's risk committee.
3. **Magic's policy is self-declared stale.** The live page (checked 2026-09-27) now opens: "Note: This policy is outdated. We're working on an update." Below it sits Version 1.0 of 2 Jul 2024.
4. **Cohere and NVIDIA, both in METR's count of twelve, are not catastrophic-risk frameworks in the RSP sense.**
   - **Cohere** explicitly sets threshold-gated catastrophic-risk approaches aside. It focuses "on risks that are known, measurable, or observable today". Its launch "bright line" is "no significant regressions compared to our previously launched model versions".
   - **NVIDIA** sorts products by use case and autonomy (MR1–MR5), and calls this "a more effective proxy for risk than relying on compute thresholds". It lists four frontier hazards: cyber, CBRN, persuasion and manipulation, and "at-scale discrimination".
   - This matters for any reading of "N company frameworks" as evidence that N developers manage CBRN / loss-of-control risk.
5. **Newcomers.** None of these is a new *developer* framework of the RSP kind:
   - METR's list still has the same twelve developers (checked 2026-09-27; newest entry is Anthropic RSP v3.4). Zhu's census (Sep 2026) likewise counts twelve.
   - **Chinese developers.** Zhipu, MiniMax and 01.AI signed the Seoul Frontier AI Safety Commitments, which called for published safety frameworks. I found no framework from any of them (\[S], via a secondary inventory, and my own searches). DeepSeek and sixteen other firms signed CAICT's domestic *AI Safety Commitments* (Dec 2024); per Carnegie \[F], these do not centre on red lines.
   - **The one new Chinese framework document** is a *guideline*: Shanghai AI Lab and Concordia AI's *Frontier AI Risk Management Framework v1.0* (Jul 2025). It is written "as a guideline for general-purpose AI model developers" and calls on developers "to adopt compatible risk management frameworks". Its force is *rec*, not a company commitment, although Shanghai AI Lab is itself a developer.
   - **SB 53 filers.** I found no public list of which companies filed as "large frontier developers" under SB 53. Secondary law-firm summaries name OpenAI, Anthropic, Google DeepMind, Meta and Microsoft as likely in scope. Treat as unestablished.

---

## 1. A force code for company frameworks (proposal to the parent)

The report's force codes have no slot for a developer's own framework. I'd suggest ***self***: binding only on the developer, and revisable by the developer at will. Two refinements, each with evidence from this slice:

- **Modal strength inside a framework varies, and it drifts.**
  - xAI Aug 2025 → Jun 2026: "we will allow xAI employees to anonymously report" (RMF p.8) is gone entirely.
  - Zhu XAI-2-035 records the Feb → Aug 2025 change from "we would take steps to stop or prevent that event" to "we may take steps".
  - I'd mark *self* where the text says "will/shall/must", and *self-disc* (discretionary) for "may / aim / intend / as appropriate / e.g.". Most of xAI's Jun 2026 mitigations are *self-disc*. Its "at least once a year" assessment and yearly Security Goal review are *self*.
- **A law overlay where a statute makes the framework enforceable.**
  - SB 53 §22757.12(a): a large frontier developer "shall write, implement, comply with, and … publish" a frontier AI framework.
  - §22757.15(a): one that "fails to comply with its own frontier AI framework shall be subject to a civil penalty … not exceed[ing] one million dollars ($1,000,000) per violation" (relata `california-2025-sb53`).
  - So *self* content becomes *self+law* only in the document the developer designates as its TFAIA framework. xAI's Dec 2025 FAIF designated itself; the Jun 2026 FAIF does not.
  - The EU Code (Commitment 1) makes the signatory's Safety & Security Framework *commit*. xAI signed only the Safety & Security chapter (report §3), and its Jun 2026 FAIF footnotes the Code's terminology twice (pp.1–2). That suggests, without stating, that this document is meant to serve the Code.
  - NAVER positions ASF 2.0 against Korea's AI Basic Act (in force 22 Jan 2026). The Act's "High-Impact AI" category defines ASF 2.0's "special domain" (p.8).

---

## 2. Proposed §1.1 source-table rows

| Date | Code | Document | Kind | relata | Tag |
| --- | --- | --- | --- | --- | --- |
| Jul 7, 2026 | NAVER-26 | NAVER, *ASF 2.0: AI Safety Framework 2.0*[^naver26] | Company framework (*self*) | `naver-2026-asf2` | P |
| Jun 30, 2026 (no announcement; server Last-Modified 10 Jul) | xAI-26 | xAI, *Frontier Artificial Intelligence Framework*[^xai26] | Company framework (*self*; TFAIA status unstated) | `xai-2026-faif` | P |
| Dec 30, 2025 | xAI-25 | xAI, *Frontier Artificial Intelligence Framework*, superseded[^xai25] | Company framework, declared TFAIA-compliant (*self+law* while current) | `xai-2025-faif` | P |
| Aug 20, 2025 | xAI-RMF | xAI, *Risk Management Framework*, superseded[^xairmf] | Company framework (*self*) | `xai-2025-rmf` | P |
| Jul 2025 | SHLab | Shanghai AI Lab & Concordia AI, *Frontier AI Risk Management Framework v1.0*[^shlab] | Guideline for developers (*rec*) | `shanghaiailab-2025-frontier` | P (Exec. Summary and §1 read) |
| Feb 17, 2025 | NVIDIA | NVIDIA, *Frontier AI Risk Assessment*[^nvidia] | Company framework (*self*) | `nvidia-2025-frontier` | P |
| Feb 11, 2025 | Cohere | Cohere, *Secure AI Frontier Model Framework* V1.0[^cohere] | Company framework (*self*) | `cohere-2025-secure` | P |
| Feb 6, 2025 | G42 | G42, *Frontier AI Safety Framework*[^g42] | Company framework (*self*) | `g42-2025-frontier` | P |
| Jun 17, 2024 | NAVER-24 | NAVER, *AI Safety Framework (ASF)* ("ASF Beta"), superseded[^naver24] | Company framework (*self*) | `naver-2024-asf` | P |
| Jul 2, 2024 | Magic | Magic, *AGI Readiness Policy* v1.0 (live page: "outdated")[^magic] | Company framework (*self*) | `magic-2024-agi-readiness` | P |
| Sep 8, 2026 (arXiv v1) | Zhu | Zhu, *Silent Revision* (arXiv 2609.08789)[^zhu] | Measurement study of framework revisions (under review, NeurIPS workshop) | `zhu-2026-silent` (already in relata) | P |

---

## 3. §2(a) crosswalk: cells for these frameworks

My view on columns: xAI-26 earns one if company frameworks get columns at all, because it adopts the EU specified-risk set verbatim. The others are better as a compact "other company frameworks" note under the table. Cells are my reading of the document; the quote bases are in §6 and the footnotes.

| # | xAI-26 | xAI-25 | NAVER-26 | NAVER-24 | G42 | Cohere | NVIDIA | Magic |
|---|---|---|---|---|---|---|---|---|
| A1 CBRN | E | E | — | E (bio/chem example) | E (bio; chem in DML-2 objective) | X¹ | E | E (bio) |
| A2 Cyber | E | E | — | P (red-team domain) | E | E (malware; insecure code) | E | E |
| A3 Loss of control | E (EU wording) | E (TFAIA "evading the control") | — | E ("severe disempowerment") | P ("may add" Autonomous Operation) | X¹ | — | D² |
| A4 Manipulation | E ("Harmful Manipulation Risks") | — | — | P (disinformation red-team domain) | P ("may add" Advanced Manipulation) | — | E | — |
| A5 Criminal / synthetic content | P ("criminal … activity" refusals) | P | P (notices for outputs "difficult to distinguish from real content") | — | P (fraud, illicit generation in DML-2 objective) | E (CSAM, cybercrime) | — | — |
| A6 Malfunction | — | — | E ("harmful or inaccurate outputs") | — | — | E ("inaccurate in a way that has a harmful impact") | D (MR scoring; healthcare example) | — |
| A7 Critical infrastructure | P ("systems of infrastructural or national security importance") | E ("Cyber Attacks on Critical Infrastructure") | — | — | — | — | P (use-case tiers) | E (in cyber threshold) |
| A8 Labour | — | — | — | — | — | — | — | — |
| A9 Power concentration | — | — | — | — | — | — | — | — |
| A10 Military | — | — | — | — | P (defence as autonomy sector) | — | P (defence as MR4 use case) | — |
| A11 Over-reliance / psychological | — | — | — | — | — | P (psychological harm via cybercrime) | — | — |
| A12 Privacy | P (personal-data security) | — | — | — | — | E (data-privacy violation; sensitive-info disclosure) | — | — |
| A13 IP | — | — | — | — | — | — | — | — |
| A14 Bias | — | — | E ("Preventing Unjust Discrimination") | E (KoBBQ, KoSBi datasets) | — | E (discriminatory outcomes) | E ("At-scale discrimination") | — |
| A15–A16, A18 | — | — | — | — | — | — | — | — |
| A17 Multi-agent | — | — | P (multi-model combination risk) | — | — | — | — | — |

Notes:
1. Cohere sets catastrophic-threshold approaches aside rather than omitting them. It notes "risks described as catastrophic or severe, such as capabilities related to radiological and nuclear weapons, autonomy, and self-replication" (p.14). It says bio-risk research "fails to account for entire risk chains beyond access to information" (p.15). Its assurance "is focused on risks that are known, measurable, or observable today" (p.15). X is my reading of that; a careful reader might prefer "—".
2. Magic names "Autonomous Replication and Adaptation" and "AI R&D" as Covered Threat Models (p.5), not "loss of control". D rather than E.

- **NAVER-26 also has an unmapped hazard.** "Protecting Economic Value", meaning harm "arising from the infringement of economic value … for users, the public, and the AI service ecosystem" (p.6), has no row in A1–A18.
- **SHLab** (if wanted as a reference column) names:
  - four categories: misuse, loss of control, accident, systemic;
  - thresholds in cyber offence, biological threats, "large-scale persuasion and harmful manipulation" and loss of control (p.2);
  - A7-type "Accident Risks" in safety-critical infrastructure (nuclear, financial stability, grid; §1.5, p.13–14).

---

## 4. §2(b) and §2(c) additions, keyed by row

Codes follow the report: role (F/T/M/I/O), then force. *self* / *self-disc* are as proposed in §1.

**B1 Dangerous general capabilities.**
- Magic's Critical Capability Thresholds (p.6): cyber "cost of discovery of new zero-days … reduced by at least 10x"; AI R&D "can effectively replace high-level machine learning researchers"; ARA "could autonomously maintain its own operation executing cybercrime and using the proceeds to create arbitrarily many replicas of itself" (F; thresholds *self*).
- G42 Frontier Capability Thresholds, bio and cyber (pp.4–6) (F; *self*).
- xAI-26: "dual-use capabilities (e.g., offensive cyber capabilities)" is one of three evaluation "buckets" (p.1) (F).

**B2 Harmful propensities.**
- xAI-26: "concerning propensities (e.g., a propensity for deceiving the user)" (p.1). Loss-of-control practice "centers around scalable model oversight, training against high-risk model behaviors such as deception and sycophancy" (p.4) (F; M *self-disc*).
- xAI-25: "AIs may develop value systems that are misaligned with humanity's interests" (p.6) (F). This is removed in xAI-26.
- SHLab: "strategic deception", "instrumental goals contrary to human ethics and morality" (p.13) (F; *rec*).

**B3 Agentic autonomy.**
- NVIDIA makes autonomy a *risk-tier input*. The Preliminary Risk Assessment scores "Level of autonomy", from "Inference API" (MR1) to "Autonomous agent without user approval" (MR5) (p.2). "A frontier model would be classified as MR5" (p.3) (F; tiering *self*).
- NAVER-26 flags agents as the reason risks "inevitably change" (p.13) (F).

**B5 Evaluation gap / test-awareness / under-elicitation.**
- xAI-25: "if the evaluation environment is recognizable as a testing environment to the AI system under test, the system may change its behavior" (p.7) (F). **Removed in xAI-26.**
- G42: in-depth evaluations use "capability elicitation … to optimize performance, overcome model refusals, and avoid underestimating model capabilities" (p.4) (M *self*).
- G42 also presumes a model below threshold if it scores lower than an outside model "evaluated to be definitively below" (p.4). Coded as M *self*; it is a scoping rule that relies on others' evaluations.

**B6 Brittle safeguards / jailbreaks.**
- xAI-26: "we continually evaluate and improve robustness to adversarial attacks that seek to remove xAI model safeguards (e.g., jailbreak attacks)" (p.3) (M *self-disc*).
- G42 DML-2 objective: "Even a determined actor should not be able to reliably elicit CBRN weapons advice … via jailbreak techniques" (p.8) (M *self*).

**B7 Weight / infrastructure security.**
- xAI-26 §2.4: "xAI will maintain a documented Security Goal … including sophisticated non-state actors, insider threats, state-sponsored actors … reviewed at least every year"; controls "adopted based on the NIST 800-171 Rev.3 framework and supported by SOC 2 Type II evaluations" (p.7) (M *self*).
  - This *replaces* xAI-25's outcome claim: "sufficient to prevent its critical model information from being stolen by a motivated non-state actor" (p.9).
- G42 SML-1 to SML-4 (pp.9–10). Key rule: "if a necessary Security Mitigation Level cannot be achieved, then further capabilities development of the model must be paused" (p.5) (M *self*; a pause commitment).
- Magic: security measures "based on recommendations in RAND's Securing Artificial Intelligence Model Weights report", conditional "if and when we observe evidence that our models are proficient" (p.6) (M *self*, conditional).
- **New sub-item: distillation / extraction as a proliferation vector.** xAI-25 and xAI-26: "security measures against the large-scale extraction and distillation of reasoning traces, which have been shown to be highly effective in quickly reproducing advanced capabilities" (xAI-26 p.8) (F; M *self-disc*). The report has no row for this; it sits between B7 and B9. The US agent may have CISA's AA26-251A on distillation campaigns, which a search surfaced; I did not read it.

**B8a Insider threats: human.**
- xAI-26 Security Goal names "insider threats" (p.7). The wording tracks EU-CoP Measure 6.1 (M *self*).
- Cohere's core controls address "insider threats" (p.9) (M *self*).

**B9 Open-weight proliferation.**
- G42 SML-1: "None. G42 may choose to open source models" (p.9).
- When G42 fine-tunes an open-source model, it "may place greater reliance on the original evaluation results" (p.4). This is a scope rule (M *self-disc*).
- NAVER-26 dropped the Beta's use-restriction ladder (next row).

**B10 Reach and scale.**
- NAVER-26 impact matrix: "Broad Scope" vs "Narrow Scope" in the general domain, "in consideration of the risk of use across diverse purposes" (p.8) (F; M *self*).
- NVIDIA "Intended use case" tiers, retail (MR1) to defence (MR4) (p.2) (F).

**B11 Value chain / integration.**
- NAVER-26: "multi-model environments—combining internal and external models … safety reviews must go beyond individual models to also examine risks that may emerge from how models are combined" (p.4) (F).
- Cohere: risks "within the context of customer deployments"; customers "may have additional tests" (pp.9, 15) (F; M *desc*).

**B14 Attacks on AI systems.**
- xAI-26: prompt injection "hijack and redirect Grok-powered applications" (p.3) (F).
- Cohere: OWASP, "Mitre Altas" (sic), prompt injection, "Excessive agency" (pp.6, 13–14) (F; M *self*).

**C1 Race dynamics.**
- SHLab's *passive* loss of control arises where "humans gradually stop exercising meaningful oversight due to automation bias, the AI systems' inherent complexity, or competitive pressures" (p.13) (F; *rec*). This is the one place in my slice where competition appears as a mechanism.
- No company framework in my slice names competition as a factor.

**C6 Safety / risk culture.**
- xAI-25: a post-mortem focuses on "changes to systemic factors (for example, safety culture)" (p.9) (M *self-disc*). xAI-26 keeps "systemic factors" and **drops the safety-culture example** (p.8).
- G42: anonymous reporting mechanisms exist "to foster a proactive safety culture" (p.12) (M *self*).

**C7 Internal risk governance.**
- **G42.** A Frontier AI Governance Board "composed of our Chief Responsible AI Officer, Head of Responsible AI, Head of Technology Risk, and General Counsel". Framework changes are "proposed by the Frontier AI Governance Board and approved by the G42 Executive Leadership Committee". There are "independent internal audits" and "annual external audits to verify compliance" (pp.11–12) (M *self*).
- **NAVER-26.** Three layers:
  - execution by service teams;
  - management by the CRO risk-management working group and the AI Safety Center ("maintains its independence");
  - the Board of Directors' Risk Management Committee as "the final decision-making body".

  AI Safety Center "established … in March 2026, … within the Chief Corporate Responsibility Officer (CRO) organization" (p.11) (M *self*).
- **NVIDIA.** MR5 requires "a detailed risk assessment … approved by an independent committee e.g. NVIDIA's AI ethics committee"; MR4 requires business-unit-leader approval (p.2) (M *self*).
- **Cohere.** "The final authority to determine if our products are safe … is delegated by Cohere's CEO to Cohere's Chief Scientist" (p.15) (M *self*). This is a single-officer gate, the opposite of EU-CoP 8.1's separation of risk ownership from business responsibility.
- **Magic.** Staff report to the Board "on a quarterly basis"; threshold changes require "approval by our Board of Directors, with input from external security and AI safety advisers" (pp.4–5) (M *self*).
- **xAI-26.** "designating risk owners"; "ongoing legal and compliance reviews" (pp.8–9) (M *self-disc*). xAI-25's "Risk owners are also responsible for periodic audits to enforce framework implementation" (p.9) is gone.

**C9 Whistleblowing / suppression.**
- **xAI-RMF and xAI-25:** "Internally, we [will] allow xAI employees to anonymously report concerns about nonadherence, with protections from retaliation" (Aug p.8; Dec p.8). Also: "xAI employees have whistleblower protections enabling them to raise concerns to relevant government agencies regarding imminent threats to public safety" (Dec p.9) (M *self*). **Both are removed in xAI-26.** What remains is "Employee escalation" as an incident-detection channel (p.8) and "(anonymous) reporting channels" for post-market monitoring, which reads as channels for users (p.5).
  - SB 53's whistleblower protections (Labor Code §1107 ff.) bind regardless of the framework text, so the removal changes xAI's *self* layer, not the *law* layer.
- **G42:** "mechanisms for employees to anonymously report potential concerns of non-compliance" (p.12) (M *self*).
- **Midas Project \[F]\[C]:** xAI "rewrote and shortened its Frontier AI Framework removing whistleblower protection language and references to California's SB 53" (entry 11 Jul 2026).

**C10 (or an "adherence" observation) \[F]\[C].** Midas Project, 28 Aug 2025: "xAI released Grok Code Fast 1 despite the model failing a safety test that the company's policy says models must pass before release." Watchdog commentary; not verified against a primary.

**C15–C17 (organizational change, turnover, investor/IPO).** A term search of every document in this slice found no provisions. The terms were: headcount, turnover, growth, investor, IPO, restructur-, reorgani-, merger, acquisition, staffing, competitive pressure. The only organizational-change *content* is NAVER-26's creation of the AI Safety Center (March 2026), which is described, not treated as a trigger.

---

## 5. Triggers for reassessment or update (T), with force

| Source | Trigger | Force |
| --- | --- | --- |
| xAI-26 §2 (p.2) | "a full systemic risk assessment … at least once a year" | T *self* |
| xAI-26 §2 (p.2) | smaller evaluations "may" occur at: "(1) the release of an updated model, (2) in the event of a serious incident, (3) if the model's use or integrations into xAI's systems materially increase risk, or (4) where xAI has reason to believe that the basis for considering the model's systemic risks acceptable has materially changed". These track EU-CoP Measure 1.3 and App. 3 language. | T *self-disc* |
| xAI-26 §2.4 (p.7) | Security Goal "reviewed at least every year" | T *self* |
| xAI-26 §1 (p.2) | "We will review this Framework periodically, and expect significant changes as the capabilities of our models expand" | T *self*, undated |
| xAI-25 §5 (p.10) | FAIF "will be continually adapted and updated as circumstances change, before major new capabilities are launched, and in response to incidents" | T *self* (removed in xAI-26) |
| NAVER-24 (p.5) | Frontier AI evaluated "Every 3 months, or when performance increases by 6x"; compute "can serve as an indicator" | T *self* (removed in ASF 2.0; Zhu NAV-1-005, announced) |
| NAVER-26 (p.13) | Changes in service context, e.g. agents: "examining risks that need to be newly defined" | T *self-disc* |
| G42 (p.4) | Framework review considers "'near miss' incidents, whether internal or industry-wide; recommendations from trusted external experts; as well as changes in industry standards" | T *self-disc* |
| G42 (p.12) | "An annual external review of the Framework"; "more frequent internal reviews, particularly in accordance with evolving standards and instances of enhanced model capabilities" | T *self* |
| G42 (p.5) | If a capability threshold is reached, G42 "will update this Framework to define a more advanced threshold" | T *self* |
| G42 (p.5) | Capability reports "at least once every six months" to the Governance Board and Executive Leadership Committee | T *self* |
| NVIDIA (p.3) | Reassess "if pre-defined thresholds are met e.g. technology matures, component is significantly modified, operating conditions change, or a hazard occurs with high severity or frequency"; a use-case change re-tiers the product | T *self* |
| Magic (p.3) | >50% on LiveCodeBench, or private-benchmark thresholds, triggers the full dangerous-capability evaluations "prior to substantial further model development, or publicly deploying" | T *self* |
| Magic (p.4) | "If we have not developed adequate dangerous capability evaluations by the time these benchmark thresholds are exceeded, we will halt further model development" | T/M *self* (pause) |
| Magic (p.5) | Thresholds "may" be raised; this "will require approval by our Board of Directors, with input from external security and AI safety advisers" | T *self* (governance gate on loosening) |
| SHLab (Exec. Summary) | Comments "integrated on a bi-annual basis" | T *rec* |

**Organizational triggers:** none in this slice. G42's "industry-wide" near misses is the only trigger external to the model.

---

## 6. Definitions record (verbatim, with location)

**Loss of control**
- xAI-26 (p.1): "Our assessment of risk of loss of control includes risks from humans losing the ability to reliably direct, modify, or shut down a model ('Loss of Control Risks')". This is identical to EU-CoP App. 1.4(2), and fn 1 cites the Code's terminology.
- xAI-26 (p.7) and xAI-25 (p.2): "Exact scenarios of loss of control risks are speculative and difficult to precisely specify. Many such scenarios, for example, speculation that a superintelligent AI system hypothetically might escape the control of its developers and wreak havoc on the public, assume dual-use capabilities such as offensive cybersecurity capabilities".
- xAI-25 (p.1 fn 1, quoting TFAIA): catastrophic risk includes a frontier model "(C) Evading the control of its frontier developer or user."
- NAVER-24 (p.3 of snapshot): "NAVER's AI Safety Framework defines the first category of risk as AI systems causing severe disempowerment of the human species." **No successor definition in ASF 2.0.**
- SHLab (p.13): "Loss of control are hypothetical future scenarios in which one or more general-purpose AI systems come to operate outside of anyone's control, with no clear path to regaining control". It distinguishes "passive loss of control, where humans gradually stop exercising meaningful oversight due to automation bias, the AI systems' inherent complexity, or competitive pressures" from "active loss of control, where AI systems behave in ways that actively undermine human control". It focuses on active.

  For §5.2's scale ladder, SHLab sits near IASR 2026: catastrophe-scale, with passive named but set aside. NAVER-24 sits at the civilizational end ("severe disempowerment of the human species"), and xAI-26 at the EU's scale-free rung.

**Misalignment**
- xAI-25 (p.6): "It is also possible that AIs may develop value systems that are misaligned with humanity's interests and inflict widespread harms upon the public." The referent is "humanity's interests", not the developer's intent (compare §5.4, GDM). Removed in xAI-26, which has no misalignment language beyond "concerning propensities".
- SHLab (p.13): AI systems that "develop instrumental goals contrary to human ethics and morality".

**Critical capability / threshold**
- G42 (p.4): "Capability thresholds establish points at which an AI model's functionality requires substantially enhanced safeguards to account for unique risks associated with high-stakes capabilities."
- Magic (p.5): "threat models … proposed mechanisms via which AI systems could cause a major catastrophe in the near future"; "Critical Capability Threshold" table (p.6).
- xAI-26 (p.5): "systemic risk acceptance criteria … incorporating a margin of security". No quantitative criterion is stated. xAI-25 (pp.6–7) gave "an answer rate of less than 1 out of 20 on restricted queries" and "a dishonesty rate of less than 1 out of 2 on MASK".
- SHLab (p.2): "red lines" = "unacceptable outcomes", "yellow lines" = "early warning indicators for escalating safety and security measures".
- NVIDIA (p.3): MR5 set by "a 'wide variety of undefined capabilities' or high levels of autonomy".

**Safeguards / mitigations**
- xAI-26 (p.7): safeguards = "Safety training", "System prompts", "Filters: Applying classifiers to verify safety when a model is queried regarding topics of CRBN risks" ("CRBN" sic).
- G42 (p.7): Deployment Mitigation Levels "protect against misuse … presuming that our development environment's information security has not been violated"; Security Mitigation Levels (p.9) protect "against the theft of model weights, model inversion, and sensitive data".

**Frontier model**
- NVIDIA (p.1): "a highly capable general-purpose AI model that can perform a wide variety of undefined tasks and exceeds the capabilities present in the most advanced models currently in existence".
- Magic (p.3): models that "exceed the current frontier of coding performance".
- xAI-26: none; scope is "xAI's frontier AI models, such as Grok" (p.1).

**Systemic risk:** xAI-26 uses the EU term throughout ("systemic risk assessment", "systemic risk acceptance determination") without defining it.

**Harmful manipulation:** xAI-26 (p.1): "risks of models with high manipulative capabilities potentially being misused in ways that could reasonably result in large scale harm ('Harmful Manipulation Risks')". This is a *misuse* framing, narrower than EU App. 1.4(4)'s "strategic distortion … through persuasion, deception, or personalised targeting". The EU text does not require a misuser.

**Catastrophic risk:** xAI-25 (p.1 fn 1) reproduces the TFAIA definition (>50 deaths or >$1B).

---

## 7. Revision observations (for §5 or a new row; role O)

These are observations about the documents. The report may want them next to FLI-S26's "weakened or voided pledges" (C1) and Zhu's aggregate finding. Zhu's aggregate, verbatim: "77% of traced changes weaken or remove a commitment, and in seven of eight pairs weakenings are more often silent than strengthenings" (abstract).

- **xAI:** five labelled versions in 16 months (Feb 10 draft, Feb 20 draft, Aug 2025, Dec 2025, Jun 2026), none with a revision account (Zhu Table 7, "none", four pairs).
  - Zhu Table 1 counts: Feb → Aug 2025, 35 material changes, 19 weakened; Aug → Dec 2025, 9 changes, 1 weakened; Dec 2025 → Jun 2026, 45 changes, 27 weakened.
  - Zhu App. K records a same-label re-upload (22 Aug 2025) that removed "AISI" from the organizations with which bio filter topics "were identified".
- **NAVER:** ASF 2.0's in-document account (pp.4–5) explains the service-centred reorientation. It does not state that loss-of-control and weapons categories were dropped. Zhu codes the pair "narrative", strict silent-revision rate 0.77.
- **Magic:** v1.0 unchanged since Jul 2024; the page now says it is "outdated".
- **Cohere, G42, NVIDIA:** one version each since Feb 2025 (METR's list and Zhu's manifest agree). G42 committed to "annual external review" and an "annual transparency report" (p.12). I did not find a revised G42 framework as of 2026-09-27. Whether those reviews happened was not checked.

---

## 8. Proposed footnote bodies

[^xai26]: \[P] xAI, *xAI Frontier Artificial Intelligence Framework*, "Effective Date: 30 June 2026". <https://media.x.ai/v1/website/xai-frontier-artificial-intelligence-framework-30-june-2026-99c40684.pdf>. relata `xai-2026-faif`; SHA-256 2c3c6313…, identical to the Zhu corpus row. PDF metadata title: "Privileged/Confidential DRAFT working FRAMEWORK DOC". No announcement or changelog found; Midas Project first logged it 11 Jul 2026 \[F]. Anchors (PDF pages):
    - p.1: "Our assessment of risk of loss of control includes risks from humans losing the ability to reliably direct, modify, or shut down a model ('Loss of Control Risks')". Fn 1: "Terminology used in the The Safety and Security Chapter of the General-Purpose AI Code of Practice".
    - p.2: "xAI will conduct a full systemic risk assessment and mitigation process of our frontier models at least once a year … These trigger points may include (1) the release of an updated model, (2) in the event of a serious incident, (3) if the model's use or integrations into xAI's systems materially increase risk, or (4) where xAI has reason to believe that the basis for considering the model's systemic risks acceptable has materially changed."
    - p.2: "Early analysis has established four primary risk domains … CBRN Risks, Offensive Cybersecurity Risks, Loss of Control Risks and Harmful Manipulation Risks."
    - p.5: "xAI applies a systemic risk acceptance criteria to each identified risk, incorporating a margin of security".
    - p.7: "xAI will maintain a documented Security Goal that identifies the threat actors … including sophisticated non-state actors, insider threats, state-sponsored actors … The Security Goal will be reviewed at least every year."
    - p.8: "If we determine that allowing a system to continue running would materially and unjustifiably increase the likelihood of a risk, we may temporarily fully shut down the relevant system".
    - p.9: "xAI's internal governance practices include managing risks across the lifecycle of our models and ongoing legal and compliance reviews".

[^xai25]: \[P] xAI, *xAI Frontier Artificial Intelligence Framework*, "Last updated: December 30, 2025" (superseded). <https://data.x.ai/2025-12-31-xai-frontier-artificial-intelligence-framework.pdf>. relata `xai-2025-faif`; SHA-256 aa01669c…. Anchors:
    - p.1: "This FAIF complies with California's Transparency in Frontier Artificial Intelligence Act (the 'TFAIA', California Business and Professions Code § 22757.10 et seq.)."
    - p.6: "Our risk acceptance criteria for system deployment is maintaining an answer rate of less than 1 out of 20 on restricted queries."
    - p.7: "maintaining a dishonesty rate of less than 1 out of 2 on MASK."
    - p.8: "Internally, we allow xAI employees to anonymously report concerns about nonadherence, with protections from retaliation."
    - p.9: "xAI employees have whistleblower protections enabling them to raise concerns to relevant government agencies"; "changes to systemic factors (for example, safety culture)".
    - p.10: "For internal use, we review catastrophic risks like oversight evasion before extensive rollout."

[^xairmf]: \[P] xAI, *xAI Risk Management Framework*, "Last updated: August 20, 2025" (superseded). <https://data.x.ai/2025-08-20-xai-risk-management-framework.pdf>. relata `xai-2025-rmf`; SHA-256 39fab200…, which is the 22 Aug 2025 same-label re-upload (Zhu App. K). Anchors: p.8, "Internally, we will allow xAI employees to anonymously report concerns about nonadherence, with protections from retaliation"; p.5, "less than 1 out of 20"; p.7, "less than 1 out of 2 on MASK".

[^naver26]: \[P] NAVER AI Safety Center, *NAVER ASF 2.0: AI Safety Framework 2.0*, "Initial Publication Date: July 7, 2026" (announced 8 Jul 2026). <https://www.navercorp.com/api/article/download/c742a6dd-b5dd-4aa7-a415-93e7af6119ef>; press release <https://www.navercorp.com/en/media/pressReleasesDetail?seq=10034489>. relata `naver-2026-asf2`; SHA-256 56e5ee0d…. Anchors:
    - p.4: "On January 22, 2026, the Framework Act on the Development of Artificial Intelligence and the Creation of a Foundation for Trust (hereinafter, the 'AI Basic Act') came into effect."
    - pp.5–6: "three protected values—protecting life and physical safety, protecting economic value, and preventing unjust discrimination".
    - p.8: "The special domain refers to areas where High-Impact AI, as defined under the AI Basic Act, is used."
    - p.9: "Based on the results, we determine whether the service meets our safety standards."
    - p.11: "in March 2026, we established the AI Safety Center, a dedicated organization for AI Safety within the Chief Corporate Responsibility Officer (CRO) organization"; Board of Directors (Risk Management Committee) is "the final decision-making body".

    The English and Korean texts were term-searched for control/통제, weapon/무기, cyber/사이버 and biolog/생물: 0 hits.

[^naver24]: \[P] NAVER, "NAVER's AI Safety Framework (ASF)", CLOVA tech blog (English page dated 7 Aug 2024; first published 17 Jun 2024). <https://clova.ai/en/tech-blog/en-navers-ai-safety-framework-asf>. relata `naver-2024-asf` (headless-Chrome snapshot with provenance header; page numbers are snapshot pages). p.3: "NAVER's AI Safety Framework defines the first category of risk as AI systems causing severe disempowerment of the human species." p.4: "misusing AI systems to develop hazardous biochemical weapons". p.5: frontier AI evaluated "Every 3 months, or when performance increases by 6x".

[^g42]: \[P] Jackson, Ben Amor, O Herlihy, Murray, Manucha, Kosior & Wilton, *G42's Frontier AI Safety Framework*, Feb 2025 (published 6 Feb 2025). <https://www.g42.ai/application/files/9517/3882/2182/G42_Frontier_Safety_Framework_Publication_Version.pdf>. relata `g42-2025-frontier` (Zhu corpus copy via Wayback; SHA-256 36ddb6b0…). Anchors:
    - p.3: "developed with input from SaferAI and METR".
    - p.4: "'near miss' incidents, whether internal or industry-wide".
    - p.5: "if a necessary Security Mitigation Level cannot be achieved, then further capabilities development of the model must be paused".
    - p.11: "A dedicated Frontier AI Governance Board, composed of our Chief Responsible AI Officer, Head of Responsible AI, Head of Technology Risk, and General Counsel".
    - p.12: "G42 will engage in annual external audits to verify compliance"; "mechanisms for employees to anonymously report potential concerns of non-compliance".

    Note the report's existing caveat: SaferAI "contributed to the process of writing G42's Frontier AI Safety Framework".

[^cohere]: \[P] Cohere, *The Cohere Secure AI Frontier Model Framework*, V1.0, Feb 2025 (announced 11 Feb 2025). <https://cohere.com/security/the-cohere-secure-ai-frontier-model-framework-february-2025.pdf>. relata `cohere-2025-secure`; the live file has the same SHA-256 (9b76fb54…) as the Zhu corpus. Anchors:
    - p.6: "Risks stemming from possible malicious use of foundation AI models, such as generating content to facilitate cybercrime or child sexual exploitation".
    - p.15: "Cohere's approach to risk assurance … is focused on risks that are known, measurable, or observable today"; "The final authority … is delegated by Cohere's CEO to Cohere's Chief Scientist."
    - p.16: "We consider models safe and secure to launch when our evaluations and tests demonstrate no significant regressions compared to our previously launched model versions … This is Cohere's bright line".

[^nvidia]: \[P] NVIDIA, *Frontier AI Risk Assessment*, undated (HTTP Last-Modified 17 Feb 2025; live file unchanged, SHA-256 8c6aade8…). <https://images.nvidia.com/content/pdf/NVIDIA-Frontier-AI-Risk-Assessment.pdf>. relata `nvidia-2025-frontier`. Anchors:
    - p.1: "a 'frontier model' is defined as a highly capable general-purpose AI model that can perform a wide variety of undefined tasks and exceeds the capabilities present in the most advanced models currently in existence".
    - p.2: "MR5 - A detailed risk assessment should be complete and approved by an independent committee e.g. NVIDIA's AI ethics committee."
    - p.3: "A frontier model would be classified as MR5 … we believe these factors are a more effective proxy for risk than relying on compute thresholds"; reassessment when "technology matures, component is significantly modified, operating conditions change, or a hazard occurs with high severity or frequency".
    - p.8: hazards "Cyber offence … Chemical, biological, radiological, and nuclear risks … Persuasion and manipulation … At-scale discrimination".

    A secondary inventory (Vorp Labs) dates it Aug 2025; I found no evidence of an Aug 2025 revision.

[^magic]: \[P] Magic, *AGI Readiness Policy*, "Version 1.0 — July 2, 2024". <https://magic.dev/agi-readiness-policy>. relata `magic-2024-agi-readiness` (headless-Chrome snapshot 2026-09-27; snapshot pages). Anchors:
    - p.1: "Note: This policy is outdated. We're working on an update."
    - p.3: "when, at the end of a training run, our models exceed a threshold of 50% accuracy on LiveCodeBench, we will trigger our commitment".
    - p.4: "If we have not developed adequate dangerous capability evaluations by the time these benchmark thresholds are exceeded, we will halt further model development".
    - p.5: "Such a change will require approval by our Board of Directors, with input from external security and AI safety advisers."
    - p.6: the Critical Capability Threshold table.

[^shlab]: \[P, partial] Shanghai Artificial Intelligence Laboratory and Concordia AI (lead author B. Tse; scientific director Zhou Bowen), *Frontier AI Risk Management Framework (v1.0)*, Jul 2025. <https://concordia-ai.com/wp-content/uploads/2025/07/Frontier-AI-Risk-Management-Framework-v1.0-en.pdf>. relata `shanghaiailab-2025-frontier`. Anchors:
    - p.2: "This framework serves as a guideline for general-purpose AI model developers".
    - p.3: "We call on frontier AI developers, policymakers, and stakeholders to adopt compatible risk management frameworks."
    - p.13: the loss-of-control definition and the passive/active split, quoted in §6.

    Only the Executive Summary and §1 were read (54 pp.).

[^zhu]: \[P] Zhu, *Silent Revision: Measuring Undisclosed Change in the Safety Frameworks of Frontier AI Developers*, arXiv 2609.08789v1, 8 Sep 2026 (preprint; under review at a NeurIPS 2026 workshop; inter-coder agreement not yet reported, §7). relata `zhu-2026-silent`. Corpus: <https://github.com/louisyzhu/frontier-safety-framework-corpus> (DOI 10.5281/zenodo.22670700). Abstract: "67% of material changes (95% CI 62 to 72) are silent under a strict standard"; "77% of traced changes weaken or remove a commitment". Table 1 has the xAI and NAVER pair counts. Table 7 codes the xAI pairs "none". The first-pass coding was by "an agentic language-model system of the Claude family" (p.5), with 244 of 710 rows adjudicated by the author. That is an independence caveat for this report, which is also written by Claude.

**Secondary items used above (for footnotes if kept):**
- The Midas Project, *AI Safety Watchtower*, <https://www.themidasproject.com/watchtower>, entries of 11 Jul 2026 and 28 Aug 2025 \[F]\[C].
- Vorp Labs, "Current Frontier AI Framework Inventory 2026" (data updated 12 Jul 2026), <https://vorplabs.com/ai-regulatory-updates/frontier-ai-frameworks> \[S]\[F]. Source for "Seoul signatories without a published framework". Not independently checked; it misdates NAVER (lists only the 2024 ASF).
- S. Singer, Carnegie Endowment, 28 Jan 2025, <https://carnegieendowment.org/research/2025/01/deepseek-and-other-chinese-firms-converge-with-western-companies-on-ai-promises> \[S]\[F]: CAICT's *AI Safety Commitments* (Dec 2024), "DeepSeek joined sixteen other Chinese companies".
- METR, "Frontier AI Safety Policies", <https://metr.org/fsp> \[F] (list checked 2026-09-27).

---

## 9. Bibkeys created (all new; none existed)

`xai-2026-faif`, `xai-2025-faif`, `xai-2025-rmf`, `naver-2026-asf2`, `naver-2024-asf`, `g42-2025-frontier`, `cohere-2025-secure`, `nvidia-2025-frontier`, `magic-2024-agi-readiness`, `shanghaiailab-2025-frontier`.

Used but pre-existing: `zhu-2026-silent`, `california-2025-sb53`.

I used only `relata add` (BibTeX on stdin) and `relata pdf`. No `ingest`, and nothing touched the shared queue.

---

## 10. Not done, and notes on the brief

- **Not read.** Shanghai §§2–6. Cohere and NVIDIA mitigation catalogues in detail. The xAI Feb 2025 drafts (Zhu covers them). Any xAI or NAVER model cards.
- **Not established.**
  - Which document is xAI's current TFAIA framework. x.ai returned 403/Cloudflare to both curl and WebFetch.
  - Whether G42's promised annual external review and transparency report were published.
  - The list of SB 53 filers.
- **For the parent.** The Anthropic *Frontier Compliance Framework* (Zhu App. L) looks like the analogue of the xAI question: a separate compliance document beside the RSP. If so, the *self* vs *self+law* split may matter most for Anthropic and xAI. Separately, Zhu's first-pass coder was a Claude-family system. That matters when Zhu is cited for Anthropic's v2.2 → v3.0 silence figures.
- **On the brief.** The newcomer question was the right one to ask. The honest answer is "none of the RSP kind", plus two regressions in scope (NAVER, xAI), which a count of frameworks would hide.
