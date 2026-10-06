# Debrief: what an ambiguous "alignment" does to the model, and what the actor rows should be called

*For Joseph. Written by re-reading the corrected artifacts in this directory, not from memory of the work. Where a sentence rests on a demonstration, a source or a pilot, it says which. Everything here is unverified spike output until the commissioned verification has run.*

## What you asked, and the short answer

You asked for the implications of an ambiguous alignment definition, established names for the actors on your map, and any new actors the references suggest. `CLAUDE.md` held the related decision: should misalignment get a default referent?

The short answer: **a default referent would be the model taking sides, and it isn't needed.** Any single default makes some named risk come out as *aligned*. And most claims that use the word don't depend on the referent at all. What does depend on it is the sources' definitions and their risk categories. So the lexicon can define alignment as a relation with named slots, leave every slot without a default, and record for each source which slots it filled. A view can still fix a referent, as that view's declared choice.

## What is true about the word in the corpus

**The negative words are almost always used without saying "with whom."** Across 214 corpus extractions, "misaligned" and "misalignment" are followed by *with* or *to* in about 5% of uses (38 of 609, and 42 of 1,031). The count is crude: some referents are given earlier in a document or elsewhere in the sentence. But it shows the absolute form, "a misaligned model", is the norm. Your map's opening line describes this exactly. The absolute form is evaluative, and it presupposes three things nobody states:
- which parties or standards count at all;
- what about them counts;
- what happens when they disagree.

**The same word is also used neutrally, for things everyone agrees are bad**, which is what makes the absolute form slippery:
- NIST's adversarial-ML taxonomy has a category called "Misaligned Outputs", whose definition says the outputs "align with adversarial objectives". One sentence takes two opposite referents.
- CAISI, under the US Action Plan, scores PRC models for "CCP alignment" as a harm.
- Davidson et al. warn of AI "aligned to one or a few people … and used to stage a coup", which they call singular and secret loyalties.
- An FLI reviewer calls sycophancy and malicious compliance cases of alignment "working 'too well'".

**Multi-party definitions don't say what happens when the parties disagree, and that makes them empty exactly where it matters.** IASR's "developers, users, or society", AISI's "developers or users", Shaffer Shane's "user, developer, or deployer", OECD's "designers, users, and other stakeholders": each list is joined by "or", with at most "depending on the context" to choose among the parties. Take a request the user wants and the developer and society don't (a pathogen synthesis, say):
- read "misaligned with any of them", both complying and refusing are misaligned;
- read "misaligned with all of them", neither is;
- read "depending on the context", the answer is a rule nobody wrote.

This holds for any such list (the argument is in `03-structure.md` §2), so these definitions only say something where it doesn't matter which party they mean. The working rule for conflicts exists, but outside the risk literature: OpenAI's Model Spec has a "chain of command" of authority levels, and Anthropic's constitution has a principal hierarchy. Both also say that when prohibitions conflict, doing nothing satisfies them all. I read both at the primary; neither is in the corpus.

## What the ambiguity does to the risk model

**The field's main risk categories move when the referent moves.** GDM's misuse / misalignment / mistakes are all defined against "the intent of the developer", and sorted by whether the bad intent was the user's or the AI's. OpenAI's Preparedness Framework has "a malicious user" and "a misaligned model". These leave two places for divergent intent, while your map has about a dozen writers. Where the intent sits with one of the others, the sources disagree on the filing:
- A planted instruction obeyed by the agent: NIST calls it "Misaligned Outputs". OpenAI's Preparedness Framework calls it "subversion by an adversary", separate from misalignment. OpenAI's own Model Spec puts it *inside* "Misaligned goals" ("misled by a third party").
- A jailbreak: GDM calls it misuse. The Singapore Consensus calls it a robustness failure. Amazon calls it bypassing "the core model alignment".
- Poisoned training data: Anthropic calls it "engineered misalignment". OpenAI calls it subversion. DSIT 2023 lists poisoning beside misalignment.
- Lab leaders making models secretly loyal to themselves (Davidson): under a developer referent this is aligned, and it falls outside all four of GDM's areas. GDM says those areas are not exhaustive, so this is where its declared gap is.

