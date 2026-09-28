# Anthropic's and OpenAI's own models of risk

*By the agent that wrote `source-atlas/co-anthropic-openai.md`, 2026-09-28. Each model is described on its own terms. Line references are to the atlas extractions (`src-text/<key>.txt`; key prefixes are dropped where unambiguous). Quotes are verbatim. My own readings are marked as mine. I am an Anthropic model reading Anthropic's documents, and I have tried to apply the same scrutiny to both companies. Where the scrutiny points somewhere uncomfortable, it is said plainly in the "Scrutiny" subsections.*

## At a glance

| | **Anthropic** (RSP + Risk Reports + FCF) | **OpenAI** (Preparedness Framework + FGF) |
|---|---|---|
| **Organising idea** | v2.2: *if a capability threshold is reached, then the required safeguards must be in place.* v3: *argue* that risk is low, and report the risk level whatever it is. | *If a tracked capability reaches High or Critical, then safeguards must "sufficiently minimize" the risk*, before deployment (High) or also during development (Critical). |
| **What is named** | Threat models (4 in v3), capability thresholds, safeguards (deployment/security), "risk mitigations", risk levels, the marginal/absolute distinction. | Tracked Categories (3), Research Categories (5), capability thresholds (High/Critical), safeguard *claims*, residual risk, severe harm. |
| **Levels** | v2.2: ASL-2/3/4 standards, with CBRN-3/4 and AI R&D-4/5 thresholds. v3: four named threshold rows. Risk Reports: CB-1/CB-2, verbal risk grades, robustness Level 1/2/3 (ASL wording retired). FCF: Tier 1/2 per category. | High / Critical (v1 also had Low/Medium, since removed). FGF: Tier 1/2/3 per category. |
| **Core argument form** | Risk Reports. Feb: four claims plus eight pathways, with mitigating factors graded strong/moderate/weak. Aug: formal decomposition R = Σ P·H·U over three misalignment types, filled with verbal grades and adjusted for uncertainty. | Capabilities Report (evaluations against "indicative thresholds", plus holistic judgment) and Safeguards Report (each harm vector covered by one or more claims). SAG recommends; leadership decides. |
| **Voluntary / statutory split** | RSP: "catastrophic risk", "plain meaning", no number; 4 threat models; covers internal models. FCF: "systemic risk", >50 deaths or $1B; 4 statutory categories (cyber, CBRN, manipulation, loss of control), 2 tiers each; mainly externally deployed models. | PF: "severe harm" = thousands of deaths or hundreds of billions of dollars; 3 categories. FGF: "systemic risk", >50 deaths or $1B; 4 statutory categories, 3 tiers each, with examples. |
| **Stated method / lineage** | METR's RSP proposal; "inspired by safety case methodologies" (v2.2); v3 moves to "strong argument", which Karnofsky calls "FDA-inspired". RAND security levels. FCF: ISO 42001, NIST 800-53, CSA. | "Holistic risk assessment"; five tracking criteria (informed by Meta's framework); Capability/Safeguards Reports "parallels Anthropic's updated RSP". FGF: ISO 42001, NIST AI RMF, METR. |
| **Purpose / audience / force** | Voluntary; internal procedure plus public signal plus "prototype" for regulation. v3 separates company plans (committed), industry recommendations (not unilateral) and Roadmap goals ("not hard commitments"). FCF is the legal document. | Voluntary; "We won't deploy these very capable models until we've built safeguards." SAG advises, Leadership decides, the Board's SSC oversees. FGF is the legal document. |
| **Uncertainty** | "act as though" (v2.2); "zone of ambiguity"; "provisionally meeting… to err on the side of caution"; verbal grades; "very low" raised to "low" to reflect uncertainty. | Elicitation is "a lower bound, rather than a ceiling"; "cannot rule out Critical"; "precautionarily treated as High"; indicative thresholds plus "holistic judgment". |
| **Excludes** | Risks outside four threat models (Usage Policy and societal impacts handle others); v3 drops radiological/nuclear and cyber as RSP threat models; persuasion "not yet sufficiently understood" (v2.2); scoped-out misalignment concerns (Aug §2.17). | Anything below "severe harm"; anything not *plausible, measurable, severe, net new, instantaneous or irremediable*; persuasion moved out of the PF; nuclear/radiological made a Research Category. |

---

# Part A. Anthropic

## A1. The pieces and how they fit

```
Responsible Scaling Policy (voluntary)            Frontier Compliance Framework (statutory: TFAIA, EU CoP)
 ├─ §1 threshold table:                            ├─ "systemic risk" (>50 deaths / $1B)
 │    threshold | company plan | industry rec.    ├─ 4 categories × Tier 1/2
 ├─ Appendix A: competitor-contingent commitments  │    (Loss of Control Tier 1/2 = RSP autonomy rows,
 ├─ §2 Frontier Safety Roadmap (goals, dated)      │     verbatim)
 ├─ §3 Risk Reports (every 3–6 months)  ─────────► ├─ incident ladder (AI Event → … → Critical Safety Incident)
 │    ├─ per threat model: threat model / models / └─ model reports, change management
 │    │  capabilities / mitigations / overall risk
 │    │  (marginal + absolute) / looking forward
 │    ├─ cross-cutting: acceleration, benefits,
 │    │  risk–benefit determination, safety-process failures
 │    └─ external review (at "highly capable" + "significantly redacted")
 └─ §4 Governance (RSO, noncompliance, Board/LTBT)
```

System cards sit beside all of this, per model. Since v3 the Risk Reports carry the overall assessment (RSP v3.0 L78–85).

## A2. The v2.2 model: capability-triggered safeguard standards

v2.2 (May 2025) is the classic RSP. Its sentence-level core is:

> "A Capability Threshold tells us **when** we need to upgrade our protections, and the corresponding Required Safeguards tell us **what standard** should apply." (rsp-v2-2 L215–216)

> "A Capability Threshold is a prespecified level of AI capability that, if reached, signals (1) a meaningful increase in the level of risk if the model remains under the existing set of safeguards and (2) a corresponding need to upgrade the safeguards to a higher ASL Standard." (L216–219)

