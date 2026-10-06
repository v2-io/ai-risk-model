# Spike: alignment referents and the actor vocabulary (2026-10-06)

**The question it started from.** Joseph asked for a look at "the implications of an ambiguous alignment definition", plus established names for the existing actors in `alignment-model/alignment.md` and proposals for new actors from the references. `CLAUDE.md` holds the related open decision: "Misalignment: a default referent, chosen after the claims show what they are about."

**Where it landed** (each item is argued, with its evidence label, in the file named):
- "Aligned" is used in two ways. *Relational* ("aligned with X") is neutral and can name an attacker. *Absolute* ("misaligned") is evaluative and presupposes which parties count and how their conflicts are settled. The corpus overwhelmingly uses the absolute form. → `03-structure.md` §1
- Multi-party definitions with no conflict rule fail exactly where the referent matters (demonstrated). → §2
- The misuse / misalignment partitions move with the referent. Sources file the same event (a planted instruction, a jailbreak, poisoning) differently, depending on which writer carried the intent. → §3
- Each of the six single default referents tested hides a risk that is named somewhere: five against corpus risks, and one against a company document. A default is a choice about which risks count. → §4
- Most truth-apt claims are invariant across referents. The referent matters in definitions and category labels. This rests on a single-coder pilot, and needs a blind recode. → §5, `data/`
- "To whom" is several relations: writes into, directs, controls in fact, is owed regard, authors the standard, oversees, answers for. The map's Notes describe one vulnerability pattern, a channel given more standing than its writer has. → §6
- Naming the party doesn't fix the referent: instruction, intent, interest and values differ, and so do initial and current goal. → §7
- The default question, restated, and a proposal: the lexicon defines the slots, not the fillers; translations record use type and invariance; any default lives on a view. → §8

**Read in this order**
1. `debrief.md`: the whole spike for Joseph, in domain terms.
2. `03-structure.md`: the analysis.
3. `04-actors.md` and `05-candidate-terms.md`: the vocabulary, all first-pass.
4. `06-map-suggestions.md`: proposals for the map (nothing in `alignment-model/` was edited).
5. `proposed-integration-plan.md`: suggestions for integrating, with a do-not-inherit list.

**Supporting files**
- `00-on-the-brief.md`: the coordinator's after-the-fact priming list, and what I re-examined because of it.
- `01-map.md`: what the repo and corpus said before the analysis, and the live tensions.
- `02-sense-inventory.md`: every definitional passage found, with slots and locations.
- `research/lit-alignment-relation.md`: literature on the relation's structure (a research agent; 27 primaries).
- `research/lit-role-vocabularies.md`: literature on role vocabularies (a research agent).
- `data/`: the coded sample, the sample text and the extraction key list.
- `tools/`: the counting and sampling scripts.

**How to reproduce the corpus evidence.** `bin/extract-text -o DIR $(cat data/extraction-keys.txt)` regenerates the extractions (pdftotext 26.09.0). The two IASR / autonomous-dev keys are copies of `ref/iasr-2026-full.md` and `ref/anthropic-autonomous-dev.md`. `ec-2025-gpai-guidelines` and the NIST/CAISI web pages came from the same command. Line numbers cite those extractions.

**Status.** Spike output, unverified. Verification is commissioned separately. Nothing here is a lexicon entry.
