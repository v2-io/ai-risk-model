# Feedback on the gamma plan, and on the first `def/` drafts

*Written 2026-10-07 by Grok, as a de novo reading of `MODEL-GAMMA-METHODOLOGY-AND-PLAN.md` against the artifacts it cites, plus the `def/` files that were in the tree while this was written. Gamma is a proposal. This is an audit of that proposal and of those drafts, not of an implementation.*

*I did not read `influx/reviews/gamma-de-novo-review.md` in order to form these findings. A search for the address-theory commit printed three lines of that review; I did not use them.*

## What was read, and what was counted

Read whole: the plan; `CLAUDE.md`; `source-catalog.md`; `alignment-model/alignment.md`; `influx/competency-questions-draft.md`; `influx/model-beta/README.md`; the six `def/def-ddd-*.ud` files and `def/README.md`; the alignment-referents spike's `03-structure.md` §§4–8, `04-actors.md` §§5–6, `debrief.md` (opening), and `proposed-integration-plan.md` (opening).

Read in part: `influx/source-models/OVERVIEW.md` through §1.4, its §2.0–2.2 correction sites, and the PHIA note in the appendix; `influx/model-beta/terms/def-risk.ud` (opening) and `def-actors.ud` (the developer/lab discussion); `influx/model-beta/notes-mp.md` item 8; the Evans booklet at `ref/DDD_Reference_2015-03/DDD_Reference_2015-03.md`, at the definitions and the context-mapping pages the drafts quote.

Counted, by script, in `influx/model-beta/`:

| The plan says | What the files contain |
|---|---|
| 287 concepts | 287 concept ids. Fifteen of them are `kind: group` (the taxonomy spine). The other 272 are the leaf records. |
| 573 relations | 573 relation ids, all unique |
| 943 claims | 943 `author:` fields in the six `relations*.yaml` files. I did not check that every such field is a claim and that no claim lacks one. The number matches. |
| 72 terms in 14 groups | 14 files, and 74 `\|term[` entries |
| broad/narrow: 46 and 70 rows in `mappings*.yaml` | `rel: broad` 46, `rel: narrow` 70 |
| about 31 and 28 in `terms/*.ud` | not re-counted as table rows. A line count that excludes the legend sentence is in the same neighbourhood. |
| about forty concepts where "developer" came to mean "a lab" | `def-actors.ud` says the *rename* "touches about 40 concept labels." I count 23 labels containing "developer", and 41 concept records whose label or definition does. |

The address-theory pin (`90f4fb6`, 2026-08-27) resolves on `github.com/v2-io/udon`. The tree at that commit has the seven `v2/references/def/*.ud` files the plan names. Local `~/src/arch/firmatum/udon` is at `4fbe741`, which contains that commit, and `v2/references/def/` is identical between the pin and that HEAD. The pin is not stale as of this check.

## Findings

### 1. Section 3.9 still asserts, in the present tense, the state its own note says has passed

The note at the start of §3.9 says the section was written mid-spike, and that the spike has since been verified and repaired. The paragraphs under the note were not brought into line with it.

They still say the sweep is "a mid-spike report, not yet verified," and that a spike "is looking at" the alignment referent. They still teach two bases of division (lifecycle/market, and what writes into an agent) and five term groups built on that pair. The note, and the spike, say something else: the bases connect by conferral rather than competing (`04-actors.md` §5); "to whom" is eight relations, of which the map's lines are only "writes into" (`03-structure.md` §6.1); the actor table the spike proposes is parties × relations.

G2 says to draft "the groups in section 3.9." As the section stands, that phrase points at the five groups in the body. The note's shape (parties × relations, and a separate agent to integrate `proposed-integration-plan.md`) is a lean beside the text, not the text G2 names. An agent that follows G2 literally will build the structure the note says has been superseded.

The done-test at the end of §3.9 is unaffected by this. It names passages, not the two-basis table.

### 2. Decision 10's recommendation is the spike's. The warrant in the plan is flatter than the spike's.

The spike's debrief: don't give alignment a single default referent, because each of seven defaults makes some named risk come out aligned. "Three of those depend on stated conditions, and one rests on a risk named only outside the corpus."