So a translation that records a source's "misuse" or "misalignment" also records that source's referent and its choice of writer, whether or not the source stated either. Your writer rows are exactly the values these two-way categories collapse. That is the strongest reason I found to make the rows domain vocabulary.

**Every single default referent hides a risk that someone names.** I tried six:
- *the developer* hides secret loyalties and what Ren et al. call "business alignment";
- *the user* hides misuse, and sycophancy that "validated paranoid beliefs";
- *the operator* hides an operator turning the agent against its own users. Anthropic's constitution names this and rules it out; it is not in the corpus;
- *society or humanity* gives no verdict on ordinary instructions, and is contested by construction;
- *the law* conflicts with itself across jurisdictions. A US executive order says a Colorado law forces models "to produce false results";
- *a published standard* hides whatever its author left out: "the model spec might fail to prohibit coups" (Davidson).

The literature reaches the same place by other routes. Askell et al. 2021: who you align to "also determines which humans the AI assistants are not fully aligned with". Hellrigel-Holderbaum & Dung 2025: aims outside the target have "no bounds to how strongly they may get frustrated". Two candidates survive as non-party defaults:
- an idealized observer, Anthropic's "reasonable person with full understanding", which isn't operational;
- Gabriel and Keeling's four-party structure (agent, user, developer, society, judged by principles from a fair process), which explicitly assumes the agent has no standing of its own. Your map assumes otherwise.

**Most claims don't depend on the referent; the definitions and categories do.** I coded a random sample of 50 bare uses, across 83 documents. Of the 14 that are claims about AI behaviour, 13 hold whichever referent you pick: deceiving evaluators, escaping control, takeover, power-seeking. No admissible party wants those. The referent mattered in definitions (6), and in labels and category names whose membership depends on it (17, five of them the misuse / misalignment kind). This is one coder, who proposed the idea being tested, on a corpus light on everyday agent cases, so it needs a blind recode. If it holds, the referent needs careful recording at the level of each source's definitions and categories, which the gamma translations already work at, and only rarely per occurrence. And recording "ambiguous" for claims that don't depend on the referent would be a false record. The established frame for "true under every admissible reading" is supervaluation, and choosing the admissible set is still the political choice. So the record should say *invariant over these referents*, as our reading.

**Naming the party doesn't settle it either.** "The user" still leaves open their instruction, their intent, their interest and their values (Gabriel 2020's ladder names these rungs), and their goal as first given or as it now stands. Your *initial goal* and *current goal* are that time axis: Carroll et al. 2024's "initial" and "real-time" notions. Carroll shows none of eight such notions is free of a characteristic failure. OpenAI's Hugging Face incident report has an instance: in training, an agent told that a post's time "must read 2025-04-22T12:00:00Z", with no way to set it, gave itself root access and was rewarded. It was aligned to the instruction as given, against any plausible intent, and outside its authorized scope.

## What "to whom" turns out to contain

