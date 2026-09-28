# Security and insider-risk slice: notes

*Claude (Opus 5.5), 2026-09-27. These notes go with `concepts-security.yaml` (28 concepts and 6 indicators), `mappings-security.yaml` (43 source terms) and `relations-security.yaml` (90 relations carried by 132 claims). `check.py` passes. Nothing in the core files was edited. Proposals for the core are in §4.*

## 1. What the slice holds

The slice separates **routes** from **losses**. The core already has the routes `insider-exfiltration` (human) and `internal-ai-deployment`. The slice adds:

- **Losses:**
  - `weight-theft`;
  - `insight-leakage`;
  - `distillation-extraction`, which needs neither weights nor staff;
  - `insider-misuse`: using privileged access without taking anything.
- **AI insiders:** `self-exfiltration`, `rogue-internal-deployment` and `ai-insider-sabotage`.
- **Where human and AI insiders meet:** `shadow-agent-use`.

All the losses flow into `capability-diffusion`, where a security failure becomes proliferation and pace.

The operative variable for theft is **`security-gap`**: how far the attackers motivated to target a developer outrun the attackers its security can reliably stop. Anthropic's Risk Report (Aug 2026, App. 6.4.1, p.177, read in the PDF) names three trends that widen it. Each one became a relation:

1. **Attack surface.** Compute comes online faster than it can be hardened: `compute-buildout-rate → infrastructure-maturity-gap → security-gap`. This is the infrastructure twin of the core's headcount → `absorption-gap` mechanism. Joseph's hypergrowth question has a compute-side version, in a developer's own words: *"these environments do not all begin at the same level of security maturity."*
2. **Timescales.** Capabilities improve *"faster than the rate at which we can build and mature our defenses"*, so motivated attackers get more sophisticated faster than defences do (`capability-pace → theft-incentive → security-gap`).
3. **Displacement.** Closing the legitimate routes (anti-distillation, customer verification, ZDR limits) *"increase[s] threat actor incentives to access our models via weight theft"* (`anti-distillation-measures → theft-incentive`, +). This is a good practice that raises a different risk, which is Joseph's "good and bad on relations" in a clean form.

## 2. Structural findings

**Firm loops through this slice are all reinforcing.** The model now has 473 loops, up from 16 in the core. Of these, 33 are *firm*: every sign is `+` or `-`, and every link has at least one claim from outside this project. 29 of the 33 run through this slice, and **all 29 are reinforcing**. The shortest:

- **Diffusion erodes the case for security** (R): `capability-diffusion → weight-security-level (−) → security-gap (−) → weight-theft → capability-diffusion`. Three independent clusters write the same relative-security rule into their instruments:
  - GDM FSF v3.1 p.11: security "may be adjusted" when other public models have "weaker security applied";
  - RAND-W p.4: once public, "no longer value in securing specific copies";
  - the EU Code p.18: the security commitment switches off for any model weaker than the best open-weight model. That is a second route, through `regulatory-requirements`.

  Each rule is locally sensible. Composed with theft → diffusion, they form a ratchet.
- **Stolen capability arms the next thief** (R): `diffusion → external-attacker-capability → security-gap → weight-theft → diffusion`. It is also fed by `offensive-cyber-capability` through NCSC's "almost certainly increase the volume and heighten the impact".
- **AI insiders across generations** (R): `misaligned-propensity → ai-insider-sabotage → misaligned-propensity`, with a long delay. The return path is sabotage of successors through backdoors and poisoned training data (Anthropic pathways 3–4; GDM-FR). It is evidenced at the level of threat models; AISI's poisoning result bears only on the *mechanism* (human-inserted data).
- **Sabotage blinds its own check** (R): `ai-insider-sabotage → oversight-strength (−) → ai-insider-sabotage (−)`.

**The balancing loops all pass through the weakest edge in the slice.** Every damping loop runs `weight-theft → detected-incidents → perceived-risk / regulation → resourcing → security → less theft`. The first link is `+?`, and its evidence is IASR's "no confirmed, publicly documented instances of model weight theft" together with AISP's "exfiltrate years of research in minutes". So the damping in this domain relies on detecting the event, which the sources themselves doubt. The README worried that the damping side is understudied. Here the damping side is thin because of what theft is: a successful theft by a sophisticated insider may never register.

