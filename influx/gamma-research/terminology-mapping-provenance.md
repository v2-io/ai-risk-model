# Terminology, mapping and provenance: the established vocabulary behind the lexicon, context maps, passage anchors and lineage

*Research input for the iteration-3 methodology document. 2026-10-06, a Claude Opus 5.5 research agent, briefed by the coordinator. Nothing here is ratified; it is evidence plus my reading of it.*

**How to read the marks.** The value of this file is the line between what was checked and what was remembered, so every claim carries one of these:

- **[V]** read at the primary source this session: the spec, ontology file or paper, fetched with `curl` and searched as text. The quotes come from that text, not from a summarizing tool.
- **[V·preview]** read in the publisher's official preview of a paywalled ISO standard (the iTeh preview PDFs, which carry the opening pages). Only what the preview shows is marked this way.
- **[V·2nd]** confirmed only at a secondary source, which is named.
- **[M]** from training memory and not checked. Treat it as a lead, not a citation.

Quotes from ISO standards are kept short (ISO text is copyrighted and this repo is public). W3C documents, CC-BY papers and the CC-BY DDD Reference are quoted more freely, with attribution.

---

## 0. Summary for the synthesis

### What held up, what didn't, and what was missing

| Named in the brief | Verdict | Where it fits |
|---|---|---|
| ISO 704 / ISO 1087, concept-oriented terminology, Wüster | **Holds up.** "Concept before name" is stated almost verbatim, most directly in **ISO 860** (not named in the brief): *"Harmonization starts at the concept level and continues at the term level."* ISO 704's own scope **excludes** knowledge, data and information modelling, and the concept-first school has a serious critique (Temmerman) that bears on AI-risk vocabulary. | The lexicon: how a concept is analysed and defined, and how a designation is chosen. |
| SKOS mapping properties | **Holds up, and the agent's warning was right.** `<A> skos:broadMatch <B>` means **B is broader**. The project's tables read "from the source's term to ours" with **broad = theirs is wider**, which is the **opposite** of SKOS/SSSOM when the source term is the subject. This is consistent inside the repo, but would invert on export. | The lexical-map rows, and any RDF export. |
| SSSOM | **Holds up, and closer to the context-map rows than expected:** justification, author/creator/reviewer, confidence, negation, "no term found", and a bare string as the subject. But it **deliberately excludes context**: *"Mappings themselves have no context (i.e. are always true)."* | The per-term lexical map (type level). Not the per-occurrence resolution record. |
| PROV-O | **Holds up** for the generic relations (derivation, revision, quotation, primary source, invalidation, alternate/specialization, bundle). It covers only a few of the corpus's lineage subtypes cleanly. Its "primary source" is the historian's sense, which collides with the repo's `channel: primary`. | The lineage relations, alongside the standards below. |
| Web Annotation selectors | **Holds up as remembered** (TextQuote: exact/prefix/suffix; TextPosition; Range; `refinedBy`; TimeState), with two details that matter here: multiple quote matches are to be *"treated as matching all"*, and the spec suggests position selectors over quote selectors for restricted texts. | Passage anchors. |
| Micropublications, nanopublications | **Hold up.** Micropublications are the closer fit, because they keep the natural-language statement with its qualifiers verbatim and treat claim-similarity judgements as assertions in their own right. | The assertion record, and corroboration. |

**Not named, and in my judgement as important as anything above:**

1. **OntoLex-Lemon** (W3C Community Group, 2016). Its *lexical entry → lexical sense → ontology reference* chain is the standard three-node model of "a source's word, the sense it is used in, our concept". The **sense** is "a reification of a pair" of word and concept, where usage conditions and rationale attach. That is very close to a context-map row. [V]
2. **IFLA LRM's *nomen*** (2017): "the reification of a relationship between an instance of res and a string". This is nearly a restatement of the address theory's *binding*, and arrived at independently. LRM also gives Work / Expression / Manifestation / Item, the established vocabulary for "same text republished", "one text, several publishers", and "document ≠ relata key". [V]
3. **ISO 860** (concept harmonization) and **ISO 25964-2** (mapping between vocabularies: directional mappings, *compound equivalence*). [V·preview]
4. **Legislative lineage already has a vocabulary.** The schema.org `legislation*` properties (from the ELI work) and **Akoma Ntoso**'s modification types: textual (repeal, substitution, insertion…), *meaning* (`termModification`, `authenticInterpretation`), *scope* (`exceptionOfScope`, `extensionOfScope`), *force* vs *efficacy* (the in-force / applies-from split), and legal-system changes (`implementation`, `republication`, `reiteration`…). [V]
5. **PAV** (authored / curated / created by; retrieved / imported / derived from; *source accessed at*) and **CiTO** (cites as authority / evidence / source document; contains assertion from; includes quotation from; qualifies; updates; corrects; retracts; shares author with; shares funding agency with). These cover the authorship-roles table (§3.1 of SCHEMA-SYNTHESIS) and much of the citation-shaped lineage. [V]
6. **Evans's own definitions** of *context map* and *anticorruption layer*. What this project calls a per-source "context map" is, in Evans's terms, closer to one **anticorruption-layer translation**. His Context Map is the map *across* contexts. [V]
7. ISO's own provenance convention for adopted definitions, `[SOURCE: ISO 1087:2019, 3.3.2, modified — …]`, which is exactly the "adopted / adapted from" marking the lexicon needs. [V·preview]

### The findings I'd weigh most in the methodology

