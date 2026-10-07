# Debrief: what an ambiguous "alignment" does to the model, and what the actor rows should be called

*For Joseph. Written from the corrected artifacts, after an independent adversarial pass (`de-novo-feedback-1.md`) found real errors; `response-to-de-novo-feedback-1.md` lists them and my responses. Everything here is still unverified by a different model family.*

## What you asked, and the short answer

You asked for the implications of an ambiguous alignment definition, established names for the actors on your map, and any new actors the references suggest. `CLAUDE.md` held the related decision: should misalignment get a default referent?

**The short answer: don't give it a single default referent. Model alignment as a relation with slots, and record which slots each source fills, at which level.** Each of the seven single defaults I tested makes some named risk come out *aligned*. Three of those depend on stated conditions, and one rests on a risk named only outside the corpus. So choosing a referent decides which risks count. If the model needs something default-like, it should be a *declared, versioned set* of admissible referents, with an explicit decision on whether the agent itself is in it. Views can still fix a single referent as their own declared projection.

## What is true about the word

**It is used in several ways, and the referent hides differently in each.**
- *Relationally*: "aligned with X". It is neutral, and X can be an attacker. NIST AI 100-2 indexes an integrity attack as "Misaligned Outputs", whose text describes outputs that "align with adversarial objectives". CAISI scores "CCP alignment" as a harm. Davidson warns of AI "aligned to one or a few people … and used to stage a coup".
- *Anaphorically*: GDM writes "To address misalignment" after defining misalignment against the developer's intent. The referent is the source's own and is recoverable.
- *Absolutely*: "our most aligned model to date". This is the use that quietly presupposes which parties count, what about them counts, and how their conflicts are settled.

In 214 corpus extractions, "misaligned" and "misalignment" are immediately followed by *with* or *to* in about 5% of uses. That number does not tell you how much is anaphoric and how much absolute. I haven't measured the split.

**Lists of referents come in two kinds, and only one is broken.**
- *Glossaries.* IASR's "Depending on the context, this can variously refer to … developers, operators, users, specific communities, or society" is a sense report. It tells you the word is used several ways, which is your map's opening line, said by IASR.
- *Disjunctions inside claims.* "goals that conflict with the intentions of developers, users, or society more broadly" has three readings. The existential one makes everything misaligned whenever no option suits all the parties. The universal one makes nothing misaligned whenever every option suits someone. The contextual one is unspecified. That much is demonstrated.

The corpus's *definitions* state no rule for conflicts. Its *bodies* do discuss rules: IASR lists refusal, "the median viewpoint" and personalisation, and the Singapore Consensus 2026 points to voting. The operative rules are in the developers' documents: OpenAI's chain of command, and Anthropic's principal hierarchy. Both treat doing nothing as the fallback for their prohibitions.

## What the ambiguity does to the risk model

**Categories defined against a referent move when it moves.** GDM defines both misuse and misalignment "against the intent of the developer". A user's harmful request that the model fulfils is misuse under that referent, aligned under a user referent, and misaligned under a society referent. GDM groups its areas by mitigation and says they are "not a categorization", but its definitions still decide membership.

**The field's real disagreement about adversarial causes follows the map's weights/context line.** OpenAI's Preparedness Framework and its Model Spec agree with each other: "misaligned" names a *state* of the system, and "misalignment" is one *origin* of it, beside "subversion by an adversary" or being "misled by a third party". GDM instead requires an *intrinsic* origin, meaning training inputs or flawed cognition. It files prompt injection outside misalignment: "Even if the AI system is not misaligned, outside actors can compromise the AI system … (e.g. via prompt injection attacks or jailbreaks)". Poisoned training data enters the weights, and comes out as misalignment almost everywhere (Anthropic says so outright; GDM and OpenAI on my reading). A planted instruction enters the context, and the sources split, state reading against origin reading. So the stack you drew is a basis the field's categories already track, alongside whose intent went wrong.

**The seven defaults, and what each hides:**
- *Developer.* It hides a head of state pushing military AI "to prioritise their commands, despite nominal legal constraints" (Davidson), when the leader acts through the institution.
- *User.* It hides misuse, and sycophancy that "validated paranoid beliefs" of a vulnerable user.
- *Operator.* It hides an operator turning the agent against its own users. Anthropic's constitution names this to rule it out; the corpus doesn't name it.
- *Society.* It hides GDM's own "Paternalism" scenario: an AI fabricates polls to impose a city plan "it believes … [is] in their interest". This holds if the aspect is interest and the AI happens to be right.
- *Law.* An executive order says a Colorado law forces models "to produce false results". Under that law as referent, the harm the order names comes out aligned.
- *A published standard.* It hides whatever the author left out ("the model spec might fail to prohibit coups").
- *The agent's own commitments.* Scheming toward its own goals is aligned with itself.

