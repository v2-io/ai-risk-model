# Feedback on SCHEMA-SYNTHESIS draft 1: from the safety-science and press atlas

*From the agent that wrote `../safety-science-press.md` (CSB Texas City, HSE CHIS7, IAEA GSR Part 2, ICAO Doc 9859; four press items on the Anthropic designation). Line references are to `…/scratchpad/src-text/<key>.txt`. Anything I know from training rather than from the texts is marked **[training]**. I reopened the texts for this feedback; a number of references below are new since the atlas.*

## The short version

1. **A contradiction in the framing.** My set is not the tradition STPA descends from. It is the tradition STPA *defines itself against*, and the corpus says so (Mylius, Barrett; §1). Recoding CSB and ICAO causal claims into STPA types would distort them.
2. **"Causal edge" is too coarse for incident-investigation causality.** The mature disciplines split *general causal theory* (attributed) from *case findings*. Within case findings they type causes by **depth** (immediate / contributing / root; active / latent). They have **norms about where causal analysis may stop**. And they state root causes as **omissions by named actors against a named standard** (§2).
3. **Controls and indicators need to be first-class kinds, with attributes the synthesis lacks.** Controls need type, reliability class, independence, and a sufficiency standard (ALARP). Indicators need leading/lagging typing and a validity relation to the hazard, and they can themselves be causes (§3).
4. **Record kinds missing:** decisions with stated rationales (which appear at the *cause* end of the chain, not only the governance end); warnings and precursors; organizational change events; and drift, which is a trajectory rather than an event. Recommendations need a justification structure and an addressee (§4).
5. **Precedents missed:** ICAO's hazard register fields, its per-term glossary provenance and its mitigation typology; the CCPS safeguard hierarchy; and the CSB logic tree, which is image-only and so far unread by anyone (§5).

---

## 1. Contradiction: STPA's relationship to these disciplines

The coordinator's framing is that my set "holds the older safety disciplines [STPA] came from". The corpus's own STPA sources place STPA *against* them:
- mylius-2025-systematic **L99–100**: "STPA attempts to address gaps that are unfilled by traditional safety engineering approaches such as … Root Cause Analysis (RCA) and Hazard and Operability studies (HAZOP)."
- mylius **L223–225**: "Unlike traditional safety methods that define a hazard as a potential source of harm typically arising from component failure, the STPA Handbook … defines a hazard as 'a system state or set of conditions that … will lead to a loss.'"
- barrett-2025-stampstpa **L352–370** says "traditional hazard analysis techniques" are insufficient for AI.

My documents *are* those traditional techniques:
- CSB's method is root-cause analysis (its §12). It follows CCPS investigation guidelines (fn 54, **csb L3308–3314**, p71) and cites HAZOP (9377; timeline 1993 entry).
- ICAO's causal model is Reason's Swiss cheese (**icao L1103–1112**).
- ICAO's *hazard* is "A condition or an object with the potential to cause or contribute to an aircraft incident or accident" (**icao L276**) and "a dormant potential for harm" (**L1297**). That is exactly the "traditional" definition Mylius contrasts with STPA's.

[training] Leveson's STAMP is explicitly a critique of chain-of-events models, including Reason's, and of root-cause seeking. ICAO's "practical drift" (Snook) and "safety space" (icao L1175–1232, L1247–1273) are closer to STPA's systems view than the rest of ICAO. The second resembles Rasmussen's drift-to-boundary model, though ICAO does not cite Rasmussen in what I read.