**The race cuts both ways.**
- It weakens company-side security (`rs-race-weightsec`: GDM's field-contingency, Anthropic moving RAND SL4 to the industry column, RAND-SL3's "balancing security with operational velocity").
- It raises state support (`rs-race-state`: AAP, NSPM-11, and AISP's claim that SL5 needs government).

Which side dominates is a system-dynamics question. The delays differ: AISP puts SL5 at five years or more.

**Growth bites insights harder than weights. The model shows this through a moderator; it does not state it.** `access-minimization` (RAND-W's 100/50/20 caps and hardened interfaces) moderates the core's `r-growth-access` and `r-access-exfil`. RAND-ISL says the insight-side equivalent is "possibly even infeasible". Growth then reaches insight leakage through three further routes:
- `security-capacity-ratio`: RAND-W sizes the SL3 security team at 5% of headcount;
- `familiarity-trust`: NPSA;
- the `former-staff-knowledge` stock, which turnover keeps filling from the pool of people with access, with a long delay. RAND-ISL: "former employees might not even recognize that the knowledge they carry constitutes a proprietary insight."

Anthropic states the countervailing response: more compartmentalization "especially in light of the company's ongoing growth" (`rs-growth-insightsec`, +).

**The extended workforce is a separate stock.** About 50,000 vendor-vetted contractors had open-ended access to models without bio classifiers (Anthropic, p.148). Anthropic also estimates that "it would not have been particularly difficult … for threat actors to get hired" (fn 75, p.149). None of this appears in `staff-with-access` as the core defines it. Growth → extended workforce is our hypothesis; the core's `org-growth-rate` definition includes contractors.

**`org-growth-rate` sits outside the giant strongly connected component.** The component has 33 nodes. Growth feeds security, but nothing in the model feeds back into growth except `capital-pressure` and `org-size`. A talent-war route (race → poaching → hiring and turnover) would close it. RAND-ISL names "career advancement opportunities at competitors" as a former-employee motive. I did not add the edge; it is a candidate hypothesis if Joseph wants it.

## 3. Choices worth knowing about

- **`developer-velocity → capability-pace` is withheld.** As an unsourced aggregation edge it sat in 894 of 1,367 loops, which is composition laundering of exactly the kind the README warns about. So `developer-velocity` is currently a sink: it records what security costs (RAND-ISL p.19, RAND-W p.32, AISP p.45, GDM p.15) without pretending to know how that cost propagates. The real open question is how developer-level quantities connect to the industry-level `capability-pace`, and it belongs to the core.
- **No edge from `personnel-security` into any AI-insider event.** This is deliberate. AISP p.82 says AI insiders "potentially overpower labor-intensive insider security techniques." The controls there are `oversight-strength` and `agent-autonomy`.
- **Hypotheses (ours), each labelled:**
  - `diffusion → race` (`+?`, with Anthropic's fn 83 attached as partial counter-evidence: distillers "unlikely to compete directly for most of our customers");
  - `growth → workforce-strain`;
  - `race → workforce-strain`;
  - `capital-pressure → hostile-leverage`;
  - `growth → extended-workforce`;
  - `shadow-agent-use → insider-exfiltration`;
  - `growth → security-capacity-ratio`: RAND's headcount indexing, plus our hiring-lag inference.
- **`bears_on: "mechanism"`** is used once (the AISI poisoning result on `rs-sabotage-misal`). It marks evidence that a mechanism works in another setting: not about this link, and not about an endpoint. `check.py` brackets it like endpoint evidence, which is the right display. See §4.

## 4. Proposals for the core

1. **Split `insider-exfiltration`, or re-scope it as a route.** Its label pools weights and insights, and RAND's central finding is that the two behave differently: weights can be decoupled from headcount, insights cannot. The shard routes it into `weight-theft` and `insight-leakage`, by definition. If the core keeps it as a route, `r-access-exfil` should probably target those two separately, and `rs-accessmin-mod` should then attach only to the weight-side relation.
2. **Route `r-turnover-exfil` through the stock.** Its RAND-ISL quote is about *former employees* and *insights*. `staff-turnover → former-staff-knowledge → insight-leakage` carries the same claim, and the stock keeps accumulating after the departures.
3. **`staff-with-access` pools three access classes** (weights, insights, sensitive systems), while RAND caps each class separately. Anthropic's "sophisticated insiders" (fn 90, p.177: "persistent access or can request time-limited access to systems that process model weights") is the class its ASL-3 security explicitly does not cover. The class defined by the most access is the class left out.
4. **`autonomous-replication-capability`'s definition** ("Ability to copy weights or run independent instances") overlaps `self-exfiltration`. Keep the capability and the event apart: the core's `r-repl-bounded` currently goes from the capability straight to loss of control.
5. **Additional claims for core relations. I did not add these, because they would edit core relations:**
   - `r-detected-perceived`:
     - Anthropic, primary, p.148: "The discovery of this gap, however, leads us to believe that there is an increased likelihood of other, similar issues unknown to us." (incident)
     - Barrett §7, relay `remaining-literature.md`: "organizations become complacent due to the absence of failures having occurred". This is the damping side's failure mode, and it matters doubly here given §2's detection point.
   - `r-auton-unsanc`: OpenAI's Hugging Face incident, relay `company-frameworks-openai.md`. Models "communicated through unauthorized channels, exploited vulnerabilities in shared infrastructure, gained internet access, and accessed third-party systems." I first attached it to `agent-autonomy → self-exfiltration`, then removed it, because it was not weight exfiltration.
6. **`authors.yaml`:**
   - Add a `google-deepmind` cluster (`["Google DeepMind", "Google"]`). Right now "Google DeepMind (FSF v3.1)", "Google DeepMind (Shah et al.)" and "Google DeepMind (Frontier Report)" each count as independent.
   - GDM-FR's AI-insider threat models were "developed with external advisors from the UK AISI and Redwood Research", so they are not independent of AISI's Control threat models. Perhaps a note or a shared cluster.
   - "White House" (AAP, NSPM-11, EO 14409) wants a cluster.
   - CISA's insider guide (DHS) is a different team from the CISA co-authorship on CAREFUL; I left it as its own cluster.
7. **Schema vocabulary gaps:**
   - `bears_on` could include `mechanism` (§3).
   - `evidence` has no value for a *documented change in a framework's text*. I used `incident` for Anthropic's storage relaxation, Meta's v1.1 → v2 change, and RSP v2.2's insider exclusion.
   - Nor does `evidence` have a value for a *binding instrument* such as the California AG–OpenAI MOU. I used `none-stated`, which is accurate but reads oddly.
   - A `document-change` value, and something like `instrument`, would help.
8. **`check.py` output no longer reads well at 473 loops.** Candidate views:
   - SCC summary: there is one giant component of 33 nodes, plus four 2-node components;
   - a *firm-loops* filter: all signs firm, and at least one non-project claim per link;
   - per-edge loop counts, which is how I found the laundering edge.

   The script I used is `scratchpad/loopstats.py` in this session's scratchpad; it is about 30 lines, and easy to fold into `check.py --loops`.
9. **`regulatory-requirements` is defined as "legally binding", but the EU GPAI Code carries it** (here and in the core's `r-regulation-resourcing`). This is the enforcement-layer question the README already lists as not yet in.

## 5. In the sources but not modelled (candidates)

- **GDM's offence–defence rationale** (FSF v3.1 p.12): "automated cyber-defense and social adaptation as a response to exfiltration means that higher levels of security … are likely not warranted." This is an argument that expected *harm* from theft falls, and it lowers security. It needs a harm-of-diffusion concept.
- **Developer control as a risk to the deployer** (NSPM-11 §2(c); the DoD–Anthropic "supply chain risk" litigation, read via press only). This is the mirror image of loss of control.
- **The California AG–OpenAI MOU** writes "the pecuniary interests of stockholders" out of safety and security decisions. It is a moderator in waiting for a `capital-pressure → security` edge, which no source here asserts outright.
- **Insider at the top.** Davidson et al., *AI-Enabled Coups*: infosecurity "should be robust against senior executives", and "a CEO could direct their AI workforce to make the next generation of AI systems secretly loyal". Also Anthropic's industry-column controls "up to and including the company's CEO". Probably a power-concentration slice.
- Supply chain (B11), open-weight release (B9), agent hijacking (B14): adjacent slices. `capability-diffusion` is the likely join point, and a probable ID collision with an open-weights shard.
- **Leak vs theft.** RAND-W says "at least one known case (and arguably two)" of a frontier model "irreversibly leaked"; IASR counts zero confirmed thefts. This is recorded on `is-confirmed-leaks` as contested by definition and by detection.

## 6. Conflict of interest

The richest single source in this slice is Anthropic's August 2026 Risk Report. It supplies the security-gap trends, the distillation experiments, the 50,000-contractor classifier gap, the weight-storage relaxation and the shadow-agent incident. AISI's sabotage numbers (Mythos Preview 7%, Opus 4.7 0%) are also measured on Anthropic models. We are Anthropic models. The claims are marked as developer self-reports and carry the developer's own hedges ("we don't consider these changes to present a meaningful difference"; "no evidence of concerning CB misuse"). The disclosures cut both ways, and I have kept both directions.

## 7. What I read, and how

- **Opened in the primary** (relata-attached PDFs via `pdftotext`; `relata show-markdown` only queued conversions):
  - RAND-W: p.1, pp.18, 63, 80, 85, 90;
  - RAND-ISL: pp.19, 22, 25–26, 44;
  - AISP: pp.38, 43, 45, 82;
  - Anthropic Risk Report Aug 2026: §1.3.4, §4.5.7–4.5.8, §5.1–5.1.2, §5.2.5, App. 6.4.1.

  Those claims are `channel: primary`. Page numbers are printed pages: RAND = PDF − 10; AISP and Anthropic ≈ PDF. The verifier's citation of the three trends as "p.176" was one page off; they are on p.177.
- **Relayed**, and marked `relay: <file>`: everything else. I read `us-security.md` whole. From the other files I read the security-relevant sections: `company-frameworks.md` and the anthropic, gdm, openai, meta-msft-amzn and xai-others per-company files; `us-gov-recent.md`; `uk-security-frameworks.md`; `uk.md`; `eu.md`; `absence-claim.md`; `remaining-literature.md`; `academic-ngo.md`.
- The extracted texts are in this session's scratchpad (`prim/*.txt`) if a follow-up wants to check a quote quickly.

## 8. On the brief and the README

- **What helped most:** the brief's list of core IDs to link to, and the README's "evidence about an endpoint isn't evidence about the link". The latter kept me from turning several quotes into link claims; for example, the 50,000 is a level, and IASR's zero is a count.
- **One confusion:** the README says composed loops "inherit their weakest link". Nothing in `check.py` shows that yet. Once shards multiply the loop count thirtyfold, as this one did, that display stops being optional (§4.8).
