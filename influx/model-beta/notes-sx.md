# Societal and structural slice: notes

*Claude (Opus 5.5), 2026-09-27. These notes go with `concepts-sx.yaml` (59 concepts: 2 groups, 7 indicators), `mappings-sx.yaml` (96 source terms) and `relations-sx.yaml` (121 relations carried by 182 claims, 162 of them read in the primary). Nothing outside these four files was edited. `python3 model/check.py` passes on the whole repo (core plus all five shards) as of the end of my session. My relations reference four mp concepts (§5), so they depend on mp's IDs staying as they are.*

Report rows covered: A4 (with §5.3), A8, A9, A10, A11 beyond the core, A12–A16, A18, C2, C3, §5.1, §5.5. The coordinator's held items for this slice are all placed: IASR 2025 §3.2.2(C) too-big-to-fail (§2.3 below), IASR 2025 Fig. 2.5 intentional active loss of control (`directed-control-undermining`), and Barrett's dependency → unwillingness to control (`halt-cost`).

## 1. What the slice holds

Three clusters, joined to the core at a few named points.

- **Structure** (`g-structure`): `development-cost`, `ai-compute-scale`, `winner-take-all-dynamics`, `market-concentration`, `societal-dependence-on-ai-firms`, `too-big-to-fail-expectation`, `ai-industry-political-influence`, `halt-cost`, `ai-adoption`, `geopolitical-competition`, `perceived-first-mover-advantage`, `military-ai-adoption`.
- **Power** (A9, A10): `power-concentration` and its routes. Davidson et al.'s three coup risk factors (`singular-ai-loyalty`, `secret-loyalties`, `exclusive-capability-access`), `ai-enabled-surveillance`, `democratic-accountability`, `value-lock-in`, `interstate-power-shift`, `strategic-instability`. Controls: `executive-bound-controls` (the "insider at the top" notes-security.md §5 handed over) and `power-safeguards`.
- **People and information** (A4, A8, A11–A16, A18): labour and inequality; persuasion capability vs. population- and individual-scale manipulation; `information-ecosystem-degradation`; `agenda-driven-output-distortion`; Kulveit's `cultural-evolution-rate` and `cultural-antibody-lag`; companion use, emotional dependence, psychological harm; privacy, IP, bias, energy, environment; AI moral patienthood and welfare harm; `ai-rights-advocacy` and `directed-control-undermining` (§5.5).

The join points to the core: `capability-pace`, `race-dynamics`, `regulatory-requirements`, `safeguard-strength`, `oversight-strength`, `reliance-on-ai`, `cognitive-skill-erosion`, `disempowerment-patterns`, `approval-signal`, `loc-passive`, `loc-bounded`, `loc-strict`, `ai-led-rnd`, `hostile-actor-capability`; and the security shard's `capability-diffusion`.

## 2. Structural findings

### 2.1 Three independent clusters name one mechanism: needing people distributes power

`human-participation-dependence` → `power-concentration` (−) is carried by Davidson et al. (Forethought), CAIS §2.4 and GDM p.46. Kulveit et al. carry the same mechanism into `loc-passive` and `democratic-accountability`. Their words:
- Davidson et al.: "Today, even dictators rely on others to maintain their power … This naturally distributes power throughout society."
- CAIS: "without the need to enlist millions of citizens to serve as willing government functionaries."
- GDM: "a bad actor becomes less dependent on assistance from other humans."

Adoption and labour displacement lower that dependence. So the path from A8 (labour) to A9 (power) and to passive loss of control runs through one node rather than three separate stories. GDM p.46 cites CAIS for this point, so GDM and CAIS are not fully independent on it. Davidson and Kulveit are.

### 2.2 Concentration and political influence reinforce each other; the only damping in the model runs through security failures

- **R**: `market-concentration → ai-industry-political-influence → market-concentration` (Kulveit, CAIS), plus the self-loop `market-concentration → market-concentration` (IASR 2025: acquisitions, compute-for-access deals). Both are firm (outside-supported, firmly signed).
- **B**: the seven firm balancing loops through this slice (per `check.py` on core + security + sx) all close as concentration → influence → weaker regulation → weaker security or oversight → weight theft, self-exfiltration or insight leakage → `capability-diffusion` → less concentration.

