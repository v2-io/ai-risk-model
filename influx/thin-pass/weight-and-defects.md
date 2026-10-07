# What the answer leaned on, and what broke

*G1b's done-test asks for two things: the terms and record fields the answer depended on, and the defects found in the plan's machinery. This file is that list. It is written for Joseph, to decide where refinement passes go first, and then for the agents doing G2 and G3. Claude (Opus 5.5), 2026-10-07. Disposable.*

**Computed or judged.** Each weight below is marked as one or the other.
- **Computed** means `tools/answer.py` evaluated the frames under every reading of an ambiguity and reported whether the choice changed a result. This was done for Q1 and four nearby scenarios (`records/scenarios.yaml`).
- **Judged** means it is my reading of the answer's structure.

The scenarios beyond Q1 are probes, not proposed questions.

## 1. Terms, ranked for refinement

### A. Form: without these, Q1 can't be put to the sources (judged)

Refine these first. They are all on the risk side (G3), and none is in the plan's §3.8 component list as a defined relation or attribute.

1. **Risk as a possibility, an occurrence, and *materialization* between them** (`thin:risk.possibility`, `thin:occurrence`, `thin:materialization`). Every word Q1 asks about classifies a risk, or a harm, never an incident. SB 53 bridges the two with its own word, "materialization" (P-sb53-bp-csi). The plan has risk components (§3.8) and an instance record (G1(e)) but no relation from an instance to the risk it realizes. Its instance record's "reference class" links an instance to a *kind of event*, which is a different thing. Whether a partial outcome counts as materialization is decisive in `v-40-deaths` (R-materialization-partial).
2. **A status an instrument confers on an event** (`thin:event-status.conferred`). SB 53's "critical safety incident" is the only label in the slice applied to an incident, and the only one with consequences. It is a constitutive rule ("X counts as Y in C") applied to an occurrence. The plan uses conferral for *roles* (§3.9) and not for events. Q1's "would call it" is a question about this kind of institutional classification.
3. **Source-declared umbrellas and source-declared sense notes** (`thin:source-umbrella`, `thin:source-sense-note`).
   - The FCF's and FGF's "systemic" is an umbrella over two other instruments' terms. This is how SB 53's bar comes to be called "systemic".
   - Both companies also say, in passing, that a sibling document uses a word differently (P-fcf-rsp-sense, P-fgf-pf-sense).
   - The plan's umbrellas are ours (§3.3); these are the sources'.
   - The FGF's note is the main evidence for the one ambiguity that decides Q1 (R-fgf-severe, decisive in every scenario).

### B. Settled by Q1, or decisive in a nearby question (computed)

| Term | Q1 | Where it decides |
|---|---|---|
| `thin:magnitude-bar` | settled: 60 > 50 | — |
| `thin:counting-unit` | settled by stipulation | which harms "a single incident" governs: `v-several-incidents` (R-single-incident-attachment) |
| `thin:aggregation` | moot | `v-mixed-casualties`: 30 deaths + 30 serious injuries is >50 only if pooled (R-pooling) |
| `thin:bar-closure` | moot | `v-40-deaths`: SB 53's closed bar says no; the FCF and FGF stay open through an unbound genus. The plan has no slot for "means" vs "includes" |
| `thin:harm.kind` | moot | `v-mixed-casualties` (judged): SB 53 counts serious injuries, the companies' sentences count fatalities |

### C. Conditioning: the answer only needs them named (computed)

These stay open in nearly every row for every scenario (answer.md, "Facts left open"):
- knowledge standard ("foreseeable");
- materiality;
- conduct bearer;
- causal contribution;
- the model-conduct list;
- the three exclusions.

Two of them end at an imported binding (California law: R-foreseeable, R-materially-contribute), and one at a declared ambiguity (R-material). Under acceptance test 1's own rules those endings pass. So for Q1, these terms need **names and slots now, and refinement later**. The exception is if Q1 is rewritten to supply those facts, which would turn them into tier B.

Two caveats:
- **Causal contribution needs a *bearer* field.** It shifts within SB 53's own definition: the developer's conduct in (c)(1), the model in exclusion (c)(2)(C). The FGF takes the model as bearer.
- **Most of these facts are written in SB 53's own words** (`developer_is_frontier_developer`, `model_is_frontier`) rather than ours. See D-scenario-in-source-terms.

### D. Plan machinery Q1 did not touch

