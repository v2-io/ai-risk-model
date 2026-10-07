# What the answer leaned on, and what broke

*G1b's done-test asks for two things: the terms and record fields the answer depended on, and the defects found in the plan's machinery. This file is that list. It is written for Joseph, to decide where refinement passes go first, and then for the agents doing G2 and G3. Claude (Opus 5.5), 2026-10-07. Disposable.*

*Repaired the same day after `de-novo-feedback-1.md`. §1 replaces a ranking that the computation didn't support (`response-to-de-novo-feedback-1.md` says what changed and why).*

## 1. What this slice can and cannot say about weight

### The short version

**This slice can't support a weight ranking of lexicon terms.** An earlier version of this file ranked terms for refinement, and the debrief summarized the ranking as "most of SB 53's precise clauses carried no weight; the structure around them did". That doesn't follow, for three reasons:

1. **Q1 stipulates two facts, 60 deaths and one incident.** A clause that tests anything else ("foreseeable", "material", "materially contribute", the conduct list, the exclusions) can only stay open. It could not have come out any other way. That is a fact about Q1, not about the clauses.
2. **The evaluator could only find an ambiguity decisive if I had encoded it as one.**
   - Seven were encoded at first, all on the magnitude, aggregation and umbrella side.
   - R-material's and R-control's candidates went in as plain facts.
   - R-foreseeable and R-materially-contribute were delegated to California law with no candidates.

   The ranking then promoted the side I had encoded.
3. **"Decisive" was first measured where the ambiguity sits, not at the row's result.** Measured at the row, 13 of the 26 labels changed nothing, and the partial-materialization reading changes no row in any scenario.

A further problem: the old tier A ("without these, Q1 can't be put to the sources") rested on Q1 asking about an *incident*. I had also listed that as a defect of Q1 (D-q1-type). Under the ex-ante form of Q1, those terms are not needed to pose it.

### What the computation does show (computed at the row, after the repair)

