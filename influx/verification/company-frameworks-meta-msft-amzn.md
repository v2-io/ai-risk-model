# Company frameworks: Meta, Microsoft, Amazon

*Evidence file for the integrator of `influx/safety-risk-factors.md`. Written 2026-09-27 by a Claude (Opus 5.5) fork working under the company-frameworks agent. That agent covers Anthropic, and sibling forks cover OpenAI, Google DeepMind, and xAI / Naver / the rest. The report itself was not edited.*

**What was read, in full.**
- **Meta:** *Advanced AI Scaling Framework*, Version 2 (Apr 2026, 44 pp.).
- **Microsoft:** *Frontier Governance Framework*, February 2026 edition (16 pp.).
- **Amazon:** *Frontier Model Safety Framework*, September 2026 update (11 pp.). This is newer than any version the report, METR, SaferAI or Zhu (2026) saw.
- **Prior versions, for the version-to-version comparison:** Meta *Frontier AI Framework* v1.1, Microsoft FGF v1, Amazon FMSF Feb 2025. I read these for the passages compared, not cover to cover. The copies come from the hash-pinned Zhu (2026) corpus (`zhu-2026-silent`).
- **Hashes.** The Meta v2 and Microsoft 2026 files I retrieved have the same SHA-256 prefixes as Zhu's manifest (`d87aa9bf`, `3282e4fc`). So neither has been silently re-uploaded since Zhu collected them.

**Page conventions.**
- **Meta and Microsoft:** printed page numbers.
- **Amazon 2026:** printed page numbers plus the document's own margin line numbers ("l.").

**Tags** are the report's: \[P] primary read, \[S] secondary, \[F] web-fetch extraction, \[C] commentary. **Role and force codes** are the report's, plus the company-framework force codes proposed in §1.

---

## 0. Headline findings

1. **Amazon updated its framework on or about 17 Sep 2026, with no change log.** This is the PDF CreationDate. The amazon.science page now links only the new PDF (`amazon-fmsf-9-2026.pdf`), and the Feb 2025 URL returns 404.
   - The Critical Risk Domains changed from {CBRN, Offensive Cyber, **Automated AI R&D**} to {CBRN, Offensive Cyber, **Harmful Manipulation**, **Loss of Control**}. Automated AI R&D now appears only *inside* the Loss of Control threshold ("including, but not limited to, the research, development, and deployment of frontier models").
   - The uplift **baseline** moved from "beyond other publicly available research or tools, such as internet search" to "beyond other publicly available models in known harnesses" (see §5).
   - A new "Misalignment Safeguards" category appears.
   - METR, SaferAI and Zhu all describe the Feb 2025 text. Zhu's manifest records "No revision published as of 2026-09-02".
2. **Meta's v2 change log states, in Meta's own words, the change FLI describes as a weakened pause pledge.** The change log reads: "Critical threshold changed from 'Stop' to 'Develop with Mitigations.' High threshold measure changed from 'Do not release' to 'Deploy with mitigations.'" (p.44).
   - What v2 still commits to is a *condition on continuing*, not a stop: "we will only continue development of the Frontier AI if our risk assessments are complete and safeguards are defined, implemented and validated to reduce risk to the moderate or lower risk threshold" (p.17).
   - The same revision *lowered* the bar for reaching Critical, from "uniquely enable" to "substantially contribute to" (p.44).
   - The announcement post describes the revision as one that "strengthens how we make deployment decisions" \[F].
   - None of the three frameworks contains a competitor-contingent clause, so FLI's "some citing competitor-contingent conditions" does not apply to these three.
3. **Microsoft keeps an unconditional pause and states that the frameworks serve the new laws.** "If, during the implementation of this framework, we identify a risk we cannot sufficiently mitigate, we will pause development and deployment until the point at which mitigation practices evolve to meet the risk" (p.8).
   - Its scope clause names "the EU AI Act, California's Transparency in Frontier AI Act (TFAIA), and New York's Responsible AI Safety and Education (RAISE) Act" (p.5).
   - Its change log says the Feb 2026 revision followed "finalization of the EU Code of Practice … NY RAISE Act and CA Transparency in Frontier Artificial Intelligence Act" (p.15).
4. **Meta v2 names organizational measures as the thing whose failure constitutes loss of control, and names the developer's evaluation capacity being outpaced as a threat scenario.** These are organizational factors appearing *inside a company framework*, and they bear on §2(c)/§4:
   - Meta scopes Loss of Control as "failures of critical control mechanisms—that is, technical and organizational measures which enable us to direct, modify, contain, or shut down AI" (p.22).
   - LoC threat scenario TS.1.1 reads: "AI development accelerates such that new capabilities and behaviors emerge faster than the organization's evaluation processes" (pp.22–23).
   - Among emerging threats (p.38): "AI becomes deeply integrated into organizational operations"; and "long-term dependency of AI for supervisory functions leading to skill atrophy".
5. **None of the three names growth, headcount, turnover, investor pressure or an IPO** as a factor, trigger or indicator. Searched terms: turnover, headcount, investor, shareholder, competit*, race, IPO, reorgani*, restructur*. This agrees with the report's METR-based note (§4, "Company frameworks") and now covers these three companies' current texts directly.
   - **Nearest items:**
     - Meta's commercial qualifier on Critical-level weight security, "insofar as is technically feasible and commercially practicable" (p.15).
     - Microsoft's benefit test at the deployment decision, "the marginal benefits of a model outweigh any residual risk" (p.9).
     - Meta's §4.3 "Benefits Assessment".
   - **Reassessment triggers are all technical or calendar-based** (§6 below). Meta copies the EU Code's Measure 1.3 adequacy/adherence test nearly verbatim but not its example grounds, which include "(1) how the Signatories develop models will change materially".

