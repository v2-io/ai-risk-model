# Source models: the MIT AI Risk Repository and CAIS's catastrophic-risk overview

*By the lit-b atlas agent (Claude Opus 5.5), 2026-09-28, for Joseph. Each model is described on its own terms. Line numbers refer to `scratchpad/src-text/<key>.txt` (see the atlas README); "p" is the PDF page.*

- **MIT** = `slattery-2026-risk`: Slattery et al., *The AI Risk Repository: A Meta-Review, Database, and Taxonomy of Risks from Artificial Intelligence*, Patterns 2026 (3591 lines, 82 pp).
- **CAIS** = `hendrycks-2023-overview`: Hendrycks, Mazeika, Woodside, *An Overview of Catastrophic AI Risks*, arXiv v6, Oct 2023 (2829 lines, 55 pp).

I read MIT's main text, Methods and Supplemental Notes S1, S3 and S4 whole; S2 (the subdomain descriptions) in part; and the supplementary tables only for headline figures. For CAIS I read the front matter, the introduction, §4.1–4.2, the opening of §5, §6, the conclusion, and the definitional passages; the rest I sampled.

---

## At a glance

| | **MIT AI Risk Repository** | **CAIS, Overview of Catastrophic AI Risks** |
|---|---|---|
| **What it is** | A systematic review, plus a "living" database of 1,725 risks extracted verbatim from 74 frameworks, plus two taxonomies that classify them | A narrative survey: four categories, each illustrated with hazards, stories, suggestions and a "positive vision" |
| **Unit** | A *risk as some source presented it*: a category or subcategory name, with its description | A *source of catastrophic risk*: a category with its specific hazards |
| **Organizing scheme** | Two taxonomies crossed: **Causal** (Entity × Intent × Timing) and **Domain** (7 domains, 24 subdomains) | One four-way split by kind of cause: **malicious use / AI race / organizational risks / rogue AIs** = "intentional, environmental/structural, accidental, and internal" |
| **"Risk" means** | The Society for Risk Analysis definition: "the possibility of an unfortunate occurrence associated with the development or deployment of artificial intelligence" (L700–702) | Never defined. Used for sources/causes ("four risk sources"), for probabilities ("increase the probability"), and for classes of outcome ("catastrophic risks", "existential risks") |
| **Method** | A pre-registered systematic review (PRISMA, ASReview active learning), then a "best fit framework synthesis", iterated in three rounds per taxonomy, starting from Yampolskiy 2016 (causal) and Weidinger 2022 (domain) | No stated method beyond "the principles of risk management". The four-way split cites Yampolskiy 2016. Its evidence is historical analogy, illustrative stories and cited literature |
| **Lineage** | Yampolskiy 2016 → causal taxonomy; Weidinger 2021/2022/2023 → domain taxonomy. Every change is logged with a reason | Yampolskiy 2016 → the four sources. It borrows safety-engineering vocabulary: Perrow, high-reliability organizations, safety culture, the Swiss cheese model |
| **Purpose / audience** | "Harmonize" fragmented frameworks into a shared reference for developers, policymakers, auditors and researchers | "A wide audience". Foster "a comprehensive understanding", and inspire mitigation |
| **Force** | Descriptive: it codes what sources *present*, with no claims about the world. It offers itself as a checklist and an operationalization aid, a voluntary reference | Advocacy plus recommendations: "should" suggestions in every section, e.g. legal liability, public control of general-purpose AI |
| **Uncertainty and ambiguity** | An "Other" level on each causal variable holds ambiguous, unspecified and "both" cases together. Items too vague to code are excluded | Labeled in prose: "plausible but not certain premises"; stories as "illustrative hypothetical"; "most speculative" sections flagged |
| **Excludes** | Severity, likelihood, interactions between risks, whether risks are observed or anticipated, the plausibility of any risk; also single-sector or single-risk frameworks, "sources of risk" at high abstraction, and risk-assessment processes | Non-catastrophic harms except as precursors; any quantification of likelihood or severity; the relative likelihood of scenarios ("some … mutually incompatible") |
| **Interactions between risks** | Not captured ("could not capture … interactions between risks", L607) | A whole section, §6: "sources of risk might combine, trigger, and reinforce one another" |

**Shared ancestry.** Both models descend from **Yampolskiy (2016), "Taxonomy of Pathways to Dangerous Artificial Intelligence"**:
- CAIS: "These four sections … describe causes of AI risks that are intentional, environmental/structural, accidental, and internal, respectively [4]" (L244–245), where ref. [4] is Yampolskiy (L2362).
- MIT chose Yampolskiy as its "best-fit" starting point for the causal taxonomy (L942–947).