| What | Rows whose result it changes | Where |
|---|---|---|
| R-fgf-severe: the FGF's "severe harm" in its own sense, or the PF's | the FGF severe-harm row | every scenario |
| R-pooling: are deaths and serious injuries pooled toward ">50 people"? | 4 (the catastrophic-risk rows: SB 53 ×2, RAISE, xAI) | `v-mixed-casualties` only |
| R-single-incident-attachment: does "a single incident involving a frontier model doing …" govern the casualties too? | 4 (the same rows) | `v-several-incidents` only |
| Closure: the FCF's and FGF's own sentences read as open (as written) or closed | 2 (the companies' own-sentence rows) | all three variants; never the umbrella rows, which the EU member keeps open |
| R-materialization-partial | 0. It decides limb (2)'s clause in `v-40-deaths`, but limbs (1), (3) and (4) keep the row open | — |
| Every other encoded ambiguity | 0 | — |

Recorded but not evaluable, so absent by construction:
- R-material, R-control and R-findings-cr, which have candidates but no encoding;
- R-foreseeable, R-materially-contribute and R-fcf-rsp-catastrophic, which are delegated.

`tools/answer.py` prints this list, so the blind spot shows wherever the tables do.

These are results about *our frames*, which carry my readings. A second translator could move them.

### What that means for refinement passes

The slice gives a list, not a ranking. Each group comes with its evidence and its limit.

- **Needed to state definitions faithfully, whatever the question.** Each of these either changes a row in some scenario (computed) or changes what drift detects:
  - bar closure ("means" vs "includes");
  - the counting unit and what it attaches to;
  - aggregation;
  - harm kinds (fatalities against death or serious injury);
  - the causal bearer;
  - source-declared umbrellas.

  None is in the plan's §3.8 component list as an attribute.
- **Needed only if questions ask about incidents.** These are the relations between occurrences and risks, of which SB 53 alone has two:
  - materialization, which realizes a risk (limb (2));
  - a demonstrated increase in a risk (limb (4), `thin:risk-increase-evidenced`, which the first frames dropped);

  plus statuses conferred on events. The slice has several of these: SB 53's critical safety incident, the FCF's AI Event → AI Incident → Serious AI Incident / Critical Safety Incident ladder, and the FGF's graded AI safety incident.

  Whether these come first depends on whether Joseph keeps incident-shaped questions. That is decision 12, not something this pass can settle.
- **SB 53's precise clauses: untested by this slice.** Q1 can name them but not weigh them. To weigh them, a question needs facts they test:
  - a documented instance (Q17–Q19, or AISI's INC-2026-07-28-01, as the verifier suggests); or
  - scenarios that supply distinguishing facts, with R-material's and R-control's candidates encoded.

  That is a different pass, not a tier.

### Plan machinery Q1 did not touch

The answer used no SKOS predicate, no SSSOM justification field, no Hohfeld position, no Institutional Grammar statement, no ASPIC+ attack, no FactBank polarity and no Searle strength. Of the assertion records it used `act`, `content` and nested `voice` (the FCF's report about the RSP, now checked against the RSP). That is a fact about Q1, which is mostly about definitions, not a verdict on that machinery.

## 2. Record fields

| Record | Fields the answer used | Fields added because the answer needed them | Not used by Q1 |
|---|---|---|---|
| passage | doc, page, quote, **line range**, match count, version as read | per-document text normalization; a table-cell selector | — |
| translation row | source term, scope, binding kind, frame | — | SKOS predicate: the only row with one, T-xai25-cr's `exactMatch`, points at another source's row, not at a term of ours; confidence |
| **definition frame** (new) | concept, closure, applies_to, in-force dates (with "end undetermined"), slots (words, slot term, resolution, test) | inheritance with overrides; frame substitution; a genus marker for open classes, so closure can be probed | — |
| resolution | outcome, candidates with evidence, what decides | status; whose preference; our preference beside the candidates, with its confidence; read-as-of vs evaluated-at; whether the candidates are encoded; a correction note | intended cardinality (always {0,N} here) |
| assertion | act (point and kind), content, voice | — | strength, factuality polarity, attacks |
| lineage | relation, acknowledged, judgment | **carries** (which claim); drift computed from frames; `not_independent_of`; a template node of unknown authorship; edges from documents not translated | — |
| scenario (new) | stipulated facts, open by default | open- or closed-world reading | — |

## 3. Defects

Each entry gives what happened, the evidence, and the change I'd suggest. The changes are collected in `proposed-changes.md`.

### In the question

#### D-q1-type
**What happened.** Q1 asks which sources would call an *incident* catastrophic, severe or systemic. None of the slice does in those words: they apply to risks (SB 53, RAISE, xAI, FCF, FGF, the AI Act) or to harm ("severe", in the FGF and PF). The slice does label incidents in other words, though:
- SB 53's "critical safety incident";
- the FCF's AI Event → AI Incident → Serious AI Incident / Critical Safety Incident ladder;
- the FGF's "AI safety incident", graded by severity in an unpublished plan.

*Corrected:* an earlier version said none of the slice classifies incidents at all (de-novo-feedback-1 §4).

**What I'd change.** Split Q1 into an ex-ante form (is a risk of this outcome X?) and an ex-post form (what label does the source give the incident?). The second lands on conferred event statuses (`thin:event-status.conferred`), of which the slice has several.

#### D-q1-world
**What happened.** Q1 says "60 deaths" and nothing about injuries or damage. Open world, OpenAI's PF "severe harm" stays *open*, since 60 deaths plus some unknown number of grave injuries could still reach "thousands". Closed world, it is *no*.

**What I'd change.** Every competency question about an event should say whether unstated harms are zero. A scenario or instance record needs that flag.

#### D-q1-date
**What happened.** Q1 has no date, and the answer changes with one:
- xAI's bar is in its 2025-12-30 framework and not in its 2026-06-30 one; whether the later one replaces the earlier is undetermined;
- the FCF v2 starts 2026-07-24;
- RAISE starts 2027-01-01.

**What I'd change.** Competency questions take an as-of date, or ask "over time".

#### D-q1-source-words
**What happened.** Q1 names source words, so it is semasiological (plan §3.1): it asks which source terms apply, not which of our concepts. That is legitimate, but the answer is then about resolution, and "severe" is a harm word where "catastrophic" and "systemic" are risk words.

**What I'd change.** Say which direction a question runs. Or pair Q1 with an onomasiological twin in our terms: "which sources' definitions reach a risk of >50 deaths from one occurrence".

#### D-q1-discrimination
**What happened.** 60 deaths in one incident clears every casualty bar in the lineage and falls below the PF's and the xAI RMF's. So the only interpretive question it forces is R-fgf-severe. Each of the following changes at least one row's result (computed at the row):
- 30 deaths with 30 serious injuries: R-pooling, 4 rows; closure, 2;
- 40 deaths: closure, 2 rows;
- 60 deaths across several incidents: R-single-incident-attachment, 4 rows; closure, 2.

None of them makes SB 53's precise clauses decide anything, for the same reason as Q1: they stipulate no fact those clauses test. A question built on a documented instance would.

An equity loss of $2B (not computed) would split SB 53, which excludes equity value (P-sb53-bp-equity), from the FCF's undefined "financial damages".

**What I'd change.** If Q1 is kept, take a variant like these as its test case.

### In the lexicon and risk side (G3)

#### D-materialization
**What happened.** The plan has no relation between an occurrence and a risk. SB 53's one incident definition has two:
- limb (2), "materialization", which *realizes* a risk;
- limb (4), "in a manner that demonstrates materially increased catastrophic risk", which is *evidence* of an increased risk.

The first frames dropped limb (4)'s clause (de-novo-feedback-1 §3.1). The plan's instance record links an instance to a *kind of event*, which is neither.

**What I'd change.** Add both relations to §3.8, if the competency questions keep asking about incidents (§1 above). Materialization needs a reading for partial outcomes.

#### D-conferred-events
**What happened.** Conferral is defined only for roles (§3.9). The slice confers statuses on events in several instruments, and in stages: the FCF's internal "AI Event" assessment feeds the statutory "Critical Safety Incident" and the EU's "Serious AI Incident".

**What I'd change.** Extend "X counts as Y in C" to events, and let the instance record carry conferred statuses (internal and statutory) as attributed assertions.

#### D-closure
**What happened.** Nothing in §3.3 or §3.8 says whether a definition's bar is a floor ("means") or an example ("includes", "including but not limited to"). Computed by the closure probe (forcing each open class's unbound genus false): it changes the companies' own-sentence rows in all three variants. It never changes their umbrella rows, which the EU member keeps open.

*Corrected:* the first version called this "computed" when `answer.py` didn't read closure at all (de-novo-feedback-1 §1.3).

**What I'd change.** A closure attribute on every definition frame.

#### D-bearer
**What happened.** "Cause" in §3.8 has no bearer or standard.

**What I'd change.** A causal-contribution slot that names its bearer and its standard ("materially contribute", "from").

#### D-bound-vs-match
**What happened.** Plan §3.3 classes a source term as either *bound* (the source defines it) or a *match* (used undefined). In address theory's terms (`def-match.ud`, `def-binding.ud`) that is two axes:
- **who maintains the name's sense:** the source, an outside institution (California law for "foreseeable"), or nobody (ordinary language);
- **how that sense reaches instances:** almost always by match, because a statutory definition is a test run as of a moment.

"Frontier developer" is a binding *to a match*. §3.3's dangle example (§22757.14 asks whether "frontier model" still "applies to foundation models at the frontier", P-sb53-bp-review) has two readings:
- a **match failing through the world's motion** ("the same criteria, run later, quietly pick out something else", `def-match.ud`);
- a **dangle**, if the binding binds the legislature's intended referent, since `def-binding.ud` covers a referent that "moved without the binding being updated".

The plan's wording, "its test no longer reaches what it was meant to", takes the second. *Corrected:* an earlier version said the plan doesn't say which (de-novo-feedback-1 §6).

**What I'd change.**
- Record the two axes separately.
- Make §3.3 name the reading it takes as one of two.

#### D-collide-scope
**What happened.** Whether one maintainer's two definitions of a word *collide* depends on whether they sit in one scope. Address theory: "two mints of one name in different scopes are simply two bindings". The slice has three cases:
- SB 53 mints "catastrophic risk" in two chapters;
- Anthropic uses it in two senses across the RSP and FCF, and says so (P-fcf-rsp-sense, confirmed by P-rsp34-fn1);
- OpenAI's PF defines "severe harm", and the FGF uses the phrase undefined. That they differ is *our* inference (R-fgf-severe). OpenAI's own note is about "catastrophic risk" (P-fgf-pf-sense). *Corrected:* an earlier version set this beside Anthropic's note as if OpenAI had said it (de-novo-feedback-1 §2.2).

The FGF may even use "severe harm" in two senses *inside one document*: its definition sentence, against two sentences reused verbatim from the PF (R-fgf-severe-reused).

Under any per-document scope rule, none of the cross-document cases is a collision. They are the kind of divergence the model most needs to surface, though, and §3.4's selection rule sets scope granularity per translation.

**What I'd change.** Record publisher-level divergence as its own relation between bindings, so it doesn't depend on a scope decision.

### In the record formats (G1(e))

#### D-row-vs-frame
**What happened.** The plan's translation row (§3.4, SSSOM-shaped, term to term) can't carry a definition. SB 53's "catastrophic risk" translates to a concept narrowed by eight slots, not to a term. No row in this pass mapped to a single term of ours.

**What I'd change, and the decision it hides.** There are two places the precision can live:
- **Frames, in the translation layer** (what this pass did). The source's definition is a frame over our slot vocabulary, and the lexicon holds the slots.
- **Lexicon concepts** (the verifier's alternative). Joseph's lexicon shape ("the union of all the most precise, scoped, bounded, and/or specific definitions", plan §2), with intensional definitions (§3.3), suggests that SB 53's catastrophic risk becomes a precise *lexicon* concept whose delimiting characteristics are these slots. The row then maps one to one.

Both are workable, and the frame's slot structure is needed either way. Which layer holds the precision is Joseph's lexicon-shape decision, not a format detail. *Added after de-novo-feedback-1 §6.*

#### D-frame-inheritance
**What happened.** Three things are almost the same definition, and frames need to express "the same except":
- SB 53's two codes;
- RAISE;
- each lineage descendant.

**What I'd change.** `inherit` plus `override` by slot. Also substitution of referenced frames, since RAISE's incident limb (b) must point at RAISE's catastrophic risk, not SB 53's.

#### D-umbrella-vs-definition
**What happened.** The FCF's and FGF's "systemic" first had to be split into an umbrella frame and a frame for the company's own sentence before drift could be computed.

**What I'd change.** Two frame kinds.

#### D-resolution-status
**What happened.** The plan's resolution record has an outcome but no status. An imported binding that we didn't follow ("foreseeable") would read as zero referents. That is the MIT "Other" mix the plan's §3.3 rules out, inside our own record.

**What I'd change.** A status field (attempted, delegated, not needed), separate from outcome.

#### D-bitemporal
**What happened.** One "as-of" field is not enough. Two moments are in play:
- the moment we read the source (`thin:read-as-of`);
- the moment the source's test applies (`thin:evaluated-at`). Foreseeability is judged as of the developer's conduct, and which framework version governs depends on the incident's date.

**What I'd change.** Two time fields: valid time vs record time, the bitemporal split (from general knowledge; not checked here).

#### D-preference-whose
**What happened.** SB 53 declares its own resolution preference ("liberally construed", P-sb53-liberal). Where I lean to one reading, the lean is ours. Address theory's *preference* (`def-resolution.ud`) makes this inspectable, but the plan's record has only "who resolved it".

**What I'd change.**
- Record the source's declared policy and our preference separately.
- Keep the outcome under the source's policy alone, so an ambiguity stays an ambiguity in the record even where we lean.

#### D-lineage-per-claim
**What happened.** A document-level revision edge (xAI's RMF to its 2025 FAIF) would have made the RMF an ancestor of the >50 bar, which it isn't. The bar came from SB 53.

**What I'd change.** Lineage edges say which claim or slot they carry (`carries`).

#### D-lineage-template
**What happened.** I modelled the FCF and FGF as two independent restatements of SB 53. They share verbatim wording that is in neither SB 53 nor the EU Code (L-fcf-fgf-template; found by the verifier, re-run here with `tools/shared_runs.py`):
- the umbrella sentence;
- the opening of the definition sentence;
- the harmful-manipulation category;
- governance boilerplate.

So their shared drift from SB 53 is plausibly one event counted twice, the error "correlation is not corroboration" exists to prevent. The bar's root count (one) is unchanged.

**What I'd change.** Lineage needs nodes for templates of unknown authorship. Every lineage check should compare descendants with *each other*, not only each with the root.

#### D-drift-needs-frames
**What happened.** Drift can only be computed if both ends are frames. Comparing words is not enough: RAISE's bearer slot has **SB 53's exact words and a different test**, because RAISE defines "person" as nongovernmental. Plan §3.7 lists drift direction (hedge dropped, claim hardened) but not structural drift.

**What I'd change.** Compute drift per slot from frames, comparing the resolved tests, not only the words.

#### D-frame-boundary
**What happened.** Drift first reported the FCF and FGF as having "dropped" SB 53's conduct list. It had moved into their category tables, which the FGF ties to "this FGF definition" (P-fgf-categories-intro). The move came with drift of its own: the FCF opens the list ("such as") and drops murder. A frame drawn at the definition sentence can't see a relocation (de-novo-feedback-1 §3.3).

**What I'd change.** A frame's boundary follows the source's own tie-ins (category tables, "this definition"), and drift reports moved clauses as moved.

#### D-encoding-limits
**What happened.** The evaluator can only show an ambiguity deciding something if it is encoded as one. My first "decisive" labels were measured where the ambiguity sits, not at the row's result. Both inflated what the computation seemed to show (§1).

**What I'd change.**
- Weights are reported at the row.
- An evaluator prints which recorded ambiguities it cannot evaluate.
- "Computed" is used only where the computation could have come out the other way.

#### D-scenario-in-source-terms
**What happened.** To evaluate the frames, I wrote the scenario's facts partly in SB 53's terms (`model_is_frontier`, `developer_is_frontier_developer`). For several sources at once, facts have to be in *our* terms (training compute, the role an actor holds), with each source's definitions becoming tests over them. That is the anticorruption layer, applied to the instance record. It also means the instance record's fields are set by the slot vocabulary the frames use, which ties G1(e) to G3 and G2.

**What I'd change.** Write instance facts in our terms only, and let the slot vocabulary define the instance record's fields.

### In anchors (plan §3.5)

#### D-anchor-duplicates
**What happened.** The plan makes the line number optional. In SB 53 the bar clause matches twice, once in each code (P-sb53-bp-bar), so only the line range tells them apart. Any statute that repeats a definition across chapters will do this.

**What I'd change.** A position selector is required wherever the match count is above one. The plan already proposes recording match counts, and `tools/check.py` does.

#### D-anchor-normalization
**What happened.** Exact-quote matching needed per-document normalization:
- NY bill text prints its own line-number column and hyphenates across lines ("inju- ry");
- the FCF is full of zero-width spaces;
- curly quotes vary throughout.

The normalization rule is part of the anchor. One that rejoins hyphens corrupts a compound split at its own hyphen, and it does: `tools/check.py` turns RAISE's "machine-\nbased" (extraction lines 98–99) into "machinebased". No anchor uses that line.

**What I'd change.** Record the normalization per document.

#### D-anchor-tables
**What happened.** Confirmed live, for cells whose row label wraps into the description column: the FGF's harmful-manipulation and CBRN cells, of which only fragments survive as quotes (P-fgf-manipulation-cell). The loss-of-control cell survives whole and is now anchored whole (P-fgf-loc-cell). *Corrected:* an earlier version said only fragments survive, and had cut that cell short (de-novo-feedback-1 §6).

**What I'd change.** A table-cell selector. I invented one; nothing checks it.

#### D-version-as-read
**What happened.** Several dates are thinly sourced:
- the FGF's date comes from the catalog, not from the text read;
- RAISE's text is "as introduced", and its enactment rests on a secondary source;
- Anthropic's FCF v1, in force at the earliest date computed, has no relata key under the name tried (`anthropic-2025-frontier-compliance-framework`). The catalog lists only v2's key.

**What I'd change.** Every passage record carries a version-as-read that the text itself supports, or says where it came from.

### Plan statements checked along the way

- **§1.3 item 3 (seven concepts in SB 53's definition):** all seven present. The frame needs more slots (eight, plus harm kinds, aggregation and closure), consistent with "at least".
- **§1.3 item 2 (">50 people or $1B recurs in four, under two names"):** true as a count (RAISE and xAI: "catastrophic"; FCF and FGF: "systemic"). "Recurs" hides that two of the four change the bar's structure, through one shared template (L-fcf-fgf-template), not two independent readings.
- **§1.3 item 5 and §3.4 (two definitions; limb (1) differs):** confirmed. §3.4 says SB 53 defines the term in "two of the codes it amends". SB 53 *adds* chapters to those codes (P-sb53-enacting). A wording point only.
- **§3.8 table, SB 53 row ("no probability or expectation involved"):** true only on two of R-material's three readings. On the likelihood-floor reading, "material" is a probability floor.
- **Acceptance test 1 (round trip of SB 53's definition):** in rough form the frame does what the test asks. It ends at two imported bindings and a declared ambiguity with candidates, evidence and what would decide. It does *not* pass the test's rule that a declared ambiguity's candidates be lexicon terms, since there is no lexicon yet.
- **The catalog's SB 53 row:** "recurs verbatim in xAI's 2025 FAIF" is confirmed by script. "NY RAISE copies its catastrophic-risk and critical-safety-incident definitions word for word" holds, apart from numerals and list formatting.
