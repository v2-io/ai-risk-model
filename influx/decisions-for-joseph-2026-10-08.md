# Decisions for Joseph, gathered (2026-10-08)

*Claude (Opus 5.5), for Joseph. Every open decision in `MODEL-GAMMA-METHODOLOGY-AND-PLAN.md`, with my lean and confidence, in one place. The reasoning stays in the plan, at the section given. Ordered by how much work each one unblocks. Answer on the "Joseph:" line in whatever words are quickest; a bare "yes" means take the lean.*

---

## A. Decide first: these unblock the most

**A1. Which competency questions to start with** (§5 decision 12; §3.11)
Lean: these eight from `influx/competency-questions-draft.md`: 4, 20, 1, 3, 2, 12, 17, 7. Together they touch 12 of the 13 axes. *Moderate.*
Unblocks: refinement passes on G2/G3 entries, and which machinery earns a place. If any incident-shaped question is kept (20, 2, 12, 17), the thin pass's proposed change 1 (how occurrences relate to risks; event statuses conferred by instruments) is needed early.
Joseph:

**A2. Where a source's precise definition lives** (§3.2 note; thin pass `proposed-changes.md` item 2, `notation/notes.md` §5)
Lean: Option C. Each source's precise terms become entries in a *hosted* namespace per document or scope (`sb53.bp:`, `oai-fgf:`, `oai-pf:`), copied verbatim with attribution. `arm:` holds our descriptive terms. Translation shrinks to resolution records. An `arm:` term never takes a source definition as its own, and an `arm:` umbrella contains only `arm:` terms. *Moderate-high.*
Builds on your 2026-10-07 words ("openai:severe-harm", "arm", "explicitly show ambiguity").
Unblocks: G1(e)'s record formats, A3, B1, and the namespace-kind column in `def/README.md`.
Joseph:

**A3. The name of the per-source document** (§5 decision 1)
Lean: keep Evans's "context map" for the map *across* sources. Under A2, call the per-source parts its *namespace* and its *resolutions*, and keep "translation" for G6's translated edition. *Low.* Decide together with A2.
Joseph:

**A4. Record format: udon now, or YAML through the pilots** (§5 decision 9)
Lean: the lexicon stays in udon. The evidence-plane records stay in YAML only while the pilots churn their formats; then udon, with our needs fed to the udon team. The parser reportedly implements 0.9; the real gap is the missing Ruby/Python bindings. *Moderate.*
Joseph:

**A5. Is the agent itself in the declared set of alignment referents?** (§5 decision 10)
The rest of decision 10 has the spike's recommendation, which I agree with: no default referent, a relation with named slots, and a declared, versioned set of admissible referents. *Moderate-high.*
Lean on the sub-question: include the agent, because the map treats it as a party with interests. The cost stays low, since takeover and power-seeking claims name their harm anyway. *Moderate.*
Joseph:

**A6. A second thin pass (G1c) on AISI's cyber-range incident** (§4, after G1b)
Lean: yes, before G2's entries get refinement passes, carried through question 20 (or 18 or 4). It weighs precise clauses against real facts, and it touches actor vocabulary: the model writes its own hand-off summary. *Moderate-high.*
Joseph:

## B. How the work runs

**B1. Which entries get your full refinement budget** (§2 note)
Lean: `arm:` terms, method terms, and any line marked "our reading". Source-namespace entries get a scripted verbatim check plus two independent slot parses, ideally from different model families. *Moderate-high.* Yours, since the lesson is yours.
Joseph:

**B2. Write no G1(d) entries (speech acts, argument, norms) until a thin pass on a norm-shaped question** (Q3, Q5 or Q11) (§4 G1 note)
Lean: yes. *Moderate-high.*
Joseph:

**B3. G2/G3: drafting may start now; refinement passes wait for A1 and G1c** (§4 G2 note)
Lean: yes. *Moderate-high.*
Joseph:

**B4. Within G2, refine the seven agent parts before the actors** (§3.9 note)
Lean: yes. If the map itself is about to change, the map goes first. *Moderate-high.*
Joseph:

