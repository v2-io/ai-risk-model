# The frontier safety framework's model of risk (the genre, excluding the RSP and Preparedness Framework)

*From the agent that wrote `../source-atlas/co-others.md`. It covers the frameworks of Google DeepMind (four versions, plus a model report and a blog post), Meta (two), Microsoft (two), Amazon (two), xAI (three), NAVER (two), G42, Cohere, NVIDIA, Magic and Shanghai AI Lab. It also draws on five analyses of the genre: METR's "Common Elements", Buhl et al. (UK AISI), Stelling et al. (SaferAI), Coggins et al., and Zhu. Anthropic's Responsible Scaling Policy (RSP) and OpenAI's Preparedness Framework are in a companion section.*

*References have the form `key L123`: lines of `scratchpad/src-text/<key>.txt`, as in the atlas. Quotes are verbatim.*

---

## At a glance

| Dimension | The shared model |
|---|---|
| **Core structure** | An **if-then commitment**: *if* evaluations show a model has reached a named capability threshold, *then* specified safeguards must be in place before development or deployment continues; otherwise the developer holds. |
| **What it names** | Risk domains (CBRN, cyber, AI R&D; later harmful manipulation and loss of control). Capability thresholds with company-specific names (CCL, TCL, Critical Capability Threshold, risk levels, red lines). Early-warning evaluations and alert thresholds. Two families of safeguard: security (protect the weights) and deployment (prevent misuse). Response plans. Safety cases. Governance bodies and named decision-makers. |
| **How risk is graded** | By **capability**, as a proxy for risk. One to four tiers. Thresholds are mostly qualitative and phrased as uplift to an actor relative to a baseline. Acceptance ("deemed acceptable if …") is a judgment assigned to a governance function, not a computed criterion. There are almost no explicit risk tolerances (probability × severity). |
| **Where the method comes from** | METR's "responsible scaling" concept (2023), Anthropic's RSP and OpenAI's Preparedness Framework as templates, and the Seoul Frontier AI Safety Commitments (May 2024), which made publishing one an obligation. Secondary borrowings: RAND weight-security levels, safety cases, ISO/NIST risk-management vocabulary. From 2025–26: the EU GPAI Code of Practice and California's TFAIA/SB 53. |
| **Purpose, audience and force** | Voluntary corporate self-governance published for governments, peers and the public. It is also an internal decision procedure. From 2026 it is increasingly a statutory compliance document. Its force is mostly discretionary ("may", "as appropriate", "aim"), and it is revisable at will (the weakening is often undisclosed; Zhu). |
| **Uncertainty** | A **safety buffer** of early-warning thresholds set below the dangerous level. **"Cannot rule out"** is treated as reaching the threshold. Conservative elicitation. Explicit admissions of "subjective analysis". Uncertainty about the *world* is mostly handled by deferral ("exploratory", "illustrative", "we are studying"). |
| **Exclusions** | Everything that isn't severe or catastrophic and capability-driven: bias, privacy, misinformation, labour and power concentration, mostly left to "broader" responsible-AI programmes. Also: unknown or emerging risks, structural and systemic risks, and (for most) quantitative tolerances. Some frameworks exclude radiological/nuclear risk and loss of control. |

Key terms, framework by framework, are in §11.

Two members reject or re-scope the model: **Cohere** argues against catastrophic thresholds, and **NAVER 2.0** moves to service-level harms. **NVIDIA** grafts it onto a generic product-risk method. **Meta** redefines the threshold as an outcome rather than a capability. **Shanghai AI Lab** restates it as general guidance in ISO risk-management form.

---

## 1. What a framework is, in its own words

The framework's job is to say, in advance, what the developer will do when a model becomes dangerous. METR, which originated the concept, describes the frameworks as:

> "protocols adopted by leading AI companies to ensure that the risks associated with developing and deploying state-of-the-art AI models are kept at an acceptable level. This concept was initially introduced by METR in 2023" (metr L64–66)

METR's own footnote at L104–105 admits the gap at its centre: "there is currently no consensus or clear framework for determining what counts as an 'acceptable level' of risk."

The earliest framework in the set, GDM v1 (May 2024), states the core components compactly. Almost every later framework repeats them:

> "● Identify capability levels at which AI models pose heightened risk without additional mitigations
> ● Implement protocols to detect the attainment of such capability levels
> ● Prepare and articulate mitigation plans in advance for when such capability levels are attained
> ● Where appropriate, involve external parties in the process to help inform and guide our approach." (gdm-2024-fsf-v1-0 L26–29)

Buhl et al. (UK AISI) name the logical form: the three areas "form a set of 'if-then' commitments (i.e. commitments about what the developer will do if they see certain evidence of risk)" (buhl L65–67).

**Scope is deliberately narrow.** The framework is presented as one layer of a larger governance programme:

> "The Framework does not, therefore, reflect the full spectrum of risks that we assess for, nor all of the evaluations that we conduct." (meta-2025 L101–102)

Microsoft splits the two layers explicitly. Its framework targets "capability-related risks", while "more culturally contextual risks that are heavily shaped by use case and deployment environments" belong to its broader programme (microsoft-2026 L55–63).

---

## 2. The shared model

### 2.1 The chain

```
 RISK DOMAIN  (CBRN · cyber · ML R&D / autonomy · [harmful manipulation] · [loss of control])
     │  threat modelling: actors, pathways, bottlenecks  (often unpublished)
     ▼
 CAPABILITY THRESHOLD  ("minimal set of capabilities a model must possess" to cause severe harm)
     │  tiered:  early-warning / alert threshold  <  tracked (TCL)  <  critical (CCL)
     ▼
 EVALUATIONS  (benchmarks → deeper "dangerous capability" evals, red teaming, uplift studies;
     │           run at a cadence: every N× compute / N months / before deployment; with elicitation)
     ▼
 DETERMINATION  (reached / not reached / "cannot rule out" → treat as reached)
     │  made by a named governance function, often with "holistic" or "subjective" judgment
     ▼
 REQUIRED SAFEGUARDS
     ├─ security   (protect weights; RAND SL levels)       ── gates DEVELOPMENT
     └─ deployment (refusal training, classifiers, monitoring, KYC, staged release)
                                                             ── gates DEPLOYMENT
     ▼
 ACCEPTANCE  ("deemed acceptable if …"; safety case reviewed by governance)
     ▼
 DECISION   deploy / deploy restricted / hold deployment / pause development
     ▼
 DISCLOSURE & UPDATE  (share with government if material risk; revise framework ≥ annually)
```