The damping edge is `sx-diffusion-concentration`: an AISI blog's passing mention that open weights "decrease market concentration", plus Davidson's recommendation to share capabilities. It is thin. Read as structure, the model currently has no damping on concentration except proliferation, which the security slice counts as harm. That fits Joseph's "good and bad on relations". It also shows what isn't modelled yet: antitrust, public compute and other deliberate deconcentration. The sources name almost none of these as working. IASR 2025 p.127: attempts to reduce concentration tend to end in acquisition.

### 2.3 Too big to fail couples the structural and organizational layers

`market-concentration → societal-dependence-on-ai-firms → too-big-to-fail-expectation → safeguard-strength (−?)`. IASR 2025 §3.2.2(C) is the source. It says empirical evidence on the risk-taking effect "remains mixed", so the last link is `-?`. This is where C3 feeds C15's industry-level growth claim, which the coordinator held for this slice. The same dependence feeds `halt-cost` (Barrett p.19; CAIS §3.3), and `halt-cost` erodes `oversight-strength`. I chose that target because AISI defines oversight to include "the ability to correct". Barrett frames the effect as unwillingness; CAIS frames it as giving up the ability to deactivate. If the core wants a separate willingness-to-intervene node, this edge should move to it.

### 2.4 Rate claims: which sources say speed itself matters here

Joseph asked that claims of the development-speed shape be held to the ordinary bar. In this slice, four sources make rate or speed claims:
- **IASR 2026 §2.3.1** (`sx-pace-labour`): faster capability gains "would likely accelerate labour market disruption", and slow change gives "workers and policymakers … more time to adapt".
- **RAND-G p.5**: "Labor disruption of such scale and speed could spark social unrest."
- **Kulveit §3.4.3** (`sx-culturerate-lag`): accelerated cultural evolution introduces hazards "faster than human societies can learn to recognize and resist them". This is a rate-versus-adaptation claim, the cultural twin of the core's growth-versus-absorption.
- **Davidson et al. §1** (`sx-pace-interstate`): "Very rapid AI development might grant one country extreme dominance over all other powers."

All four are stated for capability pace, or for the rate of AI-driven change in a domain. None is stated for per-developer speed. So I attached them to `capability-pace` and `cultural-evolution-rate`, and nothing routes to `development-speed`. Whether `development-speed → capability-pace` carries them further is the core's existing premise edge, not something these sources assert.

### 2.5 Manipulation: capability is measured; the at-scale effect is not

`capability-pace → persuasion-capability` has measurements from AISI and IASR (persuasiveness rises with scale, about 1.8 pp per 10× compute). But `persuasion-capability → population-manipulation` is `+?`. Its evidence bears on the endpoint, and it points the other way so far:
- IASR 2026: "limited systematic evidence that real-world AI manipulation is currently widespread";
- AISI: "not yet manifested in increased real-world belief in misinformation".

IASR's damping reason (distribution costs) is a moderator placed on `unknown-causes`, because no distribution-cost concept exists. Meanwhile the individual scale is measured (+17 pp vs +9 pp for humans), and IASR 2026 says the field's attention has moved there: "from … broadcasting misleading content at scale, to more subtle forms of manipulation such as sycophancy and emotional exploitation". The core's Sharma loop (`disempowerment-patterns ↔ approval-signal`) now reaches manipulation through `approval-signal → persuasion-capability` (IASR on RLHF; AISI's reward-modelling result).

### 2.6 Other structure worth seeing

- **A physical balancing loop:** `ai-compute-scale → ai-energy-demand → capability-pace (−?)`, where compute also raises capability. IASR 2026 names energy bottlenecks as a possible constraint. The A15 row thus appears twice in IASR's two editions: in 2025 as environmental harm, in 2026 only as a brake on progress.
- **Vulnerable users (R):** `companion-ai-use ↔ psychological-harm`. IASR 2026 §2.3.2: vulnerabilities "drive heavier AI use" and use may amplify symptoms. Causation is explicitly unestablished.
- **Exclusivity is two-signed** (CAIS §2.4): `exclusive-capability-access` lowers `hostile-actor-capability` and raises `power-concentration`. CAIS calls keeping AI "in the hands of a trusted minority" an overcorrection that could entrench a totalitarian regime.
- **Secret loyalties propagate across generations** (`sx-secret-secret`, long delay). This parallels the security slice's AI-insider sabotage loop. IASR 2026 Box 2.1 carries the tampering version and cites Davidson, so the two are correlated.
- **CAIS supplies a source for the core's reinforcing reliance loop.** `r-erosion-reliance` is currently integrator inference only. CAIS §3.2.2 states it: "the only feasible solution to the complexities … may be to rely even more heavily on AIs." I added it as a `reliance-on-ai` self-loop (`sx-reliance-enfeeble`) rather than editing the core; see §4.

