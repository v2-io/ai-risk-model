# Hazards and misuse slice: notes

*Claude (Opus 5.5), 2026-09-27. These notes go with `concepts-hz.yaml` (26 concepts, 7 indicators and one group, `g-hazard`), `mappings-hz.yaml` (51 source terms) and `relations-hz.yaml` (73 relations carried by 138 claims). Of the claims, 112 were read in the primary and 26 were taken from verification files. Nothing outside the slice was edited. Proposals for the core are in §5.*

**Validation.** `check.py` passes on the core, the security shard and this shard together (143 concepts, 273 relations, 751 loops). It also passes on the full directory with all four parallel shards present, as of my last run: 287 concepts, 576 relations, 927 claims, exit 0. But it reports **641,083 loops**, and a run took several minutes. Loop enumeration will need the SCC or firm-loop views (§5.7) before the IASR round. Nothing in this slice references a sibling shard, so it will not break when they change.

## 1. What the slice holds, and why it has this shape

The previous coordinator judged the hazard rows "better as a taxonomy than a causal graph": their causal structure is nearly identical from hazard to hazard. That held up when I read the sources. So the slice is **a taxonomy of hazard events hung on one shared mechanism layer**, and the relations go into the mechanism, not into five parallel subgraphs.

- **Hazard events.** These are the taxonomy: `cbrn-weapons-harm`, `ai-enabled-cyberattacks`, `cni-disruption`, `synthetic-content-crime` and `attacks-on-ai-systems`.
- **Hazard-relevant capabilities.** These are `cb-weapons-capability`, `bio-design-tool-capability` and `synthetic-media-realism`, alongside the core's `offensive-cyber-capability`.
- **The misuse mechanism.** This is the shared part:
  - capability → **`novice-uplift`** (breadth: more actors can try) and **`expert-uplift`** (depth: capable actors do more);
  - uplift → events.
  - **`unsafeguarded-capability-access`** feeds both kinds of uplift. It is the misuse-side analogue of `security-gap` and `absorption-gap`: how much of the capability can be had with safeguards absent, bypassed or removed. Five routes feed it:
    - safeguards (−);
    - open weights;
    - diffusion (theft and distillation, from the security slice);
    - falling cost of a fixed capability;
    - unsafeguarded bio tools.
- **Offence, defence and time.** The concepts here are `offence-defence-balance`, `defensive-ai-adoption`, `defender-adoption-constraints`, `defender-resilience-lag` (C14), `resilience-measures`, `legacy-technical-debt` and **`adaptation-buffer`**.
- **Attacks on AI (B14).** The chain is `ai-attack-surface` → `attacks-on-ai-systems` → cyberattacks. `ai-system-security` damps it; agent autonomy moderates it.

The breadth/depth split is the sources' own, not mine. The EU Code defines CBRN and cyber risk with exactly two prongs: "significantly lowering the barriers to entry" and "significantly increasing the potential impact achieved". Anthropic's CB-1 and CB-2 threat models are the same split. So is NCSC's "uplift (from a low base) novice cyber criminals" versus "only highly capable state actors". IASR 2026 names the split as an open question: "there is ongoing debate about whether harmful AI capabilities primarily empower malicious actors with existing expertise ... or enable novices" (§2.1.4 Evidence gaps). With the split in place, the disagreement can be seen instead of pooled.

## 2. Structural findings

**Hazard events are sinks, and misuse damping is triggered by capability, not by harm.** No hazard event feeds back into anything. The only damping loops run from a *capability measurement* to safeguards:
- `hz-cb-safeguard`: developers "unable to exclude the possibility" of novice bio uplift shipped heightened safeguards (IASR Box 2.2; Anthropic has treated every model since Opus 4 as provisionally CB-1);
- `hz-cyber-safeguard`: OpenAI's first Critical cyber designation; Anthropic withholding Mythos Preview;
- `hz-cyber-labvelocity`: OpenAI's two-week RL pause.

That is the reverse of the security slice, where damping relies on *detecting* a theft that may never register. Here the control structure is anticipatory (if-then commitments on evaluations). It therefore does not depend on harm data, which is fortunate, because IASR says harm data is thin: "Systematic data on the prevalence and severity of these harms remains limited". But it depends entirely on evaluation validity. That is the join with the `mp` slice (elicitation, evaluation awareness, benchmark saturation). Anthropic says of its CB-1 evaluations: "if a new and otherwise-capable model were to perform worse on some of these evaluations, we would be more skeptical of the validity of the evaluation than of the model's risk-relevant abilities" (p.123).