GDM v1's own statement of the gate:

> "A model may reach evaluation thresholds before mitigations at appropriate levels are ready. If this happens, we would put on hold further deployment or development, or implement additional protocols … to ensure models will not reach CCLs without appropriate security mitigations, and that models with CCLs will not be deployed without appropriate deployment mitigations." (gdm-2024-fsf-v1-0 L84–88)

Amazon 2026's version is the plainest:

> "When an evaluation indicates that a model's capabilities meet a Critical Capability Threshold, we will not deploy the model until safeguards appropriately mitigate the risks." (amazon-2026 L153–154)

### 2.2 The two gates

Security and deployment safeguards answer different threats. Security is justified by exfiltration: "the release of model weights may enable the removal of any safeguards trained into or deployed with the model, and hence access (including by bad actors) to any critical capabilities" (gdm-2024-fsf-v1-0 L119–122). The two gates are therefore asymmetric:
- inadequate **security** halts *development*, because a stolen model bypasses deployment safeguards;
- inadequate **deployment** mitigation halts *release*.

G42 makes this rule explicit: "If a necessary Deployment Mitigation Level cannot be achieved, then the model's deployment must be restricted; if a necessary Security Mitigation Level cannot be achieved, then further capabilities development of the model must be paused" (g42 L125–128).

### 2.3 The CCL, the genre's central term

> "These are capability levels at which, absent mitigation measures, frontier AI models or systems may pose heightened risk of severe harm. CCLs are determined by identifying and analyzing the main foreseeable paths through which a model could result in severe harm: we then define the CCLs as the minimal set of capabilities a model must possess to do so." (gdm-2025-fsf-v3-0 L115–119)

Three features carry the genre:
- **The threshold is a property of the model** ("capabilities"). It includes what "reasonably foreseeable fine-tuning and scaffolding" could add (gdm-2024-fsf-v1-0 L209–211).
- **It is defined "absent mitigation"**, so it measures inherent danger, with safeguards applied afterwards.
- **It is minimal and sufficient on a pathway.** It names the capability that would open a path to severe harm, not the harm itself.

---

## 3. What they name

| Kind | Typical names | Notes |
|---|---|---|
| **Risk domain** | CBRN; cyber / offensive cyberoperations; ML R&D / AI R&D / advanced autonomy; harmful manipulation (GDM v3.0 onwards, Amazon 2026, Microsoft 2026, xAI 2026); loss of control (Meta 2026, Amazon 2026, Microsoft 2026, xAI) | A short list. It is chosen by "threat modelling" and by what is measurable. Meta 2025 requires every domain to be Plausible, Catastrophic, Net new and "Instantaneous or irremediable" (meta-2025 L550–575). |
| **Threshold** | CCL, TCL (GDM); Critical Capability Threshold (Amazon); Critical/High/Moderate (Meta); low/medium/high/critical (Microsoft); Frontier Capability Threshold (G42); red/yellow lines (Shanghai); MR1–MR5 (NVIDIA) | Usually "capability X gives actor Y uplift of size Z relative to baseline B toward harm W". |
| **Early warning** | "early warning evaluations" with an "alert threshold" (GDM); "leading indicators" (Microsoft); "capability checkpoint" (Meta 2026); "preliminary evaluations" (G42) | Set below the threshold so a model can't cross it between rounds of testing. |
| **Threat model / scenario** | "threat scenarios", "enabling capabilities", "harm journeys", "bottlenecks", "critical steps" | Meta's is the most explicit (§7). Details are usually withheld for security reasons (e.g. gdm-2026-gemini L306–309). |
| **Evaluation types** | automated benchmarks, expert red teaming, uplift studies (RCTs against a baseline), human-behaviour studies (manipulation), agentic tasks | Amazon's list: amazon-2026 L165–182 (the PDF prints its own line numbers, 119–133). Uplift-study definition: meta-2025 L1168–1174. |
| **Elicitation** | "maximal capability evaluations" (Amazon); "capability elicitation" via fine-tuning, scaffolding, tools (Microsoft 2026 L238–246) | The aim is to measure what a determined actor could get, not default behaviour. |
| **Safeguards** | security levels (RAND SL2–SL4/5; G42's SML), deployment levels (GDM v1; G42's DML), specific measures (refusal training, classifiers, account actions, KYC, staged release, weight encryption) | Security levels are indexed to the attacker they resist ("state programs", "OC3"). |
| **Safety case** | "an assessable argument showing how severe risks associated with a model's CCLs have been reduced to an appropriate level" (gdm-2025-fsf-v2-0 L216–217) | Reviewed by governance before deployment. |
| **Response plan** | GDM: formulated when an alert threshold is hit (gdm v3.0 L223–227) | Its contents aren't pre-specified. |
| **Governance roles** | AGI Safety Council (GDM v2); Chief AI Officer + Director of Alignment and Risk (Meta 2026); Executive Officers (Microsoft); SVP + CSO (Amazon); Chief Scientist (Cohere); Frontier AI Governance Board (G42); risk owners (xAI); board risk committee (NAVER) | Who decides, and with what override. |
| **Deployment types** | internal / high-risk internal / low-risk external / external (GDM v3.1 L904–916); internal / limited / controlled / closed / open (Meta 2026 L1634–1647) | Obligations attach per type: "required only for external deployment, not further development" (gdm v3.0 L280). |
| **Disclosure** | information to government if "unmitigated and material risk to overall public safety" (gdm v3.0 L717–726); preparedness reports (Meta 2026 L252–337); model cards | |

---

## 4. How they grade risk

**Capability stands in for risk.** Almost no framework states a risk tolerance. Buhl: "no currently published safety framework sets explicit risk thresholds" (buhl L373). Stelling finds "all Providers score below 25% on defining risk tolerances, with thresholds often using subjective language (e.g. 'severe' or 'acceptable')" (stelling L106–107).