- **The broad/narrow inversion** (§2.3). It is cheap to fix now and expensive after context maps are written at scale.
- **The project needs both directions of terminology work, and the literature has names for them.** The lexicon is *onomasiological* (concept first, then a name). The context maps are *semasiological* (start from a source's word, ask which concept). Temmerman's critique of concept-first theory is precisely that real special languages need both (§1.3).
- **Type-level mapping vs occurrence-level resolution.** SSSOM, SKOS and ISO 25964 all model *term-to-concept, always true*. The repo's resolution record is *this occurrence, in this scope, as of this date, with this path*, which none of them model. Use them for the first and keep the address theory's resolution for the second (§3.4).
- **"Ambiguous among candidates" is not a mapping relation in any standard checked.** SKOS, SSSOM, OntoLex and Web Annotation all lack a disjunction. Several mappings read as "maps to all of these", and Web Annotation turns several quote matches into "all". That supports the address theory's position that ambiguity is a *resolution outcome* with a candidate set. It also means the outcome field is ours to define, not a gap in our reading of the standards.
- **Several of our meta-vocabulary words already mean something else in these standards** (§9): *designator*, *primary source*, *context map*, *broad/narrow*, *domain*, *concept*.

---

## 1. Terminology science (ISO/TC 37)

### 1.1 What was read

- **ISO 704:2022**, *Terminology work — Principles and methods*, 4th edition. Preview: Foreword, Introduction, clauses 1–4, 5.1–5.4.4 and the full table of contents. https://cdn.standards.iteh.ai/samples/79077/2dd50250582e4a9fa3420af5da705572/ISO-704-2022.pdf [V·preview]
- **ISO 1087:2019**, *Terminology work and terminology science — Vocabulary*. Preview: 3.1.1 through 3.4.2. https://cdn.standards.iteh.ai/samples/62330/f8493dfbf02f4f23b9d9524832aa0b9b/ISO-1087-2019.pdf [V·preview]
- **ISO 860:2007**, *Terminology work — Harmonization of concepts and terms*. A web-search summary of retailer listings says it was "reviewed and confirmed in 2021"; I did not check that at ISO. Preview: Introduction, 1–4.2.3. https://cdn.standards.iteh.ai/samples/40130/833afcafa87247d3911b486d3b6a2c01/ISO-860-2007.pdf [V·preview]
- **ISO 25964-2:2013**, *Thesauri and interoperability with other vocabularies — Part 2: Interoperability with other vocabularies*. Preview: clause 3 through 3.42, plus the TOC. https://cdn.standards.iteh.ai/samples/53658/9d9f9da6097147e68f418edf4f8350f0/ISO-25964-2-2013.pdf [V·preview]
- **ISO 30042:2019**, *TermBase eXchange (TBX)*. Preview: clause 3. https://cdn.standards.iteh.ai/samples/62510/f46331e1601947ec95744e13b1f31632/ISO-30042-2019.pdf [V·preview]

### 1.2 Core definitions, verbatim

**ISO 1087:2019** [V·preview]:

| Entry | Definition (verbatim) |
|---|---|
| 3.1.1 object | "anything perceivable or conceivable" |
| 3.1.2 extension | "set of all of the objects to which a concept corresponds" |
| 3.1.4 domain (subject field) | Note 1: "The borderlines and the granularity of a domain are determined from a purpose-related point of view." |
| 3.1.11 terminology | "set of designations and concepts belonging to one domain or subject" |
| 3.2.1 characteristic | "abstraction of a property" |
| 3.2.5 delimiting characteristic | "essential characteristic used for distinguishing a concept from related concepts" |
| 3.2.6 intension | "set of characteristics that make up a concept" |
| 3.2.7 concept | "unit of knowledge created by a unique combination of characteristics". Note 1: concepts "are, however, influenced by the social or cultural background which often leads to different categorizations." |
| 3.2.13 generic relation | the specific concept's intension "includes the intension of the generic concept plus at least one additional delimiting characteristic" |
| 3.2.15 superordinate concept (*broader concept*) | "generic concept or comprehensive concept" |
| 3.2.19 generic concept | "concept in a generic relation that has the **narrower intension**" |
| 3.2.23 associative relation | "non-hierarchical concept relation" |
| 3.2.27 causal relation | "sequential relation based on the criterion of cause and its effect" |
| 3.3.1 definition | "representation of a concept by an expression that describes it and differentiates it from related concepts" |
| 3.3.2 intensional definition | conveys the intension "by stating the immediate generic concept and the delimiting characteristic(s)"; Note 1: they "should be used whenever possible" |
| 3.4.1 **designation** (admitted term: **designator**) | "representation of a concept by a sign which denotes it in a domain or subject" |
| 3.4.2 term | "designation that represents a general concept by linguistic means" |

**ISO 704:2022** [V·preview]:

- Scope of the activity (Introduction 0.1): *"Terminology work can also support knowledge modelling, information modelling, data modelling and classification, but this document does not cover these fields."*
- Concept before name (5.1): *"objects in a given situation are observed and conceptualized mentally and then a designation is assigned to the concept rather than to the objects themselves."*
- The same objects across domains (5.1): *"Different domains or subjects view the same objects differently."* This is followed by a table defining 'water' three ways for chemistry, physics and biology. That is the bounded-context idea, in ISO's words.
- The order of terminological analysis (5.4.2): identify the domain → properties → characteristics → "how the characteristics combine to form a concept" → relations with other concepts → "writing or identifying and analysing definitions" → **"assigning a designation to the concept"**, which comes last.
- On existence claims (clause 4): *"Discussions on whether an object actually exists in reality are unproductive and should thus be avoided."* This lines up with compilation-not-adjudication.
- 5.4.3: *"The intension determines the extension."*
- The TOC confirms these sections exist: 6.4.4 *Applying the substitution principle*; 6.5 *Deficient definitions* (circular, inaccurate, negative); 6.6 *Information supplementing or replacing definitions* (contexts, explanations, notes, examples); 6.7 *Indicating sources*; 7.6.2 term-formation *Principles*; 7.7 *Relations between designations and concepts* (mononymy and monosemy, synonymy, equivalence, antonymy, polysemy and homonymy, harmonization, **acceptability rating**). [V·preview, headings only]
- What those sections say is not in the preview. My recollection [M]: the substitution principle says a definition should be able to replace its term in running text without loss or change of meaning. The term-formation principles in 704:2009 were transparency, consistency, appropriateness, linguistic economy, derivability, linguistic correctness and preference for native language. Acceptability rating grades designations as preferred / admitted / deprecated / obsolete. The ideal is monosemy and mononymy within a domain, with homonymy across domains tolerated.

**ISO 860:2007** [V·preview]:

- Introduction: harmonization is desirable because *"differences between concepts do not necessarily become apparent at the designation level"*, *"similarity at the designation level does not necessarily mean that the concepts behind the designations are identical"*, and *"mistakes occur when a single concept is designated by two synonyms which by error are considered to designate two different concepts."* Then: **"Harmonization starts at the concept level and continues at the term level."**
- 3.1 concept harmonization: an activity "leading to the establishment of a correspondence between two or more closely related or overlapping concepts … in order to eliminate or reduce minor differences between them".
- 3.4 term harmonization: "selection of designations for a harmonized concept".
- 4.2.2: harmonization is more likely when the subject field *"is well established and relatively stable"* and *"has a tradition of standardization"*.
- 4.2.3: the preliminary comparison determines *which characteristics the concepts have in common*, *which differ*, and *which are essential to each key concept*.

**ISO 25964-2:2013** [V·preview]:

- 3.41 mapping (noun): "relationship between a concept in one vocabulary and one or more concepts in another". Note 1: *"A mapping generally has a direction."*
- 3.14 **compound equivalence**: a mapping "in which one term or concept in one context is represented by two or more terms or concepts in another".
- 3.27 equivalence mapping: "the concept in the target vocabulary … is considered identical in scope to the concept … in the source vocabulary".
- 3.23 differentiated mapping: "Types of mapping that can be distinguished include equivalence, associative and hierarchical; equivalence can be further subdivided into simple or compound, and the degree of equivalence can be marked".
- Clause 11, *Exact, inexact and partial equivalence*, exists [V·preview, TOC]; its content is [M]. As I recall, inexact means overlapping concepts mapped as equivalent, and partial means one slightly broader or narrower but mapped as equivalent. NISO maintains a correspondence table from ISO 25964 to SKOS / SKOS-XL / MADS: https://www.niso.org/schemas/iso25964 [V: the page exists and says SKOS-XL was used "where the basic SKOS data model lacks a construct"; the table itself was not read].

**ISO 30042:2019 (TBX)** [V·preview]: 3.5 **concept entry** (terminological entry): the "part of a terminological data collection which contains the terminological data related to one concept". A TBX entry is one concept, with language sections and term sections inside it [M for the internal structure]. The TBX/ISO `administrativeStatus` values are `standardizedTerm`, `preferredTerm`, `admittedTerm`, `deprecatedTerm`, `supersededTerm`, `legalTerm` and `regulatedTerm` (each suffixed `-admn-sts`) [V·2nd: the TEI Consortium's ISO profile, `TEIC/Stylesheets` `profiles/iso/schema/isotei.rnc`, not ISO itself].

**ISO's own provenance marking for adopted definitions** [V·preview, seen repeatedly]: `[SOURCE: ISO 1087:2019, 3.3.2, modified — "generic concept" replaced by "superordinate concept" in the definition, …]`. Each adopted definition carries its source, the clause, and a *modified — what changed* note. The lexicon's "adopted" rows (e.g. `def-risk.ud`, IASR's four definitions) need exactly this.

**Wüster.** [M] Eugen Wüster's *General Theory of Terminology* (posthumous *Einführung in die allgemeine Terminologielehre*, 1979) is the Vienna-School source of concept orientation, as I recall: concept primacy, fixed and clearly delimited concepts, univocity. [V·2nd] The VUB record of Temmerman (2000) names "the Vienna School (Eugen Wüster, Helmut Felber, Infoterm and associated institutions)" as the traditional theory under critique.

**The critique.** Temmerman, R. (2000). *Towards New Ways of Terminology Description: The sociocognitive approach.* John Benjamins (TLRP 3), doi:10.1075/tlrp.3. Abstract [V at https://researchportal.vub.be/en/publications/towards-new-ways-of-terminology-description-the-sociocognitive-ap/]: *"the traditional approach impedes a pragmatic and realistic description of a large number of categories and terms … The main principles of this new theory imply: a combined semasiological and onomasiological perspective; only few categories can be clearly delineated; form and content of definitions vary according to category types and user's requirements; synonymy and polysemy are functional in special language and an diachronic approach is unavoidable."* Its central notion is the "unit of understanding" (chapter title, [V·2nd] via the search result). [M] Cabré's Communicative Theory of Terminology and Faber's Frame-based Terminology are the other main post-Wüster schools.

### 1.3 Does terminology science already say "settle concepts before names"?

Yes, and in nearly those words: ISO 860's *"Harmonization starts at the concept level and continues at the term level"*, and ISO 704's ordering, which puts "assigning a designation to the concept" last. The name for this is the **onomasiological** approach (concept → name). Its counterpart, **semasiological** (name → concept), is the dictionary-maker's direction.

My read for this project:

- **The lexicon is onomasiological work.** Deciding which concept gets "hazard" is, in ISO terms, term harmonization (3.4) after concept harmonization: settle the concepts and their delimiting characteristics, *then* choose a preferred designation for each, and mark the others admitted or deprecated. The SKOS Primer says the same in KOS terms: *"it is recommended that no two concepts in the same KOS be given the same preferred lexical label for any given language tag"* (https://www.w3.org/TR/skos-primer/#seclabel) [V]. The udon `:avoid` is a deprecated-term marking, and `:synonyms` maps to admitted terms.
- **The context maps are semasiological work**: start from a source's word in its scope and ask which of our concepts it denotes. ISO 704 is not written for this direction. ISO 860 §4.2.3's comparison (common, differing and essential characteristics) and OntoLex (§4) are the better guides for it.
- **So the project is in Temmerman's "combined" position whether or not it says so.** The concept-first rule is right for *our* side. The source side has the polysemy and drift that Temmerman says traditional theory "impedes" describing. The repo already shows them: "hazard" in at least three senses, "systemic risk" with opposite senses at the EU and in IASR, "misaligned outputs" reversed in AI 100-2.

### 1.4 Fit and strain

**Fits:**
- *Domain* is "determined from a purpose-related point of view", and ISO 704 shows the same object conceptualized differently per domain. That is a bounded context, in ISO's terms.
- ISO 860's preconditions for harmonization ("well established and relatively stable", "a tradition of standardization") give the project a citable reason **not** to harmonize the sources among themselves. AI-risk vocabulary fails both conditions. The repo's principle is *compilation, not adjudication*: we harmonize nothing between sources; we only map each onto ours.
- The intensional definition (genus plus delimiting characteristics) maps onto udon's existing shape: the term-group intro states the genus, and the `|invariants` carry characteristics. Reading the invariants as *delimiting characteristics*, the ones that separate this concept from its neighbours, would make "not to be confused with" mechanical rather than discretionary.
- ISO 1087 lists **causal relation** as a concept relation (3.2.27). That is useful for keeping a *definitional* causal link ("a hazard is something with potential to cause harm") separate from a source's *empirical* causal claim, which belongs in the assertion plane.

**Strains:**
- ISO 704 excludes knowledge, data and information modelling, and this project is partly all three. ISO is the authority on how to define and name. It does not claim to govern the record structure.
- ISO's concept is static. Nothing in the preview admits a time index. The repo's deictic definitions ("today's most advanced models", "the most capable models at any given time") and the address theory's as-of resolution have no counterpart in the ISO model, so time is ours to supply.
- Genus-plus-differentia presumes a clean concept system. For contested concepts (misalignment, loss of control), Temmerman's critique applies, and the udon convention of "deliberate ambiguity where it is honest" has more support in the post-Wüster literature than in ISO.
- **Collision:** ISO 1087 lists **"designator"** as an admitted term for *designation*, a sign representing a concept. `def-match.ud` uses *designator* for "a reference … that reaches its referent through a binding", the philosophy-of-language sense. A lexicon entry quoting ISO next to the address theory would carry two senses of one word.

---

## 2. SKOS mapping properties

**Sources.** *SKOS Simple Knowledge Organization System Reference*, W3C Recommendation, 18 August 2009, §10 *Mapping Properties*: https://www.w3.org/TR/skos-reference/#mapping. *SKOS Primer*, W3C Working Group Note, 18 August 2009: https://www.w3.org/TR/skos-primer/#secmapping. [V]

### 2.1 Verbatim

- Purpose (§10.1): the mapping properties "are used to state mapping (alignment) links between SKOS concepts in different concept schemes, where the links are inherent in the meaning of the linked concepts."
- closeMatch: *"used to link two concepts that are sufficiently similar that they can be used interchangeably in some information retrieval applications. In order to avoid the possibility of 'compound errors' when combining mappings across more than two concept schemes, skos:closeMatch is not declared to be a transitive property."*
- exactMatch: *"indicating a high degree of confidence that the concepts can be used interchangeably across a wide range of information retrieval applications. skos:exactMatch is a transitive property, and is a sub-property of skos:closeMatch."*
- S41: *"skos:broadMatch is a sub-property of skos:broader, skos:narrowMatch is a sub-property of skos:narrower, and skos:relatedMatch is a sub-property of skos:related."* S43: narrowMatch is the inverse of broadMatch. S44: relatedMatch, closeMatch and exactMatch are symmetric. S46: *"skos:exactMatch is disjoint with each of the properties skos:broadMatch and skos:relatedMatch."*
- **Direction** (§8.1, semantic relations): *"A triple `<A> skos:broader <B>` asserts that `<B>`, the object of the triple, is a broader concept than `<A>`, the subject of the triple."* (§10.5, Example 51): *"`<A> skos:broadMatch <B>` … (where `<B>` is broader than `<A>`)"*.
- On provenance (§10.6.1): *"using the SKOS mapping properties is no substitute for the careful management of RDF graphs or the use of provenance mechanisms."*
- What a concept is (§3.1): *"A SKOS concept can be viewed as an idea or notion; a unit of thought. However, what constitutes a unit of thought is subjective, and this definition is meant to be suggestive, rather than restrictive."*
- Labels (§5): S13, pref/alt/hidden labels are pairwise disjoint; S14, *"A resource has no more than one value of skos:prefLabel per language tag."* The Primer recommends (§2.2) that no two concepts in one KOS share a preferred label.
- Notes (Primer §2.4): *"skos:scopeNote supplies some, possibly partial, information about the intended meaning of a concept"*; *"skos:definition supplies a complete explanation of the intended meaning"*; *"skos:historyNote describes significant changes to the meaning or the form of a concept"*; editorialNote and changeNote are for "KOS managers or editors". SKOS-XL (Appendix B) makes labels first-class resources: *"identifying, describing and linking lexical entities."*

### 2.2 The direction question, settled

`<A> skos:broadMatch <B>` = "A has a broader match B" = **B is the broader one.** SSSOM's guide says the same in plain words (§3.1): *"`broad`: The object is conceptually broader than the subject."*

### 2.3 What the repo does, checked

- `influx/model-beta/terms/def-actors.ud` line 37, the legend all term files point to: *"Match, from the source's term to ours: exact · close · broad (theirs is wider) · narrow (theirs is narrower)"*.
- `influx/model-beta/mappings.yaml` lines 2–3: *"rel (from the SOURCE term to OUR concept): … broad = source term is BROADER than our concept"*. `mappings-mp.yaml` repeats it.

With the source term as subject and our concept as object, SKOS/SSSOM `broad` asserts that **our concept is broader**. The repo's **broad** therefore corresponds to **`skos:narrowMatch`**, and its **narrow** to **`skos:broadMatch`**. The usage is internally consistent, so no row is wrong as written; the labels are inverted against the standard. Counted this session: `rel: broad` / `rel: narrow` appear 46 / 70 times across `mappings*.yaml`, and the `| broad |` / `| narrow |` match cells about 31 / 28 times across `terms/*.ud`. `influx/model-beta/README.md` line 73 plans a Turtle export with "mappings → SKOS match properties". A naive export would silently flip every hierarchical row.

My lean for iteration 3: if the words *broad/narrow* are kept, adopt the SKOS/SSSOM reading (subject = source term, `broad` = object broader) and say so in one line. The other honest option is to stop borrowing the SKOS words (e.g. *theirs-wider* / *theirs-narrower*), so nobody imports a direction they don't mean.

A second direction trap from ISO 1087: the *broader* concept has the *narrower intension* (3.2.19). "Wider" in the repo's legend is extensional (it covers more cases). A lexicon that also talks about characteristics should say "wider in extension" once, explicitly.

### 2.4 Fit and strain beyond direction

- **SKOS maps concepts, not words.** Strictly, a source's *term* is not a `skos:Concept`. To use SKOS you mint a concept in the source's own scheme, one per sense, and map that. This is the gap OntoLex fills (§4).
- **The repo's `homonym` has no SKOS equivalent.** "Same word, different thing here" is a fact about the *word*, not a concept-to-concept relation. In SKOS it becomes "their concept, a different concept, maybe `relatedMatch`, maybe nothing". In SSSOM it can be stated as a negated match (§3).
- **exactMatch is transitive and symmetric.** Across twenty sources, one wrong `exact` row propagates by inference. That is the "compound errors" SKOS avoids for closeMatch. The repo's `exact` rows carry the implication "interchangeable across a wide range of applications". Many of them, e.g. NIST 600-1 "Risk" → our `risk`, are closer to "same definitional content". [My read]
- **Pooling is fine.** One source concept with `narrowMatch` to two of ours ("the EU's 'loss of control' spans bounded and strict") is consistent SKOS: several hierarchical mappings.
- **Ambiguity cannot be expressed, and that is right.** SKOS has no "this source's use is one of {A, B}, we can't tell which". Several mappings read conjunctively. In the address theory's terms, ambiguity is a resolution *outcome*, recorded per occurrence, not a mapping relation.
- **The documentation properties line up with udon sections**: definition ↔ the term line; scopeNote ↔ `|discussion`; historyNote ↔ the vocabulary change log (the Slattery precedent in SCHEMA-SYNTHESIS §5); editorialNote ↔ `|working-notes`; example ↔ `|examples`. Adopting the SKOS names in an export costs nothing.

---

## 3. SSSOM (Simple Standard for Sharing Ontological Mappings)

**Sources.** Matentzoglu, N., Balhoff, J. P., Bello, S. M., et al. (2022). "A Simple Standard for Sharing Ontological Mappings (SSSOM)." *Database* 2022: baac035. doi:10.1093/database/baac035, CC-BY 4.0, read via PMC9216545 [V]. LinkML schema at `mapping-commons/sssom`, both the `v1.0.0` tag and `master` at commit `667d3c5`: https://github.com/mapping-commons/sssom/blob/master/src/sssom_schema/schema/sssom_schema.yaml [V]. Docs `src/docs/{mapping-predicates,spec-model,confidence-model,mapping-justifications}.md` [V]. SEMAPV terms: https://github.com/mapping-commons/semantic-mapping-vocabulary/blob/main/semapv-terms.tsv [V].

**Versions.** The repo has `v1.0.0` and tags up to `v1.1.0a5`. Several slots below exist on `master` but not in the 1.0.0 schema: `record_id`, `cardinality_scope`, the `composed entity expression` type, and the expanded use of `sssom:NoTermFound` [V, by grep of both schemas]. Treat those as 1.1-in-progress.

### 3.1 Verbatim (schema descriptions unless noted)

- **mapping_justification** (required): *"A mapping justification is an action (or the written representation of that action) of showing a mapping to be right or reasonable."*
- **confidence**: *"A value assigned by the creator of the mapping to denote the creator's confidence or estimated probability that the mapping record is correct. … When not explicitly specified, confidence estimation algorithms should consider the mapping confidence to be 1.0 by default."*
- **author_id**: *"the persons or groups responsible for asserting the mappings"*. **creator_id**: *"The creator is the agent that put the mapping in its published form, which may be different from the author"*. **reviewer_id**: *"reviewed and confirmed the mapping"*. **mapping_date**: *"the date the mapping was asserted. This is different from the date the mapping was published"*.
- **predicate_modifier** = `Not`: *"Negating the mapping predicate. The meaning of the triple becomes subject_id is not a predicate_id match to object_id."*
- **subject_type** value `rdfs literal`: *"the entity being mapped is not a semantic entity with a distinct identifier, but is instead represented entirely by its literal label."* So a bare source word can be the subject.
- **mapping_cardinality** includes `1:0`: *"the subject has no match in the object vocabulary. This value MUST only be used when the object_id is sssom:NoTermFound."*
- **curation_rule** / **curation_rule_text**: *"a (potentially) complex condition executed by an agent that led to the establishment of a mapping."*
- **comment**: free-text curator notes. **see_also**: *"a URL specific for the mapping instance … Could also be a github issue URL that discussed a complicated alignment"*. **subject_source** / **subject_source_version**: the vocabulary the subject comes from, and its version.
- **Propagation** (spec-model.md): set-level values in propagatable slots *"MUST be interpreted as if all mappings within the set had that same value"*. Propagation *"is only allowed if none of the individual mapping records already have their own value in that slot."*
- Predicate guide (mapping-predicates.md): curators should seek *"intended meaning … you do not try to figure out what an apple is, but what thing in the world … the FOODON developers intended the FOODON:Apple identifier to refer to."* And on `close`: *"This is a hazy category and should be avoided in practice."*
- SEMAPV justifications include `semapv:ManualMappingCuration` (*"performed by a human agent and is based on human judgement and domain knowledge"*), `semapv:MappingReview`, `semapv:LexicalMatching`, `semapv:BackgroundKnowledgeBasedMatching`, `semapv:MappingChaining`, `semapv:MappingInversion`, and, on the main branch now, `semapv:LLMBasedMatching` and `semapv:AgentBasedMatching` (*"an autonomous agent plans and executes a multi-step workflow — typically involving tool use, retrieval, intermediate reasoning, and self-evaluation"*). Whether those last two are in a released SEMAPV version was not checked.
- Paper, aim: *"encouraging the publication of mappings that are transparently imprecise, transparently inaccurate and transparently incomplete"*.
- Paper, on context, quoted in full because it is the main strain: *"Mappings themselves have no context (i.e. are always true)."* And: *"It was an important design decision for SSSOM to decide that mappings should be universally applicable and not dependent on some global context, which would make merging and reconciling them much more complex"*. The workaround offered is to push context *into the predicate*, e.g. a custom `hasExactCrossSpeciesMatch`.

### 3.2 Fit

A context-map row in SSSOM shape:

| Context-map field | SSSOM slot |
|---|---|
| the source's word | `subject_label`, `subject_type: rdfs literal` (or a minted ID per source sense) |
| the source document / scope | `subject_source`, `subject_source_version` |
| match kind | `predicate_id` (skos:*), `predicate_modifier: Not` for the repo's "homonym" / "Stix says these are NOT loss of control" |
| our concept | `object_id` |
| "none: a gap in our vocabulary" | `object_id: sssom:NoTermFound`, `mapping_cardinality: 1:0` |
| rationale ("what is *probably* meant") | `comment`, `curation_rule_text`, `mapping_justification: semapv:ManualMappingCuration` / `AgentBasedMatching` |
| who decided | `author_id`; who wrote the row: `creator_id`; who checked: `reviewer_id` |
| our confidence | `confidence` (ours, distinct from the source's own hedge, which the repo keeps verbatim) |
| the anchoring passage | `see_also` (a URL), or an extension slot holding a Web Annotation selector |

The repo's `channel: primary | relay: <file>` has no SSSOM slot. It is provenance of *our reading*, and would go in an extension slot. SSSOM 1.1 has `extension_definitions` for exactly this.

### 3.3 Strain

- **Always-true mappings vs. scoped, timed, per-occurrence resolution.** SSSOM, SKOS and ISO 25964 all work at the type level. SCHEMA-SYNTHESIS §5's resolution record (outcome, path, author, time index, reference standard, bearer) is occurrence-level and origin-relative, which is exactly what SSSOM excluded on purpose. SSSOM's own workaround (encode context in the predicate) would multiply predicates, as the paper itself notes.
- **No disjunction.** Several rows plus `1:n` cardinality means "maps to several", not "is one of these, undetermined". "Ambiguous among candidates" needs its own field, or an occurrence-level record.
- **Propagation is all-or-nothing.** Set-level values apply only when no record overrides them. SCHEMA-SYNTHESIS §3.3's scope-inherited qualifiers with sentence-level override and *conflict flags* are a richer mechanism. SSSOM is a precedent only for the inheritance half.
- **One confidence number.** SSSOM confidence is the creator's estimate that the row is correct. That is fine for ours, but keep the source's hedge out of it.

---

## 4. OntoLex-Lemon, and the LRM *nomen* (not named in the brief)

**OntoLex.** Cimiano, P., McCrae, J. P., Buitelaar, P. (eds.), *Lexicon Model for Ontologies: Community Report*, W3C Ontology-Lexicon Community Group, Final Community Group Report, 10 May 2016. https://www.w3.org/2016/05/ontolex/ [V]. It is not a W3C Recommendation.

- *"A lexical entry represents a unit of analysis of the lexicon that consists of a set of forms that are grammatically related and a set of base meanings that are associated with all of these forms."*
- **LexicalSense**: *"A lexical sense represents the lexical meaning of a lexical entry when interpreted as referring to the corresponding ontology element. A lexical sense thus represents a reification of a pair of a uniquely determined lexical entry and a uniquely determined ontology entity it refers to."* And: *"Via the lexical sense object we can attach additional properties to a pair of lexical entry and ontological predicate … to describe under which conditions (context, register, domain, etc.) it is valid to regard the lexical entry as having the ontological entity as meaning."*
- **reference**: *"relates a lexical sense to an ontological predicate that represents the denotation of the corresponding lexical entry."* **usage**: *"usage conditions or pragmatic implications when using the lexical entry to refer to the given ontological meaning."*
- **LexicalConcept**: *"a mental abstraction, concept or unit of thought that can be lexicalized by a given collection of senses."* **evokes**: relates an entry to *"the mental concept that speakers of a language might associate when hearing the lexical entry."*
- Its stance: *"It is not a formal model of semantics but a model of lexicography. … it assumes that there is a given ontology … to be linked to a lexicon that expresses how the classes, properties and individuals defined in the ontology are lexicalized."*
- vartrans: **TerminologicalRelation**, *"relates two lexical senses of terms that are semantically related in the sense that they can be exchanged in most contexts, but their surface forms are not directly related."*

**Fit.** A per-source lexicon in OntoLex shape: each source's term is a `LexicalEntry` in that source's lexicon (its bounded context). Each sense the source uses is a `LexicalSense`, whose `reference` is our concept and whose `usage` carries the conditions and rationale. That is a context-map row, and this is the standard that separates *word*, *sense* and *concept* the way the repo's "hazard: at least three senses" needs. It also matches the two-plane design: OntoLex's lexicon/ontology split is the repo's vocabulary layer vs model plane.

**Strain.** `reference exactly 1` per sense. "Ambiguous among" is again not representable as one sense; it stays an occurrence-level outcome. OntoLex is lexicographic, so it has no time index either.

**IFLA LRM (Library Reference Model)**, Riva, P., Le Bœuf, P., Žumer, M., August 2017, revised December 2017, CC-BY 4.0. https://www.ifla.org/wp-content/uploads/2019/05/assets/cataloguing/frbr-lrm/ifla-lrm-august-2017_rev201712.pdf [V]

- **LRM-E9 Nomen**: *"An association between an entity and a designation that refers to it."* Scope note: *"An arbitrary combination of signs or symbols cannot be regarded as an appellation or designation until it is associated with something in some context. In that sense, the nomen entity can be understood as the reification of a relationship between an instance of res and a string."* And: *"Two instances of the nomen entity can have perfectly identical values for their nomen string attribute and yet remain distinct"*. Its attributes include **Scheme**, **Context of use** and **Reference source** (LRM-E9-A3/A5/A6).
- **Fit.** This is the address theory's *binding* (`def-binding.ud`: "A deliberate, maintained association from a name to a referent") from a different tradition. Like the address theory, LRM keeps the association as the object, not the string, and lets identical strings be distinct associations. LRM has no maintainer and no dangle/collide failure vocabulary; the address theory is richer there. Worth citing as convergence. [My read]

---

## 5. Passage anchoring

### 5.1 W3C Web Annotation Data Model

*Web Annotation Data Model*, W3C Recommendation, 23 February 2017. https://www.w3.org/TR/annotation-model/#selectors [V]

- **TextQuoteSelector** (#text-quote-selector): *"This Selector describes a range of text by copying it, and including some of the text immediately before (a prefix) and after (a suffix) it to distinguish between multiple copies of the same sequence of characters."* `exact`: *"A copy of the text which is being selected, after normalization."* Exactly one `exact`; prefix and suffix SHOULD each have exactly one.
- Normalization: *"The text MUST be normalized before recording in the Annotation. Thus HTML/XML tags SHOULD be removed, and character entities SHOULD be replaced"*. Selection is *"in terms of unicode code points"* and *"SHOULD NOT start or end in the middle of a grapheme cluster."*
- **On multiple matches**: *"If, after processing the prefix, exact, and suffix, the user agent discovers multiple matching text sequences, then the selection SHOULD be treated as matching all of the matches."*
- **On copyright**: *"If the content is under copyright or has other rights asserted on its use, then this method of selecting text is potentially dangerous. … For static texts with access and/or distribution restrictions, the use of the Text Position Selector is perhaps more appropriate."*
- **TextPositionSelector** (#text-position-selector): *"describes a range of text by recording the start and end positions of the selection in the stream. Position 0 would be immediately before the first character"*. The start is included and the end is not, and positions are counted after the same normalization.
- **RangeSelector** (#range-selector): start and end each given by another selector, *"everything from the beginning of the starting selector through to the beginning of the ending selector, but not including it."*
- **refinedBy** (#refinement-of-selection): *"The relationship between a broader selector and the more specific selector that SHOULD be applied to the results of the first."*
- **Multiple selectors** (§4.2): *"Multiple Selectors can be given to describe the same Segment in different ways in order to maximize the chances that it will be discoverable later"*. They *"SHOULD select the same content … Consuming user agents MUST pick one of the described segments, if they are different."*
- **FragmentSelector** has `conformsTo` for the fragment syntax. **TimeState** (#time-state): `sourceDate`, *"The timestamp at which the Source resource SHOULD be interpreted for the Annotation."*
- PDF fragments: RFC 8118 (*The application/pdf Media Type*, March 2017) §3 defines `page=<pageNum>` and `nameddest=<name>` [V, https://www.rfc-editor.org/rfc/rfc8118.txt].

### 5.2 URL Fragment Text Directives (WICG)

https://wicg.github.io/scroll-to-text-fragment/, a Draft Community Group Report, not a W3C Recommendation [V]. The syntax is `#:~:text=[prefix-,]start[,end][,-suffix]`: *"The only required parameter is start. If only start is specified, the first instance of this exact text string is the target text."* It is the URL-level cousin of TextQuoteSelector: a clickable anchor into web-only sources (agency pages, blog posts). Note that, unlike the W3C rule, it takes the **first** match.

### 5.3 Fit and strain

- The repo's line references point into `pdftotext -layout` extractions, which aren't kept. In W3C terms they are **TextPositionSelectors over a derived representation**, the most fragile kind. The repo's working rule ("PDF pages survive re-extraction; cite both") is the W3C multiple-selector pattern. The robust form is `FragmentSelector(conformsTo RFC 8118, "page=N")` `refinedBy` `TextQuoteSelector(exact, prefix, suffix)`, with the line number kept as an optional `TextPositionSelector` and a `TimeState`/version for the document as read.
- **In the address theory's terms:** a quote selector is a *match* (the test "contains this text, between these contexts"), and a position selector is a match on the current ordering, as `def-match.ud` already says. The anchor's *intended cardinality* is {1,1}. The W3C rule "treat as matching all" silently widens it to {0,N}, so a miss changes meaning without notice. I'd record the match count at anchoring and on re-check. Three against {1,1} is the address theory's "narrowed insufficiently", which should surface rather than widen.
- **Tables are the gap.** No W3C selector addresses table/row/column in a PDF. SCHEMA-SYNTHESIS §2's table locators (thresholds in framework tables that `pdftotext` interleaves) need a project-defined selector. [My read; I found no standard for it]
- **Copyright:** some `ref/` texts are git-ignored (IASR 2026 full text). The spec's own note suggests position selectors for restricted texts. For a public repo, quote-selectors on short passages are fine. Long `exact` values from restricted texts are the risk the spec names.
- [M] Hypothesis (the annotation tool) anchors robustly by recording TextQuote, TextPosition and XPath-range selectors together and re-anchoring by fuzzy match. That is a working precedent for the multi-selector approach, but I did not verify its current implementation.

---

## 6. Provenance and lineage

### 6.1 W3C PROV

*PROV-DM: The PROV Data Model*, W3C Recommendation, 30 April 2013, https://www.w3.org/TR/prov-dm/. *PROV-O: The PROV Ontology*, W3C Recommendation, 30 April 2013, https://www.w3.org/TR/prov-o/. [V]

| Concept (anchor) | Verbatim |
|---|---|
| entity (#concept-entity) | "a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary." |
| derivation (#concept-derivation) | "a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity." PROV-N `wasDerivedFrom(e2, e1)`: e2 generated, e1 used. |
| revision (#concept-revision) | "a derivation for which the resulting entity is a revised version of some original. The implication here is that the resulting entity contains substantial content from the original." |
| quotation (#concept-quotation) | "the repeat of (some or all of) an entity, such as text or image, by someone who may or may not be its original author." |
| primary source (#concept-primary-source) | "something produced by some agent with direct experience and knowledge about the topic, at the time of the topic's study, without benefit from hindsight." The relation runs "from secondary materials to their primary sources" and "can be up to interpretation". |
| attribution (#concept-attribution) | "the ascribing of an entity to an agent." |
| invalidation (#concept-invalidation) | "the start of the destruction, cessation, or expiry of an existing entity by an activity." |
| specialization (#concept-specialization) | "shares all aspects of the latter, and additionally presents more specific aspects of the same thing" |
| alternate (#concept-alternate) | "Two alternate entities present aspects of the same thing. These aspects may be the same or different, and the alternate entities may or may not overlap in time." |
| bundle | "a named set of provenance descriptions, and is itself an entity, so allowing provenance of provenance to be expressed." |
| influence | "a generic dependency of o2 on o1 that signifies some form of influence of o1 on o2." |

PROV-O names them `prov:wasDerivedFrom`, `prov:wasRevisionOf`, `prov:wasQuotedFrom`, `prov:hadPrimarySource`, `prov:wasInvalidatedBy`, `prov:specializationOf`, `prov:alternateOf`, `prov:wasAttributedTo`, `prov:wasInfluencedBy`.

### 6.2 PAV: provenance, authoring and versioning

`http://purl.org/pav/`, version 2.3.1 [V]. Paper: Ciccarese, P., Soiland-Reyes, S., Belhajjame, K., Gray, A. J. G., Goble, C., Clark, T. (2013). *J. Biomedical Semantics* 4:37, doi:10.1186/2041-1480-4-37 [V: DOI metadata only].

- **authoredBy**: *"An agent that originated or gave existence to the work that is expressed by the digital resource."* **curatedBy**: *"an agent specialist responsible for shaping the expression in an appropriate format."* **createdBy**: *"An agent primary responsible for making the digital artifact"*, with the example *"the author wrote 'this species has bigger wings than normal' in his log book. The curator … formalizes this as 'locus perculus has wingspan > 0.5m'. The creator enters this knowledge as a digital resource"*.
- **retrievedFrom**: *"the same representation as the original"*. **importedFrom**: *"the content has been preserved, but transcribed somehow … where the original was an document scan, and this resource is the plain text found through OCR."* **derivedFrom**: *"If the content has however been further refined or modified"*. **sourceAccessedAt**: *"accessed or consulted (but not retrieved, imported or derived from)… The source does not make any claims about the nice weather, that is my interpretation"*.
- **Fit.** The author/curator/creator split is SCHEMA-SYNTHESIS §3.1's writers / rendering-layer / record-maker distinction, and it applies to our own records too: a source authored the passage, an agent curated it into an assertion, a script created the YAML. The retrieved / imported / derived / accessed ladder fits *extraction condition* exactly. The relata PDF is *retrieved*; the `pdftotext` text is *imported* ("plain text found through OCR" is the spec's own example); an assertion record is *derived*; "our reading" is *sourceAccessedAt*.

### 6.3 CiTO: Citation Typing Ontology

`http://purl.org/spar/cito`, version 2.9.0 [V]. Peroni, S., Shotton, D. (2012). "FaBiO and CiTO." *J. Web Semantics* 17:33–43, doi:10.1016/j.websem.2012.08.001 [V: DOI metadata only].

- **citesAsAuthority**: *"cites the cited entity as one that provides an authoritative description or definition of the subject under discussion."* **citesAsEvidence**: *"as source of factual evidence"*. **citesAsSourceDocument**: *"as being the entity from which the citing entity is derived"*.
- **containsAssertionFrom**: *"contains a statement of fact or a logical assertion … originally present in the cited entity."* **includesQuotationFrom** and **includesExcerptFrom**.
- **qualifies**: *"places conditions or restrictions upon statements, ideas or conclusions presented in the cited entity."* **extends**, **updates**, **corrects**, **retracts** (*"constitutes a formal retraction"*), **disputes**, **refutes**, **agreesWith**, **disagreesWith**, **critiques**, **speculatesOn**, **repliesTo**.
- **sharesAuthorWith**: *"each entity has at least one author in common with the other entity."* **sharesAuthorInstitutionWith**, **sharesFundingAgencyWith**, and classes **AuthorSelfCitation**, **AffilationSelfCitation** (sic), **FunderSelfCitation**.
- **plagiarizes**: *"including textual or other elements from the cited entity without formal acknowledgement of their source."*

### 6.4 FRBR / LRM, and legislative change

- **LRM** [V]: *Work*, "The intellectual or artistic content of a distinct creation". *Expression*, "A distinct combination of signs conveying intellectual or artistic content". *Manifestation*, "A set of all carriers that are assumed to share the same characteristics as to intellectual or artistic content and aspects of physical form". *Item*, "An object or objects carrying signs".
- **Akoma Ntoso** (OASIS LegalDocML, *Akoma Ntoso Version 1.0 Part 1: XML Vocabulary*, OASIS Standard, 29 August 2018; https://docs.oasis-open.org/legaldocml/akn-core/v1.0/os/part1-vocabulary/akn-core-v1.0-os-part1-vocabulary.html) [V] applies FRBR to law: *"EXPRESSION: any version of the WORK whose content is specified and different from others for any reason: language, versions, etc. (e.g., act 3 of 2005 as in the version following the amendments entered into force on July 3rd, 2006)."* Modification types, from the schema `akomantoso30.xsd` [V]:
  - textual: `repeal, substitution, insertion, replacement, renumbering, split, join`
  - meaning: `variation, termModification, authenticInterpretation`
  - scope: `exceptionOfScope, extensionOfScope`
  - force: `entryIntoForce, endOfEnactment, postponementOfEntryIntoForce, prorogationOfForce, reEnactment, unconstitutionality`
  - efficacy: `entryIntoEfficacy, endOfEfficacy, inapplication, retroactivity, extraefficacy, postponementOfEfficacy, prorogationOfEfficacy`
  - legal system: `staticReference, implementation, ratification, application, legislativeDelegation, deregulation, conversion, expiration, reiteration, remaking, republication, coordination`

  The vocabulary also separates validity (`@start/@end`) from efficacy (`@startEfficacy/@endEfficacy`) per fragment, which is SCHEMA-SYNTHESIS §2's "in force from / applies from" at the fragment level.
- **schema.org legislation terms** (from the ELI work; https://schema.org/version/latest/schemaorg-current-https.jsonld) [V]: `legislationAmends` (*"introducing legal changes"*); `legislationRepeals` (*"cancels, abrogates"*); `legislationChanges` (*"encompasses the notions of amendment, replacement, correction, repeal, or other types of change"*); `legislationCorrects` (*"textual changes … with no legal impact"*); `legislationTransposes` (*"a legally binding link"*); `legislationEnsuresImplementationOf`; `legislationApplies` (*"an informative link, and it has no legal value"*); `legislationCommences` (*"Another legislation that this one sets into force"*); `legislationConsolidates`; `legislationDateOfApplicability` (*"can sometimes be distinct from the date of entry into force"*); `legislationLegalForce`; `legislationLegalValue` (*"The same legislation can be written in multiple files with different legal values"*); `isBasedOn`. [M] These are the schema.org renderings of ELI ontology properties (`eli:amends`, `eli:repeals`, `eli:transposes`, `eli:based_on`, …). The ELI OWL file itself could not be fetched (the Publications Office endpoints returned errors or JS-only pages).

### 6.5 The lineage table (SCHEMA-SYNTHESIS §3.4) against the standards

| Repo subtype | Best existing term(s) | Fit |
|---|---|---|
| verbatim / near copy | `prov:wasQuotedFrom`; `cito:includesQuotationFrom` / `includesExcerptFrom`; when unattributed, `cito:plagiarizes` | good for the copying. **"Wording copies, force does not"** needs force tracked separately (Akoma `forceMod`, schema.org `legislationLegalValue`) |
| citation as basis | `cito:citesAsAuthority` / `citesAsSourceDocument`; `schema:isBasedOn` / `eli:based_on` [M for eli] | good |
| restatement by a secondary source, drift either way | `prov:wasDerivedFrom` + `cito:containsAssertionFrom`; drift itself has no standard term (closest: `cito:qualifies`, `extends`) | partial. The *direction* of drift (strengthening / weakening) is ours |
| summary of, may add | `prov:wasDerivedFrom` / `pav:derivedFrom` ("further refined or modified") | partial. "Adds content not in the source" has no standard flag |
| same claim refiled in another container | not derivation but *identity of content*: LRM same Expression, different Manifestation; or micropublication *similogs* (§7) | good, if the record distinguishes text identity from claim identity |
| channel variants of one finding | `prov:alternateOf` ("present aspects of the same thing"); LRM expressions of one Work | good |
| one text, several publishers | LRM: one Expression, several Manifestations; `schema:LegislationObject` ("the same Legislation can be published in multiple files") | good |
| within-document boilerplate | none found | ours |
| via an intermediary recorded by the source | PROV qualified derivation with an intermediate entity; `pav:sourceAccessedAt` for our side | partial |
| versioned within an author | `prov:wasRevisionOf`; `pav:previousVersion` / `hasCurrentVersion`; Akoma *Expression* versions | good. *Announcement status* is ours |
| amendment | `schema:legislationAmends`; Akoma textual mods | good |
| rescinds / replaces; orders revision of; withdrawn | `legislationRepeals`; `prov:wasInvalidatedBy`; `cito:retracts`; Akoma `endOfEnactment` | good for repeal and withdrawal. **"Orders revision of"** (an external instruction) has no term |
| tasks → fulfils; implements; reports against; interprets | `legislationEnsuresImplementationOf`, `legislationTransposes`; Akoma `implementation`, **`authenticInterpretation`** (meaning mod) | good for implements/interprets. *Tasks → fulfils* and *reports against* are ours |
| preempts / carves out / disapplies; deemed equivalent | Akoma `exceptionOfScope`, `inapplication` | partial. Preemption across jurisdictions has no term found |
| same text, new force | Akoma `forceMod` / `legalSystemMod: republication, reiteration, conversion`; `legislationLegalValue` | good for the concept, but these are legal-instrument terms applied to a company document, which is our extension |

**Strains.**
- PROV relates *entities* by derivation and says nothing about whether two texts make the *same claim*. The repo's most important lineage question ("is this agreement, or one sentence propagating?") is about content identity, so it needs LRM/micropublication-style identity alongside PROV.
- **"Primary source" collides.** PROV's is the historian's sense ("direct experience … without benefit from hindsight"). The repo's `channel: primary` means *read by us in the source itself rather than via a relay file*, which is PAV's retrieved/imported distinction. Using `prov:hadPrimarySource` for the channel field would be a category error.

---

## 7. Claim-level records: micropublications and nanopublications

### 7.1 Micropublications

Clark, T., Ciccarese, P. N., Goble, C. A. (2014). "Micropublications: a semantic model for claims, evidence, arguments and annotations in biomedical communications." *J. Biomedical Semantics* 5:28, doi:10.1186/2041-1480-5-28, CC-BY, read via PMC4530550 [V].

- *"The minimal form of a micropublication is a statement with its attribution. The maximal form is a statement with its complete supporting argument, consisting of all relevant evidence, interpretations, discussion and challenges brought forward in support of or opposition to it."*
- *"Sentences need not be syntactically complete – they may consist of a phrase, single word, or single meaningful symbol (e.g. 'We hypothesize that', 'Often', '¬'). Declarative Sentences are Statements. Sentences which qualify a Statement are Qualifiers. The principal Statement in an argument is called a Claim."*
- *"A Representation assertedBy a Micropublication is originally instantiated by that Micropublication."* *"A Representation quotedBy a Micropublication is referred to by that Micropublication, after first being instantiated by another Micropublication."*
- *"The supports property is a transitive relation between Representations."* *"The challenges property is inferred when a Representation either directlyChallenges another, or indirectlyChallenges it by undercutting … a Representation which supports it."*
- Similogs: *"Groups of similar statements are equivalence classes, defined as having 'sufficient' closeness in meaning to a representative exemplar, or Holotype Claim."* The model *"allows similar claims to be normalized to a common natural language representation, without dropping necessary qualifiers and hedging."* And the key line: **"identification of statements as being similogs is itself an assertion. Your 'similarity' may not be my 'similarity'"**.
- On citation chains: *"Greenberg's analysis of the distortion and fabrication of claims in the biomedical literature demonstrates why citable claims are necessary."* *"Citable claims are a specific remedy for citation distortion by allowing ready comparison of what is cited, to what the citation is claimed to assert."*
- On nanopublications (figure caption): *"Nanopublications include a named graph called 'Support', but this is actually a set of Qualifiers used for filtering, rather than the supporting evidence and citations."*

**Fit.**
- The minimal form (statement plus attribution) is the repo's assertion.
- `quotedBy` vs `assertedBy` is compilation-not-adjudication in one distinction: the model *quotes* everything and *asserts* nothing of the sources'.
- Qualifiers as verbatim sentences matches "the source's own hedge always stays verbatim beside any coding of it".
- "Similarity is itself an assertion" is SCHEMA-SYNTHESIS §1's "a resolution is always an attributed assertion". The similog/holotype structure is the honest way to say "same claim refiled" without merging the records.
- Greenberg's citation-distortion work (cited, not read; Greenberg, *BMJ* 2009 [M]) is the empirical precedent for *correlation is not corroboration*.

**Strain.** `supports` is declared **transitive**. A corroboration view built on it would propagate support through chains, which is the inference the repo's lineage-aware corroboration exists to prevent. Argument structure itself (supports / challenges / undercut) is the sibling speech-acts agent's territory; I note the overlap only.

### 7.2 Nanopublications

*Nanopublication Guidelines* (working draft), https://nanopub.net/guidelines/working_draft/ [V; `nanopub.org` no longer resolves]. Groth, P., Gibson, A., Velterop, J. (2010). "The anatomy of a nanopublication." *Information Services & Use* 30:51–56, doi:10.3233/ISU-2010-0613 [V: DOI metadata only; text not read]. Kuhn, T., Dumontier, M. (2014). "Trusty URIs." arXiv:1401.5775 [V: abstract].

- *"A nanopublication consists of an assertion, the provenance of the assertion (simply called 'provenance'), and the provenance of the whole nanopublication (called 'publication info')."* Each part is an RDF graph, linked from a head graph. The provenance graph *"MUST contain a link to the assertion graph identifier"*. The publicationInfo graph's subject *"MUST be the nanopublication URI and SHOULD contain attribution and timestamp."*
- Trusty URIs: *"include cryptographic hash values in URIs … resources keep their hash values even when presented in a different format."*
- [M] "The smallest unit of publishable information" is the usual gloss from Groth et al. 2010, not checked.

**Fit.** The assertion / provenance / publication-info split separates *what the source said and where* (provenance) from *who made this record, when, and with what agent* (publication info). The repo has the first in rich form and the second only implicitly (git history, the `channel` field). Content hashes are the address theory's "match at its most designator-like" (`def-match.ud`). Applied to anchored passages, they would make "verbatim copy" detection a computation rather than a judgement.

**Strain.** Nanopublication assertions are formal RDF. The repo keeps natural language verbatim, so micropublications fit better.

---

## 8. DDD's own vocabulary, since the project borrows it

Evans, E. (2015). *Domain-Driven Design Reference: Definitions and Pattern Summaries.* Domain Language, Inc., CC-BY 4.0. https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf [V]

- **context**: *"The setting in which a word or statement appears that determines its meaning. Statements about a model can only be understood in a context."*
- **bounded context**: *"A description of a boundary (typically a subsystem, or the work of a particular team) within which a particular model is defined and applicable."* The pattern summary adds: *"Model expressions, like any other phrase, only have meaning in context."*
- **Context Map**: *"Identify each model in play on the project and define its bounded context. … Describe the points of contact between the models, outlining explicit translation for any communication, highlighting any sharing, isolation mechanisms, and levels of influence. Map the existing terrain. Take up transformations later."*
- **Anticorruption Layer**: *"As a downstream client, create an isolating layer to provide your system with functionality of the upstream system in terms of your own domain model. … Internally, the layer translates in one or both directions as necessary between the two models."*
- **Conformist**: *"Eliminate the complexity of translation between bounded contexts by slavishly adhering to the model of the upstream team."*

**Fit and naming.**
- Evans's *Context Map* is the whole map of contexts and their relationships. In this repo that is closer to `source-catalog.md` (with its *Influence* grouping) plus the lineage relations.
- The per-source document the CLAUDE.md calls a "context map" (term → our concept, with rationale) is, in Evans's pattern language, the **translation inside an anticorruption layer** for one upstream context.
- **Adopting a source's definition** ("adopted" rows, e.g. IASR's four in `def-risk.ud`) is **Conformist** at the level of a single term.
- "Map the existing terrain. Take up transformations later." is a good one-line warrant for compilation-not-adjudication from the tradition the project names.
- Whether to keep "context map" for the per-source document is Joseph's call. A methodology document that cites Evans should at least say the repo uses the phrase more narrowly.

---

## 9. Collisions in our own meta-vocabulary

The project's working rule (coinage where established vocabulary exists is a smell) cuts both ways: borrowing an established word in a different sense is also a smell.

| Our word | Its established sense(s) | Where it collides |
|---|---|---|
| **designator** | ISO 1087 3.4.1: an admitted term for *designation*, a sign for a concept | `def-match.ud`: a reference that reaches its referent through a binding (Kripke/Donnellan lineage) |
| **broad / narrow** | SKOS/SSSOM: object broader / narrower than subject. ISO 1087: broader concept = narrower intension | repo lexical maps: "theirs is wider", read source → ours, which is inverted (§2.3) |
| **primary** (source) | PROV: direct-experience historiographic source | `channel: primary` = read by us in the source, not via a relay |
| **context map** | Evans: the map across all bounded contexts and their relationships | the per-source term-translation document (≈ an ACL's translation) |
| **domain / scope / subject** | ISO 1087: domain is purpose-bounded special knowledge; subject is an area of interest. Address theory: scope is the jurisdiction of bindings | the lexicon will need all three. ISO "domain" ≈ a bounded context; the address theory's "scope" is finer (document, section, purpose-indexed) |
| **concept** | ISO 1087 3.2.7 Note 2 itself warns the term means different things in different domains; SKOS says "suggestive, rather than restrictive"; OntoLex distinguishes LexicalConcept from ontology entity | the repo's `concepts*.yaml` "concepts" are mostly *quantities* in the model plane, not terminological concepts |
| **exact** | SKOS: transitive and symmetric, interchangeable across a wide range of applications | repo `exact` rows often mean "same definitional content" |
| **homonym** | ISO 704 7.7.5 polysemy and homonymy [M for content] | the repo uses it for "same word, different concept here", correctly in ISO's sense, but it is not a mapping relation in SKOS/SSSOM |
| **mapping** | ISO 25964-2 distinguishes mapping (gerund, the process) from mapping (noun, the product) | worth the same split in the methodology: the act of mapping (by an agent, dated) vs the row |

---

## 10. My read, for the methodology document

These are suggestions, not findings.

1. **Cite ISO 860 + ISO 704 for "concepts before names", and Temmerman for why the source side is semasiological.** Name the two directions; the methodology needs both.
2. **Decide the broad/narrow direction now** (SKOS/SSSOM direction, or non-SKOS words), and state the intension/extension point once.
3. **Model a context-map row as an OntoLex-style *sense*** (source word + its scope → our concept, with rationale, conditions and confidence), **serialisable as SSSOM** for the type-level per-term map. Keep the address theory's **resolution record** for occurrences (outcome incl. ambiguity with candidates, path, as-of, author). Each standard covers the layer it was designed for; none covers the occurrence layer.
4. **Anchor passages with W3C selectors**: page FragmentSelector (RFC 8118) refined by TextQuote, an optional position, a document version/TimeState, and **a recorded match count against {1,1}**. Tables need a project-defined selector.
5. **Lineage**: use PROV for generic derivation and revision; PAV for retrieved/imported/derived/accessed (extraction condition) and author/curator/creator; CiTO for citation function and shared authorship/funding; LRM Work/Expression/Manifestation for "same text, several places"; Akoma Ntoso and the schema.org/ELI terms for legal change, including force vs efficacy and `authenticInterpretation`. What remains genuinely ours: drift direction, "summary that adds", within-document boilerplate, "tasks → fulfils", "orders revision of", "reports against", announcement status, and cross-jurisdiction preemption.
6. **For lexicon entries that adopt a source definition, use ISO's `[SOURCE: …, modified — …]` form.**
7. **Corroboration views must not inherit transitivity** from `skos:exactMatch` or micropublication `supports`.

---

## 11. Verification ledger

| Source | What was read | Route | Mark |
|---|---|---|---|
| SKOS Reference (W3C Rec 2009-08-18) | §3.1, §5, §7, §8.1, §10 in full | curl + pandoc, grep | V |
| SKOS Primer (W3C Note 2009-08-18) | §2.2, §2.4, §4 | same | V |
| PROV-DM / PROV-O (W3C Rec 2013-04-30) | definitions in §5.1–5.5; PROV-O §3 overview | same | V |
| Web Annotation Data Model (W3C Rec 2017-02-23) | §3.3.5 head, §4.2 (all selectors), §4.2.9, §4.3.1 | same | V |
| URL Fragment Text Directives (WICG draft) | §3.2 syntax | same | V |
| RFC 8118 | §3 | curl | V |
| SSSOM schema (v1.0.0 and master `667d3c5`), docs, SEMAPV TSV | slot descriptions, enums; 4 doc pages | curl from GitHub, parsed YAML | V |
| Matentzoglu et al. 2022 (SSSOM paper) | intro, provenance, limitations | PMC BioC full text | V |
| OntoLex-Lemon CG report 2016 | §3 core, §3.4, vartrans 6.2 | curl + pandoc | V |
| IFLA LRM 2017-12 | LRM-E1–E5, E9 with attributes | PDF, pdftotext | V |
| PAV 2.3.1 ontology | property comments | curl (RDF/XML) | V |
| CiTO 2.9.0 ontology | property comments | curl (Turtle) | V |
| Micropublications (Clark et al. 2014) | abstract, methods, results outline | PMC BioC full text | V |
| Nanopublication guidelines | whole page | curl nanopub.net | V |
| Trusty URIs (Kuhn & Dumontier) | abstract | arXiv | V |
| Groth et al. 2010; Kuhn et al. 2016; PAV 2013; Peroni & Shotton 2012 | bibliographic metadata only | Crossref API | V (metadata) |
| Akoma Ntoso v1.0 Part 1 + `akomantoso30.xsd` | §4.1.3 FRBR, §5.10.2, mod enums | curl from docs.oasis-open.org | V |
| schema.org legislation terms | rdfs:comment of each | schema.org JSON-LD | V |
| ELI ontology (OWL) | not read: endpoints failed | — | M |
| Evans DDD Reference 2015 | definitions, Bounded Context, Context Map, Conformist, ACL | PDF, pdftotext | V |
| ISO 704:2022 | Foreword, Intro, 1–4, 5.1–5.4.4, TOC | iTeh preview PDF | V·preview |
| ISO 1087:2019 | Intro, 3.1.1–3.4.2 | iTeh preview PDF | V·preview |
| ISO 860:2007 | Intro, 1–4.2.3 | iTeh preview PDF | V·preview |
| ISO 25964-2:2013 | clause 3 to 3.42, TOC | iTeh preview PDF | V·preview |
| ISO 30042:2019 (TBX) | clause 3 | iTeh preview PDF | V·preview |
| TBX administrativeStatus values | picklist | TEI `isotei.rnc` via `gh search code` | V·2nd |
| ISO 704 §6.4.4, §7.6.2, §7.7 content; ISO 25964-2 §11 content | — | memory | M |
| Wüster 1979 | — | memory (named as Vienna School in the Temmerman record) | M / V·2nd |
| Temmerman 2000 | abstract | VUB research portal | V (abstract) |
| Hypothesis fuzzy anchoring; Greenberg 2009; Cabré; Faber | — | memory | M |

---

## 12. On the brief, and adjacent things noticed

- **The brief worked well.** Naming the suspected standards *with the explicit "from memory, may be wrong"* made the checking straightforward, and the agent's broad/narrow warning was exactly right. The one thing I'd add next time is the repo's own legend lines (`def-actors.ud` L37, `mappings.yaml` L2–3). I found them by grep, but a future spike could miss that the convention is stated in two places.
- **The Turtle-export line in `model-beta/README.md` (L73)** is where the inversion would bite first. If anyone revives that export before iteration 3 settles the direction, every hierarchical row flips.
- **SEMAPV now has `LLMBasedMatching` and `AgentBasedMatching`.** The repo's mappings are agent-made, so the honest justification vocabulary exists. If it's adopted, a row could say *agent-based, then human-reviewed* (`reviewer_id`), which is the repo's actual workflow.
- **The `ref/` texts that are git-ignored** (IASR 2026 full) fall under the Web Annotation copyright note. If passage anchors ever carry long `exact` strings from those texts, that becomes a publication question for a public repo.
- **The address theory has an independent convergence worth noting:** LRM's *nomen* reifies the name–entity association exactly as `def-binding.ud` does, including identical strings remaining distinct associations. If the theory's working notes collect convergences (they cite scope-graphs this way), LRM belongs there.
- Nothing in the repo was modified except this file. No commits were made.