**B5. Have a separate agent integrate the alignment spike into §3.9** (§3.9 note)
Lean: yes, from the spike's `proposed-integration-plan.md` (now corrected on control of the weights). This keeps spiker, verifier and integrator separate. *High.*
Joseph:

**B6. A review from another model family now, before G4** (§6 note)
Lean: yes. Grok's audit was the first. Still without one: the spike, the thin pass and notation, the research reports' quotations, the citation check, and today's revisions. *High.*
Joseph:

## C. Names and senses (can wait until G2/G3 needs them)

**C1. Broad/narrow direction** (decision 2). Lean: SKOS/SSSOM's direction for gamma, with beta's files left as they are. *High.* A quick yes/no.
Joseph:

**C2. "Hazard"** (decision 3). Lean: H1, a source of potential harm, with intent as a separate attribute that carries the NRR's hazard/threat distinction. *Moderate-high.*
Joseph:

**C3. "Risk"** (decision 4). Lean: a declared umbrella with named readings, following the SRA. *High* on the structure; the names are open.
Joseph:

**C4. "Developer"** (decision 5). Lean: dissolve it into functional and institutional roles plus an organization term, and keep "developer" as a declared umbrella over them. *Moderate.*
Joseph:

**C5. Agent-part umbrella and oversight relation** (decision 6). Lean: "component", declared narrower ("the components something writes into"); and "oversees", with the Control & Eval row split into overseer and evaluator. *Low.* These are your model's words.
Joseph:

**C6. STPA** (decision 7). Lean: keep it as one translated source; any terms we take are bound to the Handbook, not to the AI papers' glossaries. *Moderate.*
Joseph:

**C7. Contest standings** (decision 8). Lean: record them only as attributed assertions or computed views, never as our fields. *High.*
Joseph:

**C8. Impact radius** (decision 11). Lean: target × degree × recoverability, where "degree" gets the thin pass's harm facets (what is counted, the operator, the number, the counting unit, pooling). *Moderate.*
Joseph:

**C9. Translated editions** (decision 13). Lean: yes, starting with the pilots, using C10's marks in place. *Moderate.*
Joseph:

**C10. The notation's syntax** (decision 14). Lean: decide which distinctions the notation must carry, then hand that to the udon team as our needs list rather than fitting the current spec. The open points are `{a | b}` against type-union `|`, `?` doing two jobs, `.` doing two jobs, ambiguity on relations and sets, inline any-of/all-of, and inheritance with overrides. *Moderate.*
Joseph:

**C11. The passage anchor** (§3.5 note). Lean: relata key + physical PDF page (from `ref/canonical/`'s markers) + exact quote, with the printed page as a display field only; a passage record can hold several anchors. *Moderate-high.*
Joseph:

## D. Open, without a lean of mine yet

- The thin pass's other proposals (`influx/thin-pass/proposed-changes.md` items 3–7 and 10–13): resolution-record fields, lineage changes, splitting bound/match into two axes, publisher-level divergence, anchor details, instance facts in our terms, and the Q1 rewrites. Each has the thin pass's own reasoning. I haven't weighed them one by one; most land in G1(e), so A2 and A4 come first.
- ~~What "superseded" means for canonicalize.~~ Decided by Joseph, 2026-10-09: `subsumed-by` for a duplicate of the same text, `superseded-by` for an earlier version that is kept but not active. Applied in `source-catalog.md` (commit `4849e10`).

## E. Left over from the catalog update (`influx/catalog-update-proposal-2026-10-08.md`)

**E1. Two candidate rows not added** (proposal §4, B26 and B27; both stay in the catalog's corpus section).
- B26, AISI's labour-market assessment: not added because the repo doesn't use it yet.
- B27, the vocabulary sources (the SRA glossary, ISO terminology standards and others): should the catalog list the lexicon's sources at all, as well as models of risk?
Joseph:

**E2. Bibliography years in relata** (proposal §6, F6). Some relata entries carry a year that won't match the key or the year the work is cited by: Yampolskiy prints as 2015, for example. The fix is an edit in relata, not in this repo, so it wasn't applied. Lean: fix them in relata, then re-run `relata emit bib`. *High.*
Joseph:
