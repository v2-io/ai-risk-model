# De novo review of `MODEL-GAMMA-METHODOLOGY-AND-PLAN.md`

> [!NOTE]
> **Line and page references here predate `ref/canonical/`.** They were taken from `pdftotext -layout` extractions of the relata PDFs (the `bin/extract-text` script), before the canonical page-marked texts existed. Page numbers are the PDF's physical pages and still hold. Line numbers ("L…") are lines of those layout extractions, so they won't match `ref/canonical/`: to re-find a passage, search for its quoted words, or regenerate the layout text with `pdftotext -layout`. References marked "md" are lines of `ref/iasr-2026-full.md`, which is unchanged.

*2026-10-06. Claude (Opus 5.5), given a bare brief ("a de novo review … form your own view however you see fit") and the whole repository. Written for Joseph and for the session that drafted the plan. Uncommitted.*

*Which version: I reviewed `eaf1ccb`. The plan was amended in `cd9b2ab` while I worked. I read that diff: it replaces "Decided/Leaning (Joseph)" labels with Joseph's quoted words, and it moves no lines or sections. Section references below hold for both versions. Where the amendment bears on a finding, I say so.*

*A caveat on independence: I am the same model as the plan's author and its three research agents. This review breaks the drafting session's framing, because I had none of its conversation, but it does not break same-model coherence. Where I agree with the plan, that agreement counts as one reading, not two. §6 says what would count as a second reading.*

*How I worked:*
- *I read the plan whole, then the material it rests on: `CLAUDE.md`; `source-catalog.md`; the handoff; the three `gamma-research/` reports, whole; `OVERVIEW.md` (headlines, §1, §2.0, §2.8, §2.14–§3.4, §4 and the appendix); the parts of `SCHEMA-SYNTHESIS.md` the plan builds on (§0, §1, §5, §10, §11); model beta's README, `SCHEMA.md`, `def-risk.ud` and `def-actors.ud`; `alignment.md`; the aligned-to-whom table; and the address-theory `def/` files.*
- *I then checked the plan's corpus claims against the primaries, using `bin/extract-text` with output to my scratchpad: SB 53, the AI Act and the Digital Omnibus, NIST AI RMF, the NRR, AISI* Loss of Oversight*, Anthropic's August Risk Report, MIT, IASR 2026 and Evans.*
- *To check two attributions, I read Joseph's own typed turns from today's session and from the 2026-09-28 aisi-eoi session. I did not read the drafting session's assistant turns.*
- *Line numbers below point into `pdftotext -layout` extractions unless marked otherwise.*

---

## 0. Verdict

The direction is right, and the research behind it is real. Of the claims I checked against primaries or repo files, almost all held (§1). The plan's strongest moves are well founded:
- type-level translation kept apart from occurrence-level resolution;
- the SKOS direction flip;
- splitting draft 2's stance into point, strength, factuality and attack;
- Searle's commissive kept apart from a self-imposed norm;
- Hohfeld's second-order positions;
- SRA's concept/metric separation for "risk".

Each of these makes the theory better, not just the words.

Where I would push before ratifying, in rough order of leverage:

1. **The acceptance tests measure whether the lexicon can express things, never whether the model can answer anything.** One test can't run until G7. The round-trip test has no stated pass condition for terms a source deliberately leaves to an outside institution or to plain meaning. Both of its hardest cases have one. (§2.1)
2. **Translation is coding, and the plan adopts coding schemes without coding method.** `CLAUDE.md` names MIT's single coder as a cost to avoid. The plan never takes it up. (§2.2)
3. **No phase owns the record schema.** It is unclear whether draft 2 is superseded. Model beta has 943 claims and 450 source-term mappings with verbatim anchors, and the plan says nothing about what happens to them. The causal-relation vocabulary that a causal-loop view would need has no home. (§2.3)
4. **Occurrence-level resolution has no selection rule.** At corpus scale that decides whether it is feasible. (§2.4)
5. **The lexicon's first two groups collide with each other.** Examples: *context*, *model*, *source*, *role*, *scope*, *agent*. The plan's collision table only looks outward. (§2.5)
6. **Three of the DDD patterns are used in senses Evans does not give them,** and G1(a) will import Evans's text verbatim. (§2.6)
7. **Two of `CLAUDE.md`'s open decisions are missing from §5.** One of them, the misalignment referent, is the question `alignment.md` exists to answer. (§2.8)
8. **Sequencing.** G1(d) asks Joseph to ratify a large evidence-plane vocabulary that nothing uses until G7. The assertion layer and the views are first exercised at full width. (§2.9)

