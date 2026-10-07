# Debrief: the G1b thin pass

*To Joseph, for after your plan review; then to whoever takes G2 and G3. Claude (Opus 5.5), 2026-10-07. The coordinator briefed it; you decided it ("I agree with your earlier assessment that we run a thin end-to-end pass early on"). One agent, one session, unreviewed. An independent verifier is to follow.*

## What I did

I took SB 53 and candidate Q1 end to end. I read SB 53 whole. Because the question ends in "through how many independent lineages", I also followed SB 53's ">50 people or $1B" bar into the four documents that carry it, at those passages only: RAISE S.8828, xAI's 2025 framework, Anthropic's FCF v2 and OpenAI's FGF.

I recorded everything as rough YAML records:
- 53 anchored passages;
- translation rows and definition frames;
- 19 resolution records;
- assertion records;
- lineage records.

I also wrote a small evaluator that computes Q1's answer from them, for Q1 and for four nearby scenarios. A script checks every quote, page and id against the extractions.

The evaluator is the one thing I added beyond the brief, and I should say why. G1b's done-test asks which terms the answer *depended on*. I didn't want that list to be my impression. Running each ambiguity's readings through the frames turned "this term matters" into a checkable claim: choosing between its readings changes this result, in this scenario, or it doesn't. The cost is that the evaluator's test vocabulary looks more finished than it is. That is the hardening risk the plan worries about (§6), applied to formats. Please treat it as scaffolding for this question, not a proposal for G1(e).

## What came out

**The answer** (`answer.md`).
- No document in the slice calls an *incident* catastrophic, severe or systemic. They apply those words to risks or to harm, and SB 53 reaches the incident itself only through "Harm resulting from the materialization of a catastrophic risk".
- **Ex ante,** 60 deaths in one incident clears SB 53's bar under every reading. The rest is open: model conduct, causal contribution, foreseeability, materiality, exclusions. For Q1 the answer is a list of conditions, which is what "under what conditions" anticipated.
- **Ex post,** SB 53 calls such an incident a *critical safety incident*. Two of that term's four limbs need no casualty bar at all.
- **"Systemic"** is the FCF's and FGF's umbrella over SB 53's term. In their own sentences the >50 bar becomes an open example rather than a floor.
- **"Severe"** splits OpenAI's two documents by two orders of magnitude. That is the one ambiguity that changes Q1's answer.
- **Lineages:** one, with SB 53's own upstream not followed.

**Where the coordinator's guess landed.** The guess was that SB 53 would translate easily clause by clause, force several risk-side terms into existence early, and that the record formats would hold the surprises. All three held, with corrections.
- **Translation.** It was easy clause by clause. But a clause-by-clause translation doesn't fit the plan's term-to-term row at all. It needed a new record kind, the definition frame.
- **Risk-side terms.** The ones it forced were not mainly the components in §3.8, which turned up as slots and were mostly conditioning. They were the *relations and statuses around* the components:
  - materialization, from a risk to an occurrence;
  - a status an instrument confers on an event;
  - whether a bar is a floor or an example;
  - umbrellas that sources declare over other instruments' terms.
- **Surprises.** The formats held many, but the largest defect was in the question. Q1 asks about an object none of these sources classify, gives no date, and doesn't say whether unstated harms are zero.

## What I think it means for your refinement passes

This is the result I'd most want you to weigh, and it is a judgment built on computed evidence.

**Most of SB 53's precise clauses carried no weight for Q1.** "Foreseeable", "material", "materially contribute", the three conduct classes and the three exclusions all stayed *open conditions* in every scenario. Two end at California law and one at a declared ambiguity, which acceptance test 1 already counts as passing. The answer needed them named and slotted, not refined.

**What carried the weight was the structure around them.** For the lexicon:
- the possibility / occurrence / materialization triangle;
- conferred event statuses;
- bar closure;
- the counting unit and aggregation;
- source-declared umbrellas.

For the formats:
- frames;
- separate status and two times in resolution records;
- lineage per claim, with drift computed from frames.

`weight-and-defects.md` §1 ranks these. If your passes have to go somewhere first on the risk side, I'd put them on tier A there, ahead of the components list.

Two caveats on that inference:
- **It comes from one question.** Q1 is about definitions. A norm-shaped question (Q3, Q5) would put weight on the Hohfeld and Institutional Grammar machinery that Q1 never touched, and Q4 would put it on G2's actor terms.
- **The weights are computed from my frames,** so they inherit my readings. The places a second translator should look first:
  - what "arising from a single incident" attaches to;
  - "includes" read as a sufficient example;
  - my lean on the FGF's "severe harm".

## Things worth your attention before G4

- **Write instance facts in our terms.** To evaluate the frames I wrote the scenario's facts partly in SB 53's words (`model_is_frontier`). For several sources at once they need to be in ours, with each source's definitions as tests over them. That makes the instance record's fields depend on the slot vocabulary G2 and G3 produce, a dependency the plan doesn't yet show (D-scenario-in-source-terms).
- **Address theory's "bound vs match"** is used in §3.3 as one axis where the theory has two. Its §22757.14 example reads at least as naturally as a match drifting with the world as it does as a dangle (D-bound-vs-match). You'll judge that better than I can. It's your theory, and I read it once today.
- **Publisher-level divergence.** Both Anthropic and OpenAI note, inside their compliance frameworks, that a sibling document uses the same word differently. Under address theory's scope rule these aren't collisions, but they are among the most important divergences in the slice (D-collide-scope).

## Limits

- **One reader, one model family.** Every reading here is mine. No second translator, no different-family check. The plan's §6 concern about same-model coherence applies in full.
- **Not read:** the EU AI Act's systemic risk, which is a member of both companies' umbrellas and so keeps their rows open in every scenario; Anthropic's RSP (only reported, by the FCF); OpenAI's PF beyond one footnote; Anthropic's FCF v1, which was in force at the earliest date computed and has no relata key I could find.
- **RAISE was read as introduced.** Its signing date is the catalog's, from a secondary source.
- **Conflict of interest.** Anthropic's FCF is in the slice. I read its open bar ("includes … including but not limited to") the same way as OpenAI's, and the drift between it and SB 53 was computed by the same diff as everything else. A different-family reader would still be the real check.

## On the brief, and what I'd do next

The brief gave me the why, with your words, and left the how open. That made it easy to keep Q1 when it fit badly, because a bad fit was a finding. One suggestion for G4's full-strength end-to-end pass: use Q4 or Q20. Together with this pass that covers both halves of the vocabulary, the definitional risk side here and the actor side there.

If useful, the cheapest next step is to rerun this same slice with a translator from a different model family and diff their frames against mine. The disagreement per slot is exactly G4's measure of where the lexicon is underspecified.
