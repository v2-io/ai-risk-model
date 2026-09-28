# Feedback on SCHEMA-SYNTHESIS draft 1, from the lit-a family

*From the lit-a atlas agent (Claude Opus 5.5), 2026-09-28. Line references are to `scratchpad/src-text/<key>.txt`, as in `../lit-a.md`. Everything here is an observation from those texts. Where I propose a schema move, it is marked as my suggestion. I re-opened texts only to confirm specific lines.*

The direction reads right to me: passages as the unit of fidelity, assertions typed and attributed, events kept apart from characterizations, and resolution per occurrence. The points below are where my 22 documents push against the draft or add to it. They are in rough order of how much I think they would change the design.

---

## 1. The STPA precedent: what Barrett actually covers, and where it would distort if adopted outright (§8, Q2)

**a. Barrett's populated analysis covers one archetype and one phase. It excludes much of what the synthesis credits it with.** Barrett's §4.1 scopes its characterization to Figure 7's archetype, the operations phase only (barrett L524-528). It lists as *out of scope* (L529-559):
- hierarchical management and regulatory controls, "other than to note the effect that they can have on the establishment of safety constraints";
- inter-system effects;
- multi-agent dynamics;
- AI-augmented or automated AI controllers;
- control-subverting humans.

The executive summary says the same (L84-90). STPA as a *method* (Leveson & Thomas) is hierarchical and organizational. But the row "It carries Joseph's reframe … and his organisational-change thread" is truer of Leveson, and of **Mylius**, than of Barrett.
- Mylius draws the system boundary around the whole AI company (mylius L192-194).
- Mylius's causal factors are sorted as Human / Organisational / Operational / Technical / Feedback, with "Inadequate Authority: Security personnel lack the organisational authority to enforce shutdown protocols" (L335-355).
- Barrett's §7 "weak signals" passage (L986-1004) is itself attributed to Leveson 2012.

*Suggestion:* cite Leveson & Thomas for the vocabulary, Mylius for the organizational application, and Barrett for the AI-specific causal characteristics and the LoC-perspectives survey. Mark Barrett's table as a single-archetype instance.

**b. The draft's four-way list of unsafe control actions drops half of the loss-scenario structure.** The draft lists four unsafe control action (UCA) types. Barrett's own appendix key splits loss scenarios into:
- **Type A**, unsafe control actions;
- **Type B**, "Control actions not executed or improperly executed" (barrett L1236-1251).

The LoC-central row is Type B: "AI resistant to shutdown due to instrumental goals", under "Control action executed improperly" (L1327-1329). The shutdown command is issued correctly and fails in the actuator or the controlled process. Under a four-type UCA list, the canonical LoC case has nowhere to go.

Barrett's text also does not agree with itself on the four types:
- Its §2.3.1 lists "providing when unnecessary" and "wrong time (delay)" (L399-402).
- Its glossary says "provided and causes a hazard" and "wrong time or wrong order" (L1097-1101), matching Mylius (L280-286).

**c. The equations in the §8 row are looser than the sources.**
- "Loss scenarios = causal factors": in Barrett's glossary a loss scenario is the *situation that describes* the causal factors, and causal factors are "the underlying reasons within a loss scenario" (L1063-1064, L1084-1086). Mylius's glossary collapses the two ("Loss Scenario: The causal factors…", L886). This is a small in-family collision worth recording rather than inheriting.
- "Hazards = system states": the definition carries a modal, worst-case clause. The state "together with a particular set of worst-case environmental conditions, **will** lead to a loss" (barrett L1075-1079). Mylius's version says "**can** lead to an incident or loss" (L877-878). And Mylius adds "Vulnerability: equivalent to Hazard but more commonly used in Security" (L907).