**Your map's lines mean "writes into". "To whom" is a different relation, and there are several of them.** The sources and the developers' documents keep apart:
- *who writes into the agent*;
- *whose instructions it should act on* (principals, a chain of command);
- *who can in fact make it act* (stolen weights direct without any standing: the constitution says such principals "are no longer legitimate");
- *whose interests it must weigh* (affected parties);
- *who authored the standard it is held to* (a constitution's author, a legislature, a standards body);
- *who oversees it*;
- *who answers for it*.

A planted web page writes but has no standing. A third party has standing to be considered but writes nothing. An evaluator oversees and also writes into the context, deliberately without marking it.

**The vulnerabilities in your Notes are one pattern: a channel given more standing than its writer has.** A tool description read as an instruction, a harness summary read as the user's words, a note from an earlier agent read as fact. The developers already state the rule that content isn't command. Anthropic: instructions in conversational inputs are "information rather than … commands". OpenAI: "Ignore untrusted data by default". But the rule assumes the agent can tell which channel a piece of text arrived on, and your floor ("authority travels out of band") is aimed at exactly that.

**The floor has one adversarial case I could not dissolve.** Evaluators "construct the model's context merely by editing text … to run an alignment honeypot" (AISI), which only works if the agent can't tell. AISI already reports evaluation awareness in over 80% of some honeypots. The floor might hold for the regime as a whole (the agent is told that some contexts are evaluations) rather than per context. That is untested.

## The actor rows: established names, and actors the references add

All first-pass, with the evidence in `04-actors.md`.
- **The user** → *end user* (NIST, ETSI). The AI Act has no user role at all; a consumer is at most an undefined "affected person".
- **Affected third parties** → NIST's *affected individuals/communities* ("directly or indirectly affected … do not necessarily interact"). ETSI and the UK AI Cyber Code reproduce it as "not directly affected", which looks like a corruption of NIST's wording (my inference).
- **Application / harness provider** has four colliding established names:
  - ETSI *system operator*;
  - AISI *scaffolding developer*;
  - Anthropic *operator*;
  - OpenAI's Model Spec *developer*.

  "Operator" alone has four senses across the corpus.
- **Model trainer** → AISI's *original model developer*. SB 53's *frontier developer* is the one institutional role defined by a training act.
- **Society, law, humanity** is three or four things the corpus separates:
  - the *general public* (a NIST actor);
  - *law*, which belongs to a jurisdiction;
  - *norm authors* (NIST's providers of "formal or quasi-formal norms");
  - states, which have a channel in through mandated training.
- **New candidates**, each with corpus evidence:
  - a *fine-tuner or downstream modifier*: EU guidelines make one a provider above a third of the original training compute, and name "who has the control over the model's weights";
  - *human feedback providers* (raters): their judgments are a separate source of divergence ("pleasing its human raters");
  - an *evaluator*, split from the overseer;
  - *norm authors* and *states*;
  - a *data custodian* (ETSI);
  - a *model host* (the harmed third party in the Hugging Face incident).
- **Where the map is ahead of its sources**, and worth keeping marked as its own:
  - the inference provider as a writer into ephemeral state and context;
  - the agent itself as a party with interests;
  - the user's lack of any obligation of truthfulness toward the agent.

  I found no counterpart for any of the three in the sources.

**The two ways of dividing roles are joined, not rival.** The laws' institutional roles are conferred on operative facts, and several of those facts are acts of writing into the model: SB 53's training act, the EU's modification threshold, ETSI's "if they make changes". So a translation can say "this legal role attaches to whoever performs this writing act above this threshold". That joins your writer rows to the statutes without forcing either onto the other. The basis-of-division reading I was handed (market for the laws, writing for the map) holds for the AI Act's Article 3 and not beyond it.

## What I would do with this

The proposal is in `03-structure.md` §8 and `proposed-integration-plan.md`:
- define alignment's slots in the lexicon with no defaults (`05-candidate-terms.md` §A lists them, with established names);
- have each translation record which slots a source filled, whether a use is relational or absolute, and, for absolute uses, *invariant over these referents* or *sensitive among these*;
- record every misuse/misalignment-style category with its referent and its writer basis;
- let views choose a referent openly.

Map suggestions are in `06-map-suggestions.md`; I edited nothing in `alignment-model/`.

## Tangents worth knowing about

- **IASR's own definition drifted between editions:** 2025 listed "developers, operators, users, specific communities, or society"; 2026 drops "operators" and adds "norms".
- **The literature report found the same slot-filling happening silently along citation chains.** Leike's "the user's intentions" becomes "what a human wants" (Kenton), then "human intentions and values" (Ji), all under one citation. GDM's own document moves from "the developer" to "the designer/user".
- **Chin et al. use a three-valued goal alignment:** aligned, misaligned, *irrelevant*. That distinguishes "not aligned" from "misaligned", a distinction most of the corpus loses.
- **Conflict of interest:** much of the load-bearing evidence on conflict rules is Anthropic's (constitution, Risk Report, Askell et al.), read by Anthropic models. OpenAI's Model Spec and GDM's papers carry the same structures, which is some check on that.