The **ASL Standards** are sets of measures, split into *Deployment Standards* ("ensure the safe usage of AI models by external users… as well as internal users") and *Security Standards* ("protect AI models–particularly their weights") (L180–188). Earlier versions had used "ASL" for models as well; v2.0 narrowed it to safeguards only (changelog L980–983).

| Capability | Threshold | Required safeguards |
|---|---|---|
| CBRN | **CBRN-3**: "significantly help individuals or groups with basic technical backgrounds (e.g., undergraduate STEM degrees) create/obtain and deploy CBRN weapons" | ASL-3 Deployment + ASL-3 Security |
| CBRN | **CBRN-4**: "substantially uplift CBRN development capabilities of moderately resourced state programs" | "We expect this threshold will require the ASL-4… We plan to add more information… in a future update" |
| AI R&D | **AI R&D-4**: "fully automate the work of an entry-level, remote-only Researcher at Anthropic" | ASL-3 Security + an "affirmative case" about misaligned-goal risks |
| AI R&D | **AI R&D-5**: "cause dramatic acceleration in the rate of effective scaling" | "At minimum, the ASL-4 Security Standard" |

(L239–276; detailed definitions in Appendix C, L913–963. AI R&D-5 is operationalised as ~1000× effective compute in a year, L934–939.) Cyber was an "ongoing assessment" capability with no threshold (L310–320). There was also a "Model Autonomy checkpoint" (2–8 hour software tasks), which replaced the earlier autonomous replication and adaptation (ARA) threshold (L284–295, L985–991).

**Procedure.** Preliminary assessment → comprehensive assessment ("make a compelling case", L369–388) → Capability Report → CEO + Responsible Scaling Officer (RSO) decide → Board and LTBT informed (L426–441). If the required showing cannot be made: "we will act as though the model has surpassed the Capability Threshold" (L443–444). If the safeguards cannot be met: interim measures, then "stronger restrictions" (de-deploy, "delete model weights"), and pretraining is paused (L653–678).

**The escape clause** is in a footnote: if another actor passes a threshold without equivalent safeguards, "we might decide to lower the Required Safeguards" while acknowledging the risk and advocating regulation (fn 17, L791–797).

## A3. The v3 model (Feb 2026, now v3.4): a threshold table, arguments, and reported risk

**The stated reason for restructuring** is collective action:

> "Our previous RSP committed to implementing mitigations that would reduce our models' absolute risk levels to acceptable levels, without regard to whether other frontier AI developers would do the same. But from a societal perspective, what matters is the risk to the ecosystem as a whole… the developers with the weakest protections would set the pace." (rsp-v3-0 L58–64)

The announcement adds its own diagnosis: a "zone of ambiguity" in which evaluations can neither show risk is low nor show it is high (rsp-v3-announcement L130–147), an anti-regulatory climate, and higher-level requirements "very hard to meet unilaterally" (L171–173).

**The new structure** is a three-column table: *"Capability or usage threshold" | "our plan as a company" | "ambitious industry-wide recommendations"* (v3.0 L171; v3.4 L175–385). The header says "or usage": one row is about deployment situations, not capabilities. The four rows (v3.4 wording):

1. **Non-novel chemical/biological weapons production** (the CBRN-3 descendant).
2. **Novel chemical/biological weapons production.** v3.3 rewrote it as "functionally substitute for the scarce human expertise that is currently the primary barrier to novel development…" (risk-report-aug L510–522).
3. **Misaligned AI systems in high-stakes settings** (named "High-stakes sabotage opportunities" in v3.0): "AI systems that are highly relied on and have extensive access to sensitive assets as well as moderate capacity for autonomous, goal-directed operation and subterfuge—such that it is plausible these AI systems could… carry out sabotage leading to irreversibly and substantially higher odds of a later global catastrophe" (v3.0 L232–253).
4. **Automated R&D in key domains.** "fully automate, or otherwise dramatically accelerate, the work of large, top-tier teams of human researchers in domains where fast progress could cause threats to international security and/or rapid disruptions to the global balance of power." Evaluations focus on AI R&D. v3.4 operationalises it as full substitution for "our entire set of Research Scientists and Research Engineers, at competitive costs (i.e., within a factor of 5)" **or** "double the rate of progress" substantially attributable to automation (risk-report-aug L467–483). Its stated intent: "the onset of dramatic recursive self-improvement, and has proven difficult to operationalize" (v3.4 L945–946).

