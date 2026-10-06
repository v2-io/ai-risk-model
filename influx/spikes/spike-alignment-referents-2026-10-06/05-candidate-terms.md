# Candidate terms (first-pass)

*Candidates for the lexicon's alignment and actor groups, each with its evidence and an established name where one exists. None is an entry: each needs the truthification passes Joseph describes before it carries weight. Where I propose a name of my own, I say so; where Joseph's call is the deciding one, I say that too. "Est." means an established term, with its source. The [P] / [S] / [M] marks for sources outside the corpus are the literature report's.*

## A. The alignment relation: slots

The proposal in `03-structure.md` §8 is that the lexicon defines alignment as a relation with named slots and puts no default on any of them. The candidate slot names:

| Slot | Candidate name | Est. name(s) and source | Evidence that the slot is real (sources fill it differently) |
|---|---|---|---|
| what is aligned | **bearer** | (no single est. term) Hubinger: an objective, a policy; Kierans: a population | model / system / computation / institution / goal (`02-sense-inventory.md` §2) |
| what about the bearer is compared | **mode** | behaviour vs. intent alignment (Kenton 2021 [P]); impact vs. intent (Hubinger 2020 [P]) | GDM's "knowingly"; Christiano's "motives"; behaviour in Singapore's working definition |
| whose claims count | **claimant set** (my label; the literature's nearest is the *alignment target*) | "alignment target" (Hellrigel-Holderbaum & Dung 2025 [P]); the "tetrad" (Gabriel & Keeling 2024 [P]); Critch & Krueger's single/multi delegation for cardinality [P] | developer / users / operators / society; lists without a rule (§2 of `03-structure.md`) |
| what about them counts | **aspect** (my label; "content" in the literature report) | Gabriel 2020's ladder [P]; "preference payload" (Leike 2018 [P]); "outcome ordering" (Askell 2021 [P]) | instructions / intent / desire / interests / values |
| when | **time index** | initial / real-time / final reward (Carroll 2024 [P]); static / dynamic (Hellrigel-Holderbaum & Dung [P]); `alignment.md`'s initial vs. current goal | the time-instruction incident; goal drift (Chin) |
| how conflicts are settled, and who is admissible | **adjudicating standard** | Gabriel & Keeling's principles "that specify appropriate conduct for a given domain" [P]; chain of command (OpenAI Model Spec [P]); principal hierarchy (Anthropic constitution [P]); legitimacy qualifier (constitution [P]) | IASR's "depending on the context"; MIT's "especially"; Davidson; NIST AI 100-2 |
| who judges | **judge** | "a reasonable person with full understanding" (Anthropic Aug); an idealized observer; "would not endorse" (GDM) | CAISI's LLM-as-judge |
| over what situations | **domain** | "problem areas" (Kierans [P]); role-appropriate norms (Zhi-Xuan 2024 [P]); "high-stakes distribution" (Anthropic Aug) | context-dependent vs. pervasive misalignment |
| how much | **degree** | "degree of overlap" (Askell [P]) | Kulveit's "the degree to which" |

**Values of the outcome**, for a single use (in translation, not in the lexicon): *aligned / misaligned / irrelevant*. "Irrelevant" is est. in Chin et al. (chin L1154–1156): actions that "do not affect the achievement of the other goal". Without it, "not aligned" collapses into "misaligned".

**Use types** (a field on each translated occurrence):
- *relational* (the complement is stated);
- *absolute* (the slots are implicit; under-specification, per the SEP *Ambiguity* entry [P via the report]);
- *activity* ("alignment training");
- *field* ("alignment research").

**Coverage outcomes for absolute uses:**
- *invariant over S* (S named): est. frame, supervaluation ("true under all admissible precisifications", SEP *Vagueness* [P via the report]);
- *sensitive among named candidates*;
- *unresolvable*.

These sit beside the gamma plan's resolution outcomes (§3.4), as reasons with an author.

**Paired names worth recording as `:synonyms` or "not to be confused with"** (all [P] in the report): thin vs. thick (Hammond); direct vs. social (Korinek & Balwit); minimalist vs. maximalist (Gabriel 2020); local vs. full-stack (Edelman et al.); misaligned *simpliciter* (Gabriel & Keeling: harm that favours no party).

## B. Words to record with their senses, not to adopt bare

| Word | Why | Evidence |
|---|---|---|
| **loyalty** | The est. word for party-directed alignment in the coup literature ("singular loyalties", "secret loyalties"). Also agency law's duty of loyalty [S via Kolt]. A candidate name for *alignment whose claimant set is one party*, with Davidson as the specimen of its risk | davidson L18–19, L105–117 |
| **principal** | At least four senses, which collide: agency law, "on whose behalf … subject to the principal's control" (Restatement via Kolt [S]); the constitution's "whose instructions Claude should give weight to" [P]; security identity, "construct each agent as a distinct principal" (ASD); LaCroix's "stakeholders" as principals [P]. *Candidate:* adopt the agency/constitution sense and record the others as collisions | asd L542–544; report §5.2 |
| **operator** | Four senses; see `04-actors.md` §2 | — |
| **developer** | Legal, organisational, individual, app builder (Model Spec's "developer" role [P]); and the holder of the reference intent | OVERVIEW §2.14; Model Spec |
| **intended / unintended** (agentless) | Deletes the claimant slot from the grammar ("behaves as intended"). Translations should record it as *claimant unstated* | sg2025 L723; stix-loss L1455 |

## C. Actor-side candidates

`04-actors.md` has the row-by-row evidence. In summary, first-pass:
- **Relations** (§1 there): *writes into* (est. nearest: the Model Spec's message *roles* as channel types [P]), *directs* (est.: *principal*, in the agency sense), *owed regard* (est.: NIST *affected individuals/communities*; the constitution's "those whose interests Claude should give weight to"), *authors a standard* (est.: NIST's "Other AI actors may provide formal or quasi-formal norms"), *oversees*, *answers for*.
- **Existing rows with est. anchors:**
  - user → *end user* (NIST, ETSI);
  - affected third parties → *affected individuals/communities* (NIST);
  - harness provider → *system operator* (ETSI) / *scaffolding developer* (AISI) / *operator* (constitution [P]) / *developer* (Model Spec [P]): all colliding;
  - model trainer → *original model developer* (AISI) / *frontier developer* (SB 53, by training act).
- **New rows, with evidence:** fine-tuner or downstream modifier; human feedback providers; evaluator (split from overseer); norm author; state or regulator as a writer through mandated training; data custodian; model host or distributor; general public (split out of "society, law, humanity").
- **Standing mismatch** (my name): a channel given more standing than its writer has. This is the common form of the map's Notes' vulnerabilities. Nearest est. language: the companies' rules ("information rather than … commands"; "Ignore untrusted data by default") [P].

## D. Additions from the role-vocabulary report (first-pass)

- **Relations, with established names:**
  - *influence* (Shavit; W3C PROV-DM) for **writes**;
  - *instruction privilege* (Wallace) / *levels of authority* (Model Spec) / *de jure authority* (SEP) for **directs**;
  - *de facto* / *effective authority* for **controls in fact**;
  - *dependent* / *indirect stakeholder* (Mitchell, Agle & Wood; VSD) for **owed**;
  - *beneficiary* (trust law) for a seventh relation, **benefits**, that can come apart from **directs**.
- **Delegated authority** (Model Spec: "authority may be delegated to these sources"; "users may *implicitly* delegate authority … AGENTS or README files"): the est. name for how the user's environment and tool outputs acquire standing.
- **Counterparty** (agency law's third party; Chan et al. 2025; AP2's merchant): a new actor candidate, likely the home of the map's "agents embedded in applications".
- **Confused deputy** (Hardy 1988; OWASP ASI03): the est. security name for a standing mismatch exploited.
- **"principal"** now has seven recorded senses. The economic one (common agency) makes an injector a principal. A declared sense is required if the word is adopted.
