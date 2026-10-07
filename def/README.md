# def/

The lexicon's term groups, one udon file per group, in the house style of the address-theory entries (`v2-io/udon`, `v2/references/def/`). Every entry is `:status proposed`. An entry carries weight only after Joseph's refinement passes (`MODEL-GAMMA-METHODOLOGY-AND-PLAN.md` §2).

## Namespaces

Each term's name carries its namespace, as in `ddd:bounded-context`, and references use the full name, as in `@{ddd:model}`. Namespaces keep this project's method words apart from its domain words, which share many names. `ddd:context` is a setting that fixes meaning; the agent part *context* is what an agent has taken in during a run. The collisions are listed in the plan, §3.2.

| Namespace | Files | What it holds |
|---|---|---|
| `ddd:` | `def-ddd-*.ud` | Eric Evans's domain-driven design terms: the strategy vocabulary for treating each source as its own bounded context |
| `addr:` | none here | Joseph's address theory (reference, binding, scope, resolution, …), imported by reference and not defined in this repository. Cited at commit `90f4fb6` of `v2-io/udon`, `v2/references/def/` (plan §3.2). The prefix is provisional |

## What an entry's blocks mean

The address-theory blocks (`|rels`, `|invariants`, `|discussion`, `|examples`, `|working-notes`, `:synonyms`, `:avoid`) keep their meanings. The `ddd:` entries add five blocks, listed below after `|invariants`, which they are read against. They keep what a term *is* apart from when it arises, what its author recommends, and what this project proposes:

- `|invariants`: what holds of every instance, the term's delimiting characteristics;
- `|conditions`: when the source says the thing arises or is called for, which is not part of what it is;
- `|practices`: the source's advice about it, which is not part of what it is either;
- `|collisions`: other senses of the same words, in the corpus or in this project;
- `|proposed-widening`: a widening of the source's scope that this project proposes but has not adopted. It is kept out of `|invariants` so that it cannot be inherited as part of the term;
- `|ambiguity`: a declared ambiguity in the source's own usage, left unresolved on purpose.

Readings are attributed:
- An invariant or condition followed by a quotation and a page number is the source's own.
- A line ending "— our reading" is this project's inference.
- `:source` on each term says which kind its definition is:
  - "verbatim": the source's definition unchanged;
  - `[SOURCE: …, modified — …]`: our definition, with what was changed (ISO 704's marking).

## Attribution

The `ddd:` entries quote and adapt Eric Evans, *Domain-Driven Design Reference: Definitions and Pattern Summaries* (Domain Language, 2015), licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). The local copy is `ref/DDD_Reference_2015-03/`, and page numbers are from its table of contents. The quotations were checked by script against that copy, allowing only for capitalization. Changes are marked term by term in `:source`. Everything not quoted is this project's.
