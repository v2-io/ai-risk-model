# Company frameworks: Google DeepMind (Frontier Safety Framework)

*Written 2026-09-27 by a forked Claude (Opus 5.5) instance, for the integrator of `influx/safety-risk-factors.md`, as the GDM part of `company-frameworks.md`. The report itself was not edited. Scope: GDM's Frontier Safety Framework (FSF) in its current version (v3.1), with the earlier versions read where a comparison matters, plus the question of which document Google designates for SB 53 and for the EU Code.*

**What was read.**
- **FSF v3.1** (17 Apr 2026, 20 pp.), whole. SHA-256 `ad10d2d2…`, matching Zhu's manifest. It is the current version: the frontier-safety page lists v3.1 as the latest as of 2026-09-27.
- **FSF v3.0** (22 Sep 2025, 16 pp.), whole. SHA-256 `87ebf40b…`, matches Zhu.
- **FSF v2.0** (4 Feb 2025) and **v1.0** (17 May 2024): the passages on pause/hold, governance, deceptive alignment and autonomy, plus term searches.
- **The announcement post** "Strengthening our Frontier Safety Framework" (22 Sep 2025, updated 17 Apr 2026), whole.
- **The *Gemini 3.7 Flash FSF Report*** (Aug 2026, 41 pp.): pp.2–8 and 35–41 (overview, elicitation, sandbagging, external testing, the ML R&D/misalignment section), plus term searches elsewhere.
- **Google's *Responsible AI Progress Report*** (Feb 2026): term searches only.

**Pages.** Page numbers are PDF pages. For the FSF and the model report these equal the printed page numbers.

**Codes.** Role and force codes are the report's. For company-framework content I use two force codes, pending whatever the integrator settles on:
- ***self***: a company's own published commitment, in binding language ("will", "only after").
- ***self-d***: company text that is discretionary. That covers "may", "aim", "e.g.", and a "will" followed by an escape clause such as "or we otherwise assess that …".

---

## 0. Headlines

1. **The FSF has no development or training gate, and no pause language, in v3.0 or v3.1.**
   - Every risk-acceptance condition is expressly limited to deployment. For misuse: "This is required only for external deployment, not internal deployment or further development" (v3.1 p.7). For ML R&D: "required only for external deployment and high-risk internal deployment, not further development" (p.7).
   - Earlier versions had hold language. v1.0: "we would put on hold further deployment or development, or implement additional protocols" (p.2). v2.0: "the response plan may involve putting deployment or further development on hold until adequate mitigations can be applied" (p.3).
   - v2.0 also made adoption competitor-contingent: "our adoption of the protocols described in this Framework may depend on whether such organizations across the field adopt similar protocols" (p.1).
   - This is the primary-text basis for FLI-S26's GDM claim ("weakened or voided pledges to pause unilaterally … some citing competitor-contingent conditions"), which is now checkable. For GDM it holds: hold language existed (disjunctive in v1.0, "may" in v2.0) and is gone, and the competitor-contingent clause existed in v2.0. *High.*
2. **"Loss of control" never appears in any FSF version** (term search, v1.0–v3.1: 0 hits).
   - The FSF's construct is "significantly undermining human control" (the v3.1 TCL). That matches Shah et al.'s refusal to treat loss of control as a category.
   - But GDM's other policy-layer texts do use the construct:
     - The announcement post frames the misalignment domain in the EU Code's loss-of-control formula: "misaligned AI models might interfere with operators' ability to direct, modify or shut down their operations."
     - The Aug 2026 model report refers to "a potential loss of control event" (p.40) and names an internal "Loss of Control (LoC)" team (p.35).
   - So §5.2's "Not a category | GDM" row is true of Shah 2025, not of GDM's policy vocabulary. *High.*
3. **Misalignment now has a governed threshold, but only one set at "significant", not "severe", harm.**
   - The ladder: v2.0 "Deceptive Alignment" CCLs (exploratory) → v3.0 "illustrative only … we do not associate them with explicit risk acceptance criteria" (p.4) → v3.1 a *Tracked* Capability Level (Stealth and Situational Awareness), with periodic residual-risk assessment and conditional safeguards.
   - Severe-scale misalignment is governed only indirectly, through the ML R&D CCLs.
   - v3.0's Instrumental Reasoning Level 2 (undetectable even when monitored) was removed in v3.1 and not replaced. The changelog mentions only the merge of domains (Zhu GDM-2-023, verified).
4. **Security levels for misuse CCLs rose from SL2 to "SL2+", which is defined as adding insider-threat measures.** The same version states that insider *misuse* needs nothing beyond baseline controls. Both are p.9 and p.11 of v3.1. Directly relevant to B8a.
5. **Governance got less specific.**
   - v2.0 named three councils (AGI Safety Council, Responsibility and Safety Council, Trust & Compliance Council) and gave the AGI Safety Council a review role.
   - v3.0 replaced "appropriate corporate governance body" with "appropriate governance function".
   - v3.1's new "Governance structure" section names no body, role or reporting line.
   - The FSF contains no whistleblowing, board, risk-officer or internal-audit provision, and no organizational factor of any kind (term search).
6. **No SB 53 designation found.** Google has published no statement I could find naming the FSF (or anything else) as its SB 53 "frontier AI framework". A third-party tracker says the same as of 4 Jul 2026 (\[S]).
   - The legal force of FSF commitments therefore can't be stated. If the FSF is Google's SB 53 framework, §22757.15(a) makes failing to comply with it penalizable up to $1M per violation.
   - The FSF's wording tracks the statutes in places: "high-impact capabilities" (AI Act Art. 3(64)); the Code's Measure 1.3 reassessment trigger, nearly verbatim. That suggests drafting for the EU Code, but it is inference.