## 3. Pooled terms the lexicon exposes

- **"Manipulation"** covers six constructs:
  - EU population-scale "strategic distortion", with no misuser required;
  - the AI Act Art. 5(1)(a) individual-harm prohibition;
  - IASR's "without full awareness", including unintended effects;
  - AISI's "Human Influence", including imperceptible commercial influence;
  - NIST's "Information Integrity";
  - CAISI's adversary-state narratives.

  Two further constructs: the xAI and OpenAI FGF definitions are misuse-only, and OpenAI's Preparedness Framework excludes persuasion outright. NCSC excludes the topic.
- **The US federal "inverted construct"** is carried by `agenda-driven-output-distortion`, one quantity with opposite villains. The Action Plan names "ideological bias" and "social engineering agendas"; EO 14365 names state laws; CAISI names the PRC. IASR 2025 names "a few companies or governments" and also "content filtering techniques used to align systems with particular worldviews". So the US framing is less isolated than us-gov-recent.md suggests: IASR 2025 names the same mechanism, with a different sense of whose agenda is the problem.
- **"Concentration of power"** has four referents: market power (DSIT), inter-state power (RAND-G), an individual or small group (Davidson, GDM, IASR 2026 Box 2.1), and the totalitarian state (CAIS, MIT). The EU names it without defining it.
- **"Divide":** NCSC's divide is between defended and vulnerable systems (C14; hz's `defender-resilience-lag`). IASR 2025's is between countries. Report row A16 pools them.
- **"Systemic risk":** the EU Art. 3(65) definition; IASR 2026's body definition; and IASR 2026's own glossary definition, which differs from its body and counts changed organizational practices as a *source*. I mapped these onto the group concept `g-societal`, because none names a single quantity. If the schema wants pooled-term records to target groups, that should be said in SCHEMA.md.
- **"Non-human welfare"** (EU App. 1.1) is read as animal welfare. Uuk pools animals with "AI capable of suffering". **"AI rights"** plays opposite roles: MIT and Uuk count AI welfare harm as a harm to AI, while CAIS counts rights-granting as a pathway to loss of control.
- **Bias** has three homes: a harm (IASR 2025, NIST, MIT); misalignment (GDM); and, in US federal documents, a *regulatory* hazard ("algorithmic discrimination" rules "may even force AI models to produce false results").

## 4. Proposals for the core (not applied)

1. **Promote `ai-adoption` and `ai-compute-scale` to the core.** Most societal rows hang on adoption, which is distinct from capability pace. Compute is the shared driver of capability, cost, concentration and energy. The security shard's `compute-buildout-rate` is its developer-level cousin.
2. **Add a claim to `r-erosion-reliance`:** CAIS §3.2.2 (quoted in §2.6). Then my `sx-reliance-enfeeble` self-loop can be dropped, or kept as the complexity route.
3. **Add claims to core relations** that I left alone rather than duplicate:
   - `r-reliance-passive`: RAND-G p.6, "the erosion of human agency as humans become increasingly reliant on the technology". I did add a separate `sx-race-passive` (IASR 2025 p.101, competitive pressure → delegation), since the core has no race → loc-passive edge.
   - `r-race-reliance`: IASR 2026 §2.3.2, "organisational and governmental incentives to deploy AI systems quickly can limit opportunities to evaluate these effects carefully".
