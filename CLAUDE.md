# AI risk model

A model of the frontier-AI risk landscape, built from what the field's own risk assessments, safety frameworks, laws and research actually claim. It is held with high fidelity to those sources and expressed in a rigorous, shared vocabulary of our own. The aim is a consolidated map that can be looked at and projected from many angles: by cause, by control, by risk event and impact, and by who is affected and who decides.

Joseph Wecker leads it. It is **in development**: the current state is two earlier attempts (in `influx/`) and a plan for what comes next (below). It is a public repository.

*This file is also the README (`README.md` is a symlink to it). It records what is currently true and what we are currently doing. History lives in `influx/` and `.archive/`.*

## Principles

- **Compilation, not adjudication.** The model records what each source claims, in its own words and with its role marked. It does not argue for or against any claim, including hypotheses of the project's own. If the structure is right, the answers to questions about the landscape should be easy to see without a verdict being written in.
- **Fidelity.** Every claim is anchored to a verbatim passage with its location, so any reader can check exactly what is being claimed. Our reading of a source is always attributed as ours, and kept beside the source's words, never in place of them.
- **Soft evidence stays in, marked.** Second-hand accounts, unverified quotes and bare assertions reduce uncertainty too. They go in, marked for what they are (author, channel, evidence, the source's own hedge), and are never silently upgraded or dropped.
- **Vocabulary first.** The lexicon comes before the claims that use it. See the next section.
- **Correlation is not corroboration.** Many sources copy, cite or share authors with one another. Agreement counts only as far as sources are independent, so derivation, shared authorship and declared interests are recorded.
- **Conflict of interest, stated plainly.** Much of the work is done with Claude models, and Anthropic appears in the evidence in both directions. Anthropic material gets the same scrutiny as anything else, and the model says so where it bears.

## The approach: bounded contexts and a shared lexicon

Every source is its own *bounded context*, in the sense of domain-driven design. It has its own lexicon (usually implicit and loosely defined), its own taxonomies, its own model of how risk works, and its own methodology. The sources' terms collide within documents, across documents, and across domains. "Hazard" alone has at least seven senses in the corpus, and "developer", "loss of control", "safeguard" and "alignment" each have several.

So the project keeps five things apart:

| | What it is | Here |
|---|---|---|
| **Lexicon** | our words and exactly what each means: shared, rigorous, unambiguous, evolving, scoped to our bounded context | term groups in udon, with invariants, relations to other terms, groupings of terms defined together, declared scope narrowing and widening, deliberate ambiguity where it is honest, and "not to be confused with" |
| **Taxonomy** | a classification scheme over some kind of thing, by a basis of division | something a source asserts; in our lexicon, broader/narrower relations |
| **Ontology** | the kinds of things that exist and how they relate | the entity kinds our assertions are about |
| **Model** | an ontology plus claims about how things behave | each source's own model (see `influx/source-models/`), and eventually ours |
| **Methodology** | how a source produces its claims | recorded with the source, because it sets what kind of claim comes out and its warrant |

The plan is:
1. build our lexicon;
2. for each source, write a *context map*: a mapping of its terminology into ours, with a rationale for what is *probably* meant. Where it is genuinely unclear, the mapping records "ambiguous among these candidates" rather than forcing one;
3. write each source's assertions in our terms, in the context of the source's own model, with its words kept verbatim beside them.

Precedents in the corpus for this way of working include MIT's AI Risk Repository (a shared governance vocabulary, built by normalising 74 frameworks into two taxonomies). Its costs are a useful caution: interaction coded as "Other", a risk spanning several domains coded to one, a single coder.

## Current plan (in development)

1. **Source catalog.** `source-catalog.md` is the canonical list of the model's main sources, with a declared *Influence* grouping.
2. **Distinctions inventory.** Every basis of division and category boundary the corpus draws, so our lexicon can express each. Examples: MIT's entity / intent / timing; the EU Code's capability / propensity / affordance; the UK National Risk Register's hazard / threat; Zwetsloot's accident / misuse / structure.
3. **Lexicon.** Tighten the term groups against that inventory and against the cross-model term collisions in `influx/source-models/OVERVIEW.md`.
4. **Context maps,** one per main source.
5. **Assertions** in our terms, anchored to passages.
6. **Views,** computed rather than maintained: a causal loop diagram, bow-ties around a chosen event, crosswalks, corroboration counts that respect lineage, and coverage by each source's declared scope.

The schema for steps 4–6 is a proposal, not yet ratified: `influx/model-beta/SCHEMA-SYNTHESIS.md` (draft 2). The risk side is organised around Joseph's causal chain:

```
(sources & causes tree) → (preventions & controls) →
  (risk events [recorded, ideated, unknown] × impact radius [harmed groups, degree/scale]) →
    (mitigations & recovery) → (policies & decision-making)
```

Stage in that chain is read as a role relative to a focal event, not as a fixed property of a kind.

## Open decisions (Joseph's)

- "Developer": dissolve into roles conferred by instruments (model trainer, inference provider, harness provider, …) plus an organisation term. This is the direction under discussion, not decided.
- Hazard vs threat: Joseph leans toward the National Risk Register's sense (hazard is the non-malicious counterpart of threat). Leaning, not decided.
- Misalignment: a default referent, chosen after the claims show what they are about.
- The impact radius as target (a group of people, or a system or shared good) × degree × recoverability.
- Whether STPA's vocabulary is adopted for the chain or kept as one mapped source among several.
- Format: udon for the lexicon is decided; the rest stays YAML until a udon parser exists.

## Layout

| Path | What it is |
|---|---|
| `source-catalog.md` | the canonical list of main sources |
| `influx/model-alpha.md` | the first compilation: a risk-factor crosswalk across sources (superseded as a structure; its source list seeded the catalog) |
| `influx/model-beta/` | the second attempt: a claim-backed causal graph (`concepts*`, `relations*`, `mappings*.yaml`, `check.py`), the draft lexicon (`terms/*.ud`), and the schema proposal (`SCHEMA-SYNTHESIS.md`) |
| `influx/source-models/` | each major source's own model, on its own terms, plus `OVERVIEW.md`: a comparison, cross-model term collisions, lineage and coverage |
| `influx/source-atlas/` | a per-family atlas of 212 source documents (TOC, glossary and representative passages), the atlas agents' feedback on the schema, and reading notes |
| `influx/verification/` | the evidence files from the first verification rounds, with verbatim quotes and locations |
| `influx/*.md` | smaller inputs: the aligned-to-whom table and diagram, a note on AI welfare framings in the sources, a note setting an in-progress philosophy discussion beside the corpus |
| `alignment-model/` | the "Aligned to whom?" map: the actors who influence a deployed agent, through what, and what reaches it. Built from `alignment-model/alignment.md`; its README says how |
| `ref/` | local copies of reference texts. Some are git-ignored (see `ref/.gitignore`), including the IASR 2026 full text. |
| `bin/extract-text` | regenerates the `pdftotext -layout` extractions that line references point into (see Working notes) |
| `.archive/` | superseded material |

`influx/` is working material and will move to `.archive/` as its contents are superseded.

## Working notes

- **Sources live in relata**, Joseph's citation manager (`relata --help`). For a document's text, `relata show <key>` gives its PDF path; extract it with `pdftotext -layout`. Avoid `relata show-markdown` to check conversion state, since it forces the conversion. Avoid `relata ingest --retry`, which re-stages the whole shared review queue.
- **Line references** in the atlas and source-model files point into `pdftotext -layout` extractions, which aren't kept in the repo; `bin/extract-text <key>…` regenerates them into `.extract/` (git-ignored). PDF pages survive re-extraction; cite both.
- **Parallel agents** each need their own scratch directory. Shared helper-script names have collided before.
- **This repository is public.** Keep private or personal material out of it.
- **Current Exposures**: influx/ai-welfare-and-release-framings.md, influx/model-beta/notes-sx.md, and influx/perspective-logos-2026-09-28.md -- Joseph may decide to remove at some point, but they are fine for now (- Joseph, 28-Sept-2026)