The exceptions are harm counts that define "catastrophic":
- xAI's own figure, ">100 deaths or over $1 billion in damages" (xai-2025-rmf L95–98);
- later replaced by TFAIA's ">50 people or … one billion dollars" (xai-2025-faif L32–35).

Neither comes with a probability.

**Tiering.** The number of tiers varies:
- one tier (Amazon);
- a threshold with an alert threshold beneath it (GDM);
- tracked below critical (GDM v3.1);
- moderate/high/critical (Meta);
- four levels mapped to "deployment allowed" vs "further review and mitigations required" (microsoft-2026 L468–575);
- green/yellow/red zones (Shanghai L1386–1401).

**Thresholds are qualitative, by design.** Microsoft: "We use qualitative capability thresholds … as they offer important flexibility across different models and contexts at a time of nascent and evolving understanding" (microsoft-2026 L216–218). Meta explains why uplift can't be quantified:

> "At present, the science of evaluation is not sufficiently robust as to provide definitive quantitative metrics for uplift. Our assessment of whether a model exhibits significant uplift is made through our AI governance process … A final assessment of uplift is approved by senior-level decision-makers" (meta-2025 L699–705)

Quantitative anchors exist, but they are few and unstable:
- GDM's ML R&D threshold of "(e.g. 2x) from 2020-2024 rates" (gdm-2025-fsf-v2-0 L296–297) became "from historical rates" in v3.0 (L607);
- xAI's answer-rate and MASK criteria (xai-2025-rmf L220–223, L311–313) were removed in 2026;
- Meta 2026 has propensity criteria "at least 40% on MASK and at most 50% on Agent Misalignment" (L1358–1359);
- Magic's 50% on LiveCodeBench (magic L65–69);
- the Gemini report's 90% bar on ML R&D, set below a nominal 100% as a safety margin (gdm-2026-gemini L125–127).

**Acceptance is a judgment assigned to someone.** GDM's risk acceptance criteria:

> "A model for which the risk assessment indicates a misuse CCL has been reached will be deemed to pose an acceptable level of risk for further development or deployment, if, for example: … We assess that the deployment mitigations have brought the risk of severe harm to an appropriate level proportionate to the risk, based on considerations such as … what capabilities and mitigations are available on other publicly available models (e.g. if other models are similarly capable and have few mitigations, then the marginal risk added by our release is likely low)" (gdm-2025-fsf-v3-0 L256–280)

> "Because the science of AI risk assessment is still developing, our assessments will often involve some level of subjective analysis. The concept of proportionality is central to our determination" (gdm v3.0 L302–307)

**Baselines make the grades relative.** Uplift is always measured against something, and the something varies and moves (details in the atlas):
- "internet search" (Amazon 2025);
- "other publicly available models in known harnesses" (Amazon 2026);
- "a baseline without generative AI" (GDM);
- "currently available open-weights models" (Microsoft);
- an outside model already judged below the threshold (G42 L88–94);
- competitors' scores in May 2024 (Magic);
- the company's own previous model (Cohere).

Stelling spells out what follows: "These relative standards create inter-dependencies: if one Provider lowers standards, the baseline against which others measure themselves also lowers" (stelling L1714–1715).

**Benefit is part of the grade in several frameworks:**
- Meta 2025 §4.3, "Benefits assessment" (L983–1020);
- Microsoft's deployment case requires that "the marginal benefits of a model outweigh any residual risk" (microsoft-2026 L376–378);
- xAI allows release to "trusted parties if it would empower defenders more than attackers" (xai-2025-rmf L419–423).

---

## 5. How they handle uncertainty

**The safety buffer** is the genre's main device:

> "Our frontier safety strategy is based on a 'safety buffer' to prevent models from reaching CCLs, i.e. if a frontier model does not reach the alert threshold for a CCL, we can assume models developed before the next regular testing interval will not reach that CCL." (gdm-2026-gemini L32–34)

Its early form: early-warning evaluations "that we are confident will be passed before the model is 6x in effective compute or 3 months of fine-tuning away from the CCL" (gdm-2024-fsf-v1-0 L104–105).

**Precautionary designation.** Failing to rule out a threshold counts as reaching it:

> "Ultimately, if we cannot rule out, based on the evidence and threat models we have, that a T/CCL has been reached, we designate the model as 'cannot rule out being at the T/CCL', and mitigate accordingly." (gdm-2026-gemini L127–129)

The same logic runs in the other direction as a presumption: G42 presumes a model is below the threshold if it scores below an outside model already judged below it (g42 L88–94). Meta instead expects false positives and re-tests (meta-2025 L543–544).

**Conservative elicitation.** The evaluators try to measure the ceiling, not the default: "our risk assessment is based on the model's absolute potential rather than its default behavior" (gdm-2026-gemini L136–138). GDM also notes that "other actors may put significantly more effort into eliciting capabilities than we put into assessing risk, thus requiring conservatism" (gdm v3.0 L198–200).

**Deferral and labelling.** Uncertainty about *which risks matter* is handled by labelling a domain rather than grading it:
- misalignment CCLs are "exploratory and intended for illustration only, [so] we do not associate them with explicit risk acceptance criteria" (gdm v3.0 L141–143);
- harmful manipulation is "exploratory" (L473–475);
- Microsoft's loss of control and manipulation are "We are studying …" (microsoft-2026 L631–649);
- Meta 2026's "emerging" outcomes (L1398–1455).

**Adopted premises.** Some frameworks state what they assume in order to proceed: "we assume that catastrophic harm would eventually materialize as a result of an AI system ceasing to perform as intended" (meta-2026 L832–836). The Gemini report's safety case "assumes that AI deployments will feature oversight similar to that of human employees" (gdm-2026-gemini L1665–1666), and it immediately lists "severe disanalogies between AIs and humans" as a limitation (L1672–1675).

---

## 6. Where the method comes from