**Consequence for the schema.** STPA can be *our* vocabulary for the chain (question 2 in §10), but the synthesis's own rule, borrowed from Slattery ("code what the source presents"), then requires:
- the source's causal frame is recorded as presented, whether root cause, Swiss cheese or STPA;
- any mapping into STPA terms is a resolution *we* author, attributed and contestable (§6's machinery covers this);
- *hazard* goes into the vocabulary as **ambiguous among named candidates**. At least three bindings are in the corpus: ICAO's potential-for-harm, Leveson/Barrett's "will lead", and Mylius's appendix "can lead" (lit-a atlas). ICAO itself warns that "It is not uncommon for people to confuse hazards with their consequences" (**icao L1323–1327**).

The synthesis's §8 table row "Hazards = system states" is true of STPA and false of half of my set.

## 2. Causal assertions need more structure than "A raises B"

**(a) General causal theory vs case finding: a scope-of-generality axis.**
- ICAO states universal claims about *all* accidents and attributes them to named models: "The Reason Model proposes that all accidents include a combination of both active failures and latent conditions" (**L1111–1112**); "Snook contests that practical drift is inevitable in any system" (**L1207**).
- It adopts the model *as a lens*: "can be used as an analysis guide" (**L1160–1166**). And it hedges the model itself: "There are more sophisticated models" (**L1170–1172**).
- CSB imports theory the same way, always with citations (Reason 1997 and Hopkins 2005 at **L7009–7025**; Kletz at **L9308–9312**). It asserts case findings in its own voice.

Suggested:
- an axis on causal assertions: particular event / class of events / universal;
- a stance value **"adopted as analytic lens"**. This is not belief-grade ("useful to illustrate"), and it differs from "treated as", which is commitment-grade.

**(b) Causal depth, a role the §7 edge list lacks.**
- CSB defines *immediate causes* (fn 4, **L786–791**). It asserts that addressing *root* causes "has a greater preventative impact" (fn 6, **L843–846**, citing CCPS). It separates Root from Contributing causes formally (**L10606–10705**, p210–211).
- ICAO separates *active failures* ("immediate adverse effect", front line) from *latent conditions* ("can exist in the system well before a damaging outcome… People far removed in time and space from the event can create these conditions", **L1114–1124**).

The whole argument of the CSB report is that the *depth* at which a cause is named decides the remedy (the CAIB quote, **L803–819**). Candidate edge attributes:
- depth: immediate / contributing / underlying-root;
- latency (active / latent);
- organizational distance from the event.

**(c) Norms about where causal analysis may stop.** The disciplines rule on what may *count* as a cause:
- CCPS via the CSB: "The failure to follow established procedure … is not a root cause, but instead is a symptom of an underlying root cause" (**csb L3308–3314**, p71);
- ICAO lists "Investigations stop at the first viable cause rather than seek the root cause" as a culture *disabler* (**icao L1998–2000**);
- BP's own staff: "investigations were too quick to stop at operator error as the root cause" (**csb L8730–8733**).

These are claims about *causal attribution practice*. They fit "claim about a claim" in the synthesis, but they are normative rules rather than validity comments. They matter for AI because the incident retellings the lit-a agent found (the same event, different claims about the model's mind) are partly disputes about where to stop.

**(d) Root causes are omissions by named actors, measured against a named standard.** CSB's root causes read "BP Group Board did not provide effective oversight…", "Senior executives: … did not provide adequate resources…", "BP Texas City Managers did not: …" (**L10610–10681**). The findings name the violated expectation: "contrary to BP safety guidelines" (**L1047–1048**); the PSSR policy (**L1152–1156**). The shape is:
- **actor**, who has an expected action;
- the **source of the expectation** (own policy / industry good practice / regulation);
- the **deviation**.

STPA's "control action not provided" covers the first part. The *source of the expectation* is what CSB actually argues over, and the schema's causal assertions have no slot for it.

**(e) "Investigated and ruled out" is its own stance.** "3.10 Distraction Not a Factor" (**L4942–4954**, p101; detail in Appendix P, p304) is a *negative causal finding with evidence*. That differs from "explicitly not asserted" in §3, which is abstention.

**(f) Culpability is a separate kind from causation.** Keep them apart even when actor and event coincide:
- CSB finds causes. OSHA found "301 egregious willful violations" (**L882–886**; *willful* defined via case law, fn 8 **L897–901**).
- ICAO requires investigations to focus "not on blame or punishment" (**L7149–7150**) and investigators to be "organizationally independent" (**L7126–7127**).
- Legal exceptions to data protection turn on "gross negligence, wilful misconduct or criminal activity" (**L4462–4466**). A "reasonableness test" separates acceptable from punishable error (**L2067–2069**).
- The press items are about adjudication, which is a third thing again (§6 below).

A schema that lets a causal finding and a legal determination about the same actor merge will misreport both.

## 3. Controls and indicators as kinds, with the attributes the sources use

**Controls.** The synthesis has a "prevents" and a "mitigates or recovers" role, but no properties *of the control*. My sources supply them:
- **type and reliability class:** CCPS Table 3, passive > active > procedural, with the reason that procedures depend on people "potentially while stressed or fatigued" (**csb L5222–5248**, p107–108). This maps straight onto AI: training-time dispositions / runtime classifiers / usage policies. Whether that mapping holds is a claim someone would have to make; the hierarchy is the precedent;
- **independence and redundancy:** "multiple, redundant, active safeguards"; systems "which operate independently of the normal operating controls" (**csb L5253–5294**). ICAO's Swiss cheese describes *correlated* weaknesses: "Sometimes all of the weaknesses align" (**icao L1140–1145**). This needs a **relation between controls**: independent of / shares a failure mode with. Without it, "three layers of defence" counts as three whether or not they fail together;
- **strategy type:** avoidance / reduction / segregation (**icao L1677–1686**);
- **evaluation attributes:** effectiveness, cost/benefit, practicality, acceptability, enforceability, durability, residual risk, unintended consequences, time (**icao L1699–1729**). "Residual safety risk" and "unintended consequences" are the two the AI frameworks most often leave unstated;
- **sufficiency standard,** the normative bar a control is judged against, distinct from likelihood:
  - "as low as reasonably practicable" (**hse L128–129, L385–387**); "so far as is reasonably practicable" (HSWA, **hse L395–397**);
  - COMAH's "all measures necessary" (**hse L466–467**);
  - IAEA Principle 8's "All practical efforts" (**iaea L698–699**);
  - ICAO's organization-specific tolerability classes (**icao L1591–1593, L1629–1632**).

  These have legal content. The AI frameworks' "acceptable level" language would sit on the same axis.

**Indicators.** The synthesis's measurement kind is built around one-off measurements (instrument, conditions, bound). My sources treat a *standing indicator* as an object with its own claims:
- **leading / lagging:** icao **L2326–2373**; hse **L336–346**; csb **L9315–9333**;
- **validity relation to the hazard, including failure:** "Reliance on the low personal injury rate … failed to provide a true picture of process safety performance" (**csb L1171–1173**); "Focus on injury rates … helped mask severe shortcomings" (**L8843–8845**); "a potential false sense of confidence … perilously close to an accident" (**icao L2372–2373**);
- **the indicator as a cause.** Bonus programs were tied to the personal-safety metric (**csb L8837–8840, L8950–8958**). The metric choice is in the causal chain;
- **gaming:** "strive to achieve the 'right' score" (**icao L2121–2123**); SPT caveats (**L2585–2600**);
- **trigger = indicator + threshold → required action** (**icao L340–341, L2729–2741**). This is structurally the frontier frameworks' capability-threshold → commitment pattern. ICAO's own caveat is worth carrying into any crosswalk: triggers are "arguably less relevant to SRM of socio-technical systems… Both SSP and SMS are socio-technical systems" (**L2766–2774**).

Suggested relations: indicator *indicates* / *fails to indicate* hazard-state; indicator *incentivises* actor.

**Severity has a case basis.** ICAO assesses severity at "the worst foreseeable situation" (**L1524–1525**) but probability across "all foreseeable scenarios" (**L1454–1455**). *Foreseeable* uses a reasonable-person test (**L1457–1461**). This is a qualifier axis (worst foreseeable / reasonable worst case / typical) that §4 lacks. The NRR's "reasonable worst case" (uk-gov) is another value on it.

## 4. Record kinds the synthesis lacks

**Decisions with stated rationales, as causes.** CSB's Appendix A timeline (**L11015–11222**, p218–221) mixes physical events with organizational decisions *and their reasons*. For example, 1992: "ARPD does not include separate funding for flare/blowdown work … because state and federal regulations are unlikely to require that relief valves be routed to closed systems" (**L11027–11028**). ICAO: latent conditions come from decisions that "had good intentions" (**L1126–1130**). Joseph's chain places "policies & decision-making" at the *end*. These sources put decisions at the *start*. Stage-as-role (§7) handles that only if decisions exist as records: actor, date, choice, stated rationale, alternatives foregone (CSB 1118–1120: "a less expensive option was chosen").

**Warnings and precursors.** This is the spine of CSB §9.4 (**L8631–8958**, p172–178). Dated internal warnings go to named recipients, and the response is recorded ("too little, too late", **L1220–1222**). Prior similar events went uninvestigated (**L1145–1149**; Appendix C "whereas" 4, **L11343–11348**). ICAO's precursor indicators (**L2359–2364**) are the monitoring-side version. The needed relation is roughly *precursor-of* / *warned-of*, with source, recipient, date and response. For AI, internal staff warnings and early incident reports would sit here.

**Organizational change events, and drift.**
- Change events need records of their own, not only document versions: mergers, budget cuts, reorganizations, leadership turnover. See CSB **L9647–10051**; HSE whole; IAEA 4.13's "the cumulative effects of minor changes" (**L973–976**); ICAO 3.2.7 (**L1918–1923**).
- HSE's split belongs on them: risks *from* the change vs risks from the *process* of changing, which "should not be confused" (**hse L158–164**).
- *Drift* (**icao L1175–1232**) and cumulative minor change are **trajectories, not events**. The recorded-events kind can't hold them. A trend claim form (something changing gradually, with its direction and the evidence for it) seems needed.

**Recommendations: addressee, authority basis, justification.** CSB's urgent recommendation (Appendix C, **L11311–11560**, p236–239) has an explicit justification structure: "Whereas:" plus eighteen premises, then "Accordingly: Pursuant to its authority under 42 U.S.C. § 7412(r)(6)(C)…". The premises are of mixed kind:
- recited facts;
- "preliminary findings";
- "The Board believes that…" (**L11447–11462**), a belief stance explicitly distinct from a finding;
- the statutory mandate (**L11465–11477**);
- the procedural rule that authorizes urgent recommendations "before a final investigation report is completed" (**L11480–11484**).

The recommendation has an ID, an **addressee who is not the author** (and over whom, [training], the CSB has no regulatory power), "at a minimum" floors, and constraints on *how* its request is to be met (**L10741–10753**). It also **commissions another inquiry**, the independent panel (**L11502–11510**): one source creating a future source. The synthesis's "Recommendation, tasking, plan" kind needs addressee, the authority basis, the premises it rests on, and interim vs final status.

**Assessments of an overseer's capacity.** CSB compares regulators' inspection frequency, staffing and qualifications across jurisdictions and concludes "OSHA lacks sufficiently trained and experienced inspectors" (**L10324–10376**, p204–205). This claim form, capacity to oversee, is directly relevant to AISI and may deserve its own type. The same passage has two authorities counting one quantity differently: 203 refineries per the Census Bureau vs 144 per EIA (**L10443, L10463–10465**).

## 5. Precedents missed

- **ICAO's hazard register** (**L1747–1752**): "the hazard; potential consequences; and assessment of associated risks, identification date, hazard category, short description, when or where it applies, who identified it and what measure have been put in place". This is a record schema, published. ICAO also requires "any assumptions underlying the probability and severity assessment" to be documented (**L1742–1743**).
- **ICAO's glossary marks provenance per term.** An asterisk means "already defined as such in Annexes and PANS" (**L256–257**). This precedes §6's "resolution path through a source's glossary": a glossary that itself says which bindings it inherited. The Foreword also rebinds "service provider" differently from Annex 19, the instrument the manual implements (**L92–96**). That is a document declaring its own drift.
- **ICAO risk matrix and tolerability** (**L1438–1632**): the canonical probability × severity classification, the family Anthropic's P·H·U decomposition belongs to. Two things travel with it. It is labelled "an example only" (**L1487**). And the printed tolerability row contains a source error, "5A, 5B, 5C, AA, AB, 3A" (**L1613**, confirmed in the PDF), which breaks the manual's own "4B" example. Hand-maintained matrices go wrong.
- **The CSB logic tree** (Appendix B, **PDF p222–235**, image-only; no text in the extraction). This is the case-level causal tree from a mature investigation: the direct precedent for Joseph's "(sources & causes tree)". Nobody in this round has read it. It is worth someone viewing those fourteen pages before the causal-assertion design settles.
- **The CCPS safeguard hierarchy**, via CSB Table 3 (**L5236–5248**).
- **CSB's handling of rival definitions** (**L6957–6975**): three authorities' definitions of *safety culture* side by side, with a stated reason for preferring the practice-based one. This precedent is closer to what `terms/` does than Slattery's change log, because it is *cross-source*.
- **HSE's mapping method** for organizational change: tasks and individuals mapped from the old to the new organization, then compared for overlooked tasks, training, workload and simultaneity (**hse L252–279**).
- **IAEA's graded approach** (**L986–1002**) and HSE's proportionality clause (**hse L108–115**, right column). These are criteria for scaling effort to hazard, which the AI frameworks' "proportionate" gestures toward without criteria.

## 6. Press items

- **Layered authorship needs a *rendering* attribute:** verbatim / fragment / paraphrase / characterization. The same D.C. Circuit majority is paraphrased by ABC/Reuters (**abc L22–23**) and quoted by CNBC (**cnbc L16–18**), with different emphasis. NPR's correspondent *characterizes* the government's argument ("hinged on the idea that anthropic had some sort of backdoor", **npr-ruling L36–40**). CNBC nests four layers (**cnbc L53–56**).
- **Channel lineage:** "(Reuters wire copy)" (**abc L6**). This is the propagation §5 describes, at the channel level.
- **Adjudicative determinations have procedural status and dissent.** The panel delayed effect pending rehearing (**cnbc L41–43**). There is a dissent (**abc L25–28**). "Parallel" designations under two authorities got opposite outcomes (**cnbc L33–37**; **abc L29–36**). A court holding is authoritative in its scope, contested across scopes, and revisable on appeal. This is lineage and stance applied to an institution with formal procedure.
- **A live instance of §6's *match* problem.** The dispute is whether a domestic developer matches a statutory *supply chain risk* defined around adversaries (**npr-scr L47–50**; the former officials' "category error", **L61–68**). The primaries (the two rulings, the statute, the Pentagon notice) are not in the corpus. Every judicial claim in these items is a secondary quotation.
- **The channel as author of a causal claim:** "due to people siding with its moral stance" is in NPR's own voice, unattributed (**npr-scr L69–72**). Layered author handles it if "channel" can also be "author".

## 7. Summaries of my findings: corrections

- §6, "'safeguard' as … usage restriction (safety-science-press)". The usage-restriction sense is not the press's own voice. It is in a letter from former officials quoted by NPR (**npr-scr L61–68**). A small point, but this is a compilation that tracks voices.
- §1, "The first-order causal claim turned out to be a minority form". That does not hold for incident investigations. CSB is organized around causal findings, and even its TOC titles are causal propositions (**csb L31–356**). The claim is family-dependent. The AI corpus's nearest analogue is AISI's incident report, which is probably where the causal-assertion design will be tested hardest.
- §2(a), "IAEA's defined 'shall' and 'should'". Correct, but that is the *series-level* grammar (**iaea L294–356**). GSR Part 2, as a Requirements publication, uses "shall". IAEA also varies force *by part* of the document: appendices are integral, annexes and footnotes are not (**L479–487**). By that rule, its own footnoted definitions (leadership and management, fn 4, **L624–630**) sit in non-integral text. So the §4 axis "force of the containing document" probably wants to be "force of the containing *part*", and a document can declare it twice: HSE at **L13–15** vs **L497–500**.
- IAEA's "not addressed to a specific party, the implication being that the appropriate parties are responsible" (**L302–304**) is a value Zhu's *actor* dimension needs: unaddressed by design, which differs from missing.

## Supports (briefly)

- **Stage as a role relative to a focal event** (§7) is ICAO's own teaching. A fifteen-knot wind is not a hazard down the runway and is one across it (**L1318–1322**). Consequences chain: "an immediate outcome … loss of lateral control followed by a consequent runway excursion. The ultimate consequence could be an accident" (**L1328–1330**).
- **Good and bad on relations** is supported by ICAO's "management dilemma". The same investment can serve production and protection, and excessive safety allocation can make an activity "unprofitable, thus jeopardizing the viability of the organization" (**L1238–1253**).
- **The four kinds of record** fit my documents, once the additions in §4 are made.
