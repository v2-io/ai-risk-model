# Model schema

**Shards.** `check.py` loads `concepts.yaml` plus any `concepts-<slice>.yaml`, and likewise for mappings and relations, so agents can work in parallel without editing the same file. IDs must be unique across shards. A shard may reference concepts defined in any other file.

Field reference for `concepts.yaml`, `mappings.yaml`, `relations.yaml` and `authors.yaml`. For what the model is and why it's shaped this way, see `README.md`.

## Concepts (`concepts.yaml`)

| Field | Meaning |
| --- | --- |
| `id`, `label` | handle, and the quantity in plain words ("strength of safety culture", not "safety culture") |
| `broader` | taxonomy parents (groups `g-*`) |
| `kind` | what sort of variable this is: `context`, `dynamics`, `capability`, `propensity`, `affordance`, `practice`, `state`, `event`, `effect`, `signal`, `indicator`, `unknown`, `group`. **Not** whether it's good or bad. |
| `aisi_term` | AISI's own term, where AISI has one (*Loss of Oversight* glossary, AISI blogs, the incident report) |
| `definition`, `scale`, `notes` | our working sense; its position on severity or scope; anything else |
| `distinct_from` | concepts that look alike but are not the same (the ontological guardrail) |
| `proposed_by` | who introduced the concept: a source, "widely used", or this project (Joseph, the integrator, a prior agent report). Concepts are claims too: which concepts exist decides which relations can be stated. |
| `sd_kind`, `units` | system-dynamics hooks (stock / flow / auxiliary). Mostly blank. |

**Roles are never stored on concepts.** "Control", "escalation factor" and "escalation control" are what a relation makes of a concept. The same practice can reduce one thing and raise another.

## Mappings (`mappings.yaml`)

Each record maps one source term to one of our concepts: `rel` is `exact`, `close`, `broad` (the source term is broader than ours), `narrow` or `related`. It also carries `src` (relata key), `term`, `loc`, `quote`, `channel` and `note`. When one source term maps `broad` onto several concepts, that is a pooled term.

## Relations (`relations.yaml`)

| `type` | Meaning |
| --- | --- |
| `influences` | causal. `sign`: `+`, `-`, `?`; `+?`/`-?` = direction asserted weakly. **No magnitudes** unless a source quantifies, and then the number stays in the claim's quote. |
| *(any relation)* | optional `delay`: `short`, `long`, or a quoted duration. Delays are what let a CLD show a race between effects (e.g. growth rate raises volatility now; size dampens it later, through routinization). |
| `moderates` | acts on other relations (`targets: [relation ids]`). Example: management of change weakens the effect of structural churn on controls; it doesn't reduce churn. |
| `indicates` | an observable measure of a concept (indicators, or a contested "is this a sign of that?"). Not causal. |
| `part_of` | definitional (auditing is part of oversight). Not causal. |

**Each claim records provenance in three layers, plus a qualifier.** The three layers follow Joseph's candidate in `src/ideation-truth-taxonomy.md`:

| Field | Meaning |
| --- | --- |
| `author` | who asserts it |
| `channel` | how it reached us: `primary`, `press`, `secondary summary`, `relay: <verification file>`, `prior agent report`, `dialog` |
| `evidence` | what backs it: `none-stated`, `definition`, `instrument` (a binding text, e.g. a statute or MOU, that builds the relation in), `argument`, `expert-judgment`, `established-practice`, `document-change` (a documented revision of a framework's text), `measurement`, `incident` |
| `qualifier` | the source's own hedge or status, and any other ad-hoc label: "may", "Highly likely (PHIA)", "hypothesis H1", "proposal", "possible contributing factor; no causal analysis", "integrator inference" |
| `bears_on` | optional. What the evidence is about. Absent = `link`: the relation itself. Otherwise `from`, `to`, `both endpoints`, or `mechanism` (evidence that the mechanism works in another setting): the source measured a quantity at an endpoint, not the effect between them. Example: Anthropic's 26% measures how much AI R&D is AI-led; it doesn't measure that share's effect on capability pace. |
| `doc`, `loc`, `quote` | relata key (or file), location, verbatim text |

Unqualified assertions stay in, and their thinness shows: `evidence: none-stated`, one author, a press channel.

## Author clusters (`authors.yaml`)

Claims whose authors share people, an institution or a research lineage are not independent. For example, RAND-ISL and AISP share three authors; CAIS, VCT and Ren et al. share Hendrycks; everything from Joseph, the integrator and prior agent reports is one cluster, `this-project`. `check.py --standing` counts distinct clusters per relation. An author that matches no cluster counts as its own.