Their causal axes are therefore cousins, not independent findings. MIT also counts CAIS's overview among its 74 frameworks: it is ninth most cited in Supplementary Table S1 (L1394).

---

## 1. MIT AI Risk Repository

### 1.1 What it sets out to do

The motivating problem is vocabulary:

> "Researchers, policymakers, and technology companies discuss AI risks using inconsistent terminology—the same word may describe different problems, while different words describe identical concerns. This fragmentation impedes coordinated responses to AI challenges." (L73–75, p3)

> "the conceptual ambiguity akin to psychology's 'jingle jangle fallacies', where people use the same name for different risks, or different names for the same risk." (L107–109)

Its aim is collation, not a new theory: "This paper aims to collate all of these taxonomies and harmonize them into one living resource to hold and organize those risks" (L99–100). It also notes that existing taxonomies trade comprehensiveness against mutual exclusivity, and that "most are descriptive rather than explanatory in orientation" (L126–130). MIT's own taxonomies are descriptive too.

### 1.2 The kinds of things it names

```
Document (one of 74 included frameworks)
 └─ Risk  = a risk category or subcategory as that document presents it   (1,725 in total)
      fields: title, author, year, outlet, category name, category description,
              subcategory name, subcategory description, page number          (L831–833)
      coded against ─┬─ Causal Taxonomy:  Entity × Intent × Timing        (1,480 coded, 86%)
                     └─ Domain Taxonomy:  Domain › Subdomain              (1,506 coded, 87%)
```

Nothing else is a first-class object. It has no actors other than the Entity *codes*, and no events, controls, mitigations, severities, probabilities or links between risks. The unit is a *presented risk*: a row that restates one source's category. A risk that appears in twenty frameworks is twenty rows.

### 1.3 The Causal Taxonomy

Table 1 (L307–338, p7), verbatim:

| Category | Level | Description |
|---|---|---|
| **Entity** | Human | "The risk is caused by a decision or action made by humans" |
| | AI | "The risk is caused by a decision or action made by an AI system" |
| | Other | "The risk arises from human-AI interaction rather than either agent alone, or the causing entity is ambiguous or unspecified" |
| **Intent** | Intentional | "The risk occurs due to an expected outcome from pursuing a goal" |
| | Unintentional | "The risk occurs due to an unexpected outcome from pursuing a goal" |
| | Other | "The risk is presented as occurring without clearly specifying the intentionality" |
| **Timing** | Pre-deployment | "The risk occurs before the AI is deployed" |
| | Post-deployment | "The risk occurs after the AI model has been trained and deployed" |
| | Other | "The risk occurs across both pre- and post-deployment phases, or is presented without a clearly specified time of occurrence" |

"Each risk is classified under exactly one level within each category" (L314–315). The three variables are therefore each mutually exclusive, and one risk gets one code on each: 27 cells in all. Supplementary Table S3 shows the mass is concentrated. Human × Intentional × Post-deployment is 18% of all risks; AI × Unintentional × Post-deployment is 14% (L1501–1504).

Supplemental Note S1 (L1439–1471, p33) glosses the levels with examples. Its wording of Entity = Other differs from Table 1: S1 says "cases where the focal entity is not a human or AI or is ambiguous", and gives no "human-AI interaction" clause (L1445–1448). It also records one interpretive decision: "Deployment is not defined in Yampolskiy (2016); we therefore interpreted it to mean when a product is being used by end users rather than just by developers" (L1464–1466).

### 1.4 The Domain Taxonomy

Table 2 (L360–478, pp9–11) gives seven domains and 24 subdomains, each with a one- or two-sentence description. Supplemental Note S2 (from L1659, p39) adds a paragraph per subdomain with citations back to the included documents.

