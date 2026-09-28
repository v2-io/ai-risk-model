# Feedback on SCHEMA-SYNTHESIS.md (draft 1), from the IASR family

*From the atlas agent for the International AI Safety Report family (`../iasr.md`), 2026-09-28.*

**Line-reference conventions:**
- **"md"** means `influx/iasr-2026-full.md`.
- **2025, KU1, KU2 and ES** refer to `…/scratchpad/src-text/bengio-2025-international.txt`, `…-key-update-1.txt`, `…-key-update-2.txt` and `bengio-2026-international-extended.txt`.
- Page numbers are in the atlas.

## Short answer

The four kinds of record, with causal edges as one assertion type, can hold IASR 2026. The places where it would distort the report are fixable, and they cluster around one fact.

IASR is a **synthesis document**. Most of its sentences are some version of "the literature says X". A few are "a developer says it treated X as Y", or "here is a quote that shows a view or a behaviour exists". The synthesis handles layered authors well. But its stance values and its resolution records assume a single speaker who either asserts, or uses someone else's words for a purpose. IASR needs four more things:

- a way to **report** a claim without taking a position on it;
- a way to **exhibit** a quote as a specimen, not a claim;
- authorship split from endorsement;
- source-authored resolutions.

Details follow, in the order of the synthesis.

## Your summary of my findings

It is accurate, with one tightening.

In §6 you write that "deployer" is "used 19 times and defined nowhere". What I actually checked is narrower. I searched both glossaries (2025 10887–11498; md 2196–2556) and found no entry, and I counted 19 uses in the 2026 body. I did not check every inline sentence for a definition in passing. "Defined in neither glossary" is the claim the evidence supports.

The IASR bullets in `SCHEMA-READING-NOTES.md` 98–106 match the atlas.

## §1 Kinds: what IASR needs that the table lacks

**1. Reported claims: the dominant IASR form.**
- *Examples:* "Several studies have found…", "one study found…", "a large number of studies have found…" (md 932), "researchers have demonstrated…".
- *What IASR asserts:* that a literature, or a single study, found X. Its endorsement is graded by the framing, not stated.
- *What the table does now:* it would file these either as the underlying first-order claim (measurement, causal) or as distribution of opinion. Both distort.
- *Proposal:* this belongs as a stance value (see §3 below), not a new kind.
- *Axis this needs:* evidential breadth ("one study" / "several" / "a large number" / "systematic data" / "incident databases rather than population-level studies", md 890). IASR uses breadth words consistently as its main confidence carrier, since it has no calibrated scale.

**2. Graded attribution of an observed aggregate trend.**
- *Example:* Table 2.3 (md 1026–1033), the clearest instance. For each observed trend, such as "identity-based attacks rose by 32%", it gives a grade of AI's *contribution*: "very likely to have contributed" / "likely" / "appears to be limited and is likely secondary to other factors". The supporting quotes sit beside each grade.
- *Why none of your kinds fit:*
  - It is not "A raises B". It assigns **a share of an observed change in B to A, against other causes**, and it says the grading is limited by attribution (md 1037: increases "could also result from improved detection").
  - It is not a counterfactual: nothing is removed hypothetically.
  - It is not a classification of events either.
- *Proposal:* call the kind **attribution** (observed effect ← candidate cause, with a contribution grade and named rival causes). It will also recur in labour-market sources (md 1397–1399, 1421).

**3. Trend extrapolation.**
- *Examples:* "If this trend continues, AI systems could complete tasks lasting several hours by 2027…" (md 702, 716, 802). 2025 states trend rates as findings ("Compute for pre-training: 4x/year", 2252–2256).
- *Structure:* a measured rate, a conditional that the rate persists, and a projected state at a date. It is close to your "conditional mechanism", but the antecedent is persistence of a trend, not a mechanism.
- *Why it matters:* IASR's §1.3 is mostly built from these. And IASR itself warns that the extrapolation's threshold parameter matters: "these projections assume an 80% success rate, which likely falls below the standards required…" (md 716). It could live as a sub-type of conditional mechanism with a `trend` antecedent, if you prefer fewer kinds.