The conditions are in `03-structure.md` §4. The developer row holds when "developer" means the controlling authority acting through the institution, and not under a legitimacy-qualified reading. The society row holds when the aspect is society's interest and the model's belief is correct, which the scenario leaves open. The law row takes the executive order's claim as the named risk. The operator row is marked "Named outside the corpus" (the Anthropic constitution).

Decision 10's list states each of these as a clean case: "developer: a head of state directing military AI through the institution," and so on, with no conditions and no outside-the-corpus mark. The recommendation that follows (no single default; a relation with named slots; a declared admissible set; the agent-membership question left for Joseph) matches `03-structure.md` §8, including the slot list and the five use types. The list of seven defeats, as written in the plan, is stronger than the spike was willing to say.

The plan is right, in the same note, that this is one model family's work.

### 3. The phase list and the lean at G4 are two different orders

The phase text puts the thin end-to-end pass inside G4, after G2 and G3, and says G2 can run beside G1(d)–(e). The note inside G4 says to run that pass *before* G2 and G3, on SB 53, with disposable formats kept outside `def/`. It is marked as a lean, confidence moderate. It does not say it replaces the phase list.

Both are instructions an implementer can follow. They prescribe different sequences, and different moments at which lexicon entries start to carry weight. Section 2 says downstream work does not lean on an entry before the refinement passes. The lean is an attempt to honour that. The phase list spends G2 and G3 before the pass that would show which entries a question actually uses. Until one of them is withdrawn, "implement the plan" does not pick a sequence.

### 4. G3 cannot meet its own done-test until G5 has finished, and G5 is specified as parallel with G3

G3 is done "when acceptance tests 1, 2 and 5 pass for the risk-side terms." Test 5 is: every basis of division in the distinctions inventory can be expressed in the lexicon. That inventory is G5's output. G5 is "in parallel with G2–G4" and "feeds G3."

So either G3 waits on G5, in which case it is not parallel and not prior, or "for the risk-side terms" silently narrows test 5 to the risk-side distinctions, in which case the corpus-wide test has no phase whose done-condition it is. Acceptance test 2 has a similar shape (every sense in OVERVIEW §2), and that one G3 can meet without G5, because OVERVIEW already exists.

### 5. "One translation per source" is several units, and G6's counts describe the catalog rows rather than the work remaining

I count 11 rows marked anchor and 26 marked major in `source-catalog.md`. That part of the sentence is right.

The same sentence calls them "the remaining translations." Four of them are the G4 pilots: SB 53, the EU Code, and IASR 2026 are anchors; Anthropic's August 2026 Risk Report is a major row (and that row also contains the February report). Read one way, G6 translates those four again. Read the other way, "remaining" drops them and the numbers 11 and 26 are the full catalog rather than the remainder. The sentence doesn't decide.

A catalog row is also not yet a translation unit. Several rows bundle more than one document (the RSP series, IASR 2026 full and extended summary, the AI Act and the Digital Omnibus). G4's pilots are single documents cut out of those rows.