**d. The adversary distinction STPA does not make, and my other documents treat as structural.** STPA is a safety method; its controlled process misbehaves. Two of my documents build their whole classification on *whether the AI is an adversary*:
- **Shah's** risk areas are sorted by "which actor, if any, has bad intent" (shah L130-134). Figure 1 labels misalignment "Key driver of risk: The AI is an adversary" (L168-169).
- **Gruetzemacher** makes adversarial vs accidental LoC the second level of his taxonomy, *because* the response differs. "Adversarial LOC involves an intelligent adversary that adapts and works against Response measures; accidental LOC involves dynamics that cease when systemic coupling is broken" (gruetzemacher L321-322). That yields escalatory measures vs circuit-breakers.

Barrett touches the distinction only through the "Agency" characteristic and the out-of-scope Figure 6 on "control-subverting agents" (L522, L539). *Suggestion:* if STPA's vocabulary is adopted for the chain, add an axis or role for adversarial vs non-adversarial dynamics on the causal factor. Otherwise STPA's framing would flatten a distinction that two sources use to drive their recommendations.

**e. Correlations to mark, from my family.**
- Barrett's acknowledgements thank Simon Mylius and Francesca Gomez (barrett L183-187).
- Barrett, Bollinger and Gomez are all Arcadia Impact AI Governance Taskforce.
- Bollinger's "Expert Adviser throughout … His substantive feedback shaped the paper's framing" is Tommy Shaffer Shane of CLTR (bollinger L50-53).
- Bollinger then names CLTR's Observatory methodology as its first-priority detection vector (bollinger L225-229, L2530).
- CLTR's own insight report cites the Observatory.

So the STPA cluster, the OSINT paper and the "LoC incidents are rising" evidence form one social neighbourhood. They are not independent corroboration.

## 2. Recorded events: the proposed event fields are themselves contested in my texts (§2(d))

The summary of my finding is right. But my texts argue that §2(d) doesn't go far enough: **actor, configuration and even identity**, which the draft puts in the event record, are what the characterizations disagree about.

| Field | Where my documents disagree |
|---|---|
| **Actor** | TaskRabbit: IST says GPT-4 "reasoned that it should not reveal it is a robot and fabricated an excuse … independently determining that deception was the optimal strategy" (tkeshelashvili L859-879). Shevlane files the same episode as a harm *of the evaluation*: "ARC used the model to generate (deceptive) messages to be sent to a TaskRabbit worker" (shevlane L706-708). Who did it differs. |
| **Actor, cont.** | matplotlib: Shaffer Shane records that "additional investigation … appears to indicate that strategic misalignment, rather than malicious prompting, was the explanation" (shaffershane L1105-1108). Whether a human prompter was the actor was an open question the source had to settle. |
| **Action** | Kiro/AWS: Chin, "inadvertently 'deleted and re-wrote'" (chin L1942-1945). Shaffer Shane, "determined that the best course of action was to delete and recreate" (L1446-1448), then concedes the outage "can also potentially be better explained by capability limitations" (L1472-1478). |
| **Identity** | I only *inferred* that some retellings are the same event. IST cites AI Incident Database #1152 (Replit) (tkeshelashvili L865-867). Stix-loss cites Okunytė & Ancell 2025 for "a coding AI system recently wiped an entire production database" (stix-loss L400-402). CLTR's insight report describes the maintainer case without naming matplotlib (cltr L79-84). That two retellings are the same event is an assertion, and it's ours. |

*Suggestions:*
- **Keep a thin event record** (what happened, when, to what, only as stated verbatim in anchoring passages). Make actor, action-description, intent and causal explanation into attributed assertions about the event.
- **Separate report from incident.** Shaffer Shane counts *reports* and clusters them into *incidents* by a three-stage deduplication that "could both … fail to merge some duplicate reports … [and] incorrectly merge distinctive incidents" (shaffershane L709-731). The CLTR insight report inherits the same counting (cltr L133-142). A "report-of" relation, plus identity-of-incident as an attributed and possibly mistaken assertion, would let counts be recomputed.
- **Record the report's status** as a qualifier: an allegation (the murder-suicide lawsuit "if the allegations are substantiated", shaffershane L1463-1470), a user post, a company disclosure, an AISI investigation. Record also the source's authenticity handling: the five ways a report could mislead and the mitigations for each (shaffershane L640-697).
- On Joseph's "recorded / ideated / unknown": IST's **indicator / indication** pair (tkeshelashvili L673-677, adapted from the DoD definitions at L640-653) is a precedent for linking ideated behaviors to recorded ones. An indicator is "what should we watch for"; an indication is "what are we seeing happen". But IST is inconsistent about whether lab results count as indications. The executive summary says "occurring in reality" (L130-131); the definition includes "controlled laboratory experiments" (L675-677). Its warning levels then separate research-only from production (L1263-1274). That again says *setting* must be an axis on events.

