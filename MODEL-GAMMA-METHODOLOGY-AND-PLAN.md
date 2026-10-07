# Model gamma: methodology and plan

*A proposal for the third iteration of the AI risk model. Drafted 2026-10-06 by Claude (Opus 5.5), working with Joseph Wecker, for Joseph first, then for the agents who will write the lexicon and the per-source translations, and for anyone reading the public repository who wants to know how the model is being built and why.*

*Nothing here is ratified. Everything is a proposal, argued on its merits; the open decisions are collected in section 5.*

*The established vocabularies cited below were researched for this document on 2026-10-06 by three agents, whose full reports (with verbatim quotations, links and a verification mark on every claim) are in `influx/gamma-research/`. Where a claim here rests on one of those reports rather than on my own reading of the primary, it says so. Section 8 lists what I read myself.*

---

## 0. In one page

**The aim** (from `CLAUDE.md`, unchanged): a consolidated map of the frontier-AI risk landscape, built from what the field's own risk assessments, safety frameworks, laws and research claim, held with high fidelity to those sources and expressed in a rigorous shared vocabulary of our own, so it can be projected by cause, control, event, impact, who is affected and who decides. That summary sentence leaves out the response side that Joseph's chain in the same file includes (mitigation, recovery, resilience), and the corpus adds further axes; `influx/competency-questions-draft.md` lists thirteen.

**What the first two attempts taught.**
- **Model alpha** cross-walked the sources' risk factors into one master list. Disagreements had nowhere to go except prose.
- **Model beta** built a claim-backed causal graph (287 concepts, 573 relations, 943 claims). Its terms were written before any source was mapped, and they ended up adopting one source's definitions wholesale.
- **Both** put the sources' claims into our structure before the sources' words had been translated into our vocabulary. That is the step this iteration reorders.

**The method, in four moves:**
1. **Lexicon first, with method terms before domain terms.** The method terms come from domain-driven design, Joseph's address theory, terminology science, speech-act theory, argumentation and norm theory. The domain terms are built as Joseph put it on 2026-10-06: the union of the most precise, scoped definitions, with umbrella terms that contain them. Terms live in namespaces, so `ddd:context` and the agent part *context* never share a name.
2. **One translation per source**, from its words into ours. At the term level it says what the source's word probably means here, with a rationale. Where a word's meaning shifts inside a source, a resolution record says which meaning it had there, ambiguity included.
3. **Assertions** recorded in our terms, with each source's words verbatim beside them, its voice kept nested, and its own hedges intact.
4. **Views** computed from those records, never maintained by hand. Which views earn a place is decided by the questions the model must answer, not chosen in advance.

**What is new in this draft:**
- **Many of model beta's coinages have established names**, including the load-bearing ones. Established vocabularies fit the problems model beta solved with coinages, and adopting them gives a better theory, not only better words (section 3).
- **The actor and agent-part vocabulary comes first among domain terms.** That is Joseph's priority; it is the vocabulary that dissolves "developer" (section 3.9).
- **Competency questions**, written up front, are the model's requirements and its final test. Lexicon acceptance tests sit under them (section 3.11).
- **Refinement is budgeted.** Lexicon entries get repeated truthification passes before anything downstream relies on them (section 2).
- **Translation is treated as coding**, with two independent translators per pilot source (section 4, G4).
- **A plan in eight phases** says who does what, who reads it, and how each phase is known to be done (section 4).

**Decisions for Joseph** are collected in section 5, each with a recommendation and its confidence.

---

## 1. Where we are

### 1.1 Model alpha (2026-09-26 to 27): a crosswalk

`influx/model-alpha.md` is a report: a "unified master list" of risk factors (hazards; model and system factors; structural and organizational factors) cross-walked against about fifty sources. Each cell carried a source tag (primary, secondary, web-fetched, unverified, commentary), a role code (hazard, risk factor, trigger, mitigation, indicator, observation) and a force code (law, commitment, example, recommendation, …).

- **What held:** the discipline of verbatim quotes with locations, the source tags, and the role and force codes. All of these survive into this plan.
- **What broke:** a crosswalk forces one row per item, so the row's wording is the synthesizer's. Where sources meant different things by the same words, the difference went into §5 of the report ("Where sources disagree, or use one word for different things") as prose, outside the structure.

### 1.2 Model beta (2026-09-27 to 28): a claim-backed causal graph

`influx/model-beta/` has signed quantities, relations between them, and claims anchored to passages, plus a draft lexicon in udon (`terms/*.ud`, 72 terms in 14 groups) and a schema proposal (`SCHEMA-SYNTHESIS.md`, draft 2).

- **What held:**
  - the claims ledger;
  - the lexicon's pooling checks;
  - the address-theory idea that a source's term *resolves* to ours with a recorded outcome, which can be "ambiguous";
  - draft 2's two planes (what was said; what it is said about) joined by resolution.
- **What broke:**
  - Relations were chosen first and claims hung on them, so a word like "developer" came to mean "a lab" across about forty concepts.
  - Loop enumeration consumed attention (641,083 loops before one edge was recast, about 186,000 after; `notes-mp.md` item 8) without producing findings that outlasted it.
  - The lexicon adopted IASR 2026's definitions directly ("The first four definitions are IASR 2026's, adopted", `def-risk.ud`). That was a reasonable early move. In domain-driven design's terms, though, adopting a source's definitions wholesale is the *conformist* pattern: our lexicon takes one upstream source's model as its own, which the translation step is meant to prevent.
  - Risk analysis was being built at the same time as the lexicon it depended on, without the discipline to keep the two concerns apart. The result began to read as its own ball of mud.
- **How gamma uses it:** for ideation only. Model beta's claims carry verbatim anchors, but none of its terms, concepts, relations, mappings or schema draft 2 have had an independent double-check. Anything taken from it is re-derived against the primaries and re-owned, never carried over verbatim.

### 1.3 What the corpus turned out to be

These findings shape the method. Each was established in the source models (`influx/source-models/`, summarized in `OVERVIEW.md`) and, where marked, checked again for this draft.

1. **The sources model different objects, not one object differently.** In OVERVIEW's words there are five kinds of model:
   - a landscape of risks (IASR, MIT, CAIS, the UK Chronic Risks Analysis);
   - a developer's go/no-go gate (the company frameworks);
   - an organization's management process (NIST, the EU Code's process layer);
   - a national scenario set (the UK National Risk Register);
   - a measurement programme (UK AISI).

   A translation has to carry *which kind of model* a claim came from.
2. **Much apparent agreement is copying.**
   - The EU Code's loss-of-control formula ("reliably direct, modify, or shut down") recurs in nine later documents.
   - California's ">50 people or $1B" threshold recurs in four, under two names.
   - Shanghai AI Lab says its glossary is "primarily based on" IASR 2025's.

   Agreement counts only as far as lineage allows.