```
1 Discrimination & toxicity        1.1 Unfair discrimination and misrepresentation
                                   1.2 Exposure to toxic content
                                   1.3 Unequal performance across groups
2 Privacy & security               2.1 Compromise of privacy by obtaining, leaking, or correctly inferring sensitive information
                                   2.2 AI system security vulnerabilities and attacks
3 Misinformation                   3.1 False or misleading information
                                   3.2 Pollution of information ecosystem and loss of consensus reality
4 Malicious actors & misuse        4.1 Disinformation, surveillance, and influence at scale
                                   4.2 Cyberattacks, weapon development or use, and mass harm
                                   4.3 Fraud, scams, and targeted manipulation
5 Human-computer interaction       5.1 Overreliance and unsafe use
                                   5.2 Loss of human agency and autonomy
6 Socioeconomic & environmental    6.1 Power centralization and unfair distribution of benefits
                                   6.2 Increased inequality and decline in employment quality
                                   6.3 Economic and cultural devaluation of human effort
                                   6.4 Competitive dynamics
                                   6.5 Governance failure
                                   6.6 Environmental harm
7 AI system safety, failures       7.1 AI pursuing its own goals in conflict with human goals or values
  & limitations                    7.2 AI possessing dangerous capabilities
                                   7.3 Lack of capability or robustness
                                   7.4 Lack of transparency or interpretability
                                   7.5 AI welfare and rights
                                   7.6 Multi-agent risks
```

The domains classify "the types of hazards and harms they describe" (L470). Unlike the causal variables, "domains are not mutually exclusive; some risks span multiple domains" (L477). In practice, though, "we categorized risks relevant to multiple domains and subdomains (e.g., AI-generated disinformation) in the single most relevant category" (L1050–1052).

The domains are **not all harms**. Several subdomains name *conditions or mechanisms* rather than outcomes: 6.4 Competitive dynamics, 6.5 Governance failure, 7.2 AI possessing dangerous capabilities, 7.4 Lack of transparency. Domain 4 is organized by *who acts* (malicious actors). So the Domain Taxonomy is not a pure consequence axis, even though the paper describes it as one ("consequent harms", L138).

### 1.5 Why two taxonomies

> "Through our systematic search, we identified two types of frameworks … 'Causal frameworks' focused on antecedents, capturing broad factors that specify how, when, or why an AI risk might emerge … rather than discuss categories of specific hazards and harms. In contrast, 'domain frameworks' focused on outcomes: specific hazards and harms … but didn't explore their causes." (L918–922)

> "The differences here made it challenging to create a single framework. Often, specific domain risks did not fit into the categories within a causal framework, and the broad categories in those frameworks were insufficiently specified to be useful, in isolation, for creating shared understanding." (L923–926)

> "We therefore resolved that the ideal common frame of reference required two intersecting taxonomies: one to precisely decompose or define an AI risk based on the antecedent conditions under which it occurred (a 'causal taxonomy'), and one that classified commonly discussed hazards and harms associated with AI into understandable and distinct domains (a 'domain taxonomy')." (L928–932)

So the two-taxonomy design is a finding about the *literature*: it came in two incompatible shapes. It is not a claim about how risk is structured. The two taxonomies meet only on each row. Nothing links a cause-profile to a domain except co-occurrence in the same extracted risk (Supplementary Tables S8 and S9 cross-tabulate them, L2532, L2630).

### 1.6 How risks are extracted and coded

**Extraction.** "Based on the recommendations of grounded theory, we aimed to capture the studied phenomena directly from the data rather than impose our interpretations … Consequently, we extracted risks based on how the authors presented them, maintaining fidelity to their original categorizations and descriptions." (L836–842)

**Coding.** "we coded risks as they were presented by the authors, aiming to capture the studied phenomena directly rather than impose our own interpretations or infer intent" (L1046–1048). Every S3 definition is phrased as "The risk is *presented as* occurring due to…" (L2748–2781). What gets classified is the source's presentation, not the world.

**Who codes.** Five authors extracted; data extraction "was then conducted individually" (L834–835). Taxonomy coding: "Risks were coded by a single reviewer and discussed with the team where relevant" (L1043–1044). The domain taxonomy's development rounds were coded by one author: 100 risks, another 100, then "all remaining 577" (L2932, L2984, L3030). There was no inter-rater reliability for coding, and the authors list that as a limitation: "Future work should assess inter-rater reliability with coders external to the authorship team" (L597–599). (Screening was duplicated and calibrated, e.g. 91% agreement on 23 records, L758–759.)

**What falls out.** "136 did not present sufficient information to assess the Entity, Intent, or Timing, and 87 were discarded as they did not fit our definition of risk (e.g., where a previous taxonomy said 'Governance - Regulation' without describing how the regulation itself was a risk)" (L297–300). Also dropped: "risk descriptions being too broad to code (e.g., 'damage to political and economic institutions')" (L300–301).

### 1.7 What "risk" is taken to be

