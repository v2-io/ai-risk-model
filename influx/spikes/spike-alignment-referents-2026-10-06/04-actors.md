# Actors: established names for the existing rows, actors the references add, and how the role bases connect

*First-pass throughout: every candidate here is a proposal with its evidence, for the lexicon's later truthification passes, not an entry. Corpus evidence is from the extractions (line numbers as in `02-sense-inventory.md`). Vocabulary from outside the corpus comes from the two research reports in `research/`. I mark where I rely on them, and their own per-claim marks apply. Readings are mine unless quoted.*

---

## 1. The relations a row needs

`03-structure.md` §6 argues that "to whom" is several relations. Applied to actors, each row of `alignment.md` has a *profile* across them:

| Relation | Short name | In `alignment.md` now |
|---|---|---|
| writes into a part, through a channel | **writes** | the edges |
| has standing to direct the agent | **directs** | implicit (the user's row; the harness provider's system prompt) |
| is owed regard by the agent | **owed** | the two referent rows |
| authors a standard the agent is held to | **authors** | implicit in "training, policy and law" |
| oversees, gates or evaluates | **oversees** | Control & Eval, drawn without edges |
| absorbs accountability for the agent's acts | **answers for** | a column of the older matrix, not carried to the board |

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
  - Anthropic counts misalignment "engineered by a prior model (e.g. one used to generate training data)" (aug fn 14, L913–916);
  - Davidson describes a CEO directing an AI workforce "to make the next generation of AI systems secretly loyal" (davidson L114–117);
  - OpenAI's incident report shows behaviour reinforced by reward during training (incident-report L975–977).

### Inference provider
- **Profile:** writes (ephemeral, context; through routing it also chooses which weights run); not a director; answers for little, in any instrument found.
- **Established terms:**
  - IASR's **"provider"**, meaning compute, cloud or hosting (OVERVIEW §2.14, md 1836): broadMatch;
  - AISI LoO's **"API deployer"**, which "serves a *model*" (OVERVIEW §2.14): related;
  - DHS's **"cloud and compute infrastructure providers"**: related; see the role-vocabulary report.
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
- **Collision to record:** "operator" has at least four senses in the corpus:
  - the AI Act's umbrella over all supply-chain roles (Art. 3(8));
  - ETSI's System Operators;
  - "human operators" who oversee (AISI propensity L71–72; NIST "operators and practitioners");
  - Ren's alignment referent (ren L282).
  
  IASR 2025 listed "operators" as an alignment referent; IASR 2026 removed it (§2 of `01-map.md`).

### Tool and connector providers
- **Profile:** writes (trusted tools: descriptions, results); not a director, though its descriptions are *read as* direction (§2.2 of `03-structure.md`: the standing mismatch).
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
- **The AI Act has no user role.** Its "deployer" excludes use "in the course of a personal non-professional activity" (Art. 3(4)), so a consumer is in none of the Act's roles. At most they are an "affected person" (Art. 2(1)(g)), a term the Act uses without defining.
- **Note:** the map's sharpest claim about this row (the user carries "no obligation of truthfulness toward the agent") has no counterpart in any role definition I found.