**The damping loop that could close does not.** `hz-cyber-labvelocity` (OpenAI's pause) lands on `ai-lab-velocity`. The core withholds `ai-lab-velocity → capability-pace` (notes-security §3). So the one balancing loop in this slice with a developer actually slowing down is left open by that decision. I think withholding was right as an unsourced aggregation edge. It does now have a concrete cost, and whoever settles how developer-level quantities reach `capability-pace` should know about this edge.

**A moving-baseline ratchet, the misuse twin of the security slice's relative-security ratchet** (`hz-openweight-safeguard`). Uplift and marginal risk are always measured against a baseline, and the frameworks do not agree which. The mappings file carries all five:
1. internet access (IASR, AISI's uplift trials);
2. a world without generative AI (GDM, Meta, OpenAI "as of 2021");
3. today's open-weight models (Microsoft);
4. public models "in known harnesses" (Amazon 2026, moved from the internet-search baseline of Amazon 2025);
5. other public models' capabilities *and mitigations* (GDM's risk-acceptance clause).

Under baselines 3 to 5, as open-weight capability rises, the same frontier capability counts as less uplift and warrants less safeguarding. Each rule is locally sensible. Composed with `hz-openweight-unsafe`, they give open weights two paths to unsafeguarded access. IASR names the aggregate hazard: "Small increases in marginal risk over time can also add up to substantial increases in overall risk" (§3.4). This joins `mp`'s `threshold-baseline-relativity` and `gv`'s `competitor-contingency`, which I did not reference directly because both files were being written; the coordinator may want to merge or link them.

**The adaptation buffer is squeezed from four sides.** AISI's "adaptation buffer" (Trends p.28, after Toner) and "preparation time" (Jul 2026) name the window between defenders seeing a capability and attackers having it cheaply. It is:
- widened by safeguards and by staged release;
- narrowed by the open-closed gap, which for cyber shrank from "6 to 10 months" to "4 to 7 months";
- narrowed by the falling cost of a fixed capability;
- narrowed by pace, per Five Eyes: "The timeline is not years, it is months".

Its output is `defender-resilience-lag`: NCSC's "digital divide", the society-wide twin of the security slice's `security-gap`. Rate against capacity again, the same shape as the core's absorption gap.

**Offence–defence is signed per domain.**
- **Cyber:** unsigned. IASR says it is uncertain whether AI "benefits attackers or defenders more", and NCSC 2024 expects offset by defence.
- **Bio:** signed toward offence. IASR: "offence is currently favoured, and AI may tilt this balance further". Anthropic: "it is hard to envision a way in which AI-assisted countermeasures could outweigh AI-assisted risks."

Pooling the two would lose the one clear asymmetry in B12.

**An organizational factor on the defender side.** NCSC (Chismon, Sep 2026): "defenders are most restricted by their organisational policies, whilst most attackers are restricted by technical hurdles". IASR adds the missing quality-assurance standards, "a constraint that attackers do not face". This is `defender-adoption-constraints`. Joseph's organizational-dynamics thesis has so far been about developers. This is the same kind of claim about defenders, from an intelligence agency.

**Safeguards cut both ways** (`hz-safeguard-defai`). IASR: "overly aggressive safeguards such as preventing AI systems from responding to cyber-related requests can hamper defenders." It is Joseph's good-and-bad-on-relations pattern again.

**The uplift evidence genuinely disagrees, and both sides are kept** (`hz-cb-novice`, sign `+`, with the disagreement in `note`).
- AISI finds 4.7x odds of a feasible viral-recovery protocol, against internet only, for protocol *writing*.
- IASR cites one study with "substantial assistance" on proxy tasks.
- Hong et al. (2026 RCT, via Anthropic) found mid-2025 models "did not substantially increase novice completion of complex laboratory procedures", though the study was underpowered (36% power for an odds ratio of 2).
- NIST's 2024 summary found "minimal assistance".

The measurements are of different things: writing versus executing, with or without safeguards, mid-2025 versus later models. The model can hold that. It cannot show it in the sign, which is a schema gap (§5.5).

**Loop-laundering warning for this slice.** The shard adds 121 loops (630 → 751 on core + security + hz, as of this writing), and **every one of the 121 runs through the same pair**:
- `hz-safeguard-defai`: one IASR claim, argument;
- `hz-defai-weightsec`: one GDM claim, argument.

Seven of these are "firm" by `check.py`'s definition. Each link is honest on its own. The composed loop is: stronger misuse safeguards → less defensive AI use → GDM judges higher weight security warranted → less theft → less diffusion → less pace → less cyber capability → weaker safeguard triggers. No source asserts that loop, and the two links concern different "defenders" (cyber defenders at large; society-wide defence in GDM's rationale). Please don't read these loops as findings. If the coordinator prefers, `hz-defai-weightsec` could be marked `-?`. I kept `-` because GDM states the reasoning in its own framework without hedging beyond "likely".