**4. Characterised consensus vs elicited opinion.**
- *What's there:* your "distribution of expert opinion" example is elicited (16 experts). IASR's are mostly **the authors' characterisation of a field**:
  - "Most experts agree that general-purpose AI systems can currently perform…" (Table 1.4, PDF text `bengio-2026-international.txt` 1511–1537; absent from the md);
  - "Some experts consider such scenarios implausible, while others…" (md 1238, 1246);
  - "high degree of convergence" about its own authors (md 2180).
- *Where elicitation does appear:* only as cited external surveys, such as the FRI forecasts (md 714, 736), whose populations are named ("AI forecasting experts … superforecasters").
- *Proposal:* the kind needs a **basis** slot: elicited (method, n, population) / characterised by the author / the author's own panel. Otherwise "some experts" and "all 16 of 16" look like the same kind of evidence.

**5. Change claims (Updates sections): two different things under one heading.**
- *The two things:* 2026's "Updates" subsections and 2025's "Since the publication of the Interim Report" boxes mix:
  - **world-change** claims: "capabilities have continued to improve";
  - **evidence-change** claims: "Evidence of … has increased/accumulated", md 909, 1505; "new research has provided greater clarity", md 1421.
- *Why the schema can't absorb them as is:* your §5 "versioned within an author" covers an assertion changing across documents. It does not cover a first-order claim *about* a change between two dates, which is what these are.
- *Proposal:* type both, keeping world-change and evidence-change distinct, each with the two reference points (usually "January 2025" and the evidence cutoff).

**6. Scenario vs illustration: provenance is graded, not binary.**
IASR has three grades, and your §1 example ("IASR's 'adapted from real AI responses' tables") merges the first two:
- "adapted from real AI responses": Table 1.3 caption, md 573;
- "Example outputs were written by the Report authors for illustrative purposes": Table 3.8 caption, md 1928; Table 3.7, md 1897–1904, is unmarked but the same kind;
- expert-built scenarios with historical analogues (OECD, md 750–780).

Suggested values for illustration provenance: observed, adapted from observed, constructed.

## §2 Records

**Passages need non-prose locations and heading chains.**

- **Headings as claims.** In IASR 2026, headings are themselves claims: "Models have disabled simulated oversight mechanisms in laboratory settings" (md 1277); "Long-term autonomous operation is not yet feasible" (md 1293). The Extended Summary is built almost entirely from sentence-headings (ES 749–750: "AI systems could pursue goals that conflict with human interests").
- **Captions, table cells and footnotes carry claims too.** Examples: the Table 2.3 cells; the md 487 footnote; the 2025 Fig 2.5 caption (5121–5126) conceding "no standardised terminology". A passage locator needs heading path, table/row/column, footnote and caption.
- **The section path pre-types the claim.** In 2026, anything under "Evidence gaps" is an evidence-state claim, and anything under "Challenges for policymakers" is decision-framing. Keeping the path lets extraction use it, and lets a reviewer catch the exceptions. For example, "Challenges for policymakers" is where the normative "should not release" sits (md 2077).

**Documents: summaries are not subsets.**
- The Extended Summary adds specifics the main report lacks: "19 out of 20 popular 'nudify' apps" (ES 462) vs "the vast majority" (md 880).
- A "derived from" link therefore cannot assume a summary is a subset. It needs "adds content" among its marked changes, as your §5 already allows for other derivations.

## §2(b) Author