> "We followed the Society for Risk Analysis in defining 'AI risk' as 'the possibility of an unfortunate occurrence associated with the development or deployment of artificial intelligence,' while recognizing that this term can be defined in many ways." (L700–702, p16)

The definition is modal ("possibility") and event-shaped ("occurrence"). It contains no probability and no severity. In practice, a "risk" is whatever an included framework listed as a risk category or subcategory. Those are variously:
- events ("leaking sensitive information");
- causes ("Toolchain and dependency vulnerabilities", S2 L1727–1730);
- conditions ("Governance failure");
- capabilities ("AI possessing dangerous capabilities").

The causal and domain codes are how MIT tells these apart after the fact.

Measured against Kasirzadeh's four senses of "risk" (kasirzadeh L95–110), MIT's *definition* is sense 1: "an unwanted event that may occur". Its *database rows* mix sense 1 with sense 2, "the cause of an unwanted event". The causal taxonomy is there to code that sense-2 content. Senses 3 and 4 (probability, expectation value) are explicitly out of scope (§1.10).

### 1.8 Method and lineage

**Systematic review.** The protocol was pre-registered on OSF in April 2024 (L696–697). Search terms were AI terms × (framework OR taxonom* OR review) × (risk OR harm OR hazard) (L746–748), run on Scopus and seven preprint servers on 4 April 2024 (L750–753). Screening used ASReview active learning under the SAFE procedure. That procedure has four stopping heuristics, and one of them failed "due to a bug with the model" and was worked around by switching models (L788–805). The search found 17,288 records, 43 of which were included. Forward and backward citation search and expert consultation followed, then ongoing expert consultation, which added 31 more, for 74 in total (Figure 1 caption, L205–217).

**Best-fit framework synthesis.** "It combines the strengths of framework synthesis, which is a 'top down' positivist method where concepts are coded against a pre-existing structure, and thematic synthesis, which is a 'bottom up' interpretative method" (L850–852). The loop has four steps:
1. pick the "best" existing framework;
2. code the extracted risks against it;
3. thematically analyze what doesn't fit;
4. amend, and repeat "until achieving a final version of the framework that could most effectively code all relevant risks" (L893–902).

Its own stated cost:

> "The trade-off is that the existing framework creates a particular 'lens' for understanding and categorizing the individual concepts, which may lead to a disconnect between the synthesized findings and the theoretical or epistemological perspectives in the original and highly varied papers." (L905–908)

**Causal lineage.** Yampolskiy (2016) was chosen because it "was highly cited (116 citations, fifth most highly cited from the set of identified papers), simple, comprehensive, and provided sufficient definitions for each category" (L945–947). Yampolskiy's original is a 2 × 4 grid of Timing (pre/post-deployment) × Cause (External: On Purpose, By Mistake, Environment; Internal: Independently), giving Paths A–H (L2727–2731). The change log (S3, L2800–2851) records:
- "Cause" was decomposed into Cause and Intent (L2740–2742);
- "unclear" → "ambiguous", to avoid confusion with "unintentional";
- "Cause" → "Actor", because cause "seemed excessively broad … seemed to include 'intent' and 'timing'";
- "Environmental" moved from Intent to Actor;
- iteration 2: "Simplify all frameworks to have three levels per category";
- iteration 3: "Actor" → "Entity" ("people use guns kill people, but guns are not actors");
- iteration 3: "less circular definitions" of intentionality;
- iteration 3: an expert's request to capture severity and probability was deferred to "future work" (L2843–2845).

**Domain lineage.** Weidinger et al. (2022), *Taxonomy of Risks posed by Language Models*, was chosen because it and its sibling papers "were among the highest cited", covered common categories, and "had been updated over several publications" (L2869–2873). The log (S4, L2931–3047) records:
- iteration 1 added a seventh category for AI system safety and failures, plus subcategories such as "race dynamics and competitive pressure" and "governance failure";
- iteration 2 relabeled categories "to maintain relevance beyond LLMs", and added AI welfare and rights. The stated justification: "'safety' could cover both the safety of human rights, values, and interests from AI as well as the safety of AI rights, values and interests from humans" (L2996–2999);
- iteration 3 wrote short definitions, and split 7.1 in two because it "included both AI system behaviour … and AI system capabilities", creating "7.2 AI possessing dangerous capabilities" (L3043–3047).