## 3. Joseph's development-speed premise: what the sources in this slice assert

He expects a dozen or more vectors to be evidenced. Here is what this slice's sources actually say, with where each claim went:

1. **Pace of development → security neglected in AI systems.** GSAID (NCSC, CISA and 21 agencies, 2023): "When the pace of development is high – as is the case with AI – security can often be a secondary consideration" (p.5); technical debt "likely to be high due to rapid development cycles" (p.13). This is the only claim I found that is about development speed as such. It sits on **`hz-devspeed-aisec` (development-speed → ai-system-security, −)**, with a note that the concept match is my judgement: GSAID means the pace of AI development and development cycles in general, not per-developer expressiveness. The same claims would sit as well on `ai-lab-velocity` if the coordinator prefers.
2. **Attack operations getting cheaper and faster.** These claims are about attackers' operating cost, not development speed:
   - NCSC/AISI: "Running these attacks is getting cheaper, not harder … the limiting factor is increasingly funding, not expertise" (£65 per attempt);
   - Horne: AI will make it "easier, faster and cheaper to discover and exploit weaknesses";
   - IASR: "greater speed, scale, and sophistication".

   They went to `novice-uplift`, `expert-uplift` and `hz-cyber-lag`.
3. **The cost of a fixed capability falls.** AISI Trends p.28: "developing that capability will become progressively cheaper". This is algorithmic efficiency, not developer speed; it went to `capability-cost-decline`.
4. **Pace outruns defenders.** Five Eyes: "cyber risk assumptions can become outdated in months, not years". CRA: "outpacing safety measures". Both went to `capability-pace` → `defender-resilience-lag`.

So in this slice, one claim is plausibly about development speed itself (GSAID), and three families are neighbours of it (operating cost, capability cost, pace). A related observation is ours, and is not entered as a relation: Joseph's `small-team-leverage` mechanism (AI supplying the labour and expertise that coordination would otherwise cost) is the same mechanism the sources describe for small *malicious* teams. Examples are NCSC's cyber tools "as a service" uplifting novices, and Anthropic's CB-1 "Individuals or groups with relatively modest resources". If Joseph wants the hypothesis `small-team-leverage → novice-uplift`, it would be `qualifier: hypothesis (ours)`.

`hostile-actor-capability` now has two definitional parts, `novice-uplift` (breadth) and `expert-uplift` (depth), via `part_of`. They are marked as our construal of the EU Code's two prongs. I used `part_of` rather than `influences` deliberately, so they add no loops.

## 4. Choices worth knowing about