The documents the plan's own lineage findings depend on are, in the catalog's words, "not listed": Microsoft, Amazon, xAI, Shanghai AI Lab, and the other frameworks, which "enter this catalog through METR-CE and `influx/source-models/frontier-safety-frameworks.md`." Finding 2 is about those copies (the loss-of-control formula in nine later documents; the California threshold in four; Shanghai's glossary "primarily based on" IASR 2025). G6, followed literally, never assigns them a translation. The "eleven models" slice in G4 uses OVERVIEW's eleven rows, where those companies are one row, FSF. Nothing says whether that slice records each copy or one bundled model. The method's reason for existing is that those are not the same thing.

NRR and CRA are two of the eleven. OVERVIEW §1.4 says the UK national model contains no loss of control. A slice "through all eleven" needs an explicit empty outcome for those two, or it will be read as a gap in the slice.

### 6. The five kinds of model are OVERVIEW's. The membership in the plan's list is a paraphrase, and it mis-files the Anthropic pilot.

OVERVIEW §1.4:

- landscape: IASR, MIT, CAIS, CRA;
- gate: FSF, OpenAI, Anthropic v2.2, and the EU Code's acceptance loop;
- process: NIST, and the EU Code's process layer;
- scenario: the NRR;
- measurement: AISI Trends, *Loss of Oversight*, and NIST 800-2.

The next paragraph says Anthropic's v3 Risk Reports are a hybrid, "a landscape for one company, graded in words," defined against safety cases, which are gate-shaped.

The plan (§1.3, finding 1) says "in OVERVIEW's words" and then lists "a developer's go/no-go gate (the company frameworks)" and "a measurement programme (UK AISI)." That files every company framework as a gate, including the August 2026 Risk Report, which is one of the four pilots, and which is the document OVERVIEW has just set outside the gate list. It also drops NIST 800-2 from measurement, and it mentions the EU Code only as a process model, not also as a gate. Finding 1 says a translation has to carry which kind of model a claim came from. The list a translator would carry it in currently sorts the pilot into the kind OVERVIEW says it left.

### 7. Calling the address-theory import a shared kernel fails the delimiting characteristics the new entry gives that term. The same drafts classify RAISE's copying twice.

The plan (§3.2): import the terms by reference, pinned to `90f4fb6`, and call that a shared kernel because Joseph maintains both sides.

`def-ddd-relationships.ud` defines a shared kernel as a subset two teams agree to share, explicitly bounded, changed only in consultation, including the code or data design that implements it. One team adopting another's terms without agreement is, by that entry's invariant, not a shared kernel. The discussion then gives the import as the example of a shared kernel.

What the plan actually specifies is a citation of one repository at one commit. This repository does not hold the subset, and there is no second team whose consultation a change waits on. The pin is a snapshot (and, as checked above, a currently accurate one). Evans's published language, which `def-ddd-translation.ud` defines as a documented medium that is not either side's own model, is also a poor fit: address theory is one side's model. The accurate description is the one G1(b) already uses beside the classification: imported by reference, cited at a commit. The shared-kernel label adds a maintenance relationship the pin does not create. When udon's `def/` does change, the pin will be a dangling citation in the plan's own vocabulary, and nothing in G1 says who moves it.

The two drafts also split on the RAISE Act. `def-ddd-relationships.ud` lists "New York's RAISE Act copying SB 53's definitions word for word" as a conformist relationship, and defines conformist as a kind of upstream-downstream. `def-ddd-context-map.ud` uses the same pair as the example of what upstream-downstream is *not*: a copied definition is lineage, "not this relation." The plan lists the same example as conformist in §3.2 and treats copying as lineage in §3.7. Both records can be kept, if a copying is allowed to be a lineage fact and a context-map relationship at once. Neither the plan nor the drafts say that, and as written the two entries exclude each other.

### 8. The failure mode named for loose sources and the test named as its guard are different tests

Section 6 says the round-trip favours statutes and rigorous company documents, and that loose sources test something else: whether declared ambiguity stays honest rather than becoming a dumping ground. It names the MIT "Other" test as the guard.

That test (acceptance test 3, §3.3) says a category must not merge a thing in the world with a fact about our reading. A term whose only content is "ambiguous among these candidates," used whenever a loose source is hard, passes that test. It is the dumping ground the paragraph is worried about. Acceptance test 1's three round trips are SB 53, AI Act "systemic risk," and Anthropic's "misalignment risk." IASR is a pilot and is not in that test. The risk is correctly named. The test that would catch it is a round trip through a source the plan itself calls loose, with a stated limit on how a declared ambiguity is allowed to close.

## The `def/` drafts

Six files, all `:status proposed`, plus a README. They cover the DDD vocabulary G1(a) asks for, and they add `deep-model`, `refactoring-toward-deeper-insight`, `open-host-service`, and the three dependence terms (`upstream-downstream`, `mutually-dependent`, `free`), which are Evans's and which G1(a)'s "relationship patterns" can be read to include.

G1(a) says "DDD terms verbatim." The README and the `:source` lines do something more careful, and they should win: a definition is either verbatim or marked `[SOURCE: …, modified — what changed]`, and a line that is this project's ends with "— our reading." The sentences I compared to the local Evans copy match, including:

- domain, model, ubiquitous language, context, and bounded context, against the definitions section;
- upstream-downstream, mutually dependent, and free, against the context-mapping section, with the parentheticals removed where the `:source` line says they are;
- the big-ball sentence "multiple conceptual systems and mix together," which is ungrammatical in Evans's text and is quoted that way.

I did not repeat the README's claim of a mechanical check of every quotation. The ones above are the ones I looked at.

These are the places a refinement pass has something to decide, rather than something to repair:

- **Widenings, already marked as ours, already written as part of the entry.** Conformist is widened so that adoption without translation counts even when Evans's occasion (an unmotivated upstream) is absent; legal compatibility is the example. Bounded context is given nesting by defining it through address theory's scope, which the entry says Evans's text does not provide. The anticorruption layer is narrowed to one direction and widened from "functionality" to "claims and meanings." Each is labeled. Each is also the kind of line a later agent will inherit as the term, because it sits in the entry rather than in a proposal beside it. That is the failure mode §6 names ("first-pass entries can look finished"), and the README's "`proposed` carries no weight yet" is the guard the plan asked for. The guard works if the next reader believes the status line more than the prose.
- **A collision the plan's namespace table does not list.** `def-ddd-domain-model.ud` notes that `CLAUDE.md`'s "Model" row, "an ontology plus claims about how things behave," is narrower than Evans's model. The §3.2 table has AI model, source model, and "model gamma," and not this one.
- **The example table says the plan "judged" model beta "was not a deep one."** The plan calls beta a ball of mud and a conformist adoption of IASR's definitions. It does not use Evans's "deep model."
- **`def-ddd-translation.ud` is Evans's layer (anticorruption, open host, published language).** Decision 1, still open, is whether the per-source document is called a translation. The filename is easy to read as that decision having been made.
- **The shared-kernel example and the RAISE split** are finding 7.

`def-ddd-big-ball-of-mud.ud` keeps the distinction the plan draws: the condition can describe beta and the self-inconsistent sources; Evans's prescription (draw one boundary and stop modeling inside) is the wrong response to those sources. `def-ddd-relationships.ud` refuses separate ways for a deliberately unbound term inside a connected document. Both of those are the plan, carried accurately. The Foote and Yoder paper is marked "from memory, not re-read."

## What held

Recorded so the findings above are the residue of the check, not the whole of it.

- The loop figures match `notes-mp.md` item 8: 641,083 before one edge was recast, about 186,000 simple cycles with all five shards after.
- `def-risk.ud` does say "The first four definitions are IASR 2026's, adopted."
- The broad/narrow legend in `def-actors.ud` is "broad (theirs is wider)," the opposite of SKOS with the source term as subject. The mapping-file counts are 46 and 70.
- OVERVIEW now contains the corrections §7 says were applied: Guide 51 rather than ISO 31000 for the probability × severity form, with the NIST attribution left ambiguous (item 1 and 2); an eighth hazard sense, root cause (item 3); the NRR's "Highly unlikely (5–25%)" against the yardstick's ≈10–20% (item 6).
- The agent-part glosses and the actor list in §3.9 match `alignment.md`, including empty edges for Control & Eval and the two referent rows with no channel in. "Control & eval" having no lines is what the map shows. The spike's finding that some evaluators also write is additional, and the plan's item 3 records it.
- The competency-question draft has thirteen axes (A–M) and twenty questions. The eight named in decision 12 touch A, B, C, D, E, G, H, I, J, K, L, and M. F is absent. K appears only on question 12. That is what the plan says.
- The alignment slot list and the five use types in decision 10 match the spike's §8 and §5.

## What this pass did not check

The three research reports' quotations from outside this repository: ISO 704 and 860 and 1087, Searle, FactBank, Goffman, ASPIC+, SACM, Institutional Grammar, Hohfeld, von Wright, LegalRuleML, the SRA glossary sentence, Kaplan & Garrick, the STPA Handbook page 133, the CAA bow-tie steps, MIT's Table 1 and the 21% figure, SB 53's sentence and the seven-way split, the IASR lines (1688, 2077, and the glossary). The plan says which of those its author checked and which rest on a report's verification mark. I took that attribution as the plan's claim about its own evidence, and I did not re-open those primaries. Grüninger & Fox 1995 is already marked unchecked in §3.11.

A count of `author:` fields is not a schema audit. Whether beta's terms were written before any source was mapped is a chronology claim; I did not reconstruct it from git. The mappings exist and are large, and `def-risk.ud`'s IASR adoption is in the file either way.