**Claimed lineage.**
- GDM v1 says it "is informed by the broader conversation on Responsible Capability Scaling". Its footnote cites the UK government's *Emerging processes for frontier AI safety*, METR's RSP post, Anthropic's RSP and OpenAI's Preparedness Framework (gdm-2024-fsf-v1-0 L23–24, L46–49).
- Later GDM versions add the Frontier Model Forum (gdm v3.0 L55–58). v3.1 adds Anthropic's SB 53 compliance framework (gdm v3.1 L57–58).
- METR claims the origin (metr L66). It is credited with input by Magic (L31), Amazon (amazon-2025 L24) and G42 (L29–30, with SaferAI).

**The trigger for the genre.** The Frontier AI Safety Commitments at the Seoul Summit (May 2024) turned publication into a signed obligation:
- "Microsoft's Frontier Governance Framework … has its genesis in the voluntary Frontier AI Safety Commitments that Microsoft and fifteen other AI labs made in May 2024" (microsoft-2026 L37–40);
- Meta, "In line with the Frontier AI Safety Commitments, which Meta signed in May 2024" (meta-2025 L94);
- Amazon, "Consistent with Amazon's endorsement of the Korea Frontier AI Safety Commitments" (amazon-2025 L10–11).

Buhl et al. built their thirteen components out of those commitments (buhl L69–73).