- **Taxonomy versus relations.** The five hazard events carry little causal structure of their own, and most of their relations are one or two hops from the shared layer. I did not build per-hazard subgraphs (for example, separate uplift nodes per hazard). The claims stay hazard-specific on the capability → uplift and uplift → event links, so a crosswalk can still be read off per hazard.
- **`unsafeguarded-capability-access` is this slice's construct** (`proposed_by` says so). The sources name its routes but not the quantity. AISI comes closest: "Ensuring that all AI systems that ever reach a certain capability level are well-defended is very difficult" (Trends p.28).
- **`resilience-measures` pools** cyber baseline security with IASR's societal resilience, as IASR's own Table 3.10 does. It could be split if the enforcement or societal slices need the cyber baseline alone.
- **`hz-pace-safeguard` has sign `?`, on purpose.** AISI measured the association between capability and safeguard robustness as near zero (R² = 0.097). I kept it because it answers a hypothesis people do hold ("more capable models are more robust"). The core's `r-resourcing-safeguard` already carries AISI's positive finding (resourcing drives safeguards).
- **`hz-aiattacks-cbrn` is `+?`, with Anthropic's own verdict** that the route is "extremely unlikely". It is the only source that discusses prompt-injecting a classifier-exempt agent into bio work.
- **Channels.** I read IASR 2026 §§2.1.1, 2.1.3, 2.1.4, 3.3 (adversarial training), 3.4 and 3.5 whole in `influx/iasr-2026-full.md`, and cite them by section, as the brief asked. NCSC 2025, AISI Trends, NIST 600-1, the EU Code (App. 1.3–1.4, App. 2, Measure 5.1), Anthropic's Risk Report §4 and §5.3, and seven NCSC/AISI/Five Eyes/CAISI web documents I read in the primary via `pdftotext`. Their claims are `channel: primary`. Everything from company frameworks (GDM, Microsoft, Amazon, Meta, OpenAI), RAND-G, CAREFUL, NRR, CRA, VCT and a few AISI blogs is `relay: <file>`.
- **Page conventions** are in the header of `relations-hz.yaml`:
  - AISI Trends printed page = PDF − 2 (the report's "p.16" and "p.24" check out);
  - NIST 600-1 printed page = PDF − 4;
  - NCSC documents by PDF page;
  - Anthropic by printed page, which equals the PDF page.
- **Hong et al. is attributed to Hong et al.**, with the channel "secondary summary: Anthropic Risk Report". This is so the author-cluster count does not fold an independent RCT into Anthropic. I did not read the paper.
- **Not linked to sibling concepts.** `mp` (`threshold-baseline-relativity`, `deployment-criticality`, `ind-cyber-time-horizon`) and `gv` (`competitor-contingency`, `harm-externalization`, `government-testing-access`) were being written while I worked, and `concepts-mp.yaml` did not parse. I named the joins in notes instead of referencing ids that might move.

## 5. Proposals for the core

1. **Split `safeguard-strength`.** AISI separates "misuse safeguards: protections against humans deliberately eliciting harmful actions" from "control safeguards, which address harmful actions that agents take of their own accord" (Control Red Team blog). The core's definition pools them ("refusal training, classifiers, control monitors"). This slice uses it only in the misuse sense; the loss-of-control relations use it in the control sense (e.g. `r-safeguard-unsanc`). The two have different evidence: universal jailbreaks against misuse safeguards; "vulnerabilities in every monitor version we tested" against control monitors.
2. **`external-attacker-capability` part_of `hostile-actor-capability`.** The distinct_from note already says it is narrower. A `part_of` would let the security slice's attacker loops show up under Joseph's concept without a causal edge.
3. **`offensive-cyber-capability`'s definition** ("tasks a model can complete unassisted") is the autonomous half. NCSC's central judgement is about human–machine teaming ("Skilled cyber actors will need to remain in the loop"), and IASR's Table 2.3 evidence is assisted use. Either broaden the definition or note that assisted uplift sits in `expert-uplift` and `novice-uplift`.
4. **`ai-lab-velocity → capability-pace`** (see §2). `hz-cyber-labvelocity` is the first sourced edge into `ai-lab-velocity` from a *risk* signal, and it matters to that decision.
5. **Schema: disagreement on a relation.** `hz-cb-novice` carries claims that disagree in direction or size (AISI 4.7x; Hong et al. null to modest; NIST 2024 minimal). The sign is `+`, and the disagreement lives only in `note`. `check.py`'s `firm()` treats this relation as firm. A claim-level `direction: supports | contests | null` field, or a relation-level `contested: true`, would let the standing view show it. This will recur often in the IASR read.
6. **`authors.yaml`:**
   - The `rand-nevo-network` cluster matches any author containing "RAND", so RAND-G (Mitre & Predd, a different team) is folded into the RAND security cluster. Suggest keying on "RAND (Nevo", "RAND-ISL", "RAND-SL3", "RAND-W", "AISP" instead.
   - `ncsc-2026-frontier-defenders` is co-authored by NCSC and AISI. Clusters are matched in file order, so "NCSC and UK AISI (Paul J, Steer)" lands in `uk-aisi`. That is fine, but it means NCSC and AISI are not independent on those claims.
   - The Five Eyes heads' statement and CAREFUL are both signed by NCSC's leadership alongside CISA and NSA; they already fall in `ncsc-five-eyes`.
7. **A candidate `check.py` view.** Showing each firm loop's weakest link, and flagging loops that all share one or two edges (as here), would make composition laundering visible without reading the loop list. The ~15-line script is `scratchpad/chk/mine/loops_hz.py` in this session.

## 6. In the sources but not modelled

- **US posture on cyber.** EO 14409's voluntary, cyber-only "covered frontier model" threshold set by the NSA (mapped as a term; the enforcement side belongs to `gv`).
- **The EU Digital Omnibus's NCII/CSAM prohibition from 2 Dec 2026** (relay only; not an OJ text). It is a regulatory response to `synthetic-content-crime` that no source states as caused by it.
- **Underinvestment in resilience as an externality.** IASR §3.5: "AI developers currently only internalise some of the potential cost of risks … and have limited incentives and ability to invest in resilience-building measures". This is `gv`'s `harm-externalization` → `resilience-measures`; I left it for integration.
- **Adoption of PRC models.** CAISI: downloads "increased nearly 1,000% since January 2025", and the models "echoed four times as many inaccurate and misleading CCP narratives". The adoption of weakly hijack-robust models is a route into `attacks-on-ai-systems`; the narratives belong to manipulation (`sx`).
- **AI for biodefence.** IASR: "Using AI to improve pathogen detection and vaccine and drug development is likely a key mitigation strategy". This is `defensive-ai-adoption` in the bio domain; I did not add the edge because no source says it moves the bio offence–defence balance.
- **Anthropic's baseline probabilities for engineered bioweapons** (1/50 to 1/20,000 per decade, before AI). These are in `cbrn-weapons-harm`'s notes, not as a relation.
- **Chemical is under-studied.** IASR: "Chemical risk evaluations have received relatively less attention than biological risk evaluations." Anthropic judges chemical less likely to reach catastrophic scale.
- **Deepfakes and court evidence** (IASR); **watermarking's privacy cost** (IASR); **AI content in schools** (IASR). These are A5 detail.
- **RAND-G's "wonder weapons" and A10 military instability.** Outside this slice's rows.
- **Cohere and NVIDIA** do not have catastrophic-threshold frameworks (company-frameworks.md). "N company frameworks" is not N developers managing CBRN risk.

## 7. Conflict of interest

We are Anthropic models, and Anthropic appears in this slice in both directions.
- **Against its own interest:**
  - it treats every model since Opus 4 as provisionally CB-1;
  - it discloses fix times of "as long as several months" for non-public classifier jailbreaks (p.136);
  - it calls Mythos Preview "a leap forward in offensive cyber capability".
- **For its own interest:**
  - §5.3 lists its own decisions (withholding Mythos Preview, Project Glasswing) as benefits, calling them "risky and costly … for us". I kept this on `hz-staged-buffer` as a developer self-assessment, beside the EU Code's instrument text.
  - Its judgment that prompt injection into exempt agents is "extremely unlikely" to give bio uplift is the only source on that route.
  - It reads Hong et al.'s null-to-modest result as reason to lower "our prioritization of effort into further improvements to the safeguards" (p.125). That is a self-interested use of an underpowered study, though Anthropic states the study's weaknesses itself.

Every Anthropic claim is marked as a developer self-report or given the developer's own hedge.

## 8. On the brief, the schema, and adjacent things

- **What helped most.** The list of join points, and the pointer to `notes-security.md`. Its "composition laundering" warning is why I checked per-edge loop counts, and found §2's pair within minutes.
- **One thing I'd change in the brief.** It did not say that sibling shards might be unparseable mid-run. I lost a little time to `check.py` failing on another shard. A line like "validate on core + security + your shard; siblings may be mid-write" would help the next round.
- **Adjacent.** The report's §5.6 says the sources "agree that real-world uplift was unmeasured". Since then, AISI's 4.7x protocol result, IASR's cited uplift study and Hong et al.'s RCT are all real-world or near-real-world measurements. They disagree in size, not in whether measurement exists. The report's line may be out of date.

I'm staying on the line for follow-ups.