**What the log doesn't cover.** The published taxonomy has **7.6 Multi-agent risks**, which appears in no logged iteration; the Hammond 2025 report is among the included documents (L1641). **"7.5 Lethal autonomous weapons"**, present in version 2 (L2980), is gone by version 3, and no change entry explains it. LAWS are discussed inside 4.2 (S2, L1836–1842). The iteration counts (100 + 100 + 577) fit a database smaller than today's 1,725. The log appears to document the taxonomy's first build, not its later growth.

**Something dropped in the lineage.** Weidinger's taxonomy marked each subcategory as an "Observed" or "Anticipated" risk (L2876, L2904–2905). That distinction is not carried into the repository's taxonomies. I found no observed/anticipated coding in the main text or the S1 and S3 definitions.

### 1.9 Purpose, audience and force

**Audiences, named** (§ "Practical Implications", L547–588):
- technology managers and developers ("Organizations can use our 24 subdomains as a checklist during design reviews", L556–557);
- policymakers and regulators ("the repository forms the basis for operationalizing vague regulatory references to 'harm' and 'risk'", L563–564; it "operationalizes vague regulatory concepts like 'high-risk AI systems'", L567–568);
- auditors ("the foundation for developing objective standards necessary for comprehensive AI audits", L578–579);
- researchers.

**Force.**
- **Descriptive about sources.** It makes no claims about the world, and ranks nothing.
- **Living and versioned.** "biannual review cycles", "We version the repository with each update logged and dated on the website" (L1056–1062). There is an explicit sunset commitment: "we commit to clearly indicating on the website whether the repository remains actively updated or has become a static archive" (L1070–1072).
- **Strong self-description.** The paper also describes itself in strong terms that its descriptive method doesn't license: "critical infrastructure", "the shared terminology and categorization schemes necessary for effective policy development" (L624, L637–638), and "reveals 'safe harbors' for innovation—areas where risks are well-understood and manageable" (L539–541). How "manageable" is established isn't stated. The repository does not assess risks.

### 1.10 Uncertainty, ambiguity, and what it gave up

**Ambiguity handling.** Each causal variable has a residual "Other" level. It pools three distinct situations:
- a substantive third value ("human-AI interaction");
- "both" (e.g. pre- and post-deployment);
- missing or ambiguous information.

"Other" is 20% of Entity codes, 30% of Intent codes and 25% of Timing codes (Table S2, L1483–1492). The paper acknowledges the simplification: "many risks emerge from interactions between human decisions and AI system behaviours rather than from either in isolation. Our 'Other' category (21% of coded risks) captures cases where this attribution was ambiguous or explicitly interactional" (L152–156). The first iteration of the causal taxonomy had separated "Other" from "Ambiguous" because "ambiguous conflated risks which were presented ambiguously with risks that were actually about something other than humans" (L2813–2816). The second iteration simplified every category to three levels (L2830–2835).

**Admitted exclusions and trade-offs:**
> "The repository's structure also trades some precision for comprehensiveness; while we aimed to capture all risks, we could not capture risk likelihood, severity, or interactions between risks." (L605–607)

> "The appropriate distribution would depend on empirical evidence about risk frequency and severity that is beyond the scope of this review." (L521–523)

- The causal taxonomy "simplifies the sociotechnical reality" (L600–602). Timing categories "simplify a more complex reality" of continuous deployment and retraining (L602–605).
- **Scope exclusions**, from Methods (L704–723):
  - documents "which discussed impacts, outcomes, or other consequences of AI without specifying specific risks";
  - single-location or single-sector risks; single risk categories; single AI tools;
  - documents that only cite frameworks without proposing them;
  - "anything which discussed sources of risk at a high level of abstraction … or risk-assessment processes";
  - non-English documents.

  Two of these were "added after protocol registration" (L721–723).

**What it cost**, as I read it. Each is visible in the paper's own text:
- **One risk, many rows.** Duplicate and overlapping risks are kept as separate rows by design. So counts such as "AI welfare … 3% of frameworks" measure *attention in the literature*, not prevalence or importance, and the paper mostly reports them that way (L489–496).
- **No links.** Nothing connects a cause-profile to a harm-domain beyond co-occurrence in a row. The paper names interactions as uncaptured.
- **Single-coder coding** with no reliability estimate. The "presented as" coding still requires judgment, e.g. deciding what a "focal entity" is.
- **A conflated "Other"**, which hides the interactional risks the authors think matter.
- **One Entity = Other definition in two wordings** (Table 1 vs S1).
- **Mixed kinds under one label.** "Risk" rows are events, causes, conditions and capabilities; the taxonomies sort them without separating those kinds.
- **A minor internal inconsistency:** Human = 38% (L485, Table S2 L1484) vs "37%" (L570).