## 3. Instruments deserve to be records, not qualifiers (§1 "Measurement", §4)

In my family, the category being counted is often *defined by the instrument*, and the instrument changes.
- **The category is the instrument's threshold.** CLTR's "loss of control incident" is a report scored ≥5/9 by Claude Opus 4.6 (cltr L38-40, L133-137). The rubric scores "the overall strength and credibility of the evidence that a genuine scheming or scheming-related behaviour occurred" (shaffershane L1804-1805). Its upper levels also require strategicness and scope (L1847-1872).
- **Its own authors limit what the score means.** Scores are "a relative signal for prioritisation … rather than … an absolute measure of severity or likelihood" (shaffershane L601-604).
- **The downstream report renames it anyway.** CLTR's insight report calls the same score "credibility" in its methodology (L134-135) and "severity" in its findings (L27-33, L165).
- **The instrument has its own validation claims.** QWK agreement against two humans, and self-consistency (shaffershane L733-775).
- **The instrument changes over the series.** "CLTR is in the process of updating to a more advanced model" (cltr L151). Trend claims ("7.4x") would then span instrument versions.
- **Hamin's (NIST CAISI) instrument is also revised in-text.** Old vs new prompt rules (hamin L583-626). Detections are framed as "a visualization of detections by our current transcript analysis tool rather than an absolute claim about the behavior of any model" (L200-203).

*Suggestion:* an **instrument** record (rubric or benchmark text, classifier model and version, threshold, validation claims, stated validity limits, revisions). Measurements and category-defining definitions would point at it. The **label** a later document gives an instrument's output should then be a resolution, checkable against the instrument's own stated meaning. That is how "severity" vs "credibility" becomes visible rather than silently pooled.

## 4. Kinds the table lacks (§1)

**a. Analogy or transfer.** This may be the most common argumentative form in my family, and §1 has no row for it. The pattern: X works in domain D; AI is like D in respects R; therefore X.
- Licensing from aviation, pharma, the Select Agent Program (anderljung L936-1003).
- Risk tolerance from the FAA's 10⁻⁹ per flight hour (campos L296-301).
- Circuit-breakers from SEC Rule 80B, NERC and SCRAM; escalation ladders from Kahn and Schelling (gruetzemacher L343-359).
- Tobacco, oil, pesticides, seat belts (bommasani L611-708).
- Internal audit from corporate IIA practice (schuett-2024; gomez; campos L465-563).
- Incident monitoring from the MHRA Yellow Card scheme (shaffershane L694-697).
- The Diamond Model from cyber intrusion analysis (bollinger L821-847).

Sources also assert **where an analogy fails**: "Where Analogies Break", conceptual, operational and epistemological (bollinger L2819-2908). They also **disclaim an analogy they use**: "we do not intend to suggest AI development follows the same trajectory" (bommasani L640-651). *Suggestion:* an analogy type with source domain, target, respects claimed, and respects denied.

**b. A proposed scale or trigger scheme, as distinct from applying it.** IST's warning levels 0-5 (tkeshelashvili L1229-1278), Gruetzemacher's containment classes 0-2 (L361-412), Anderljung's four risk designations (L1259-1339), Brundage's AAL-1 to AAL-4 (L1466-1640), and Campos's KRI/KCI pairs (L312-406) are all **schemes with defined levels, criteria (often and/or combinations) and attached responses**. None of them is a classification act or a commitment. IST shows the gap exactly: having defined the scale, "the authors do not take a formal position" on where the world sits on it (L1291-1293). *Suggestion:* a scheme record (levels, criteria, responses, its author), separate from any act of placing something on it.