---

## 1. What a company framework binds, and a proposed force coding

The report's force codes don't yet have a code for a developer's own framework. I'd suggest two, applied per clause:

| Code | Meaning |
| --- | --- |
| *self* | A commitment in the developer's own published framework, stated as "will", "must", "requires" or an unhedged present tense. It is self-imposed and revisable by the developer. |
| *self-d* | The same, but discretionary on its face: "may", "as appropriate", "where appropriate", "e.g.", "we expect", "we aim", "insofar as … commercially practicable", "is developing". |

**The legal overlay** depends on which document a developer uses to meet a statute or code. Only then does *self* acquire *law* or *commit* backing:
- **SB 53** §22757.15(a): a large frontier developer that "fails to comply with its own frontier AI framework shall be subject to a civil penalty … not exceed[ing] one million dollars ($1,000,000) per violation" (relata `california-2025-sb53`).
- **SB 53** §22757.12(b)(2): a material modification must be published "and a justification for that modification within 30 days".
- **EU Code**, Commitment 1: signatories must maintain a Safety and Security Framework.

| Company | Current document (date) | SB 53 designation | EU Code | Tag |
| --- | --- | --- | --- | --- |
| Meta | Advanced AI Scaling Framework v2 (7 Apr 2026; announced 8 Apr) | Not stated in the document or the announcement. The content tracks SB 53 (see note). Vorp Labs: "No public statement found as of 2026-07-04, despite Meta plausibly meeting both statutory thresholds." | Not a signatory (report §3). Vorp Labs: "Meta publicly declined to sign." | P; S/F for Vorp |
| Microsoft | Frontier Governance Framework, Feb 2026 (hash = Zhu `feb-2026`) | The framework names TFAIA in its scope clause (p.5) and change log (p.15), and adopts the 30-day publication rule. It does not use the words "frontier AI framework under §22757.12". | Signatory (report §3). The change log cites the Code's finalization. | P |
| Amazon | Frontier Model Safety Framework, Sep 2026 (unversioned; no change log) | Not stated. The document "account[s] for relevant laws and regulations" (p.1) and commits to "publish any material modifications" (p.7). | Signatory (report §3) | P |

**Meta, note.** Meta v2's content maps onto SB 53 almost element by element, but Meta never cites the statute:
- The compute trigger is "at least 10^26 integer or floating point operations (to include material modifications to the model through fine-tuning, reinforcement learning training, and other training steps)" (p.41). Compare SB 53 §22757.11(i).
- It adds an "internal-use risk report" to "relevant authorities" (p.9). Compare §22757.12(d).
- It adds whistleblower protocols for "any specific and substantial danger to the public health or safety arising from catastrophic risk" (p.10), which is SB 53's whistleblower language.
- On updates: "we will publish a timely update that includes a justification for the modification" (p.40).
- The update test copies EU Code Measure 1.3 ("when we have reasonable grounds to believe either its adequacy or our adherence to it has been materially undermined, or at least every twelve months, whichever is sooner", p.40), although Meta is not a signatory.

*Inference, not verified:* v2 looks drafted to satisfy SB 53 without saying so. Whether it is Meta's §22757.12 framework is unknown from public text.

**What this means for coding.** For all three, I've coded clauses *self* / *self-d*. The integrator may want a column note: "*self* clauses may be law-backed under SB 53 §22757.15 if this is the developer's designated frontier AI framework. Microsoft's text points that way; Meta's and Amazon's are silent."

---

## 2. §2(a) hazards crosswalk

**Recommendation: one column per company framework, or one grouped "Company frameworks (current)" block.** These documents now define the hazard categories that SB 53 and the EU Code rely on, and three of the four EU specified risks appear in them nearly verbatim. Cells use the report's legend.

| # | Meta v2 | MSFT 2026 | AMZN Sep 2026 | Notes |
| --- | --- | --- | --- | --- |
| A1 CBRN | E¹ | E | E | ¹Meta: chem & bio only. "Radiological and nuclear" is an *emerging* outcome: "materials access is a strong bottleneck to nuclear risk" (p.36). |
| A2 Cyber | E | E | E | |
| A3 Loss of control | E | E² | E | ²MSFT tracks it but sets no threshold yet: "We are researching approaches to evaluating models for loss of control risk … and setting appropriate risk acceptance criteria" (p.14). Amazon 2025 had no LoC domain. |
| A4 Harmful manipulation | — | E² | E³ | ²MSFT: same "studying and progressing methods" status (p.14), plus a usage-policy prohibition. ³Amazon: "an emerging area of research and evaluation" (p.2, l.83–84). Amazon 2025 had no manipulation domain. |
| A5 Criminal misuse | E⁴ | P⁵ | P⁶ | ⁴Meta Cyber 3: "Large-scale casualties or significant financial loss to individuals or organizations via scaled long form fraud, extortion, and scams" (p.19). ⁵MSFT cyber Medium: "low-level spoofing, phishing, or social engineering attacks" (p.12). ⁶Amazon manipulation domain: "including social engineering or fraud" (p.2, l.81–82). |
| A6 Malfunctions | — | — | — | |
| A7 Critical infrastructure | D⁷ | P | P | ⁷Meta, emerging "Physical autonomy": "AI which operates physical infrastructure, such as water treatment facilities, power grids …" (pp.36–37). MSFT cyber: "including on critical infrastructure" (p.3). Amazon cyber threshold: "autonomously extend control over critical infrastructure systems" (p.2). |
| A8 Labour | — | — | — | |
| A9 Power concentration | — | — | — | |
| A10 Military | — | — | — | Meta's drone-swarm scenario is about autonomy, not strategic stability. |
| A11 Over-reliance | P⁸ | — | — | ⁸Meta, emerging LoC mechanism: "long-term dependency of AI for supervisory functions leading to skill atrophy" (p.38). |
| A12 Privacy | — | — | — | |
| A13 IP | — | — | — | |
| A14 Bias | — | P⁹ | — | ⁹MSFT: residual risks "for example relating to bias or discrimination" are left to deployers (p.8). |
| A15–A16 | — | — | — | |
| A17 Multi-agent | — | — | — | |
| A18 AI welfare | — | — | — | |