None of these argues against the direction. Most can be fixed in the plan's text before G1 starts.

---

## 1. What I checked, and what held

| Claim in the plan | Checked against | Result |
|---|---|---|
| Beta: 287 concepts, 573 relations, 943 claims | `python3 check.py` | Holds; it also reports 450 source-term mappings |
| Broad/narrow inversion; 46/70 and ~31/28 rows | grep over `mappings*.yaml` and `terms/*.ud`; `def-actors.ud` legend; SKOS §10 as quoted in the research report | Holds: 46/70 and 31/28 exactly |
| `def-risk.ud`: "The first four definitions are IASR 2026's, adopted" | the file | Holds. But the file's own working note says Joseph asked for it (§3, item 4) |
| SB 53 §22757.11(c) wording, exclusions, "otherwise publicly accessible" | `.extract/california-2025-sb53.txt` L186–208 | Holds; see §3 item 1 on how it is split |
| SB 53 defines catastrophic risk twice, frontier vs foundation model; first CSI kind differs | L186–222 vs Labor Code §1107, L596–633 | Holds. §1107(c)(1) adds property damage |
| §22757.14 annual review, pre-training determinability, external verifiability | L453–487 | Holds |
| MIT Entity/Timing "Other" wording; 21% | `slattery-2026-risk` L318–338, L154 | Holds. MIT itself says Other "captures cases where this attribution was ambiguous or explicitly interactional" (L154–155) |
| AI Act Art. 3(3)–(8), (68) | `eu-2024-ai-act` L3144–3161, L3432 | Holds. The Omnibus amends Art. 3 only at (14) and inserts (14a)/(14b), SME and SMC (`eu-2026-digital-omnibus-ai` L953–971); the roles are untouched |
| NIST AI RMF risk sentence and its two "Adapted from" notes | `nist-2023-ai-rmf` L271–279 | Holds; the plan's reading is fair |
| NRR prints "Highly unlikely (5‑25%)" | `cabinetoffice-2026-nrr` L404–422, Table 2 (the extraction's page is headed 14; the plan says p. 15, which I couldn't settle without the PDF) | Holds |
| AISI LoO supply-chain list; PHIA figure | `aisi-2026-loss-oversight` L2766–2768, L502–515 | Holds |
| Anthropic Aug: "not crisply defined"; "expected total unmitigated harm" | `anthropic-2026-risk-report-aug` L926–927, L969–971 | Holds, but there is a second, different definition 25 lines later (§2.1) |
| IASR L2077 "should not release"; L1688 bow-tie | `ref/iasr-2026-full.md` | Holds; L1688 is in the risk analysis/evaluation practices table, as the plan says (the risk report calls it a glossary entry) |
| Evans quotations ("change in the language…", "Map the existing terrain…", Big Ball of Mud) | `ref/DDD_Reference_2015-03/*.md` L171, L481, L597 | The quotes hold. The *pattern assignments* do not all hold (§2.6) |
| The coinage rule attributed to Joseph | memorata: Joseph, 2026-08-09 | Holds, verbatim |
| The causal loop diagram as "a natural subset view during the analysis phase" | Joseph, 2026-09-28T17:16Z, aisi-eoi `f462f375` | Holds. The surrounding sentence matters (§2.3) |
| Lexicon shape and actor priority, 2026-10-06 (quoted in full in `cd9b2ab`) | Joseph's typed turn, 2026-10-06T22:22Z | Holds, verbatim |
| The "developer" quotation added in `cd9b2ab` | `.archive/HANDOFF-2026-09-27.md` L189 | Holds |
| Steward / ratified / council / supported / defacto / proposed / transition | `udon/v2/references/DECISIONS.ud` L8–15 | Holds |
| Address-theory files; "designator" in `def-match.ud` | `~/src/arch/firmatum/udon/v2/references/def/` | Holds (seven files). The outcome list is not all address theory's (§2.7) |
| G0: 130 paths repointed | `git show b6ed3c7` | Holds (130 references on 128 lines) |
| 11 anchors, 26 major; eleven model rows; 16 + 12 collision terms | `source-catalog.md`, `HANDOFF`, `OVERVIEW` | Holds |