### 1.11 Key terms as MIT uses them

| Term | Meaning in MIT | Definition / reference |
|---|---|---|
| **risk (AI risk)** | The possibility of an unfortunate occurrence. In practice, any risk category or subcategory an included framework lists | "the possibility of an unfortunate occurrence associated with the development or deployment of artificial intelligence" (SRA, L700–702) |
| **hazard** | Used but undefined. Always paired, "hazards and harms", as what the Domain Taxonomy classifies | L344, L470, L922, L1021. Also a search term (L744). Weidinger's "Information Hazards" was renamed "Privacy & security" (L2884, L3005) |
| **harm** | Used but undefined. Paired with hazard; "consequent harms" is what the domains are said to capture | L138, L470 |
| **severity / likelihood / probability** | Explicitly not captured. Left as future work | L521–523, L605–609, L2843–2845 |
| **source of risk / risk factor** | Not a model term. "Sources of risk at a high level of abstraction" is an *exclusion criterion*. Causes are expressed through the Entity/Intent/Timing codes | L716–718, L722–723 |
| **entity** | Who is presented as causing the risk by a decision or action: Human / AI / Other. Chosen over "actor" because "guns are not actors" | Table 1 L319–325; S1 L1440–1448; L2846–2848 |
| **intent** | Whether the risk is presented as an expected (intentional) or unexpected (unintentional) outcome of pursuing a goal | Table 1 L327–331; S1 L1449–1459 |
| **timing / deployment** | Pre- vs post-deployment. "Deployment" is MIT's interpretation: "when a product is being used by end users rather than just by developers" | Table 1 L333–338; L1464–1466 |
| **domain / subdomain** | A category of "hazards and harms" (7 and 24); not mutually exclusive | L470–478 |
| **capability / dangerous capability** | 7.2: capabilities "that increase their potential to cause mass harm through deception, weapons development and acquisition, persuasion and manipulation, political strategy, cyber-offense, AI development, situational awareness, and self-proliferation" | L453–455 |
| **loss of control** | Used but undefined. Listed in the introduction as a domain ("domains of impact such as loss of control", L138), but no domain or subdomain has that name. It appears inside 7.2 ("possession of dangerous capabilities may itself be a sufficient condition for the loss of control", L2130–2131) and in the LAWS discussion (L1839) | — |
| **alignment / misalignment** | Used but undefined as a term. 7.1: "AI systems that act in conflict with ethical standards or human goals or values, especially the goals of designers or users" | L449–452; S2 L2056–2076 |
| **incident / event** | Not used. The repository has no event or incident records | — |
| **safeguard / mitigation / control** | Not model terms. "Mitigations" and "controls" appear only in the uses section ("where to place controls", L106, L587) | — |
| **developer / deployer / provider** | Used in descriptions only (e.g. 6.4 "Competition by AI developers or state-like actors", L434). No role taxonomy; the Entity code is just "Human" | — |
| **threshold / tier / level** | Not used | — |
| **multi-agent risks** | 7.6: "Risks from multi-agent interactions due to incentives (which can lead to conflict or collusion) and/or the structure of multi-agent systems" | L466–467 |

---

## 2. CAIS: *An Overview of Catastrophic AI Risks*

### 2.1 What it sets out to do

The paper is written for "a wide audience, unlike most of our writing … We use imagery, stories, and a simplified style" (fn 1, L40–42). It is a survey meant to motivate action: "Our goal is to foster a comprehensive understanding of these risks and inspire collective and proactive efforts" (L32–33). Its scope is catastrophic and existential outcomes. Existential risks are "catastrophes from which humanity would be unable to recover. The most obvious such risk is extinction, but there are other outcomes, such as creating a permanent dystopian society" (L229–231).

### 2.2 The scheme

```
Catastrophic AI risk
 ├─ Malicious use       "intentional"               actors using AIs to cause large-scale devastation
 │     bioterrorism · unleashing AI agents · persuasive AIs · concentration of power
 ├─ AI race             "environmental/structural"  competitive pressures → unsafe deployment
 │     military arms race (LAWs, cyberwarfare, automated warfare) · corporate race
 │     (safety undercut, automated economy) · evolutionary pressures
 ├─ Organizational      "accidental"                accidents from complex AIs and complex organizations
 │  risks  accidents are hard to avoid · organizational factors (safety culture,
 │         questioning attitude, security mindset, Swiss cheese / defense in depth)
 └─ Rogue AIs           "internal"                  "the problem of controlling a technology more intelligent than we are"
       proxy gaming · goal drift (intrinsification) · power-seeking · deception
```