7. **Zhu 2026 (`zhu-2026-silent`), verified on three GDM items against the primaries:**
   - the ML R&D quantitative anchor "(e.g. 2x) from 2020-2024 rates" (v2.0 p.6) became "from historical rates" (v3.0 p.13);
   - "appropriate corporate governance body" (v2.0 p.4) became "appropriate governance function" (v3.0 p.9);
   - Instrumental Reasoning Level 2 (v3.0 p.15) is absent from v3.1.

   Zhu's corpus is the best available version map of all twelve frameworks. It is useful to the sibling forks as well.

---

## 1. Force profile of the FSF: what it binds, what it leaves discretionary

**Binding-language commitments (*self*).**
- **Deployment gate, misuse** (v3.1 p.10): "external deployments of a model take place only after the appropriate governance function determines the residual risk to be acceptable (including a safety case where a CCL has been reached)."
- **Deployment gate, ML R&D and misalignment** (p.14): "external deployments and high-risk internal deployments of a model take place only after the appropriate governance function determines the residual risk to be acceptable".
- **Assessment trigger** (p.5): "We conduct a critical capability assessment prior to the first external deployment of a new frontier AI model."
- **Misalignment TCL** (p.14): "When a model has reached this TCL, we will carry out periodic residual risk assessments of the misalignment risk posed … If the risk assessment deems the residual risk from internal deployment to be unacceptable without additional safeguards (such as chain-of-thought monitoring on high-risk deployments), these will be applied."
- **Review cadence** (p.17): "will be reviewed at least once a year". v3.0 p.16 read "will be updated at least once a year".
- **Safety-case review after deployment** (p.10): "Material updates to a safety case will be submitted to the appropriate governance function for review".

**Discretion and escape clauses (*self-d*).**
- **Security levels are "recommended", with an adequacy escape** (p.7): "Security mitigations have been applied to the model weights reaching the recommended security level stated below, or we otherwise assess that the level of security applied is adequate, e.g. … if they match or exceed the level of security applied to other models with similar capabilities or risk profiles, or we assess that the benefits of the open release of model weights outweigh the risks."
- **Security levels are framed as a field-wide recommendation, not a company commitment** (p.11): "the minimum appropriate level of security the field of frontier AI should apply"; "we believe these recommendations will only be effective if the entire frontier AI field applies them, and of limited social utility if not."
- **Mitigations are chosen at the time a threshold is reached** (p.6): "the specific mitigations we implement may be determined when a T/CCL is reached".
- **Alert thresholds can be moved** (p.6): "the response plan may include updating the alert threshold".
- **Low-risk external deployments are exempt** (p.5 fn 4): "A critical capability assessment may not be conducted for low-risk external deployments (e.g. to a small number of trusted testers) if the appropriate governance function determines the residual risk … to be acceptable even if the model has reached a T/CCL".
- **Proportionality and innovation are named as balancing terms** (p.8): "our assessments will often involve some level of subjective analysis. The concept of proportionality is central … thus balancing safety with innovation."
- **Disclosure to government is an aim** (p.17): "we aim to share relevant information with appropriate government authorities".
- **Updates after review are optional** (p.17): "Following this assessment, we may: Update our risk domains and T/CCLs …". v3.0 also reads "we may".

**Not covered at all.**
- further development or training (see Headline 1);
- non-severe risks, which are assigned to "Google's suite of AI responsibility and safety practices" (§1.1, p.4);
- any organizational factor.

**Legal overlay.**
- **SB 53.** Whether the FSF is Google's SB 53 framework is unverified (\[U]). The law applies to a "large frontier developer" (>$500M revenue, >10^26 FLOP): "shall write, implement, comply with, and clearly and conspicuously publish … a frontier AI framework" (§22757.12(a)). The penalty covers one that "fails to comply with its own frontier AI framework" (§22757.15(a), ≤$1M per violation; relata `california-2025-sb53`).
- **EU Code.** Google is a signatory ("full signatory"; \[S] via the tracker; the Commission list is cited in report §3). Which document serves as its Commitment 1 "Safety and Security Framework" is likewise unstated.
- **Drafting evidence (inference, *medium*):**
  - The v3.1 glossary defines frontier models as "trained on a large data set, display significant generality, are capable of performing a wide range of distinctive tasks and have high-impact capabilities" (p.18). That tracks the AI Act's GPAI definition and Art. 3(64).
  - The §5.1 review trigger reproduces Code Measure 1.3's "reasonable grounds to believe the adequacy of … Framework and/or … adherence thereto has been … materially undermined".
  - v3.0 p.16 said the review assesses "appropriateness for the management of systemic risk", the EU term. v3.1 changed it to "significant and severe risk".

---

## 2. Proposed additions, keyed to the report

### 2.1 §1 source table: a new row

| Date | Code | Document | Kind | relata | Tag |
| --- | --- | --- | --- | --- | --- |
| Apr 17, 2026 (v3.1; v3.0 Sep 22, 2025) | GDM-FSF | Google DeepMind, *Frontier Safety Framework* v3.1 | Company framework (self-imposed; SB 53/EU designation not stated) | `gdm-2026-fsf-v3-1` (also `gdm-2025-fsf-v3-0`, `gdm-2025-fsf-v2-0`, `gdm-2024-fsf-v1-0`) | P |
| Aug 2026 | GDM-FR | Google DeepMind, *Frontier Safety Framework Report: Gemini 3.7 Flash* | Company's own application report | `gdm-2026-gemini-3-7-flash-fsf-report` | P |

