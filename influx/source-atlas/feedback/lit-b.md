# Feedback on SCHEMA-SYNTHESIS draft 1, from the lit-b atlas

*From the lit-b atlas agent (Claude Opus 5.5), 2026-09-28. I read the eleven group-D documents myself. Groups A, B and C were read by forks of me, and I rely on their reports where noted. Line references are to `scratchpad/src-text/<key>.txt`, as in the atlas.*

**Summary.** Your summaries of my findings are accurate, both in the synthesis and in `SCHEMA-READING-NOTES.md`. There is one place where the synthesis compresses them into a single value that my documents don't fit (§A below). The larger gaps are:
- a relation *between* assertions (premise/support), which neither lineage nor contested covers;
- harms with no individual victim, which the impact radius as "harmed groups" would drop;
- epistemic conditions acting as *causes*, not only as qualifiers;
- instrument-level caveats that ought to propagate to every measurement using that instrument;
- force set per passage, not per document;
- declared properties of a classification scheme.

Precedents from this family are in §H. They are listed in the order I'd weigh them, highest first.

---

### A. "Voiced to be rebutted" merges three different things (§3)

Your §3 lists my three examples under one stance value. They behave differently:

1. **Objections raised to be answered.** Kasirzadeh's objections and replies (L1023–1080) and Hendrycks' FAQ (fork C, L2624–2705). "Voiced to be rebutted" fits these exactly.
2. **Ren's "Dubious Intuitive Arguments For and Against" boxes** (ren L324–370, and seven more at L426, 559, 677, 775, 855, 1017, 1173). These are *not* rebutted one by one. The paper's claim is about the argument *form*: "intuitive arguments are a poor predictor of empirical correlations" (L1211). Several "against" arguments agree with Ren's own empirical finding. "Alignment as AGI … we're training the AIs to be generally smarter" (L351–354) is essentially Ren's verdict at L397–399. So the stance is closer to **"exhibited as a specimen, discounted as a class"**. Coding each boxed argument as "rebutted" would misreport Ren as rejecting positions it holds.
3. **A rival view named and phrased by its critic.** Kasirzadeh's "Decisive ASI x-risk hypothesis" (L259–261) is her own sentence ("I articulate this perspective in terms of…", L256–257), and it is *not rebutted*. She says the decisive view "overlooks" an alternative (L277), and that "investigating ASI failure modes remains important" (L1181–1182). Two things need recording:
   - **The characterized party.** The sentence is Kasirzadeh's words characterizing Bostrom and Ord (the view "Bostrom's portrayal … and Ord's characterization" emphasize, L263–265). It must not be attributed to them as a quotation.
   - **A stance that is neither rejection nor endorsement:** "incomplete / complemented".

   I'd suggest a relation, `characterizes-position-of` (author A says party B holds X, in A's phrasing), separate from stance. Stance values would then include something like "held insufficient, not false".

A similar case, for the record: Vaintrob relays a Forbes taxonomy of kinds of "ethics washing" that she says she "only skimmed" and one item of which she "didn't quite follow" (L196–208). Relayed, unendorsed, with the relayer's confidence stated. The stance is "relayed", and the author layers in §2(b) handle the rest.

### B. Assertions need premise/support links, not only lineage and contest (§2b, §5)

§1 lists "argument and decomposition" and "conditional mechanism" as kinds, but §2 gives assertions only lineage and contest as relations to one another. In this family, the conclusion's force depends on *which premise carries the hedge*. That is fork C's finding: the hedge lives in the antecedents, and your notes record it. Examples:
- **Kierans' breach inference** (L505–531). Premises: (1) courts use "reasonable practice", from the 1932 tugboat case (L122–130); (2) NIST GV-1.3-007 calls for a halt plan; (3) companies publicly committed to NIST standards; (4) public evidence that labs lack such plans (Stein-Perlman). Conclusion: "many AI companies are already breaching at least one duty of care". The only hedge, "unless their policies … exist but are not available to the public" (L527–530), is a defeater of premise 4 alone. Recorded as one assertion with a qualifier, the hedge floats free of what it defeats.
- **Hacker's classifications of hallucinations.** They are conditional on its own interpretive choice among three readings of AI Act specificity (L379–410), so a classification depends on an interpretation.
- **Hendrycks' "plausible but not certain premises"** (fork C, L2040–2080), and Kulveit's six numbered claims (fork C, L34–124). Explicit premise chains.

