# Risk census model

To Joseph, and to whoever extends this next.

This is a model of the frontier-AI risk landscape, built for Joseph's own understanding. It started on 2026-09-27 as a response to a table-shaped report (`influx/safety-risk-factors.md`) and fourteen verification files (`influx/verification/`). Its job is to hold everything those sources say, **including what they merely assert and what we merely suspect**, in a form where the structure of the risk (what drives what, what dampens what, where the loops are) can be seen and interrogated.

The field reference is in `SCHEMA.md`. This file is the what and the why.

## What it is

> **In transition (2026-09-28).** The model is moving to four layers, agreed with Joseph:
> - **terms:** the things and kinds, defined in udon in `terms/def-*.ud`, each group with a per-term lexical map;
> - **quantities:** the entries below; the only nodes causal claims connect;
> - **causal claims;**
> - **the lexicon.**
>
> The terms are written and still `proposed`. Several decisions are open (see `../HANDOFF-2026-09-27.md`, "Joseph's decisions, 2026-09-28"). The quantities have not yet been sorted against the terms. Until they are, the description below is accurate for the YAML files, but `terms/` is the vocabulary authority. Read it first.

Three layers share one set of concept IDs:

1. **A taxonomy** (`concepts.yaml`). Canonical concepts sit under ten groups. Each concept is a *quantity that can rise or fall* ("strength of safety culture", not "safety culture"), which is what lets a relation carry a sign. The taxonomy is primary, and scannable like a list.
2. **A lexicon** (`mappings.yaml`). Each source's own term is mapped onto our concepts with SKOS-style relations (exact / close / broad / narrow / related). Its main use is to expose **pooling**: one word covering distinct things. The EU Code's "loss of control" maps *broad* onto both bounded and strict loss of control. IASR 2026's maps *close* onto strict only. Apollo says today's unsanctioned agent actions aren't loss of control at all, while CLTR counts them.
3. **Relations** (`relations.yaml`). These are typed links: *influences* (signed), *moderates* (acts on another relation), *indicates* (an observable measure) and *part_of* (definitional). **Each relation is carried by claims**, and each claim records *author*, *channel*, *evidence* and *qualifier*. Relations are optional; a concept with none is still in the census.

Views are derived, never maintained by hand: the causal loop diagram, a bow-tie around any event, the crosswalk of hazards against sources, and the lexicon of pooled terms. `check.py` is the first of these: it validates references, finds loops, and describes each relation's standing.

## Why this shape: decisions made with Joseph

- **Compilation, not adjudication.** Joseph: *"What I wanted was a risk-factors compilation and synthesis — not any kind of adjudication on whether something I have hypothesized is or is not in it. If the factors are put together well, the answer to that question should be pretty easy to see."* His own hypothesis (hypergrowth degrades safety) sits in the model as ordinary concepts and relations, with its provenance marked like anything else's.
- **A causal loop diagram, then a taxonomy with optional relations.** The first design was a pure CLD. Joseph steered it to a taxonomy with optional edges: *"a large taxonomy with optional edges — an RDF graph almost, is still the cleanest way until we have more of it modeled."* The hazard list (CBRN, cyber, bias, privacy …) is better as a taxonomy. Its causal structure is nearly identical from hazard to hazard, and forcing it into subgraphs adds physics without insight. The CLD earns its place where relationships carry the story: organizational dynamics, oversight, cognition, racing.
- **Good and bad live on relations, not concepts.** Joseph: *"It allows things to be both good and bad at the same time, as is common in causal loop modeled systems."* Some examples:
  - personnel vetting reduces insider risk *and* slows research and talent attraction;
  - public listing brings governance structures *and* short-term earnings pressure;
  - cognitive offloading frees capacity *and* erodes skill.

  "Control" and "escalation factor" are roles a relation gives a concept, never properties of the concept.