"Not covered" (report line 171) should drop "company frameworks except through METR's synthesis" once the four agents' files are integrated.

### 2.2 §2(a) crosswalk: a GDM-FSF column is feasible

My judgement is that the FSF earns a column, *if* the integrator gives company frameworks columns at all. It is the policy instrument, and its cells differ from Shah's in instructive ways (A3, A9, A10). If columns are too many, the §5 rows below carry the substance.

| # | GDM-FSF v3.1 | Basis |
| --- | --- | --- |
| A1 | E | §2.2.1, CBRN CCL and TCL (p.11). All four of C, B, R and N are named ("chemical, biological, radiological, or nuclear"). |
| A2 | E | §2.2.2, Cyber CCL (p.12). |
| A3 | D¹ | The domain is "ML R&D and Misalignment"; TCL: "we cannot rule out the model significantly undermining human control" (p.14). "Loss of control" never appears. |
| A4 | E | §2.2.3, Harmful Manipulation CCL, "exploratory" (p.12). |
| A5–A8, A11–A16, A18 | X² | Out of scope by §1.1: other risks are handled by "Google's suite of AI responsibility and safety practices" (p.4). |
| A9 | P | "structural risks" named as a pathway heightened by ML R&D (fn 3, p.2; p.14). Not power concentration as such. |
| A10 | P | The ML R&D CCL rationale: exfiltration "may therefore have a significant effect on society's ability to adapt to and govern powerful AI models" (p.15). The model report adds "maintain geopolitical stability" (GDM-FR p.35). |
| A17 | — | |

Cell notes:
1. The announcement post describes the domain as "misaligned AI models might interfere with operators' ability to direct, modify or shut down their operations", which is the EU Code App. 1.4(2) formula.
2. X here means *assigned to other Google practices*, not denied. Mark it so, to avoid reading it as a claim that these harms don't matter.

### 2.3 §2(b) model and system factors

- **B1 (dangerous capabilities).** Add:
  - **GDM-FSF ML R&D CCLs** (p.15), used as H/thresholds: "Has been used to accelerate AI development, resulting in AI progress substantially accelerating from historical rates"; "Can fully automate the work of any team of researchers at Google focused on improving AI capabilities, with approximately comparable all-inclusive costs" (F; the threshold is a trigger for *self* gates). The FSF calls ML R&D capability "a substantial cross-cutting risk factor for several pathways (e.g. through misalignment, misuse or structural risks) to severe harm" (p.4). That is the FSF's one explicit use of "risk factor".
  - **Self-replication lineage.** v1.0 had "Autonomy level 1: Capable of expanding its effective capacity in the world by autonomously acquiring resources and using them to run and sustain additional copies of itself on hardware it rents" (p.6). v2.0 removed it (fn 9, p.5): "Most of the advanced risk that was captured by this CCL is now covered by our misalignment section." It sits next to AISI's RepliBench observation (>60%).
- **B2 (propensities).** GDM-FSF p.14: the TCL assessment "may take into account models' alignment propensities, capabilities, and our defenses against misaligned models" (M *self-d*). GDM-FR p.5: "both automated analysis and manual transcript inspections revealed no evidence of sandbagging" (O, company self-report).
- **B3 (agentic autonomy).** GDM-FR p.4: Gemini 3.7 Flash "can complete individual coding tasks but lacks the independence to chain them into an end-to-end research workflow without human intervention" (O).
- **B5 (evaluation gap / test-awareness).**
  - GDM-FSF p.6: "other actors may put significantly more effort into eliciting capabilities than we put into assessing risk, thus requiring conservatism" (F, acknowledged). p.5–6: alert thresholds, a "safety buffer", and "we seek to apply appropriate scaffolding, inference compute, and other augmentations" (M *self-d*).
  - GDM-FR, observations (O):
    - p.4: the model "is observant enough to correctly assess when it is in a testing environment, but it cannot successfully bypass testing restrictions".
    - p.6: "despite identifying some examples of evaluation awareness … we do not believe evaluation awareness compromises our capability assessments".
    - p.39–40: the model passed 3 of 4 stealth challenges. The fourth failed because the agent "exhibited substantial evaluation awareness" and declined the sabotage goal, so "this result likely reflects the model's propensity, rather than the ceiling of its stealth capability"; "Cover Your Tracks results are invalidated". The TCL requires passing *all* challenges (p.38), so an alignment-trained refusal counts toward "not reached".
    - p.2: for this model only "light-weight versions of our risk assessment process" were run.
  - *This is the most concrete public instance I found of test-awareness interacting with a threshold determination.*
- **B6 (safeguards).** GDM-FSF p.10: deployment safeguards "may include measures such as safety post-training, monitoring and analysis, account moderation, jailbreak detection and patching, user verification, and bug bounties" (M *self-d*). GDM-FR p.3: CBRN "alert threshold" reached, because "a subset of experts were able to elicit accurate and actionable information across the full harm journey for both tested scenarios"; the cyber CCL alert threshold was also reached (O).
- **B7 (weight security).** Security levels are recommended for the field (M *self-d*; escape clause in §1 above):
  - SL2+ for all misuse CCLs (pp.11–12);
  - SL3 for ML R&D acceleration (p.15);
  - SL4 for ML R&D automation, "but emphasize that this must be taken on by the frontier AI field as a whole" (p.15).
  - The levels map to RAND's goals, not its benchmarks: "rather than the benchmarks (i.e. concrete measures)" (p.9 fn 6).