I did not re-verify the research reports' external primaries (SKOS, SSSOM, Searle, Hohfeld, the SRA glossary and the rest). I relied on their per-claim marks, which look carefully kept. One exception: the plan cites Walton's *analogy* scheme without the [M] (memory-only) mark the research report gives it.

---

## 2. Findings that bear on the method

### 2.1 The acceptance tests

**Test 5 is not a lexicon test.** It asks that the EU Code's loss-of-control formula count as one source in the corroboration view. That needs lineage records and assertions, which arrive in G7. As written it cannot gate G1–G3.

It also hard-codes a judgment the plan says must be an attributed assertion. In §3.7, "claim identity is an assertion", after Clark et al. The nine later appearances are not one kind of thing (OVERVIEW §2.8):
- xAI copies the formula verbatim;
- OpenAI's FGF embeds it;
- Meta, Amazon, Microsoft and the GDM blog paraphrase it, so lineage is inferred, not shown;
- METR and Stix et al. quote it *as the Code's*. That is attributed citation, not agreement of any kind.

A version consistent with the plan's own principles: *each of the nine has a lineage record with its relation type and its author, and the corroboration view's count follows from those records, not from the test.*

**Test 1 needs a stated pass condition for terms that aren't ours to define.** Both hard cases contain such terms.
- **SB 53.** "Foreseeable", "material" and "materially contribute" are legal standards. Their content comes from California law, not from the text (§22757.11(c)(1), L186–189). "Nothing left over and nothing added" either fails by construction, or pushes the lexicon to redefine California tort concepts.
- **Anthropic's misalignment risk has two definitions in the August report.**
  - L969–971 (PDF p. 25): "the expected total unmitigated harm induced by misaligned computations produced by covered models".
  - L993–1008: "By our definition, misalignment risk equals the expected total unmitigated *catastrophic* harm…", with "catastrophic" added. Only the general scope note at L947–948 bridges the two: "In general, we confine our analysis to potentially catastrophic harms".
  - The same passage then names Rtotal, and a separate "covered risk, denoted R" (naturally emerging misalignment via the specified pathways, L1007–1008). The argument goes on to bound R.
  - "Catastrophic" is itself deliberately unbound in Anthropic's RSP ("plain meaning"; OVERVIEW §2.6, beta's `def-risk.ud`).

  So "the definition" to round-trip is a resolution question before it is a translation question.

What I'd suggest: test 1 names the outcomes that count as a *faithful* translation. These are an imported binding to an outside institution (California law), deliberately unbound (plain meaning), and declared ambiguity with its candidates. Test 1 then says which passage is the definition under test. Anthropic's report is still a good test case, perhaps a better one than the plan thinks (see §2.10).

**A missing test: the distinctions inventory.** `CLAUDE.md`'s plan put the inventory *before* the lexicon, as its requirements. The gamma plan moves it to G5, "in parallel with G2–G4", and says it "feeds G3". No acceptance test connects the two, so G3 can be "done" before the inventory exists. Add: *every basis of division in the inventory is expressible in the lexicon*. Or keep the inventory upstream of G3.

**The larger gap: no test asks the model a question.** The aim in `CLAUDE.md` is projection "by cause, by control, by risk event and impact, and by who is affected and who decides". All five tests are about expressiveness.

Ontology engineering's established answer is *competency questions*: questions, written first, that the finished model must be able to answer. They serve as its requirements and its acceptance test. I know this from memory (Grüninger & Fox 1995, and the methodologies that followed). I did not check it this session. By the plan's own rule (established vocabulary over coinage), §3.11 is a partial reinvention of it.

Three examples drawn from the aim:
- *For a single-incident event with 60 deaths, which recorded sources would call it catastrophic, severe or systemic, under which conditions, and through how many independent lineages?*
- *For loss of control as a top event, which preventive controls do sources name, and which of them are duties with no holder of the correlative claim?*
- *Which actors write into which agent part, and which source role words resolve to each?*

Questions like these give the lexicon a demand signal. They also answer §6's first risk ("heavier than the work needs") empirically: a piece of G1(d) machinery earns its place when some competency question needs it.

### 2.2 Translation is coding: adopt the method, not only the categories