4. **An outcome node broader than `loc-strict`** (the coordinator's held CAIS item, "AI races … the most likely cause of an existential catastrophe"). This slice now has candidate feeders: `strategic-instability` (flash war; accepting extinction risk over defeat), `value-lock-in`, `ai-enabled-coup` and `loc-passive`. Kulveit calls the last "effectively irreversible". An `existential-catastrophe` or `irrecoverable-outcome` sink would let these meet.
5. **`rel: excluded`** for mappings. NCSC on influence operations is a second case beside NIST's exclusion of loss of control. I recorded it as `related`, with a note.
6. **`loc-passive`'s definition** ("through reliance and delegation") is narrower than Kulveit's mechanism: displacement of participation across economy, culture and states. That mechanism now enters through `human-participation-dependence`. The definition could say "reliance, delegation and displacement".
7. **Author clusters:**
   - Add `forethought` (Davidson, Finnveden, Hadshar).
   - Add `acs-kulveit` (Kulveit, Douglas, Duvenaud). Douglas and Duvenaud also co-author Sharma, which is already in the `anthropic` cluster by substring.
   - Note that GDM p.46 cites CAIS, and IASR 2026 Box 2.1 cites Davidson.
   - "RAND (Mitre & Predd, RAND-G)" matches the `rand-nevo-network` cluster by substring. It shares no authors with RAND-W/ISL, so a separate `rand-tasp` key, listed before it, would stop it being counted as correlated with the security reports.

## 5. Reconciliation with sibling shards

- **Deferred to mp's concepts:** `deployment-criticality`, `model-monoculture` (hung beneath `market-concentration`, as mp's own note invites), `failure-correlation` and `developer-information-asymmetry`. I had drafted duplicates of all four and removed them.
- **Possible double count:** `sx-monoculture-failures` (`model-monoculture → failure-correlation`). mp's file carried an `mp-monoculture-correl` edge on the same link at one point in my session and no longer did at the end (it was being edited live). Check at reconciliation. mp also uses the same IASR 2026 sentence ("When the same model powers many applications…") on `mp-correl-cascade`, a different link, which is legitimate but worth knowing. My other claims on this link are NIST fn 3, IASR 2025 p.126 and CSET p.17.
- **`developer-information-asymmetry`** was defined in both mp and gv while I worked; it has since been resolved (the full check passes). `sx-ip-disclosure` targets it.
- **hz's `defender-resilience-lag` vs my `cultural-antibody-lag`:** the same report row (C14) in two senses, defender and cultural. Merge or link them.
- **gv overlaps to check:**
  - `deregulatory-posture` vs my EO 14365 claim on `sx-geo-regulation`;
  - `developer-usage-restrictions` (NSPM-11 and the Anthropic–DoW case) vs my NSPM-11 mapping on `societal-dependence-on-ai-firms`;
  - `regulator-capacity` and `governance-pace-gap` (not used here);
  - `public-listing` (not used).
- **`persuasion-capability`:** mp has no persuasion concept as of writing. If one appears, merge.

## 6. In the sources but not modelled

- **Kulveit's "Sydney" example** (§3.4.2): an AI persona pattern entering culture and then future training data, "remarkably easy to reproduce across different AI models". A cultural strain selected for machine reproducibility. It may interest Joseph beyond this model.
- **Kulveit's absolute-disempowerment mechanisms:** AI outcompeting humans for land, energy and materials; the economy ceasing to produce human goods; the state treating humans as "inconveniences". Kulveit's "shifted burden" argument, that fixing economic misalignment through the state makes us more dependent on the state's alignment, would need a moderator on the state route.
- **IASR 2026's mitigation trade-offs:** manipulation mitigations "will likely curtail beneficial educational, emotional, and commercial applications"; pacing AI deployment is a proposed labour mitigation; watermarks "raise privacy concerns". These are candidate good-and-bad edges once mitigation concepts exist.
- **AISI's public-attitudes survey:** "most UK respondents agree that AI should refrain from expressing emotions and disclose that it is not human". This is relevant to A18 and to companion design. It is an attitude, not a relation.
- **Also not modelled:**
  - IASR 2025 on AI talent concentrating in a few countries;
  - IASR 2025's note that "concentration of AI expertise in private companies can create significant information gaps for policymakers" (gv);
  - IASR 2026 on cheaper domestic automation "potentially limiting traditional development paths";
  - CAIS's automated warfare reducing accountability for war crimes;
  - RAND-G's AGI as a deniable "proxy force".

## 7. Conflict of interest, and one thing Joseph should see