- **Signs only, no magnitudes.** The first draft's ±1/±2/±3 weights were the integrator's calibration, not the sources'. Numbers stay in claim quotes where a source actually measured something.
- **Provenance in three layers, plus a qualifier.** Author, channel and evidence come from Joseph's candidate in `src/ideation-truth-taxonomy.md`. The qualifier is his addition: *"'qualifier' or equivalent so that it can capture many other kinds of adhoc labels."* The reason: *"a lot of AI risk literature is going to be a lot of unqualified assertions."* The model keeps them, and shows them as what they are.
- **Delays.** Joseph asked whether the model captured that growth *rate* raises volatility while *size* slows organizations down. It didn't, until an `org-size` stock, `routinization` (with `delay: long`) and `coordination-costs` were added. Rate acts now; size damps only later, through routines that reorganization keeps resetting. Signs and delays show that race between timescales. Which side wins needs system dynamics, and the `sd_kind`/`units` hooks are there for it.
- **Open ends are first-class.** Three kinds of case are allowed, and each is named rather than left out:
  - a capability or change that *feels* dangerous for reasons not yet known;
  - a known effect to prevent whose causes are unknown (Joseph's example: *devaluing other human life*);
  - an observed, unprecedented change with no named consequence yet (his example: *problem-solving dependency*).

  The placeholders `unknown-causes` and `unknown-events` carry them.

## What makes it "true", and what doesn't

The model records **claims, not facts**: "X asserts that A raises B, on basis Z, hedged as W". A claim can be true as a record even when the relation it asserts is a guess. So hypotheses of any quality can be added without making the model less true. It just becomes more complete about what is being *thought*. Two relations are our own hypotheses, with no source in hand:
- size slows growth (`org-size → org-growth-rate`);
- capital pressure speeds it (`capital-pressure → org-growth-rate`).

Both are marked `qualifier: hypothesis (ours)`.

It is tempting to say the "strong subset" of the graph is the high-confidence system. **We deliberately leave "strong" undefined**, for these reasons:

- **This is a risk model, and likelihood is one axis of risk.** Joseph: *"likelihood is just one perspective — multiply by harm-scale at even very low likelihoods and/or confidence and it's still very meaningful for decision-making."* A weakly evidenced relation into a catastrophic event (`scale: catastrophic to existential`) can matter more than a well-evidenced one into a minor event. So the standing view *describes* each relation's support and shows the target's scale beside it. It never combines them into one number, and it never drops what is weak.
- **Well-evidenced relations map what has been studied, not what is true.** Measurement clusters where it's easy or mandated. CAISI doesn't measure loss of control; AISI measures what AISI can reach. A relation missing from the well-evidenced part usually means nobody has studied it. And filtering can bias the picture: if the damping loops are less studied than the amplifying ones, the evidenced subgraph looks more runaway than the world is.
- **Counting claims overstates support when claims share a lineage.** That's why claims are grouped into author clusters (`authors.yaml`). RAND-ISL and AISP share three authors; everything from this project is one cluster. Many claims also arrived through the same relay (a verification file) or the same prior-agent report, and the `channel` field records that. This is the correlated-watchers problem applied to our own evidence base.
- **Composed loops inherit their weakest link.** `check.py` finds loops no source asserted as a whole. Several run through the regulation arm, e.g. commercial pressure → monitorability → oversight → detection → regulation → loosening → race → back to commercial pressure. They're real structural findings, and only as strong as their weakest `+?` claim. Any view that draws loops should show which links are weak, or composition will launder hypotheses into structure.
- **Evidence about an endpoint isn't evidence about the link.** Anthropic's 26% measures how much AI R&D is AI-led; it doesn't measure the effect of that share on capability pace. Claims carry a `bears_on` field (`link`, `from`, `to`, `both endpoints`) so the two can't blur.
- **Concepts are claims too.** Which concepts exist decides which relations can be stated. "Absorption gap" and "decision coherence" are constructs from a hypothesis report written for Joseph; "detected incidents", "perceived risk" and "monitor independence" are the integrator's. Every concept carries `proposed_by`. The standing view stars concepts that exist only within this project, and marks relations asserted only by it.

## State, as of 2026-09-27

A worked slice: about 70 concepts, over 50 source-term mappings, about 100 relations carried by over 115 claims, and 16 loops. It covers loss of control by degree; oversight and evaluation; organizational dynamics, rebuilt on `ref/safety-and-hypergrowth.md` (absorption gap; people, structure and commitment layers; H3/H4; size and routinization); the recursive AI-R&D loop and oversight measures from `ref/anthropic-autonomous-dev.md`; human cognition with open ends; and indicators.

Not yet in:
- most of the hazard taxonomy;
- most of the round-2 verification material (company frameworks, US posture, UK/security frameworks);
- the enforcement layer (law vs voluntary vs benchmark, and who actually checks);
- visual views: Joseph wants these to judge whether the model works;
- Turtle export. The YAML is shaped for it: concepts → `skos:Concept`, mappings → SKOS match properties, claims → reified statements with `prov:wasAttributedTo`.

Next steps and open questions are in `HANDOFF-2026-09-27.md` at the repo root.

## Tools

```
python3 model/check.py              # validate; list loops (R/B by sign parity)
python3 model/check.py --standing   # plus per-relation standing, described not scored
python3 model/check.py --loops      # loop enumeration (slow with all shards; opt-in)
```