The answer used no SKOS predicate, no SSSOM justification field, no Hohfeld position, no Institutional Grammar statement, no ASPIC+ attack, no FactBank polarity and no Searle strength. Of the assertion records it used only `act`, `content` and, once, nested `voice` (the FCF's report about the RSP). That is a fact about Q1, which is mostly about definitions, not a verdict on that machinery. Q3, Q5 and Q7 would exercise it.

## 2. Record fields

| Record | Fields the answer used | Fields added because the answer needed them | Not used by Q1 |
|---|---|---|---|
| passage | doc, page, quote, **line range**, match count, version as read | per-document text normalization; a table-cell selector | — |
| translation row | source term, scope, binding kind, frame | — | SKOS predicate (no row had one target); confidence |
| **definition frame** (new) | concept, closure, applies_to, in-force dates, slots (words, slot term, resolution, test) | inheritance with overrides; frame substitution | — |
| resolution | outcome, candidates with evidence, what decides | status; whose preference; our preference kept beside the candidates; read-as-of vs evaluated-at | intended cardinality (always {0,N} here) |
| assertion | act (point and kind), content, voice once | — | strength, factuality polarity, attacks |
| lineage | relation, acknowledged, judgment | **carries** (which claim); drift computed from frames | — |
| scenario (new) | stipulated facts, open by default | open- or closed-world reading | — |

## 3. Defects

Each entry gives what happened, the evidence, and the change I'd suggest. The changes are collected in `proposed-changes.md`.

### In the question

#### D-q1-type
**What happened.** Q1 asks which sources would call an *incident* catastrophic, severe or systemic. None of the slice does. The words apply to risks (SB 53, RAISE, xAI, FCF, FGF) or to harm ("severe", in the FGF and PF).

**What I'd change.** Split Q1 into an ex-ante form (is a risk of this outcome X?) and an ex-post form (what does the source call the incident?). The second will mostly land on conferred event statuses (`thin:event-status.conferred`).

#### D-q1-world
**What happened.** Q1 says "60 deaths" and nothing about injuries or damage. Open world, OpenAI's PF "severe harm" stays *open*, since 60 deaths plus some unknown number of grave injuries could still reach "thousands". Closed world, it is *no*.

**What I'd change.** Every competency question about an event should say whether unstated harms are zero. A scenario or instance record needs that flag.

#### D-q1-date
**What happened.** Q1 has no date, and the answer changes with one:
- xAI's bar is present from 2025-12-30 and gone from 2026-06-30;
- the FCF v2 starts 2026-07-24;
- RAISE starts 2027-01-01.

**What I'd change.** Competency questions take an as-of date, or ask "over time".

#### D-q1-source-words
**What happened.** Q1 names source words, so it is semasiological (plan §3.1): it asks which source terms apply, not which of our concepts. That is legitimate, but the answer is then about resolution, and "severe" is a harm word where "catastrophic" and "systemic" are risk words.

**What I'd change.** Say which direction a question runs. Or pair Q1 with an onomasiological twin in our terms: "which sources' definitions reach a risk of >50 deaths from one occurrence".

#### D-q1-discrimination
**What happened.** 60 deaths in one incident clears every casualty bar in the lineage and falls below the PF's and the xAI RMF's. So the only interpretive question it forces is R-fgf-severe. Each of the following decides at least one source (computed):
- 30 deaths with 30 serious injuries;
- 40 deaths;
- 60 deaths across several incidents.

An equity loss of $2B (not computed) would split SB 53, which excludes equity value (P-sb53-bp-equity), from the FCF's undefined "financial damages".

**What I'd change.** If Q1 is kept, take a variant like these as its test case.

### In the lexicon and risk side (G3)

#### D-materialization
**What happened.** No relation from an occurrence to the risk it realizes (tier A.1).

**What I'd change.** Add one to §3.8's components. It needs a reading for partial outcomes.

#### D-conferred-events
**What happened.** Conferral is defined only for roles (tier A.2).

**What I'd change.** Extend §3.9's "X counts as Y in C" to events, and let the instance record carry conferred statuses as attributed assertions.

#### D-closure
**What happened.** Nothing in §3.3 or §3.8 says whether a definition's bar is a floor ("means") or an example ("includes", "including but not limited to"). It decides `v-40-deaths`.

**What I'd change.** A closure attribute on every definition frame.

#### D-bearer
**What happened.** "Cause" in §3.8 has no bearer or standard.

**What I'd change.** A causal-contribution slot that names its bearer and its standard ("materially contribute", "from").

#### D-bound-vs-match
**What happened.** Plan §3.3 classes a source term as either *bound* (the source defines it) or a *match* (used undefined). In address theory's terms (`def-match.ud`, `def-binding.ud`) that is two axes:
- **who maintains the name's sense:** the source, an outside institution (California law for "foreseeable"), or nobody (ordinary language);
- **how that sense reaches instances:** almost always by match, because a statutory definition is a test run as of a moment.

"Frontier developer" is a binding *to a match*. The same pull shows in §3.3's dangle example. §22757.14 asks whether "frontier model" still "applies to foundation models at the frontier" (P-sb53-bp-review). That reads as a **match failing through the world's motion** ("the same criteria, run later, quietly pick out something else", `def-match.ud`). It reads as a **dangle** only if the binding is taken to bind the legislature's *intended* referent rather than its test. The plan picks dangle without saying which.

**What I'd change.**
- Record the two axes separately.
- Make §3.3's example say which reading it takes.

#### D-collide-scope
**What happened.** Whether one maintainer's two definitions of a word *collide* depends on whether they sit in one scope. Address theory: "two mints of one name in different scopes are simply two bindings". The slice has three cases:
- SB 53 mints "catastrophic risk" in two chapters;
- Anthropic uses it in two senses across the RSP and FCF;
- OpenAI uses "severe harm" in two senses across the PF and FGF.

Under any per-document scope rule, none of these is a collision. They are the kind of divergence the model most needs to surface, though, and §3.4's selection rule sets scope granularity per translation.

**What I'd change.** Record publisher-level divergence as its own relation between bindings, so it doesn't depend on a scope decision.

### In the record formats (G1(e))

#### D-row-vs-frame
**What happened.** The plan's translation row (§3.4, SSSOM-shaped, term to term) can't carry a definition. SB 53's "catastrophic risk" translates to a concept narrowed by eight slots, not to a term. No row in this pass had a single SKOS target.

**What I'd change.** A definition-frame record, with the row pointing to it.

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

#### D-drift-needs-frames
**What happened.** Drift can only be computed if both ends are frames. Comparing words is not enough: RAISE's bearer slot has **SB 53's exact words and a different test**, because RAISE defines "person" as nongovernmental. Plan §3.7 lists drift direction (hedge dropped, claim hardened) but not structural drift.

**What I'd change.** Compute drift per slot from frames, comparing the resolved tests, not only the words.

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

The normalization rule is part of the anchor, and one that rejoins hyphens would corrupt a compound split at its own hyphen.

**What I'd change.** Record the normalization per document.

#### D-anchor-tables
**What happened.** Confirmed live. The FGF's risk-category table interleaves row labels with cells, so only fragments survive as quotes (P-fgf-manipulation-cell).

**What I'd change.** A table-cell selector. I invented one; nothing checks it.

#### D-version-as-read
**What happened.** Several dates are thinly sourced:
- the FGF's date comes from the catalog, not from the text read;
- RAISE's text is "as introduced", and its enactment rests on a secondary source;
- Anthropic's FCF v1, in force at the earliest date computed, has no relata key under the name tried (`anthropic-2025-frontier-compliance-framework`). The catalog lists only v2's key.

**What I'd change.** Every passage record carries a version-as-read that the text itself supports, or says where it came from.

### Plan statements checked along the way

- **§1.3 item 3 (seven concepts in SB 53's definition):** all seven present. The frame needs more slots (eight, plus harm kinds, aggregation and closure), consistent with "at least".
- **§1.3 item 2 (">50 people or $1B recurs in four, under two names"):** true as a count (RAISE and xAI: "catastrophic"; FCF and FGF: "systemic"). "Recurs" hides that two of the four change the bar's structure (L-fcf-derived, L-fgf-derived).
- **§1.3 item 5 and §3.4 (two definitions; limb (1) differs):** confirmed. §3.4 says SB 53 defines the term in "two of the codes it amends". SB 53 *adds* chapters to those codes (P-sb53-enacting). A wording point only.
- **§3.8 table, SB 53 row ("no probability or expectation involved"):** true only on two of R-material's three readings. On the likelihood-floor reading, "material" is a probability floor.
- **Acceptance test 1 (round trip of SB 53's definition):** in rough form the frame does what the test asks. It ends at two imported bindings and a declared ambiguity with candidates, evidence and what would decide. It does *not* pass the test's rule that a declared ambiguity's candidates be lexicon terms, since there is no lexicon yet.
- **The catalog's SB 53 row:** "recurs verbatim in xAI's 2025 FAIF" is confirmed by script. "NY RAISE copies its catastrophic-risk and critical-safety-incident definitions word for word" holds, apart from numerals and list formatting.