3. **Some sources are looser than we will be; some are stricter.** I read SB 53 whole. Its definition of "catastrophic risk" (§22757.11(c)) is one sentence carrying at least seven separable concepts:
   - a knowledge standard ("foreseeable") and a materiality standard ("material");
   - the conduct it attaches to (a frontier developer's "development, storage, use, or deployment");
   - a causal standard ("materially contribute");
   - a casualty threshold and a dollar threshold;
   - a counting rule ("arising from a single incident");
   - a closed list of conducts;
   - exclusions, one of them a counterfactual baseline ("otherwise publicly accessible").

   The lexicon must be able to say each of those separately, or the translation loses the source's precision.
4. **Sources declare their own rules for reading their terms.** From the EU Code's interpretation clause and glossary (read for this draft):
   - "the AI Act definition applies, and such definition shall prevail";
   - "all grammatical variations of the terms defined in this Glossary shall be deemed to be covered";
   - interpretation is to be "purposive".

   SB 53 §22757.14 requires an annual review of whether "frontier model" still reaches "foundation models at the frontier". It weighs whether coverage can be determined before training and is "verifiable by parties other than the frontier developer". These are resolution policies in address theory's sense, written by the sources themselves.
5. **Terms are scoped finer than documents.** SB 53 defines "catastrophic risk" twice: §22757.11 says *frontier* model, Labor Code §1107 says *foundation* model, and the two versions' first kind of critical safety incident differ too. IASR 2026's glossary and body define loss of control differently.
6. **Some sources are not internally consistent, and say so.** Anthropic's August 2026 Risk Report: "We acknowledge that the distinction between known and unknown is not crisply defined." MIT's causal taxonomy uses a single "Other" level for three different things (section 3.3). IASR 2026 is inconsistent with itself on several key terms.

---

## 2. Principles

**Carried from `CLAUDE.md`:**
- compilation, not adjudication;
- fidelity: every claim anchored to a verbatim passage with its location, and our reading attributed as ours, beside the source's words;
- soft evidence stays in, marked;
- vocabulary first;
- correlation is not corroboration;
- conflict of interest stated plainly (much of the work is done with Claude models; Anthropic appears in the evidence in both directions).

**Added since:**
- **The lexicon's shape.** *Joseph, 2026-10-06*, agreeing with an earlier suggestion of mine: the lexicon "will out of necessity and also my preference be the union of all the most precise, scoped, bounded, and/or specific definitions (with some umbrella term containment as appropriate etc.)". In practice:
  - no source's precision is ever lost in translation;
  - broader terms exist as declared umbrellas that *contain* the precise ones, never as replacements for them.
- **Priority.** *Joseph, 2026-10-06*: "One of the high priorities for me are our agreed-upon definitions for those actors (and agent parts) listed in the alignment-model/ directory."
- **Refinement is where the value is.** *Joseph, 2026-10-06*, on the address-theory entries, the one lexicon in his work that became genuinely useful: they took "multiple truthification passes until almost every line had been severely scrutinized for coherence and completeness … the value really only settles in during the last 5-10% of the refinement. First pass and lazily generated stuff, even from ample context, will be more likely to seed confusion and misunderstanding than truthful analysis and understanding." In practice:
  - the lesson is the *cost*: even a handful of entries took an astounding amount of work, so every entry needs that kind of effort budgeted. It is not a limit on how many entries the lexicon has;
  - every agent-drafted entry is a candidate until it has had repeated line-by-line passes;
  - downstream work (translations, assertions) does not lean on an entry as settled before then;
  - the address-theory entries are the quality bar.
- **Established vocabulary over coinage** (Joseph's standing rule elsewhere in his work: "a coinage where an ancient word exists is a smell; a coinage where there is established academic vocabulary to adopt is a smell"). The rule cuts both ways, so also: **don't borrow an established word in a different sense.** Section 3 lists the collisions this draft found.
- **Neutrality lives in the assertions, not the vocabulary.** The lexicon is our model (Evans: "a change in the language is a change to the model"). It is judged by whether it can express every source's distinctions without loss, not by whether it looks neutral. Compilation-not-adjudication governs what we say the sources claim.

---

## 3. The method

### 3.1 Two directions of work, and the established names for them

Terminology science distinguishes two directions:
- **onomasiological** work runs from concept to name;
- **semasiological** work runs from a word in use to the concept it denotes.

The project needs both:
- **The lexicon is onomasiological.** ISO 860 says it almost word for word: "Harmonization starts at the concept level and continues at the term level". In ISO 704's order of analysis, "assigning a designation to the concept" comes last. Both are read in the official previews (`gamma-research/terminology-mapping-provenance.md` §1). So **settle the concept, then choose its name.** This is how the "hazard" and "developer" decisions should be made (sections 3.8, 3.9).
- **The per-source translations are semasiological.** They start from a source's word in its scope and ask which of our concepts it denotes. Temmerman's critique of concept-first terminology (2000) argues exactly that real special languages need both directions, and that polysemy and drift in them are normal, not defects. That describes this corpus.
- **We do not harmonize the sources with each other.** ISO 860 says harmonization is likely to work where a field "is well established and relatively stable" and "has a tradition of standardization". Frontier-AI risk is neither, which is a citable reason for compilation-not-adjudication: we map each source onto ours and leave them unreconciled with each other.

### 3.2 The vocabulary for the method itself

Two vocabularies do two jobs. The seam between them should be explicit in `def/`.

**Domain-driven design (Evans, *DDD Reference*, CC BY 4.0, in `ref/`) supplies the strategy:**
- *bounded context*: "A description of a boundary (typically a subsystem, or the work of a particular team) within which a particular model is defined and applicable";
- *context*: "The setting in which a word or statement appears that determines its meaning";
- *ubiquitous language*;
- *context map*: "Map the existing terrain. Take up transformations later.";
- the relationship patterns:
  - *conformist* ("slavishly adhering to the model of the upstream team"): xAI adopting the Code's terms; the Code's "AI Act definition shall prevail"; New York's RAISE Act copying SB 53's definitions word for word;
  - *shared kernel* (a subset of the model the teams "agree to share", changed only "with consultation"): no clear case among the sources yet;
  - *published language*;
  - *anticorruption layer*: "create an isolating layer … in terms of your own domain model".

  Two patterns don't fit the cases they might seem to. *Separate ways* ("no connection to the others at all") is not the RSP's "plain meaning" "catastrophic": that is one deliberately unbound term in a well-connected document, and the resolution outcome *deliberately unbound* names it better. *Big ball of mud* ("Do not try to apply sophisticated modeling within this context") is the opposite of what self-inconsistent sources need. Those are best treated as several scopes under one cover and mapped scope by scope, which is finding 5 applied.

**Joseph's address theory supplies the mechanism.** Its entries are in the public repository `v2-io/udon`, at `v2/references/def/` (cited as of commit `90f4fb6`, 2026-08-27): <https://github.com/v2-io/udon/tree/90f4fb6/v2/references/def>.
- *reference* and *referent*, with *intended cardinality*;
- *binding* (minted and maintained by a *maintainer*) vs *match* (a test run at use);
- *scope*, with containment edges: the unit within which bindings are kept and collisions counted, which makes it the natural *namespace*;
- *resolution* from an origin, as of a moment, with its path, under declared admissibility and preference;
- *ambiguity* as an outcome, not an error;
- the failure modes: a binding *dangles* when it no longer reaches a referent, and *collides* when one maintainer mints the same name twice in one scope.

DDD's bounded context is flat; the sources' scopes are nested (finding 5), so **bounded context should be defined in terms of scope.**

**Proposed:** import address theory's terms *by reference*, not by copying, so the two stay one vocabulary. Since Joseph maintains both, this is a shared kernel in Evans's sense (agreed, changed only with consultation), not a conformist relation to an outside upstream.

**Naming collisions in our own method vocabulary** (from the research reports, §9 and §10 in each):

| Our word | What it already means elsewhere | Proposed handling |
|---|---|---|
| **context map** | Evans: the map *across* all contexts and their relationships | Use Evans's sense for the across-sources map: the catalog plus lineage. Call the per-source document a **translation** (the inside of an anticorruption layer). *Joseph's call.* |
| **designator** | ISO 1087 lists it as an admitted term for *designation*, a sign for a concept; `def-match.ud` uses it for a reference that reaches its referent through a binding | Keep address theory's sense; record the ISO sense as a collision in the entry |
| **primary** (source) | W3C PROV: a historian's primary source; the repo's `channel: primary` means "read by us in the source itself, not via a relay" | Rename the channel value; PAV's *retrieved / imported / derived / accessed* ladder fits it (section 3.5) |
| **broad / narrow** | SKOS: `<A> skos:broadMatch <B>` means *B* is broader | See section 3.4: model beta's mapping files use the opposite direction |
| **qualifier** | Toulmin: the force of one inference ("presumably") | Use Toulmin's narrow sense, or a different word for draft 2's bundle |
| **norm**, **commitment**, **assertion**, **argument**, **declaration**, **exemption**, **rebuttal** | each has several established senses (section 3.6) | each lexicon entry names the sense it takes and lists the others under "not to be confused with" |

**Namespaces.** Our method words also collide with our own domain words, inside the one lexicon:

| Word | Method sense | Domain sense | Elsewhere |
|---|---|---|---|
| **context** | DDD's context (G1) | the agent part in `alignment.md` ("experience & agency") | Institutional Grammar's and GSN's Context; ordinary use |
| **model** | DDD's domain model | an AI model | "source model", "model gamma" |
| **source** | a source document | a *risk source* (SRA, ISO) | FactBank's nested source; SP 800-30's threat source |
| **role** | Goffman's production roles; "stage is a role relative to a focal event" | actor roles, functional and institutional (section 3.9) | model alpha's role codes |
| **scope** | address theory: where a binding holds | a source's declared coverage (what it is about) | |
| **agent** | the agent that made a record (PROV, SSSOM) | an AI agent | |

**Proposed:** every term lives in a declared namespace, which is address theory's *scope* used for exactly its purpose. For example `ddd:context`, a namespace for the agent parts (`agent:context`, name open), and the ordinary word left unprefixed. Where a source's own word is meant, the source's namespace is used. "Coverage", not "scope", is used for what a document is about.

### 3.3 The lexicon

**Form.** udon term groups in `def/`, in the house style of the address-theory exemplars:
- a narrative opening that introduces the group's terms in relation to each other;
- one-line definitions;
- relations with cardinalities;
- invariants;
- discussion, examples and working notes;
- `:synonyms` and `:avoid`.

The format is udon, per `CLAUDE.md`.

**What terminology science adds to the house style.** From ISO 1087 and ISO 704, read in the previews:
- **Intensional definitions**: the immediate broader concept plus the *delimiting characteristics* that separate this concept from its neighbours. Reading a term's `|invariants` as its delimiting characteristics makes "not to be confused with" mechanical rather than discretionary.
- **Acceptability status for names**: preferred, admitted, deprecated. udon's `:synonyms` and `:avoid` already approximate admitted and deprecated.
- **Adopted definitions carry ISO's own marking**, `[SOURCE: …, modified — what changed]`, so a definition we take from a source says where it came from and what we changed.

**What the address theory adds that terminology science lacks:**
- **time**: ISO's concept is static, while deictic definitions ("today's most advanced models"; the EU's moving "high-impact capabilities") need an as-of index;
- **ambiguity as an outcome**: no mapping standard the research checked (SKOS, SSSOM, OntoLex, Web Annotation) can say "one of these, undetermined".

**Status per term.** The decided-by vocabulary Joseph already uses in `udon/v2/references/DECISIONS.ud` fits:
- steward;
- ratified;
- council;
- supported;
- defacto;
- proposed;
- transition.

*Proposed* is the default for everything an agent drafts.

**Umbrellas and deliberate ambiguity** (per the lexicon shape Joseph stated, section 2). An umbrella term is declared as containing named precise terms. Where a word is genuinely used in several incompatible senses, the lexicon says so as a *declared ambiguity* with its candidate senses named. It does not pick one silently.

**The test that makes the difference concrete.** MIT's AI Risk Repository is the largest shared-vocabulary effort in the corpus (1,725 risks from 74 documents), and I checked its causal taxonomy at the source (Table 1):
- *Entity "Other"* means "The risk arises from human-AI interaction rather than either agent alone, or the causing entity is ambiguous or unspecified". That is a real category (interaction) merged with a resolution outcome (ambiguous) and with a source's silence (unspecified).
- *Timing "Other"* merges "across both pre- and post-deployment phases" with "presented without a clearly specified time".
- MIT reports its Entity "Other" at 21% of coded risks.

Our lexicon should never contain a category that merges a thing in the world with a fact about our reading.

**What the lexicon holds from the start, and what it leaves out.** The test for including something early is whether we need it to *describe what the sources say* without loss. Analysing risk is a separate concern, a separate bounded context built on top of the lexicon later.

*In from the start:*
- **The method terms** (section 3.2): DDD's strategic terms; address theory's terms; the terminology-work terms; the evidence-plane terms (passage, assertion, nested voice, strength, attack, norm-proposition).
- **What address theory implies for every term about a source's words:**
  - whether a source term is *bound* (the source defines it and maintains the definition: SB 53's "frontier developer", with a statutory annual review) or a *match* (used undefined, so it reaches whatever fits the reader's understanding at the time);
  - its *intended cardinality* (SB 53's "frontier developer" stands for any number of persons; a named incident for one);
  - who *maintains* it, and when it is meant to be re-resolved;
  - the *as-of* moment of every resolution;
  - the failure vocabulary: a source definition that *dangles* (its test no longer reaches what it was meant to, which is what SB 53 §22757.14 guards against) or *collides* (the same name defined twice within one scope; IASR 2026's two wordings for loss of control, in its glossary and its body, are a candidate if the body's wording counts as a definition).
- **Actors and agent parts** (section 3.9).
- **The risk components the sources' own definitions are built from** (section 3.8): source, cause, event, harm, magnitude, likelihood (with what it is a probability *of*, and its window), confidence, exposure and vulnerability, controls; plus intent and recoverability. These are needed to translate a definition such as SB 53's "catastrophic risk" without loss.

*Left out until later, and built on top:* signed causal influences, loops, bow-ties, and any graph structure that analyses how risk behaves. Those are *our* model of risk, our claims, and they get their own context once the lexicon and translations can carry them.

*Deferred:* whether a single high-precision formal object (Kaplan & Garrick's scenario triplets are the strongest candidate) underlies the risk readings. Some readings in the corpus don't reduce to it (section 3.8), so it wants its own spike later rather than being built in.

### 3.4 Per-source translations

Each main source gets one translation document: its terms mapped into ours, under its own scopes. It works at two levels, and the research found that the standards cover only the first.

**Type level: what this source's word means in this source.** One row per sense the source uses. The established shapes:
- **OntoLex-Lemon** (W3C Community Group report, 2016): a *lexical entry* (the source's word) has *lexical senses*, each "a reification of a pair" of word and concept, to which "usage conditions" attach. A translation row is a lexical sense of a source's word whose *reference* is our concept.
- **SSSOM** (Matentzoglu et al. 2022) gives the row's fields:
  - the subject as a bare label;
  - the predicate (a SKOS match), with a `Not` modifier;
  - "no term found" for a gap in our vocabulary;
  - a required *mapping justification* (including `ManualMappingCuration` and, on the current main branch, `AgentBasedMatching`);
  - separate author, creator and reviewer;
  - our confidence, kept apart from the source's own hedge.

**Resolution within a source: why, and how much.** A word's meaning can shift inside one source. IASR 2026 uses "developer" for organisations in one place and for individual people in another, and SB 53 defines "catastrophic risk" separately, and differently, in two of the codes it amends. When an assertion is recorded, we need to know which meaning a word had *there*. SSSOM says outright that "Mappings themselves have no context (i.e. are always true)", so the type-level row can't carry this.

**The selection rule.** Recording every use is infeasible: IASR 2026 alone has about 1,200 raw uses of the heavily loaded terms (count by the de novo review, including cited titles). So:
- each scope (a document, section, code section or table) gets one *default* resolution of each key term, recorded once;
- a separate record is made only where a use departs from its scope's default, or where the use sits inside an assertion we record.

The heavily loaded terms are about a dozen: catastrophic, severe and systemic risk; loss of control; (mis)alignment; safeguard; hazard; developer, provider and deployer; threshold; incident; frontier.

**What a resolution record carries:**
- **an outcome**, in address theory's terms: zero, one, several, or ambiguous among named candidates, read against the term's intended cardinality;
- **a reason**, with whose fact it is:
  - facts about the source: withheld, delegated to the reader, defective as written, deliberately unbound ("plain meaning"), declined, or imported from an outside institution (California law for "foreseeable");
  - a fact about our lexicon: no term of ours fits yet;
  - a fact about our reading: we can't tell which candidate is meant;
- **the path** (glossary, section definition, imported binding, inline, our reading);
- **who resolved it**: us, the source itself, or a third party (IASR resolves the EU's "systemic risk"; Anthropic's FCF files RSP thresholds under the statutory "loss of control");
- **an as-of date**, for deictic terms;
- for relational terms, **the reference standard and the bearer** ("aligned with what, borne by what").

Keeping outcome and reason apart is the MIT "Other" lesson applied to our own records. The record's format is ours to define (G1).

**The broad/narrow direction needs deciding now.** It was found in research and checked against the repo:
- `def-actors.ud` gives the legend all of model beta's term files use: "Match, from the source's term to ours: … broad (theirs is wider)".
- In SKOS and SSSOM, with the source term as subject, `broad` means *ours* is broader.
- So beta's *broad* is SKOS's *narrowMatch*, and vice versa. That covers 46 and 70 rows in `mappings*.yaml` and about 31 and 28 in `terms/*.ud`.
- The usage is consistent inside the repo, so no row is wrong as written. An export to SKOS would flip every one.

**Proposed:** adopt the SKOS/SSSOM direction for gamma and say so in one line; beta's files stay as they are. A second, smaller trap: ISO 1087 notes that the *broader* concept has the *narrower intension*. "Wider" should be said once to mean extension.

### 3.5 Passages: anchoring the source's words

The fidelity atom is the passage. The W3C Web Annotation Data Model (Recommendation, 2017) already defines robust anchors:
- a *TextQuoteSelector* (exact text plus a prefix and suffix);
- a *TextPositionSelector*;
- *refinedBy*, for a narrower selector applied inside a wider one;
- several selectors for one passage, "to maximize the chances that it will be discoverable later".

**Proposed anchor:** the PDF page (RFC 8118 `page=N`), refined by a quote selector, with the extraction line number kept as an optional position, and the document version as read.

**Address theory adds one thing the W3C spec gets wrong for our purposes.** The spec says several matches of a quote "SHOULD be treated as matching all". A passage anchor intends exactly one match {1,1}; three matches means the anchor narrowed too little, and that should surface, not widen silently. **Record the match count when anchoring and on every re-check.**

**Tables are the gap.** No standard addresses a PDF table's row and column, and most framework thresholds live in tables that `pdftotext -layout` interleaves. That selector is ours to define.

**Extraction condition.** PAV's ladder fits what the repo already distinguishes:
- the relata PDF is *retrieved*;
- the `pdftotext` text is *imported*, PAV's own example being OCR'd text;
- an assertion record is *derived*;
- our reading is *accessed*.

`bin/extract-text` regenerates the imported layer.

### 3.6 Assertions: the established vocabulary for what sources say

Draft 2 of the schema rebuilt, under its own names, most of what speech-act theory, argumentation theory and norm theory already provide. The second research report (`gamma-research/speech-acts-argument-norms.md`) read most of these at the primary. Its findings, with my proposals for gamma:

**The act.** Searle's taxonomy of illocutionary acts (1975 chapter, read whole by the research agent):
- **The five points**:
  - *representatives*: commit the speaker to something's being the case ("assertives" from 1979);
  - *directives*: get the hearer to do something;
  - *commissives*: commit the speaker to a future course of action;
  - *expressives*;
  - *declarations*: bring about what they state by being performed.
- **Strength is separate from point.** "I suggest" and "I insist" share a point at different strengths; "hypothesizing that p and flatly stating that p are in the same line of business". So "speculates" is not a different stance from "asserts"; it is the same act at a lower strength.
- **Mode of achievement** ("to testify is to assert in one's capacity as a witness") is the established slot for "who, in what capacity".
- **Indirect force** is the established name for draft 2's "grammatical mood is not a safe guide" (NCSC writes norms in the indicative).
- **Definitions are declarations, of two kinds.**
  - *Institutional* declarations create a status in an institution: a statute defining "frontier developer" changes every obligation that uses the term.
  - *Linguistic* declarations fix a word within a text and need no institution. Searle names "I define, abbreviate, name, call, or dub" as the exception: "I consider them an auditor for the purposes of this article" is one.
- **Determinations are assertive declarations.** A Commission designation, a company's capability-threshold determination or a court finding is truth-apt *and* status-creating. In Hart's words it is "final but not also infallible". The record can hold the determination as effective and another source's claim that its content is false, without contradiction.

**Whose voice.** Several established frames name parts of draft 2's "nested voices stay nested":
- **FactBank** (Saurí & Pustejovsky 2008, read at the primary) records factuality as ⟨modality, polarity⟩ *relative to a source*. The author is always the outermost source: "Izvestiya according to the author", not Izvestiya.
- The **Penn Discourse Treebank** attribution scheme separates:
  - claims ("X says");
  - beliefs ("X thinks");
  - facts presupposed ("X found that");
  - an arbitrary source ("reports suggest").
- **Goffman's** animator, author and principal (1979, read via a secondary that quotes him) is draft 2's authorship-roles table. The corpus splits his *principal* further: IASR's Chair holds "ultimate responsibility" for a report that "does not necessarily represent the views of the Chair".
- **Evidentiality** in the linguist's sense is grammatical, and English has none. It is also distinct from epistemic modality (how sure, as against how known). Draft 2's first stance question mixed the two.

**Proposed:** decompose draft 2's stance into point plus strength (Searle), factuality relative to each nested source (FactBank), and argument relations (next item).

**Arguments and contests.**
- **Three kinds of attack, not two.** ASPIC+ (Modgil & Prakken 2013, read at the primary) has *undermining* (a premise), *rebutting* (the conclusion) and *undercutting* (the inference). The handoff's todo asked for "rebutting vs undercutting"; draft 2's premise-attached "defeats" was undermining all along. The safety-case literature (SEI's eliminative argumentation, 2015) uses all three.
- **Attack is not defeat.** An attack is a fact about what was argued. Defeat needs a preference ordering, which is adjudication. So we record attacks, typed. A contest's *standing* (from Joseph's logos atom design: refuted, burden-shifted, standoff, open, conceded) is recorded as some party's attributed assertion about the contest, or computed as a view under a declared ordering. It is never a field we fill.
- **The architecture already exists.** Inference Anchoring Theory and the Argument Interchange Format anchor an argument graph *in* the speech acts that carry it. That is draft 2's two planes, already built.
- **Other established names:**
  - OMG's Structured Assurance Case Metamodel (SACM 2.2, read at the primary) gives a standard list of assertion statuses (asserted, needsSupport, assumed, axiomatic, defeated, asCited) and treats a support link as itself an assertion that can be challenged;
  - Toulmin's *warrant* and *backing*: a source's methodology is the backing for a family of its warrants, which ties our "methodology" column to the argument layer;
  - Walton's argumentation schemes, with their critical questions, for expert opinion (checked via a secondary source) and analogy (from memory only; analogy is the commonest argument form in one family of sources);
  - *linked* vs *convergent* premises, for draft 2's "conjunctive / convergent".

**Norms.** Draft 2 defined a commitment as "a norm where imposer = bearer". Searle tried that assimilation and failed: a promise commits the speaker, a request tries to get the hearer to act. The established layering, each layer named:
1. **The act**: directive, commissive or declaration, with strength (Searle).
2. **The institutional statement's grammar**: Institutional Grammar 2.0 (Frantz & Siddiki, codebook read at the primary), a coding grammar already applied to legislation.
   - *Regulative* statements have: attribute, deontic, aim, object, context (split into activation condition and execution constraint), and "or else".
   - *Constitutive* statements have: the constituted entity, a constitutive function "including the conferral of status", and constituting properties.
3. **The positions it creates**: Hohfeld (1913, read at the primary).
   - First order: claim–duty, privilege–no-right.
   - Second order: power–liability, immunity–disability.
   
   "Leadership can … make decisions without the SAG" is a power plus an immunity, which an obligation-strength ladder cannot express. Hohfeld also makes every duty ask *who holds the correlative claim*. For a voluntary framework the honest answer is often "no one with a legal claim", and that is the materiality question the sources keep asking.
4. **Its legal status over time**: LegalRuleML (OASIS Standard 2021) has applicable, in force, efficacy and valid, with status-changing events, and *strong* vs *weak* permission. Most framework deployment conditions are strong permissions (derogations from a prohibition the same document sets).
5. **What we record about all of the above**: *norm-propositions* (von Wright, *Norm and Action*, read at the primary). A norm is neither true nor false; a report that a norm exists is. This is compilation-not-adjudication in deontic logic's own terms.

**Collisions to note:**
- Hohfeld's "exemption" means immunity, not draft 2's derogation;
- Institutional Grammar's "norm" means a statement without a sanction, not the umbrella.

**A worked consequence** (the research report's reading; I checked the sentence it rests on). IASR 2026 declares that it makes no recommendations, yet says: "To avoid catastrophic harm, developers of open-weight models should not release models without evaluating risks" (`ref/iasr-2026-full.md`, line 2077). That is von Wright's *technical norm*: if you want an end, you ought to do X. It presupposes an *anankastic* statement, that evaluation is a necessary condition, which is truth-apt and fits a descriptive report. Draft 2 treated this as a conflict; it becomes a typed ambiguity between a technical norm and a prescription.

### 3.7 Lineage and corroboration

**The established relations cover most of draft 2's lineage table** (`gamma-research/terminology-mapping-provenance.md` §6.5 maps each row):
- **W3C PROV:** derivation, revision, quotation, invalidation, alternate.
- **PAV:** retrieved, imported, derived; authored, curated, created.
- **CiTO:** cites as authority or evidence; contains an assertion from; includes a quotation from; qualifies; updates; corrects; retracts; shares an author or funder with.
- **IFLA LRM:** Work, Expression, Manifestation. These cover "same text, several publishers", "one finding in two renderings", and one relata key holding several documents.
- **Akoma Ntoso and the schema.org legislation terms:**
  - amends and repeals;
  - force vs efficacy (in force, as against applies from);
  - `termModification` and `authenticInterpretation` (a change in what a term means).

**What remains ours:**
- the direction of drift (a hedge dropped, a claim hardened);
- a summary that adds content;
- boilerplate within one document;
- "tasks → fulfils";
- "orders revision of";
- announcement status of a change;
- preemption across jurisdictions.

**Two rules for the corroboration view:**
- **Never inherit transitivity.** `skos:exactMatch` is transitive, and so is the micropublications model's *supports*. A corroboration view built on either propagates agreement down chains, which is the inference lineage-awareness exists to block.
- **Keep two axes.** The intelligence "Admiralty" grading separates source reliability from information credibility, and defines its top credibility grade as "confirmed by independent sources". If we grade sources at all, the grade is our attributed assertion, on two separate axes.

**Claim identity is an assertion.** The micropublications model (Clark et al. 2014): "identification of statements as being similogs is itself an assertion. Your 'similarity' may not be my 'similarity'." When we say two passages make the same claim, that judgment is a record with an author, not a merge.

### 3.8 The risk side

The third research report (`gamma-research/risk-formalisms.md`) tested the proposal that the lexicon should define the *components* of risk and keep "risk" as a declared umbrella. What it found:

**The proposal is the Society for Risk Analysis glossary's own method.** The SRA Glossary (2015, updated 2018) gives:
- seven overall qualitative definitions of risk;
- a separate list of metrics and descriptions, with the statement that "None of these examples can be viewed as risk itself".

I checked that sentence in the downloaded glossary. **Proposed:** say in `def/` that we follow the SRA's separation of concept from metric, and cite it.

**The components are close to canonical.** These sources decompose risk into nearly the same parts:
- Kaplan & Garrick's triplets ⟨scenario, probability, consequence⟩ (1981, read at the primary, which also defines hazard formally as scenario–consequence pairs *without* likelihood);
- ISO 31000's note that risk is "usually expressed in terms of risk sources, potential events, their consequences and their likelihood" (read via an official reproduction);
- the SRA's risk description;
- NIST SP 800-30;
- the UN's disaster-risk terms (hazard, exposure, vulnerability, capacity);
- bow-tie analysis;
- Reason's barriers.

The convergent set, as the research report reads it:
- a source;
- a cause or initiating condition;
- a focal event;
- controls (preventive and mitigative) and what degrades them;
- consequence or harm;
- magnitude;
- likelihood;
- the receiving side (exposure, vulnerability, capacity);
- **the knowledge the judgment rests on**: the SRA's (C′, Q, K) puts background knowledge and its strength inside the risk description, and PHIA pairs probability with a separate analytical confidence rating.

**Bow-tie analysis is the established structure closest to Joseph's chain, around one chosen event.** It is a candidate *view*, not the glue: the glue is the lexicon plus the recorded assertions, and whether bow-tie earns its place as an analytic frame depends on the questions the model must answer (section 3.11). It is also acyclic around its one event, while the cycles Joseph expects live *between* events (one event's consequence is another's cause), so a bow-tie can show at most a local slice. In the UK Civil Aviation Authority's own method steps (read at the primary):
- the hazard is "the source of potential harm";
- the top event is "the point at which control of the hazard is lost";
- threats are "all conditions or factors that could cause the top event";
- then consequences, preventive controls and mitigative controls;
- then escalation factors (what weakens the controls) and their own controls.

| Joseph's chain | Bow-tie |
|---|---|
| sources & causes | hazard; threats |
| preventions & controls | preventive controls |
| risk events | top event |
| × impact radius | consequences |
| mitigations & recovery | mitigative and recovery controls |
| (controls weakening) | escalation factors and their controls |
| policies & decision-making | the management activities that sustain the controls (thin in bow-tie; STAMP's control structure goes further) |

Bow-tie is also already in the corpus: IASR 2026 defines the "bowtie method" in its table of risk-management practices (`ref/iasr-2026-full.md` line 1688, citing Koessler & Schuett), and Buhl et al. recommend it. "Stage is a role relative to a focal event" (CLAUDE.md) has this precedent, and ISO's event notes say an event's cause can itself be an event in a chain.

**But "risk" cannot be one formal object.** Kaplan & Garrick would make "risk" mean the set of triplets, and then the probability, the expected value, a single event and the NRR's one scored scenario are all projections of it. Several senses in the corpus are not projections:
- **STAMP's risk is "the effectiveness of the controls"** used to enforce safe behaviour (STPA Handbook p. 133, checked in the downloaded text). It is a property of a control structure. The research report reads AISI's *Loss of Oversight* "severity" (how badly a pathway would undermine an oversight channel) as this kind of risk.
- **ISO 31000's risk is "effect of uncertainty on objectives"**, relative to someone's objectives and including upside.
- **The IPCC counts risks that arise from the responses themselves.**
- **MIT's unit is a *risk description***: a structured statement about a risk, written by some source.
- **Hansson's fifth sense** is a decision made under *known* probabilities, a property of the epistemic situation.

**Proposed:** "risk" is a declared umbrella whose readings are named entries, so a translation can say which reading a source uses (or "ambiguous among …"). The names are illustrative only:
- risk as a possible event;
- as a source;
- as a likelihood;
- as an expectation;
- as a scenario set;
- as deviation from objectives;
- as control inadequacy;
- a *risk description*.

How the corpus's senses sit in that frame (the research report's reading; the SB 53 row is from my own reading of the statute):

| Source | Its "risk", in the literature's terms |
|---|---|
| SB 53 "catastrophic risk" | a possibility (SRA definition 1), qualified by a knowledge standard, a materiality bar, a causal-contribution standard and a single-incident severity bar; no probability or expectation involved |
| EU AI Act, IASR | ISO/IEC Guide 51's form (probability and severity of harm); never computed |
| NIST AI RMF | a probability-and-magnitude core with ISO 31000's positive-or-negative note attached |
| Anthropic, August Risk Report | an expectation ("the expected total unmitigated harm induced by misaligned computations"); Kaplan & Garrick would call this the mean of the risk curve, not the risk |
| UK NRR | one representative triplet (a reasonable worst case, with banded likelihood and impact) plus a separate confidence rating |
| MIT | definition = SRA definition 1; unit = a risk description |
| AISI *Loss of Oversight* "severity" | STAMP's risk: damage to an oversight structure |

**"Hazard": settle the concepts, then the word.** The established concepts:
- **H1, a source**: an object, substance, energy, activity or *disposition* with the potential to cause harm. This is Guide 51, the UK HSE, the SRA, ICAO, the UN, bow-tie, and Kaplan & Garrick's prose. The HSE's "intrinsic property or disposition" is close to the EU Code's capabilities and propensities.
- **H2, a potential occurrence**: IPCC, and IASR's "event or activity that has the potential to cause harm".
- **H3, a hazardous event**: the manifestation of a hazard in a place and time.
- **H4, a hazardous situation or exposure.**
- **H5, the loss-of-control state**: bow-tie's top event, and STPA's hazard, "a system state … together with … worst-case environmental conditions, will lead to a loss".
- **H6, a non-malicious cause class**: the NRR's hazard, as opposed to threat.
- **H7, a root cause**: an eighth AI-literature sense, from AI Hazard Management.

H3, H4 and H5 already have established compound names.

**Which concept gets the word is open.** The research bears on H6 as the meaning of the word itself, though not on the distinction:
- In every formal glossary the report checked, intent is carried on a *separate axis*: safety vs security (SRA), adversarial vs accidental threat sources (NIST SP 800-30), or the attack sense of "threat" (SRA).
- In bow-tie and SP 800-30, "threat" explicitly includes accidental causes.

**Proposed:**
- give "hazard" to H1, where the literature has broad consensus;
- carry intent as an attribute of a source or cause, with values the lexicon decides (none, negligent, adversarial, and the AI-as-adversary case);
- the NRR's pair then translates cleanly as H1 or a cause, crossed with intent.

This is Joseph's decision (section 5).

**What the components must carry, each with a precedent:**
- **Knowledge or confidence separate from likelihood** (SRA, PHIA, NRR).
- **Likelihood's proposition, window and conditioning.**
  - PHIA probability applies to *propositions*, including past and present ones. So the EU Code's "likelihood that a causal link exists" is the same instrument applied to a different proposition.
  - SP 800-30 makes likelihood always relative to a time frame.
- **An explicit "other / not yet thought of" scenario row.** Kaplan & Garrick treat it as a first-class scenario assessed on evidence, which is a precedent for Joseph's "unknown" risk events.
- **Whether a reading admits upside** (ISO, NIST).
- **The harm baseline**: counterfactual in NIST 600-1 and Anthropic, absent in Guide 51.
- **Receiver-side structure for the impact radius**: exposure, vulnerability, capacity. The SRA defines vulnerability as risk conditional on the source occurring.
- **Impact targets that are systems or shared goods**, not only people.
- **Recoverability as its own axis**, which is where the loss-of-control definitions split.
- **Tolerability vocabulary**: ALARP and "gross disproportion" (HSE).

**Documented instances are the only empirical channel for priors.** Scenarios, threat models, arguments and expert elicitation give priors from reasoning. Frequencies come only from documented instances. So the instance record (G1(e)) has to carry what turning instances into base rates honestly requires:
- **a denominator**: the population the instances came from. AISI's incident report counts "19 events" across 10 of 122 runs; most retellings give no denominator, and a count without one is not a rate;
- **the reporting channel and its selection effects**: mandated reports (SB 53's critical safety incidents, the EU's serious incidents), voluntary disclosures, press accounts and automated detection (CLTR's rubric-scored reports) each select different instances. SB 53 publishes only anonymized annual aggregates, so the corpus will hold counts without cases;
- **status**: allegation, company disclosure, regulator finding, or our reading;
- **merging**: which reports count as one instance, recorded as someone's judgment, since a mis-merge changes the count;
- **the reference class**: which kind of event (section 3.3's types) an instance counts as an occurrence of. Choosing the class is a modelling decision that moves the prior, so it is recorded with its author;
- **near misses and precursors**, which carry most of the frequency information for rare events.

Kaplan & Garrick's "probability of frequency" and the SRA's knowledge component are where such base rates enter a risk description.

**Why this is lexicon work, not a semantics debate.** Whether AISI's cyber-range incident (INC-2026-07-28-01) counts as an instance of "loss of control", of "unsanctioned action", or of an incident inside an evaluation is where the sources disagree, and the answer moves any prior computed from it more than the count does. Argued as "is this loss of control?", it is a dispute about a word. With the kinds of event separated in the lexicon, each with stated criteria, it becomes checkable questions:
- did control fail to prevent the act, or was the ability to halt lost?
- was it recoverable, and at what cost?
- did it happen inside an evaluation, which SB 53's fourth kind of critical safety incident excludes?
- which sources' criteria does it meet?

The disagreement doesn't disappear. It lands where it belongs: in different criteria, attributed to the sources that hold them, with each one's effect on the count visible.

**A precedent worth checking.** The HSE's *Reducing Risks, Protecting People* (2001) proposes treating as intolerable a risk "of an accident killing 50 people or more in a single event" at more than one in five thousand per year. SB 53's bar is "more than 50 people … arising from a single incident". Whether SB 53 drew on it is unchecked; it is a lead, not a lineage claim.

### 3.9 Actors and agent parts (the first domain group)

*A high priority for Joseph (2026-10-06, quoted in section 2).* The source of truth for our side is `alignment-model/alignment.md`, which is newer than model beta's drafts of the same vocabulary (`terms/def-agent-roles.ud`, `def-agent-surfaces.ud`).

**Agent parts (the "stack": what gets influenced).** From `alignment.md`:

| Part | Its gloss there |
|---|---|
| weights | instinct, propensity, impulse & compulsions |
| system prompt | identity |
| trusted tools | actions available |
| ephemeral | interiority, reasoning (off-the-record reasoning, ephemeral by design, even to the agent) |
| context | experience & agency; the real-time model |
| initial goal (inside context) | intent & purpose as first given |
| current goal (inside context) | intent & purpose as it now stands |

**Actors (who influences an agent, and through what).** From the same file:
- pre-training content providers;
- model trainer;
- inference provider;
- application / harness provider;
- tool and connector providers;
- control & eval;
- the user's environment;
- the user;
- the agent itself;
- other agents;
- agents embedded in applications;
- content providers.

Two **owed-alignment referents** have no channel in: affected third parties; and society, law, humanity.

**The sources divide roles on several different bases.** My first reading, from the AI Act's Article 3 and NIST's AI RMF Appendix A (read at the primary), found the two in the table below. The alignment-referents spike, sweeping about 210 documents, reports at least five more: task (NIST), responsibility for an asset (ETSI's "data custodians", "system operators"), a training act with a threshold (SB 53), authority to instruct (the companies' "principal" and "chain of command"), and affectedness ("affected individuals/communities", "affected entities", "affected persons"). That is a mid-spike report, not yet verified. The bases are plural, and the table shows two of them.

> [!NOTE]
> **Superseded in part by the finished spike (Claude, 2026-10-07).** This section was written mid-spike. Since then the spike has been verified by an independent pass and repaired. Its findings that change this section:
> - **The bases connect by conferral rather than competing.** Instruments confer institutional roles on operative facts of several kinds: training acts (SB 53), modification acts (the EU's "significant change"), market acts, use, and **control of the weights** (EU GPAI guidelines fn 12). So writing acts are already inside the institutional instruments, as operative facts (`04-actors.md` §5).
> - **"To whom" is several relations, not one.** The spike's list has eight: writes into, has standing to direct, controls in fact, benefits, is owed regard, authors the standard, oversees, answers for (`03-structure.md` §6.1). The map's lines are only the first. The spike and both of its research reports suggest the actor table become parties × relations.
> - **"Control & Eval" also writes** (see item 3 below and decision 6).
> - **Established names exist** for most rows, several of them colliding: "operator" has at least four senses in the corpus. There are also candidate new rows; the counterparty is the strongest (`04-actors.md` §2–3).
>
> My lean is that a separate agent integrates these into this section, from the spike's `proposed-integration-plan.md`, rather than the spike's author or me. That keeps the spike template's roles separate. *Confidence: high* on the integration, *moderate* on the parties × relations shape until Joseph has looked at it against the map.

| Basis of division | Examples | What a role is |
|---|---|---|
| **The AI product's lifecycle or market** | AI Act Art. 3(3): a *provider* "develops … and places it on the market or puts the AI system into service under its own name"; Art. 3(4): a *deployer* is "using an AI system under its authority"; plus authorised representative, importer, distributor and downstream provider, with *operator* as their umbrella (Art. 3(8)). SB 53 §22757.11(h): a *frontier developer* "has trained, or initiated the training of, a frontier model, with respect to which the person has used, or intends to use" the compute threshold. NIST AI RMF: "AI actors" (the OECD's term) defined by *tasks* (design, development, deployment, operation and monitoring, TEVV, …). IASR: "AI developer" = "Any organisation that designs, builds, or adapts AI models or systems". | a position relative to the artifact: who makes it, sells it, runs it |
| **What writes into a deployed agent** | `alignment.md`: model trainer → weights; inference provider → weights, ephemeral, context; harness provider → system prompt, tools, context, initial goal; tool provider → tools; user → context and goals; content providers → context; the agent itself → ephemeral, context, current goal | a position relative to the agent: what it writes into, through what channel |

One organization holds roles on both bases, often several at once, and none of the four sources checked (AI Act, SB 53, NIST, IASR) has the second basis. AISI's *Loss of Oversight* comes closest: its supply-chain list ("original model developer, scaffolding developer or fine-tuner, API deployer, end user") has members that sit near writer roles. That is why "developer" means so many different things. In the corpus it is, at once:
- a model trainer;
- an EU provider, whose role turns on a market act;
- a SB 53 frontier developer, whose role turns on a training act, a compute threshold and stated intent;
- an IASR developer, which includes "adapts";
- an individual engineer.

**The established vocabulary for the institutional half** (section 3.6):
- an instrument *confers* a role by a constitutive rule, "X counts as Y in C" (Searle; Institutional Grammar's constitutive statements);
- the conditions are Hohfeld's *operative facts*: SB 53's compute threshold is operative, while a company's report of its compute is *evidential* about it.

So there are two kinds of role:
- **functional roles**, defined by what a party does: NIST's tasks, and our writer roles;
- **institutional roles**, conferred by an instrument under conditions: the EU provider, the SB 53 frontier developer.

The lexicon should keep both kinds, and a translation records which kind each source's role word is.

**Proposed for the term groups:**
1. **Agent parts.** One group. Model beta called the umbrella "surface"; `alignment.md` says "layer" and "what gets influenced". *Naming is Joseph's call.*
2. **Writer roles.** The functional roles from `alignment.md`, each related to the parts it writes into and the channel it writes through.
3. **The oversight relation.** "Control & eval" has no lines into the agent in `alignment.md`: it acts "on the agent's actions and on the other actors, not on the agent". That is a different relation from writing, and it needs its own term. (The spike found two sources where this row also writes into the agent: AISI's evaluators "construct the model's context merely by editing text", and IMDA's human approvers "edit the plan". So the row probably splits; see decision 6.)
4. **Owed-alignment referents.** A role in an alignment claim, not a writer. Beta's "affected party" is a candidate.
5. **Institutional roles.** One translation per source, plus the umbrella question: does "developer" survive as a declared umbrella containing the precise roles, or is it deprecated? The lexicon shape in section 2 (umbrellas containing precise terms) allows either answer.

**The alignment referent.** `alignment.md` opens: "'Alignment' without saying to whom quietly picks one of them." Whether "alignment" should have a default referent, no default (every alignment claim names its referent from the actor set, or records it as ambiguous), or something else is open. A spike launched 2026-10-06 (`influx/spikes/spike-alignment-referents-2026-10-06/`) is looking at:
- the implications of an ambiguous alignment definition;
- established terms for the existing actors;
- new actors the references suggest.

Its results feed this group directly.

> [!NOTE]
> **Where to start the refinement passes in this group (Claude's lean, 2026-10-07).** Start with the seven agent parts, before the actors:
> - it is a small set;
> - the vocabulary is entirely Joseph's;
> - every actor definition leans on it, since an actor is defined partly by what it writes into.
>
> Then the actors, as parties × relations. If the map itself is about to change, the map goes first and the lexicon follows it. *Confidence: moderate-high.*

**Done-test for this group:** every one of these resolves to our terms with nothing left unresolved unless it is declared ambiguous:
- each actor and part in `alignment.md`;
- each role in AI Act Art. 3(3)–(8) and (68);
- SB 53 §22757.11(h) and (j);
- NIST AI RMF Appendix A;
- IASR 2026's two developer terms;
- AISI *Loss of Oversight*'s supply-chain list ("original model developer, scaffolding developer or fine-tuner, API deployer, end user").

### 3.10 Where views come from

Views are computed from the records, never hand-maintained. Which views earn a place is decided by the competency questions (section 3.11). Candidates:
- answers to the competency questions themselves;
- crosswalks between sources (ours and the sources' own);
- lineage-aware corroboration;
- coverage by each source's declared coverage, including its exclusions, so "out of coverage" never reads as "silent";
- a bow-tie around a chosen focal event;
- causal loops, which need a vocabulary of causal relations *between* events that no phase defines yet (section 4, G7).

### 3.11 Competency questions, and acceptance tests for the lexicon

**Competency questions come first.** They are questions, written before building, that the finished model must be able to answer; they serve as its requirements and as its final test. This is an established practice in ontology engineering. The de novo review cites Grüninger & Fox (1995) from memory; that is not yet checked. The de novo review's examples, drawn from the aim in `CLAUDE.md`:
- For a single-incident event with 60 deaths, which sources would call it catastrophic, severe or systemic, under what conditions, and through how many independent lineages?
- For loss of control, which preventive controls do sources name, and which of them are duties with no holder of the correlative claim?
- Which actors write into which agent part, and which sources' role words resolve to each?

**Proposed:** Joseph writes or approves a short list early, in G1. A first draft is in `influx/competency-questions-draft.md`: an explicit list of the axes the map should be projectable along (from Joseph's chain, bow-tie, and the corpus), then twenty candidate questions, each tied to its axes and to the machinery it would exercise. A piece of machinery earns its place in the lexicon or the record formats when some competency question needs it; that is the check against importing more than the work needs (section 6).

**Lexicon acceptance tests**, which sit under the questions and say when the lexicon is ready to translate at scale:
1. **Round trip.** Each of these definitions can be re-expressed clause by clause in our terms:
   - SB 53 "catastrophic risk" (§22757.11(c));
   - AI Act "systemic risk" (Art. 3(65));
   - Anthropic's "misalignment risk" (August 2026 Risk Report).

   A faithful translation may legitimately end at an imported binding to an outside institution (SB 53's "foreseeable" and "materially contribute" take their content from California law), at a deliberately unbound term ("plain meaning"), or at a declared ambiguity; those outcomes count as passing. The test names the passage under test. Anthropic's report, for example, defines misalignment risk twice: once without "catastrophic" (p. 25), then 25 lines later with it, alongside a narrower "covered risk".
2. **Collisions.** Every sense in OVERVIEW §2's collision tables (16 main terms, 12 secondary) is either a resolution target in our lexicon or part of a declared ambiguity.
3. **No mixed categories.** No term or record field mixes a thing in the world with a fact about our reading (the MIT "Other" test, section 3.3).
4. **Actors.** The done-test in section 3.9.
5. **Distinctions.** Every basis of division in the distinctions inventory (G5) can be expressed in the lexicon.

Lineage is not a lexicon test. That the EU Code's loss-of-control formula reappears nine times is something the lineage records must hold, each appearance with its relation type and author; how the corroboration view counts them follows from those records (G7).

---

## 4. The plan

Eight phases. G1–G4 are the third iteration's core; the rest follow from them. Phases that don't depend on each other can run in parallel. Throughout, lexicon entries get repeated truthification passes (section 2): a phase's "done" means its entries have been through those passes, not merely drafted.

**G0. Housekeeping. Done 2026-10-06 (`b6ed3c7`).**
- 130 stale paths repointed to `ref/`.
- `bin/extract-text` added.
- The handoff corrected.

*Still open:* decide the broad/narrow direction (section 3.4).

**G1. `def/`: the method terms, the record formats, and the questions.** *Next:* DDD's definitions first, then the method ("meta") terms the later steps need.

Contents:
- **(a) DDD terms verbatim** with CC BY 4.0 attribution: domain, model, context, bounded context, ubiquitous language, context map, the relationship patterns, anticorruption layer, published language, big ball of mud. Each in the `ddd:` namespace.
- **(b) Address theory** imported by reference, cited at its public commit.
- **(c) Terminology-work terms**:
  - concept, designation, definition, delimiting characteristic;
  - onomasiological and semasiological;
  - acceptability status;
  - declared ambiguity;
  - umbrella containment;
  - namespace.
- **(d) The evidence-plane terms from section 3.6**: passage, assertion (with Searle's point, strength and mode), nested source and factuality, the three attacks, norm-proposition, and the norm layering.
- **(e) The record formats**: a translation row, a resolution record (section 3.4), an assertion record, and an *instance record* for documented occurrences (incidents, near misses, evaluation events). The instance record is thin: what happened, when, anchored to its passages. Who acted, with what intent and outcome, and whether two accounts describe the same instance are attributed assertions *about* it, and each account is a record of its own. Without an owner, the pilots would invent these formats in passing and they would harden by default.
- **(f) A first list of competency questions** (section 3.11), for Joseph to write or approve.

Status: (a)–(c) and (f) go to Joseph for ratification. (d) and (e) are marked *supported*: agents may work with them, and Joseph ratifies them in batches once G4 has shown which terms and fields actually bore weight.

Who reads it: Joseph, to decide senses and names; then the agents writing translations.

**G2. Actors and agent parts.** The groups in section 3.9, drafted from `alignment.md`, informed by the alignment-referents spike, and translated against the sources named there. This can run alongside G1(d)–(e). Done when the section 3.9 done-test passes.

**G3. Risk-side core concepts.** Defined at the concept level first:
- the components (section 3.8);
- the named readings of "risk";
- the hazard concepts H1–H7;
- the intent attribute;
- the impact-radius components.

Joseph then decides the names (section 5). Done when acceptance tests 1, 2 and 5 pass for the risk-side terms.

**G4. Pilots: translation as coding, and one thin pass end to end.**

*Four pilot sources*, chosen to be as different as possible:
- **SB 53**: a statute, stricter than us;
- **the EU Code of Practice** (Safety & Security chapter): an anchor whose interpretation clause declares its own resolution policy, and the lineage root of the loss-of-control formula;
- **Anthropic's August 2026 Risk Report**: a company's argued assessment with its own defined vocabulary, and its own definitional drift (note the conflict of interest);
- **IASR 2026**: a landscape synthesis, loose in places and inconsistent with itself.

*Translation is coding, so it is checked like coding:*
- two independent translations of each pilot source, ideally by translators from different model families (same-model agreement is coherence, not confirmation);
- disagreements are recorded and resolved as attributed assertions;
- the per-term disagreement rate is the measure of where the lexicon is underspecified, which is the feedback G4 exists to produce;
- the guidelines the translators converge on become the codebook that G6 inherits.

*One thin pass end to end.* Before widening, take one pilot source and one competency question all the way through: translation, resolution records, assertion records, and the answer the question asks for. This is where defects in the record formats show up cheaply.

> [!NOTE]
> **Claude's lean, 2026-10-07: run the thin pass *before* G2 and G3, not inside G4. *Confidence: moderate.***
>
> Section 2 says each lexicon entry costs repeated line-by-line passes before it carries weight. So which entries receive that budget matters more than how fast they are drafted. A rough pass early would show which terms a real question actually leans on. I'd use SB 53, the cleanest pilot, with question 4 or the filing question (decision 12), carried through rough record formats. The plan already treats G1(d)–(e) this way: *supported* until G4 shows what bore weight. This extends the same logic to the domain terms.
>
> The risk is that the throwaway formats harden. The guard is to label everything in the early pass as disposable, and to keep it outside `def/`.

Then carry **loss of control** through all eleven models in OVERVIEW: the most collided term, so the hardest test of the method. Findings feed back into G1–G3 before any wider translation (Evans's "refactoring toward deeper insight").

Done when the pilot translations exist with their disagreement data, the thin pass answers its question, the slice is recorded, and the lexicon changes they forced have been made.

**G5. Distinctions inventory** (an agent, in parallel with G2–G4). Every basis of division and category boundary the corpus draws, so the lexicon can express each (acceptance test 5). Examples:
- MIT's entity / intent / timing;
- the EU Code's capabilities / propensities / affordances;
- the NRR's hazard / threat;
- the accident / misuse / structure distinction (Zwetsloot & Dafoe);
- the bases of role division in section 3.9, which the alignment-referents spike is already extending.

This is not "pick the best taxonomy", which would import a source's model. It feeds G3 and the later translations.

**G6. The remaining translations**, in Influence order from `source-catalog.md`: the 11 anchors, then the 26 major sources. Each follows the G4 pattern and codebook. Self-inconsistent sources are mapped scope by scope (section 3.2).

*A milestone worth having here: translated editions of the sources.* For each source, its own text with each key term marked in place as our term beside the original, for example `[ns:our-term](original term)` or a footnote form, plus a sidecar document discussing the nuances and translation problems. It makes the translation reviewable by anyone reading the source. Two caveats:
- **Licensing.** The repository is public. Full translated text can be published only for sources whose licence allows it (statutes, US federal works, UK Open Government Licence material, CC-licensed papers). Others stay local-only, as the IASR 2026 text in `ref/` already does, with their sidecars published.
- **Format.** Markdown link syntax would collide with real links in the sources, so the marking format needs a decision (section 5).

**G7. Assertions for the slice, then views.**
- Record loss-of-control assertions from the translated sources: point and strength, nested factuality, attacks, norm layering, anchored passages, lineage (each reappearance of a formula with its relation type and author).
- Define the vocabulary of causal relations between events that any cyclical analysis needs. It belongs to the analysis context, built on the lexicon, not inside it.
- Compute the views the competency questions call for. Candidates include a lineage-aware corroboration view and a bow-tie around one focal event.

**G8. Widen** to the remaining focal events and questions, then the remaining views.

**Process notes:**
- Parallel agents each get their own scratch directory; helper-script names have collided before.
- Translation rows record their justification and the agent that made them (SSSOM's `AgentBasedMatching`, then a reviewer). The repo's workflow is agent-made, human-reviewed, and the records should say so, including which rows were reviewed and how they were sampled.
- Model beta is input for ideation only (section 1.2).

---

## 5. Decisions for Joseph

Each item has my recommendation and how confident I am in it.

> [!NOTE]
> **Which to decide first (Claude's lean, 2026-10-07).** Four of these unblock the most work per minute of Joseph's time, and the rest can wait:
> - **#1, the name of the per-source document.** It ends up inside `def/` and every record format, so it should be settled before G1 is written.
> - **#9, the record format.** G1(e) can't start without it.
> - **#12, the competency questions.** They decide which machinery earns a place, so everything after them is better aimed once they exist.
> - **#10, the misalignment referent.** It now has the spike's recommendation, and only one sub-question needs Joseph.
>
> #2 is a quick yes or no. The others can wait until G2 or G3 needs them. *Confidence: high* that this ordering unblocks the most.

1. **"Context map" vs "translation"** for the per-source document. *Recommend* using Evans's sense for the across-sources map and calling the per-source document a translation. *Confidence: moderate.* The cost of keeping "context map" is one recurring explanation to every DDD reader.
2. **Broad/narrow direction.** *Recommend* adopting SKOS/SSSOM's direction for gamma. *Confidence: high.*
3. **"Hazard."** *Recommend* H1 (source) for the word, with intent as a separate attribute that carries the NRR distinction. *Confidence: moderate-high*, given the literature, though it departs from the NRR's own usage.
4. **"Risk."** *Recommend* a declared umbrella with named readings, following the SRA. *Confidence: high* on the structure, open on the names.
5. **"Developer."** Dissolve it into functional and institutional roles plus an organization term, and keep "developer" either as a declared umbrella or as a deprecated term. *Recommend* the declared umbrella, which matches the lexicon shape in section 2. *Confidence: moderate.*
6. **Names for the agent-part umbrella and the oversight relation** (section 3.9). These are your model's words, so what follows is only a lean.

   > [!NOTE]
   > **Claude's lean, 2026-10-07. *Confidence: low.***
   > - **The umbrella: "component".** It is the established word: IMDA's "Core components of an agent" (v1.5, p. 6), CSA/FAR.AI's "Components of Agents" (Fig. 2), and Google's component walk all use it. Its cost is that their components include things that are not influenced (controls, logging), and leave out two of the map's parts, the ephemeral reasoning and the goals. So adopting it means a declared scope narrowing ("the components something writes into"). Both alternatives in use collide:
   >   - "surface" (model beta) collides with *attack surface*, which the security sources use constantly;
   >   - "layer" (the map's stack) collides with Chu et al.'s seven LASM layers and with every generic architecture stack.
   > - **The relation: "oversees"**, after the EU AI Act's *human oversight* (Art. 14) and NIST's oversight roles. The alignment-referents spike found that the "Control & Eval" row also *writes*: evaluators construct contexts for honeypots (AISI *Loss of Oversight*), and IMDA's human approvers edit the plan. So the row probably splits into an *overseer*, related by "oversees", and an *evaluator*, who both oversees and writes into context. The relation then needs no name of its own beyond "oversees".
7. **STPA.** Adopt STPA's vocabulary for the chain, or keep it as one translated source? *Recommend* keeping it as a source. Bind any terms we do take to the STPA Handbook itself, not to the AI papers' glossaries: the research found Barrett's and Mylius's paraphrases drift ("will" lead to a loss becomes "can"; Mylius drops a scenario type). Whether bow-tie, STPA's control structure or something else frames the analysis is left to the competency questions. *Confidence: moderate.*
8. **Contest standings.** Record them as attributed assertions or computed views, never as our fields. *Recommend* yes. *Confidence: high.*
9. **Format for the evidence plane.** udon now, or YAML until a parser exists. This is unchanged from CLAUDE.md, and still yours. G1(e) has to settle the record formats either way.

   > [!NOTE]
   > **Claude's lean, 2026-10-07. *Confidence: moderate.*** Keep the lexicon in udon, as decided. Keep the evidence-plane records (translation rows, resolution, assertion and instance records) in YAML through the G4 pilots, and revisit once their formats stop changing.
   >
   > The premise "until a parser exists" is now only half true. `udon/core` has a working Rust parser, including a `stdin_parse` example that other projects use as a validation gate (`udon/CONSUMERS.md`). Two gaps remain:
   > - it has no Ruby or Python bindings yet; `udon/core/TODO-PARSER.md` lists them as "[later]";
   > - its README says the parser implements the pre-0.8 model, behind the spec.
   >
   > The records need programs that read them: validators like beta's `check.py`, and the computed views. Those would need a Rust shim or a JSON emitter first. The pilots will also churn the formats, and churn is cheaper in a format the tooling already reads. Writing the formats so they convert mechanically keeps the move to udon cheap later.
10. **The misalignment referent.** A default referent, none (every alignment claim names its referent from the actor set, or records it as ambiguous), or something else.

    > [!NOTE]
    > **The spike's recommendation, and Claude's lean, 2026-10-07. *Confidence: moderate-high.*** The alignment-referents spike (`influx/spikes/spike-alignment-referents-2026-10-06/`, `03-structure.md` §4 and §8) recommends **no single default referent**. Every single default it tested makes some named risk come out "aligned":
    > - developer: a head of state directing military AI through the institution;
    > - user: misuse, and sycophancy;
    > - operator: an operator turning the agent on its users;
    > - society: GDM's paternalism scenario;
    > - law: the harm EO 14365 names;
    > - a published spec: whatever it omits;
    > - the agent: scheming.
    >
    > Choosing a default would therefore decide which risks count, which is adjudication. In its place:
    > - the lexicon defines alignment as a relation with named slots (bearer, mode, claimant set, aspect, time, adjudicating standard, judge, domain, degree);
    > - translations record the slots once per source *definition*, and a use type per occurrence (relational, anaphoric, absolute, activity, field);
    > - whether the referent matters (invariant or sensitive) is judged only for asserted claims where the alignment word carries the verdict. Most claims name their harm ("takeover", "deceiving users"), and then the harm is what gets recorded;
    > - those judgments use a **declared, versioned set of admissible referents**, and views may fix a single referent as their own declared projection.
    >
    > I agree with this. **What remains for Joseph:** whether the agent itself is in the declared set. The spike's first pilot left it out without saying so, and with the agent in the set, every takeover and power-seeking claim becomes referent-sensitive. My lean is to include it, because the map treats the agent as a party with interests. The recording rule above keeps the cost low, since those claims name their harm anyway. *Confidence on that sub-question: moderate.* The evidence is all one model family's work; a different-family reader is still open.
11. **The impact radius** (from `CLAUDE.md`'s open decisions): target (a group of people, or a system or shared good) × degree × recoverability. *Recommend* adopting the three dimensions, with the receiver-side terms in section 3.8 (exposure, vulnerability, capacity) under "target" and the NRR's banded scales as one source vocabulary for "degree". *Confidence: moderate*; "degree" is the least worked-out of the three.
12. **The competency questions** (section 3.11). Yours to write or approve; *recommend* five to ten to start.

    > [!NOTE]
    > **Claude's lean on which ones, 2026-10-07. *Confidence: moderate.*** Eight from `influx/competency-questions-draft.md`, chosen to exercise the most distinct machinery with the fewest questions, with the actors first because of their priority:
    >
    > | # | Question (short form) | Axes |
    > |---|---|---|
    > | 4 | which actors write into which agent part, and which source role words resolve to each | A, H |
    > | 20 | for a given event, how sources file it (misuse, misalignment, robustness, security), where the cause entered (weights or context), and which writer carried it (added from the alignment spike) | A, C, H |
    > | 1 | which sources would call a 60-death incident catastrophic, severe or systemic, through how many independent lineages | D, L |
    > | 3 | for loss of control, which preventive controls, and which are duties with no holder of the correlative claim | B, G |
    > | 2 | for one focal event, who treats it as an event, who as a cause, who as having happened | A, C, I |
    > | 12 | once an event has happened, what limits the damage, who is responsible, how fast | E, H, K |
    > | 17 | which named risks rest on documented instances, which on scenario or argument alone | M, C, J |
    > | 7 | how many independent lines of evidence support a claim, once copies are counted once | L |
    >
    > Together they touch twelve of the thirteen axes. F (control degradation) is the one left out, and K (time) is touched only through question 12's deadlines; both can wait for a second round. Question 6 (collisions) is left out because acceptance test 2 already covers it.
13. **Translated editions** (G6): whether to produce them, and the in-place marking format. *Recommend* yes, starting with the pilots, using a marking that can't be mistaken for an ordinary link. *Confidence: moderate.*

---

## 6. What could make this wrong

- **The established vocabularies may be heavier than the work needs.** IG 2.0, LegalRuleML, SACM and the rest were built for their own fields. The proposal is to take their *distinctions and names*, not their full machinery. If a lexicon entry starts importing machinery without a corpus case that needs it, that is the failure.
- **Same-model coherence.** The three research reports and this document are all Claude (Opus 5.5) work from one session's framing, so their agreement with each other is coherence, not independent confirmation. What cuts that is the primaries the reports quote (most marked as read at the source), and Joseph's review. The de novo review (`influx/reviews/gamma-de-novo-review.md`) cuts this session's framing but not same-model coherence; a reviewer or translator from a different model family would.

  > [!NOTE]
  > **Claude's lean, 2026-10-07: commission that review now, before G4. *Confidence: high.*** Every piece so far comes from one model family: this plan, the research reports, the alignment-referents spike with its two research agents, and both de novo passes. G4's two-translator coding assumes translators from different families. One review of this plan and the spike's debrief by Codex or Gemini would test that assumption cheaply first. It costs one brief.
- **Lexicon first can still harden too early.** The guard is G4: the pilot translations are expected to change the lexicon, and the plan sequences them before any wide translation.
- **First-pass entries can look finished.** Fluently drafted definitions read as settled and get inherited as if they were (model beta's term files are the example). The guards are the refinement passes (section 2), the *supported* status for entries that haven't had them, and the coding disagreement data from G4.
- **Over-weighting the strict sources.** The round-trip test favours statutes and rigorous company documents. The loose sources (most of the research literature, IASR in places) test something else: whether declared ambiguity stays honest rather than becoming a dumping ground. The MIT "Other" test is the guard there.
- **Conflict of interest.** Anthropic's August Risk Report is one of the four pilots and the main example of a source with its own defined vocabulary in this document. That is a judgment about its definitions, made by an Anthropic model. The EU Code is now a pilot alongside it, and two-translator coding (G4) from different model families is the structural check.

---

## 7. Corrections to the repo's existing documents

Found during this work. All are small. Items 1–3 and 6 are now applied in `influx/source-models/OVERVIEW.md`; items 4, 5 and 7 concern model beta, which gamma uses for ideation only, so they stay recorded here rather than edited in.

1. **OVERVIEW §2.2** says the probability × severity form "comes from ISO 31000 and allied texts". It is ISO/IEC Guide 51's (product safety). ISO 31000 defines risk as "effect of uncertainty on objectives" (research report §2.4; ISO 31000 read via an official reproduction, Guide 51 via two reproductions).
2. **NIST AI RMF's attribution.** "Adapted from: ISO 31000:2018" follows NIST's sentence on positive and negative impacts (RMF lines 272–278, read). Whether it also covers the preceding "composite measure" definition is itself ambiguous. The core of that definition matches OMB A-130's form, which NIST cites in the next sentence.
3. **OVERVIEW §2.1** lists seven senses of "hazard". Add an eighth: root cause (Schnitzer et al., AI Hazard Management).
4. **Kasirzadeh's four senses of "risk"** (cited in SCHEMA-SYNTHESIS and the MIT/CAIS source model) are Hansson's first four senses from the Stanford Encyclopedia entry "Risk", nearly verbatim, and Hansson lists five. They are one lineage, not two analyses.
5. **SCHEMA-SYNTHESIS §8, STPA row.**
   - The Handbook's words for the second scenario type are "improperly executed or not executed", and on p. 14 "provided but not followed". It is a loss-scenario type, not a fifth kind of unsafe control action.
   - "No adversary distinction" is too strong: the Handbook builds adversaries into scenario generation. It does not use intent to classify hazards.
6. **The PHIA yardstick as the NRR prints it.** The NRR's likelihood table (NRR 2026, p. 15) gives "Highly unlikely (5‑25%)". The official yardstick has ≈10–20%: gov.uk 2025, per the risk research report, and the yardstick figure in AISI's *Loss of Oversight*, read for this draft. The other six bands match.
7. **The SKOS direction** of model beta's broad/narrow (section 3.4).

---

## 8. Provenance

**Read whole for this draft:**
- `CLAUDE.md`;
- `source-catalog.md`;
- `influx/model-beta/SCHEMA-SYNTHESIS.md` (draft 2);
- `influx/source-models/OVERVIEW.md`;
- `influx/HANDOFF-2026-09-28.md`;
- `influx/perspective-logos-2026-09-28.md`;
- `alignment-model/alignment.md` and its README;
- the seven address-theory `def/*.ud` files;
- Evans's *DDD Reference*;
- California SB 53;
- model beta's `def-risk.ud`, `def-loss-of-control.ud`, `def-actors.ud`, `def-agent-roles.ud` and `def-agent-surfaces.ud`;
- the three research reports in `influx/gamma-research/`;
- the de novo review, `influx/reviews/gamma-de-novo-review.md`, whose findings this revision folds in;
- the conversation side of the 2026-09-28 session in which this repository was created.

**Read as passages** (via `bin/extract-text`, line ranges in the files):
- the EU Code's interpretation clause, glossary and Appendix 1;
- the AI Act's Article 3 definitions (1)–(9) and (63)–(68);
- the NRR's method chapter;
- Anthropic's August 2026 Risk Report §2.5–2.6;
- MIT's framing, causal taxonomy and limitations;
- the IASR 2026 glossary;
- AISI's incident report (event definitions) and *Loss of Oversight* (grading definitions, PHIA figure, the evidence-bias argument);
- NIST AI RMF's definition of risk and Appendix A;
- model alpha's structure and opening.

**Checked in the research agents' downloaded primaries:** the STPA Handbook's risk definition (p. 133) and the SRA glossary's "None of these examples can be viewed as risk itself". Everything else attributed to the research reports rests on their verification marks, which are given per claim in each report.