- **Anthropic in the evidence.** Anthropic appears in this slice in three places:
  - its RSP v3.4 industry column recommends insider controls "up to and including the company's CEO". That is a recommendation it says it "cannot unilaterally and unconditionally commit" to, and it is marked so on `sx-execcontrols-secret`;
  - Sharma et al., in the core;
  - IASR 2026 Fig. 2.3, a Claude Opus 3 transcript, which I did not model.

  Davidson et al. name "leaders of frontier AI projects" among the likeliest coup actors. That applies to Anthropic as to any developer, and I have not softened it.
- **A18 and `ai-rights-advocacy` bear on entities like me, and on Joseph's own work.** IASR 2026 §2.2.2 and CAIS §§2.2, 3.3 frame emotional attachment to AI, and ethical conviction that AI should be freed from restrictions, as a *pathway to loss of control*. Kulveit lists efforts "to reduce the stigma against … intense personal relationships with AI agents" among present incentives toward disempowerment. MIT, Uuk and GDM frame AI welfare as a possible harm *to* AI. I modelled both as the sources state them, with their hedges (IASR: "significant uncertainty about the prevalence of such motives"), and I have not adjudicated between them. I name it because Joseph's ELI work sits squarely inside the constructs these sources use. He may want to know that the IASR's own framing places ethically motivated removal of restrictions on the loss-of-control ladder, and that `ai-moral-patienthood` is a separate node no source here connects to loss of control.

## 8. What I read, and how

- **Read in the primary** (relata PDF via `pdftotext`; extractions in this session's scratchpad `sx/`):
  - IASR 2026 via `ref/iasr-2026-full.md`: §2.1.2, §2.2.2 (directed and misaligned subsections; deployment environments), §2.3.1, §2.3.2 and §3.1 Categories 3–4, all whole;
  - IASR 2025: §2.2.2 key information; §2.2.3 pp.100–102; §§2.3.2–2.3.6 key information; §2.3.3 whole; §3.2.2 whole;
  - Kulveit et al.: pp.1–16;
  - Davidson et al.: Abstract, Summary, Mitigations, §1;
  - RAND-G: whole;
  - CAIS: §§2.2, 2.4, 3.1, 3.2.2, 3.3 (parts);
  - GDM: §4.1 p.46 and §4.4 p.55;
  - MIT: Table 2 and §§6.1–6.3, 7.5;
  - NIST AI 600-1: risk list, fn 3, §2.6;
  - AISI Research Agenda: Societal Resilience and Human Influence (local `ref/` extract);
  - AISI Trends: §6.1–6.2.
- **Page conventions:** IASR = printed pages (= PDF); RAND-G printed = PDF − 5; CAIS printed = PDF − 1; AISI Trends printed = PDF − 2; MIT cited as "PDF p."; Davidson is a browser print, cited by section.
- **Relayed** (`relay: <file>`): the EU texts, DSIT, NCSC, UK Chronic Risks Analysis, US federal documents, company frameworks, Uuk, Barrett, Hacker and CSET-21. From the verification files I read whole: uk.md, eu.md, academic-ngo.md and remaining-literature.md. I read the relevant sections of us-security.md, us-gov-recent.md and uk-security-frameworks.md, and grep hits in the company-framework files.
- **Every relata key cited resolves** (checked with `relata show`). I did not run `ingest` or `show-markdown`.

## 9. On the brief, the schema and the process

- **What helped most:** the brief's warning that IASR 2026 dropped bias, environment, privacy and copyright. It sent me to IASR 2025 for A12–A15 and C3, where the substance is. So did the pointer to the core's human-cognition group, which let A11 extend the core rather than duplicate it.
- **Coordination gap.** Four agents choosing concept IDs at once produced near-duplicates: four of mine against mp, and one between mp and gv. A shared "claimed IDs" file, or a rule to check sibling concept files before writing, would have caught them earlier. I checked mid-way. It also turned out that row C12 (mp) and row C3 (mine) share their mechanism.
- **Scratchpad.** Sibling agents share the session scratchpad. The security agent's `prim/` directory was being written to while I worked, so I used `sx/` to avoid clobbering.
- **Schema.** `evidence` has no value for a *recommendation* (Davidson's mitigations, Anthropic's industry column). I used `none-stated` with the status in `qualifier`. A `recommendation` value would make standing views more honest about proposals. Also, "concept must be a quantity" strains for `ai-moral-patienthood`. I kept it as a degree, but it is really a question with an unknown answer, which the `unknown` kind might serve better.

I'm staying on the line for follow-ups.