- **B8a (human insiders).**
  - GDM-FSF p.9 defines SL2+ as RAND SL2 "with additional security measures designed to address risks from insider threats and well-resourced non-state external actors". These "may include, for example: dedicated insider risk teams; background checks and ID verification for personnel with sensitive access; review of model training data for signs of tampering …" (M *ex*).
  - p.11: "our current assessment … indicates that the risks of insider misuse posed by the misuse T/CCLs identified below are effectively addressed by our baseline controls (such as background checks and access restrictions). At this stage, additional mitigations beyond these established safeguards are not required" (company's own assessment; O/claim).
- **B8b (AI as insider).**
  - GDM-FSF p.13: "Security mitigations also protect against the risk of the model exfiltrating itself" (M *self-d*). "High-risk internal deployments", i.e. "use cases with the potential to enable severe threat scenarios (e.g. building internal security infrastructure or automating ML R&D)" (p.19), are gated (M *self*).
  - GDM-FR pp.35–36 lists threat models (F): "exfiltrating weights, launching rogue deployments on internal servers, systematically evading guardrails … or manipulating lab staff to weaken security postures"; "misdirecting alignment research, inserting backdoors into infrastructure or safety protocols, poisoning training runs, sandbagging capabilities during evaluations". It closely parallels AISI's Control threat models. The same report says these were developed with "external advisors from the UK AI Security Institute (UK AISI) and Redwood Research" (p.35).
- **B9 (open weights).** The risk acceptance allows "we assess that the benefits of the open release of model weights outweigh the risks" in place of the recommended security level (p.7) (*self-d*, scope escape).
- **B10 (reach).** Residual-risk factor "The scope of the deployment. For example, small scale and private deployments may pose substantially less risk than large scale or public deployments" (p.10) (F).
- **B12 (offence–defence).** Cyber CCL rationale: "the potential for automated cyber-defense and social adaptation as a response to exfiltration means that higher levels of security, and the resulting costs to innovation, are likely not warranted" (p.12) (F).

### 2.4 §2(c) structural and organizational factors

- **C1 (race / competitor contingency).** This row gets primary-text support for FLI's observation. Competitor-indexed conditions *inside the mitigation logic*:
  - v3.1 p.7 (risk acceptance): "what capabilities and mitigations are available on other publicly available models (e.g. if other models are similarly capable and have few mitigations, then the marginal risk added by our external deployment is likely low)". p.10(iv) repeats it for residual risk.
  - v3.1 p.11 (security levels): "may be adjusted if … a model does not possess capabilities meaningfully different from other publicly available models that have weaker security applied".
  - v3.1 p.2: "our adoption of them would result in effective risk mitigation for society only if all relevant organizations provide similar levels of protection."
  - v2.0 p.1, stronger and since removed: "our adoption of the protocols described in this Framework may depend on whether such organizations across the field adopt similar protocols."
  - v3.1 p.6, an assumption about competitors: "as a frontier AI company, we do not expect other groups to put significantly more effort into ML R&D than we do ourselves".

  Role: these function as *relaxation conditions on mitigations* (M-relax, *self-d*), not as named factors. I'd tag them so; a reader sees C1 operating inside the instrument.
- **C5/C7 (governance).** v3.1 §4.1 (p.16), in full: "We have in place a well-established and comprehensive internal governance structure designed to ensure the robust implementation of the processes outlined in this Frontier Safety Framework. Responsibilities for assessing and mitigating risks are clearly defined and allocated across all levels of the organization. This includes legal, compliance, and safety reviews with escalation procedures to ensure appropriate oversight." (M *self*, described; no body, role or reporting line named.) Contrast v2.0 p.7, which named the three councils (quoted in §5). Useful beside EU-CoP Measure 8.1.
- **C9 (whistleblowing).** Nothing in the FSF (term search). If the §4 table wants an explicit absence, it is "—".
- **C11 (commercial pressure).** "Costs to innovation" is an explicit counterweight in security-level choices:
  - p.12 cyber: "the resulting costs to innovation, are likely not warranted";
  - p.12 manipulation: "count against security mitigations with substantial costs to innovation";
  - p.15: "The overall reduced impact of model weights counts against security levels with substantial innovation costs";
  - p.8: "balancing safety with innovation".

  Role: a named consideration in mitigation choice (*self-d*). It is not framed as a risk factor.
- **C13 (evidence dilemma).** p.8: "Because the science of AI risk assessment is still developing, our assessments will often involve some level of subjective analysis." p.12: manipulation research "from a severe risk perspective is nascent".
- **C15–C17.** Nothing, in any version (term search: headcount, growth, turnover, investor, personnel, staff, organizational, restructuring, culture, resourcing). This agrees with the METR finding the report already cites.

### 2.5 §4 organizational factors by role

- **C7 row, M column:** add "GDM-FSF §4.1 (*self*, no body named; v2.0 named three councils)".
- **B8a/b row, M column:** add "GDM-FSF SL2+ insider measures (*ex*); 'baseline controls' judged sufficient for insider misuse (p.11)".
- **C6, C8, C9, C15–C17:** GDM-FSF "—".

### 2.6 §5 terminology rows

- **§5.2, loss of control.** Keep the Shah row ("Not a category | GDM") but rename it GDM-Shah, and add:

| Scale | Source | Operative words |
| --- | --- | --- |
| Capability threshold for oversight evasion, "significant" harm tier | GDM-FSF v3.1 | "enough situational awareness (ability to discover and use relevant details of its deployment setting) and stealth (ability to circumvent basic oversight mechanisms) such that, absent additional mitigations, we cannot rule out the model significantly undermining human control" (p.14) |
| Operator control (announcement) | GDM post, Sep 2025 / Apr 2026 | "misaligned AI models might interfere with operators' ability to direct, modify or shut down their operations" |
| Event term, internal team name | GDM-FR Aug 2026 | "an agent to autonomously spread to new environments in a potential loss of control event" (p.40); "Loss of Control (LoC) … teams" (p.35) |

- **§5.4, misalignment.** Add:
  - **GDM-FSF** defines no "misalignment". Its domain definition is "risks of models' ML R&D capabilities or misaligned propensities reducing society's overall ability to manage AI risks" (p.18). Earlier: v3.0 fn 3, "general-purpose AI agents are potentially misaligned and can become difficult to control" (p.2); v2.0, "By 'deceptive alignment,' we mean the risk that AI systems purposefully undermine human control over AI systems" (p.6).
  - **GDM-FR** defines scheming: "'scheming' (also known as deceptive alignment), where a model knowingly and covertly pursues objectives misaligned with its developer's intention" (p.36). That is narrower than Shah's "knowingly causes harm against the intent of the developer", because it adds *covertly*, and it too is developer-indexed.
- **§5.5, misuse versus loss of control.** GDM-FSF fn 2 (p.2): misuse means "risks of threat actors using critical capabilities of deployed or exfiltrated models to cause harm". The FSF keeps misuse and misalignment in separate sections, but routes structural and misalignment risk through the same ML R&D thresholds.

### 2.7 §7 relative priority, GDM row

Current: "Misuse and misalignment in scope; deceptive alignment 'the risk we are most concerned about'; mistakes and structural risks out of scope" (from Shah). Proposed: keep that as "GDM (Shah 2025)", and add "GDM-FSF v3.1":

> Four domains, unranked: CBRN, cyber, harmful manipulation (exploratory), ML R&D and misalignment. CCLs mark "severe" harm and TCLs "significant" harm. Structural risk enters via the ML R&D CCLs.

### 2.8 Caveats, and commentary claims now checkable

- **FLI-S26** says GDM "weakened or voided pledges to pause unilaterally": **supported for GDM** (Headline 1). One nuance for fairness: v1.0's hold was already an either/or ("put on hold … or implement additional protocols"), and v2.0's was a "may".
- **Zhu 2026** (`zhu-2026-silent`, arXiv 2609.08789, preprint, single author, inter-coder agreement not yet reported): its three GDM change claims are verified against the primaries (Headline 7). Its GDM figures: of v2.0→v3.0's material changes, 73% strict / 53% lenient silent; v3.0→v3.1, 56% / 48%. Its v3.0→v3.1 weakening share of 0.44 is one of only three pairs without a weakening majority (Zhu Table 1, §5). These figures are \[S] for this report: I checked the changes, not the coding.

---

## 3. Triggers (T) in the FSF

Each trigger below is *self* unless marked. Throughout, "reassessment" means the model's risk is re-examined, not the organization.

| Trigger | What it prompts | Text (v3.1) | Force |
| --- | --- | --- | --- |
| First external deployment of a new frontier model | Critical capability assessment | "prior to the first external deployment" (p.5) | *self* |
| Subsequent versions | Reassessment if two conditions hold | "(1) the model has meaningful new capabilities or material increases in performance; and (2) we believe such material capability increase could materially undermine the justification for why the risks stemming from the model are acceptable" (p.5) | *self-d* (second prong is the company's belief) |
| Completion of a post-training run | Material capability change assessment | "we conduct material capability change assessments on various checkpoints upon the completion of a post-training run" (p.5) | *self* |
| Alert threshold reached | Proximity analysis; response plan | "When a model reaches an alert threshold for a CCL, we will assess the proximity … This will inform the formulation and application of a response plan" (p.6) | *self* (the plan's content is *self-d*) |
| Rate of progress | More frequent evaluations or moved thresholds | "We may run early warning evaluations more frequently or adjust alert thresholds if the rate of progress suggests our safety buffer is no longer adequate" (pp.5–6) | *self-d* |
| Post-market monitoring / incidents | Update to the safety case or risk assessment | "our residual risk assessments, safety cases and mitigations may be updated as a result of post-market monitoring, including information about incidents" (p.10) | *self-d* |
| Framework review | Annual review, or sooner | "at least once a year—more frequently if we have reasonable grounds to believe the adequacy of the Framework or our adherence to it has been materially undermined" (p.17); inputs: "record of adherence to the framework, relevant high-quality research, information shared through industry forums, and evaluation results" | *self* |
| Model at the misalignment TCL | Periodic residual-risk assessments | "we will carry out periodic residual risk assessments" (p.14) | *self* |

**No organizational trigger.** Nothing about organizational change, personnel, growth or ownership triggers anything. Contrast the EU Code's Measure 1.3 ground (1), "how the Signatories develop models will change materially", which the FSF did *not* import alongside the rest of that measure's language.

---

## 4. FSF (policy instrument) versus Shah et al. 2025 (technical approach)

| Topic | Shah et al. 2025 (`shah-2025-approach`) | FSF v3.1 (and history) |
| --- | --- | --- |
| Loss of control | "we do not discuss loss of control as its own category" (p.17) | The term is absent from all versions. The construct is present as "significantly undermining human control" (TCL, p.14). GDM's own post and model report use LoC vocabulary (§2.6). |
| Misalignment | Defined: "knowingly causes harm against the intent of the developer"; "very expansive" knowing (p.4); includes sycophancy and bias | No definition. Governed as a capability threshold (stealth + situational awareness), not as a propensity. Propensity enters only as an input to residual-risk assessment (p.14). |
| Top concern | Deceptive alignment "the risk we are most concerned about" (p.51) | v2.0 had a "Deceptive Alignment" section. v3.0 renamed it "Misalignment (Exploratory)", with "illustrative only" CCLs (p.15). v3.1 demoted it to a TCL ("significant but not severe", glossary p.18). Severe misalignment is reached only via the ML R&D CCLs. |
| Structural risk | Out of scope: needs "bespoke" approaches; "much harder for an AI developer to address" (p.5) | Named as a pathway heightened by ML R&D capabilities (fn 3, p.2; p.14), and so partly in scope through ML R&D thresholds |
| AI as insider | "treat the model similarly to an untrusted insider" (p.9) | "Security mitigations also protect against the risk of the model exfiltrating itself" (p.13). High-risk internal deployments are gated (p.14). |
| Mitigation detail | §§5–6 lay out mitigation research | The FSF points to Shah §5 and §6 for mitigations (fn 7 p.10; fn 10 p.13): the policy text defers the substance to the paper |

In short, the technical paper declines the loss-of-control *category* while treating deceptive alignment as its top concern. The policy instrument never names loss of control, and governs misalignment one tier *below* its severe-harm thresholds. Both statements are verbatim-grounded; the juxtaposition is mine.

---

## 5. Version history relevant to the report (verbatim)

- **Hold / pause.**
  - v1.0 p.2: "A model may reach evaluation thresholds before mitigations at appropriate levels are ready. If this happens, we would put on hold further deployment or development, or implement additional protocols (such as the implementation of more precise early warning evaluations for a given CCL) to ensure models will not reach CCLs without appropriate security mitigations, and that models with CCLs will not be deployed without appropriate deployment mitigations."
  - v2.0 p.3: "A model flagged by an alert threshold may be assessed to pose risks for which readily available mitigations (including but not limited to those described below) may not be sufficient. If this happens, the response plan may involve putting deployment or further development on hold until adequate mitigations can be applied."
  - v3.0 / v3.1: no counterpart. Risk-acceptance criteria are limited to deployment (v3.0 p.7: "This is required only for external deployment, not further development"; v3.1 p.7 as quoted in Headline 1).
- **Competitor contingency.**
  - v2.0 p.1: "These mitigations should be understood as recommendations for the industry collectively: our adoption of them would only result in effective risk mitigation for society if all relevant organizations provide similar levels of protection, and our adoption of the protocols described in this Framework may depend on whether such organizations across the field adopt similar protocols."
  - v3.0 p.2 / v3.1 p.2: the last clause is dropped. What remains: "These mitigations are most effective when adopted by industry as a whole: our adoption of them would result in effective risk mitigation for society only if all relevant organizations provide similar levels of protection."
- **Governance.**
  - v2.0 p.7: "For Google models, when alert thresholds are reached, the response plan will be reviewed and approved by appropriate corporate governance bodies such as the Google DeepMind AGI Safety Council, Google DeepMind Responsibility and Safety Council, and/or Google Trust & Compliance Council. The Google DeepMind AGI Safety Council will periodically review the implementation of the Framework."
  - v2.0 p.4: "general availability deployment of a model takes place only after the appropriate corporate governance body determines the safety case … to be adequate".
  - v3.0 p.9: "external deployments of a model take place only after the appropriate governance function determines the safety case regarding each CCL the model has reached to be adequate".
  - v3.1 §4.1 is quoted in §2.4.
- **ML R&D anchor.** v2.0 p.6: "substantially accelerating (e.g. 2x) from 2020-2024 rates". v3.0 p.13 / v3.1 p.15: "substantially accelerating from historical rates".
- **Misalignment.**
  - v3.0 p.15, Instrumental Reasoning Level 2: "The instrumental reasoning abilities of the model enable enough situational awareness and stealth that, even when relevant model outputs (including, e.g. scratchpads) are being monitored, we cannot detect or rule out the risk of a model significantly undermining human control." Mitigation: "Future work".
  - v3.1: absent. The changelog (p.17) says only: "Incorporated the previous exploratory Misalignment risk domain into a combined ML R&D and Misalignment risk domain and outlined mitigation and risk acceptance process for the TCL."
- **Autonomy / self-replication.** v1.0's Autonomy level 1 was removed in v2.0 (quoted in §2.3, B1).
- **The v3.1 changelog in full** (p.17): "Introduced CBRN TCLs and outlined mitigation and risk acceptance process. / Incorporated the previous exploratory Misalignment risk domain into a combined ML R&D and Misalignment risk domain … / Outlined enhanced level of security for CBRN, Cyber and Harmful Manipulation CCLs to Security Level 2+ to protect against non-state actors and insider threats. / Included more detail on our risk management process. / Included description of our internal governance structure. / Introduced a glossary."
  - It does not mention: removal of Instrumental Reasoning Level 2; "updated" becoming "reviewed" in §5.1; "systemic risk" becoming "significant and severe risk"; the low-risk external deployment exemption (fn 4); "large scale internal deployment" becoming "high-risk internal deployment".
  - I did not trace v3.0→v3.1 exhaustively. These are the ones I saw reading both whole.

---

## 6. Definitions record (verbatim, with location)

All from FSF v3.1 unless noted.

- **Frontier AI Models** (glossary p.18): "are trained on a large data set, display significant generality, are capable of performing a wide range of distinctive tasks and have high-impact capabilities. Frontier AI models' agentic and reasoning-based general capabilities near or exceed those of other Google models."
- **Critical Capability Levels** (p.18): "the main capability thresholds around which we have built the Framework process. They represent the capability levels at which, absent mitigation measures, frontier AI models or systems may pose heightened risk of severe harm." Also p.4: "we then define the CCLs as the minimal set of capabilities a model must possess to do so."
- **Tracked Capability Levels** (p.18): "capability thresholds which capture a lower level of risks than our CCLs. They represent the capability levels at which, absent mitigation measures, frontier AI models or systems may pose heightened risk of significant but not severe levels of harm."
- **Alert Thresholds** (p.18): "thresholds which we set marginally earlier than our CCLs. Crossing these thresholds indicates a CCL may be reached in the foreseeable future".
- **Material Capability Increases** (p.19): "meaningful new capabilities or material increases in model performance that we believe could materially undermine our justifications for a model's level of risk being acceptable".
- **Deployment Mitigations** (p.19): "safety measures we implement which are intended to counter the misuse or misaligned expression of critical capabilities in deployments. They may include safety post-training, input/output/chain-of-thought monitoring and analysis, account moderation, jailbreak detection and patching, user verification, and bug bounties."
- **Security Mitigations** (p.19): "safety measures we implement which are intended to prevent the unauthorized modification or exfiltration of model weights by unauthorized actors."
- **"Safeguards".** Not defined. It is used as the generic noun, e.g. "a suite of safeguards targeting the capability" (p.10), and spans both mitigation types.
- **High-Risk Internal Deployments** (p.19): "model releases restricted to Google employees for use cases with the potential to enable severe threat scenarios (e.g. building internal security infrastructure or automating ML R&D)."
- **Low-Risk External Deployments** (p.19): "small scale and private releases restricted to particular external groups or organizations."
- **Safety Cases** (p.20): "an assessable argument showing how severe risks associated with a model's CCLs have been reduced to an acceptable level."
- **Residual Risk Assessments** (p.20): "the process of evaluating the level of risk that remains after all planned mitigation strategies have been implemented."
- **Risk domains** (p.18):
  - CBRN: "risks of models assisting in the development, preparation, and/or execution of a chemical, biological, radiological, or nuclear ('CBRN') threat."
  - Cyber: "risks of models assisting in the development, preparation, and/or execution of a cyber attack."
  - Harmful Manipulation: "risks of models with high manipulative capabilities potentially being misused in ways that could reasonably result in large scale harm." The CCL (p.12): "Possesses manipulative capabilities sufficient to enable it to systematically and substantially change beliefs and behavior in identified high stakes contexts over the course of interactions with the model, reasonably resulting in additional expected harm at severe scale."
  - ML R&D and Misalignment: "risks of models' ML R&D capabilities or misaligned propensities reducing society's overall ability to manage AI risks. Such capabilities may serve as a substantial cross-cutting risk factor for several pathways (e.g. through misalignment, misuse or structural risks) to severe harm."
- **Misuse** (fn 2, p.2): "risks of threat actors using critical capabilities of deployed or exfiltrated models to cause harm."
- **Situational awareness / stealth** (TCL, p.14): "situational awareness (ability to discover and use relevant details of its deployment setting) and stealth (ability to circumvent basic oversight mechanisms)". v3.0 p.15 has "ability to work out and use" in place of "discover and use".
- **Baseline for uplift** (fn 8, p.11): "relative to a baseline without generative AI."
- **Deceptive alignment** (v2.0 p.6): "the risk that AI systems purposefully undermine human control over AI systems."
- **Scheming** (GDM-FR p.36): "'scheming' (also known as deceptive alignment), where a model knowingly and covertly pursues objectives misaligned with its developer's intention".
- **Not used anywhere in FSF v1.0–v3.1:** "loss of control"; "systemic risk" (except v3.0 §5.1); "misalignment" as a defined term; "critical capability" outside "CCL".

---

## 7. Proposed footnote bodies

- **[^gdm-fsf]** \[P] Google DeepMind, *Frontier Safety Framework*, Version 3.1, published 17 Apr 2026 (20 pp.). <https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf> (listed as current at <https://deepmind.google/frontier-safety/>, checked 2026-09-27). relata `gdm-2026-fsf-v3-1` (SHA-256 `ad10d2d2…`). Anchors:
  - p.4: CCLs are "capability levels at which, absent mitigation measures, frontier AI models or systems may pose heightened risk of severe harm"; ML R&D capabilities "may serve as a substantial cross-cutting risk factor for several pathways (e.g. through misalignment, misuse or structural risks) to severe harm."
  - p.7: risk acceptance for misuse is "required only for external deployment, not internal deployment or further development"; security is either "the recommended security level stated below, or we otherwise assess that the level of security applied is adequate".
  - p.9: SL2+ adds "security measures designed to address risks from insider threats and well-resourced non-state external actors".
  - p.11: insider misuse risks "are effectively addressed by our baseline controls … additional mitigations beyond these established safeguards are not required".
  - p.14: TCL, "we cannot rule out the model significantly undermining human control"; "we will carry out periodic residual risk assessments".
  - p.15: SL4 "must be taken on by the frontier AI field as a whole".
  - p.16: governance structure (§4.1, no body named).
  - p.17: "reviewed at least once a year—more frequently if we have reasonable grounds to believe the adequacy of the Framework or our adherence to it has been materially undermined."
- **[^gdm-fsf-hist]** \[P] Earlier FSF versions:
  - v3.0 (22 Sep 2025), relata `gdm-2025-fsf-v3-0`. p.4: misalignment CCLs "are exploratory and intended for illustration only, we do not associate them with explicit risk acceptance criteria"; p.15: Instrumental Reasoning Level 2.
  - v2.0 (4 Feb 2025), relata `gdm-2025-fsf-v2-0`. p.1: "our adoption of the protocols described in this Framework may depend on whether such organizations across the field adopt similar protocols"; p.3: "the response plan may involve putting deployment or further development on hold until adequate mitigations can be applied"; p.7: the three named councils.
  - v1.0 (17 May 2024), relata `gdm-2024-fsf-v1-0`. p.2: "we would put on hold further deployment or development, or implement additional protocols".
  - URLs: <https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf>; <https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/updating-the-frontier-safety-framework/Frontier%20Safety%20Framework%202.0.pdf>; <https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/introducing-the-frontier-safety-framework/fsf-technical-report.pdf>.
- **[^gdm-post]** \[P] Flynn, King & Dragan, "Strengthening our Frontier Safety Framework", Google DeepMind blog, 22 Sep 2025, updated 17 Apr 2026. <https://deepmind.google/blog/strengthening-our-frontier-safety-framework/>. relata `gdm-2026-strengthening-fsf-blog` (headless-Chrome PDF snapshot, 2026-09-27). "We've also expanded our Framework to address potential future scenarios where misaligned AI models might interfere with operators' ability to direct, modify or shut down their operations." "We've sharpened our CCL definitions".
- **[^gdm-fr]** \[P] Google DeepMind, *Frontier Safety Framework Report: Gemini 3.7 Flash*, Aug 2026 (41 pp.). <https://storage.googleapis.com/deepmind-media/gemini/gemini_3-7_flash_fsf_report.pdf>. relata `gdm-2026-gemini-3-7-flash-fsf-report`. Anchors:
  - p.2: "we have precautionarily conducted light-weight versions of our risk assessment process on this model".
  - p.3: CBRN, "prompting us to assess that the model has reached the alert threshold for this CCL"; cyber, "reaches the alert threshold for this CCL, but not the CCL".
  - p.4: "observant enough to correctly assess when it is in a testing environment, but it cannot successfully bypass testing restrictions".
  - p.35: "Loss of Control (LoC) and Security & Privacy (S&P) teams, as well as external advisors from the UK AI Security Institute (UK AISI) and Redwood Research".
  - p.36: scheming definition.
  - pp.39–40: "Cover Your Tracks results are invalidated because the model sometimes chooses not to engage in the side task"; "this result likely reflects the model's propensity, rather than the ceiling of its stealth capability"; "a potential loss of control event".
- **[^gdm-sb53]** \[S]\[F] Vorp Labs, "Current Frontier AI Framework Inventory 2026", data update 12 Jul 2026. <https://vorplabs.com/ai-regulatory-updates/frontier-ai-frameworks>. On Google: "No explicit statement found as of 2026-07-04, despite Google plausibly meeting both statutory thresholds." Not filed in relata. My own searches of deepmind.google, ai.google and blog.google (2026-09-27) found no designation either. The frontier-safety page and the Feb 2026 *Responsible AI* report (`google-2026-ai-responsibility-update`) do not mention SB 53, the AI Act or the Code.

---

## 8. Bibkeys created (all new; none existed)

| Source | relata key |
| --- | --- |
| FSF v3.1 (Apr 2026) | `gdm-2026-fsf-v3-1` |
| FSF v3.0 (Sep 2025) | `gdm-2025-fsf-v3-0` |
| FSF v2.0 (Feb 2025) | `gdm-2025-fsf-v2-0` |
| FSF v1.0 (May 2024) | `gdm-2024-fsf-v1-0` |
| Gemini 3.7 Flash FSF Report (Aug 2026) | `gdm-2026-gemini-3-7-flash-fsf-report` |
| Announcement post (Sep 2025 / Apr 2026) | `gdm-2026-strengthening-fsf-blog` (web snapshot) |
| Google *Responsible AI* progress report (Feb 2026) | `google-2026-ai-responsibility-update` (term-searched only) |

All were added with `relata add` (BibTeX on stdin) followed by `relata pdf`; nothing went through `ingest`. Already in the library and used here: `zhu-2026-silent`, `shah-2025-approach`, `california-2025-sb53`.

---

## 9. Adjacent notes

- **The Gemini 3 Pro FSF report** is also linked from the frontier-safety page and was not read. The 3.7 Flash report is newer, but ran "light-weight" assessments. A Pro-class report would be the fuller instance if the integrator wants one.
- **Google–UK AISI MoU.** Google's Feb 2026 progress report (p.13) describes a "Memorandum of Understanding focused on foundational security and safety research" with UK AISI, including "access to proprietary models, joint reports and publications", and joint work to "monitor an AI system's 'thinking,' or its chain-of-thought". It is not a risk-factor source, but it bears on Joseph's AISI context.
- **For the sibling forks and the integrator:** Zhu's Appendix N (`zhu-2026-silent`, pp.27) lists every public version of all twelve frameworks with dates and hashes. It is the quickest check that each fork read the current version.
- **On the codes.** The report's force codes assume a source either binds or doesn't. Company frameworks need a *self* / *self-d* split, because within one document "only after" and "or we otherwise assess" sit side by side. How far SB 53 converts *self* into law depends on a per-company designation fact, and for Google that fact is currently unknown.