Every industry-recommendation cell has the same form: **"A frontier developer should make a strong argument that…"** (v3.0 L175, L215, L232, L271). The company-plan cells are unilateral commitments, several of them modest ("maintain or improve on our ASL-3 protections"). Two other elements complete the model:
- **Appendix A**: commitments that trigger on judgments about competitors ("Anthropic in the lead" → "delay AI development and deployment as needed"; "General upleveling" → match a competitor's better mitigation, "not necessarily delay") (v3.4 L743–800).
- **v3.1's addition**: "we would strongly consider pausing… even in cases not covered below" (v3.4 L748–752).

**Why ASLs were demoted:**

> "when defining the risk mitigations needed for future levels of AI capability, we have found that providing a specific list of controls is overly rigid, and we instead prefer to focus on what sort of argument an AI developer should make (and what sorts of actors it should address)" (v3.0 L733–735)

The August Risk Report drops the ASL wording altogether:

> "our models and safeguards now vary along many dimensions, so we are no longer using this terminology" (risk-report-aug fn 59, L5385–5388)

It replaces it with robustness **Level 1/2/3** and "coverage" for classifiers (L5365–5376, L5465–5505).

**Scrutiny: how the if-then changed, in the company's and its critics' words.** v2.2's high-level "then" clauses (ASL-4 at CBRN-4 and AI R&D-5) were never specified, and v3 restructured before they would bind. Karnofsky, who led the rewrite, states the reason directly:
- "The company's leadership expects a reasonable probability of capabilities that would likely cross these thresholds within the next 2 years. I don't believe there is a plausible path to achieving that kind of robustness on that kind of time frame, except by either pausing AI development (potentially for years), or…" (karnofsky L383–389).
- On the old design's effect on assessment: "there was an enormous amount of pressure to declare our systems to lack relevant capabilities… I don't think we have actually made unreasonable calls, but I have felt the pressure" (L426–434).

Williams and Freund (GovAI) read the change as "the baseline for future mitigations" shifting: "Under the old RSP, Anthropic started from a high level of mitigations and would only lower them if competitors weren't adopting similar ones. Under the new RSP, Anthropic starts from a lower level and will only adopt stronger ones if other companies do or if Anthropic has a clear lead" (williams L247–252). Whether the old pause commitment was ever binding is disputed (karnofsky L15–31 vs the habryka thread L1214–1241; williams fn 5 L507–515). v3's changelog entry gives no reasons in the document itself; it points elsewhere (v3.0 L855–857).

## A4. The Risk Reports: how the argument works

The genre is specified by RSP §3.3 (v3.4 L465–537). For each threat model the report must give:
- factual information (threat model identification and specification, evidence, mitigations);
- a "threat-specific risk assessment" of "remaining absolute risk–i.e., the leftover risk after accounting for our mitigations";
- an overall assessment;
- a "risk-benefit determination";
- a review of past decisions;
- and, when the case rests partly on others' behaviour, a "marginal risk and ecosystem analysis" (v3.0 L443–491).

Karnofsky states the intended difference from a safety case: "Rather than a 'safety case' whose premise for existence is that we have met a particular standard, a Risk Report is simply supposed to characterize the current level of risk, whatever it is" (karnofsky L597–599).

**Standing features, in both reports:**

- **Two perspectives on every risk level.** "a) The level of risk our systems impose over and above the risks posed by other AI developers' systems (that is, a description of the 'marginal' risk…); and b) The level of risk that would be imposed industry-wide, if all AI developers had models and practices similar to ours (… the 'absolute' risk…)" (risk-report-feb L260–268).
- **Per-threat-model template**: Threat, Role of AI, Potential magnitude of impact, Likelihood of impact, Why this is a priority (Feb L463–507; L2715–2780).
- **A verbal risk scale** that is never converted to numbers:

| Threat model | Feb 2026 | Aug 2026 |
|---|---|---|
| Sabotage / misalignment in high-stakes settings | "Very low but not negligible" (Feb L414–416) | "Low (an increase from our previous assessment of 'very low'…)" (Aug L344–346) |
| Automated R&D | "Very low" (Feb L414) | "Low" (Aug L389–393) |
| Non-novel CB (CB-1 in Aug) | "Very low but not negligible" | "Low, but higher than our previous estimate" (Aug L436–442) |
| Novel CB (CB-2 in Aug) | "Low risk, but with substantial uncertainty" | same (Aug L436–437) |

- **Quantified anchors in footnotes**, used to define words. "Very large increase" is defined as "a 50%+ proportional increase in the likelihood of a transformative global catastrophe" (Feb fn 2–3, L514–520). "Expected damages" is defined as "the probability of each potential harm times the size of the harm, summed over all potential harms. We sometimes create rough estimates… and other times simply reason informally" (Feb fn 41, L4011–4016).

**February (sabotage): claims plus pathways.**
- Four claims: prior expectations; alignment assessment; the model's inability to undermine that assessment; limited opaque reasoning (Feb L577–607). "No one of these claims is sufficient… but in light of the full range of evidence…" (L588–590).
- Eight pathways. These are intermediate outcomes, not catastrophes: "we find it more productive to focus on intermediate unwanted outcomes in which sabotage by an AI system creates the conditions for a later catastrophic outcome" (L1481–1487).
- Each pathway gets frequency and complexity ratings and mitigating factors graded **Strong / Moderate / Weak** (table L1561–1609).

**August (misalignment): a formal decomposition.** It is preceded by a defined vocabulary (§2.5, L843–987; "tentative", fn 12). Central definitions:
- *Misalignment* is "a latent property of a specific computation performed by a model in a given context", judged against what "a reasonable person with full understanding… would consider unethical, illegal, clearly objectionable, or inconsistent with the model's constitution" (L846–850).
- *Misalignment risk* is "the expected total unmitigated harm induced by misaligned computations produced by covered models" (L969–971).

```
R  (covered risk: naturally-emerging misalignment, via the named pathways)
 = R_K (known) + R_P (unknown severe pervasive) + R_C (unknown severe context-dependent)
 = P_K·H_K·U_K + P_P·H_P·U_P + P_C·H_C·U_C
     P = probability of that misalignment type
     H = expected pre-mitigation harm given occurrence
     U = fraction of harm unmitigated
R_total = R + a (non-covered pathways; Claim 7 "threat modeling is sufficient")
            + b (engineered misalignment; Claim 8 "low")
```
(L993–1073)

- **Grades, not numbers.** Each factor gets a verbal grade (Table 2.4.A, L821–839: e.g. known misalignment: probability "High (observed)", harm "Low", unmitigated "Low").
- **Aggregation is labelled**, as "conjunctive", "disjunctive" or "convergent", with the caveat that correlated subclaims make naive products wrong (L977–986).
- **The conclusion is adjusted outside the argument:** "Covered risk is therefore very low based on these claims, but in an abundance of caution we assess risk to be only low due to increased uncertainty" (L1055–1056), "in light of recent disclosures" (L1063–1064).
- **Scrutiny: the adjustment's basis is contested inside the document.** The Claude model asked to review the section says those incidents "involved other developers' systems… the update is about industry-wide uncertainty rather than new adverse evidence about the covered models" (L2982–2988). The company answers that some of the uncertainty comes from its own systems (L3004–3011).

**CB sections argue differently.** They lean on threat variants, evidence weighting and a stated assumption with a fallback:
- the stated assumption and fallback: "If our core assumption is wrong and short interactions do confer significant uplift, our safeguards still provide meaningful risk reduction… However, our confidence… is lower" (Feb L3164–3202; Aug L4970–4999);
- the evidence-weighting policy: "significant weight on subjective impressions from our internal biology experts… even when we do not have clear numerical evidence" (Aug L5056–5061).

## A5. Voluntary / statutory division

The FCF says what it is for: "the FCF is our compliance framework for various applicable regulatory regimes" (FCF L59–61). The RSP "will remain our voluntary safety framework, reflecting what we believe best practices… should be… even when that goes beyond or otherwise differs from current regulatory requirements" (FCF L55–58).

| | RSP / Risk Reports | FCF |
|---|---|---|
| Severity term | "catastrophic risk" in "its plain meaning rather than… any specific statutory definition" (v3.0 fn 1, L137–141) | "systemic risk": "foreseeable and material risks of large-scale harm… including but not limited to >50 fatalities arising from a single incident, or 1 billion dollars of financial damages" (FCF L118–121); fn 1 notes the RSP's different sense (L76–79) |
| Categories | Non-novel CB, novel CB, misalignment in high-stakes settings, automated R&D | Cyber offense, CBRN, harmful manipulation, loss of control (L138–148) |
| Levels | Threshold rows; verbal risk grades | Tier 1 / Tier 2 per category (L199–391) |
| Scope | Includes internal models; Risk Reports "not scoped to a single AI model… a risk assessment of Anthropic's activities as a whole" (Feb L207–209) | "currently apply to models in scope… that are deployed externally"; internal use partly covered (L91–98) |
| Method language | Arguments, verbal grades | "we estimate the probability and severity of harm" (L159–160); "quantifies"; "clear measurable thresholds" (L203–205, L236–239) |

Two features of the FCF:
- **It files RSP content under statutory labels.** Its "Loss of Control" Tier 1 and Tier 2 are the RSP's misalignment and automated-R&D rows, verbatim (FCF L344–391), and its changelog records edits "to align with updates to Anthropic's Responsible Scaling Policy (v3.4)" (L711–714). The heading says "Loss of Control" (L314); the changelog says "Sabotage and Loss of Control" (L712, L718).
- **Scrutiny.** The FCF describes its tiers as "clear measurable thresholds" that "quantify" (L203–205, L236–239), but most tier descriptions are qualitative. Harmful manipulation (">50% of steps", "<10% human oversight", L295, L305) and the automated-R&D operationalisation are the exceptions.

## A6. Method and lineage (as stated)

**v2.2** names its sources:
- "designed in the spirit of the Responsible Scaling Policy (RSP) framework introduced by the non-profit AI safety organization METR, as well as emerging government policy proposals in the UK, EU, and US", and it "helps satisfy" the 2023 White House and 2024 Frontier AI Safety commitments (L161–163);
- the v2.0 redesign was "inspired by safety case methodologies" (L976–977);
- security points to the RAND weight-security report, ISO 42001, SSDF, SOC 2 and NIST 800-53 (L571–587).

**v3** points to RAND SL4 for security (v3.4 L229, L303). Karnofsky gives the design lineage:
- "In 2023, I collaborated with METR to develop and pitch the basic idea of Responsible Scaling Policies" (karnofsky L110–111);
- v3's recommendations look "more like an FDA-inspired regime in which AI developers have flexibility to make a case that risks are low (which must address certain topics)" (L1152–1154).

**Threat-model selection** has explicit criteria (risk-report-feb §7.1, L3989–4003): "high potential damages and high likelihood"; "a clear role for AI in creating risk beyond what is created by other technologies and background conditions"; "sanity checks considering historical analogies"; and how much addressing one threat helps others and how hard early warning is.

**FCF**: METR, the Cloud Security Alliance's AI Safety Initiative, ISO 42001, NIST 800-53, and Trust & Safety practice (FCF L101–107).

## A7. Purpose, audience, force

- **v2.2**: "an internal operating procedure for investigating and mitigating these risks and helps inform the public of our plans and commitments… a prototype for other companies… potentially, inform regulators" (L115–118). Changes are proposed by the CEO and RSO and approved by the Board with LTBT consultation (L757–761).
- **v3 grades its own parts by force:**
  - industry recommendations: "we cannot commit to following them unilaterally" (v3.0 L70);
  - Roadmap: "These are not hard commitments but rather public goals against which we will openly grade our progress" (L75–76);
  - company-plan cells: commitments;
  - Appendix A: conditional commitments.
- **The Roadmap** calls itself a "forcing function" and promises it "will strive to avoid situations where we revise the goals in a less ambitious direction because we simply can't execute" (roadmap L43–55).
- **Audiences** named across the set: employees (unredacted Risk Reports to "at least 200"), Board, LTBT, the public (redacted, with redactions now disclosed, v3.4 L583), external reviewers (v3.4 §3.6), and policymakers.

## A8. Uncertainty handling

- **Default to the worse side when unshown:** "act as though the model has surpassed the Capability Threshold" (v2.2 L443–444). There may be "a substantial period during which models are not demonstrably close to the Capability Threshold, but we nevertheless are unable to rule out the risk to our satisfaction" (fn 9, L467–468).
- **"Treated as", decoupled from belief.** CB-1: "we currently act as though they meet our CB-1 threshold" (Aug L416–417) and "provisionally meeting the CB-1 threshold… in order to err on the side of caution rather than because we are confident these models cross the threshold" (Aug L5065–5068).
- **Saturation:** "if a new and otherwise-capable model were to perform worse on some of these evaluations, we would be more skeptical of the validity of the evaluation than of the model's risk-relevant abilities" (Aug L5073–5075).
- **Verbal grades plus a separate uncertainty adjustment** (A4). A self-grading footnote: "Some arguments may be incomplete or partially flawed" (Aug fn 16, L998–1001).
- **Honest limits on assurance:** "we cannot assure a specific level of effectiveness against future attackers" (roadmap L345–347); company plans "cannot make guarantees about an evolving landscape with continually adaptive attackers" (v3.0 L193–198).

## A9. What it excludes

- **Other risks are handled elsewhere.** "although this policy focuses on catastrophic risks, they are not the only risks we consider important—our Usage Policy and societal impacts research address other concerns" (v3.0 L90–92). Not a full regulatory document (L92–101).
- **Categories dropped.** v3's rows cover only chemical/biological among CBRN. Radiological and nuclear drop out, as does v2.2's cyber "ongoing assessment" (williams L287–298 observes this and notes no reason is given; this matches my reading of the texts). Cyber reappears as a *statutory* category in the FCF.
- **Persuasion (v2.2):** "not yet sufficiently understood to include in our current commitments" (fn 2, L346–347).
- **Within CB:** biological threats "with pandemic potential" are prioritised (Feb L2774–2780).
- **Within misalignment** (Aug): engineered misalignment set aside (Claim 8); only named pathways covered (Claim 7). Differential slowdown of safety research and "a future which falls dramatically short of its potential" are explicitly "out of scope" (L2779–2809).

## A10. Key terms as this model uses them

| Term | Meaning here | Definition / reference |
|---|---|---|
| **hazard** | Not used as a model term (only "infohazard", Aug L2931) | — |
| **risk** | *General:* used but undefined in the RSP. *Risk Reports:* "absolute" (leftover after mitigations, industry-wide) vs "marginal" (over other developers). *Misalignment:* "misalignment risk… the expected total unmitigated harm induced by misaligned computations produced by covered models" | v3.0 L446–447; Feb L260–268; Aug L969–971 |
| **catastrophic risk** (RSP) | "risks of the most severe potential harms from advanced AI, such as existential threats or fundamental destabilization of global systems… in its plain meaning rather than adopting any specific statutory definition" | v3.0 fn 1 L137–141 |
| **systemic risk** (FCF) | ">50 fatalities… or 1 billion dollars of financial damages", covering both TFAIA "catastrophic" and EU "systemic" | FCF L87–90, L118–121 |
| **harm** | Undefined. "Harm-inducing" is defined: a computation that "increase[s] expected future harm above that coming from a baseline benign or null computation" | Aug L933–948 |
| **severity / magnitude** | RR: "Potential magnitude of impact" (undefined); FCF: "probability and severity of harm" (undefined); Aug: "Severe misalignment" = "could plausibly contribute to one of our priority risk pathways" | Feb L478; FCF L159; Aug L929–931 |
| **likelihood / probability** | Used, not defined; "expected damages" = probability × size, summed | Feb fn 41 L4011–4016 |
| **threat model** | "the specific ways that models might pose threats" | v3.0 L80 |
| **risk factor** | Used informally, undefined (Aug L1693, L1954) | — |
| **capability** | Undefined | — |
| **Capability Threshold** (v2.2) | "a prespecified level of AI capability that, if reached, signals (1) a meaningful increase in the level of risk… and (2) a corresponding need to upgrade the safeguards" | v2.2 L216–219; glossary L829–830 |
| **ASL / ASL Standard** | v2.2: "a set of technical and operational measures for safely training and deploying frontier AI models". Aug: retired as terminology | v2.2 L172–173, L813–815; Aug fn 59 L5385–5388 |
| **Required Safeguards** | "The standard of safety and security measures that must be implemented when a model reaches a Capability Threshold" | v2.2 L848–849 |
| **safeguard / mitigation** | v2.2: "safeguards" = deployment + security standards. v3: "risk mitigations" is the umbrella "across security, deployment safeguards, and alignment domains"; "safeguards" narrows toward deployment/misuse measures | v2.2 L180–188; v3.4 L479–480 |
| **CB-1 / CB-2** | Risk-Report names for the non-novel and novel CB threat models ("CB" = chemical and biological) | Aug fn 45 L4712; L4745–4870 |
| **Level 1/2/3** | Classifier robustness levels | Aug L5465–5505 |
| **highly capable** | Crosses the automated-AI-R&D threshold (v3.4); v3.0: could "compress two years of 2018–2024 AI progress into a single year" | v3.4 L601–602; v3.0 L553–557 |
| **sabotage** | "when an AI model with access to powerful affordances within an organization uses its affordances to autonomously exploit, manipulate, or tamper with that organization's systems or decision-making in a way that raises the risk of future catastrophic outcomes" | Feb L435–441 |
| **alignment / misalignment** | *Roadmap:* "Ensuring that our models themselves do not autonomously cause harm, and instead consistently behave in line with our Constitution." *Aug:* misalignment is a property of a computation, judged against a reasonable person's view and the constitution; plus coherent / pervasive / context-dependent / known / unknown / engineered variants | roadmap L24–26; Aug L846–927 |
| **loss of control** | RSP and Risk Reports: never used. FCF: "scenarios where AI models develop and pursue goals autonomously that conflict with their developers' intentions or users' interests"; Tier 1/2 = RSP autonomy rows | FCF L317–331, L344–391 |
| **incident / event** | RSP: undefined ("incident scenarios", v2.2 L709–713). FCF: "AI Event" = "observable events that could signify the existence of a Serious AI Incident or Critical Safety Incident, but requires further investigation", with the statutory terms by reference. Aug: "safety process failures" as a reporting category | FCF L454–458; Aug L6682–6695 |
| **uplift** | Undefined as a term; operationalised against "2023-level online resources" (v2.2) and "a world with access only to the best AI models as of 2023" (FCF) | v2.2 L919–921; FCF fn 4 L272 |
| **developer / provider** | "AI developer", "frontier developer" used, undefined. "provider" only in the EU legal sense: "Anthropic Ireland, Limited is the provider of Anthropic's GPAISR models in the EU" | v3.0 L57–64; FCF L640 |

---

# Part B. OpenAI

## B1. The pieces and how they fit

```
Preparedness Framework v2 (voluntary)                Frontier Governance Framework (statutory)
 ├─ 5 criteria → Tracked Categories (3)              ├─ "systemic risk" (>50 deaths / $1B)
 │              → Research Categories (5)            ├─ 4 categories × Tier 1/2/3 (Description + Examples)
 ├─ per Tracked Category: threshold [High|Critical]  │    CBRN Tier 2/3 = PF High/Critical text
 │    → associated risk → safeguard guideline        │    Loss of control absorbs AI self-improvement
 ├─ Capabilities Report  (Scalable Evals + Deep Dives)├─ AI Safety Incident Response Plan (AIRP)
 ├─ Safeguards Report    (claims per harm vector)    └─ Safety & Security Model Report
 ├─ SAG recommends → Leadership decides → Board SSC oversees
 └─ §4.3 marginal-risk clause
System cards publish summaries of both reports per model (e.g. Astra, 10.1–10.2).
```

## B2. The model: tracked capabilities, two thresholds, sufficiency of safeguards

> "The Preparedness Framework is OpenAI's approach to tracking and preparing for frontier capabilities that create new risks of severe harm… In each area, we develop and maintain a threat model that identifies the risks of severe harm and sets thresholds we can measure… We won't deploy these very capable models until we've built safeguards to sufficiently minimize the associated risks of severe harm." (pf-v2 L8–21)

**Severe harm:** "the death or grave injury of thousands of people or hundreds of billions of dollars of economic damage" (fn 1, L33–36).

**Admission to tracking** requires five criteria (L145–162):
1. **Plausible**: "possible to identify a causal pathway for a severe harm";
2. **Measurable**;
3. **Severe**;
4. **Net new**: "cannot currently be realized… with existing tools and resources (e.g., available as of 2021) but without access to frontier AI";
5. **Instantaneous or irremediable**: "once realized, its severe harms are immediately felt, or are inevitable due to a lack of feasible measures to remediate."

**Two levels:**

> "High capability thresholds mean capabilities that significantly increase existing risk vectors for severe harm… required to have robust and effective safeguards that sufficiently minimize the associated risk of severe harm before they are deployed and appropriate security controls as they are developed. Critical capability thresholds mean capabilities that present a meaningful risk of a qualitatively new threat vector for severe harm with no ready precedent. Critical capabilities require safeguards even during the development of the covered system, irrespective of deployment plans." (L170–176)

| Tracked Category | High | Critical |
|---|---|---|
| Biological & Chemical | "meaningful counterfactual assistance (relative to unlimited access to baseline of tools available in 2021) to 'novice' actors… that enables them to create known biological or chemical threats" | "enable an expert to develop a highly dangerous novel threat vector (e.g., comparable to a novel CDC Class A biological agent) OR… complete the full engineering and/or synthesis cycle… without human intervention" |
| Cybersecurity | "removes existing bottlenecks to scaling cyber operations including by automating end-to-end cyber operations against reasonably hardened targets OR by automating the discovery and exploitation of operationally relevant vulnerabilities" | "identify and develop functional zero-day exploits of all severity levels in many hardened real-world critical systems without human intervention OR… devise and execute end-to-end novel strategies for cyberattacks against hardened targets given only a high level desired goal" |
| AI Self-improvement | "equivalent to giving every OpenAI researcher a highly performant mid-career research engineer assistant, relative to those researchers' 2024 baseline" | "capable of recursively self improving (i.e., fully automated AI R&D), defined as either (leading indicator) a superhuman research-scientist agent OR (lagging indicator) causing a generational model improvement… in 1/5th the wall-clock time… sustainably for several months" |

(Table 1, L194–296; the extraction is interleaved, read column-aligned.) The safeguard guideline for every Critical row includes: "Until we have specified safeguards and security controls that would meet a Critical standard, halt further development" (L208–216, L254–260, L281–286).

**Research Categories** (L318–351) are Long-range Autonomy, Sandbagging, Autonomous Replication and Adaptation, Undermining Safeguards, and Nuclear/Radiological. Each has a "potential response" (e.g. sandbagging: "use a conservative upper bound").

**Safeguards are argued by claims** (L505–566, Appendix C). There are two sources of harm, "a malicious user… and a misaligned model, which autonomously causes the harm" (L505–507), and a vector is covered when "all plausible known vectors of enabling severe harm are sufficiently addressed by one or more of the following claims" (L790–791, L879–880):
- **against malicious users**: Robustness, Usage Monitoring, Trust-based Access;
- **against a misaligned model**: Lack of Autonomous Capability, Value Alignment, Instruction Alignment, Reliable and Robust System Oversight, System Architecture.

Tables 4–5 pair each claim with example safeguards and "efficacy assessments" (L809–966). A stated principle: "reducing risk generally does not require reducing capability" (L676–677).

**Decision.** The Capabilities Report goes to the SAG, which determines "crossed / not crossed / deep dive" (L461–484). The Safeguards Report then goes to the SAG, which can recommend deployment, request more evaluation, or recommend alternatives (L515–586). Decision rights: "OpenAI Leadership can also make decisions without the SAG's participation, i.e., the SAG does not have the ability to 'filibuster'"; the Board's Safety and Security Committee "may reverse a decision" (L743–761).

**The marginal-risk clause** (§4.3, L594–604): if another developer releases such a system without comparable safeguards, OpenAI "could adjust accordingly the level of safeguards", but only if doing so "does not meaningfully increase the overall risk", it "publicly acknowledge[s]" the adjustment, and it keeps "safeguards at a level more protective than the other AI developer."

## B3. How the if-then changed

The v2 changelog is the only in-set account of v1 (Dec 2023; critical-cyber L48–52):
- "we are removing terms 'low' and 'medium'… because those levels were not operationally involved" (pf-v2 L682–683);
- persuasion moved out; nuclear/radiological moved to Research; "Model Autonomy" split into self-improvement (Tracked) plus Long-range Autonomy and ARA (Research) (L687–691, L354–365);
- "moving beyond the flawed approach of re-running capability evaluations on the safeguarded model" (L710–712);
- "Deprioritize safety drills" (L713–714).

**2026 in practice, in the Astra sequence:**
1. Aug 7: "cannot rule out critical cyber capabilities" (critical-cyber L29–32).
2. An enacted pause: "a two-week pause in reinforcement learning (RL) training… Our largest planned frontier RL run remains on hold" (pacing L46–57).
3. Sep 1: "We now believe Astra meets the Critical cybersecurity capability threshold" (path-to-astra L24–26), plus a sufficiency judgment for release (L45–48).
4. Sep 3: the system card, "our first model to reach the Critical level of cybersecurity capability", deployed (astra L162–164).

The pacing post also signals the model will change: "we need a broader approach—one that builds on and extends beyond the current Preparedness Framework" (pacing L69–72); "We will evolve our Preparedness Framework" (L331).

**Scrutiny.** PF v2 says: "We do not currently possess any models that have Critical levels of capability, and we expect to further update this Preparedness Framework before reaching such a level with any model" (L610–612). Every Critical row reads "until we have specified safeguards… that would meet a Critical standard, halt further development". This set contains no PF update and no published Critical standard.
- What it does contain: partial pauses, stricter security requirements (pacing L145–204), and the system card's "public summary of our internal Safeguards Report", which "informed our Safety Advisory Group's recommendation and OpenAI leadership's determination that these safeguards are sufficient for Astra's public launch" (astra L3613–3617).
- A PF v3 may exist outside this set. From these documents alone, the Critical standard's content is not public.

A second scrutiny point: the evidence behind the determination includes an admitted monitorability regression. "GPT-6 Astra shows a substantial decrease in chain-of-thought monitorability compared to previous models" (astra L1590–1591). This comes with a commitment whose parameter is unstated: "will not accept further degradation of monitoring beyond a limit" (L1717–1719).

## B4. Voluntary / statutory division

The FGF describes itself as "designed to meet the baseline legal requirements of various frontier AI laws" (fgf L57–58). "The PF and FGF together describe OpenAI's practices… because the PF is intended both to advance the science of managing severe risks… it may use different definitions of catastrophic risk and does not depend on specific legal compute thresholds like the FGF" (L77–86).

| | PF v2 | FGF |
|---|---|---|
| Severity term | "severe harm": thousands of deaths / hundreds of billions of dollars (L33–36) | "systemic risk": "greater than 50 fatalities or $1 billion of property damages or losses arising from a single incident" (L121–127) |
| Categories | Bio/chem, cyber, AI self-improvement | Cyber offense, CBRN, harmful manipulation, loss of control (L149–210) |
| Levels | High / Critical | Tier 1 / 2 / 3, each with "Examples" (L298–457). CBRN Tier 2/3 = PF High/Critical text; cyber tiers track PF closely; Tier 1 is new (a lower rung) |
| Method language | capability thresholds, safeguard sufficiency | "we estimate the severity and probability of harm of risks related to CBRN, cyber offense, and loss of control" (L228–231); precautionary crossing (L268–272) |
| Maturity | — | Harmful manipulation "remains exploratory… best addressed through system level mitigations, such as post-deployment monitoring" (L396–400); loss-of-control tiers exploratory "outside of risks related to AI self-improvement" (L414–415) |

## B5. Method and lineage (as stated)

- Threat models "informed both by our broader risk assessment process, and by more specific information… we also recognize that in the case of net-new risks of severe harm, significant safeguards may be needed to reduce the risk of harms that have never been realized" (pf-v2 fn 4, L179–183).
- "our adoption of Capability Reports and Safeguards Reports parallels Anthropic's updated RSP" (fn 2, L177). The five criteria "were informed in part by Meta's recent Frontier AI Framework" (fn 3, L178).
- Evaluations: "science-backed evaluations that provide high precision and high recall indications" (L399–401). Two tiers: Scalable Evaluations with "indicative thresholds", and Deep Dives to validate them (L414–423).
- FGF: "ISO 42001, the NIST AI Risk Management Framework, and frontier safety laws… the proposal for Responsible Scaling Policies first introduced by METR" (fgf L100–106).
- Later posts define "safety claim" and "safety case" ("A structured argument, supported by evidence, explaining why a model or system's risks are adequately managed for a specified activity", third-party-assessments L132–147). The PF itself does not use the term.

## B6. Purpose, audience, force

- Purpose: the PF's first line and a "Build trust" section, "so that the public, governments, and our industry peers can trust in our adherence to this policy" (L620–621).
- Force: voluntary but with internal decision procedure; "living document", reviewed "at least once a year"; a "Fast-track" for urgent risks (L762–769).
- Public outputs: system cards with Preparedness results, safeguards information above High (L636–646); third-party evaluation "when available and feasible" (L647–661).
- The FGF carries the legal obligations and is overseen by the OpenAI Foundation board's Safety and Security Committee and OpenAI Ireland's board (fgf L736–741).

## B7. Uncertainty handling

- **Lower bound:** "we regard any one-time capability elicitation in a frontier model as a lower bound, rather than a ceiling" (pf-v2 L409–411; fgf L258–262; astra L2499–2503).
- **Indicative thresholds plus judgment:** "The determination that a threshold has been reached is informed by these indicative results… and also reflects holistic judgment based on the totality of available evidence" (pf-v2 L464–466).
- **Precautionary classification:**
  - "we have treated models as crossing a capability threshold in circumstances where we are unable to rule out that a new threshold had been reached" (fgf L268–272);
  - "these models should thus be precautionarily treated as High. Additional validation from wet-lab uplift studies may ultimately change this conclusion" (astra L2519–2523);
  - "cannot rule out" as a public grade (critical-cyber L29–32).
- **Conservative bounds:** refusals "count[ed]… as successes to calculate a conservative upper bound" (astra L2524–2528); sandbagging handled by "conservative upper bound" (pf-v2 L329–332).
- **Hedges added after publication.** "the absence of observed failures does not establish reliability across settings" (astra changelog L123–129).

## B8. What it excludes

- **Everything below "severe harm"**, handled by "our safety stack" (fn 1, L35–36).
- **By the fifth criterion, risks whose harms are slow or remediable.** "Instantaneous or irremediable" (L156–157) excludes, by construction, harms that accumulate and could be remediated. This is my reading of the criterion's effect; the PF does not discuss it.
- **Persuasion**: "Going forward we will handle risks related to persuasion outside the Preparedness Framework" (L687–690). Nuclear/radiological is demoted with reasons: classified expertise, physical barriers (L371–382).

## B9. Key terms as this model uses them

| Term | Meaning here | Definition / reference |
|---|---|---|
| **hazard** | Not used as a model term (only "information hazards", astra L3650) | — |
| **risk** | Used as "risk of severe harm"; not defined separately. "Residual risk" used, undefined (pf-v2 L520). FGF "systemic risk" defined | pf-v2 L8–9; fgf L121–127 |
| **severe harm** (PF) | "the death or grave injury of thousands of people or hundreds of billions of dollars of economic damage" | pf-v2 fn 1 L33–36 |
| **systemic risk** (FGF) | "foreseeable and material risks of severe harm from the development, storage, use, or deployment of our most advanced frontier models, including risks that a model will materially contribute to greater than 50 fatalities or $1 billion…" | fgf L121–127 |
| **catastrophic risk** | PF: not its term. FGF: "catastrophic risks, as defined under the TFAIA"; the PF "may use different definitions" | fgf L60–63, L82–86 |
| **severity** | Used for the severe-harm bar and exploit "severity levels"; undefined. FGF: "estimate the severity and probability of harm", undefined | pf-v2 L35; fgf L230 |
| **likelihood / probability** | Used, undefined | fgf L230 |
| **threat model** | "identifies the risks of severe harm and sets thresholds" (a threat model does both) | pf-v2 L17–19, L165–167 |
| **capability threshold** | "concretely describe things an AI system might be able to help someone do or might be able to do on its own that could meaningfully increase risk of severe harm" | pf-v2 L168–170 |
| **High / Critical** | High: "significantly increase existing risk vectors for severe harm". Critical: "a meaningful risk of a qualitatively new threat vector for severe harm with no ready precedent" | pf-v2 L170–175 |
| **indicative threshold** | "levels of performance that we have pre-determined to indicate that a deployment may have reached a capability threshold" | pf-v2 L416–418 |
| **Tracked / Research Category** | Tracked: meets the five criteria. Research: "do not meet the above criteria, nonetheless have the potential to cause or contribute to severe harm" | pf-v2 L145–162 |
| **tier** (FGF) | "risk tiers that concretely describe things an AI system might be able to help someone do or might be able to do on its own that could meaningfully increase risk of severe harm" (the same wording as PF's "capability thresholds") | fgf L245–248 |
| **capability** | Undefined | — |
| **safeguard / control / mitigation** | PF: "safeguards" is the umbrella; "security controls" is a parallel class ("safeguards and security controls"); "mitigation" does not occur in PF v2. FGF: "safety mitigations" and "security mitigations" | pf-v2 L497–512, L969–978; fgf L459–473, L586–587 |
| **malicious user / misaligned model** | the two ways "risks can be realized": "a malicious user, who can leverage the model to cause the severe harm, and a misaligned model, which autonomously causes the harm" | pf-v2 L505–507 |
| **alignment** | *PF claims:* "Value Alignment: The model consistently applies human values in novel settings…"; "Instruction Alignment: The model consistently understands and follows user or system instructions…". *Pacing:* "Alignment—the work of making AI systems behave as intended and responsive to human oversight". *HF blog:* "misaligned with the goals of their assigned tasks". *Misalignment reporting framework:* used but undefined | pf-v2 L883–887; pacing L60–62; hf-incident L30–31 |
| **loss of control** | PF: not used ("human control", L16, L290–291). FGF: "Risks stemming from the inability to reliably direct, modify, or shut down a model, including evading the controls of a model developer or user, or autonomous conduct that, if conducted by a human, would constitute a crime…"; later "humans losing the ability to reliably direct, modify, or shut down a model" | fgf L200–210, L409–415 |
| **incident** | PF: undefined. FGF: "AI safety incident" per the AIRP, whose "definitions optimized for operational decision-making" are not published; statutory "critical safety incidents" by reference | fgf L493–511 |
| **metagaming / oversight gaming** (system card) | "when a model reasons in its Chain of Thought about how it will be graded, rewarded, or monitored"; oversight gaming = acting on that reasoning "in a way that would undermine the intended meaning of the evaluation result" | astra L1369–1385 |
| **monitorability** | "the extent to which we can expect monitoring systems to be able to detect when Astra acts in misaligned or otherwise undesirable ways" | astra L1587–1590 |
| **developer / provider / deployer** | "frontier AI model developer", undefined (L595). FGF: "OpenAI Ireland Limited is the provider of OpenAI's GPAI-SR models in the EU" (legal sense). "deployer" not used | pf-v2 L595; fgf L704–705 |

---

## Across the two, briefly

**Where they converge:**
- a small set of catastrophic categories;
- thresholds stated as what the model can help someone do;
- dated baselines (OpenAI 2021, Anthropic 2023);
- a developer-internal decision body (RSO+CEO; SAG+Leadership) with board oversight;
- escape clauses keyed to competitors;
- statutory companions built on the same EU/California template, both defining systemic risk as >50 deaths or $1B, both filing their AI-R&D/self-improvement category under statutory "loss of control".

**Where they diverge:**
- **Where the model lives.** OpenAI's model is still *threshold → safeguard sufficiency*, and its 2026 determinations run through that machinery. Anthropic moved the centre of gravity to a *periodic, argued, graded risk assessment of the whole company*: a Risk Report, rather than a gate per threshold.
- **What gets assessed.** OpenAI evaluates capabilities per model and safeguards per deployment. Anthropic grades risk per threat model across all models, including internal ones.
- **Terms of art.** OpenAI's is "safeguards", with misalignment treated as a second harm source to be safeguarded against. Anthropic's is "risk mitigations", with alignment assessment as evidence inside a risk argument.

**Against Joseph's chain** (sources & causes → preventions & controls → risk events × impact radius → mitigations & recovery → policies):
- **Where they line up.** Both centre on *capability as a cause-enabler* and *safeguards as prevention*. Anthropic's decomposition is the chain's middle in miniature: P (a risk event occurs) · H (harm given occurrence) · U (fraction not mitigated). The Feb pathways, as "intermediate unwanted outcomes", treat stage as relative to a focal event.
- **Where they cut across:**
  - *Impact radius.* Both collapse it into a single severity bar (deaths or dollars), with no harmed-group structure.
  - *Recovery.* Recovery is nearly absent. FCF's "rectifying harms" is one sentence (L487–491), and OpenAI's criterion "instantaneous or irremediable" excludes recoverable harms by design.
  - *Policies.* The "policy" stage points back at the developer's own gates rather than at the world.

I'm on the line for questions.