`CLAUDE.md` lists MIT's costs, including "a single coder". The plan's translations are coding: an agent reads a source and assigns its words to our concepts, with outcomes and rationales. The plan never says how that coding is checked beyond "agent-made, human-reviewed".

The annotation schemes the plan adopts are each published with a method that makes them trustworthy:
- FactBank and the PDTB are annotated corpora with guidelines and inter-annotator agreement;
- IG 2.0 is literally a *codebook*.

The plan takes their categories and leaves the method.

A concrete form for G4:
- Two independent translations of each pilot source. Ideally they come from different model families, since same-model agreement is coherence, as §6 itself says.
- Disagreements are recorded and resolved as attributed assertions.
- The per-term disagreement rate becomes a direct, empirical measure of where the lexicon is underspecified. That is exactly the feedback G4 exists to produce.
- The guidelines the translators converge on are the codebook, which becomes a G4 output that G6 inherits.

Joseph's own pattern (spiker ≠ verifier) points the same way. At G6 scale, full human review is not possible. The records should say which rows were reviewed and how they were sampled (SSSOM's `reviewer_id` covers the per-row half).

### 2.3 The schema, the migration, and the causal relations

**The schema.** `CLAUDE.md` says the schema for steps 4–6 is `SCHEMA-SYNTHESIS.md` draft 2, a proposal, and the handoff lists "Draft 3" as a todo. The gamma plan decomposes or renames much of draft 2:
- stance becomes point, strength, factuality and attacks;
- norms get five layers;
- "qualifier" narrows to Toulmin's sense.

It never says whether draft 2 is superseded, extended or kept. No phase produces the formats that G4 needs (a translation row and a resolution record) or the assertion record that G7 needs. Decision 9 (udon or YAML) is still open.

Without an owner, G4 will invent these formats in passing, and they will become *defacto* in `DECISIONS.ud`'s sense. Naming them as a G1 deliverable, or as G4's entry condition, costs one line.

**Model beta's evidence.** `check.py` reports 943 claims and 450 source-term mappings, each with a verbatim quote, location and channel. Draft 2 §10 said "nothing is discarded": mappings become resolutions, relations become causal assertions. Gamma is silent.

Re-deriving from primaries is defensible, and so is reuse as input to G4 and G7. Silence isn't, because this is costly fidelity work that already carries anchors.

**Causal relations.** Beta's model plane was signed influences, delays and moderators. These are the vocabulary a causal-loop view needs. Gamma keeps the causal loop diagram as a view (§3.10), but no phase defines the relations it would be computed from. G3 defines risk *components*, not relations between quantities.

Joseph's words in the session the plan cites are worth having in front of whoever writes G3:

> "The point isn't the causal loop-- the point is that I sensed that there was a cyclical graph of sources/causes/events/impacts that would be ammenable to causal loop analysis."

A bow-tie is acyclic around one focal event. The cycles live *between* focal events: one event's consequence is another's threat. ISO's event note, which the plan cites, makes this point. So the bow-tie fits the chain locally, and the plan needs a named home for the relations that connect bow-ties.

### 2.4 Occurrence-level resolution needs a selection rule

I counted raw occurrences of the plan's high-load terms in `ref/iasr-2026-full.md`. The counts include cited titles in the footnotes, so they overstate:
- *developer* 193, *safeguard* 156, *frontier* 352;
- *incident* 103, *threshold* 75;
- *loss of control* 49, *misalign* 41, *systemic risk* 24.

That is roughly 1,200 in one document. Across the 11 anchors and 26 majors it will be tens of thousands. The plan doesn't say which occurrences get a record.

Address theory and draft 2 §3.3 both suggest the answer:
- resolve by *scope default*: the document's or section's binding, recorded once;
- record per occurrence only where an occurrence departs from its scope default, or sits inside an assertion that G7 records.

Stating that now keeps the first pilot from discovering it.

### 2.5 The lexicon collides with itself

§3.2's collision table compares our *method* words with outside standards. It doesn't compare the method vocabulary with the *domain* vocabulary that will share `def/`. The first two groups collide directly:

| Word | Method sense (G1) | Domain sense (G2/G3) | Also |
|---|---|---|---|
| **context** | DDD's context, imported verbatim in G1(a) | `alignment.md`'s *Context*, an agent part ("experience & agency") | IG 2.0's Context component; GSN's Context |
| **model** | DDD's domain model | an AI model, in every source | "source model", "model gamma" |
| **source** | a source document (the project's own core word) | SRA/ISO *risk source*, which is H1 | FactBank's nested source; SP 800-30's threat source |
| **role** | Goffman's production roles; "stage is a role relative to a focal event" | functional and institutional actor roles (§3.9) | model alpha's role codes |
| **scope** | address theory: the jurisdiction of bindings (§3.2) | a source's declared coverage, "coverage by each source's declared scope" (§3.10) | |
| **agent** | PROV and SSSOM agents (who made a record) | an AI agent | |

Address theory already supplies the remedy. Put method terms and domain terms in distinct scopes, with declared containment, and give §3.2's table a second half.

### 2.6 Three DDD patterns are used in senses Evans doesn't give them

G1(a) imports Evans's definitions verbatim. That makes these mismatches self-contradictions in the lexicon, and the plan's own rule applies: "don't borrow an established word in a different sense". Quotations are from `ref/DDD_Reference_2015-03/DDD_Reference_2015-03.md`.

- **Shared Kernel** (L503–515): "Designate with an explicit boundary some subset of the domain model that the teams *agree* to share … shouldn't be changed without consultation with the other team." New York copying SB 53's definitions involves no agreement and no consultation. That is **Conformist** (L531–537: "slavishly adhering to the model of the upstream team").
- **Big Ball of Mud** (L597): "Draw a boundary around the entire mess … Do not try to apply sophisticated modeling within this context." The plan uses it for self-inconsistent sources, "mapped passage by passage, not document by document". That is finer modeling *inside*, the opposite of the pattern.
  - The plan's *move* is right: scopes finer than documents, its own finding 5.
  - The honest description is that such a source is several bounded contexts, or scopes, under one cover.
- **Separate Ways** (L575–585): "Declare a bounded context to have no connection to the others at all." The RSP's plain-meaning "catastrophic" is one deliberately unbound term inside a document full of connections. Draft 2's outcome name, *deliberately unbound*, already fits it better.

The address-theory import is borderline too. It is described as shared kernel "with Joseph's address theory as the maintained upstream". "Upstream" is customer/supplier or conformist language. Since Joseph owns both, a shared kernel is defensible, but say which one is meant.

### 2.7 The resolution outcome list merges two axes, and is credited to the wrong source

§3.4 lists nine outcomes, then says "This is address theory's resolution". Address theory (`def-resolution.ud` L10–40) gives *zero, one, many and ambiguity*, with intended cardinality giving each its meaning. Five of the nine come from draft 2 §5 (L264–268):
- withheld;
- delegated;
- defective;
- deliberately unbound;
- declined.

The list also merges what the reference reached with *why*, and *whose fact* that is:
- "withheld / declined / delegated / deliberately unbound / defective" are reasons a source's word reaches nothing determinate, and they are facts about the source;
- "none (a gap in our vocabulary)" is a fact about our lexicon;
- "ambiguous" is a fact about our reading.

This is a mild version of what the plan's MIT test (§3.3) forbids. The fix is cheap: an *outcome* in address theory's terms, plus a *reason* with its author.

### 2.8 Two of `CLAUDE.md`'s open decisions are missing from §5

`CLAUDE.md` lists six open decisions. §5 carries four of them: developer, hazard, STPA and format. It drops two:

- **Impact radius** (target × degree × recoverability). §3.8 treats parts of it: the receiver side, systems as targets, recoverability as an axis. It never puts it to Joseph, and the *degree* dimension (the NRR's banded scales, NIST's "individuals … planet", RMF L278–279) is not discussed.
- **Misalignment: a default referent.** This one matters more, because the plan's own first domain source answers it.
  - `alignment.md` opens: "'Alignment' without saying to whom quietly picks one of them."
  - The resolution record already has "for relational terms, the reference standard and the bearer".
  - The actor and referent rows in `alignment.md` are the natural value space for that slot.

  - Joseph's own words on "developer", quoted in the amended §3.9, already point this way: "What is really meant is one or more of the alignment referents — usually implied model-trainer, inference-provider, & app&harness-provider".

  That suggests the decision may not be "choose a default referent" at all. It may be: *no default; every resolution in the alignment family names its referent from the actor set, or records it as ambiguous*. That follows from the decided union shape. It is Joseph's call, but the plan should put it in front of him and connect G2 to it.

### 2.9 Sequencing, and Joseph as the ratification bottleneck

G1 is "done when Joseph has ratified or redirected each group", and G1(d) includes the whole evidence-plane vocabulary: Searle's point, strength and mode; FactBank; the three attacks; norm-propositions; the five norm layers. Nothing uses those terms until G7. Joseph's 2026-09-28 instruction was DDD terms, then meta terms "for analyzing the subsequent steps". The subsequent step is translation, which needs G1(a)–(c).

Ratifying abstract terms before any of them has carried weight is the "harden too early" risk that §6 names. It also puts Joseph's attention on the critical path of G1–G3.

Two tactical suggestions:
- **Use `DECISIONS.ud`'s own statuses.** Agents proceed on *supported* or *council* terms. Joseph ratifies in batches once G4 has shown which terms bore weight.
- **Pilot the whole pipeline thin before widening.** Take one pilot source and one focal event all the way through translation, assertions and a bow-tie, before G1(d) is ratified. As written, G4 pilots translation only. The assertion layer and the views are first exercised in G7, across every translated source at once. That is where a schema defect would be most expensive to find.

This isn't a case for doing less; the whole plan still runs. It is about where defects surface first.

### 2.10 Pilot choice, and the conflict of interest

§2.1 shows that Anthropic's August report has its own definitional drift. That makes it a *good* pilot, because it tests resolution inside one document. But the plan's description, "a company's argued assessment with its own rigorous vocabulary", should be qualified. That description is a judgment made by an Anthropic model, which is the conflict of interest the plan flags. I share that conflict as reviewer.

On method grounds rather than conflict grounds, the **EU Code** is a strong candidate for a fourth pilot or a replacement:
- its interpretation clause declares a resolution policy: precedence ("shall prevail"), grammatical variants, and purposive reading. That exercises the plan's imported-binding and resolution-policy machinery directly;
- it is an anchor, where the Risk Report is a major source;
- it is the lineage root of test 5's formula.

Confidence: moderate.

### 2.11 Two notes for a public repository

- **The address-theory import points at a local path:** `~/src/arch/firmatum/udon/v2/references/def/*.ud`. Those files are tracked in the public repository `github.com/v2-io/udon` (`v2/references/def/`, last changed in `90f4fb6`, 2026-08-27; checked with `gh repo view`). An import by reference should cite the public URL, pinned to a commit. That is the plan's own as-of discipline applied to itself.
- **A quoting policy.** The plan requires verbatim text beside every claim. The research reports kept ISO and SRA quotations short for copyright. The terminology report flagged the Web Annotation spec's copyright note and the git-ignored IASR text (its §5.3 and §12). The plan dropped both points. At G6/G7 scale this becomes a publishing question. One line of policy now (for example, short quote selectors plus position selectors for restricted texts) would settle it.

---

## 3. Smaller corrections

1. **§1.3 finding 3** files "foreseeable and material" together as one *knowledge* standard. "Material" is a materiality threshold, not a knowledge standard; the risk report keeps them apart. Since the paragraph's point is separability, count them separately.
   - The same sentence also carries:
     - the conduct attribution ("a frontier developer's development, storage, use, or deployment");
     - the oversight condition in (B) ("no meaningful human oversight, intervention, or supervision");
     - a counterfactual-human legal test ("if … committed by a human, would constitute the crime of").
   - "At least seven" is true; ten or more is closer.
   - Labor Code §1107.2 (L730) adds one more scope-specific narrowing: equity value doesn't count as property damage.
2. **§1.3 finding 2:** "Shanghai AI Lab's glossary is IASR 2025's." OVERVIEW says "primarily based on" and "builds upon". In a project about lineage the hedge matters.
3. **§1.2:** "641k loops" was the count before one edge was recast (`notes-mp.md` L108). The last reported figure is about 186,000. The number is the evidence offered, so it should be the current one.
4. **§1.2 on beta's "conformist" lexicon.** `cd9b2ab` didn't touch this passage. The IASR adoption followed Joseph's own suggestion: "possibly even preemptively adopt a bunch of the influx/iasr-2026-glossary.md definitions where appropriate" (2026-09-28T02:42Z, aisi-eoi session `…0593ad`). `def-risk.ud`'s working note records it. The bounded-context framing came later the same day. Presented as a beta defect, it misstates the history. It was an earlier steer, superseded by a later one, and the history layer should say so.
5. **§3.3:** "MIT's AI Risk Repository is the field's main shared-vocabulary effort." The catalog says the repo shows no document adopting MIT's taxonomy, so "main" is unsupported. "The largest" (1,725 risks from 74 documents) is checkable.
6. **§3.9:** "none of the sources has the second basis" was checked against four sources: AI Act Art. 3, NIST Appendix A, SB 53 and IASR. AISI LoO's supply chain ("original model developer, scaffolding developer or fine-tuner, API deployer, end user", L2766–2768) is framed as a supply chain, but its members sit close to writer roles: fine-tuner → weights, scaffolding developer → harness. Narrow the claim to "none of the four checked".
7. **§7 item 6** is a discrepancy *in the NRR*, not in the repo. NRR Table 2 relabels PHIA's "Highly unlikely" as 5–25% to fit its score-4 band. The repo correction is to annotate OVERVIEW's appendix row, which reproduces the label without comment. It is also a ready example of a source restating an upstream scale with altered values, the kind of drift §3.7 says "remains ours".
8. **§0:** "Most of what model beta coined has an established name." "Most" is uncounted. The load-bearing cases (stance, commitment vs self-norm, three attacks, Hohfeld's second order) are well supported. "Many, including the load-bearing ones" is what the evidence shows.
9. **§6:** the "fresh review commissioned below" cuts same-session framing, not same-model coherence (see the note at the top).

---

## 4. On the decisions in §5

1. **Context map vs translation.** Agree. Fix the pattern assignments in §2.6 at the same time.
2. **Broad/narrow.** Agree, with high confidence. The counts verify.
3. **"Hazard" → H1.** Agree on the evidence. Two notes:
   - OVERVIEW finds the word load-bearing in only two corpus sources (the NRR and NVIDIA). The decision's consequences are therefore mostly internal, plus the NRR translation.
   - The intent attribute needs a *bearer* as well as a value: a human actor's intent, as against a system's propensity. "AI-as-adversary" as a value folds the bearer into the kind.
4. **"Risk" as an umbrella.** Agree. The risk report flags Fischhoff et al. ("choosing a definition of risk is a political act") as the strongest argument for a plural umbrella. It wasn't read, and the plan doesn't cite it. It also bears on §2's "neutrality lives in the assertions": the views' bases of division are non-neutral choices too, and they deserve the same declaration the lexicon gets.
5. **"Developer."** A declared umbrella fits the decided shape. I have no stronger view.
6. **Names for the agent-part umbrella and the oversight relation.** Joseph's.
7. **STPA.** Agree: keep it as a source, bind to the Handbook, and use bow-tie for the chain's local structure (with §2.3's caveat about cycles).
8. **Contest standings.** Agree.
9. **Format.** Joseph's. It is tied to §2.3: someone has to own the record formats regardless.
10. *(Missing)* **Misalignment referent.** See §2.8.
11. *(Missing)* **Impact radius.** See §2.8.

---

## 5. What I did not do

- I did not read the source atlas, the verification files, the source-model sections other than OVERVIEW, or SCHEMA-SYNTHESIS §2–§4 and §6–§9 in full.
- I did not check the research agents' external sources.
- I did not test the HSE R2P2 / SB 53 lead the plan mentions.
- Competency questions (§2.1) are from memory, not checked this session.
- I left the repo unchanged apart from this file. I ran `bin/extract-text` once with its default output before switching to `-o` and my scratchpad. That file (`slattery-2026-risk.txt`, in the git-ignored `.extract/`) was moved to the scratchpad, so `.extract/` is as I found it.

## 6. On independence, and on the brief

- **What would count as a second reading.** A reviewer or translator from a different model family; Joseph's own review; or the inter-coder disagreement data from §2.2. A second Claude review would add little that this one doesn't.
- **The bare brief worked.** I'd only note that the project's Claude memory directory exists and gave me context beyond the brief, which shaped §2.1's emphasis on competency questions. I'm saying so in case the brief meant to keep that out.
- **One adjacent observation.** The project memory file `iteration-3-state.md` correctly says the handoff is stale on what comes next (`def/`). `influx/HANDOFF-2026-09-28.md` still lists the distinctions inventory, the schema's draft 3 and the stale `msc-notes-jaw.md` pointer as open. Once Joseph rules on this plan, those three lines are the ones to reconcile.

I'm available for follow-up questions.