**Borrowed apparatus:**
- RAND's weight-security levels, used for principles "rather than the benchmarks (i.e. concrete measures)" (gdm v3.0 L368–373);
- safety cases (GDM, citing UK AISI's template: gdm-2025-fsf-v2-0 L218);
- uplift studies;
- threat modelling and Delphi elicitation (gdm-2026-gemini L271–273).

**Risk-management vocabulary arrives later:**
- GDM v3.1 reorganises into risk identification → inherent risk assessment → mitigation → residual risk assessment → acceptance (gdm v3.1 L167–359);
- Shanghai cites ISO 31000, ISO/IEC 23894 and GB/T 24353 (shanghai L198–199, L236–241);
- Microsoft and xAI cite the NIST AI RMF and ISO/IEC 42001 (microsoft-2026 L436–439; xai-2025-faif L60–61);
- NVIDIA borrows the V-model and FMEA-style scoring from product safety (nvidia L100–116, L203–212).

**Regulatory absorption, 2025–26.** Frameworks now rewrite themselves in statutory terms:
- xAI's became a TFAIA compliance document, "This FAIF complies with California's Transparency in Frontier Artificial Intelligence Act" (xai-2025-faif L11–12), and then took the EU Code's vocabulary (xai-2026-faif L40–42);
- Microsoft's scope trigger became "applicable laws, such as the EU AI Act, California's … TFAIA, and New York's … RAISE Act" (microsoft-2026 L171–173);
- NAVER 2.0 is built around Korea's AI Basic Act (naver-2026-asf2 L94–100, L258–260).

**Is there a method?** A shared *form* (the if-then gate) with borrowed tools, yes. A method for *setting* thresholds or tolerances, largely no. Stelling scores the genre against risk-management practice in other high-risk industries: median 18%, highest 34% (stelling L31–39). Its conclusion: "current frameworks may be better understood as tools for internal iteration on AI risk management than for external accountability" (stelling L132–133).

---

## 7. Purpose, audience and force

**Purpose as stated:** anticipate severe risks and commit to responses in advance. GDM frames safety as "a global public good" and adds that certain mitigations "are most effective when adopted by industry as a whole" (gdm v3.0 L39–44). Its earlier version made its own adoption conditional on others':

> "our adoption of the protocols described in this Framework may depend on whether such organizations across the field adopt similar protocols." (gdm-2025-fsf-v2-0 L32–34)

**Audiences:**
- governments and summits;
- the industry: GDM "recommend[s] a security level … the field of frontier AI should apply" (gdm v3.0 L413–416);
- the public;
- regulators, increasingly.

Internally, the framework works as a decision procedure. Meta presents openness itself as a safety benefit (meta-2025 L388–391).

**Force.** The language is overwhelmingly discretionary. Stelling: "Most Providers use phrases like 'may consider' or 'as appropriate' for significant actions such as pausing development, and it is not clear who has final decision or veto rights" (stelling L112–115). Hard stops, where they exist, are hedged or have since been softened:
- Meta 2025 would "stop development" at critical risk (meta-2025 L116–117). Meta 2026's change log records "Critical threshold changed from 'Stop' to 'Develop with Mitigations'" (meta-2026 L1678–1679).
- Microsoft keeps "we will pause development and deployment" if a risk cannot be mitigated (microsoft-2026 L365–367).

**Revisable at will, and often quietly.** Zhu measured that "67% of material changes … are silent" in the developers' own accounts, and "77% of traced changes weaken or remove a commitment" (zhu L26–31). Coggins's reading of one framework: it "requests some safety measures but demands none of them" (coggins L56–57).

---

## 8. What they exclude

- **Non-catastrophic harms.** Discrimination, toxicity, privacy, misinformation and labour are delegated to "broader" responsible-AI programmes (microsoft-2026 L55–63; gdm v3.0 L106–111; meta-2025 L99–102). Coggins maps one framework onto the MIT AI Risk Repository and finds that 21 of 24 risk subdomains are merely *allowed*, not required, to be evaluated (coggins L302–358).
- **Unknown and emerging risks.** "Most Providers score near zero on commitments to identify previously unknown risks" (stelling L103–105). Meta acknowledges "unknown unknowns" in a footnote (meta-2025 L486–488).
- **Structural and systemic risk.** Shanghai names systemic risk and then puts it out of scope, as needing "coordinated industry-wide and societal-level responses" (shanghai L420–423). GDM mentions "structural risks" only as a consequence of ML R&D (gdm v3.1 L148–151).
- **Loss of control** for many members. Microsoft and Amazon 2025 omit it. GDM keeps it "exploratory" until v3.1. NAVER 2.0 drops it. xAI calls it "speculative" (xai-2025-rmf L53–54).
- **Radiological and nuclear**, for some, citing materials bottlenecks (meta-2026 L1406–1411; xai-2025-rmf L204–210).
- **The harm itself.** Consequence, recovery and harmed populations are mostly outside the model. What is gated is the model's capability, not the event. Incident response appears as a governance line item (e.g. xai-2025-rmf L379–405; g42 L410–417).

---

## 9. Departures that matter

**Google DeepMind: the reference implementation, restructured four times.**
- v1: CCLs with security and deployment *levels*.
- v2: deployment levels replaced by a safety-case *process*; the Autonomy domain dropped (gdm v2 L271–275); a "deceptive alignment" section added.
- v3.0: explicit risk-acceptance criteria and harmful manipulation.
- v3.1: Tracked Capability Levels for "significant but not severe" harm (L153–159); misalignment merged into "ML R&D and Misalignment"; a glossary; an ISO-style process.

Distinctive throughout: it treats its own progress as the evidence for ML R&D thresholds (gdm v3.0 L198–215), and it frames security requirements as recommendations to the whole field. GDM is also the only member in my family that publishes a model-level report with measurements against its thresholds (gdm-2026-gemini).

**Meta: thresholds tied to outcomes, not capabilities.**

> "We start by identifying a set of catastrophic outcomes we must strive to prevent, and then map the potential causal pathways that could produce them … and we define our risk thresholds based on the extent to which a frontier AI would uniquely enable execution of any of our threat scenarios." (meta-2025 L441–447)

The argument is a necessity test on a pathway:

> "By testing whether our model can uniquely enable a threat scenario, we're testing whether it uniquely enables that essential part of the pathway. If it does not, then we know that our model cannot be used to realize the catastrophic outcome, because this essential part is still a barrier." (meta-2025 L506–509)

Its tables run outcome → threat scenario → enabling capabilities (meta-2025 L743–863). In 2026 the operative test weakened from "uniquely enable" to "substantially contribute to" (a "material factor", meta-2026 L1616–1620). Loss of Control was added, defined as the failure of named control mechanisms rather than as enumerated harms (meta-2026 L794–808). Meta also sets its "Frontier AI" threshold by capability or by ≥10^26 FLOP.

**Microsoft: indicators, then levels.** Cheap general benchmarks serve as "leading indicators", and only models that trip them get "deeper capability assessment" (microsoft-2026 L156–200). The benchmark inclusion rules sit in footnote 1 (L201–204). Levels are low/medium/high/critical against an actor-skill grid (Appendix I). Stated principles: "Targeted and proportional", "Flexible and durable" (L65–79).

**Amazon.** One threshold per domain, no tiers. The uplift baseline moved from internet search to "other publicly available models in known harnesses". The 2026 version adds "Misalignment Safeguards" framed as instilling a "model persona" (amazon-2026 L274–288). The document is heavy with AWS security practice.

**xAI: risk as model behaviours.** It organises by "individual model behaviors, which we categorize into three buckets: abuse potential …, concerning propensities …, and dual-use capabilities" (xai-2025-rmf L34–37). It set numeric acceptance criteria on benchmarks, cites public deployment on X as a monitoring channel (L64–68), and reasons about bottleneck "critical steps" in the bio attack chain (L157–202). By 2026 the document is an EU-Code-shaped systemic-risk process with no numbers.

**NVIDIA: product-risk method with autonomy tiers.** A Preliminary Risk Assessment scores **use case × capability × level of autonomy** into MR1–MR5 (nvidia L41–69), and "A frontier model would be classified as MR5 due to potential adversarial capabilities … operating within an undefined domain" (L91–92). Risk is a product of scored factors: "Risk = frequency x (duration + speed of onset) x (detectability + predictability)" (L207–208). It says frontier models are "not currently under development at NVIDIA" (L14–15). Because the category is set by *how the product is deployed*, it can be lowered by restricting use (L184–190), which differs from the rest of the genre, where the threshold belongs to the model.

**Cohere: rejects the catastrophic-threshold approach.** It describes that approach as addressing risks "speculated to arise when models attain specific capabilities", and says the research behind it is "limited in [its] methodological maturity and transparency" (cohere L568–589). Cohere focuses on "risks that are known, measurable, or observable today" (L593–595). Its acceptance line is relative: no "significant regressions compared to our previously launched model versions" (L632–638).

**NAVER: from frontier model to service.** ASF 2024 defined loss of control as "severe disempowerment of the human species" (naver-2024 L69–71). ASF 2.0 (2026) is "service-centered". Its taxonomy crosses subjects of protection (users, society, the AI service ecosystem) with protected values (life, economic value, non-discrimination) (naver-2026 L147–219). Loss of control and catastrophic risk no longer appear.

**G42.** The two-gate rule, stated most cleanly (§2.2). Deployment and security levels are defined by the adversary they resist. Presumption by comparison. A phased plan with dates.

**Magic.** A commitment to write the full framework once a coding benchmark is crossed (50% on LiveCodeBench, calibrated to competitors in May 2024; magic L53–69). The live page now says the policy "is outdated" (L9).

**Shanghai AI Lab.** Guidance to *other* developers in ISO form. It describes six stages, and three dimensions of deployment Environment, Threat source and enabling Capability (E-T-C) (shanghai L257–283). **Red lines** are "absolute thresholds for unacceptable outcomes … defined based on expert consensus"; **yellow lines** are early warnings (L698–757). Risk domains are keyed by threat source (L369–417).

---

## 10. How the analyses see the genre

These five analyses are sources in their own right. Each brings its own grid:
- **METR** (Dec 2025): nine common elements (capability thresholds, weight security, deployment mitigations, conditions for halting deployment and development, full elicitation, timing, accountability, updating), shown by verbatim excerpt (metr L83–122). Descriptive, and says so (L51–56).
- **Buhl et al.**: three areas, thirteen components and 56 "emerging practices" derived from the Seoul commitments. Normative ("can", "could").
- **Stelling et al.**: 65 criteria from established risk management, and a score for every framework.
- **Coggins et al.**: the modal force of each clause (allow / encourage / request / demand / refuse).
- **Zhu**: revision over time, coded commitment by commitment.

They converge on four points: thresholds stand in for risk tolerances, commitments are discretionary, deciders are internal, and revision goes largely unaccounted for.

---

## 11. Key terms as this model uses them

Most frameworks use their core words without defining them. Glossaries arrive late: Meta 2025, GDM only from v3.1, Shanghai. Where frameworks differ, there is a row per framework. "Undefined" means the word is used but nowhere defined in that document. Line references are to the version named. Usage counts come from grep; they are case-insensitive, and some counts include other senses of the word (e.g. "aligned with RAND SL").

**hazard.** Absent from GDM, Meta 2025, Amazon, NAVER and Cohere (0 occurrences).

| Framework | Use |
|---|---|
| Microsoft 2026 | Undefined, in passing: "societal and institutional factors that can impact whether and how a hazard materializes" (L251–252). |
| NVIDIA | Undefined, but it is the **unit of risk analysis**: "identify possible hazards, estimate the level of risk for each hazard" (L196–197). Each hazard is scored for frequency, duration, speed of onset, detectability and predictability (Table 1, L220–240). Table 2 has a "Hazard source" column (L283–284). |
| Shanghai | "Hazard: Any event or activity with the potential to cause harm, such as loss of life, injury, social disruption, or environmental damage." (L2130–2131) |
| Stelling (analysis) | Undefined. It appears inside "Risk Identification: The process of recognizing and categorizing potential hazards, risk sources, models and scenarios" (L1909–1910). |

**risk**

| Framework | Use |
|---|---|
| GDM | Undefined as a word; used as "risk of severe harm". v3.1 defines the *processes* around it: "Inherent Risk Assessments: the process of evaluating the level of risk posed by the model" (L861–862); "Residual Risk Assessments: the process of evaluating the level of risk that remains after all planned mitigation strategies have been implemented" (L938–939). |
| Meta 2025 / 2026 | Undefined as a word. "Risk thresholds are the incremental levels of risk that a frontier AI model might pose towards realization of a catastrophic outcome" (2025 L1110–1112). "Residual risk describes the level of risk that a frontier AI model presents after mitigations have been implemented" (2025 L1117–1119). |
| NVIDIA | "We defined risk as the potential for an event to lead to an undesired outcome, measured in terms of its likelihood (probability), its impact (severity) and its ability to be controlled or detected (controllability)." (L203–205). Operationalised as "Risk = frequency x (duration + speed of onset) x (detectability + predictability)", scored 1–64 (L205–208). |
| Shanghai | "Risk: The combination of the probability and severity of harm arising from the development, deployment, or use of AI." (L2128–2129) |
| xAI 2025 FAIF | Imports TFAIA: "Catastrophic Risk as 'a foreseeable and material risk that a frontier developer's development, storage, use, or deployment of a frontier model will materially contribute to the death of, or serious injury to, more than 50 people or more than one billion dollars …'" (L32–35). |
| xAI 2026 | Undefined; "systemic risk" is taken from the EU Code of Practice as terminology (L40–42, L90–92). |
| Stelling (analysis) | "Risk Tolerance: The maximum level of risk an organization is willing to accept. Ideally expressed quantitatively as probability × severity per unit time" (L1920–1922). |

**harm, severe harm, catastrophic**

| Framework | Use |
|---|---|
| GDM | "Severe harm" is undefined. v3.1's TCLs cover "significant but not severe levels of harm" (L851–853); neither grade is defined. Misuse CCLs speak of "additional expected harm at severe scale", "relative to a baseline without generative AI" (v3.0 L486). |
| Meta | "Catastrophic outcomes are outcomes that would have large scale, devastating, and potentially irreversible harmful impacts on humanity that could plausibly be realized as a direct result of access to frontier AI in the future" (2025 L1076–1078; 2026 L1597–1599). Entry criteria: Plausible, Catastrophic, Net new, Instantaneous or irremediable (2025 L550–575). |
| xAI RMF | "requests that pose a foreseeable and non-trivial risk of more than one hundred deaths or over $1 billion in damages from weapons of mass destruction or cyberterrorist attacks on critical infrastructure ('catastrophic malicious use events')" (L95–98). Replaced by TFAIA's ">50 people" in the 2025 FAIF, and gone in 2026. |
| Microsoft | "national security and at-scale public safety risks" (2026 L37–38); undefined. |
| Amazon 2026 | "significant public harm" (L60); undefined. |
| Cohere | Two categories: "Harm to individual users" and "Societal harm" (L221–224). Likelihood and severity are judged "in context" (L211–213). |
| NAVER 2.0 | Defined by what is protected: users, members of society and the AI service ecosystem, crossed with life and physical safety, economic value, and unjust discrimination (L147–219). |

**severity; likelihood / probability.** Mostly undefined. GDM v3.0 lists "the likelihood and consequences of model misuse" as safety-case factors (L381–383). Meta 2025 uses neither word (0/0).

| Framework | Use |
|---|---|
| NVIDIA | Defined only through its scales (Table 1, L220–240). Likelihood = frequency (4 levels). Severity = duration + speed of onset. Observability = detectability + predictability. |
| Shanghai | Only inside the definition of risk (L2128–2129). |
| Cohere | Illustrative verbal grades per harm ("High, there is a large body of research …", L230–280). |
| Stelling (analysis) | "probability × severity per unit time" (L1921). It reports that no provider expresses a tolerance this way (L875). |

**capability**

| Framework | Use |
|---|---|
| GDM | Undefined as a word, but scoped: "when we refer to a model's capabilities, we include capabilities resulting from any reasonably foreseeable fine-tuning and scaffolding to turn the model into a functioning system" (v1 L210–211). |
| Meta | "Enabling capabilities are a set of capabilities that are identified as essential to enabling the realization of a threat scenario" (2025 L1091–1092). |
| Microsoft 2025 | "Frontier capabilities are defined as a significant jump in performance beyond the existing capability frontier in one advanced general-purpose capability or beyond frontier performance across the majority of these advanced general-purpose capabilities" (footnote, L194–195). Removed in 2026 (Zhu MSFT-1-008, zhu L1107–1121). |
| Cohere | Idiosyncratic: risks "that have a high likelihood of occurring based on the types of tasks LLMs are highly performant in, as well as the limitations inherent in how these models function. This is what we refer to as 'model capabilities.'" (L174–176) |
| Shanghai | "Capabilities: The range of tasks or functions an AI system can perform, and the level of proficiency it demonstrates in performing them." (L2112–2113). Plus "Enabling Capability (C)" (L272–277) and a list of named capabilities (L2537–2604). |

**threshold, level, tier**

| Framework | Use |
|---|---|
| GDM v3.1 | "Critical Capability Levels (CCLs): … the capability levels at which, absent mitigation measures, frontier AI models or systems may pose heightened risk of severe harm" (L847–849). "Tracked Capability Levels (TCLs): … heightened risk of significant but not severe levels of harm" (L851–853). "Alert Thresholds: are thresholds which we set marginally earlier than our CCLs" (L855–858). Earlier versions also have *security levels* (RAND-indexed) and, in v1, *deployment levels*. |
| Meta | "Risk thresholds" (above). The levels Critical / High / Moderate or lower are defined only in Table 1 (2026 L507–552). The operative predicate changed from "uniquely enable" to "substantially contribute to" (2026 L1616–1620, L1675–1677). |
| Microsoft | "capability thresholds and corresponding risk levels" (low / medium / high / critical), defined by table (2026 L468–575). |
| Amazon 2026 | "Critical Capability Thresholds describe model capabilities that could enable this significant harm" (L61–62). One per domain. |
| G42 | "Capability thresholds establish points at which an AI model's functionality requires substantially enhanced safeguards" (L54–56). Deployment Mitigation Levels and Security Mitigation Levels are separate ladders. |
| Shanghai | "red lines" = "absolute thresholds for unacceptable outcomes that pose intolerable risks" (L712–713). "yellow lines" = "early warning indicators" (L700–701, L745–748). "Zones" (green / yellow / red) sort residual risk (L1386–1401). |
| NVIDIA | "Model risk (MR) score between 1 and 5" (L53). "The MR score is correlated to the maximum permissible harm relative to our trustworthy AI principles" (L71). A *product* category, not a capability threshold. |
| Stelling (analysis) | "Capability Thresholds: Defined levels of AI system performance that, when reached, require implementation of specific mitigation measures" (L1875–1876). Also KRI and KCI (L1888–1895). |

**incident, event.** Used but undefined everywhere in the frameworks. The senses differ:

| Framework | Use |
|---|---|
| GDM v3.1 | "incidents relating to our frontier safety risk domains" (L227–228). |
| Microsoft 2026 | "serious or critical incidents that may pose public safety or national security risks" (L347–348). |
| Amazon 2026 | "AI safety incidents" (L231). |
| xAI 2026 | "serious AI safety incidents" (L360–361). |
| Meta 2026 | "unexpected tail events … critical incidents" (L394–397). |
| G42 | "Incidence Response" is about **non-compliance with the framework**: "in the event of non-compliance" (L410–411). Also "'near miss' incidents" as an input to review (L84–85). |
| TFAIA via xAI 2025 FAIF | "arising from a single incident involving a frontier model" (L35). |

**loss of control.** The terms collide on category: outcome, capability, situation, or risk.

| Framework | Use |
|---|---|
| NAVER 2024 | "AI systems causing severe disempowerment of the human species" (L69–71). Gone in 2.0. |
| GDM | Not a domain name. v2: "'deceptive alignment,' we mean the risk that AI systems purposefully undermine human control over AI systems" (L324). v3.0: "general-purpose AI agents are potentially misaligned and can become difficult to control" (L63–65). Blog: "interfere with operators' ability to direct, modify or shut down" (L45–47). |
| Meta 2026 | "a situation where humans lose—and cannot feasibly regain—the ability to direct, modify, contain, or shut down AI systems which have potential for significant real-world impact" (footnote 4, L826–828). Operationalised as failures of "control mechanisms" (L795–797). |
| Microsoft 2026 | A **model ability**: "A model's ability to undermine effective human control through adaptive, deceptive, or self-reinforcing mechanisms such that, when deployed, a model can no longer be reliably directed, modified, or shut down." (L101–103) |
| Amazon 2026 | A **risk domain**: "risks that could arise from a model's ability to autonomously execute long-horizon, expert-level tasks that could undermine the ability to direct, modify, or shut down the model" (L122–124). |
| xAI | RMF: "loss of control of advanced AI systems … difficult to pinpoint particular risk scenarios" (L255–256). 2026: "risks from humans losing the ability to reliably direct, modify, or shut down a model" (L25–26). |
| TFAIA via xAI 2025 FAIF | "(C) Evading the control of its frontier developer or user." (L44) |
| Shanghai | "Loss of control scenario: A scenario in which one or more general-purpose AI systems come to operate outside of anyone's control, with no clear path to regaining control" (L2116–2117). Distinguishes "passive loss of control (gradual reduction in human oversight) and active loss of control (AI systems actively undermining human control)" (L378–380). |

**safeguard, mitigation, control.** Used interchangeably by most frameworks. "Mitigation" is by far the most frequent word (GDM v3.1: 132 occurrences).

| Framework | Use |
|---|---|
| GDM v3.1 | "Deployment Mitigations: are safety measures we implement which are intended to counter the misuse or misaligned expression of critical capabilities in deployments" (L899–900). "Security Mitigations: are safety measures we implement which are intended to prevent the unauthorized modification or exfiltration of model weights by unauthorized actors" (L918–919). |
| Amazon 2026 | "Safeguards" in three families: Abuse, Security and Misalignment (L202–288). "Risk Mitigations" is the umbrella (L43–45). |
| Meta 2026 | **Control** = "control mechanisms—that is, technical and organizational measures which enable us to direct, modify, contain, or shut down AI" (L795–797). |
| Shanghai | **Control** is a human ability: "Control: The ability to supervise an AI system and intervene to adjust or stop its behavior when it acts inappropriately." (L2114–2115) |
| NVIDIA | **Controls** are the measures applied per hazard (Table 2, L283–292). "Controllability" is a risk attribute (L204). |
| Stelling (analysis) | Three families: "Containment Measures" (security, L1880–1883), "Deployment Measures" (L1884–1887) and "Assurance Processes" ("affirmative evidence that an AI model will not cause harm", L1865–1869). |

**developer, provider, deployer.** Mostly unused: frameworks speak as "we". Where the words appear, they are undefined.

| Framework | Use |
|---|---|
| Microsoft 2026 | "downstream actors integrating models into systems, including external system developers and deployers" (L142–144). |
| xAI 2026 | "downstream modifiers, downstream providers" (L370), EU vocabulary. |
| NVIDIA | "providers of AI systems" vs "providers of foundation models" (figure captions L124, L138). |
| Shanghai | Addresses "general-purpose AI developers" / "model developers" throughout (e.g. L26–31). |
| TFAIA via xAI 2025 FAIF | "frontier developer" (L32–33). |
| Stelling (analysis) | Coins "Providers" for the companies (L221). Zhu also says "provider". |

**alignment, misalignment**

| Framework | Use |
|---|---|
| GDM | "deceptive alignment" (v2 L324, quoted above). Misalignment is "exploratory" (v3.0 L137–143), later merged into "ML R&D and Misalignment" (v3.1 L842–844). Gemini report: "'scheming (also known as deceptive alignment), where a model knowingly and covertly pursues objectives misaligned with its developer's intention" (L1447–1449). |
| Amazon | 2025: "Alignment Training: We implement automated methods to ensure we meet the design objectives for each of Amazon's responsible AI dimensions" (L152–153). 2026 adds "To contain model misalignment, we identify a model persona that ensures that the model emphasizes ethical practices" (L276–277). |
| xAI | "incidental alignment resulting from post-training (our models naturally tend to refuse malicious requests …)" (RMF L228–229; 2026 L299–300). "value systems that are misaligned with humanity's interests" (RMF L259–260). |
| Google responsibility update | "User Alignment Critic … vetoing actions that do not align with the user's specific intent" (L148–151). |
| Shanghai | "Misalignment: The tendency of an AI system to use its capabilities in ways that conflict with human intentions or values. Depending on the context, this may refer to the intentions and values of developers, operators, users, specific communities, or society at large." (L2120–2122). "Deceptive alignment: A difficult-to-detect form of misalignment in which the system behaves benignly—at least initially—while concealing harmful intentions." (L2123–2124) |
| METR (analysis) | "Deceptive alignment: AI models that intentionally deceive its developers by appearing aligned with their objectives when monitored, while pursuing the AIs' own conflicting objectives in secret." (L362–364) |

**Other terms the model builds on**

| Term | Definitions |
|---|---|
| **frontier AI / frontier model** | GDM v3.1: "are trained on a large data set, display significant generality, are capable of performing a wide range of distinctive tasks and have high-impact capabilities. Frontier AI models' agentic and reasoning-based general capabilities near or exceed those of other Google models" (L824–826).<br>Meta 2025: "models and systems … that exceed the capabilities present in the most advanced models" (L1071–1073). Meta 2026 replaces this with a capability test *or* ≥10^26 FLOP (L1580–1595).<br>NVIDIA: "a highly capable general-purpose AI model that can perform a wide variety of undefined tasks and exceeds the capabilities present in the most advanced models currently in existence" (L23–25).<br>Shanghai: "particularly capable general-purpose AI" (L2056–2058).<br>Buhl, after the Seoul commitments: "match or exceed the capabilities present in the most advanced models" (L79–81). |
| **uplift** | Amazon 2025: "'Uplift' can be quantitatively assessed through uplift studies, which use controlled trials to compare the abilities of a group with access to the frontier model to the abilities of a group without access" (L101–104).<br>Meta: "Uplift studies are experiments that assess the extent to which access to frontier AI increases a person or group's ability to complete a particular task or scenario in comparison to a control group that only has access to existing resources, such as textbooks, the internet, and existing AI models" (2025 L1168–1174).<br>The baseline differs by framework (§4). |
| **uniquely enable / substantially contribute** (Meta) | "Uniquely enabling describes a model that is an essential controlling factor in a given outcome. A model is considered to meet the critical risk threshold if it is determined that a specified threat scenario would not occur without this particular model." (2025 L1094–1097)<br>"Substantially contribute means that the model is a material factor in a given outcome." (2026 L1616–1617) |
| **threat scenario / threat model** | Meta 2025: "Threat scenarios describe how different threat actors might achieve a catastrophic outcome" (L1085–1086). Meta 2026 revises this to "the real-world events – including enabling capabilities, deployment context, and threat actors (as relevant) – that may be sufficient to produce a catastrophic outcome" (L1605–1607).<br>Magic: "We use the term threat models to refer to proposed mechanisms via which AI systems could cause a major catastrophe in the near future." (L128–129) |
| **safety case** | GDM: "an assessable argument showing how severe risks associated with a model's CCLs have been minimised [v3.1: reduced] to an appropriate [v3.1: acceptable] level" (v2 L216–217; v3.1 L943–944). |
| **misuse** | GDM: "risks of threat actors using critical capabilities of deployed or exfiltrated models to cause harm" (v2 L50–51; v3.0 L60–61). |
| **sandbagging** | Gemini report: "deliberate underperformance in order to avoid being flagged as dangerous" (L171–172). |
| **deployment (types)** | Company-specific, defined in glossaries: GDM v3.1 L904–916; Meta 2025 L1131–1152; Meta 2026 L1634–1647. |

---

## Closing note: against Joseph's chain

*Sources & causes → preventions & controls → risk-events × impact radius → mitigations & recovery → policies & decision-making*

- **The framework models the developer's decision, not the risk process.** Its one tracked variable is a *capability of the model*. Causes, actors and pathways appear only inside threat modelling that sets the threshold, and that modelling is usually withheld. So the framework sits almost entirely at the last link, "policies & decision-making", with a gate reaching back to "preventions & controls" (security and deployment safeguards).
- **Risk events and impact radius are compressed into the threshold's wording.** "Severe harm", "mass casualty", ">100 deaths". Harmed groups are rarely named. NAVER 2.0's protected subjects and Shanghai's E-T-C are the partial exceptions.
- **Mitigation & recovery after an event** is nearly absent: incident response is a governance line item.
- **The line-up is closest in three places.** Meta's outcome → scenario → enabling capability, Shanghai's E-T-C, and the bottleneck reasoning in xAI and the Gemini report each run *backwards* along a chain like Joseph's, from harm to the model property that could enable it. This backward pass is the genre's implicit causal model. It shows only in fragments (tables, footnotes, withheld scenarios).
