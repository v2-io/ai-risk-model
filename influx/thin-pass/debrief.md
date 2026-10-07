# Debrief: the G1b thin pass

*To Joseph, for after your plan review; then to whoever takes G2 and G3. Claude (Opus 5.5), 2026-10-07. The coordinator briefed it; you decided it ("I agree with your earlier assessment that we run a thin end-to-end pass early on"). An independent verifier (same model family) audited the first version. This debrief is rewritten after repairing what the audit found (`de-novo-feedback-1.md`, `response-to-de-novo-feedback-1.md`).*

## A correction first

The first version of this debrief said: *"most of SB 53's precise clauses carried no weight; the structure around them did"*. The coordinator passed that to you as the main finding. **It doesn't hold, and I've withdrawn it.**

Three reasons, each checked:
- **Q1 stipulates two facts,** 60 deaths and one incident. A clause that tests anything else ("foreseeable", "material", "materially contribute", the conduct list, the exclusions) could only come out "open".
- **My evaluator could only find an ambiguity decisive if I had encoded it as one,** and I had encoded only the magnitude, aggregation and umbrella side.
- **I measured "decisive" below the row's result.** Measured at the row, half the labels changed nothing.

What the slice actually supports is narrower. **It can't rank lexicon terms for refinement.** For a two-fact hypothetical like Q1, SB 53's precise clauses can be named but not weighed.

## What I did

I took SB 53 and candidate Q1 end to end. I read SB 53 whole. Because the question ends in "through how many independent lineages", I also followed SB 53's ">50 people or $1B" bar into the four documents that carry it, at those passages:
- RAISE S.8828, as introduced;
- xAI's 2025 framework;
- Anthropic's FCF v2;
- OpenAI's FGF.

In the repair I added single passages from Anthropic's RSP v3.4 and the EU AI Act's Art. 3(65).

The records are rough YAML: 65 anchored passages, translation rows and definition frames, 22 resolution records, assertion records and lineage records. A small evaluator computes Q1's answer from them for Q1 (open- and closed-world) and three variants. A checker confirms every quote, page and id against the extractions.

The evaluator is useful only if it is honest about what it can show. It now does three things:
- it reports each ambiguity's effect at the row;
- it probes open classes by reading them as closed;
- it prints the recorded ambiguities it cannot evaluate.

Its test vocabulary is scaffolding for this question, not a proposal for G1(e).

## The answer, in brief (`answer.md`)

- **No document in the slice calls an incident catastrophic, severe or systemic in those words.** They use the words of risks or of harm, and label incidents with other terms:
  - SB 53's "critical safety incident";
  - the FCF's AI Event → AI Incident → Serious AI Incident / Critical Safety Incident ladder;
  - the FGF's severity-graded "AI safety incident".
- **Ex ante,** 60 deaths in one incident clears every casualty bar in the lineage. Whether the risk is catastrophic turns on nine facts Q1 doesn't state, so the answer is a list of conditions.
- **Ex post,** SB 53's critical safety incident is open for Q1. Three of its four limbs have no >50 bar, and one needs no harm, only evidence of "materially increased catastrophic risk".
- **"Systemic"** in the FCF and FGF is an umbrella over SB 53's catastrophic risk and the EU's systemic risk.
  - The companies' own sentences turn SB 53's floor into an open example and drop its exclusions.
  - They share template wording with each other that is in neither SB 53 nor the EU Code.
- **In Q1 itself, one reading changes a result:** whether the FGF's undefined "severe harm" is its own (60 fatalities qualifies) or the PF's (thousands of deaths).
  - The FGF reuses two PF sentences containing the phrase, which is evidence for the PF sense.
  - My lean stays with the FGF's own sentence, at low-moderate confidence.
  - The FGF may be using the phrase in two senses.
- **Lineages: one.** Six definitions in five documents trace to SB 53. SB 53's own upstream was not followed.
- **The answer depends on a date Q1 doesn't give.**

## What it means for your refinement passes

There's no ranking to hand you. What the slice does give is a list, each item with its evidence (`weight-and-defects.md` §1):

- **Needed to state definitions faithfully, whatever the question:**
  - whether a bar is a floor or an example;
  - the counting unit and what it attaches to;
  - how casualties pool;
  - which harms are counted;
  - who must causally contribute;
  - umbrellas the sources declare themselves.

  Each of these changes a computed row in some variant, or changes what lineage drift detects, and none is in §3.8's component list as an attribute.
- **Needed only if questions are about incidents:**
  - two relations between occurrences and risks, both in SB 53 (an incident *realizes* a catastrophic risk; an incident *demonstrates an increase* in one);
  - statuses conferred on events, which the slice has several of, some staged.

  Whether these come early depends on decision 12.
- **SB 53's precise clauses are untested by this slice.** To weigh them, the next pass would need a question that supplies the facts they test. A documented instance is the natural one: Q17–Q19, or AISI's INC-2026-07-28-01.

## Things worth your attention before G4

- **Where a definition's precision lives** (proposed change 2). This pass kept each source's definition as a *frame* over a slot vocabulary in the translation layer. The verifier pointed out that your stated lexicon shape ("the union of all the most precise, scoped, bounded, and/or specific definitions") reads more naturally as making each one a precise *lexicon* concept whose delimiting characteristics are those slots. The slot structure is needed either way. Which layer holds the precision is your call, and I hadn't flagged it as a choice.
- **Lineage has to compare descendants with each other.** I modelled the FCF and FGF as two independent restatements of SB 53. They share a template, so their shared drift is probably one event counted twice. This is the error "correlation is not corroboration" is meant to prevent, made inside a pass that was checking lineage.
- **Instance facts in our terms.** To evaluate the frames, I wrote some facts in SB 53's own words (`model_is_frontier`). For several sources at once they need to be in ours. That ties the instance record's fields to the slot vocabulary G2 and G3 produce (D-scenario-in-source-terms).
- **Address theory in §3.3.** "Bound vs match" is two axes in the theory: who maintains a name's sense, and how the sense reaches instances. The plan's §22757.14 example takes the dangle reading ("what it was meant to"). It could say that this is one of two readings (D-bound-vs-match). You'll judge this better than I can.

## Limits

- **One reader's readings, and one model family's audit.** The verifier is the same family, so where we agree, that is coherence. A different-family translator diffing frames slot by slot is still the real check, on the computed results as much as anything.
- **Not read:**
  - the EU Code's systemic-risk tests;
  - xAI's 2026 "systemic risk";
  - the companies' incident ladders beyond their headings;
  - Anthropic's FCF v1, which has no relata key I could find.
- **Partially sourced:** RAISE was read as introduced; its signing date is the catalog's, from a secondary source.
- **Conflict of interest.** Anthropic's FCF is in the slice, and the one ambiguity that decides Q1 landed on OpenAI. The verifier ran the parallel check on Anthropic (the RSP's footnote; any binding of "large-scale harm") and found no parallel ambiguity. That check is now in the records.

## On the brief

The brief gave the why and left the how open, which made it easy to keep Q1 when it fit badly. In hindsight, Q1 was a good test of the *formats* and a poor test of *term weight*, and I should have seen the second before writing a ranking. For a weight-finding pass, a question built on a documented instance would do what this one couldn't. For G4's full-strength pass, Q4 or Q20 would cover the actor vocabulary you named as your priority, which Q1 never touches.