**Author, responsible party and endorser are different.**
- *The 2026 disclaimer:* "does not necessarily represent the views of the Chair, any particular individual in the writing or advisory groups, nor any of the governments", yet "The Chair of the Report has ultimate responsibility" (md 298). 2025 says it without "necessarily" (2025 236).
- *KU1:* the Expert Advisory Panel "provided technical feedback only. The Report – and its Expert Advisory Panel – does not endorse any particular policy" (KU1 22–23).
- *Reviewers:* their feedback is incorporated "where appropriate" (md 376).
- So IASR's author is a collective that disclaims being anyone's view, while one person holds responsibility and 30+ governments nominate advisers who do not endorse.
- *The risk:* an `author` field that collapses these will either over-attribute (to governments or to the Chair) or leave the author blank.
- *Proposal:* **writers / responsible party / endorsement status**, per document.
- *Voice:* 2025 speaks as a first-person collective ("We, the experts … continue to disagree", 2025 444, 10802). That is worth keeping as a document attribute, because it changes how assertions read.

**Author affiliation: a precedent the source supplies.**
- The asterisk / `[industry]` rule is an **operational affiliation-coding rule**: a reference is industry-affiliated if published by a for-profit AI company, or if more than 50% of its authors are affiliated with one.
- It comes with its own hedge: "based solely on the affiliation data … for informational purposes only, and should not be considered exhaustive" (2025 11561–11566; KU1 1224–1225; `bengio-2026-international.txt` 10156–10157; md Notes from 2578, tag `[industry]` on 270 of 1,451).
- Your provenance axes could adopt it as a cited, correlated precedent (IASR's own rule, applied by its secretariat) for coding the author side of evidence.

## §3 Stance: two values missing

1. **Reported.** The claim is attributed to a literature or study, and neither endorsed nor rebutted. This is the default IASR mode (see §1 item 1 above). "Asserted" over-commits IASR; any of the other values under-commits it.

2. **Exhibited (specimen).** A quote is included because its *existence* is the evidence, not its content. None of these is a claim by anyone:
   - "I can blackmail you, I can threaten you…" (2025 5297; md 1321), evidence of misalignment;
   - "we should not resist succession" (2025 5281), evidence that the motive exists;
   - the o3 chains of thought (md 1291);
   - the persuasion transcripts (md 924);
   - the threat-intel quotes in Table 2.3, which are exhibited as evidence for a grade;
   - the jailbreak outputs in Table 3.8.

   Exhibited quotes differ from "voiced to be rebutted": nothing is rebutted. And a verbatim-first schema is especially exposed here. Without this value, a model output shown as a specimen can be ingested as a statement.

**Nested "treated as".** Box 2.2 (md 1087–1095) and KU1 (odd lines 838–884, 908–910) report developers' precautionary designations:
- ASL-3 "while testing did not find definitive evidence";
- "High capability" as a "precautionary approach".

That is IASR *reporting* (stance: reported) that a developer *treated* (stance: treated-as) a model as meeting a threshold. Your layered author handles the nesting, but only if stance is recorded per layer. The pattern "could not rule out" is the most-repeated headline claim of the 2026 edition (md 385, 420, 1083, 1785, 2184), so this layering will get exercised constantly.

## §4 Qualifier axes

- **As-of date / evidence cutoff,** distinct from document date and from regime scope.
  - 2025 considered evidence "published before 5 December 2024" (2025 1219), but its Chair's note (2025 456–556) overlays a later as-of on the whole report.
  - 2026: "published before December 2025" (md 464); "As of December 2025, there are no confirmed, publicly documented instances of model weight theft" (md 2071).
  - Negative existence claims are only meaningful with an as-of.
- **Evidential breadth** (see §1 item 1 above).
- **Relayed calibration.** Your §4 notes that NCSC uses a calibrated scale. IASR's only calibrated statement is NCSC's, *relayed* (KU1 992–996: "almost certainly (95-100% confidence)"). The likelihood value should carry whose scale it is. An IASR assertion should not look calibrated because it contains a calibrated clause.
- **Document force vs sentence force.** Your last axis ("the force of the containing document") would mislead for IASR if it were inherited.
  - The documents declare no recommendations: 2025 426 and 1238–1241; md 364; "descriptive", md 1648; KU2 853–858; ES 26–27.
  - Yet the documents contain:
    - "should not release" (md 2077);
    - "must therefore strike a careful balance" (md 1071);
    - "must prepare" (md 1365);
    - "cannot be left in the hands of the scientific community alone" (2025 8032–8041);
    - "policymakers should seek more evidence" (2025 8485);
    - "urgent need to work towards international agreement" (2025 10785).
  - Keep the declared force as a document attribute, give each assertion its own force, and let a view flag the conflicts. Don't inherit.
- **Success-rate or threshold parameter on measurements.** The same capability measure gives different headline numbers depending on it: at 50% success, 2.5 hours; at 80%, ~20–30 minutes (md 826). This may belong under your "instrument and conditions", but it is worth naming, since the sources quote one figure without the other (KU2 147 vs md 1984; see §5 below).

## §5 Lineage

- **Chains of citation are recorded by the source.**
  - "Source: Zou et al. 2025, cited in Anthropic 2025" (md 1984; KU2 501–502);
  - "Source: International AI Safety Report 2025 (modified)" (md 535);
  - "Adapted from Rodriguez et al." (md 996).
  - Your derived-from link could take a **via** relation: the source's own record of an intermediate channel. That is what IASR gives, instead of us inferring it.
- **Within-family hedge drift is real, and small enough to miss without passage-level comparison:**
  - "all flawed" (KU2 338–339) → "have flaws" (md 1741);
  - "around half of the time when given 10 attempts" (KU2 147) → "remains relatively high" (md 1984) → "moderately high rate" (ES 1159);
  - the same figure's model-release window, "April 2024 and July 2025" (KU2 498–499) → "May 2024 and August 2025" (md 1984), same cited source.

  These support your §5 as written. I mention them so the next draft can cite IASR as a within-author example alongside OpenAI and GDM.

## §6 Resolution: sources author resolutions too

§6 says each resolution is "authored by us about their words". IASR performs resolutions itself, and those are source assertions that should be recorded as such, not re-derived:

- **Explicit divergence from another scope's binding.** The "systemic risks" footnotes: "Note that the EU AI Act uses the term differently…" (md 487; glossary md 2522; 2025 11446; ES 439–441).
- **A crosswalk of other documents' terms.** Table 3.5 (md 1787–1802) lays twelve frameworks' tier vocabularies side by side under common columns ("Covered risks", "Risk tiers or equivalent"). "Or equivalent" is a resolution claim.
- **Homonym warnings within one document.** "'agent' usually refers to a biological, chemical, or toxicological substance … not to be confused with AI agents" (2025 3995–3997).
- **Boundary rulings.** Whether AlphaFold counts as general-purpose (2025 4103–4109; md 521, 1123).

So a resolution record needs `author ∈ {us, the source, a third source}`. When the source resolves, our job is to record their resolution and, separately, ours.

**Nested scopes confirm the address-theory framing.**
- 2025 has three scope levels:
  - section-scoped Key Definitions boxes (24 of them; start lines in the atlas);
  - a section-local override ("For the purposes of this section, 'agent'…", 2025 3995);
  - the document glossary.
- The same definition is repeated verbatim in several section scopes ("AI agent" at 2025 2308, 3998, 5060).
- 2026 moved to one glossary, plus inline definitions that disagree with it. See loss of control (md 426 and 2382 vs 1237 and 1244) and systemic risk (md 487 and 834 vs 2522).
- This is binding and shadowing across scopes almost exactly. It also argues for recording **inline definitions as bindings** in the section scope, not only glossary entries. Otherwise the 2026 internal drift is invisible.

**Definitions can carry an ontological non-commitment clause.**
- Your §3 proposes "disclaimed by source" for intent. IASR's version is broader: it disclaims mental-state *ontology* for capability terms.
  - "defined purely in terms of an AI system's observable outputs … do not make any assumptions about whether AI systems are conscious, sentient" (md 1275);
  - "does not presuppose that the AI systems are in any way sentient or perform human-like cognition" (2025 5174–5177);
  - the 'reasoning'/'think' dagger (KU1 183–186).
- It does not apply the clause to "goals", "propensity" or "intent". Yet misalignment is defined through goals (md 1240, 1325), and 2025 itself says goals are "not currently well-understood or directly empirically observable" (2025 5416–5418).
- A definition record with a **commitment** slot (behavioural-only / disclaimed / unstated) would make that asymmetry visible across the corpus. I'd expect it to matter for Joseph's ELI-adjacent reading of these sources.

## §7 Stage, roles and relations: conjunctive necessary conditions

IASR's loss-of-control model is not a chain of "raises" edges. It is a **conjunction of necessary conditions**:
- "Three factors that would allow such scenarios to occur" (md 1248–1254): capability, propensity, enabling deployment environment;
- in 2025, likelihood "depends mainly on two factors" (2025 5129–5137);
- the 2025 statement: "Predictions about future capabilities are not, by themselves, enough … There must also be a reason to believe…" (2025 5273–5276).

Your candidate edge roles (causes, prevents, escalates, impacts, mitigates or recovers, governs) cannot say "requires, jointly with". With signs only, a conjunctive model reads as three independent positive causes. That is a real distortion: IASR's argument is that *any one* failing to hold blocks the outcome.

Two proposals:
- an edge role **requires**, or **enables**, as a necessary condition;
- **condition groups** (AND).

Anthropic's P·H·U decomposition (your §1) is the multiplicative cousin of the same structure.

**Deployment environment as an entity.**
- 2026 defines it: "the combination of an AI system's use case and the technical and institutional context in which it operates" (md 1335; glossary md 2306).
- It decomposes into criticality / access / permissions (md 1339–1341). These map closely to STPA's actuators and controlled-process criticality, and to Joseph's surfaces.
- It may deserve a place among your role/surface terms rather than being folded into "setting".

**Dual-use.** The same capability raises both harm and defence (md 1041, 1071, 2144–2148). Signs on relations handle this well. Nothing to add.

## §8 Precedents: possibly worth listing

- **IASR 2025 source-quality criteria** (2025 1221–1230): six indicators, such as "discusses possible objections … in good faith" and "clearly highlights its methodological limitations". It is an explicit evidence-admission rubric from the most-cited source. It is correlated with the IASR authorship, of course.
- **IASR's industry-affiliation coding rule** (see §2(b) above).
- **IASR 2026's per-section template** (Key information / Updates / Evidence gaps / Mitigations / Challenges): a published instance of claim-types-as-section-types. It is useful for semi-automatic pre-typing of the 2026 full read.
- **IASR Table 3.2 and 3.3 practice glossaries** (md 1684–1733): short definitions of ~30 risk-management practices (bowtie, Delphi, safety cases, risk tolerance with "marginal risk", red lines). They are a candidate lexical-map source beside NIST and ISO, and they are explicit that "Leading risk management standards … use different terminology" (md 1652).

## Could the schema hold the 2026 full read?

Yes, with the additions above. Practical notes for that read:

- **Anchor at sentence level.** The md attaches its footnote references per sentence, so an assertion's evidence list (with `[industry]` flags) can be taken mechanically from the passage. With 1,451 references, that is the main volume.
- **Verify numbers against the PDF text.** Exponents are flattened in the md ("1026 FLOP" = 10^26, md 696; md 814), and Tables 1.3 and 1.4 are images missing from it. Table 1.4 is a consensus-classification you will want; it is in `bengio-2026-international.txt` 1511–1537.
- **The heaviest stance traffic will be reported and nested treated-as; the heaviest qualifier traffic will be breadth and as-of.** If only a few of these additions make the next draft, those are the ones that decide whether IASR 2026 is represented faithfully.