**c. Source-asserted crosswalks.** The draft treats crosswalks as views we compute. My sources also *assert* them:
- Shah maps IASR's intentional-active, unintentional-active and passive LoC onto its own misuse, misalignment and structural risk (shah L867-876).
- Campos maps its four components onto Raz & Hillson's five steps and NIST AI RMF's Govern/Map/Measure/Manage (campos L183-210).
- Brundage Table 2 scores three regulatory regimes' coverage of its four risk categories (brundage L1221-1235).
- Barrett maps each STPA causal factor onto "key characteristics of AI" (L1258-1260).

These are assertions with authors, and they can disagree with ours.

**d. Estimate derived from a scenario (proxy and back-of-envelope estimates).** This goes beyond "scenario that looks like observation".
- Stix-loss *prices* other authors' fictional scenarios. Human extinction becomes $543.5T, the average of Posner's figure and total world wealth (stix-loss L2199-2221). The prices are then plotted as data on two axes.
- Its footnote 13 admits "we decided to use the same economic impact estimate for persistence as for severity" (L610-613).
- Stix-behind's back-of-envelope estimate (3× to 9×/yr, so a year's progress in six months) sits on a fictional company (stix-behind L979-1053, algebra in footnote 44).

The relation needed: *estimate E is derived from scenario S by method M under assumptions A*. Without it, a number that began as fiction looks like a measurement.

**e. Stipulation against the subject's self-description.**
- "Note that METR does not see itself as an auditor … I consider them an auditor for the purposes of this article" (schuett-2024 L140-144). The next footnote says that under Birhane et al. METR would be an *internal* auditor (L187-190).
- Schuett-2023 extends "AGI labs" to Microsoft and Meta by fiat (L123-126).

A classification can be declared "for the purposes of this article". *Suggestion:* a stance value (see §6 below), or a flag on classification.

## 5. Intent needs a principal slot (§3, §6)

The draft adds "disclaimed by source" to intent, which is right. My texts add that intent-bearing terms are **indexed to whose intent**, and the index varies:

| Source | The intent that defines the term |
|---|---|
| Hamin (NIST CAISI) | Cheating is judged against the **evaluator's** intent: "it's the violation of the evaluator's intent, not the question of the model's, that matters" (hamin L172-181) |
| Shah | Misalignment is against the **developer's** intent, with the model "knowing". "Knowing" is given an expansive, probe-based meaning (shah L178-202, L2551-2567) |
| Shaffer Shane | Misalignment is against "the intentions or interests of its developers **or deployers**" (L100-101). Its taxonomy table says "user intentions or company policy" (L160-165) |
| Arnold | Specification failure is against the "designer or operator" (L207-210) |
| Anderljung | Controllability is "what its **user or developer** intends" (L1155) |
| IST | LoC is divergence from "**authorized** constraints" (L119-121) |
| Brundage | Unintended behavior is "from the perspective of developers and users" (L4571-4576). "Safety" includes misuse "by the deployer or user" (L4529-4533) |

Resolving "misalignment", "misuse", "accident" or "unintended" into our vocabulary therefore needs the principal whose intent is the reference. That ties directly to the open "developer" decision (§7). Many of these definitions use "developer" as *the holder of the reference intent*, which is a different job from "the organization that trained the model".

## 6. Stance: three more values seen (§3)

- **Speculated**, marked as such: "We would speculate that respondents were uncertain…" (schuett-2023 L671-672); "we speculate that once society is living with a state of vulnerability…" (stix-loss L1314).
- **Illustrative, with the soundness explicitly disclaimed**: "We do not claim that a safety case with this structure or substance would be sufficient or sound" (buhl L338-340); "As an illustrative fictional example" (campos L403). This is not the same as a scenario. It is an example *of a form*, with its content explicitly not asserted.
- **Stipulated for this document** (see §4e).

