# Schema synthesis: a holistic model for the source claims

*Draft 2, 2026-09-28. Coordinator 3 (Claude Opus 5.5), for Joseph. **A proposal, not ratified**; nothing in `model/` has changed on its strength. Draft 1 is in git (`7226942`). This draft is rebuilt around the ten atlas agents' feedback (`../source-atlas/feedback/*.md`, cited below as `fb:<family> §n`). Each feedback file carries the line references behind its points.*

## 0. What this is for, and what changed from draft 1

**Joseph's aim** is a schema that works as a high-fidelity, consolidated landing space for everything the sources claim, so the risk landscape can be looked at and projected from many angles. The causal loop diagram is one analysis-phase view among several. His chain is the spine of the risk side:

```
(sources & causes tree) → (preventions & controls) →
  (risk-events [recorded, ideated, unknown] × impact-radius [harmed groups, degree/scale tree]) →
    (mitigations & recovery) → (policies & decision-making)
```

Draft 1 proposed four kinds of record, with causal edges as one assertion type. The feedback accepted that direction from all ten families. What it showed, repeatedly and independently, is that draft 1 still put too much into single slots:
- "commitment" held what is really a family of norms;
- "author" held several distinct roles;
- "qualifier" held values the sources declare once, for a whole scope, not per sentence;
- the event record held fields the sources dispute;
- "stance" held three separate questions;
- STPA was credited with more than Barrett's paper covers.

The decisions already made with Joseph still stand:
- compilation, not adjudication;
- soft evidence in, marked;
- good and bad on relations;
- signs, not magnitudes, for *our* quantities (source magnitudes are carried verbatim);
- provenance by author, channel, evidence and qualifier (now expanded, §3);
- governance as commitments (now generalised to norms, §6.4);
- vocabulary before quantities.

## 1. The shape: two planes and the resolution between them

```
 EVIDENCE PLANE (what was said)                       MODEL PLANE (what it is said about)
 ───────────────────────────────                      ────────────────────────────────────
 documents ─ parts ─ passages                         vocabulary: scopes, bindings, terms, schemes
     │                                                entities: actors, roles, systems, quantities,
 assertions (speech acts)  ──── resolution ──────▶              events, decisions, norms, controls,
     • who, in what capacity                                    indicators, instruments, scenarios,
     • stance (3 questions)                                     impact targets
     • kind + content                                 relations: the causal chain (edge roles
     • qualifiers (scoped, inherited)                           relative to a focal event), plus
     • relations to other assertions                            structural relations
       (lineage · argument · contest)
                                     ▼
                         VIEWS (computed, never hand-maintained)
     causal loop diagram · bow-tie per focal event · crosswalks (ours and the sources') ·
     lineage-aware corroboration · coverage by declared scope · regenerated report · conflict flags
```

**Evidence plane.** Every document is broken down into passages. Every claim, definition, norm or classification is an assertion anchored to its passages, with its authorship, stance, kind, qualifiers and relations recorded. Nothing here is our reading.

**Model plane.** This is our vocabulary, plus the things the assertions are about. It is where the risk landscape lives. It holds no bare facts: everything in it is reachable from the assertions that support it.

