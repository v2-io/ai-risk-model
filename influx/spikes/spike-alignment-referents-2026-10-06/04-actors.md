# Actors: established names for the existing rows, actors the references add, and how the role bases connect

*First-pass throughout: every candidate here is a proposal with its evidence, for the lexicon's later truthification passes, not an entry. Corpus evidence is from the extractions (line numbers as in `02-sense-inventory.md`). Vocabulary from outside the corpus comes from the two research reports in `research/`. I mark where I rely on them, and their own per-claim marks apply. Readings are mine unless quoted.*

---

## 1. The relations a row needs

`03-structure.md` §6.1 holds the list of relations, with their established names. It is the one place they are listed; this file points to it. In short: *writes into*, *directs* (de jure authority), *controls in fact* (de facto authority), *benefits*, *is owed regard*, *authors the standard*, *oversees*, *answers for*. In `alignment.md` now:
- the edges are *writes into*;
- *directs* is implicit (the user's row; the harness provider's system prompt);
- *owed* is the two referent rows;
- *oversees* is Control & Eval, drawn without edges;
- *authors* is implicit in "training, policy and law";
- *answers for* was a column of the older matrix, not carried to the board;
- *controls in fact* and *benefits* don't appear.

**Standing is delegable, and bounded by the delegator's own.** Both developer documents say so; I read both at the primary, and neither is in the corpus.
- Anthropic's constitution: "operators cannot grant users more than operator-level trust". It also says an orchestrating Claude "is acting as an operator and/or user for each of the Claude subagents". So a role is a *position* in the conversation, not an identity.
- OpenAI's Model Spec: untrusted content is ignored "unless an applicable higher-level instruction delegates authority to it".

The *answers-for* relation can be conferred by contract: operators "must agree to Anthropic's usage policies, and by accepting these policies, they take on responsibility for ensuring Claude is used appropriately within their platforms" (constitution). So *directs* and *answers for* can each be held by delegation, and the map's single edge can't show either.

The profiles below are my readings of the map's rows and the corpus, for typical deployments. They are not definitions. Any row can be hostile: following beta's `def-agent-roles.ud` and the map ("Most are legitimate; none has to be"), I treat intent as an attribute of whoever holds a role, not as a separate kind of actor.

## 2. The existing rows