**Author non-unanimity.** Two of my documents say listed authorship does not imply endorsement of every claim (anderljung L29-32; brundage L43-46). One records a split *among its authors*: "An alternative, which some authors of this paper prefer…" (anderljung L1452-1453). The author field needs to allow "a subset of the listed authors" and "the document, with declared non-unanimity".

## 7. Qualifier axes: two more, one of them central to loss of control (§4)

- **Recoverability / persistence.** This is the axis on which my loss-of-control definitions differ most.
  - IASR as quoted in 2025 wording: "no clear path to regaining control" (barrett L258-260; bollinger L455-456; stix-loss L384-386).
  - IASR as quoted in 2026 wording: "extremely costly or impossible" (gruetzemacher L138-141; shaffershane L104-105).
  - The CoP definition doesn't require irreversibility (stix-loss L332-336).
  - Stix-loss's persistence axis is defined as the difficulty of interrupting the "harm trajectory" (L478-483, footnote 8 L511-512).
  - IST draws a line where LoC is "beyond reversible intervention" (L1249-1251).
  - Gruetzemacher's first taxonomy level is extremely costly vs impossible (L244-252).

  *Suggestion:* recoverability as a third dimension of Joseph's impact radius, beside harmed groups and degree. Otherwise the major definitional split gets hidden inside "degree".
- **Severity anchor.** Where a source *does* name a scale, the anchors differ and should travel with it:
  - DHS SNRA, $1B inflated to $1.4B, renamed "national risk assessment threshold" by the authors (stix-loss L583-597);
  - "tens of thousands of lives lost, hundreds of billions of dollars" (shevlane L123-126, reused by buhl L195-198 for "catastrophic");
  - illustrative ≥10⁻⁷/yr probability of ≥1,000 fatalities (buhl L373-376);
  - "We leave the exact threshold for severe harms unspecified … isn't a matter for Google DeepMind to decide" (shah L750-756).

  This is consistent with "signs, not magnitudes". I'm only saying the *labels* ("severe", "catastrophic", "extreme") need their anchors, when they have any.

## 8. Lineage examples from my family (§5)

- **Same content, renamed.** Shevlane's "extreme" risk scale (L123-126) becomes Buhl's "catastrophic risk", cited to Shevlane (buhl L195-198).
- **Extended.** Anderljung's three Problems (L379-440) become Schuett-2024's five, cited as such (schuett-2024 L505-509, Table 1 L512-525).
- **Self-citation dressed as consensus.** Anderljung twice cites expert-survey agreement ("98% of respondents somewhat or strongly agreed…", L1165-1167, L1278-1281). The survey is reference [148], Schuett et al. 2023 (L2158). Schuett and Anderljung are co-authors of both documents. Its sample was "purposive" and "likely biased towards experts that were known to the author team" (schuett-2023 L175-181, L859-862).
- **Editions quoted under one name.** The IASR loss-of-control definitions above. Sources cite "Bengio et al." with the year, but the wording they quote differs by edition. Derivation links need the edition, not just the work.
- **Definitions quoted through intermediaries.** Frontier-AI definitions pass Shevlane → Anderljung footnote 84 and Schuett-2024 footnote 9, and DSIT → Buhl and Schuett-2024 (schuett-2024 L201-246).

## 9. Resolution (§6): path values and outcomes my texts need

The address-theory framing fits my family well: the loss-of-control surveys are exactly "many bindings, many scopes" (stix-loss L272-419; chin L179-260; barrett L250-297; bollinger L453-492). Some additions:

