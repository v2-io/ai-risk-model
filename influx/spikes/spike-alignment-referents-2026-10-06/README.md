# Spike: alignment referents and the actor vocabulary (2026-10-06)

**The question it started from.** Joseph asked for a look at "the implications of an ambiguous alignment definition", plus established names for the existing actors in `alignment-model/alignment.md` and proposals for new actors from the references. `CLAUDE.md` holds the related open decision: "Misalignment: a default referent, chosen after the claims show what they are about."

**Where it landed** (revised after `de-novo-feedback-1.md`; each item is argued, with its evidence label, in the file named):
- **Use types.** "Aligned" is used *relationally* (neutral; X can be an attacker), *anaphorically* (bound to the source's own stipulation), and *absolutely* (generic and evaluative, with which parties count and how conflicts are settled presupposed). → `03-structure.md` §1
- **Lists of referents.** Disjunctions inside claims fail under genuine conflict (demonstrated). Glossary lists are sense reports, not failed definitions. The corpus *bodies* discuss conflict rules; its definitions don't. → §2
- **Filings.** Categories defined against a referent move with it. On adversarial causes the field splits by where the cause enters the stack: weights mostly count as misalignment, context splits between state and origin readings. → §3
- **Defaults.** Each of seven single defaults tested hides a named risk, three of them conditionally. A declared, versioned candidate *set* is proposed in place of a default. → §4
- **Where the referent bites.** When a claim names its harm, the referent is idle. The pilot's ratio did not survive review; the recording rule did. → §5, `data/`
- **Relations.** "To whom" is eight relations (listed once, in §6.1). The map's Notes describe three confusions: attribution, force and epistemic status. → §6
- **Aspect and time.** Naming the party leaves instruction, intent, interest and values open, and initial vs. current goal. → §7
- **Proposal.** Slots in the lexicon; three recording levels; categories with their basis; no single-referent default. → §8
- **Response to the verification.** What changed and what I contest → `response-to-de-novo-feedback-1.md`

**Read in this order**
1. `debrief.md`: the whole spike for Joseph, in domain terms.
   - `response-to-de-novo-feedback-1.md`: the verification's corrections, and my responses.
2. `03-structure.md`: the analysis.
3. `04-actors.md` and `05-candidate-terms.md`: the vocabulary, all first-pass.
4. `06-map-suggestions.md`: proposals for the map (nothing in `alignment-model/` was edited).
5. `proposed-integration-plan.md`: suggestions for integrating, with a do-not-inherit list.

**Supporting files**
- `de-novo-feedback-1.md`: the independent adversarial pass (not mine).
- `00-on-the-brief.md`: the coordinator's after-the-fact priming list, and what I re-examined because of it.
- `01-map.md`: what the repo and corpus said before the analysis, and the live tensions.
- `02-sense-inventory.md`: every definitional passage found, with slots and locations.
- `research/lit-alignment-relation.md`: literature on the relation's structure (a research agent; 27 primaries).
- `research/lit-role-vocabularies.md`: literature on role vocabularies (a research agent).
- `data/`: the coded sample, the sample text and the extraction key list.
- `tools/`: the counting and sampling scripts.

**How to reproduce the corpus evidence.** `bin/extract-text -o DIR $(cat data/extraction-keys.txt)` regenerates the extractions (pdftotext 26.09.0). The two IASR / autonomous-dev keys are copies of `ref/iasr-2026-full.md` and `ref/anthropic-autonomous-dev.md`. `ec-2025-gpai-guidelines` and the NIST/CAISI web pages came from the same command. Line numbers cite those extractions.

**Status.** Spike output, unverified. Verification is commissioned separately. Nothing here is a lexicon entry.
