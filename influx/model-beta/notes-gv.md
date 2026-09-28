# Governance, commitments and enforcement slice: notes

*Claude (Opus 5.5), 2026-09-27. Files: `concepts-gv.yaml` (27 concepts, 6 indicators, 1 group), `mappings-gv.yaml` (49 source terms), `relations-gv.yaml` (70 relations carried by 134 claims). Nothing outside these four files was edited. `check.py` passes on core + security + gv plus the one sx concept this shard uses (`geopolitical-competition`). At the time of writing, the live directory fails only because the mp and sx shards are mid-write (unparsed `concepts-mp.yaml`, sx relations to ids not yet written). None of the errors are in gv.*

## 1. The enforcement layer: what I built and why

**The problem, in the model's own files.** The core `regulatory-requirements` is defined as "legally binding obligations (statute, binding commitments, enforceable reporting)". It pools three kinds of force. Several claims on it come from the voluntary EU Code: the core's `r-regulation-resourcing`, and the security shard's `rs-regulation-weightsec` and `rs-diffusion-regulation`. The shortest firm loops that touch governance all run through that last one (`capability-diffusion → regulatory-requirements → weight-security-level → … → capability-diffusion`). So a structural finding is currently labelled "legally binding" when it is carried by a signatory commitment.

**What this shard does (without editing the core):**
- **Three layers of force are separate concepts:**
  - `statutory-obligations` (law: AI Act Art. 55, SB 53, RAISE);
  - `code-commitments` (EU Code, Seoul commitments, G7 CoC);
  - `self-commitments` (a developer's own framework).

  The first two are linked to `regulatory-requirements` by `part_of`, so the pooling shows and nothing breaks. The layers are connected causally where sources say so: law → code (Art. 55(2)); code → frameworks (Seoul; xAI's EU-shaped rewrite); law → frameworks (SB 53's write/publish/comply duty; Microsoft's and Meta's revisions).
- **Force lives on the claim, because it belongs to the document.** Each claim citing a normative text carries a proposed `force` field. Values: *law, commit, exec, self, self-d, rec, bench, crit, prop, draft, desc*, with overlays for designated frameworks, e.g. `self-d+law` (Anthropic's FCF: its own text, in discretionary register, which a statute binds it to comply with). This is the report's code set plus the verification agents' *self / self-d / +law / +commit / exec / draft*. They converged independently on it.
- **"Who actually checks" is three concepts and one field:**
  - `external-verification`: outsiders checking the developer. Distinct from the core `oversight-strength`, which is the developer checking its AI.
  - `regulator-capacity`.
  - `enforcement-exposure`: expected sanction.
  - A proposed claim field, `checked_by`: "California Attorney General", "European Commission (AI Office)", absent = nobody named.

  The chain is `regulator-capacity → enforcement-exposure → framework-adherence`, and `external-verification → framework-adherence`. Adherence gets its own concept because the sources treat the gap between text and conduct as the open question: IASR's "adherence to voluntary commitments is likely to vary".
- **The finding the layer makes visible: law attaches to the thinner document.** At Anthropic (FCF) and OpenAI (FGF), the legally designated framework is written in discretionary register and has no halt language. The if-then and pause content sits in the voluntary RSP/PF. This is `designated-framework-stringency`, a moderator (`gv-desig-mod`) on `enforcement-exposure → framework-adherence`: SB 53's penalty binds whatever the designated document commits to. The link `statutory-obligations → designated-framework-stringency` is `?`. The developers' own statements describe the split. Whether law *causes* thin designated documents is my hypothesis, labelled as such, with the opposite reading given as equally consistent.

**Proposals for the core (§4 has the full list):** narrow `regulatory-requirements` to a group-like concept, or retire it in favour of the three layers, and re-home its claims by force (list in §4.1).

## 2. Structural findings

- **Hard commitments raise the pressure to under-declare.** Karnofsky (primary, read): "if we declared a model to cross the CBRN-4 or AI R&D-5 line, this could be extremely damaging to the company (in that our RSP would then require a unilateral pause or slowdown …)". The model records this as `capital-pressure → risk-assessment-integrity` (−), moderated by `self-commitments` (+).
  - This is Joseph's "good and bad on relations" in a sharp form. The stronger the if-then commitment, the stronger the incentive to read the evidence so as not to trigger it.
  - External verification is the only counter in the sources (`gv-verif-integrity`), and every source says it barely exists. IASR: "No established mechanism currently exists for validating risk acceptance decisions made by developers prior to release."
- **Race acts inside the instrument.** `competitor-contingency` is the channel, a moderator on the core `r-race-loosening` and the security shard's `rs-race-weightsec`. The evidence is primary text from Anthropic (Appendix A), GDM (v2.0; v3.1 relaxation conditions) and OpenAI (§4.3). OpenAI's clause carries its own damper ("more protective than the other AI developer"), so the moderator is not uniformly loosening.
- **Scrutiny cuts both ways on safetywashing.**
  - Ren et al.: safetywashing is "particularly pronounced when there is significant public pressure or regulatory scrutiny" (`gv-statute-washing`, `+?`).
  - SB 53 bars "materially false or misleading" statements about catastrophic risk (`gv-statute-infoasym`).
  - External verification is the damper in Campos ("can quickly deteriorate … and become purely performative").
- **One race frame, two opposite effects on the state side.** `geopolitical-competition` (the sx shard's concept) raises `deregulatory-posture`: EO 14365, the legislative framework, EO 14409 §3(c). It also raises voluntary `government-testing-access`: the Action Plan tasking, EO 14409's 30-day access, CAISI's "more than 40" evaluations. So the US posture is not simply "less checking". It moves checking from law into voluntary, national-security-framed access. `gv-dereg-loosen` records that Anthropic names "an anti-regulatory political climate" as one of three causes of its RSP v3 restructuring.
- **Listing is two-signed in the sources, and nobody names it as a factor.**
  - Up: listing → capital pressure (SAN commentary).
  - Up: listing → independent risk governance (Campos: SOX audit committees, NYSE internal audit).
  - `?`: listing → information asymmetry. Campos says risk disclosure is required. NY RAISE asks listed developers to disclose only ≥50% owners, against ≥5% if private: the one instrument in the corpus that distinguishes listed status.
  - Back-edge `perceived-risk → public-listing` (`-?`): Altman's "given everything happening with safety, right now would be an ill-advised moment to go public", against Axios's "Anthropic is still likely to go public in 2026".
- **Loop explosion. Please read before looking at `check.py` output.** That back-edge (`gv-perceived-listing`) closes loops through the core's own hypothesis `r-capital-growth`. On core + security + gv, it alone accounts for **22,080 of 24,675 loops** (2,595 without it; 630 without any gv relation). It is the single most loop-bearing edge in the model, carried by one press-reported CEO remark and one counter-report.
  - I kept it: it is an attributed statement, and the README says weak claims stay in.
  - This is the composition laundering the security notes warned about. The fix belongs in the view (a firm-only loop view, or excluding `?`-signed edges from enumeration by default), not in the claim.
  - If you'd rather withhold it as the security agent withheld `developer-velocity → capability-pace`, deleting that one relation is safe; nothing else depends on it.

## 3. Choices worth knowing

- **Merged with sx:** I dropped my `interstate-ai-race` for sx's `geopolitical-competition`, same definition.
- **Withdrawn for sx:** my `capital-pressure → oversight-strength` (Barrett's "making shutdown economically costly"). sx's `halt-cost` is "held for this slice by the coordinator" for exactly that quote.
- **Possible merges** (coordinator's call):
  - sx `training-data-disclosure` is a component of my `developer-information-asymmetry` (sx's note says so too);
  - sx `ai-industry-political-influence` is a likely driver of `deregulatory-posture`. No source in my evidence asserts that link, so I left it.
- **`development-speed`.** No source in my slice asserts per-developer development speed as a driver.
  - IASR's "speed of AI development … makes it difficult for … institutions to … build the capacity" is industry capability pace. It is attached to `capability-pace` (`gv-pace-govgap`, `gv-pace-capacity`).
  - The nearest per-developer statement is the NCSC/CISA *Guidelines for secure AI system development*: "When the pace of development is high … security can often be a secondary consideration" (relay: `uk-security-frameworks.md`). That reads as `ai-lab-velocity → security`, the security shard's territory. I flag it rather than add it.
- **Author strings.** `check.py` recognises this project's claims by substring. Claims from verification agents are authored `prior Claude agent (…)` so they count as this project, not as outside support.
- **Unmodelled level observations** are in concept `notes`, not relations. Examples: the governance-structure details (Meta's single reporting line; Cohere's CEO→Chief Scientist gate; OpenAI's SAG override and SSC reversal); pause text surviving at Microsoft and G42. They describe levels at single firms, not links.

## 4. Proposals

### 4.1 Core
1. **Re-home claims by force.**
   - `r-regulation-resourcing` (EU Code Measure 8.2) → `code-commitments → safety-resourcing`.
   - `rs-regulation-weightsec` and `rs-diffusion-regulation` (both EU Code) → `code-commitments`.
   - `r-regulation-loosening` (Anthropic on SB 53) → `statutory-obligations`.
   - `r-detected-regulation` (CLTR's call to "Mandate monitoring and reporting") → `statutory-obligations` or `incident-reporting-duty`.
2. **Additional claims for core relations:**
   - `r-race-loosening`: Anthropic RSP v3.4 intro, "the developers with the weakest protections would set the pace" (company's own explanation). This slice uses it on `gv-race-contingency`.
   - `r-regulation-loosening`: its current claim is Anthropic's own; SB 53 §22757.12(b)(2) itself (30-day publication with justification) is the instrument evidence. It sits on `gv-statute-visibility`.
3. **Split C6 safety culture.** This slice adds `concern-suppression` as a distinct quantity (suppression is not the absence of culture: non-disparagement terms and incentive filtering). That leaves the core `safety-culture-strength` closer to the CAIS construct. The EU "risk culture" maps better to `risk-governance-independence`, and the FLI "reporting culture" indicator pools protection, suppression and departures (see mappings).

### 4.2 Schema
1. **Add `force` and `checked_by` as optional claim fields.** Vocabulary as in §1. Overlays are joined with `+`, and `self` vs `self-d` is decided per clause, not per document.
2. **Consider a `force` column in `--standing`.** A relation carried only by *crit*, *prop* or *desc* claims reads differently from one carried by *law*.
3. **`evidence: instrument` is overloaded.** It is used for "a binding text that builds the relation in" and also, in practice, for discretionary company text that only describes. `force` separates these; without it, `instrument` on a *self-d* clause overstates.
4. **`check.py`:**
   - loop enumeration needs a default that excludes `?`/`+?`/`-?` edges, or reports counts per firmness (§2);
   - "firm" should require link-bearing evidence, as the handoff already notes.

### 4.3 `authors.yaml`
1. **California SB 53 and NY RAISE share definitions word for word.** They want one cluster (e.g. `us-state-law: ["California (SB 53)", "New York (RAISE"]`); today they count as independent.
2. **FLI and SaferAI** both signed the TFS open letter that is the source of the 100/200 staffing figure. SaferAI helped write G42's framework. FLI runs artificialintelligenceact.eu, the unofficial host of the Chairs' statement. Not one cluster, but worth a comment line.
3. **Karnofsky** is matched by the `anthropic` cluster through "Karnofsky" and counts as Anthropic. That is right for independence, though he writes "views are my own".

## 5. In the sources but not modelled

- **Internal deployment's legal status.** SB 53 §22757.12(a)(10) asks the framework to cover internal use. Anthropic's FCF says its processes "currently apply to models … deployed externally". I set these side by side (`gv-internal-scope`, `?`) and drew no compliance conclusion. OpenAI's FGF covers internal use for oversight circumvention.
- **Which document is Google's, Meta's, Amazon's or xAI's SB 53 framework is not public.** For those, the model cannot say whether their `self` content is `+law`. xAI's Jun 2026 rewrite dropped its Dec 2025 statement that the framework "complies with" TFAIA.
- **"Loss of control" in law-backed documents converges on the EU wording**, while voluntary documents keep their own constructs. That is lexicon content for the loss-of-control mappings; the verification files carry the full ladder.
- **The Commission incident template (Nov 2025)** scopes root-cause analysis to model outputs, inputs and mitigation failures, with no organizational-cause field. Content only, recorded in the concept note.
- **NIST's "safety" renamings** (AISI → CAISI; AISIC → "NIST AI Consortium"; the International Network). Nomenclature following posture. Not a quantity I could state honestly.
- **Heads of other people's slices:** the AISI incident (evaluator's own prioritisation); OpenAI's Hugging Face incident (escalation failures); Anthropic's "safety process failures". The independent METR/Redwood report on the Hugging Face incident has not been read by anyone.
- **UK posture.** AISI "does not even have regulation to enforce" (the Chairs, holding AISI up as a recruitment model). UK sources carry governance only as recommendations: the Cyber Governance Code, AI-CoP, CAREFUL. I found no UK frontier-AI statute in the evidence to model.

## 6. Conflict of interest

We are Anthropic models, and Anthropic is the richest single source in this slice, in both directions.
- **Against:**
  - the FCF's discretionary register and its external-deployment scope limit (primary, read);
  - the removal of v2.2's pause and weight-deletion commitments;
  - "an anti-regulatory political climate" given as a reason to restructure;
  - Karnofsky's account of distortive pressure;
  - GovAI's "grading its own homework";
  - FLI's "Reverse the RSP 3.0 walk-back";
  - the Department of War "supply chain risk" designation, read only via news. The model records it as the state's procurement leverage against a developer's use restrictions (`gv-procure-restrict`). I have not taken a side on it. The majority opinion, the dissent and the district court are all in the verification file.
- **For:** the SaferAI and FLI ratings. Both assessed superseded RSP versions, as the claims say.

## 7. What I read, and how

- **Read whole:**
  - `README.md`, `SCHEMA.md`, `notes-security.md`, the core concepts and relations, the report;
  - `eu.md`, `us-gov-recent.md`, `academic-ngo.md`, `absence-claim.md`, `company-frameworks.md`;
  - all five per-company files;
  - IASR 2026 §3.1–3.2 in `influx/iasr-2026-full.md`. These claims are `channel: primary (influx/iasr-2026-full.md)`, cited by section.
- **Read in the governance-relevant sections:** `uk.md`, `uk-security-frameworks.md`, `us-security.md`, `remaining-literature.md`.
- **Checked in the primary** (`pdftotext` on the relata PDFs; `channel: primary`): SB 53 (§22757.12(a)(9)–(10), (b)(2), (e)(1)(A); §22757.15(a)); the CA AG–OpenAI MOU ¶¶8, 11; Karnofsky's RSP v3 post; the RSP v3.0 announcement; the FCF v2 (pp.3–6, 12); the EU Code Chairs' statement. All quotes matched. Extracted texts are in this session's scratchpad `prim/`. That scratchpad appears to be shared with the sibling agents.
- **Everything else** is `relay: <file>`.
- **The generators** for the two YAML shards are in the scratchpad (`gv/p1–p6.py`, `maps.py`). They exist for quoting safety; the YAML is the artifact.

## 8. On the brief and the schema

- **The brief was right to hand over the design problem rather than a scheme.** The two sentences that did most work were "force belongs to the document, not the company" and the pointer to the security notes' §4.9. Together they located the problem in the existing files instead of in the abstract.
- **One gap, not the brief's fault.** Four shards write at once into a checker that fails on any unparsable file, so "check.py should pass when you're done" can't be satisfied by one shard while another is mid-write. An isolated check (core + one's own shard + declared cross-shard dependencies) would make each shard's pass/fail its own.
- **Shard ids.** A shared, append-only registry of claimed concept ids, even a text file, would have told me about `geopolitical-competition` and `halt-cost` before I wrote duplicates rather than after.