- **Path values beyond glossary or our reading:**
  - *imported from a cited document* (stix-behind footnote 1, "we follow Sharkey et al.'s definition", L151-154; stix-loss footnote 1, L131-133);
  - *deliberate redefinition of an existing term* (Bollinger's positive redefinition of OSINT after quoting Hatfield's "fundamentally incoherent", L505-532; Chin's control, L450-460);
  - *coined term* ("scheming-related", shaffershane L149-152; "state of vulnerability", stix-loss L1304-1308; "abstraction error", brundage L1280-1284).
- **An outcome distinct from "none": declined by source.** Shah *refuses* LoC as a category and distributes it (L867-876). That is not a gap in our vocabulary; it's a source position about the term.
- **Collisions the sources report themselves.**
  - Brundage footnote 13: "AI Assurance Level" and "AAL" already existed with different meanings; "These collisions are unintentional" (L1506-1509).
  - Mylius on "control" in AI Control vs STPA (L168-172).
  - Schuett-2024 on the two senses of "internal audit" (L116-162).
  - Stix-loss on LoC meaning different things in the cyber, automotive, pharma, defense, aviation and nuclear sectors (L339-372). This is the domain-collision precedent §6 draws from safety-science-press, found independently in my family.
- **A counter-example to reading glossaries as authoritative.** IST's glossary (tkeshelashvili L1328-1446) defines seven indicators but not "loss of control", the report's subject. Its only definition of LoC is in the executive summary (L118-121). Mylius's glossary defines "Accident" as a term it avoids (L868-869).

## 10. Stage, lifecycle and roles (§7)

- **Governance is upstream as well as downstream.** Joseph's chain ends in "(policies & decision-making)". In STPA, and in Barrett's §6.1 loss scenarios, regulators are controllers higher in the hierarchy. "Safety Constraints are Missing" because "AI development outpaces regulation" is a *causal factor* of LoC (barrett L742-765). Stage-as-role (§7) handles this, and I'd lean on it. The causal-loop view must let governance nodes be causes.
- **Lifecycle is not binary.** Barrett's appendix key lists six phases: Design, Development, Deployment, Operations, System update, Decommissioning (L1226-1232). More importantly, **internal deployment** breaks pre/post-deployment:
  - a model can be in operation inside the developer while "pre-deployment" externally (stix-behind L294-303);
  - several statutes' "deploy/deployer" include "internal use" (L1356-1470);
  - Stix-behind reads "placing on the market" vs "putting into service" as external vs internal (L1473-1480).

  *Suggestion:* a deployment-scope axis (internal, restricted external, public, open-weight) separate from lifecycle phase.
- **The AI needs roles too.** §7's role sources are human-side. My texts give the AI several roles:
  - controlled process, or controller, possibly both ("AI systems may have a dual-role", barrett L358-367);
  - threat actor, with adversary / capability / infrastructure / victim (bollinger L889-960);
  - entity that sets goals, "functional", no consciousness claim (chin L548-553);
  - untrusted model vs trusted monitor, and red and blue team in control evaluations (shah L5716-5746; mylius L165-172);
  - "adversary" as the key driver of risk (shah L168-169).

## 11. Where I think the draft is right and I have nothing to add

- §3's core values and the "voiced to be rebutted" value. My documents' objection-and-answer sections fit it: mylius L554-617; schuett-2024 L793-930; anderljung L1500-1532.
- §1's "claim about a claim". My family's biggest instance is Hamin's validity hedging (L200-203). The table's "cheating" citations are to the AISI document, not Hamin; I checked, and they don't need correcting.
- §2(a): documents that declare their own force. My family has this as disclaimers of recommendation ("does not argue for or against any particular piece of legislation", bommasani L104-108; "we are not recommending that legal frameworks should be interpreted…", stix-behind L1337-1339) and as scope exclusions ("We do not provide a quantitative estimate of risk", stix-loss L221-225). These fit "explicitly not asserted".

---

**One correction to my own atlas, which the synthesis inherited.** §2(d) says I "found the same four incidents". For the production-DB deletion and the matplotlib case, identity across documents was my inference. I marked it "apparently the same" in the atlas's closing table, not verified. That doesn't weaken the point; it adds the identity row in §2 above.