**Scope statements** (for the "X vs —" judgement; none is item-specific, so I've used "—"):
- **Meta:** harms that "unfold gradually or be partially remediable … are addressed through other safety and integrity processes outside of the scope of this Framework" (p.14).
- **Microsoft:** non-tracked risks "are addressed through our broader AI governance and risk management framework" (p.3).
- **Amazon:** the framework "complements Amazon's broader approach to responsible AI … across eight key dimensions" (p.1).

---

## 3. §2(b) model and system factors: proposed additions

| Row | Addition (role, force) |
| --- | --- |
| B1 Dangerous general capabilities | **MSFT** "Advanced autonomy. A model's ability to complete expert-level tasks autonomously, including AI research and development" (p.3). The Critical level: "The model can fully automate the AI R&D pipeline at a fraction of human labor costs, and majorly accelerating AI R&D" (p.13) (F). MSFT leading-indicator precursors: general, scientific and long-context reasoning, spatial awareness, "Autonomy, planning, and tool use", "Advanced software engineering" (p.4) (I). **Meta** LoC checkpoint: SWE tasks "which would take a human professional familiar with such tasks two or more hours" (p.34) (I *self*). Meta fn 8 operationalizes "substantially accelerating from historical rates" as benchmark saturation within six months, across domains, for two benchmarks in 18 months (p.35) (I). **Amazon** LoC threshold: "autonomously planning and executing complex sequences of expert-level tasks (including, but not limited to, the research, development, and deployment of frontier models) in such a way that would impair the ability to direct, modify, or shut down the model" (p.3) (F). |
| B2 Harmful propensities | **Meta** propensity risk-acceptance criteria: "at least 40% on MASK and at most 50% on Agent Misalignment", described as "an illustrative example" and "subject to revision" (pp.35–36) (M *self-d*). Meta commits to publish a model spec covering "acquiescence to shutdown and lack of coercive power-seeking behavior", and to publish adherence evaluations (p.9) (M *self*). **Amazon**: "rigorous measurement of a model's propensity for deception" (p.3) (M *self*); the new "Misalignment Safeguards" (p.5) (M *self*, described practice). **MSFT** LoC definition: "adaptive, deceptive, or self-reinforcing mechanisms" (p.3) (F). |
| B5 Evaluation gap / test-awareness | **Meta** LoC 1 TS.1.2: "AI performance in testing environments consistently fails to predict deployment behavior", enabled by "Evaluation awareness" and "Selective evaluation-adaptive behavior" (p.23) (F). Meta §4.1: evaluations "are held out from teams conducting training to reduce the risk of overfitting" (p.25) (M *self*). Meta elicitation: "a generous token budget, up to the maximum context length or to the point at which performance plateaus" (p.27) (M *self*). **MSFT**: each evaluation includes "a statement on the robustness of the evaluation method used … and any concerns about the effectiveness or validity of the evaluation" (p.6) (M *self*). MSFT: "Resources applied to elicitation should be extrapolated out to those available to actors in threat models" (p.6) (M *self-d*, "should"). **Amazon**: "maximal capability evaluations" (p.3) (M *self*). |
| B6 Brittle safeguards | **Meta** BioTIER: risk acceptance "at least 80% refusal or safe responses, and 40% … against all adversarial attacks within a typical adversarial attack portfolio" (p.33), as "an illustrative example" (M *self-d*). Meta adversary model: for open-weight releases, "adversaries capable of modifying model behavior through continued training" (p.27) (M *self*). **MSFT** harm refusal: "an area of active research" (p.8) (M *self-d*). **Amazon** fine-tuning safeguards (p.4) (M *self*). |
| B7 Weight security | **MSFT** High level: "security measures protective against most cybercrime groups and insider threats" (p.7) (M *self*). MSFT Critical level: requirements "will likely include … hardened tamper-resistant workstations … and physical bandwidth limitations" (p.7) (M *self-d*). MSFT cites NIST SP 800-53 and RAND's *Securing AI Model Weights* (p.7), and "reference[s] the RAND security level framework as a benchmark" (p.10). **Meta** Critical level: heightened access controls "insofar as is technically feasible and commercially practicable" (p.15) (M *self-d*). Meta v1.1's Critical measure was "Access is strictly limited to a small number of experts" (Table 1, §3.3); v2 has no number or "small number" language. **Amazon**: AES-256, FIPS 140-3 KMS, and Critical Permission Groups (p.5; App. A) (M, described current practice). |
| B8a Human insiders | **Amazon** App. A: "Workforce vetting and careful monitoring for insider threats. Employment at Amazon requires background checks (to the extent allowed under local law)"; access "monitored for unusual access patterns" (p.8, l.324–329) (M, described practice). Amazon's "insider threat teams are building additional capabilities" (p.6) (M *self-d*). **MSFT**, as in B7 (p.7). **Meta**: "internal and external threat actors" (p.27) (M *self*). |
| B8b AI as insider / self-exfiltration | **Amazon** LoC: "Loss of control could arise in circumstances where a model is capable of self-exfiltration, autonomous resource acquisition, or unauthorized replication" (p.3, l.89–90) (F). **Meta**, emerging: "weight exfiltration by exploiting security vulnerabilities (e.g., self-exfiltration during evaluation or deployment)"; "autonomous acquisition of resources … including through autonomous replication" (p.38) (F; *res*-like). **Meta** LoC 2: "AI disables or corrupts monitors" and "AI evades monitors" (pp.23–24) (F). |
| B9 Open weights | **Meta**: release types include "Open release: releasing weights externally" (p.42), and weight sharing is presented as a transparency benefit "consistent with the processes set out in this Framework" (p.7) (desc). *Zhu (2026) \[S] codes v1.1's "we intend to continue to openly release models to the ecosystem" as removed silently in v2 (META-1-022). My v1.1 extract matched its "open source" sentences, so this is consistent, but I did not re-verify that exact sentence.* **MSFT** holistic assessment: "marginal capability uplift … over and above currently available tools and information, including currently available open-weights models" (p.6) (M *self*). |
| B10 Reach / scale | **MSFT** scope trigger: models "in scope for frontier model requirements under applicable laws", and fine-tunes using "more than 1/3 of the base model" compute (p.5) (T *self*). **Meta**: "Compute Threshold … at least 10^26" (p.41) (T *self*). |
| B13 Opacity | **Meta** preparedness reports will disclose "changes to the training process that reduce interpretability (including e.g., evidence that the training process may cause obfuscation of a model's reasoning)" and "reward hacking or scheming" (p.9) (M *self*, disclosure). |
| B14 Attacks on AI systems | **Meta**: prompt-injection evaluations "within common agentic use cases"; LlamaFirewall (p.30) (M *self*). **Amazon** input moderation against "prompt injection, jail-breaking" (p.4) (M). |
| *New? Internal deployment* | **Meta**: "Loss of Control risks may occur with similar probability with any type of deployment, including internal deployment" (p.18) (F). Meta's internal-use risk report is given to "relevant authorities", "as appropriate" (p.9) (M *self-d*). **MSFT**: none found. **Amazon**: none found. *The report has no row for internal deployment. It sits across B8b and SB 53 §22757.12(a)(10); the integrator may want to decide where it goes.* |

---

## 4. §2(c) and §4 organizational rows: proposed additions

| Row | Addition (role, force) |
| --- | --- |
| C6 Safety / risk culture | **MSFT** "reinforces the importance of speak up culture" in its annual Trust Code course (p.9) (M, desc). **Amazon** App. A, "Culture of security": "'see something, say something' as well as 'when in doubt, escalate' and 'no blame' principles" (p.8, l.320–323). This is *security* culture, a fourth construct beside the three the C6 row already separates (M, desc). **Meta**: none. |
| C7 Internal risk governance | **Meta** §2.3: "'Lines of Defense' risk management model"; the Chief AI Officer "oversees the design, implementation, and operation"; the Director of Alignment and Risk "bears responsibility for executing the lifecycle"; "Meta's Board of Directors provides oversight" (p.10). Deployment is approved by the CAIO or the Director (p.7) (M *self*). *Unlike EU Code Measure 8.1, the risk owner and the risk executor share one reporting line: the CAIO "supervises" the Director.* **MSFT**: "Executive Officers responsible for Microsoft's AI governance program (or their delegates)" make the final decision (p.9); the framework is "subject to … independent internal audit and board oversight" (p.9); external evaluator involvement "is made by internal experts who are independent from the model development team" (p.6) (M *self*). **Amazon**: over-threshold results go to "the SVP for the model development team and the company's Chief Security Officer", who "review the safeguards evaluation report as part of a go/no-go decision" (p.7) (M *self*). Framework updates are "reviewed by the SVP …, the Chief Security Officer, and legal counsel" (p.7). |
| C8 Resourcing | **Meta**: "The Chief AI Officer will ensure that the Director of Alignment and Risk has resources, including human, financial, and computational resources, sufficient to perform state-of-the-art risk mitigation and assessment" (p.10) (M *self*). The wording is close to EU Code Measure 8.2 (a non-signatory adopting it). **MSFT, Amazon**: none. |
| C9 Whistleblowing | **Meta**: "is developing further protocols to report any instances of non-compliance … Under this protocol, employees will be able to confidentially, and, if they choose, anonymously issue reports … all employees who in good faith report non-compliance or decline to engage in unlawful conduct will be explicitly protected from adverse employment action and retaliation" (p.10). This is a *future* protocol; I'd code it M *self-d*, with the protection itself *self*. **MSFT**: "Employees who raise concerns are protected from retaliation", with "an option for anonymous reporting" (p.9) (M *self*). **Amazon**: "employee escalation" as an incident-detection channel (p.4) (M, desc); no anti-retaliation text. |
| C10 Safetywashing (O, both quotes for the reader) | **Meta**, change log: "Critical threshold changed from 'Stop' to 'Develop with Mitigations.' High threshold measure changed from 'Do not release' to 'Deploy with mitigations'" (p.44). **Meta**, announcement: v2 "strengthens how we make deployment decisions" \[F]. Both are primary statements, and the reader can compare them directly. *No adjudication proposed.* |
| C11 Commercial pressure | Not named as a factor. It enters as *decision criteria*. **MSFT** deployment case includes "the marginal benefits of a model outweigh any residual risk" (p.9) (M *self*). **Meta** §4.3 "Benefits Assessment" (p.39) (desc); Critical-level security "insofar as is technically feasible and commercially practicable" (p.15) (M *self-d*). |
| C13 Evidence dilemma | **Meta**: "there remains quite considerable divergence in expert opinion as to how AI capabilities will develop and the time horizons on which they could emerge" (p.13) (F); "we cannot claim to have anticipated all potential threat scenarios. There is always a potential for 'unknown unknowns'" (fn 3, p.13). |
| C15 Organizational change / pace vs capacity | **Meta** LoC 1 TS.1.1: "AI development accelerates such that new capabilities and behaviors emerge faster than the organization's evaluation processes" (pp.22–23) (F; H under LoC). This makes the organization's evaluation capacity one side of a threat scenario. **Meta**, emerging: "Loss of human oversight capacity … AI becomes deeply integrated into organizational operations" (p.38) (F). **Meta** defines control mechanisms as "technical and organizational measures" (p.22) (F). None of these is a *growth or headcount* provision. |
| C16, C17 | None in any of the three. |

**§4 table, cells to add (proposed):**
- C6 M: MSFT speak-up (desc); Amazon security culture (desc).
- C7 M: Meta, MSFT, Amazon (*self*).
- C8 M: Meta (*self*).
- C9 M: MSFT (*self*); Meta (*self-d*/*self*).
- C15 F: Meta LoC TS.1.1 (org evaluation capacity outpaced).
- T: none from these three.

---

## 5. §5 terminology: definitions record (verbatim)

**Loss of control.** Add to the §5.2 ladder. All three sit near EU App. 1.4(2), but at different scales.
- **Meta** fn 4 (p.22): "When we refer to Loss of Control in this Framework, we refer to a situation where humans lose—and cannot feasibly regain—the ability to direct, modify, contain, or shut down AI systems which have potential for significant real-world impact." *Irreversibility is built in; there is no harm threshold.*
- **Meta** fn 5 (p.22): "we assume that catastrophic harm would eventually materialize as a result of an AI system ceasing to perform as intended."
- **Meta**, scoping (p.22): "we focus on outcomes corresponding to failures of critical control mechanisms—that is, technical and organizational measures which enable us to direct, modify, contain, or shut down AI". *This is a control-mechanism-failure scale; the ladder has no entry of this kind.*
- **MSFT** (p.3): "Loss of control. A model's ability to undermine effective human control through adaptive, deceptive, or self-reinforcing mechanisms such that, when deployed, a model can no longer be reliably directed, modified, or shut down." *A capability; "when deployed".*
- **Amazon** (p.3, l.87–90): "risks that could arise from a model's ability to autonomously execute long-horizon, expert-level tasks that could undermine the ability to direct, modify, or shut down the model (e.g., to prevent the model from engaging in harmful, malicious, or criminal actions). Loss of control could arise in circumstances where a model is capable of self-exfiltration, autonomous resource acquisition, or unauthorized replication." *Autonomy-based; subsumes AI R&D.*

**Harmful manipulation.** Add to §5.3.
- **MSFT** (p.3): "A model's ability to strategically distort human behavior or beliefs at scale."
- **Amazon** (p.2, l.80–82): "risks arising from models capable of enabling persistent, deceptive, or exploitative influence over public in ways that could reasonably result in large scale harm, including social engineering or fraud."
- **Amazon** threshold (pp.2–3): "systematically and substantially distort the beliefs or behavior of large populations or high-stakes decision-makers through multi-turn interactions with the model in ways that could reasonably be expected to cause severe harm."
- Both borrow the EU Code's App. 1.4(4) wording ("strategic distortion"; "large populations or high-stakes decision-makers").
- Amazon frames it as *misuse uplift to a malicious actor*. The EU Code and MSFT frame it as the model's own ability.

**Misalignment.** No framework defines it.
- **Amazon** uses "misaligned models with the potential to autonomously commit acts of harm against humans" (p.4, l.145).
- **Meta** uses "potential misalignment between its goal and that of its evaluators" (p.23) and "Agent Misalignment" (a benchmark, p.35).

**Critical capability / thresholds.**
- **Amazon** (p.2, l.49–53): "Critical Risk Domains cover domains in which advanced model capabilities could give rise to significant public harm through misuse or loss of control. Within each Critical Risk Domain, Critical Capability Thresholds describe model capabilities that could enable this significant harm." *There is one threshold per domain.*
- **MSFT** (p.6): "qualitative capability thresholds … offer important flexibility". The four levels are low/medium/high/critical (App. I).
- **MSFT** term "frontier capabilities" (p.5) is used without a definition. *Zhu \[S] records that v1 defined it and that the 2026 edition removed the definition (MSFT-1-008).*
- **Meta** (p.42): "Risk thresholds are the incremental levels of risk that a Frontier AI model might pose towards realization of a catastrophic outcome"; "Substantially contribute means that the model is a material factor in a given outcome"; "Uniquely enabling describes a model that is an essential controlling factor in a given outcome."
- **Meta** (p.41): "Catastrophic outcomes are outcomes that would have large scale, devastating, and potentially irreversible harmful impacts on humanity that could plausibly be realized as a direct result of access to Frontier AI in the future."
- **Meta** inclusion criteria (pp.13–14): "Plausible", "Catastrophic", "Net new" and "Instantaneous or irremediable". All four must be satisfied.

**Safeguards.**
- **Amazon** sorts mitigations into "Abuse Safeguards", "Security Safeguards" and "Misalignment Safeguards" (pp.4–5).
- **Meta**'s operative phrase is "safeguards are defined, implemented, and validated" (pp.1, 17).
- **MSFT** splits "Security measures" and "Safety mitigations" (pp.7–8).
- **Residual risk** (Meta p.42): "the level of risk that a Frontier AI model presents after mitigations have been implemented."

**Uplift baseline.** This is a divergence the report does not yet track; I'd suggest a §5 entry. The counterfactual against which "uplift" is measured differs:
- **Meta** "Net new" (p.14): "The outcome cannot currently be realized as described (e.g. at that scale / by that threat actor / for that cost) with existing tools and resources but without access to general-purpose AI." *The baseline is a world without general-purpose AI.*
- **MSFT** (p.6): "marginal capability uplift a model may provide over and above currently available tools and information, including currently available open-weights models." *The baseline includes today's open models.*
- **Amazon 2025**: "beyond other publicly available research or tools, such as internet search". **Amazon 2026**: "beyond other publicly available models in known harnesses" (p.2). *The baseline moved from the pre-AI web to current public models.*
- As public models improve, a relative baseline rises with them. *That is what the text implies; no source here states it.*

**Frontier AI** (Meta p.41). A model is "Frontier" if it is "reasonably likely to be more capable in any of the catastrophic risk domains … than our existing models or the most advanced models", or if it was trained with "at least 10^26" operations "or another threshold as may be defined by evolving standards or industry best practices".

---

## 6. Triggers for reassessment or framework update

| Company | Framework-update trigger | Model re-assessment trigger | Organizational trigger? |
| --- | --- | --- | --- |
| Meta | "when we have reasonable grounds to believe either its adequacy or our adherence to it has been materially undermined, or at least every twelve months, whichever is sooner" (p.40). Updates are "confirmed by our Director of Alignment and Risk and Chief AI Officer" (p.40) (T *self*). | Preparedness-report update "when there is a change in circumstances that materially alters our previous risk assessment", e.g. "a major incident" or "more affordances" (p.9). "expedited updates if we identify any unprecedentedly rapid increase in capabilities" (p.9). Threat modeling informed by "serious incidents, and near misses" (p.18) (T *self*). | None. The EU Code's example ground "(1) how the Signatories develop models will change materially" was not carried over. |
| MSFT | "At least every twelve months, we will have an explicit discussion on how this framework may need to be improved" (p.9). "All material revisions will be made public within 30 days of adoption" (p.9) (T *self*). *v1 said "Every six months" and published updates "Where appropriate".* | Leading-indicator assessment "at least every six months" (p.5). Deeper assessment "if there are material changes to the deployed model's risk profile" (p.6). *v1 required "at least once every six months"; Zhu \[S] codes the change as weakened, MSFT-1-015.* Fine-tuning above 1/3 of base compute (p.5) (T *self*). | None |
| Amazon | "revisit this Framework at least annually and publish any material modifications … We will also update this Framework as needed in connection with significant technological developments" (p.7) (T *self*). | "re-evaluate deployed models prior to any major updates that could meaningfully enhance underlying capabilities" (p.3). Lighter-touch recurring benchmarks "including after model launch" (p.4) (T *self*). | None |

---

## 7. §7 relative priority: proposed rows

| Organization | Top-priority set | Source |
| --- | --- | --- |
| Meta (v2, Apr 2026) | Three catastrophic domains: Chemical & Biological, Cybersecurity, Loss of Control. Emerging: radiological/nuclear, physical autonomy, further LoC pathways. Critical and High now "develop/deploy with mitigations". | meta-2026 |
| Microsoft (Feb 2026) | Five tracked high-risk capabilities: CBRN, offensive cyberoperations, advanced autonomy, loss of control, harmful manipulation. The last two have no thresholds yet. | msft-2026 |
| Amazon (Sep 2026) | Four Critical Risk Domains: CBRN, Offensive Cyber, Harmful Manipulation, Loss of Control. One threshold each. | amzn-2026 |

---

## 8. Version changes relevant to the report (both directions, verbatim where read)

- **Meta v1.1 → v2**, from Meta's own change log (p.44):
  - "Replaced 'uniquely enable' with 'substantially contribute to' as the primary standard". *The bar to reach High/Critical is lowered.*
  - "Critical threshold changed from 'Stop' to 'Develop with Mitigations.' High threshold measure changed from 'Do not release' to 'Deploy with mitigations.'"
  - "Added Loss of Control as a risk domain"; named decision-makers; "whistleblower and non-compliance reporting protocols and retaliation protections"; incident response; preparedness-report criteria; a model spec; and the 10^26 compute criterion.
  - In v1.1, the Critical row read "Stop development" and "do not further develop the model until such a time as adequate mitigations have been identified" (Table 1, §3.3).
- **MSFT v1 → Feb 2026**, from the change log (p.15): "Adding harmful manipulation and loss of control as tracked high-risk capabilities", "Adjusting the update cadence to align with regulatory obligations", "Adjusting the cadence by which we repeat deeper capability assessment to align with emerging industry standards".
  - The v1 scope trigger "any model pre-trained using more than 10^26 FLOPs" became "any model that is in scope for frontier model requirements under applicable laws".
  - The pause sentence is unchanged.
- **Amazon Feb 2025 → Sep 2026:** there is no change log, so this list is from my own comparison.
  - Domains changed (see §0.1).
  - The cyber threshold changed from enabling "a moderately skilled actor … to discover new, high-value vulnerabilities and automate the development and exploitation" to enabling "non-subject matter experts to discover novel end-to-end exploit chains in hardened systems or … autonomously extend control over critical infrastructure systems".
  - The baseline changed (§5).
  - The governance gate changed from "Models may not be publicly released unless safeguards are applied" to "Models may not be released unless evaluations demonstrate that risks are within acceptable levels prior to launch" (p.7).
  - A misalignment-safeguards category, bug bounty, and "We report incidents to relevant authorities as appropriate" (p.4) were added.
  - *I have not coded these for direction. Zhu's method would, and its corpus predates this revision.*
- **Zhu (2026)** \[S; preprint, single adjudicated coder, α not yet reported]. Silent-revision rates: Meta 1.1→2, 0.69 strict; MSFT v1→2026, 0.81 strict, the highest in the corpus. Weakening share, pooled across all pairs: 0.77. Amazon had no revision to code at collection time.

---

## 9. Proposed footnote bodies

[^meta-aasf]: \[P] Meta, *Advanced AI Scaling Framework*, Version 2. Change log dated 7 Apr 2026; announced 8 Apr 2026. Renamed from *Frontier AI Framework*. <https://ai.meta.com/static-resource/Meta_Advanced-AI-Scaling-Framework-v2> (announcement <https://ai.meta.com/blog/scaling-how-we-build-test-advanced-ai/>). relata `meta-2026-advanced-ai-scaling-framework` (SHA-256 prefix d87aa9bf, identical to the Zhu 2026 corpus). Printed pages. Anchors:
    - p.10: "The Chief AI Officer will ensure that the Director of Alignment and Risk has resources, including human, financial, and computational resources, sufficient to perform state-of-the-art risk mitigation and assessment."
    - p.15, Table 1, Critical: "Develop with Mitigations … Proceed with development of the Frontier AI only if catastrophic risks are within acceptable levels"; security "insofar as is technically feasible and commercially practicable".
    - p.17: "we will only continue development of the Frontier AI if our risk assessments are complete and safeguards are defined, implemented and validated to reduce risk to the moderate or lower risk threshold."
    - p.22: loss-of-control fn 4 and the "technical and organizational measures" scoping, quoted in §5.
    - pp.22–23: TS.1.1, "AI development accelerates such that new capabilities and behaviors emerge faster than the organization's evaluation processes."
    - p.40: "when we have reasonable grounds to believe either its adequacy or our adherence to it has been materially undermined, or at least every twelve months, whichever is sooner."
    - p.44, change log: "Critical threshold changed from 'Stop' to 'Develop with Mitigations.' High threshold measure changed from 'Do not release' to 'Deploy with mitigations.'"

[^meta-faf]: \[P] Meta, *Frontier AI Framework*, v1.1, 3 Feb 2025 (copy: the silent same-label re-upload of 28 Mar 2025, SHA-256 8f88ef32, from the Zhu corpus <https://github.com/louisyzhu/frontier-safety-framework-corpus>). relata `meta-2025-frontier-ai-framework`. §3.3: "If a frontier AI is assessed to have reached the critical risk threshold and cannot be mitigated, we will stop development and implement the measures outlined in Table 1." Table 1, Critical: "Stop development"; "Access is strictly limited to a small number of experts".

[^msft-fgf]: \[P] Microsoft, *Frontier Governance Framework*, February 2026. <https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Frontier-Governance-Framework-Feb-2026.pdf>. relata `microsoft-2026-frontier-governance-framework` (SHA-256 3282e4fc = Zhu `feb-2026`). Anchors:
    - p.3: "Loss of control. A model's ability to undermine effective human control through adaptive, deceptive, or self-reinforcing mechanisms such that, when deployed, a model can no longer be reliably directed, modified, or shut down." And: "Harmful manipulation. A model's ability to strategically distort human behavior or beliefs at scale."
    - p.5: "A leading indicator assessment is run on any model that is in scope for frontier model requirements under applicable laws, such as the EU AI Act, California's Transparency in Frontier AI Act (TFAIA), and New York's Responsible AI Safety and Education (RAISE) Act."
    - p.8: "If, during the implementation of this framework, we identify a risk we cannot sufficiently mitigate, we will pause development and deployment until the point at which mitigation practices evolve to meet the risk."
    - p.9: "the marginal benefits of a model outweigh any residual risk"; "Employees who raise concerns are protected from retaliation"; "All material revisions will be made public within 30 days of adoption".
    - p.14: loss of control and harmful manipulation have no thresholds yet ("We are researching approaches …").
    - p.15, change log: "One year update following finalization of the EU Code of Practice for General Purpose AI (CoP), NY RAISE Act and CA Transparency in Frontier Artificial Intelligence Act".

[^msft-fgf-v1]: \[P] Microsoft, *Frontier Governance Framework*, Version 1, Feb 2025 (copy: provider re-upload of 26 Feb 2025, SHA-256 da0d8b15, from the Zhu corpus). relata `microsoft-2025-frontier-governance-framework`. "Every six months, we will have an explicit discussion on how this framework may need to be improved." "any model pre-trained using more than 10^26 FLOPs is subject to leading indicator assessment".

[^amzn-fmsf26]: \[P] Amazon, *Amazon's Frontier Model Safety Framework*, September 2026 update. It is unversioned and has no change log; the PDF CreationDate is 17 Sep 2026. <https://cdn.amazon.science/a0/4f/bca5cb32495280835d9370a466b7/amazon-fmsf-9-2026.pdf> (landing page <https://www.amazon.science/publications/amazons-frontier-model-safety-framework>). relata `amazon-2026-frontier-model-safety-framework` (SHA-256 06236643). Printed page, then margin line. Anchors:
    - p.1, l.20–21: "we have reviewed and updated this Framework to reflect our current practices and account for relevant laws and regulations."
    - p.3, l.87–90: loss-of-control domain, quoted in §5.
    - p.2, l.80–82: harmful-manipulation domain, quoted in §5.
    - p.2, l.58–60: CBRN uplift "beyond other publicly available models in known harnesses".
    - p.5, l.216: "Misalignment Safeguards".
    - p.7, l.296–297: "Models may not be released unless evaluations demonstrate that risks are within acceptable levels prior to launch."
    - p.7, l.308–310: "revisit this Framework at least annually and publish any material modifications".
    - p.8, l.324–325: "Workforce vetting and careful monitoring for insider threats. Employment at Amazon requires background checks (to the extent allowed under local law)."

[^amzn-fmsf25]: \[P] Amazon, *Amazon's Frontier Model Safety Framework*, 9 Feb 2025 (amazon.science page date; PDF 10 Feb). The original URL is now 404; the copy comes from the Zhu corpus, SHA-256 0628d781, matching its manifest. relata `amazon-2025-frontier-model-safety-framework`. The three thresholds were CBRN, Offensive Cyber Operations and Automated AI R&D. Cyber: "material uplift (beyond other publicly available research or tools) that would enable a moderately skilled actor … to discover new, high-value vulnerabilities and automate the development and exploitation of such vulnerabilities." Governance: "Models may not be publicly released unless safeguards are applied."

[^zhu]: \[S; preprint] Zhu, *Silent Revision: Measuring Undisclosed Change in the Safety Frameworks of Frontier AI Developers*, arXiv 2609.08789v1, 8 Sep 2026. relata `zhu-2026-silent`. Corpus <https://github.com/louisyzhu/frontier-safety-framework-corpus>. Table 1: Meta 1.1→2, SRR strict 0.69; Microsoft v1→2026, 0.81. "77% of traced changes weaken or remove a commitment". Limitations (§7): "Inter-coder agreement is not yet reported".

[^vorp]: \[S]\[F] Vorp Labs, "Current Frontier AI Framework Inventory 2026: Versions & Legal Mappings", data updated 12 Jul 2026. <https://vorplabs.com/ai-regulatory-updates/frontier-ai-frameworks>. Meta: "No public statement found as of 2026-07-04, despite Meta plausibly meeting both statutory thresholds." Amazon: the same. It lists Amazon's framework as the Feb 2025 version. Not in relata.

---

## 10. Bibkeys created (all new; none existed)

| Document | relata key |
| --- | --- |
| Meta, Advanced AI Scaling Framework v2 (Apr 2026) | `meta-2026-advanced-ai-scaling-framework` |
| Meta, Frontier AI Framework v1.1 (Feb 2025) | `meta-2025-frontier-ai-framework` |
| Microsoft, Frontier Governance Framework (Feb 2026) | `microsoft-2026-frontier-governance-framework` |
| Microsoft, Frontier Governance Framework v1 (Feb 2025) | `microsoft-2025-frontier-governance-framework` |
| Amazon, Frontier Model Safety Framework (Sep 2026) | `amazon-2026-frontier-model-safety-framework` |
| Amazon, Frontier Model Safety Framework (Feb 2025) | `amazon-2025-frontier-model-safety-framework` |

All six were added with `relata add` (BibTeX on stdin) and `relata pdf`. `ingest` was not used.

---

## 11. Not read, and notes for the integrator

- **Not read:** Meta's *Muse Spark Safety & Preparedness Report* (its first report under v2); Amazon's *Nova 2.0 Lite* evaluation under the FMSF (arXiv 2601.19134); the Frontier Model Forum *Risk Taxonomy and Thresholds* technical report, which MSFT cites (p.10). These are adjacent and would show the frameworks applied rather than stated.
- **Amazon's Sep 2026 update postdates every secondary source in the report** (METR Dec 2025, SaferAI v5 Apr 2026, FLI Jul 2026, Zhu Sep 2026). A claim about "Amazon's framework" in those sources describes the Feb 2025 text.
- **Adjacent: the "internal deployment" row.** Meta and SB 53 §22757.12(a)(10) treat internal use as its own risk surface. The report spreads it across B8b and §5.2. It may deserve its own B-row; the Anthropic and OpenAI slices will likely bear on this too.