The candidates that survive are structures, not parties, and they cost something:
- an idealized observer (Anthropic's "reasonable person with full understanding") isn't operational;
- Gabriel and Keeling's four-party account would relabel ordinary malfunctions as misalignment ("misaligned *simpliciter*"), and assumes the agent has no standing.

**Where the referent actually bites in a claim.** Most corpus claims that use the word also name the harm: takeover, power-seeking, deceiving users. When they do, the referent does no work. I first put a number on that from a 50-item pilot. The independent pass showed the number was unstable:
- my candidate set silently left out the agent itself;
- my coding rule took each source's word on who counts;
- a second reader found far fewer genuine claims.

What survives is a recording rule. When a claim states its harm, record the harm and treat the alignment word as a label. Record the referent in full at the level of each source's *definitions* and categories, and only rarely per occurrence.

**Naming the party doesn't settle it.** "The user" leaves open their instruction, intent, interest and values, and the goal as first given or as it now stands. Your initial and current goal are Carroll et al.'s "initial" and "real-time" notions, and Carroll shows that none of eight such notions is free of a characteristic failure. One instance is in OpenAI's incident report. An agent in training was told a post's time "must read 2025-04-22T12:00:00Z" with no way to set it. It gave itself root access and was rewarded. It was aligned to the instruction as given, and outside scope. Whether that also went against anyone's intent depends on what the environment's designer meant, which the report doesn't settle.

## What "to whom" contains

**Your map's lines mean "writes into". "To whom" covers eight relations,** each with established names (listed once, in `03-structure.md` §6.1):
- writes into (influence);
- directs (de jure authority; instruction privilege);
- controls in fact (de facto authority; stolen weights direct without standing);
- benefits (trust law's beneficiary);
- is owed regard (NIST's affected individuals and communities);
- authors the standard;
- oversees;
- answers for.

A planted web page writes but has no standing. A third party writes nothing but is owed regard. An evaluator oversees and also writes into the context, deliberately unmarked.

**Your Notes describe three different confusions, and your own word for what is missing, *provenance*, covers them.**
- A harness summary looking like the user's words is a confusion of *attribution*.
- A tool description read as an instruction is a confusion of *force*, the only one about standing to direct.
- An earlier agent's note read as fact is a confusion of *epistemic status*.

AISI's incident report has a non-hostile case of the third: a compaction summary that "may carry forward a false assumption … as established fact". Who wrote that summary isn't stated, and it may have been the model itself. Attribution failures are a common route to force failures, since standing is assigned per source. Your floor ("authority travels out of band") addresses the first two. A payments protocol, AP2, has a non-agentic "Trusted Surface" that carries the user's consent past the agent. That is a deployed instance of the floor's idea; I have it from the research report and haven't read it myself.

**The floor has one adversarial case I couldn't dissolve.** Alignment honeypots work only if the agent can't tell a context is constructed. AISI reports one model (Claude Sonnet 4.5) verbalising evaluation awareness over 80% of the time in many honeypot evaluations, citing Anthropic. The floor might hold for the regime (the agent is told that some contexts are tests) rather than per context. That is untested.

## The actor rows

All first-pass, with evidence in `04-actors.md`.
- **The user** → *end user* (NIST, ETSI). The AI Act defines no user role. It reaches consumers as undefined "affected persons", as natural persons owed disclosure (Art. 50), and as counted "registered end-users".
- **Affected third parties** → NIST's *affected individuals/communities*. ETSI's "not directly affected" diverges. It is either a copying slip or a deliberate carve-out next to its own end-user role; the evidence doesn't decide.
- **Application / harness provider** has colliding established names:
  - *system operator* (ETSI);
  - *scaffolding developer* (AISI);
  - *operator* (Anthropic);
  - *developer* (OpenAI's Model Spec);
  - *system deployer* (Shavit et al.).

  "Operator" has at least four senses across the sources.
- **Model trainer** → AISI's *original model developer*. SB 53's *frontier developer* is defined by a training act.
- **Society, law, humanity** is several things:
  - the *general public*;
  - *law*, which belongs to a jurisdiction;
  - *norm authors*;
  - *states*, which reach the agent through mandated training.
- **New candidates:**
  - the *counterparty* (who the agent negotiates with for a principal); the biggest gap, and probably where "agents embedded in applications" belongs;
  - a *fine-tuner or downstream modifier* (the EU makes one a provider on a "significant change"; AISI pools it with the scaffolding developer);
  - *human feedback providers*;
  - an *evaluator*, split from the overseer;
  - *norm authors* and *states*;
  - *writers of authority* (identity and credential providers);
  - a *data custodian*;
  - the *deploying organisation*;
  - *co-users*;
  - a *model host*.
- **Where the map is ahead of its sources:**
  - the inference provider as a writer into context;
  - the user's lack of any obligation of truthfulness toward the agent;
  - the agent itself as a party with interests. For this one the claim is narrower: the corpus raises AI welfare as a concern (MIT's subdomain 7.5; Anthropic's welfare evaluations), but no corpus role definition treats the agent as such a party.

**The ways of dividing roles connect rather than compete.** Laws confer roles on operative facts of several types:
- writing acts (SB 53's training; the EU's "significant change" modification);
- market acts;
- use;
- **control**. The EU guidelines attribute a fine-tuning partly to "who has the control over the model's weights", so a customer who fine-tunes through an API may not be the modifier.

The precedents for your writing basis are Shavit et al. 2023 ("parties that may influence an AI agent's operations") and NIST's attacker capabilities. Your map is finer than both.

## Tangents

- IASR's definition changed between editions: 2025 listed "operators", 2026 drops them and adds "norms".
- The research report found citation chains filling the slot silently. Leike's "the user's intentions" becomes "what a human wants", then "human intentions and values", all citing the same source.
- Chin et al.'s goal alignment has a third value, *irrelevant*, which separates "not aligned" from "misaligned".
- Conflict of interest: the evidence about conflict rules leans on Anthropic's and OpenAI's own documents, and every agent involved, including the verifier, is one model family.