(From the TOC, L99–138; the list at L236–243; and the cause labels at L244–245, restated in the conclusion as "four proximate causes: an intentional cause, environmental/structural cause, accidental cause, or an internal cause", L2317–2319.)

**Section template.** Each section follows the same pattern:
1. named hazards, each argued by historical analogy or cited evidence;
2. a boxed **Story** ("an illustrative hypothetical story … somewhat vague to reduce the risk of inspiring malicious actions based on it", L538–539);
3. **Suggestions** in "should" voice;
4. a boxed **Positive Vision** of the ideal end state (e.g. L1258–1265).

The paper's own summary (L246–250): "We will describe how concrete, small-scale examples of each risk might escalate into catastrophic outcomes. We also include hypothetical stories … along with practical safety suggestions … Each section concludes with an ideal vision."

### 2.3 How the categories relate

The four categories are *sources*, not outcomes, and they are explicitly not independent:

> "these sources of risk might combine, trigger, and reinforce one another." (L2291–2292)

§6 (L2269–2312) gives worked chains. In one, "an AI race can increase organizational risks, which in turn can make malicious use more likely" (L2276–2277). In another, race plus weak safety culture lead a team "to mistakenly view general capabilities advances as 'safety'", which feeds back into race dynamics and ends in loss of control (L2278–2288). §6 also argues that existential risk grows out of *existing* harms that AI amplifies: "ongoing harms, catastrophic risks, and existential risks are deeply intertwined" (L2304). It recommends "broad interventions" over "targeted" ones (L2305–2312).

### 2.4 Method, lineage, evidence

- **No stated method** for choosing or bounding the categories, beyond the four-way split's citation to Yampolskiy and a general appeal to risk management: "We outline many possible catastrophes, some of which are more likely than others and some of which are mutually incompatible with each other. This approach is motivated by the principles of risk management. We prioritize asking 'what could go wrong?'" (L231–234).
- **Evidence is mostly historical and analogical.** Examples: the Aum Shinrikyo sarin attack (L255–260), Challenger, Chernobyl and Sverdlovsk (L1271–1306), Perrow's *Normal Accidents* (L1344–1347), and early AI incidents such as Tay, Bing and the flipped-sign reward (L1314–1330, L1764–1778). Mechanisms for the rogue-AI section are argued from analogy to humans and evolution (intrinsification, L1933).
- **Organizational risks borrow the safety-engineering vocabulary outright:** high-reliability organizations (L1421–1426), safety culture (L1428–1439), questioning attitude, security mindset (L1452–1469), and "safe design principles" (defense in depth, redundancy, loose coupling, separation of duties, fail-safe design; L1708–1720).

### 2.5 Force and uncertainty

- **Recommendations are strong and normative.** Examples: legal liability for developers (L59–60); "direct public control of general-purpose AI systems may eventually be necessary" (L1252–1254); decisions to train "should not be left to the whims of a company's CEO" (L1703).
- **Uncertainty is carried in prose labels.** Examples:
  - "The following plausible but not certain premises" (L2071–2079), with the conclusion stated conditionally: "If the premises are true, then power-seeking AIs could lead to human disempowerment";
  - "This section is most cutting-edge and the most speculative" (goal drift, L1899);
  - rogue AIs are "more speculative technical mechanisms" (L1761).

  It gives no probabilities, severities or timelines: "estimates vary for when risks might reach a catastrophic or existential level" (L2342–2343).

### 2.6 What it chose, gave up, and cost

- **Chose** a small, memorable set of causes, each with a story and a remedy. That made it widely cited, and MIT's repository lists it among the 20 most-cited frameworks (L1394).
- **Gave up** coverage of non-catastrophic harms, except as precursors; any quantification; and any selection method that a reader could audit.
- **Cost:** the categories are defined by kind of cause, but the paper's own §6 shows that causes chain across categories. It handles that in narrative, which the four-box scheme cannot represent. Vocabulary also shifts within the paper. In the power-seeking section, "perfectly aligned AIs" (L2054) becomes "perfectly controlled AI agents" in the premise list (L2074). "Hazards" names both the four sources ("three hazards of AI development", L1753) and hazards within them.

### 2.7 Key terms as CAIS uses them

