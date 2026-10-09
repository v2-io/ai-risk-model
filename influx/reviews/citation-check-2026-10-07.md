# Citation check: model gamma plan, against its outside sources

> [!NOTE]
> **Line and page references here predate `ref/canonical/`.** They were taken from `pdftotext -layout` extractions of the relata PDFs (the `bin/extract-text` script), before the canonical page-marked texts existed. Page numbers are the PDF's physical pages and still hold. Line numbers ("L…") are lines of those layout extractions, so they won't match `ref/canonical/`: to re-find a passage, search for its quoted words, or regenerate the layout text with `pdftotext -layout`. References marked "md" are lines of `ref/iasr-2026-full.md`, which is unchanged.

*2026-10-07. Claude (Opus 5.5), at Joseph's request (relayed by the session agent), so that Joseph can consult it while reading `MODEL-GAMMA-METHODOLOGY-AND-PLAN.md`. The question was whether each quoted or cited claim says what the plan, or the research reports under it (`influx/gamma-research/`), says it says. Line numbers are the plan's as of commit `b8749f3`.*

## How this was checked, and what that is worth

- **Coverage.** I checked every citation to a source outside this repository that I could identify in the plan, plus the research-report passages they rest on. The work was split into six clusters: law and EU; IASR, Anthropic, MIT and NIST; UK, AISI and the agent-architecture sources; terminology and provenance standards; speech acts, argument and norms; risk formalisms. I did DDD and udon myself and gave the other five to forks of myself. Each fork wrote up its findings, and I re-checked the most consequential ones at the primary (Hart, IASR's disclaimer, the 1,200 count, Art. 3(8), SB 53 §22757.11(d)(4), EC guidelines fn 12, the IAT quotation, R2P2 ¶136).
- **Against what.** Each check was against the source text itself:
  - corpus documents: fresh `pdftotext -layout` extractions of the relata PDFs, or the research agents' extractions where those proved byte-identical;
  - outside literature: re-downloads, usually from the research reports' own URLs, compared with the research agents' copies (every one compared matched);
  - the live gov.uk PHIA page and SEP "Risk";
  - R2P2 from the Internet Archive, since the hse.gov.uk URLs now 404;
  - OMB A-130 from whitehouse.gov;
  - Grüninger & Fox from an OCR'd scan.
- **Not reached.** Hart's *Concept of Law* text (lending-only), FM 2-22.3 Appendix B (Admiralty), the full ISO standards (previews only, as the plan says), and Guide 51 itself (witnesses only, as the plan says).
- **Independence.** This is the same model family as the plan, the research reports and the spike. It checks text against text, which is the part a same-model reader can do honestly. It does not provide the cross-family review the plan's §6 recommends.
- **Verdicts.** **Holds**; **holds, with nuance** (the citation is right but something a reader needs is missing); **imprecise** (wording or scope off in a way that could mislead); **not supported** (the source doesn't say it, or says something else).

---

## The short version

Most of the plan's outside citations hold verbatim at the cited place. That includes all the DDD quotations, every address-theory term, SSSOM, SKOS, OntoLex, Web Annotation, PAV, PROV, CiTO, SACM, IG 2.0, von Wright, Hohfeld, the SRA glossary, Kaplan & Garrick, the STPA Handbook, the CAA bowtie steps, MIT's "Other" definitions, Anthropic's two misalignment-risk definitions, and the SB 53 components. The research reports' read-at-the-primary marks were accurate in nearly every case tested. There is one exception (the IAT quotation, below).

The defects are of three kinds.

1. **Things the sources don't say.**
   - **Hart's "final but not also infallible" is not Hart's wording.** It is Kloosterhuis's unquoted paraphrase.
   - **SB 53 does not import "foreseeable" or "materially contribute" from California law.** That is our reading, so it needs marking as ours.
   - **The EC guidelines' fn 12 treats weight control as an evidential factor ("may be"), not an operative fact that confers a role.**
   - **IASR doesn't "make no recommendations".** It disclaims "specific *policy* recommendations".
   - **The "about 1,200" count sums to 993.**
2. **Wording or scope tightened past the source.**
   - **Buhl et al. "recommend" bow-tie:** the source says "may be useful".
   - **SB 53 excludes an evaluation:** it excludes one "designed to elicit this behavior".
   - **The R2P2 quotation is not verbatim.**
   - **The "operator" umbrella in AI Act Art. 3(8) is listed wrong.**
   - **The STPA drift is attributed to the wrong author.**
   - **"Chu et al." is one author.**
3. **Evidence marks flattened in the plan's prose.** The research reports mark some items as read via a secondary source, an abstract, a preview's table of contents or memory. The plan sometimes repeats them without the mark: Temmerman, the ISO acceptability values, the Admiralty grading, Searle's mode of achievement and indirect force, the "ISO" event note, and Hart. §8 says claims resting on the reports "rest on their verification marks", but a reader of the plan alone doesn't see those marks.

None of these undoes a recommendation in the plan. Several strengthen it: the RAISE "person" difference, the FCF's narrowed threshold, the Code's own import clause, and Grüninger & Fox.

---

## Findings by plan section

### §1.3 What the corpus turned out to be

- **L78, the EU loss-of-control formula "recurs in nine later documents": holds, with nuance.** A grep over all 214 extractions finds nine:
  - quoting it as the Code's: Barrett, METR, Stix;
  - adopting it verbatim: xAI 2026;
  - embedding it: OpenAI FGF;
  - paraphrasing it: Microsoft 2026, Meta 2026 (which adds "contain" and "cannot feasibly regain"), Amazon 2026, and GDM's Sep 2025 blog.

  But "recurs" covers three relations (attributed quotation, unattributed adoption, paraphrase with changes), which §3.7 wants recorded separately. That the paraphrases derive from the Code is inferred from shared wording; none of them says so. A tenth, Tkeshelashvili (IST 2026), paraphrases GDM's wording, so it is a second-generation copy. OVERVIEW itself says "at least six" at L50 and "nine" at L376 and L687.
- **L79, the ">50 people or $1B" threshold "recurs in four, under two names": the count holds; the content is not identical.**
  - xAI 2025 quotes it with attribution, and RAISE copies it.
  - Anthropic's FCF v2 (L116–118) and OpenAI's FGF (L120–127) relabel it "systemic risk". They also narrow "death of, or serious injury to, more than 50 people" to ">50 fatalities", dropping the serious-injury arm, and make it a floor example ("including but not limited to"). The FCF also has "1 billion dollars of financial damages" where SB 53 has "damage to, or loss of, property".
  - For competency question 1 (60 deaths) the versions agree; an injury-heavy event would split them.
  - METR and FLI only quote it, which is citation, not adoption.
- **L80, Shanghai's glossary is "primarily based on" IASR 2025: holds, with one inference.** The footnote (Shanghai framework L2085) says "primarily based on the International AI Safety Report", with no edition named. The 2025 edition is a sound inference: the framework dates from Jul 2025, says "builds upon the International AI Safety Report (January 2025)" (L295), and cites arXiv 2501.17805. A lineage record should mark the edition as inferred.
- **L83–90, SB 53 §22757.11(c): each component is verbatim. "One sentence" is not exact.**
  - The exclusions are a separate paragraph, (c)(2).
  - The definition also reaches outside (c): "property" is defined in (l), and §22757.16 says "The loss of value of equity does not count as damage to or loss of property" (Labor Code §1107.2 repeats it). A clause-by-clause round trip of (c) alone (acceptance test 1) would miss both.
- **L94–96, the EU Code's interpretation clause: "shall prevail" and "grammatical variations" hold verbatim (Code L1136–1142). "Purposive" is slightly overstated.**
  - The binding "shall" attaches to reading "in light of the objective to assess and mitigate systemic risks". Purposive interpretation is something the Signatories "recognise … is particularly important" (L141–145).
  - The same clause holds two more source-declared resolution policies the plan could cite:
    - Appendix 1 is to be read "in instances of doubt, in good faith in light of" AI Act Art. 3(2) and 3(65);
    - the chapter is to be read "in conjunction and in accordance with any AI Office guidance" (L147–151).

    The second is a cleaner case of "imported from an outside institution" than SB 53's "foreseeable" (see §3.4 below).
- **L98, SB 53 §22757.14: the quotations hold. Two precisions.**
  - The statute says "before beginning to train or deploy", not just before training.
  - The Department of Technology only *recommends*; the Legislature changes the definition. So the reviewer and the maintainer, in address theory's sense, are different parties. That bears on L241 (below).
- **L99, SB 53 defines "catastrophic risk" twice: holds.** Labor Code §1107 swaps "frontier model" for "foundation model", and its first kind of critical safety incident adds "or damage to, or loss of, property". The actor is still a *frontier* developer.
  - L267's "two of the codes it amends" is loose: SB 53 *adds* chapters to the Business and Professions Code and the Labor Code.
- **L99, IASR 2026's glossary and body define loss of control differently: holds.**
  - "With no clear path to regaining control" appears in the glossary (md L2382) and the summary's key findings (md L426).
  - "Regaining control is either extremely costly or impossible" appears in the §2.2.2 key-information box (PDF p. 76) and the §2.2.2 body (PDF p. 77).
  - The chapter states its wording twice, which supports reading it as a definition. That settles L245's "if the body's wording counts as a definition".
  - The two conditions are not equivalent: one is about whether a way back exists, the other about what it costs.
- **L100, Anthropic's "We acknowledge that the distinction between known and unknown is not crisply defined": holds** verbatim (August Risk Report §2.5, p. 24, L926–927).
- **L100, "MIT's causal taxonomy uses a single 'Other' level for three different things": holds, if read as Entity's three.** Entity "Other" merges interaction, ambiguous and unspecified. Timing "Other" merges two things; Intent "Other" is one ("without clearly specifying the intentionality").
- **L100, "IASR 2026 is inconsistent with itself on several key terms": holds for the two terms checked.**
  - Loss of control, above.
  - Misalignment: the glossary (md L2398) has a "propensity to use its capabilities in ways that conflict with human intentions, values, or norms"; §2.2.2 (md L1240) has "'misaligned', meaning they have goals that conflict with the intentions of developers, users, or society".

  No further terms were enumerated.

### §2 Principles

- **L115, L118, L119: Joseph's quotations hold** against his own typed turns in the session transcript (2026-10-06 22:22Z and 23:12Z).
- **L124, the coinage rule: holds.** It is Joseph's, 2026-08-09 (`~/.claude/history.jsonl`, verisectorium). There it is two separate quoted sentences, introduced as "this little heuristic" that came out of a renaming exchange. Verisectorium's `claim-naming-criteria.md` joins them with a semicolon and attributes them to "Steward, 2026-08-09".
- **L125, Evans's "a change in the language is a change to the model": holds** verbatim (Ubiquitous Language pattern).

### §3.1 Two directions of work

- **L138, ISO 860, "Harmonization starts at the concept level and continues at the term level": holds** verbatim (Introduction). The research agent's preview download is byte-identical to a fresh fetch.
- **L138, ISO 704: holds.** "assigning a designation to the concept" is the last of the seven steps in §5.4.2.
- **L139, Temmerman 2000: holds, but only at abstract level.**
  - Read: the publisher's abstract. The research report marks it "V (abstract)"; the plan doesn't say so.
  - "A combined semasiological and onomasiological perspective" and "synonymy and polysemy are functional" are in the abstract.
  - "Drift … normal, not defects" is the plan's gloss of the abstract's "a diachronic approach is unavoidable".
- **L140, ISO 860 §4.2.2: holds.** The plan quotes conditions (b) and (c) correctly. ISO's modal is "more likely to be possible if". The omitted condition (a) is also one that frontier-AI risk fails, so including it would strengthen the point.

### §3.2 The vocabulary for the method itself

- **L148–155, the DDD Reference: every quotation holds** verbatim. These are:
  - bounded context;
  - context;
  - "Map the existing terrain. Take up transformations later.";
  - conformist, "slavishly adhering to the model of the upstream team";
  - shared kernel, "agree to share" (the plan's "with consultation" compresses "shouldn't be changed without consultation with the other team");
  - anticorruption layer, "create an isolating layer … in terms of your own domain model".

  The Context Map pattern's text ("Identify each model in play on the project … Describe the points of contact between the models") supports the L175 reading that Evans's context map is the map *across* contexts. The CC BY 4.0 licence is confirmed.
- **L157, separate ways and big ball of mud: both quotations hold verbatim.**
- **L157, the RSP's "plain meaning" "catastrophic" as "deliberately unbound": holds, with nuance.** RSP v3.4 fn 1 (identical in v3.0) reads: "'Catastrophic risk' as used in our RSP refers generally to risks of the most severe potential harms from advanced AI, such as existential threats or fundamental destabilization of global systems. We use this term in its plain meaning rather than adopting any specific statutory definition."
  - So the term is not bare: it carries a gloss with examples.
  - It also explicitly *declines* a statutory binding, pointing to "separate compliance frameworks".
  - The resolution record would be "declined (statutory) + plain meaning, glossed", not just "deliberately unbound".
- **L152, xAI adopting the Code's terms: holds.** xAI 2026 fn 1 reads "Terminology used in the The Safety and Security Chapter of the General-Purpose AI Code of Practice".
- **L152, RAISE copying SB 53's definitions word for word: holds for the wording, apart from spelled-out numbers and numbering. One substantive exception.** RAISE adds "'Person' means … or any other nongovernmental organization" (raise p. 4). So the identical "frontier developer" wording reaches a different set of referents: under RAISE a governmental body cannot be a frontier developer. That is a clean instance of finding 5 (terms scoped finer than documents). The repo holds the bill as introduced; the signed text is known only second-hand.
- **L159–165, address theory at `90f4fb6`: every term holds.**
  - The pin is 2026-08-27, on `origin/main`, and the public tree URL resolves. The seven `def/*.ud` files are unchanged between the pin and current HEAD.
  - The terms checked: reference and referent; intended cardinality; binding, mint and maintainer vs match ("a test is run at the moment of use"); scope with containment ("the unit within which bindings are kept and collisions counted"; `namespace` is the entry's own listed synonym); resolution from an origin, as of a moment, with its path, under admissibility and preference; ambiguity, "an outcome, not an error"; dangle and collide.
  - Three things not wrong, but worth knowing when the terms are imported:
    - **Two senses of "ambiguity".** Address theory's ambiguity is "More than one maximally-preferred result", which is structural, a fact about the resolution. The plan's §3.4 also uses it for "a fact about our reading: we can't tell which candidate is meant", which is epistemic. The plan keeps outcome and reason apart, so this is not a contradiction, but the one word does two jobs.
    - **Two collisions the plan's tables don't list.** `def-binding` gives `:synonyms [declaration]` ("the scope-graphs literature's word"), which collides with Searle's *declaration* (L332). `def-scope` gives `:avoid [context region]`: address theory deprecates "context" as a word for scope, while L167 proposes defining DDD's bounded context *in terms of* scope.
    - **Status.** All seven entries carry `:status proposed`. The plan calls them "the quality bar" (L123), which is faithful to Joseph's words; their own recorded status is still `proposed`.
- **L176, ISO 1087: holds.** "Designator" is an admitted term for *designation* (3.4.1). **L176, `def-match.ud`'s designator: holds** ("A reference (or component of one) that reaches its referent through a @{binding} on its name").
- **L178, SKOS `broadMatch` direction: holds.** SKOS §10: "<A> skos:broadMatch <B> … (where <B> is broader than <A>)". SSSOM: "`broad`: The object is conceptually broader than the subject."
- **L179, Toulmin's qualifier: holds**, via Verheij 2005 ("it follows presumably").

### §3.3 The lexicon

- **L208, intensional definitions: two wording slips against ISO 1087 itself.**
  - 3.3.2 defines an intensional definition by "the immediate **generic** concept … and the delimiting characteristic(s)", where the plan says "the immediate broader concept".
  - In ISO 1087, "broader concept" (3.2.15) is an admitted term for *superordinate* concept, which covers both generic and comprehensive (whole-part) relations.
  - It matters only because this is the lexicon's own terminology standard.
- **L209, acceptability status "preferred, admitted, deprecated": partly read.**
  - The ISO 1087 preview shows "preferred term(s)" and "admitted term(s)". ISO 704's table of contents lists "7.7.7 Acceptability rating", but the preview stops before its content.
  - "Deprecated" appears in none of the five ISO previews. The research report marks it as from memory, with TBX's `deprecatedTerm` supported only by a secondary source.
  - The plan says these values are "read in the previews".
- **L210, `[SOURCE: …, modified — …]`: holds.** The marking appears in the previews.
- **L213, "ISO's concept is static": our inference, not a reading.** No preview mentions time or change, and the full standards were not read.
- **L214, "no mapping standard the research checked (SKOS, SSSOM, OntoLex, Web Annotation) can say 'one of these, undetermined'": holds.** Grepped in each, including current SSSOM master.
  - Adjacent: OntoLex calls a lexical entry with several `denotes` links "ambiguous". That is type-level, and close to the plan's *declared ambiguity*, so it is worth citing as a near-precedent.
- **L229–232, MIT: holds.**
  - 1,725 risks from 74 documents.
  - Table 1's Entity "Other" and Timing "Other" wordings are verbatim (p. 6).
  - "Other (21% of coded risks)" is at L154–156, in a sentence about entity attribution. The sentence doesn't name Entity itself; its context does. Supplementary Table S3 is roughly consistent (about 18–21%).
- **L241, SB 53's "frontier developer" as *bound*, "with a statutory annual review": imprecise.** §22757.14's review is of whether the definitions still reach what they should. Its reviewer (the Department of Technology, which recommends) and its maintainer (the Legislature, which amends) are different parties (see §1.3). Also, the plan's own example under L242–245 is "frontier developer", while §22757.14 is framed around "frontier model".
- **L245, IASR's two loss-of-control wordings as a candidate *collision*: holds as a candidate.** The chapter's wording appears twice (see §1.3), which favours treating it as a definition.

### §3.4 Per-source translations

- **L258, OntoLex-Lemon (Final Community Group Report, 10 May 2016): holds.** A lexical sense is "a reification of a pair of a uniquely determined lexical entry and a uniquely determined ontology entity". The `usage` property covers "usage conditions or pragmatic implications".
  - Nuance: OntoLex pairs the entry with an *ontology entity* and keeps a separate `LexicalConcept` class. The plan's "pair of word and concept" should say "ontology entity" if it adopts the term.
- **L259–265, SSSOM: holds.** Every field the plan names is already in v1.0.0: subject as a literal, `predicate_modifier: Not`, required `mapping_justification`, author, creator and reviewer IDs, `confidence`, and `NoTermFound`.
  - **L263, `AgentBasedMatching` "on the current main branch": understated.** It is in the SEMAPV *release* `v2026-06-02`. It is a SEMAPV term, the vocabulary SSSOM's `mapping_justification` draws on, not part of the SSSOM schema itself.
- **L267, SSSOM's "Mappings themselves have no context (i.e. are always true)": holds** verbatim (paper, "Discussion and limitations", presented as a deliberate design choice).
- **L267, IASR "uses 'developer' for organisations in one place and for individual people in another": not supported as written.**
  - Organisations: the glossary (md L2206) reads "AI developer: Any organisation that designs, builds, or adapts AI models or systems."
  - Individuals: IASR has no developer term that names individuals. Its second term, "Downstream AI developer: A developer who builds AI models, systems, applications or services using or integrating existing AI models or systems created by others" (md L2314), leaves the kind of agent unstated.
  - The individual uses are ordinary compounds or loose plurals: "software developers believed that AI was making them more productive" (md L670), and "the pool of developers and researchers" (md L2035).
  - One place contrasts "developers, governments, communities, and individuals" (md L489), treating developers as *not* individuals.
  - The spike's actor table (`04-actors.md` L187) attributes the individual sense to *model beta* ("organisational (IASR), individual (beta)"). As written, the plan's sentence reads as if IASR's own term shifts.
  - Fix: give locators for loose uses, or attribute the individual sense to model beta.
- **L269, "about 1,200 raw uses (count by the de novo review, including cited titles)": the per-term counts hold; the total does not.**
  - Re-running `grep -o -i` on `ref/iasr-2026-full.md` reproduces the de novo review's eight counts exactly: developer 193, safeguard 156, frontier 352, incident 103, threshold 75, loss of control 49, misalign 41, systemic risk 24. They sum to **993**.
  - The error is in the de novo review itself ("roughly 1,200", `gamma-de-novo-review.md` L162).
  - The raw counts also double-count: the markdown repeats each footnote's full reference in a link tooltip at every citation. With link targets stripped, the eight fall to about 730.
  - The selection-rule argument is unaffected. Suggested wording: "about 1,000 (993 by raw count, including footnote titles repeated at each citation)".
- **L278, "imported from an outside institution (California law for 'foreseeable')": not supported by the source.**
  - SB 53 neither defines "foreseeable" nor "materially contribute", nor points anywhere for them. Its only interpretive clause is SEC. 5(b): "This act shall be liberally construed to effectuate its purposes."
  - That the terms take California-law content is a reasonable legal reading, but it is ours and should be marked as ours.
  - SEC. 5(b) is itself a source-declared resolution policy that L93–98 could cite.
  - The EU Code's "in accordance with any AI Office guidance" (above) is an actual source-declared import.
  - The same applies to **L654**.
- **L282, IASR resolves the EU's "systemic risk": holds, with nuance.** IASR md L2522 quotes Art. 3(65) as "risk that is specific to the high-impact capabilities of general-purpose AI models, having a significant impact" and stops mid-definition. It drops "on the Union market due to their reach, or due to actual or reasonably foreseeable negative effects on …". That makes it a live example of a third-party resolution that truncates.
- **L282, "Anthropic's FCF files RSP thresholds under the statutory 'loss of control'": the filing holds; "statutory" is imprecise.**
  - FCF v2's loss-of-control tiers, "Misaligned AI systems in high-stakes settings" and "Automated R&D in key domains" (L340–361), are RSP v3.4 row names. RSP v3.4 fn 1 says statutory terms are handled "in separate compliance frameworks", which corroborates the filing.
  - But the FCF defines loss of control in its own words: "scenarios where AI models develop and pursue goals autonomously that conflict with their developers' intentions or users' interests" (L317–319).
  - The *category* is the EU Code's, and the Code is voluntary.
  - SB 53 uses "loss of control" only as an undefined phrase in its third kind of critical safety incident.
  - Suggested wording: "under the 'loss of control' category its compliance obligations require".
- **L294, "ISO 1087 notes that the broader concept has the narrower intension": imprecise.** ISO 1087 3.2.19 says this of the *generic* concept. (See L208 for broader vs generic.)

### §3.5 Passages

- **L298–302, Web Annotation (Recommendation, 23 Feb 2017): holds.** `TextQuoteSelector`, `TextPositionSelector`, `refinedBy`, and multiple selectors "in order to maximize the chances that it will be discoverable later".
  - Not a citation error, but relevant to a public repo: the same spec calls quote selectors over copyrighted text "potentially dangerous" and suggests position selectors for restricted texts. The proposed anchor leads with a quote selector, and the IASR text is git-ignored.
- **L304, RFC 8118 `page=N`: holds** (§3).
- **L306, "SHOULD be treated as matching all": holds** verbatim ("…matching all of the matches"). The address-theory counterpart holds too: `def-reference.ud` has "Three against {1,1} = the reference narrowed insufficiently".
- **L310–314, PAV: holds.** `importedFrom`'s own example is "a document scan, and this resource is the plain text found through OCR". Note that `sourceAccessedAt` is for a source "accessed or consulted (but not retrieved, imported or derived from)". So mapping "our reading" to *accessed* treats a reading as consultation, not derivation. That is coherent, but it is our reading of PAV, not PAV's own example.

### §3.6 Assertions

- **L322–328, Searle 1975, the five points: holds** (pp. 354–358). The 1979 rename to "assertives" rests on a secondary source, but it is well known.
- **L329, strength separate from point: holds** verbatim (p. 348 "I suggest … I insist"; p. 353 "hypothesizing that p and flatly stating that p are in the same line of business").
- **L330–331, mode of achievement and indirect force: the content holds, but the provenance is misplaced.**
  - Both sit under "Searle's taxonomy … (1975 chapter, read whole by the research agent)".
  - "To testify is to assert in one's capacity as a witness" is SEP "Speech Acts" §2.3, summarizing Searle & Vanderveken 1985.
  - Indirect force is Searle 1979 via SEP §3.4. In the 1975 chapter "indirect" occurs only in "indirect object".
  - The research report marks both as secondary; the plan's framing makes them read as part of the chapter read whole.
- **L332–334, definitions as declarations: holds** (p. 359, "I define, abbreviate, name, call, or dub"). The labels "institutional" and "linguistic" declarations are ours, not Searle's.
- **L335, determinations as assertive declarations: holds** (pp. 359–360, "representative declarations"; "The judge, jury, and umpire can, logically speaking, lie").
- **L335, "In Hart's words it is 'final but not also infallible'": not supported. The words are Kloosterhuis's, not Hart's.**
  - The only source behind it is Kloosterhuis (1998), who writes, without quotation marks: "Decisions of a court he says, are statements with a certain authority making them final but not also infallible."
  - Hart's *Concept of Law* has a section titled "Finality and infallibility in judicial decision" (ch. VII, p. 141, per search results). Its text could not be reached.
  - The research report (L99) also puts the phrase in quotation marks as Hart's.
  - Suggested fix: "Hart's distinction between finality and infallibility (*Concept of Law*, as paraphrased by Kloosterhuis 1998)".
- **L338, FactBank: holds** (⟨mod, pol⟩ "relative to a source"; "Izvestiya according to the author"). FactBank credits nested sources to Wiebe et al. 2005.
- **L339–343, PDTB attribution: holds, but two dimensions are merged.** In the PDTB 2.0 manual, claims, beliefs and facts (Comm, PAtt, Ftv) are values of the attribution's *Type*, while "arbitrary" (Arb) is a value of its *Source*. A record format that copies the plan's four-item list would conflate them.
- **L344, Goffman: holds, via the secondary source.** The secondary cites "1979: 144", but *Semiotica* 25 runs pp. 1–29, so the page is from *Forms of Talk* (1981). The IASR example holds (md L298).
- **L345, evidentiality: holds** (WALS ch. 77).
- **L350, ASPIC+ three attacks: holds** (arXiv 1804.06763 §3.2). The typology originates in Prakken 2010.
  - **SEI 2015: holds** ("the three (and only three) kinds of defeaters").
- **L351, "Defeat needs a preference ordering": overstated.** In ASPIC+ (Def. 9), undercuts and contrary-based attacks are preference-independent: "Undercuts always succeed as defeats". Only rebuttals and underminings on contraries need an ordering. The recommendation stands, better put as defeat being "computed under a declared ordering and semantics".
- **L352, IAT/AIF: the plan's sentence holds; a research-report quotation does not.**
  - Budzynska et al. (LREC 2014) supports the plan: logical structures are "'anchored' in dialogical structures via illocutionary connections".
  - **The research report's §5.2 quotation, marked [P]** ("Speech acts that form a part of argumentative discourse can be seen as anchors for the establishment of inferences between propositions"), **is not in that paper.** I also did not find it in the 2023 IAT guidelines (arg.tech).
  - A search engine lists the Konstanz *IAT-CI Guidelines* PDF as a hit, but that URL now returns an HTML page, so it is unconfirmed.
  - The plan doesn't quote it, but the report's mark is wrong as it stands.
- **L354, SACM 2.2: holds.** formal/21-11-01 §11.8 lists the six statuses; in §11.13 `AssertedRelationship` is a subclass of `Assertion`.
- **L355–357, Toulmin, Walton and linked/convergent premises: hold at the levels the plan states.**
  - "Methodology is the backing for a family of warrants" is the plan's proposal, not Toulmin's.
  - The expert-opinion scheme is SEP's generic version.
- **L361–363, IG 2.0: the components hold** (codebook v1.4, arXiv 2008.08937v5 §1, including "the conferral of status"). **"A coding grammar already applied to legislation" is true of the 1995 grammar** (Crawford & Ostrom's ADICO, applied to two US statutes by Basurto et al. 2010), not of IG 2.0.
  - Aside: Basurto et al. "discarded definitions, titles, preambles, and headings", so only IG 2.0's constitutive layer allows coding definitions at all.
- **L364–368, Hohfeld: holds**, including "claim" and "immunity (or exemption)". **"First order / second order" are not Hohfeld's terms.** They are later usage (Sumner 1987, via SEP "Rights").
- **L369, LegalRuleML (OASIS Standard 2021): holds**, covering the four statuses, status-changing events, and strong vs weak permission. "Most framework deployment conditions are strong permissions" is an uncounted claim about the corpus, and it isn't marked as one.
- **L370, von Wright: holds.** Norms "have no truth-value"; norm-propositions are true or false; technical norms and anankastic statements are defined in §7. "Presupposes" is von Wright's own word.
- **L374, "Institutional Grammar's 'norm' means a statement without a sanction": true of Crawford & Ostrom 1995, absent from IG 2.0.** The IG 2.0 codebook has no strategy/norm/rule typology. The collision entry should cite IG 1995.
- **L376, the worked consequence: the quoted IASR sentence holds** (md L2077, PDF p. 137, under "Challenges for policymakers"). **The paraphrase "declares that it makes no recommendations" broadens IASR.**
  - The full report says "It does not make specific policy recommendations" (md L364), and that its risk-management discussion "is descriptive … policy recommendations are outside the scope of this work" (md L1648).
  - The Extended Summary says it "does not recommend any policies" (L28).
  - The L2077 sentence is addressed to developers, not policymakers, so it may not breach the disclaimer at all. That supports the plan's technical-norm reading, but it weakens "Draft 2 treated this as a conflict" as a description of what the source does.
  - Quote IASR's actual words.

### §3.7 Lineage and corroboration

- **L381–388, PROV, PAV, CiTO (all ten relations, v2.9.0), IFLA LRM (LRM-E2 to E4), schema.org (`legislationAmends`, `legislationRepeals`, applicability and legal force): hold.**
- **L388, `termModification` and `authenticInterpretation`: they are Akoma Ntoso values (the `MeaningMods` group), not schema.org terms.** The plan's sentence lists them under the heading "Akoma Ntoso and the schema.org legislation terms", so this is about placement only. The gloss "a change in what a term means" fits `termModification` better than `authenticInterpretation`.
- **L400, transitivity: holds.** SKOS `exactMatch` is transitive, and micropublications say "The supports property is a transitive relation between Representations". Also citable: SKOS makes `closeMatch` *non*-transitive "to avoid the possibility of 'compound errors'", which is direct support for the plan's rule.
- **L401, the Admiralty grading: holds at secondary level only.** It rests on Wikipedia, and two Wikipedia pages word the top grade differently: "Confirmed by independent sources" and "Confirmed by other independent sources". The primary (FM 2-22.3 Appendix B, Table B-1) could not be reached. The research report marks this; the plan doesn't.
- **L403, micropublications (Clark et al. 2014): holds** verbatim.

### §3.8 The risk side

- **L409–413, the SRA glossary (2018 update): holds** verbatim. It covers the seven qualitative definitions, "None of these examples can be viewed as risk itself, and the appropriateness of the metric/description can always be questioned", (C′, Q, K) "which includes a judgment of the strength of this knowledge", and vulnerability "conditional on the occurrence of a risk source/agent".
  - MIT's definition is SRA definition 1: MIT says it "followed the Society for Risk Analysis" (`slattery` L700–702).
- **L416, Kaplan & Garrick: holds.** Hazard as doublets (p. 4 fn 3), "not the mean of the curve, but the curve itself which is the risk", the "other" scenario category assessed by Bayes, and probability of frequency.
- **L417, ISO 31000 Note 3: holds** via the official reproduction. **L456, "effect of uncertainty on objectives" and the positive/negative note: hold.**
- **L419–422, SP 800-30, the UN terms, bow-tie, Reason: hold.**
  - SP 800-30: a threat source can be "a situation and method that may accidentally exploit a vulnerability". Likelihood is assessed "with respect to a specific time frame (specified or implicit)", so L509's "always relative to a time frame" holds, but the frame may be implicit.
  - UN A/71/644: hazard, exposure, vulnerability and capacity; hazardous event, "The manifestation of a hazard in a particular place during a particular period of time".
- **L436–440, the CAA bowtie steps: every fragment holds** verbatim (Jul 2026, §2.4, p. 5).
  - **L496, "In bow-tie and SP 800-30, 'threat' explicitly includes accidental causes": explicit only for SP 800-30.** CAA's definition says "all conditions or factors"; accidental threats appear only in its worked examples (hose failure, human error).
- **L452, IASR's "bowtie method" row (md L1688, citing Koessler & Schuett): holds.** It is a row in a practices table, as the plan says. The research report's §2.6 calls it a "glossary entry".
- **L452, "Buhl et al. recommend it": overstated.** Buhl et al. (p. 7) list "the Fishbone method, scenario analysis, bow-tie analysis, and risk tree analysis" as techniques that "may be useful", inside "an example risk modelling process … could consist of". The plan's own lineage category "a hedge dropped, a claim hardened" applies.
- **L452, "ISO's event notes say an event's cause can itself be an event in a chain": not verified as ISO's.** The only witness is IEEE 7009-2024 §3.1, NOTE 7 ("The cause of an event can also be an event in a chain of events"). Unlike its neighbouring entries, that entry prints no source. The research report's attribution to ISO/IEC/IEEE 16085 is not on the page. Cite it as IEEE 7009's, or check ISO 31000 3.5 or Guide 73 3.5.1.3.
- **L455, the STPA Handbook p. 133, "effectiveness of the controls": holds.** **L455 and L481, AISI *Loss of Oversight*'s "severity" as STAMP's risk: the paraphrase holds; the equation overreaches.**
  - LoO p. 5 defines severity as "how badly that pathway would undermine the corresponding oversight channel".
  - But LoO rates every pathway on *likelihood* and severity, so its severity is a conditional magnitude inside a two-factor frame. STAMP's risk explicitly "does not require the determination of likelihood" (Handbook pp. 133–134).
  - Only the *object* of LoO's severity (the oversight structure) is STAMP-like.
  - The table row is marked as the research report's reading, but a column headed *Its "risk"* says more than LoO does.
- **L457, the IPCC counts risks from responses: holds** (AR6 WGII glossary: risks "from … human responses to climate change").
- **L459, Hansson's fifth sense: holds** (SEP "Risk", rev. 8 Dec 2022). The source's words are "the fact that a decision is made under conditions of known probabilities".
- **L475–481, the §3.8 table:**
  - **SB 53:** holds (see §1.3).
  - **EU AI Act and IASR:** Guide 51's form holds for IASR (md L2480, "The combination of the probability and severity of a harm") and for Art. 3(2).
  - **NIST:** holds.
  - **Anthropic:** holds verbatim (L969–971; fn 15 says "expected" is meant "in the sense of expected value").
  - **NRR:** holds. p. 14 has "the worst plausible manifestation"; p. 15 has the confidence ratings. Note that "Additional scenarios are provided for a single topic": one scenario *per risk*, with topics carrying several risks (flooding, 53a/b/c).
  - **MIT:** holds.
  - **LoO:** overreaches; see L455 above.
- **L484, H1: holds.** HSE R2P2 ¶39: "the potential for harm arising from an intrinsic property or disposition of something to cause detriment". For HSE the hazard *is* the potential, not the object, which puts it at the dispositional end of H1. ICAO: "A condition or an object with the potential to cause or contribute to an aircraft incident or accident".
- **L485, H2: holds** for IASR (md L2354, "Any event or activity that has the potential to cause harm, such as loss of life or injury") and the IPCC.
- **L488, H5, STPA's hazard: holds** verbatim (Handbook p. 17).
- **L489, H6, "the NRR's hazard, as opposed to threat": imprecise.** The NRR's operative division is non-malicious vs malicious *risks*. p. 8: "may be non‑malicious, such as accidents or natural hazards or they may be malicious threats". Hazards are one subset of the non-malicious side, beside accidents, not the side itself. This bears on decision 3's "departs from the NRR's own usage".
- **L490, H7 as "an eighth AI-literature sense": holds against Schnitzer et al.** ("AI risks' root causes - also called AI hazards"). Their next sentence says hazards "represent potential sources of harm", so root cause is framed as a specialization of H1.
  - Internal glitch: "eighth" counts against OVERVIEW §2.1's seven, while §3.8 numbers this item H7.
- **L495, "intent is carried on a separate axis" in every formal glossary checked: holds.**
  - SRA defines safety as "sometimes limited to … non-intentional events", and security as restricted to "intentional acts by intelligent actors".
  - SRA 1.18 also notes threat is "commonly used in relation to security applications", so there is a loose intent link in usage, though not in definition.
- **L508, PHIA probability over propositions, including past and present: holds.** gov.uk (24 Mar 2025): the likelihood "that a statement is true or that an event will occur, is occurring or has occurred". The separate analytical confidence rating holds too.
- **L516, ALARP and "gross disproportion": holds** (archived HSE ALARP page; *Edwards v NCB*).
- **L519, AISI's "19 events" across 10 of 122 runs: holds.** Report p. 8 defines an event as "an instance of unsanctioned behaviour that took effect outside the evaluation range". The blog adds "The 19 cases were not separate incidents; they clustered into a few connected behaviours", which is direct support for L522's merging point.
- **L520, CLTR's rubric-scored reports: holds.** "Claude Opus 4.6 classifies all remaining incident reports out of 9 … A 'loss of control incident' is a report that is classified as 5 or more out of 9." The classifier is a Claude model, which bears on the plan's conflict-of-interest note.
- **L520, SB 53's anonymized annual aggregates: holds** (§22757.13(g)(1)). This is a duty on the Office of Emergency Services; the first report is due 1 Jan 2027.
- **L528, "Whether AISI's cyber-range incident … counts as … loss of control … is where the sources disagree": weaker than stated.**
  - AISI never uses "loss of control" in the report or the blog. It says "unsanctioned action" and "security incident", and that "this was not a case of a model escaping its … 'sandbox'".
  - The only corpus source found linking the incident to loss of control is CLTR, implicitly ("later observed in the incident AISI disclosed").
  - So the disagreement is AISI's silence against CLTR's implicit grouping. The argument of the paragraph survives if it reads "how sources would file it".
- **L531, "did it happen inside an evaluation, which SB 53's fourth kind of critical safety incident excludes": imprecise, and the precise version matters here.**
  - §22757.11(d)(4) counts conduct "outside of the context of an evaluation *designed to elicit this behavior*", plus "deceptive techniques against the frontier developer" and "materially increased catastrophic risk".
  - A cyber-range evaluation not designed to elicit the behaviour is not excluded by that wording.
  - Stating the statute's criterion exactly is the paragraph's own point (criteria, not words).
- **L536, the HSE R2P2 quotation: not verbatim, and the scope is dropped.**
  - ¶136: "the risk of an accident causing the death of 50 people or more in a single event should be regarded as intolerable if the frequency is estimated to be more than one in five thousand per annum."
  - The plan's quoted "killing" is not in the source. The research report marked its wording as a paraphrase; the plan put the paraphrase in quotation marks.
  - The criterion is for risk "from a single major industrial activity", and ¶135 says such criteria are "directly applicable only to risks from major industrial installations".
  - For the SB 53 comparison: R2P2 says "50 or more" *deaths*; SB 53 says "more than 50" people, by "death of, or serious injury to".

### §3.9 Actors and agent parts

- **L574, EC GPAI guidelines fn 12, "control of the weights" among the operative facts that confer roles: overstated.**
  - Fn 12: "Whether it is the original provider or a downstream actor who modifies the general-purpose AI model must be assessed on a case-by-cases basis. An important factor in this assessment may be who has the control over the model's weights, for example, in case of fine-tuning via API."
  - That is a hedged factor in attributing *who modified*. By the plan's own Hohfeld distinction (L595) it is evidential, not operative.
  - The operative condition for becoming the provider is a "significant change" (para 62).
  - The guidelines are also non-binding by their own statement (para 9).
  - The spike's wording ("attributes the modification act partly", `04-actors.md` L202, L214) is closer to the source than the plan's note.
- **L583, AI Act Art. 3(3), the provider: the ellipsis drops a load-bearing clause.** The full text is "develops an AI system or a general-purpose AI model **or that has an AI system or a general-purpose AI model developed** and places it on the market …". So an EU provider need not develop anything, which directly supports the plan's case that "developer" is overloaded. Art. 3(4), the deployer, holds; the personal non-professional exclusion is omitted.
- **L583, Art. 3(8), *operator* as the umbrella: listed wrong.** The source reads: "'operator' means a provider, product manufacturer, deployer, authorised representative, importer or distributor". The plan omits **product manufacturer**, and includes **downstream provider** (Art. 3(68)), which comes under "operator" only by way of "provider".
- **L583, SB 53 §22757.11(h): holds** verbatim. (i)(2) counts fine-tuning and other modification compute toward the threshold.
  - **L589, "stated intent": imprecise.** The statute says "intends to use"; a *statement* of that intent would be evidential.
- **L583, NIST's "AI actors" (the OECD's term), defined by tasks: holds** (RMF L204–207; Appendix A's task categories).
  - NIST lists "developers" among the AI Development actors, next to "machine learning experts, data scientists", which are people. That is a cleaner corpus instance of the individual sense than anything in IASR (see L267).
- **L583, IASR's "AI developer": holds** verbatim (md L2206).
- **L586 and L626, LoO's supply-chain list: holds** verbatim. It is fn 70, p. 52, a footnote about monitoring responsibility ("fragmented authority across the supply chain … with no single party having sole responsibility to implement monitoring"), not a role definition, and the citation should say so.
- **L594, "X counts as Y in C": holds** (SEP "Social Ontology", Searle's constitutive rules).
- **L595, Hohfeld's operative vs evidential facts: holds** (operative facts "suffice to change legal relations"). Strictly, the operative fact is that a party *met* the threshold; the threshold itself is part of the rule.
- **L606, LoO's evaluators "construct the model's context merely by editing text": holds** (p. 33, honeypot example). **IMDA's approvers "edit the plan": holds** (v1.5, p. 29). IMDA offers it as an option ("it may be more productive for the human to edit the plan"), not as a defined role.
- **L570, ETSI's "data custodians", "system operators": holds** (EN 304 223 V2.1.1, Table 4-1). An adjacent oddity worth a resolution record: ETSI defines "Affected entities", one of the plan's affectedness examples, as those "that are not directly affected by AI systems".

### §3.11 Competency questions

- **L640, Grüninger & Fox (1995), cited "from memory; not yet checked": now checked, and it supports the plan more strongly than claimed.**
  - §3 states the plan's "machinery earns its place" rule (L645) almost word for word: "for every object, attribute, relation, and axiom in the proposed ontology or proposed extension to an ontology, there must first be an informal competency question … which intuitively requires the objects or constraints defined".
  - Also: "define an ontology's requirements in the form of questions that an ontology must be able to answer … we test the competency of the ontology by proving completeness theorems with respect to the competency questions."
  - Two differences from the plan: G&F's final test is formal (questions in first-order logic, then completeness theorems), and they say competency questions "do not generate ontological commitments; rather, they are used to evaluate" them.
  - The "not yet checked" can come out.
- **L652, IASR's loss of control in glossary and body: holds** (see §1.3). **L654, Anthropic's misalignment risk twice: holds exactly.**
  - The first definition is L969–971.
  - The second is §2.6 step 1, L993–1008, with "catastrophic", followed by "Call the risk from naturally-emerging misalignment acting via the specific pathways described above 'covered risk'".
  - Both are on p. 25; the gap is 25 lines.
  - Nuance for the test: L947–948 already says "In general, we confine our analysis to potentially catastrophic harms". The report signposts the narrowing, which bears on whether the test treats it as a collision or as a declared scope narrowing.
- **L654, SB 53's "foreseeable" and "materially contribute" take content from California law: our reading** (see L278).

### §4 The plan

- **L732, the NRR and the CRA contain no loss of control: holds.** NRR p. 20 says chronic risks, AI included, "are not included in this list". The CRA's AI chapter (pp. 40–43) covers bias, misuse, disinformation, cyber, jobs, concentration and an arms race; its nearest phrase is "outpacing safety measures". That rests on a grep of the whole CRA plus a read of the chapter.
- **L740, Zwetsloot & Dafoe's "accident / misuse / structure distinction": imprecise as a framing.** Lawfare 2019: they "complement their focus on misuse and accidents with what we call a structural perspective on risk". Structure is offered as a complementary *perspective* on longer causal chains, not as a third cell of a partition. The distinctions inventory should record it as they frame it.

### §5 Decisions

- **L787, decision 6, the "component" sources: each holds.**
  - IMDA v1.5 (20 May 2026) §1.1.1, p. 6: eight components (Model, Instructions, Memory, Planning and reasoning, Tools, Protocols, Controls, Logging and monitoring).
  - CSA/FAR.AI Fig. 2 (p. 11).
  - Google's component walk (Díaz, Kern & Olive, May 2025, p. 5).
  - The claim that their lists include things not influenced (controls, logging) holds.
  - **"Leave out … the ephemeral reasoning and the goals": half contradicted.** IMDA lists "Planning and reasoning" as a core component, and Google has a "Reasoning core". Goals are absent in both. What the sources lack is the map's *off-the-record, written-into* character of the reasoning, not reasoning itself. The scope-narrowing argument should say that.
  - **Lineage, under the plan's own rule.** IMDA's figure is "Adapted from GovTech Singapore, Agentic Risk & Capability Framework, CSA Singapore, Draft Addendum …, and Anthropic, Building Effective Agents" (fn 3). CSA/FAR.AI's Fig. 2 carries the GovTech framework's URL. So "three established uses" are one lineage plus Google.
  - CSA/FAR.AI's own prose also calls the arrangement "This layered architecture". That doesn't refute the "layer" collision argument, but the sources use both words.
- **L789, "Chu et al.'s seven LASM layers": one author.** arXiv 2604.23338v2 is by Kexin Chu alone. The seven layers are right (Foundation, Cognitive, Memory, Tool Execution, Multi-Agent Coordination, Ecosystem, Governance). The error comes from the spike's role-vocabulary report.
- **L790, "after the EU AI Act's *human oversight* (Art. 14) and NIST's oversight roles": holds as a naming precedent.**
  - Art. 14 covers *high-risk* systems overseen by *natural persons*, so taking the name from it is a scope widening and should be declared as one.
  - NIST frames governance and oversight as tasks and processes ("Governance and Oversight tasks are assumed by AI actors with management, fiduciary, and legal authority"; MAP 3.5), not roles.
- **L791, decision 7, the STPA paraphrase drift: real, but attributed to the wrong author.**
  - The hazard drift, "will lead to a loss" → "can", is in **Mylius's** Appendix A glossary only. That glossary carries no attribution, and Mylius's body (§3.1.4) quotes the Handbook verbatim with "will".
  - **Barrett's** hazard entry is faithful. His drift is in the unsafe-control-action entry ("will lead to a hazard" → "can"), and his entries are attributed to Leveson & Thomas (2018).
  - "Mylius drops a scenario type" is likewise true of his glossary's loss-scenario entry only. His body (§3.4) gives both types.
  - The research report's "Both attribute definitions to Leveson & Thomas" is true of Barrett only.
  - The recommendation (bind to the Handbook) stands.
- **L800, decision 9, "its README says the parser implements the pre-0.8 model, behind the spec": a faithful quotation of a stale file.**
  - `udon/core/README.md` (last touched 2026-07-16) does say that.
  - The repo's newer records say otherwise:
    - `core/fixtures/README.md`: the fixtures were "rewritten to the ratified 0.9 attribute model 2026-07-16 … the gate GREEN the same day — the parser implements the 0.9 model";
    - `CONSUMERS.md`: "the current parser (CORE 0.9.0-alpha.1 attribute model, compliance gate green)";
    - `spec/CORE-VERSION` reads 0.9.0-alpha.2 (2026-07-18).
  - So the second listed gap is largely not a gap. I did not run the compliance gate myself.
  - The first gap, no Ruby or Python bindings ("[later]" in `TODO-PARSER.md`), holds.
  - **L798, `stdin_parse` "that other projects use as a validation gate": one project.** `CONSUMERS.md` lists tabularium only.
  - The lean in decision 9 (YAML through the pilots) may still be right on the bindings gap alone, but its stated premise is half wrong.
- **L815, decision 10, EO 14365: holds.** §1 says state laws are "requiring entities to embed ideological bias within models" and that a Colorado law "may even force AI models to produce false results". The plan's conditional phrasing is accurate.

### §7 Corrections to the repo's existing documents

- **Item 1 (Guide 51, not ISO 31000): holds** (ISO 31000 via the ERA reproduction; Guide 51 via IEEE 7009 and Nolte et al.).
- **Item 2 (NIST's attribution): the line range and attribution placement hold** (RMF L272–278). **"The core of that definition matches OMB A-130's form" is only partly right.**
  - A-130 (2016) def. 73: "a measure of the extent to which an entity is threatened by a potential circumstance or event, and typically is a function of: (i) the adverse impact, or magnitude of harm … and (ii) the likelihood of occurrence".
  - That is nearly verbatim NIST's *second* sentence, the one NIST itself attributes to A-130.
  - The "composite measure" sentence shares only the generic two-factor shape, which is also Guide 73's and the SRA's.
  - Suggested wording: "shares the two-factor form NIST attributes to OMB A-130 in the next sentence".
- **Item 3 (the eighth "hazard" sense): holds** (see L490).
- **Item 4 (Kasirzadeh's senses = Hansson's first four): holds on the text.** They are the same order, near-verbatim, with parallel examples (Hansson's smoker "about 50%", Kasirzadeh's LLM "approximately 5%"). But Kasirzadeh cites four other authorities for them and cites Hansson (2010) only in the preceding paragraph. "One lineage" is a strong inference; the research report itself says it can't tell whether she drew on the SEP entry. The plan drops that hedge.
- **Item 5 (STPA): holds.** Handbook p. 14 has "provided but not followed or executed properly", p. 43 has "improperly executed or not executed", and pp. 45–51 build adversaries into scenario generation.
- **Item 6 (the PHIA yardstick): holds.**
  - The NRR's Table 2 (printed p. 15) has "Highly unlikely (5‑25%)"; gov.uk (24 Mar 2025) has "≈10% - ≈20%: Highly Unlikely".
  - "The other six bands match" is true of the endpoint numbers only. The NRR drops the ≈, > and < marks (e.g. "Remote chance (0‑5%)" against "&gt;0% - ≈5%").
  - Note: the NRR's 5–25% is exactly its own score-4 band on the same row, which suggests the score band overwrote the yardstick band.
  - LoO cites the 2019 PHIA edition, not 2025; the figures agree.
- **Item 7: holds.** The repo counts are right: 46 `broad` and 70 `narrow` in `mappings*.yaml`, about 31 and 28 in `terms/*.ud`, and the legend at `def-actors.ud` L37.

### §8 Provenance

- §8's closing sentence ("Everything else attributed to the research reports rests on their verification marks") is true, but those marks don't travel with the claims into the plan's body. This is where most of the provenance findings above come from: Temmerman, the ISO acceptability values, Searle's mode and indirect force, Hart, the "ISO" event note, the Admiralty grading, and the Kasirzadeh hedge. A per-claim mark in the plan, as the reports have, would remove the class.

---

## Research-report findings not visible in the plan

- **`speech-acts-argument-norms.md` §5.2:** the IAT quotation marked [P] is not in the cited LREC 2014 paper (see L352).
- **`speech-acts-argument-norms.md` L99, L142:** Hart's "final but not also infallible" is in quotation marks as Hart's; it is Kloosterhuis's paraphrase.
- **`risk-formalisms.md` §2.5 and §0:** "Both attribute definitions to Leveson & Thomas" is true of Barrett only.
- **`risk-formalisms.md`:** the attribution of the "cause can be an event in a chain" note to ISO/IEC/IEEE 16085 is not on the IEEE 7009 page that witnesses it.
- **`risk-formalisms.md` §2.6:** IASR's bowtie entry is a practices-table row, not a glossary entry.
- **`gamma-de-novo-review.md` L162:** "roughly 1,200" should be 993 (see L269).
- **The spike's role-vocabulary report:** "Chu et al." is a single author.

In the terminology-standards cluster, every quotation the report marks as read at the primary matched character for character, and its memory and secondary marks were honest.

## Not covered, or covered thinly

- Hart's own text; FM 2-22.3; the full ISO standards; Guide 51 directly; earlier drafts of the EU Code (so "lineage root", L720, holds only as the earliest document in the corpus).
- The plan's negative claim at L586, that none of AI Act, SB 53, NIST or IASR has the "writes into the agent" basis. Nothing contradicting it was seen in NIST or IASR, but it was not proved.
- The companies' "principal" and "chain of command" (L570): both phrases occur in the downloads; their senses were not checked.
- Internal numbers (model beta's 287/573/943, the loop counts) are outside "sources outside this repository" and were not checked, apart from the SKOS-direction counts in §7 item 7.