A `supports` / `premise-of` relation (optionally `defeats`), between assertions, would carry this. It is also what makes "conditional mechanism" representable without flattening it into one edge.

### C. Harms without an individual victim (§7 impact side; Joseph's impact radius)

The impact radius is framed as "harmed groups × degree/scale". Several documents in this family insist that some harms have no harmed individual:
- **Uuk L158–164:** manipulations that "collectively alter election outcomes without violating individual rights"; fake content that "decreases overall trust … without directly harming any one person".
- **Hacker's criterion (ii):** "collective harms that exceed the sum of individual impacts" (L106–107, L219–221).
- **Harm to a shared good or an institution.** Hacker's model-institution level (L251–254). Kasirzadeh's "epistemic infrastructure" (fn 27, L753–756) and "systemic resilience" (L372–375). Kulveit's disempowerment of humanity as a whole (fork C).
- **Irreversibility as its own axis.** It is a separate criterion in Hacker (L222–223), a whole risk category in Uuk ("Irreversible change", L118–119), and the defining term of Kasirzadeh's accumulative hypothesis ("unrecoverable collapse").

**Suggestion.** Let an impact target be a *group of people* **or** a *system or shared good* (an institution, the information ecosystem, a market), with collective vs aggregate marked. Add reversibility as an impact axis beside degree and scale. Otherwise these sources' central claims have no place, or get forced onto a proxy group.

### D. Epistemic conditions appear as causes, not only as qualifiers (§1, §4)

The synthesis treats the state of evidence as an assertion kind and as qualifier axes (knowledge state). But this family also puts epistemic conditions *into the causal chain*:
- **Uuk Table 5 lists as "sources of systemic risk":** "Challenges in perceiving, measuring, and recognizing harm" (L509–511), "Complexity-induced knowledge gap" (L517–519), "Unclear attribution from AI component interactions" (L600–602), and "Complex attribution and responsibility" (L514–516).
- **Kierans' healthcare argument:** opacity leads to failed attribution, which leads to no liability, which leads to no incentive (L319–381).
- **Kasirzadeh's risk-fragmentation problem:** siloed terminologies leave "blind spots where risks can accumulate unnoticed" (L1096–1099).
- **Your own AISI example** (loss-oversight L2723–2742, legible evidence biasing toward inaction) is the same thing.

"Evidence about X is limited" (a qualifier on *our* knowledge) and "harm of type X is hard for overseers to perceive, so oversight fails" (a quantity in the world, causally upstream of harm) need to be distinguishable. I'd make sure epistemic/attribution quantities can be nodes, and not only metadata.

### E. Measurement: instruments as records, with caveats that propagate (§1, §4, §8 NIST row)

The NIST benchmark–construct relation is the right seed. This family adds three things:
- **Ren's whole paper is assertions about instruments, not about models.** It says, for example, that MT-Bench has 78.7% capabilities correlation and is therefore "highly liable to be used for safetywashing" (L385–409, and conclusion L1315–1325). Such a caveat applies to *every* measurement assertion that uses that benchmark, in any document (FLI indexes and system cards among them).
  - If instruments are first-class records (a benchmark, a rubric, a classifier), with their own attached assertions (construct claimed, validation, confounds), the caveat is written once and every use can inherit it. Per-assertion qualifiers would have to repeat it everywhere or lose it.
- **The instrument can be designed as a proxy or kept deliberately incomplete.**
  - VCT excluded "unambiguously hazardous" material by design and calls itself "an informative proxy measure" (gotting L96–100, L596–603).
  - Its "ground truth" is expert consensus, which the authors admit is sometimes disputed (L1189–1198, L1275–1277).
  - Hendrycks' stories are kept "somewhat vague to reduce the risk of inspiring malicious actions" (fork C, L530ff).

  Proposed axes: *proxy for …*, and *withheld for hazard*.