### The agent itself
- **Profile:** writes (ephemeral, context, current goal, and *successors' weights* via generated data); directs (its later instances?); owed (the welfare question, open); the corpus treats it mainly as a possible adversary.
- **Established terms:**
  - MIT's causal entity **"AI"**;
  - GDM's **"The AI is an adversary"** (shah Fig. 1);
  - **"prior model"** as a writer of successors (Anthropic aug fn 14);
  - ASD: "developers should construct each agent as a distinct **principal**, a cryptographically anchored identity" (asd L542–544). That is the *security* sense of principal (an authenticated identity), which collides head-on with the agency sense (§4).
- **Note:** no corpus document defines the agent as an actor with interests of its own. The map's row is the project's own.

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
  - ETSI/DSIT **"Affected entities"**: includes "technologies, such as apps and autonomous systems", but says "**not directly affected**" (etsi L504–508), probably a corruption of NIST's wording (`01-map.md` §2.12);
  - EU **"affected persons"**: used, not defined in Art. 3;
  - OpenAI's incident report: "actions that could harm third parties" (incident-report L1331–1332).
- **Recommendation (first-pass):** adopt NIST's term and definition as the anchor (with ISO-style `[SOURCE: NIST AI 100-1, App. A]`), and record ETSI's version as a drifted derivative.

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
| **Fine-tuner / downstream modifier** | writes (weights); may *become* a provider | EU guidelines: "downstream actors (distinct from the original provider and not acting on its behalf) may modify a general-purpose AI model"; a downstream modifier becomes provider if modification compute exceeds "a third of the training compute of the original model"; fn 12: "who has the control over the model's weights" (gpai-guidelines L779–806); AISI LoO "fine-tuner" (L2767) | Writes into weights without being the original trainer. In the corpus it is distinguished both institutionally (EU) and operationally (AISI) |
| **Human feedback providers (raters, labellers, supervisors)** | write (weights, through the trainer's reward); have interests and biases of their own | Voudouris et al.: "Human judgements are a critical component at every stage of the modern alignment training pipeline", with bottlenecks including "biased and context-sensitive judgement, plural and contested values" (voudouris L48–66); Stix: learning "for the wrong reasons, such as pleasing its human raters" (stix-behind L789–790); IASR: feedback made systems "better at 'convincing' human evaluators" (md 1327); IASR glossary "data workers" (via beta) | The map folds them into the model trainer's "RL objectives". The corpus treats them as a distinct source of divergence, with their own judgment, not the trainer's intent |
| **Evaluator (separate from overseer)** | writes (constructed contexts) and oversees | LoO L1720–1722; honeypots and evaluation awareness (LoO L1417–1446) | See Control & Eval above |
| **Norm author** (constitution author, standards body, civil-society norm setter) | authors | NIST rmf L1704–1707; the constitution as a misalignment standard (aug L849–850); IASR: a behaviour specification "serves as a blueprint for AI alignment" (md 1725); Davidson's "protective model specs" (L1113–1114) | Authoring a standard is a different relation from writing into the agent. It reaches the agent only through the trainer, and it can bind the trainer (`03-structure.md` §4, §6) |
| **State or regulator as writer** | authors (law), and directs training indirectly | CAISI's "CCP alignment" (L115–116, L1742–1746); US Action Plan "free from ideological bias … pursue objective truth" (L139–140); EO 14365 on state law forcing "false results" (L31–35) | The map's "Society, law, humanity" has "no channel in". The corpus shows states with a channel through mandated training content and through law |
| **Data custodian** | controls data that reaches context or training | ETSI etsi L474–487 | Controls, rather than authors, what the user's environment and retrieval supply |
| **Model host / distributor** (open-weight platforms) | neither writes nor directs, but controls availability; can be a harmed third party | AI Act "distributor" (Art. 3(7)); CAISI on "model sharing platforms" (deepseek L49–50); the OpenAI incident, where Hugging Face's systems were compromised (hf-incident L23–24) | Absent from the map. In the corpus it is both a supply-chain role (EU) and a victim |
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
- a *modification act with a threshold* (EU downstream modifier → provider, at > ⅓ of original compute);
- *tasks* (NIST AI actors);
- *responsibility for an asset* (ETSI system operators, data custodians);
- *affectedness* (NIST, ETSI, EU).

`alignment.md` adds *writing into the agent*. The research may add *standing to direct*.

*Inference:* these are not two rival taxonomies. They are **one functional layer and several institutional layers, connected by conferral.** An instrument confers an institutional role when certain operative facts hold, and several of the operative facts it chooses *are writing acts*:
- SB 53's frontier developer has "trained, or initiated the training of";
- the EU's downstream modifier becomes a provider by modifying weights past a compute threshold, and footnote 12 points at "who has the control over the model's weights";
- ETSI's system operator becomes an EU provider "if they make changes to the system".

Other operative facts are market acts or use. So a translation of a source's role word can often say: *"this institutional role is conferred on parties who perform writing act W (into part P) above threshold T, or market act M"*. That joins `alignment.md`'s writer rows to the laws' roles without forcing either onto the other. It is also the gamma plan's §3.9 suggestion (institutional roles conferred by an instrument under Hohfeldian operative facts), with the operative facts named.

*What this overrules in the brief's reading:* "the laws divide by lifecycle or market; the map divides by writing" holds for the EU's core Art. 3 roles. It does not hold for SB 53, whose frontier developer is defined by a training act, or for the EU's own guidelines on modification. The writing basis is already inside the institutional instruments, as operative facts.