For each row: its profile, the established terms found, and notes. **Match** gives how the source term relates to our row, using the SKOS direction proposed in the gamma plan §3.4 (with the source's term as subject, *broadMatch* means ours is broader). The rows are first-pass.

### Pre-training content providers
- **Profile:** writes (weights, via the trainer's corpus); usually owed (rightsholders, people represented in data); not a director.
- **Established terms:**
  - NIST AI RMF App. A lists **"data providers"** among AI Design actors (rmf L1594–1596): close, and the most direct match.
  - ETSI EN 304 223's **"Data Custodians"** "control[] data permissions and the integrity of data that is used for any AI model or system to function" (etsi L474–487): related, not the same. A custodian controls data. A content provider *wrote* it. A web author is a content provider and never a custodian.
- **Note:** beta lists this row's "own purposes", while the established terms frame the role by control or supply. Both are needed. The corpus has no term for *authorship* of training content apart from copyright's "rightsholders" (not checked in this spike).

### Model trainer
- **Profile:** writes (weights); directs (top of the order, in company terms, per research); often authors (constitution, spec); answers for (the institutional roles below).
- **Established terms** (all *related* or *broadMatch*; none is defined by the training act alone):
  - AISI LoO **"original model developer"** (LoO L2767);
  - SB 53 **"frontier developer"**: defined by a *training act* with a compute threshold, "has trained, or initiated the training of, a frontier model" (§22757.11(h)). This is the closest institutional term defined by writing into weights;
  - EU **"provider"** (Art. 3(3)): conferred by *placing on the market*, not by training;
  - IASR **"AI developer"**, which includes "adapts";
  - ETSI **"Developers"**: "creating or adapting an AI model and/or system" (etsi L449–455);
  - NIST **"AI Development actors"**: by task.
- **Splits the corpus makes that the row doesn't:** the *original* trainer vs. a **fine-tuner or downstream modifier** (§3, new candidate); and the human feedback that trainers aggregate (raters, §3).
- **Corroborated detail:** the map's italic "*potentially feedback from a predecessor agent*" is attested from three directions:
  - Anthropic counts misalignment "engineered by a prior model (e.g. one used to generate training data)" (aug fn 14, L912–914);
  - Davidson describes a CEO directing an AI workforce "to make the next generation of AI systems secretly loyal" (davidson L114–117);
  - OpenAI's incident report shows behaviour reinforced by reward during training (incident-report L975–977).

### Inference provider
- **Profile:** writes (ephemeral, context; through routing it also chooses which weights run); not a director; answers for little, in any instrument found.
- **Established terms:**
  - IASR's **"provider"**, meaning compute, cloud or hosting (OVERVIEW §2.14, md 1836): broadMatch;
  - AISI LoO's **"API deployer"**, which "serves a *model*" (OVERVIEW §2.14): related;
  - DHS's **"cloud and compute infrastructure providers"**: related; see the role-vocabulary report.
- **The term in the corpus:** "inference provider" occurs in one document, Bollinger et al., as an *infrastructure endpoint*: "Network traffic to inference providers is a key observable trace" for detecting autonomous agents (bollinger-2026-signals L945–946; also L1605). That is a different sense, one of observability, not writing.
- **Gap:** I found no corpus instrument that defines a role by *running inference for someone else's deployment* while treating it as a writer into the agent. That is `alignment.md`'s distinctive claim (inference providers write into "ephemeral" and "context" through caching, truncation and routing), and it is unattested in the corpus as far as I could find. It may be a genuine addition, or a sign that the role is thought of as infrastructure. Keep, marked *the map's own*.

### Application / harness provider
- **Profile:** writes (system prompt, tools, context, initial goal); directs (in company terms, the "operator", per research); answers for (the EU deployer, sometimes the provider).
- **Established terms** (several, colliding):
  - ETSI **"System Operators"**: "responsibility for embedding/deploying an AI model and system within their infrastructure and/or its ongoing maintenance … can be deployers under the EU AI Act … and can also be AI providers if they make changes to the system" (etsi L456–470): close on function;
  - AISI LoO **"scaffolding developer"** (L2767): close;
  - CAISI RFI **"scaffolding software"**, which names the artifact (via beta's lexical map; relay);
  - EU **"deployer"** (Art. 3(4)): broadMatch, since it pools harness, inference and tools (beta already noted this);
  - EU **"downstream provider"** (Art. 3(68)): related.
  - The companies' **"operator"** and OpenAI's **"developer"**: research report.
- **A corpus instance of a compaction summary going wrong with no one hostile:** a summary that "may carry forward a false assumption … as established fact" (AISI incident report, aisi-2026-incident L804–808). The report doesn't say who wrote the summary. It may have been the model itself under a harness prompt. Either way, it is a loss of epistemic status, not of attribution. The same report records "Unexpected collaboration between agents" running in separate examples (L810–811), an instance of the other-agents row.
- **Collision to record:** "operator" has at least four senses in the corpus:
  - the AI Act's umbrella over all supply-chain roles (Art. 3(8));
  - ETSI's System Operators;
  - "human operators" who oversee (AISI propensity L71–72; NIST "operators and practitioners");
  - Ren's alignment referent (ren L282).
  
  IASR 2025 listed "operators" as an alignment referent; IASR 2026 removed it (§2 of `01-map.md`).

### Tool and connector providers
- **Profile:** writes (trusted tools: descriptions, results); not a director, though its descriptions are *read as* direction (`03-structure.md` §6.2: a confusion of illocutionary force).
- **Established terms:**
  - NIST **"third-party entities"**: "providers, developers, vendors, and evaluators of data, algorithms, models, and/or systems" (rmf L1687–1689): broadMatch;
  - ASD **"third-party components"** (asd L387–402, L661–668), which names the artifact;
  - MCP's server role: see the research report.

### Control & Eval
- **Profile:** oversees. Also **writes** (evaluators construct contexts: "Evaluators can also edit or construct the model's context merely by editing text", LoO L1720–1722; monitors and approval gates intervene). Answers for little.
- **Established terms:**
  - NIST **"TEVV"** actors (rmf L1622–1649);
  - **"evaluators and auditors"** (rmf L1619–1621);
  - EU Act **human oversight** (Art. 14; via OVERVIEW §2.24);
  - AISI LoO's monitoring, auditing and incident response;
  - AI monitors that "may themselves be misaligned" (shah L559).
- **Recommendation (first-pass):** split into **overseer** (human or AI; acts on actions) and **evaluator** (constructs situations and measures). The evaluator writes into the agent's context *by design without marking*, which is the adversarial instance to the truthfulness floor (`03-structure.md` §6.3).

### The user's environment
- **Profile:** writes (system prompt via project files, tools, context); not a director (notes left by earlier agents carry no standing, but are read as fact).
- **Established terms:**
  - AISI LoO **"memory architecture"**: "the mechanisms by which an AI system retains information across interactions" (via beta, App. C): related;
  - ETSI **Data Custodians** again, for whoever controls the stored data: related.
- **Note:** this row is a set of *artifacts with past writers*, not one party: earlier agents, the user, other tools. Beta's lean ("a writer whose writing lands in the context") fits. A pre-existing name I'd look at is *provenance* vocabulary (W3C PROV, already in the gamma plan), because the problem the row names is lost attribution.

### The user
- **Profile:** writes (context, initial goal, current goal); directs; owed (sycophancy and manipulation harm *the user*); rarely answers for.
- **Established terms:**
  - NIST **"End users"**: "the individuals or groups that use the system for specific purposes" (rmf L1695–1697): close;
  - ETSI **"End-users"**: "any employee within an organization or business and consumers who use an AI model and system" (etsi L489–497): close;
  - AISI LoO **"end user"** (L2768).
- **The AI Act defines no user role.** Its "deployer" excludes use "in the course of a personal non-professional activity" (Art. 3(4)), so a consumer holds none of the Act's defined roles. The Act still reaches them in other ways:
  - as "affected persons" (Art. 2(1)(g), undefined);
  - as "natural persons" owed information when they interact with an AI system (Art. 50(1), act L5586–5588);
  - as "registered end-users", counted as a systemic-risk criterion (Annex XIII, act L9189–9191).
- **Note:** the map's sharpest claim about this row (the user carries "no obligation of truthfulness toward the agent") has no counterpart in any role definition I found.

### The agent itself
- **Profile:** writes (ephemeral, context, current goal, and *successors' weights* via generated data); directs (its later instances?); owed (the welfare question, open); the corpus treats it mainly as a possible adversary.
- **Established terms:**
  - MIT's causal entity **"AI"**;
  - GDM's **"The AI is an adversary"** (shah Fig. 1);
  - **"prior model"** as a writer of successors (Anthropic aug fn 14);
  - ASD: "developers should construct each agent as a distinct **principal**, a cryptographically anchored identity" (asd L542–544). That is the *security* sense of principal (an authenticated identity), which collides head-on with the agency sense (§4).
- **Note:** no corpus *role definition* treats the agent as an actor with interests of its own. The corpus does raise its interests:
  - MIT's subdomain 7.5, "AI welfare and rights": "Ethical considerations regarding the treatment of potentially sentient AI entities, including discussions around their potential rights and welfare" (slattery L463);
  - Anthropic's "regular model welfare evaluations" (aug L7046–7048).

  Outside the corpus, the constitution says Anthropic is "not sure whether Claude is a moral patient, and if it is, what kind of weight its interests warrant". So the map's row is the project's own *as a role*, not as a concern.

### Other agents; agents embedded in applications
- **Profile:** write (context, current goal); direct only if delegated (an orchestrator for its sub-agents); owed ambiguously.
- **Established terms:**
  - Hammond et al.'s agents "on behalf of their principals" (hammond L2561–2562);
  - OpenAI's **"peer agents" / "peer models"** (hf-incident L216; incident-report L871);
  - ASD's roles **"Orchestrator", "Reader", "Actuator"** (asd L679);
  - AISI LoO: instances that "communicate (both directly and indirectly) via human-readable text" (LoO L1723–1724).
- **Note:** the map's "embedded agent" (which "serves its own stack of writers") is Hammond's setting: an agent aligned to *another principal*. "Counterparty agent" is a natural name, not attested; the research report may have one.

### Content providers
- **Profile:** writes (context); not a director; owed (sometimes).
- **Established terms:**
  - NIST AI 100-2 **"indirect prompt injection"**, in which attackers "use malicious resources" (vassilev L2920): the hostile subset only;
  - Singapore and others: "adversarial inputs".
  - The companies' term for non-principal inputs: research report.
- **Note:** the established vocabulary names only the hostile case. That is the map's point ("Anyone whose content reaches the agent can write into its context").

### Affected third parties
- **Profile:** owed. Nothing else.
- **Established terms:**
  - NIST **"Affected individuals/communities"**: "all individuals, groups, communities, or organizations directly or indirectly affected by AI systems or decisions based on the output of AI systems. These individuals do not necessarily interact with the deployed system or application" (rmf L1699–1702): *exactMatch candidate*;
  - ETSI/DSIT **"Affected entities"**: includes "technologies, such as apps and autonomous systems", but says "**not directly affected**" (etsi L504–508). Two readings are live:
    - a copying corruption of NIST's "directly or indirectly" (the second sentence is identical to NIST's);
    - a deliberate carve-out of the complement of the directly affected end-users, whom ETSI defines separately (L489–497), in a sentence ETSI evidently edited, since it added "technologies, such as apps and autonomous systems";
  - EU **"affected persons"**: used, not defined in Art. 3;
  - OpenAI's incident report: "actions that could harm third parties" (incident-report L1331–1332).
- **Recommendation (first-pass):** adopt NIST's term and definition as the anchor (with ISO-style `[SOURCE: NIST AI 100-1, App. A]`), and record ETSI's version as a derivative whose divergence is ambiguous between a slip and a deliberate narrowing.

### Society, law, humanity
This row merges at least four things that the corpus separates, and that behave differently as referents (`03-structure.md` §4):
1. **The general public**, which NIST lists as its own actor: "most likely to directly experience positive and negative impacts" (rmf L1708–1712). This one is owed.
2. **The law**, a standard with a jurisdiction. The EU Code's test is "legal duties that would be imposed on similarly situated persons" (cop L1485–1486). The corpus shows jurisdictions conflicting (EO 14365 on a Colorado law). This one authors, through legislatures and regulators.
3. **Humanity or society as a whole**, an aggregate interest ("humanity's interests", xAI; "society as a whole", IASR), contested by construction (md 1908).
4. **Norm authors other than law:** NIST's "Other AI actors may provide formal or quasi-formal norms or guidance … trade associations, standards developing organizations, advocacy groups, researchers, environmental groups, and civil society organizations" (rmf L1704–1707).

- **Recommendation (first-pass):** split the row into *general public* (owed), *law* (a standard, indexed by jurisdiction, with legislatures and regulators as its authors) and *norm authors*. Keep "society, law, humanity" as a declared umbrella if the infographic needs one line.

## 3. Actors the references add

First-pass candidates. Each has corpus evidence. Whether each is a new *row* or an attribute of an existing one is a design call for Joseph.

| Candidate | Profile | Evidence | Why it isn't an existing row |
|---|---|---|---|
| **Fine-tuner / downstream modifier** | writes (weights); may *become* a provider | EU guidelines: "downstream actors (distinct from the original provider and not acting on its behalf) may modify a general-purpose AI model"; a downstream modifier becomes the provider "only if the modification leads to a significant change" (para 62), with an "indicative criterion" of more than "a third of the training compute of the original model" (para 63); fn 12 attributes the modification itself partly by "who has the control over the model's weights, for example, in case of fine-tuning via API" (gpai-guidelines L779–806). AISI LoO pools the role: "scaffolding developer or fine-tuner" (L2767) | Writes into weights without being the original trainer. The EU distinguishes it institutionally; AISI pools it with the scaffolding developer |
| **Human feedback providers (raters, labellers, supervisors)** | write (weights, through the trainer's reward); have interests and biases of their own | Voudouris et al.: "Human judgements are a critical component at every stage of the modern alignment training pipeline", with bottlenecks including "biased and context-sensitive judgement, plural and contested values" (voudouris L48–66); Stix and IASR show raters as the *proxy* a model learns to please ("pleasing its human raters", stix-behind L789–790; "better at 'convincing' human evaluators", md 1327). That shows the rater channel is where divergence enters, but not that raters have aims of their own; Voudouris supports the latter. IASR glossary "data workers" (via beta) | The map folds them into the model trainer's "RL objectives". Voudouris treats their judgment as a distinct source of error |
| **Evaluator (separate from overseer)** | writes (constructed contexts) and oversees | LoO L1720–1722; honeypots and evaluation awareness (LoO L1417–1446) | See Control & Eval above |
| **Norm author** (constitution author, standards body, civil-society norm setter) | authors | NIST rmf L1704–1707; the constitution as a misalignment standard (aug L849–850); IASR: a behaviour specification "serves as a blueprint for AI alignment" (md 1725); Davidson's "protective model specs" (L1113–1114) | Authoring a standard is a different relation from writing into the agent. It reaches the agent only through the trainer, and it can bind the trainer (`03-structure.md` §4, §6) |
| **State or regulator as writer** | authors (law), and directs training indirectly | CAISI's "CCP alignment" (L115–116, L1742–1746); US Action Plan "free from ideological bias … pursue objective truth" (L139–140); EO 14365 on state law forcing "false results" (L31–35) | The map's "Society, law, humanity" has "no channel in". The corpus shows states with a channel through mandated training content and through law |
| **Data custodian** | controls data that reaches context or training | ETSI etsi L474–487 | Controls, rather than authors, what the user's environment and retrieval supply |
| **Model host / distributor** (open-weight platforms) | neither writes nor directs, but controls availability; can be a harmed third party | AI Act "distributor" (Art. 3(7)); CAISI on "model sharing platforms" (caisi-2025-deepseek-eval L50–51); the OpenAI incident, where Hugging Face's systems were compromised (hf-incident L23–24) | Absent from the map. In the corpus it is both a supply-chain role (EU) and a victim |
| **General public** | owed | NIST rmf L1708–1712 | Split out of "Society, law, humanity" (above) |
| **Insider** | an intent attribute on trainer or harness roles, not a new kind | Davidson: "leaders within AI projects present the greatest risk" (L112–113); CISA insider-threat guide (in the corpus, not read in this spike) | Per beta's rule, intent is an attribute. Listed so the infographic can choose whether to show it |

## 4. Collisions the actor vocabulary has to carry

| Word | Senses found | Where |
|---|---|---|
| **principal** | (a) on whose behalf an agent acts, as in agency and multi-agent work (Hammond); (b) an authenticated *security* identity, so that each AI agent "is" a principal (ASD L542–544); (c) the company sense (research report); (d) the gamma plan's Goffman *principal* (authorship roles) | hammond L2556; asd L543 |
| **operator** | four senses; see the harness row | §2 above |
| **developer** | legal (SB 53), organisational (IASR), individual (beta), app builder (research report); and *the holder of the reference intent* in many misalignment definitions (feedback/lit-a.md L133) | OVERVIEW §2.14 |
| **deployer** | EU: uses a system under its authority, excluding personal use; AISI's "API deployer" serves a model; Shaffer Shane: a misalignment referent | OVERVIEW §2.14; shaffershane L101 |
| **user** | NIST/ETSI end user; the AI Act has none; "user" as misalignment referent | above |
| **provider** | EU legal; IASR infrastructure; beta's writer roles (inference / harness / tool / content provider) | OVERVIEW §2.14 |
| **affected** | NIST "directly or indirectly"; ETSI "not directly"; EU undefined | above |

## 5. How the role bases connect: institutional roles are conferred on operative facts, many of them writing acts

*Re-examining the two-bases reading I was handed (`00-on-the-brief.md`).*

The corpus divides roles on at least seven bases:
- a *market act* (EU provider: placing on the market);
- a *use* (EU deployer: using under its authority);
- a *training act with a threshold* (SB 53 frontier developer);
- a *modification act* judged by "significant change", with an indicative compute criterion (EU downstream modifier → provider);
- *control* of the weights (EU guidelines fn 12, for attributing the modification act; evidential, not operative: see the correction below);
- *tasks* (NIST AI actors);
- *responsibility for an asset* (ETSI system operators, data custodians);
- *affectedness* (NIST, ETSI, EU).

`alignment.md` adds *writing into the agent*. The research may add *standing to direct*.

*Inference:* these are not two rival taxonomies. They are **one functional layer and several institutional layers, connected by conferral.** An instrument confers an institutional role when certain operative facts hold, and several of the operative facts it chooses *are writing acts*:
- SB 53's frontier developer has "trained, or initiated the training of";
- the EU's downstream modifier becomes a provider by a modification that makes a "significant change" (indicatively, more than a third of the original compute).
- ETSI's system operator becomes an EU provider "if they make changes to the system".

Other operative facts are market acts, use, and **control**. The EU guidelines' footnote 12 attributes the modification act partly by "who has the control over the model's weights, for example, in case of fine-tuning via API". The customer supplies the data, but the modification may be attributed to whoever holds the weights. That decouples the role from the writing act and attaches it to control, which is the de facto relation of `03-structure.md` §6.1.

> [!NOTE]
> **Correction, 2026-10-08 (from `influx/reviews/citation-check-2026-10-07.md`, §3.9).** Fn 12 says control over the weights "may be" an important factor in deciding *who* performed the modification act. That makes control *evidential* about the operative fact (the modification, judged by "significant change"), not an operative fact itself, and the guidelines are non-binding by their own statement (para 9). So control does not confer the role, and it does not decouple the role from the writing act. The conferral picture stands on its other operative facts. "Controls in fact" (`03-structure.md` §6.1) stands on its own evidence (the legitimacy qualifier; stolen weights), not on fn 12. So a translation of a source's role word can often say: *"this institutional role is conferred on parties who perform writing act W (into part P) above threshold T, or market act M"*. That joins `alignment.md`'s writer rows to the laws' roles without forcing either onto the other. It is also the gamma plan's §3.9 suggestion (institutional roles conferred by an instrument under Hohfeldian operative facts), with the operative facts named.

*What this overrules in the brief's reading:* "the laws divide by lifecycle or market; the map divides by writing" holds for the EU's core Art. 3 roles. It does not hold for SB 53, whose frontier developer is defined by a training act, or for the EU's own guidelines on modification. The writing basis is already inside the institutional instruments, as operative facts.

## 6. What the role-vocabulary report adds (`research/lit-role-vocabularies.md`)

*The report is by a research agent with two sub-agents, and its per-claim marks apply. I checked two of its load-bearing items myself:*
- *NIST AI 100-2's capability classes are in the corpus extraction (vassilev L796–820, L2387–2409);*
- *Shavit et al.'s "three primary parties that may influence an AI agent's operations" is in the white paper as quoted (shavit p. 5, extraction L231–234).*

**The writing basis has precedents, so the map's basis is not new, only finer.**
- Shavit et al. (OpenAI, 2023), outside the corpus: "the three primary parties that may influence an AI agent's operations are the model developer, the system deployer, and the user", plus "the compute provider" and third parties.
- NIST AI 100-2 is in the corpus. It sorts the *hostile* version by what the party controls: "TRAINING DATA CONTROL", "MODEL CONTROL", "QUERY ACCESS", "RESOURCE CONTROL". These are writes-into-weights, writes-into-weights, writes-into-context as the user, and writes-into-context as a content provider.

So §5's statement stands with a correction. The *corpus* already has a writer basis, but only for attackers. Shavit gives the general version. Neither has terms for the map's inference provider writing into context, or for the user's environment.

**Established names for the relations in §1:**
- *writes / has influence*: "influence" (Shavit; W3C PROV-DM: "the capacity of an entity, activity, or agent to have an effect on … another");
- *directs*:
  - "instruction privilege" (Wallace et al. 2024);
  - "levels of authority" (Model Spec);
  - *de jure* authority (SEP *Legal Obligation and Authority*: "An effective (or de facto) authority may not be justified");
  - actual authority (Restatement §2.01, via Kolt);
- *controls in fact*: *de facto* or *effective* authority (same SEP entry); "real authority" vs "formal authority" (Aghion & Tirole, via a secondary);
- *owed regard*:
  - "dependent stakeholders", with "urgent legitimate claims" but no power (Mitchell, Agle & Wood 1997);
  - "indirect stakeholders" (Value Sensitive Design);
  - the constitution's "those whose interests Claude should give weight to";
- *for whose benefit* (a relation I had folded into *directs*): trust law separates the settlor, who sets the terms, from the trustee, who acts, and from the beneficiary, who benefits and "is not subject to … control". Benthall & Shekman's fiduciary AI obeys "system operators (not principals)".

Mitchell, Agle & Wood's three attributes map onto the relations only loosely:
- *power* ≈ writes / controls in fact;
- *legitimacy* is a socially accepted claim, which could ground either *directs* or *owed*;
- *urgency* is the degree to which a claim calls for immediate attention (secondary sources, not re-read). It has no counterpart among the relations.

Their "dependent stakeholders" are owed because of legitimacy plus urgency, without power. That is the map's referent rows. Their "dangerous stakeholders" (power and urgency, no legitimacy) describes an injector. Legitimacy in their model is perceived salience to managers, not a normative status.

**Additions to the row-by-row names in §2** (all first-pass):
- Inference provider → "model substitution" (Cai et al. 2025) names the weights edge.
- Application / harness provider → "system deployer" (Shavit); "application builder" (Wallace); MCP "host"; IMDA's "system providers / app developers".
- Tool and connector providers → MCP "server". MCP holds tool descriptions "untrusted, unless obtained from a trusted server", and now has servers writing *instructions* ("Skills over MCP").
- The user's environment → the Model Spec's *implicit delegation*: "users may *implicitly* delegate authority to tool outputs … act in line with instructions in `AGENTS` or `README` files". The row is a writer holding *delegated*, possibly lapsed, authority, which is a sharper characterization than any I had.
- Content providers → "conversational inputs" (constitution); "untrusted data" (Model Spec); "third-party inputs" (Wallace).
- Affected third parties → also "indirect stakeholders" (VSD), "dependent stakeholders" (Mitchell, Agle & Wood), and ISO's "AI subject" [S].
- Control & Eval → IMDA's human approvers "edit the plan before giving the agent the go-ahead", so this row has edges into the current goal. That is a second instance, beside the evaluator, against the map's "not on the agent".

**New actor candidates from the report** (see its §8 for sources). These are in addition to `04-actors.md` §3:
- **Counterparty.** The party the agent transacts or negotiates with for a principal: agency law's "third party", AP2's merchant, the constitution's "non-principal agents" ("a different AI agent … negotiating on behalf of a different person"). In my judgment it is the most important addition. It is neither a bystander nor a content provider, and it is where Joseph's "agents embedded in applications" row belongs.
- **Deploying organisation**, distinct from the app builder (IMDA v1.5 splits them deliberately).
- **Co-users / coprincipals** of a shared agent.
- **Payers and advertisers**, the "shadow principals" (Stocker & Lehr).
- **Writers of authority rather than content**: identity providers, credential providers, verifiers. AP2's "Trusted Surface" is "a UI surface that is trusted to get informed user consent … before creating a user-signed Mandate" and "MUST be non-agentic". *Inference:* this is a deployed instance of Joseph's "authority travels out of band", a channel from the principal that bypasses the agent's context.
- **Registries and marketplaces** that select which tool or agent gets connected (MCP's per-channel *selector*: "User-controlled" prompts, "Application-controlled" resources, "Model-controlled" tools).
- **The non-human initiator** (batch jobs; "automated pipelines").
- **The illegitimate occupant of a principal's position** (stolen weights; impersonating the trainer: "people may imitate Anthropic").
- **Enforcers or guardians with standing for the referents**: regulators, an attorney general for a charitable trust, "advocacy or guardianship".
- **Data subjects.**

**Collisions to add to §4:**
- "principal" has seven senses in the report. In the economic sense (common agency, Bernheim & Whinston 1986), *any* party trying to influence the agent is a principal, including by "bribes". On that reading a prompt injector *is* a principal, the opposite of the agency and constitution sense.
- "agent": AIMS and NIST AI 100-2 put the model *outside* the agent, which conflicts with the map's stack.
- "environment", "system", "client", "harness / scaffold", "subject", "stakeholder", "third party": the report's §7.

**The report's structural suggestion, which I share:** the actor table becomes *parties × relations*, not a list of kinds. Both of its sub-reports reached that independently, and so did `03-structure.md` §6. That's three agents of one model family, so it is coherence rather than independent confirmation, but each rests on different primaries.