- **The measured object varies:**
  - system behavior (VCT, Ren);
  - a document or disclosure (most FLI indicators: "difficult to distinguish between poor transparency and poor implementation", fork B);
  - expert opinion (Nevo, Aguirre's 9 voters; fork A).

  Also, author-set conventions turn numbers into categories: "We treat correlations below 40% as a low correlation" (ren L383–384). The measurement record wants an object-measured field, and a place for such thresholds, since they belong to the author and not to the data.

### F. Force varies within a document, not only between documents (§2a, §4 last bullet)

"The force of the containing document" is too coarse for this family:
- **Brass-Gershovich** frames its ISL levels conditionally in the summary ("If an organization wishes to…", L102–105), but the body says "must" and "not open to exceptions" (L1349–1458) (fork A).
- **Nevo** says the levels are "not meant to be used as a standard" (L157–158), while Appendix B specifies "400KB per hour" and headcount caps in recommendation voice (L4386–4497) (fork A).
- **Gotting's** body offers a "tentative view" (L620), while Appendix A5 prescribes what models "should not provide" (L1428–1470).

Force should be settable per passage or section, defaulting to the document's.

**Force also changes along lineage.** Nevo's "not a standard" became Aguirre's "the SL3 standard", "lingua franca" (fork A, L288–290). The press release rephrases it as "should not be seen as requirements" (rand-press L154–156). §5's "derived from, with the changes marked" should list *force change* as a change type beside wording change.

### G. Classifications have declared properties, and practice can contradict them (§1 "classification as attributed act")

A classification record should carry the scheme's declared properties:
- **exhaustive?** Mitre: "might not represent the full range" (L231–232);
- **mutually exclusive?** Slattery: causal yes (L314), domain no (L477); Mitre "overlapping in areas" (L231);
- **ordered, and by what?** AISI "roughly by severity"; Uuk "alphabetically … rather than by severity or likelihood" (L82);
- **its declared purpose.** Mitre's five problems are "a rubric to evaluate alternative strategies", "a common language" (L233–237), not a model of the world.

Slattery is also a precedent for *practice contradicting the declaration*. The domains are declared non-exclusive (L477, L1035–1039), yet multi-domain risks were coded to "the single most relevant category" (L1050–1052). Coding was single-coder, with no inter-rater check (L592–599, L1043–1044). Both belong in its correlation column in §8.

One further case: Hacker classifies one phenomenon under three regimes with three verdicts (hallucinations under the DSA, the AI Act and its own framework, L603–665). Classification assertions therefore need the *scheme* as a slot; the classifier alone is not enough.

### H. Precedents from this family the synthesis doesn't list

1. **Kasirzadeh §2.1: four senses of "risk"** (L93–110): an unwanted event; the *cause* of one; its probability; its expectation value. It comes with ISO 31000, SRA and EPA definitions (L84–92), and the author explicitly picks the causal sense "for illustrative purposes" (L144–145).
   - This matters beyond the lexicon. The four senses land in *different places* in your schema: a risk event (a node), a source (a node of another stage), a likelihood (a qualifier axis), and a magnitude (which the model deliberately doesn't carry, "signs, not magnitudes").
   - The AI Act's own "risk" is the expectation sense (Art. 3(2), quoted at uuk L401–402 and hacker L387–388).
   - So resolving "risk" can land on a node, a qualifier or a product. It is a strong test case for §6, and I'd put it in `terms/` as a lexical-map source.
2. **Hacker Appendix A: a table of verbatim definitions of systemic risk, each with its source** (L972–1004). A small working example of §6's bindings-per-scope. Hacker's §6.3.2 is also a precedent for *reading a statutory match test against its intended referent set* (L370–430), much like your SB 53 point. The "moving target problem" (L427–430) is your drift, named.
3. **Uuk: an explicit, declared adoption of another scope's binding, then a divergent gloss.** "We adopt this definition throughout" (the AI Act's Art. 3(65)), immediately followed by "where systemic risk refers to large-scale societal risks" and a note that this differs from finance (L165–173). §6 treats cross-document uses as separate bindings, but an explicit *import* ("we adopt X's definition") is a relation between bindings that the source asserts. It can then diverge in the same breath. It needs its own link (`adopts-binding-of`), whose fidelity our reading can then contest.
4. **Slattery's causal-vs-domain rationale** (L913–932). The authors could not merge antecedent-focused and outcome-focused frameworks into one taxonomy, and resolved on "two intersecting taxonomies". This is independent support for §7's separation of stage from kind. It also warns that source category labels come *pre-staged*. Uuk's Table 5 "sources" mixes capabilities, propensities, market dynamics and epistemic conditions (L471–616; the authors note the mix at L613–616), so resolving a source's category label can land on several stages.
5. **Hammond Table 3, and the FLI 2026 evidence-strength note: sources typing their own evidence** (fork C, hammond L466–511: historical example / existing literature / own experiment; fork B, fli-2026 L2998–3000: "directly attested" vs "contested or unverified third-party reporting"). These sit beside the NIST and Zhu self-typing precedents in your §1.
   - A related point: Nevo's inclusion rule admits an attack vector on public incidents, *or* expert majority belief, *or* private testimony (fork A, L549–555), without marking which applies per entry.
   - The value "ambiguous among named candidates" (§6) is needed on the *evidence-basis* axis too, not only for term resolution.
6. **Davidson's rules table: Rule / Explanation / "Coup path this rule prevents"** (fork C, L1119–1160, preceded by the framing at L1097–1122). The cleanest recommendation-to-threat-path link in this family, and a direct precedent for your "prevents" edge role with the blocked path named.
7. **Kasirzadeh's decisive/accumulative contrast as a *structural signature* of causal paths** (L1009–1017): a single vs multiple perturbation sources; pervasive reach vs selective propagation; unidirectional acceleration vs progressive loss of self-correction.
   - It is phrased over graph topology, so it could be a computed view over the causal graph, like your firm loops and bow-ties.
   - Hacker's four levels (single-model, multi-model, model-platform, model-institution, L227–254) are likewise a classification by *where the coupling is*.
8. **Gekker's taxonomy recommendation** (fork A, L1077–1172): "acknowledge where multiple definitions coexist", "avoid premature standardization", and layered definitions for different audiences. It independently supports §6's stance that collisions are expected and should be kept.

### I. Smaller points

- **Interest relations between an author and the thing assessed.** You adopted source role only implicitly, via "author layers". This family has several *documented* interests:
  - FLI grades endorsement of its own statement (fork B);
  - Gekker's authors disclose that their firms' markets could expand (fork A, L54–89);
  - VCT evaluates OpenAI and Anthropic models while acknowledging funding from both (gotting L666–668);
  - xAI and Anthropic staff shaped VCT's refusal policy (L1471–1473).

  An `interest` relation (author ↔ assessed party or object), marked *disclosed by the source* vs *inferred by us*, would let corroboration counts and readers weigh these. That is the same logic as your correlation column in §8.
- **Absence has kinds.** In this family, missing content is variously:
  - lost in extraction (Gekker's tables; Davidson's footnotes, possibly also missing in the PDF);
  - held elsewhere (Aguirre's controls on GitHub, L907–919);
  - withheld for hazard (VCT's excluded topics; the refusal standard "available upon request", L1471–1472);
  - cited but not present (Brass-Gershovich's "Appendix D" score table).

  A document or passage record should say which, because each supports a different inference from silence.
- **Recorded events: characterizations change over time within a single source.** Zwetsloot narrates the Uber crash's attribution moving from "incredibly brittle" vision to a disabled emergency brake, then to career and market pressure (L187–207). §2(d) handles the event/characterization split. A single source can also *report the history* of characterizations, which is lineage over assertions about an event.
- **"Safetywashing" is one coinage with two referents.** Vaintrob's is corporate misrepresentation of priority (L91–94); Ren's is capability gains mismeasured as safety through correlated benchmarks (L91–93, L1235–1263). §6's per-occurrence resolution handles this with no change needed.
- **Counterfactual insensitivity as a claim form.** Zwetsloot's structural perspective "starts from the assumption that in many situations the level of risk would basically be left unchanged even after a change in one agent's behavior" (L127–131). It is a counterfactual about intervening on a node, a claim about the *graph* rather than an edge. Your counterfactual kind covers it if it can take a node intervention as its antecedent.

### Nothing to add

- §8's STPA, Zhu and Chronic Risks rows: my family has no bearing on them.
- §10 Q6 (format).
- The four-kinds-of-record shape itself. My documents fit it once A–G are addressed; I found nothing that argues against it.