**Resolution.** This connects the two planes. For each key term in an assertion, a resolution records what it refers to in our vocabulary, how that was determined, and who determined it. Sometimes the source does its own resolving (IASR's note that the EU uses "systemic risk" differently; Anthropic filing RSP thresholds under the statutory "loss of control"). A resolution is always an attributed assertion.

**Why two planes.** The alternative, putting the sources' claims directly into a causal graph, is what the model has done so far. The feedback shows that this destroys exactly what makes the compilation trustworthy:
- the same incident is told with different actors (TaskRabbit, fb:lit-a §2);
- one sentence propagates and looks like agreement (fb:intl-eu §4, fb:uk-gov §10);
- the same word reverses meaning ("misaligned outputs" in NIST AI 100-2 means aligned with the *attacker*, fb:us-gov §4).

A view can collapse these differences on purpose. The records cannot.

## 2. The evidence plane: documents, parts, passages

- **Document ≠ key.** One relata key can hold several documents: NSPM-11 plus its fact sheet, and the RFI key with three Federal Register notices (fb:us-gov §1b). The relata copies of four frameworks are silent re-uploads (co-others atlas). Record the version actually read, its date, and its **extraction condition**, because silence caused by our tooling must not read as the source's silence (fb:co-anthropic-openai §2k).
- **Documents have parts, and parts carry force.**
  - Recitals vs articles; the Code's "recognise / commit to / will" layers (fb:intl-eu §2a).
  - IAEA's integral appendices vs non-integral annexes and footnotes (fb:safety-science-press §7).
  - SB 53's "encouraged, but not required" inside a statute (fb:us-gov §1b).

  **Force belongs to a part or passage, defaulting to the document's declaration.** Other documents also make *assertions about* a document's force, and they can be wrong (four authors on the Code's legal effect, one of them mistaken, fb:intl-eu §2a). So force is an attributed assertion, not an attribute.
- **Temporal validity for normative text:** in force from, applies from, enforceable from, superseded by. The AI Act applies provision by provision, the Omnibus moves some dates, and GPAI duties applied a year before they could be enforced (fb:intl-eu §2b). "The Act as in force on date D" is a computed view (Act + amendments).
- **Declared scope, including exclusions, at document or section level.** Examples: NIST 600-1 excludes "speculative risks"; AI 800-1 covers deliberate misuse only (fb:us-gov §1d); Singapore 2026 excludes agents "functioning exactly as engineered" (fb:intl-eu §8). This is what lets a coverage view tell "out of declared scope" from "silent".
- **Passage locators:**
  - line and page;
  - heading path, since in IASR 2026 headings are themselves claims and the section path pre-types the claim (fb:iasr §2);
  - table/row/column, since nearly every framework threshold lives in a table that `pdftotext -layout` interleaves (fb:co-others C8);
  - footnote and caption.

  For tables the text should come from the PDF, not the extraction line order.
- **Kinds of absence**, recorded on the passage or document: lost in our extraction; held elsewhere (Aguirre's controls on GitHub); withheld for hazard (VCT); redacted with a stated reason ("Threat variant 7: [redacted]"); cited but not present; classified (the NSPM-11 annex); published only as a group average (NRR cyber scores). Sources: fb:lit-b §I, fb:co-anthropic-openai §2k, fb:uk-gov §15. Each supports a different inference from silence.
- **Documents that are schemas.** Forms, templates and questionnaires assert little directly; their fields *define what a record is*. The EU incident template and the HAIP questionnaire are two (fb:intl-eu §3g). Treat them as sources of vocabulary and record structure.

## 3. The assertion record

An assertion is one speech act, over one content, anchored to one or more passages. Several speech acts can share a content. RSP v3 Appendix A makes one standard both an industry recommendation and a competitor-contingent commitment (fb:co-anthropic-openai §3).

### 3.1 Who: authorship is several roles

| Role | Why it's separate | Example |
|---|---|---|
| **writers** | who produced the text | IASR's writing group |
| **responsible party** | who answers for it | IASR's Chair holds "ultimate responsibility" while the report "does not necessarily represent the views of the Chair" (fb:iasr §2b) |
| **endorsement status** | full / subset of listed authors / collective, non-unanimous / none | Anderljung and Brundage disclaim unanimous endorsement; the UN report is "majority consensus" (fb:lit-a §6, fb:intl-eu §8) |
| **relation to the subject** | self-report / commissioned or published by the subject / independent; **interests**, disclosed by source vs inferred by us | Anthropic publishing Claude's review of its own report; FLI grading endorsement of its own statement; VCT funded by the labs it tests (fb:co-anthropic-openai §3, fb:lit-b §I) |
| **rendering, per layer of relay** | verbatim / fragment / paraphrase / characterisation | the same court majority paraphrased by Reuters and quoted by CNBC (fb:safety-science-press §6) |
| **channel as author** | a relay can add its own claim | NPR's unattributed "siding with its moral stance" (fb:safety-science-press §6) |

Nested voices stay nested. For example: IASR *reports* that Anthropic *treated* a model as meeting a threshold. Stance is recorded per layer (fb:iasr §3).

### 3.2 Stance: three questions, not one list

The feedback produced about fifteen stance values. They sort into three independent questions.

1. **Commitment to the content's truth:**
   - asserts;
   - believes, with adjudication deferred to another body ("supports allowing the Courts to resolve this", fb:us-gov §2);
   - speculates (fb:lit-a §6);
   - reports without endorsing, IASR's default mode (fb:iasr §3);
   - relays (Vaintrob's skimmed Forbes taxonomy, fb:lit-b §A);
   - explicitly abstains or declines a position (IST on where the world sits on its own scale; Shah declining loss of control as a category);
   - holds insufficient but not false (Kasirzadeh on the decisive view);
   - rejects or rebuts;
   - discounts as a class (Ren's "Dubious Intuitive Arguments", fb:lit-b §A);
   - rules out on evidence ("Distraction Not a Factor", fb:safety-science-press §2e).
2. **The content's mode:**
   - factual;
   - hypothetical or scenario (see §6.9);
   - illustrative, soundness disclaimed ("We do not claim that a safety case with this structure … would be sufficient", fb:lit-a §6);
   - exhibited as a specimen: a quote included because its existence is the evidence, e.g. "I can blackmail you…" (fb:iasr §3);
   - presupposed, inside a directive or a question (EO 14365's "truthful outputs", fb:us-gov §1c);
   - stipulated for this document ("I consider them an auditor for the purposes of this article", fb:lit-a §4e);
   - adopted as an analytic lens (ICAO's use of the Reason model, fb:safety-science-press §2a).
3. **Coupling to action:**
   - none;
   - treated-as: commitment-grade, not belief-grade ("provisionally meeting … to err on the side of caution");
   - adopted in reliance: the author records a claim and makes its own action conditional on it (the AG–OpenAI MOU, fb:us-gov §7);
   - adopted assumption, which comes in three kinds (fb:uk-gov §4): the author's own working assumption (it belongs on the *condition* of the claims it scopes), an assumption prescribed to the reader (a recommendation about belief), and precautionary treat-as.

**Characterises-position-of** is a relation, not a stance: author A says, in A's own words, that party B holds X (Kasirzadeh on Bostrom and Ord, fb:lit-b §A). The sentence must never be attributed to B as a quotation.

**Intent**, wherever a kind carries it, has four values beyond a positive claim: unknown / disclaimed by the source / investigated and not found (the Gemini report, fb:co-others C3) / mechanism asserted in place of intent ("deception emerged as a by-product", fb:uk-aisi §3d). It also needs its **principal**: whose intent defines the term. That can be the evaluator (cheating, Hamin), the developer (Shah's misalignment), developers or deployers, the user, "authorized constraints" (IST), or an attacker (AI 100-2). See fb:lit-a §5 and fb:us-gov §4.

### 3.3 Qualifiers: declared in scope, inherited, typed

Sources declare many qualifiers once, for a whole document, section or table, and every assertion inside inherits them. Examples:
- *Loss of Oversight*: "Likelihood … absent substantial effort to prevent it"; "regime before full automation of AI R&D".
- The Frontier report: "should not be read as a forecast".
- Cyber-horizons: token cap and success threshold, "spelled out" once as the "full interpretation" (fb:uk-aisi §2b).
- The Code's precautionary-principle recital (fb:intl-eu §8).
- Declared non-recommendation (IASR).

**Proposal:** a qualifier can be a **binding minted in a scope**, which the assertions inside that scope resolve through. This is address theory applied to qualifiers, the same mechanism as §5 applies to terms. The resolution path says "inherited from the scope statement at L…" or "stated in the sentence". Declared force works the same way, but must *not* be inherited blindly: IASR declares no recommendations and still says "should not release" (fb:iasr §4). A view flags conflicts between a declared scope qualifier and a sentence.

Qualifier axes, grouped:
- **Likelihood**, as a structured value, not one axis (fb:uk-gov §2–3):
  - the scale's identity: PHIA as printed where; NRR 1–5; prose. The same word is not safely the same number across documents, and the NRR's mapping onto PHIA puts five PHIA words into one score;
  - what it is a probability *of*: a proposition vs a defined scenario;
  - the window;
  - composition (intent × capability × vulnerability);
  - **confidence as a separate rating**;
  - relayed calibration: whose scale it is (IASR's one calibrated clause is NCSC's, fb:iasr §4).

  The value may be typed status / trend / conditional rather than probability. *Loss of Oversight*'s "Likelihood" column holds "Current limitation", "Likely to increase" and "Dependent on misalignment", and gives the same pathway different values in the summary and the body (fb:uk-aisi §2a).
- **Knowledge and evidence:**
  - knowledge state ("to the best of our knowledge");
  - evidential breadth ("one study" / "several" / "a large number"), IASR's main carrier of confidence (fb:iasr §1);
  - **as-of or coverage date**, distinct from document date: negative existence claims mean nothing without it (fb:iasr §4, fb:co-anthropic-openai §2d);
  - evidence exists but is unpublished ("internal evaluations", fb:uk-aisi §3h);
  - withheld or classified;
  - practice maturity, and a stability flag on tentative definitions (fb:us-gov §5, fb:co-anthropic-openai §2m).
- **Conditions and scope:**
  - condition;
  - regime or timeline;
  - **perspective**: marginal vs absolute, which both companies make definitional (fb:co-anthropic-openai §2b);
  - **mitigation state**: unmitigated or fully elicited / with mitigations / residual. The Commission separates risk posed from risk after mitigation (fb:intl-eu §3c);
  - **severity basis**: worst foreseeable / reasonable worst case / typical (ICAO; NRR; fb:safety-science-press §3);
  - **legal-standard qualifiers**: "foreseeable and material", "reasonable cause to believe". These are tests a fact-finder applies, not probabilities (fb:us-gov §5).
- **Measurement conditions:**
  - **elicitation, as a ladder:** unprompted / inherited trajectory / environmental nudge / explicitly directed / task pressure (including an impossible task) (fb:uk-aisi §2d);
  - **context of use** (evaluation / internal / public) **vs where effects landed** (sandbox / the evaluator's infrastructure / third parties). These are two axes, and containment is nested (fb:uk-aisi §2c);
  - **baseline**: dated, and attachable to definitions and commitments as well as measurements (fb:co-others B1, fb:co-anthropic-openai §2c);
  - bound direction;
  - **derivation of the number**: direct / aggregated / imputed / extrapolated from a fitted trend (fb:us-gov §5);
  - **disclosure or aggregation**: "value is the mean over group G; the individual value is withheld" (fb:uk-gov §15);
  - instrument access: public / private / semi-private.

  The *subject* of a measurement is a configured system (§6.3), not a qualifier.
- **Severity labels carry their anchors** where they have any, e.g. SB 53's >50 deaths or $1B, OpenAI PF's "thousands of people", or none ("plain meaning"). "Signs, not magnitudes" holds for our quantities; source magnitudes and banded thresholds are carried verbatim as structured qualifiers (fb:uk-gov §3, fb:lit-a §7).

The source's own hedge always stays verbatim beside any coding of it.

### 3.4 Relations between assertions

**Argument structure** (fb:lit-b §B, fb:co-anthropic-openai §2f):
- `premise-of` / `supports`;
- `defeats`, attached to the premise it defeats: Kierans' one hedge defeats premise 4 alone;
- `justifies`, from a finding or purpose clause to a normative provision it grounds (SB 53's findings; EO purpose clauses; CSB's "Whereas" premises) (fb:us-gov §2, fb:safety-science-press §4). This is the most direct bridge from the policy end of the chain back to the risk claims;
- properties of an argument:
  - aggregation mode: conjunctive, disjunctive or convergent, with the source's own caveat about correlated sub-claims;
  - support strength per premise (Strong / Moderate / Weak);
  - load-bearing dependencies;
  - coverage claims ("threat modeling is sufficient");
  - an assumption with its stated fallback;
  - **transfer by dominance** ("serve as an upper bound for the risks of this model as well").
- The claims–arguments–evidence (CAE) tradition and its notation, GSN, are the mature form of this. That is from fb:uk-aisi §5, marked there as training knowledge.

**Lineage**, with subtypes. "Changes marked" can hold several edits: subject replaced *and* predicate truncated (HMG → DSIT); a hedge dropped (SL5 "most"); force changed; content added.

| Subtype | Example |
|---|---|
| verbatim / near copy | G7 → AI Act recital 110; Code Measure 9.2 → incident template; DSIT code → ETSI EN 304 223 (**wording copies, force does not**) |
| citation as basis | the Code's "LEGAL TEXT" headers; recital 110 behind App. 1 (fb:intl-eu §1, §4) |
| restatement by a secondary source, drift in either direction | Hoffmann's "presumption of conformity"; Singapore 2026 *strengthening* AI Act Art. 14 |
| summary of (may add) | NCSC's blog adds "loss of control", which the ASD guidance never uses; the IASR Extended Summary adds "19 of 20" (fb:uk-gov §10, fb:iasr §2) |
| same claim refiled in another container | the FCF's "Loss of Control" tiers are the RSP's thresholds verbatim: one claim, not corroboration (fb:co-anthropic-openai §2e) |
| channel variants of one finding | AISI's blog and technical report headlines: one assertion, two renderings, scope slightly different (fb:uk-aisi §4) |
| one text, several publishers | the Kimi K3 assessment (AISI + CAISI) |
| within-document boilerplate | one AI sentence repeated across ~10 NRR summaries (fb:uk-gov §10) |
| via (an intermediary recorded by the source) | "Source: Zou et al., cited in Anthropic 2025" (fb:iasr §5) |
| versioned within an author, with announcement status | OpenAI's four-step cyber determination; framework revisions under Zhu's ANN / ANN-P / SIL / NCL (fb:co-others B2); AISI's own doubling-time series 8 → 4.7 → "exceeded" (fb:uk-aisi §4) |
| amendment | Omnibus → Act, by edit instruction |
| rescinds / replaces; orders revision of; withdrawn | NSPM-11 rescinds NSM-25; the Action Plan orders the AI RMF revised (external, not the author's drift); a withdrawn CAISI page (fb:us-gov §3) |
| tasks → fulfils; implements; reports against; interprets | Action Plan → the DeepSeek report; Code → Arts. 53/55; Perset → G7 Actions; Commission guidelines → Act |
| preempts / carves out / disapplies; deemed equivalent | EO 14365; SB 53 Sec. 5(d); federal-standard equivalence (fb:us-gov §3) |
| same text, new force | xAI's RMF relabelled as a TFAIA compliance instrument (fb:co-others C7) |

**Contest:** within a source (AISI's counter-evidence to its own misconfiguration hypothesis; the Aug report's reviewer vs the company on the risk upgrade) and across sources (commentary vs its primary).

**Corroboration** is a view, computed after lineage, author clusters, interests and channel variants are known. It is never a count of passages.

## 4. Assertion kinds

Kinds are open to extension. Where a source's sentence is ambiguous between kinds, the kind itself can be recorded as **ambiguous among named candidates**. Present tense in the frameworks, for example, can be a report of practice, a standing commitment or a claim about the world (fb:co-others A6). Grammatical mood is not a safe guide: NCSC writes norms in the indicative ("You are confident that…", fb:uk-gov §7).

| Family | Kinds, with the fields the feedback asked for |
|---|---|
| **About the world** | **measurement/observation** (instrument §6.8, configured subject §6.3, conditions §3.3); **causal**, "A contributes to B" (fields in §7); **attribution**: a share of an observed change assigned to a cause against named rivals (IASR Table 2.3, fb:iasr §1); **counterfactual**, including on a node intervention (fb:lit-b §I); **trend** and **trend extrapolation**: rate, persistence condition, projected state at a date (fb:iasr §1); **forecast**, possibly required by a norm (fb:intl-eu §3e); **change claim**, world-change kept distinct from evidence-change (fb:iasr §1); **assessment/verdict**: level or sufficiency of a node, with subject, scale, perspective and as-of (fb:co-anthropic-openai §2a); **mind attribution**: belief about situation, motive, awareness, each with its evidence channel, whose reliability is itself assessed (fb:uk-aisi §3d); **existence claim about an event class**, with no events described (fb:uk-gov §6); **capacity-to-oversee assessment** (CSB on OSHA, fb:safety-science-press §4) |
| **About knowledge** | **evidence state**, split three ways into gap / barrier / open question (AI 800-4, fb:us-gov §2); **opinion distribution**, with a basis (elicited: method, n, panel composition / characterised by the author / the author's own panel) (fb:iasr §1, fb:uk-aisi §5); **claim about a claim** (validity, scope, interpretation of an instrument, comparison); **epistemic policy**: standing rules for weighing evidence, and burden-of-proof defaults (fb:co-anthropic-openai §2g–h, fb:co-others C2); **formal or impossibility result** (AI 100-2, fb:us-gov §2) |
| **Normative** | **norm** (§6.4), with **commitment** as the case imposer = bearer; **recommendation**: addressee, authority basis, premises (`justifies`), interim vs final (fb:safety-science-press §4); **decision** (§6.5); **assignment of decision authority**: decider, considerations, veto or override, who is informed (fb:co-others A4) |
| **Definitional and classificatory** | **definition** = a binding (§5); **classification**: scheme + classifier + subject, "for the purposes of" allowed (§6.10); **crosswalk**: a source's own mapping between vocabularies (fb:lit-a §4c); **exemplar**: worked examples that fix a term's extension, i.e. match test cases (fb:intl-eu §3f); **scheme proposal**: levels, criteria, attached responses, with no placement act (IST's 0–5, Brundage's AAL-1 to AAL-4, fb:lit-a §4b) |
| **Argumentative** | **argument** (§3.4); **analogy/transfer**: source domain, target, respects claimed and denied ("Where Analogies Break"), the most common argument form in lit-a (fb:lit-a §4a); **scenario** (§6.9); **estimate derived from a scenario**: method and assumptions, so a number that began as fiction doesn't pass as measurement (Stix prices extinction at $543.5T, fb:lit-a §4d) |

## 5. The vocabulary layer, and resolution

Address theory (`~/src/arch/firmatum/udon/v2/references/def/`) supplies the mechanism, and the corpus exercises every part of it.

**Scopes** are nested: document, part, section, code section. They can also be purpose-indexed: "training compute" means one quantity for one classification and another for a second (fb:intl-eu §7). SB 53 defines "catastrophic risk" twice, once per code section (fb:us-gov §4). IASR 2025 has three nested scope levels, with section-local overrides (fb:iasr §6).

**Bindings** come in several forms:
- minted;
- **imported** ("the AI Act definition applies, and such definition shall prevail"; xAI adopting the Code's terminology; "we adopt this definition throughout", then a divergent gloss) (fb:intl-eu §7, fb:co-others C6, fb:lit-b §H3);
- a common word **rebound** ("model" in the Code; "AI systems" in Singapore);
- definitions of **function words** ("including" is non-exhaustive);
- **inline** definitions, which must be recorded as bindings in their section scope, or IASR 2026's internal drift is invisible (fb:iasr §6).

A field *labelled* "Definition" may not define: the CRA's boxes are characterisations (fb:uk-gov §11). A glossary may omit the report's own subject: IST defines neither "loss of control" nor accident (fb:lit-a §9).

**Deictic definitions need a time index:**
- "today's most advanced models" fixes its referent at the document date;
- "the most capable models at any given time" moves;
- Magic pins "as of May 2024".

This is SB 53 §22757.14 (widen to L453–487 to include external verifiability) and the AI Act's "high-impact capabilities" (a rebuttable, per-model test) in definition form (fb:uk-gov §11, fb:co-others C5, fb:intl-eu §7).

**A resolution record** is kept per occurrence of a key term:
- **outcome**, one of:
  - one;
  - several;
  - none (a gap in our vocabulary);
  - ambiguous among named candidates;
  - **withheld by source** (Model A/B, ⟨PERSON_A⟩, a classified threshold);
  - **delegated to the reader** (CISA, DHS);
  - **defective as written** (DSIT and ETSI's "Affected entities … not directly affected");
  - **deliberately unbound** (the RSP's "plain meaning");
  - **declined by source** (Shah on loss of control);
- **path**: the source's glossary / a section definition / imported / the methods section (the DeepSeek "hijacked" = *attempted*, which the headline drops) / our reading / coined;
- **author**: us / the source / a third party;
- **time index** where the term is deictic;
- for relational terms, a **reference standard** and a **bearer**. Examples:
  - "Alignment" is measured against a task, developer intent, a constitution, human values, oversight, authorised constraints, or an attacker's goal, and is borne by a computation, a behaviour, a model, an activity or an institution (fb:co-anthropic-openai §2l);
  - "Misalignment", "misuse", "accident" and "unintended" also need the **principal** whose intent is the reference (§3.2).

The load is concentrated. Per-occurrence resolution matters most for about a dozen terms:
- catastrophic, severe and systemic risk;
- loss of control;
- (mis)alignment;
- safeguard(s);
- hazard;
- developer, provider and deployer;
- capability thresholds, and High/Critical;
- marginal/absolute;
- incident;
- sabotage;
- "frontier".

A per-term lexical map suffices for the rest (fb:co-anthropic-openai §5). Kasirzadeh's four senses of "risk" (an event, its cause, its probability, its expected value) are the test case: they resolve to a node, a node at a different stage, a qualifier and a product respectively (fb:lit-b §H1). **"Hazard"** resolves as ambiguous among at least three bindings in the corpus:
- ICAO's "potential to cause or contribute", the traditional definition;
- Leveson and Barrett's state that "will lead" to a loss under worst-case conditions;
- Mylius's "can lead".

ICAO itself warns that people confuse hazards with their consequences (fb:safety-science-press §1).

**Collisions the sources report themselves**, and cross-source handling of rival definitions, are both precedents. Brundage flags that AAL already existed with other meanings. CSB sets three definitions of safety culture side by side with its reason for choosing one (fb:lit-a §9, fb:safety-science-press §5). The vocabulary layer keeps its own change history, with reasons, after Slattery.

## 6. The model plane: entity kinds

### 6.1 Actors
Actors persist across names, with dated names and mandates. US AISI became CAISI "Pro-Innovation, Pro-Science"; the consortium was renamed (fb:us-gov §5). An actor has a **grouping level**: legal entity vs undertaking, as in the Omnibus's "same undertaking" (fb:intl-eu §5).

### 6.2 Roles: conferred by an instrument, under conditions
A role is not a label on an organisation. It is **conferred by an instrument under stated conditions**, and each conferral is an attributed assertion: "under instrument I, actor A holds role R because condition C" (fb:intl-eu §5). The conditions include:
- activity plus a market act (AI Act provider);
- a quantitative threshold that fine-tuners can cross (SB 53, the guidelines' one-third-compute rule);
- control over weights or the execution environment;
- corporate grouping;
- jurisdictional fallback.

The same organisation can hold different roles under different instruments for the same model. This is the frame for Joseph's open "developer" decision. SB 53's "frontier developer" is a threshold-tested role attaching to a legal person (fb:us-gov §4). In many definitions, "developer" is also *the holder of the reference intent*, which is a separate job (fb:lit-a §5).

Role vocabularies found in the corpus:
- Joseph's writers map, on the agent-facing side;
- AISI's supply-chain list;
- AI RMF Appendix A's roles as **tasks** per lifecycle phase;
- DHS's five roles × five responsibility areas ("entities may play more than one role"; its own glossary collides internally);
- ETSI's in-source crosswalk to AI Act roles;
- STPA's controllers at multiple levels;
- threat actors defined by capability profile (Microsoft's grid, Meta, Gemini, G42; AI 800-1's threat profiles);
- the evaluator as trusted-access partner, both a prevention and a hazard source (AISI's incident);
- bystanders as barriers;
- responders, in the NRR's three classes;
- addressees, including "the field" (GDM) and "unaddressed by design" (IAEA).

**AI systems hold roles too:** controlled process, controller or both; actor; target (a prompt injection aimed at coding agents); collaborator (agents coordinating through a shared repository); adversary (Shah's "the AI is an adversary") (fb:lit-a §10, fb:uk-aisi §3f).

### 6.3 Systems: the configured subject
The subject of a measurement or verdict is **model × configuration × surface**. Configuration includes checkpoint, safeguard state ("GPT-5.6 Sol without cyber classifiers"), helpful-only variant, scaffold, token budget, quantisation, API vs self-hosted, access regime and **deployment scope** (internal / restricted external / public / open-weight). One set of weights can be two named products. "Model 1", "IM1" and "Model A" are subjects too. Comparisons across documents usually compare differently configured systems. Sources: fb:uk-aisi §3a, fb:co-anthropic-openai §2j, fb:us-gov §5. Joseph's surfaces vocabulary (`terms/def-agent-surfaces.ud`) is part of this.

### 6.4 Norms (commitment as a special case)
Three families reached this independently (fb:intl-eu §2c, fb:us-gov §1a, fb:co-others A1–A5). A **norm** has:
- **roles:** imposer or issuer; **bearer** (who is bound, often a role defined by a match test); **addressee** (self / named others / "the field" / regulators); beneficiary; **enforcer**;
- a **deontic type:** obligation / prohibition / permission / exemption / **power** (who may decide). The most consequential framework sentences grant permissions ("benefits … outweigh the risks") or assign decision authority ("Leadership can … make decisions without the SAG"). Coggins's allow / encourage / request / demand / refuse is the precedent (fb:co-others A1);
- **strength** within its type: Zhu's ladder, for obligations;
- **applicability condition**, structured over roles × classifications (Canada's matrix; the AI Act's role × GPAI-class keying);
- **trigger → time limit → act:** notification within two weeks; incident reports at 2, 5, 10 or 15 days; 15 days vs 72 hours between SB 53 and RAISE;
- **consequence**, conditioned-on other actors (competitor-contingent), **burden-holder** and **default if unshown**;
- **temporal validity** (§2);
- **depends-on-definition** links. A definition edit can change every trigger that uses it, as when Meta replaced "uniquely enable" with "substantially contribute to" (fb:co-others A5);
- the object can be **a future commitment**, and a slot can be **declared but empty**: "we are studying…", "open research problem", "a limit" left unstated (fb:co-others A3, fb:co-anthropic-openai §3).

A **commitment** is a norm where imposer = bearer, or one that a party adopts ("Signatories commit to"). **Enactments** link to the norms they fulfil or breach (§6.5). Zhu's six materiality dimensions carry over once "actor" is split into imposer, bearer and enforcer. They also apply *across instruments*: SB 53 vs RAISE is one provision text at two strengths (fb:us-gov §1a). Add "duplicated into a companion" beside "relocated" (fb:co-anthropic-openai §5).

### 6.5 Events, reports, decisions, changes
- **Recorded events are thin:** what happened, when, to what, stated verbatim in the anchoring passages. **Actor, action description, intent, causal explanation and even identity across sources are attributed assertions *about* the event.** The sources dispute exactly these: TaskRabbit's actor, Kiro's action, whether two retellings are the same incident (fb:lit-a §2).
- **Reports are distinct from incidents.** CLTR clusters reports into incidents by a deduplication that can mis-merge. A report carries its status: allegation, user post, company disclosure, regulator finding. Counts should be recomputable (fb:lit-a §2).
- **Event outcomes are graded:** attempt / success / real-world effect / harm. **Barriers that held are part of the record**, including ones never designed as controls ("a human reviewer"; a member of the public; GitHub's first-contributor hold), with the margin ("resting on human vigilance rather than a technical barrier") (fb:uk-aisi §3b).
- **Denominators:** events link to the run population they came from (19 events across 10 of 122 runs), so rates are derivable (fb:uk-aisi §3c).
- **Event relations:**
  - motivates a revision of a register (CrowdStrike → the NRR);
  - cited as evidence of salience;
  - used as an exemplar of a generalisation (fb:uk-gov §6);
  - characterisations change over time within one source (Zwetsloot on Uber, fb:lit-b §I).
- **Institutional acts are events:** determinations with procedural standing, pauses and restarts, weight quarantines, ASL-3 activation, goals dropped or rescheduled. They link to the commitments they enact or leave unenacted (fb:co-anthropic-openai §2i).
- **Decisions:** actor, date, choice, stated rationale, alternatives foregone ("a less expensive option was chosen"). They appear at the *cause* end of the chain as well as the governance end (CSB's timeline; ICAO's latent conditions from decisions that "had good intentions") (fb:safety-science-press §4).
- **Warnings and precursors:** source, recipient, date, response, and a `warned-of` / `precursor-of` relation.
- **Organisational change events,** with HSE's split between risks *from* the change and risks from the *process* of changing. **Drift and cumulative minor change are trajectories, not events**, held as trend claims (fb:safety-science-press §4). This is where Joseph's hypergrowth thread lands structurally.
- **Aggregate-only events:** statutory incident reports that will surface only as anonymised annual aggregates, classified by an interested party (fb:us-gov §5).

### 6.6 Controls
Controls get attributes the sources use consistently (fb:uk-aisi §3e, fb:safety-science-press §3, fb:uk-gov §13):
- **locus:** model / scaffold / procedural;
- **reliability class:** passive > active > procedural (the CCPS hierarchy);
- **strategy:** avoidance / reduction / segregation (ICAO);
- **timing:** synchronous vs asynchronous; online vs offline;
- **removability** ("easily reversible with access to the weights");
- **operator;**
- **robustness measured as attacker effort** (10 minutes vs 7+ expert-hours);
- **maturity ladder** (NCSC's levels 1–4);
- **purpose:** harm prevention vs incrimination;
- **conflict with measurement validity** (the incident's controls were off *because* they would have defeated the evaluation);
- **sufficiency standard** (ALARP, "all measures necessary", tolerability classes; the frameworks' "acceptable level" sits on this axis);
- ICAO's evaluation attributes, including **residual risk** and **unintended consequences**.

**Controls are related to each other:** independent of / **shares a failure mode with**. Otherwise "three layers" counts as three whether or not they fail together (ICAO: "Sometimes all of the weaknesses align").

### 6.7 Indicators
An indicator is a standing measure with its own claims (fb:safety-science-press §3):
- leading vs lagging;
- `indicates` / **fails to indicate** a hazard state (BP's personal-injury rate);
- **incentivises** an actor, so the indicator can be a cause (BP's bonuses);
- gaming;
- **trigger = indicator + threshold → required action.** This is structurally the frontier frameworks' capability-threshold pattern. ICAO's caveat travels with any crosswalk: triggers are "arguably less relevant to … socio-technical systems".

The IST indicator/indication pair ("what should we watch for" vs "what are we seeing happen") links ideated and recorded events (fb:lit-a §2).

### 6.8 Instruments
Benchmarks, rubrics, classifiers and scales are records with:
- version and threshold;
- the construct claimed;
- validation claims;
- stated validity limits;
- access (public / private);
- **proxy for …**;
- **withheld for hazard;**
- the **object measured**: system behaviour / a disclosure / expert opinion;
- revisions over a series.

Caveats are written once on the instrument and **propagate** to every measurement that uses it:
- Ren's finding that a safety benchmark correlates 78.7% with capabilities;
- CLTR's score called "credibility" in its method and "severity" in its findings, when its own authors say it is neither a severity nor a likelihood;
- an instrument swapped mid-series;
- a definition diverging from its operationalisation (self-replication "without being explicitly prompted" measured by directed tasks).

AI 800-2's construct / criterion / instrument / validity is measurement theory's version of §5. Sources: fb:lit-b §E, fb:lit-a §3, fb:uk-aisi §3i, fb:us-gov §6.

### 6.9 Scenarios
A scenario has:
- a **function:** planning / exploratory / illustrative / method;
- a **selection rule** for a scenario set (GO-Science deliberately excluded benign scenarios);
- a **provenance grade:** observed / adapted from observed / constructed.

The NRR's **reasonable worst-case scenario is a scored focal event**, carrying likelihood, impact, key assumptions and variations (fb:uk-gov §5, fb:iasr §1). Joseph's "ideated" risk events live here.

### 6.10 Schemes and classifications
A classification scheme declares its properties:
- exhaustive or not;
- mutually exclusive or not;
- ordering, and by what;
- purpose (Mitre's five problems are "a rubric", not a model of the world).

Practice can contradict the declaration: Slattery declares non-exclusive domains, then codes single-category with a single coder (fb:lit-b §G). A classification assertion names its scheme. Hacker classifies one phenomenon under three regimes with three verdicts. Kinds can sit under several parents with stable IDs (AI 100-2's polyhierarchy, fb:us-gov §6).

### 6.11 Quantities and impact targets
Quantities remain the nodes causal assertions connect, each `of:` its terms. **Epistemic and attribution conditions can be quantities:** "challenges in perceiving … harm" and "unclear attribution" are *sources of risk* in Uuk; opacity leads to no attribution, no liability, no incentive in Kierans. These are distinct from qualifiers on *our* knowledge (fb:lit-b §D). **Governance nodes can be causes** ("AI development outpaces regulation" is a causal factor of loss of control in Barrett, fb:lit-a §10).

**Impact targets** are a group of people **or a system or shared good** (trust, an institution, the information ecosystem), with collective vs aggregate marked ("collective harms that exceed the sum of individual impacts", fb:lit-b §C). **Vulnerability is relative to the focal risk** ("vulnerable in the context of one risk might not be for another", NRR), so a harmed group is a role in an impact assertion, not an attribute of people (fb:uk-gov §9). The CRA makes vulnerable persons both a risk and a target.

## 7. The causal chain in the model plane

**Stage is a role relative to a focal event,** not a property of a kind. Every family that spoke to it agreed (ICAO: a fifteen-knot wind is a hazard across the runway and not along it; the Feb Risk Report: "our pathways don't represent catastrophic outcomes in themselves"; AISI's incident). Kinds may carry a typical stage for navigation. **Lifecycle phase** (six phases in Barrett's key) and **deployment scope** are separate axes. Internal deployment breaks a pre/post binary (fb:lit-a §10, fb:co-others A7).

**Edge roles** (all attributed, all signed where a sign is asserted):
- causes / contributes;
- **requires / enables**, as a necessary condition, with **condition groups (AND)**. IASR's loss of control needs capability *and* propensity *and* deployment environment; with signs only, that would read as three independent causes. The frameworks' logic is mostly necessity ("this essential part is still a barrier") (fb:iasr §7, fb:co-others C1);
- **is a barrier or bottleneck to;**
- prevents (with the path it blocks named, as in Davidson's rules table);
- escalates;
- impacts: target, degree across banded dimensions (the NRR's seven), **reversibility/recoverability**. Recoverability is the axis on which the loss-of-control definitions split, and the sources keep it distinct from severity (fb:lit-a §7, fb:uk-gov §12, fb:lit-b §C);
- mitigates or recovers; a mitigation edge can also carry harm (NRR Principle 5);
- governs;
- justifies.

**Attributes of causal assertions** (fb:safety-science-press §2):
- **generality:** particular event / class of events / universal. Named general theories (Reason, Snook) are kept apart from case findings in the investigator's own voice;
- **depth:** immediate / contributing / root;
- **latency:** active / latent;
- organisational distance from the event;
- **the source of the expectation**, for causes stated as omissions: actor, expected action, the standard it is measured against, the deviation. This is what CSB actually argues over;
- **adversarial vs non-adversarial dynamics.** Shah and Gruetzemacher build on this distinction and STPA doesn't make it (fb:lit-a §1d);
- attribution share (§4).

Norms about where causal analysis may stop ("failure to follow procedure is not a root cause") are claims about causal attribution practice, and matter for the disputed AI incident retellings. **Culpability is a separate kind from causation:** CSB finds causes, OSHA finds wilful violations, courts adjudicate.

## 8. Precedents, corrected and extended

Each is correlated with something; the correlation travels with it.

| Precedent | What the model takes from it | Correlation / caveat |
|---|---|---|
| **STPA** (Leveson & Thomas: vocabulary; **Mylius**: organisational application, system boundary around the whole company; **Barrett**: AI-specific causal characteristics and a survey of loss-of-control perspectives) | losses; hazards (the STPA binding); control structure at levels; unsafe control actions; **Type B scenarios: a control action executed improperly or not followed**, where "AI resistant to shutdown" lives | Barrett covers one archetype and the operations phase only (regulatory layers, multi-agent dynamics and AI controllers are out of scope). STPA defines itself *against* root-cause analysis, HAZOP and the Reason model, so mapping CSB or ICAO into STPA terms is *our* resolution. No adversary distinction. Barrett, Bollinger, Gomez, Mylius and CLTR are one social neighbourhood. AISI's own agenda uses STPA and FTA. Six national cyber agencies (ASD-led) recommend STPA and CAST. (fb:lit-a §1, fb:safety-science-press §1, fb:uk-gov §13, fb:uk-aisi §5) |
| **Zhu codebook** + **Coggins** mechanisms + **Stelling** KRI/KCI | norm strength, materiality dimensions, change outcomes, announcement status; deontic type; thresholds paired with required mitigation levels | Zhu's first-pass coding by a Claude model; Zhu verifies against Stelling (both SaferAI-adjacent); SaferAI advised G42 and scores it |
| **NRR / NSRA method** | reasonable worst case as the scored focal event; likelihood as P(≥ once in window); composite intent × capability × vulnerability; confidence as its own rating; **seven impact dimensions with banded, logarithmic thresholds** (the nearest precedent for Joseph's degree/scale tree); common consequences → 23 generic response capabilities; responders by class; vulnerability relative to risk | UK government; the public text is a declassified subset |
| **UK Chronic Risks Analysis** | a signed interaction network; groups of people as impact targets; per-risk diagrams with edges labelled by causal sentences | the full network is unpublished; polarity appears only on the vulnerable-groups map; edges cross into NRR nodes (fb:uk-gov §14) |
| **NIST AI 800-2** §3.3 + construct / criterion / instrument; **AI RMF App. A** (roles as tasks); **AI 800-1** threat profiles and barriers; **AI 100-2** stable IDs in a polyhierarchy; **CAISI's four-voice report template** | assertion typing; instrument records; roles; the prevention stage seen from the misuse side; multi-parent kinds; layered voice formatted by a source | an ipd; the RMF revision has been ordered; 800-1 never finalised |
| **DHS roles matrix** and **scale-ordered risk categories** | roles × responsibilities; an asset → sector → systemic → national scale | a board including the labs; a prior administration |
| **EU incident template + Code Commitment 9** | an incident record whose fields map onto Joseph's chain; the "reasonable likelihood" causal-attribution standard; "near miss" and "resolved" defined | the template is derived from the Code: one lineage |
| **EU Code App. 1** | risk sources as capabilities / propensities / affordances; **contributing characteristics** (velocity, cascading, irreversibility, asymmetric impact) as a degree vocabulary | drafting chairs include Bengio (also IASR, Singapore) |
| **Singapore 2026** hazard → principle → practice table; defence-in-depth stages | the causes → controls link as a table; stages close to Joseph's chain, adding societal resilience | developer input; Concordia AI, FLI |
| **UN vulnerability framing**; **OECD Annex A** | "who is at risk and where"; provenance of how a risk list was built | snowball sample |
| **ICAO**: hazard register fields; glossary provenance per term; risk matrix and tolerability; mitigation typology | a published record schema; bindings marked as inherited; the P × S family | "an example only"; a source error in the printed tolerability row |
| **CCPS safeguard hierarchy** (via CSB); **CSB logic tree** | control reliability classes; **the case-level causal tree**, the direct precedent for "sources & causes tree" | **the logic tree is image-only (PDF pp. 222–235) and unread by anyone**; worth viewing before the causal design settles |
| **MIT / Slattery** | codes what a source *presents*; a vocabulary change log with reasons; causal and domain taxonomies kept separate (supports separating stage from kind) | an FLI co-author; single coder; declared non-exclusive, coded exclusive |
| **Kasirzadeh**'s four senses of "risk"; **Hacker** App. A verbatim definitions; **Davidson** rules → blocked paths; **Gekker** on living glossaries | resolution test case; a bindings-per-scope table; the `prevents` edge with the path named; "avoid premature standardization" | Kasirzadeh co-authors across four documents |
| **IASR**: source-admission criteria, the `[industry]` tag rule, per-section template, practice glossaries | evidence admission; affiliation coding; pre-typing for the 2026 full read | IASR authorship |
| **AISI *Loss of Oversight***; **CAE/GSN** (training knowledge) | degradation pathways; status assessments; marked voices; argument structure | 6 of 23 named experts are AISI staff |
| **Anthropic Aug §2.5**, **OpenAI PF tracking criteria**, **OpenAI misalignment framework**, **HF technical report event table**, **autonomous-dev measurement records** | practitioner argument vocabulary; inclusion rules; event status fields; a timestamped event record; measurement records with "what this doesn't capture" | developer self-reports; we are Anthropic models |
| **Shanghai E-T-C**, threat-source-keyed taxonomy, red and yellow lines | a government-lab sources-and-causes tree | Concordia AI co-author |

## 9. Corrections to draft 1

- AISI's blog *highlights* four behaviours (a selection plus grouping by attack line); it does not regroup all 19 events (fb:uk-aisi §1).
- The orders-of-magnitude "catastrophic" gap is inside OpenAI, between two different words ("severe harm" vs "systemic risk"). Anthropic's RSP is deliberately unbound (fb:co-anthropic-openai §1a).
- "Loss of control appears only in the statutory frameworks": the *label* is statutory, but the content is the RSP's thresholds, refiled (fb:co-anthropic-openai §1b).
- The R = Σ P·H·U decomposition is used only for misalignment, and its "abundance of caution" step has a contested rationale inside the same report (fb:co-anthropic-openai §1c).
- PHIA is not confined to NCSC and *Loss of Oversight*: HMG 2023 and the NRR use it, and the NRR maps it onto its own score (fb:uk-gov §2).
- STPA's scope, its missing Type B, its lack of an adversary distinction, and its stance against the traditional disciplines (§8 row).
- "Deployer" is defined in neither IASR glossary. I didn't check the report inline for a definition (fb:iasr).
- Recital 110 → Code is citation as basis, not a copy; the AI Act's role set is larger than provider/deployer (fb:intl-eu §1).
- The moving baselines are in definitions and acceptance criteria, not measurements. "Silent" covers two different cases (fb:co-others B).
- The usage-restriction sense of "safeguard" is a quoted letter, not the press's own voice. "Causal claims are a minority" doesn't hold for incident investigations (fb:safety-science-press §7).
- Identity of the database-deletion and matplotlib retellings was the lit-a agent's inference (fb:lit-a).

## 10. Implementation: a staged core, not the whole thing at once

Everything above is what the corpus *demands*; not all of it is needed on day one. My suggestion is a core that makes the rest addable without migration:

1. **Evidence plane first:** documents (with parts, force per part, declared scope, extraction condition) → passages (structured locators) → assertions with authorship roles, the three stance questions, kind, qualifiers (including scope-inherited ones) and the lineage and argument relations. Without this, nothing later is trustworthy.
2. **Resolution for the dozen high-load terms** (§5), with the outcome, path and author fields. A per-term lexical map for the rest, which is what `terms/` already does.
3. **Model-plane entities in the order the IASR 2026 read will need them:** quantities (the existing concepts), systems (configured), events (thin) with reports, instruments, norms. Then controls, indicators, scenarios, decisions and schemes as the sources demand them.
4. **Views last:** the causal loop diagram, bow-ties with barriers, lineage-aware corroboration, and coverage by declared scope.

Nothing is discarded:
- `relations*.yaml` claims become causal assertions anchored to passages;
- `mappings*.yaml` rows become resolutions;
- `concepts*.yaml` stay as quantities, gaining `of:`;
- `terms/` is the vocabulary layer.

## 11. Open questions for Joseph

1. Does the two-plane shape (evidence plane → resolution → model plane → views) match the holistic map he wants?
2. **STPA:** adopt its vocabulary for the chain as *our* resolution target, with source frames (root cause, Swiss cheese) recorded as presented? Or keep his chain's own terms primary, with STPA as one lexical-map source among several? My lean is the second, given STPA's self-positioning and its missing adversary distinction.
3. **"Developer":** the conferred-role frame (§6.2) is where the corpus points: roles conferred by instruments under conditions, plus an actor with a grouping level. Does that settle his open decision, or sharpen it?
4. **Impact radius:** adopt target (a group *or* a system/shared good) × degree (the NRR's banded dimensions as a starting vocabulary) × **recoverability** as the three dimensions?
5. **Format:** udon for the vocabulary layer is decided. For the evidence plane (many assertions, many relations), stay YAML until a udon parser exists, or start in udon now?
6. Does someone view the **CSB causal logic tree** (fourteen image-only pages) before the causal design settles?