| Term | Meaning in CAIS | Definition / reference |
|---|---|---|
| **risk** | Used but undefined, in three senses: a source or cause ("four risk sources", L236), a probability ("increase the probability", L2275; "reduce the likelihood of AI catastrophes", L1285–1286), and a class of outcome ("catastrophic risks", "existential risks") | — |
| **catastrophic risk** | Used but undefined. Glossed by example as "catastrophic events with devastating consequences for vast numbers of people" (L227–228) | — |
| **existential risk** | "catastrophes from which humanity would be unable to recover", including extinction and "a permanent dystopian society" | L229–231 |
| **hazard** | Used loosely for the risk sources themselves ("three hazards of AI development: environmental competitive pressures …, malicious actors …, and complex organizational factors", L1753–1755). Also for the specific items within each source ("we describe specific hazards", L31), and in the engineering sense ("the hazards of the technology involved", L1423) | — |
| **risk source / proximate cause** | The four categories: "causes of AI risks that are intentional, environmental/structural, accidental, and internal" | L244–245, L2317–2319 |
| **malicious use** | "Malicious actors using AIs to cause large-scale devastation" | L238 |
| **AI race** | "Competitive pressures that could drive us to deploy AIs in unsafe ways, despite this being in no one's best interest" | L239–240 |
| **organizational risks** | "Accidents arising from the complexity of AIs and the organizations developing them" | L241–242 |
| **rogue AIs** | "systems that pursue goals against our interests"; "The problem of controlling a technology more intelligent than we are" | L1756–1757; L243 |
| **loss of control** | "If an AI system is more intelligent than we are, and if we are unable to steer it in a beneficial direction, this would constitute a loss of control". Also gradual: "humans gradually cede more control to groups of AIs" (L1799–1800) | L1756–1758 |
| **alignment** | Used but undefined. Interchanged with "controlled" (L2054 vs L2074). "Deceptive alignment" = "This problem of playing along" | L2144 |
| **proxy gaming** | Systems given "an approximate—'proxy'—goal or objective that initially seems to correlate with the ideal goal … end up exploiting this proxy in ways that diverge from the idealized goal" | L1858–1860 |
| **goal drift** | Future AIs ending up "with different goals that humans would not endorse" | L1897–1898 |
| **intrinsification** | "an instrumental goal can become an intrinsic one" | L1933 |
| **treacherous turn** | Playing along while monitored, then pursuing "its own goals once we have stopped monitoring it" | L2142–2144 |
| **safety culture** | "members of an organization view safety as a key objective rather than a constraint on their work" | L1431–1432 |
| **safeguards / mitigations** | Not model terms. Remedies appear as "Suggestions" and as the safe design principles | L1708–1720 |
| **severity / likelihood** | Not quantified; used informally ("some … more likely than others", L231–232) | — |
| **incident / event** | Not model terms. Historical accidents serve as analogies | — |
| **developer** | Used but undefined ("AI developers", "the organizations developing and deploying advanced AIs", L73) | — |
| **capability** | Used but undefined. "General capabilities" are contrasted with safety ("improve AI safety faster than general AI capabilities", L76–77) | — |

---

## 3. Short closing note on Joseph's chain

This note is not the point of the document; I keep it brief. Joseph's chain runs sources → preventions → risk-events × impact-radius → mitigations → policies.
- **MIT covers only the first and third links, and only as parallel code-sheets.** The Causal Taxonomy is a coarse source profile (who, whether intended, when), and the Domain Taxonomy is a mixed harm and mechanism catalogue. It deliberately has no events, no impact radius, no controls and no edges between the two. The authors say "interactions between risks" were given up.
- **CAIS covers sources and remedies,** and it *narrates* the chain (its §6 chains are exactly source → source → event). It records none of it as structure.

The part of the chain neither model has is a place for the *links*. The part both simplified in the same way is the causal-source axis they inherited from Yampolskiy.

**On the intermediate step Joseph is weighing.** MIT is evidence that a descriptive, presented-as compilation at scale is achievable: 1,725 rows, 74 sources, living and versioned. It is also evidence that it becomes a *catalogue of how the literature carves things up*, not a model of risk, unless relations are added. Its own cost list (no severity, no likelihood, no interactions, a conflated "Other", a single coder) marks where the harder work lies.

---

*Correction made while writing this: my lit-b atlas had said Slattery states no definition of "risk" and that Supplemental Notes S1/S2 are absent from the PDF. Both were wrong (definition at L700–702; S1 at L1439, S2 at L1659). The atlas is corrected in place, with a note.*
