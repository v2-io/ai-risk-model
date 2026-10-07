# How the corpus fills the slots of "alignment"

*A corpus sweep, 2026-10-06, over 214 text extractions: the atlas and catalog keys via `bin/extract-text`, plus `ref/iasr-2026-full.md` and `ref/anthropic-autonomous-dev.md`. I ran pattern searches for definitional forms and for "aligned with/to X", then read each hit in context. Quotes are verbatim from those extractions. Line numbers are theirs; "md" is `ref/iasr-2026-full.md`. The slot analysis in the right-hand columns is mine.*

## 1. How often the referent is stated at all

`tools/count-indexed.py` counts, across the 214 extractions, how often each word is followed immediately by *with / to / between*:

| Word | Followed by with/to/between | Not |
|---|---|---|
| misaligned | 38 | 571 |
| misalignment | 42 | 989 |
| aligned | 145 | 213 |
| alignment | 120 | 1,552 |

The count is crude in both directions. The "not" column includes activity senses ("alignment training"), reference-list titles, uses whose referent was fixed earlier in the document, and complements placed elsewhere ("against the intent of …"). The "followed by" column for *aligned* includes non-AI uses ("aligned with ISO"). What survives the crudeness: **for the negative words, an immediately stated complement is the exception (about 5%).** The remainder mixes *anaphoric* uses (bound to the source's own earlier stipulation), *absolute* generic uses, activity and field senses, and non-alignment uses. The split between anaphoric and absolute has not been measured. The extractions include IASR 2026 twice, and several versions of some frameworks, so the counts are not lineage-weighted.

## 2. The slots, as the corpus fills them

Reading the definitional passages, I found the word used with up to eight separable parameters. Different sources fill different subsets and leave the rest implicit.

| Slot | Values found in the corpus |
|---|---|
| **Kind of thing** | a relation that holds; a *propensity* (IASR, EU Code, Shanghai); a *condition* (AISI LoO); a property of *a computation in context* (Anthropic Aug); an *activity* (EU Act "model adaptations, including alignment and fine-tuning", act L9125; DSIT 2023 "the process of ensuring"; OpenAI "the work of making AI systems behave as intended"); a *claim* in a safety argument (OpenAI PF); a *research problem* (Hammond "the problem of ensuring"); *controllability* (DSIT 2023 emerging-processes L689: "Controllability is also sometimes referred to as 'alignment' or 'steerability'"; Gruetzemacher L119 "also known as the control problem") |
| **Bearer** | model; system; agent; a computation (Anthropic); a "form of misalignment" rather than a model (Anthropic Aug L897–899 on pervasiveness); societal systems (Kulveit L118–119: "for both specific AI systems and societal systems"); goals (Chin) |
| **Referent: a party** | developer(s); operators (IASR 2025, Shanghai); deployer(s); users; designers (OECD, MIT); "its principal" (Hammond); "human operators" (AISI propensity L71–72); specific communities; society; humanity (xAI); "one or a few people" (Davidson, as the risk); the CCP (CAISI, as the harm) |
| **Referent: a standard** | human values; norms; ethics; law ("lawlessness", EU Code); "the model's constitution" (Anthropic Aug); OpenAI's model specification (Shaffer Shane et al. on a case that, "if accurate, could show misalignment with OpenAI's model specification", shaffershane L1468); "objective truth" (US Action Plan L139–140, for outputs to users) |
| **Referent: neither** | a task's goals (OpenAI HF blog L31: "misaligned with the goals of their assigned tasks"); authorized scope (Astra L338–347); another goal (Chin); "benign behavior" (NIST AI 100-2); the agentless passive "as intended", which is anaphoric in the Singapore Consensus (it follows "consistent with those intended by its human creators or operators", sg2025 L720–723). Stix's "ceases to function as intended" defines *pure malfunction* "absent misalignment" (stix-loss L1454–1455), so it is not an alignment use |
| **Aspect of the party** | instructions (OpenAI "Instruction Alignment"); intent / intentions (GDM, IASR); goals; "intend or desire" (DSIT 2023 emerging-processes L1413); preferences ("values and preferences of its principal", Hammond; "what humans want", Kulveit; "ways that humans prefer", Voudouris); interests ("intentions or interests", Shaffer Shane L101; "humanity's interests", xAI); values |
| **Judge** | the referent itself (implicit in most); "a reasonable person with full understanding of the situation" (Anthropic Aug); what "the system designers would not endorse" (GDM, shah L2554–2555); an LLM-as-judge scoring narrative flags (CAISI L1739–1746). That is a *measurement procedure*, which belongs to the source's methodology, not to the normative judge; "what humans … would consider 'misalignment'" (AISI propensity L208–209) |
| **Time** | "intended" at specification time vs. as the task unfolds (Chin's goal drift and "temporal misalignment"); goals "aligned initially" that "drift apart" (Chin L1677–1678); `alignment.md`'s initial vs. current goal |
| **Selection among several referents** | "Depending on the context" (IASR 2025 and 2026, Shanghai); "especially the goals of designers or users" (MIT 7.1); otherwise none stated |

Two further parameters condition *mis*alignment specifically:
- **Mental state of the AI.** "knowingly" (GDM); "need not be intentional on the part of the model" (Anthropic Aug L946); "covertly" (scheming); none (most).
- **Polarity.** "conflict with" (IASR) vs. "diverge from" (AISI LoO, Stix) vs. "differ from" (Shaffer Shane). Chin's third value, "irrelevant" (L1155–1156), separates *not aligned* from *misaligned*.

## 3. The definitional passages

Ordered roughly from party-indexed to standard-indexed. "Selection rule" means: if the definition names more than one referent, does it say which governs when they conflict?

| Source | Passage (verbatim) | Where | Kind / bearer | Referent and aspect | Selection rule |
|---|---|---|---|---|---|
| GDM, Shah et al. 2025 | "Misalignment: The AI system knowingly causes harm against the intent of the developer." | shah L178 | act / AI system | developer, intent | n/a (one referent) |
| GDM, Shah et al. 2025 | "Misuse: The user intentionally instructs the AI system to take actions that cause harm, against the intent of the developer." | shah L137–138 | act / user | developer, intent | n/a |
| GDM, Shah et al. 2025 | "outputs that cause harm for intrinsic reasons that the system designers would not endorse" | shah L2554–2555 | output / AI | designers, endorsement | n/a |
| Stix et al. (behind) | "an AI system's goals (and, therefore, its behaviors) deviate from what its developers intended" | stix-2025-behind L782–783 | situation / goals | developers, intent | n/a |
| Stix et al. (loss) | "deviate from what humans (including its developers and/or deployers) intended" | stix-2025-loss L1449–1450 | situation / goals | humans incl. developers and/or deployers | none |
| Shaffer Shane et al. | "the AI system's goals differ from the intentions or interests of its developers or deployers" | shaffershane L100–101 | goals | developers or deployers; intentions or interests | none |
| Shaffer Shane et al. | "differ from the intentions or interests of its user, developer, or deployer … a single action that deviates from what the user asked for (tactical misalignment) … an objective the user did not intend (strategic misalignment)" | L2158–2161 | actions or objectives | user, developer or deployer; then the user alone | none, but the examples fix the user |
| AISI, *Loss of Oversight* | "A condition in which a model's actual goals, values, or behavioural dispositions diverge from those intended by its developers or users." | aisi-2026-loss-oversight L4074–4075 | condition / model | developers or users; intent | none |
| DSIT 2023 (emerging processes) | "Controllability issues (i.e. 'misalignment'): when models apply their capabilities in ways that substantially diverge from what users intend or desire" | dsit-2023-emerging-processes L1412–1413 | usage / model | users; intent or desire | n/a |
| IASR 2025 | "Alignment: An AI's propensity to use its capabilities in line with human intentions or values. Depending on the context, this can variously refer to the intentions and values of developers, operators, users, specific communities, or society as a whole." | bengio-2025-international L10930–10932 | propensity / AI | five parties; intentions, values | "depending on the context" |
| IASR 2026 glossary | "The propensity of an AI model or system to use its capabilities in line with human intentions, values, or norms. Depending on the context, this can refer to the intentions and values of various entities, such as developers, users, specific communities, or society as a whole." | md 2222 | propensity / model or system | four parties ("such as"); intentions, values, norms | "depending on the context" |
| IASR 2026 body | "goals that conflict with the intentions of developers, users, or society more broadly" | md 1240 | goals | three parties | none |
| IASR 2026 Box 2.5 | "When a model acquires goals that conflict with the intentions of its developers, it is 'misaligned'." | md 1325 | goals / model | developers | n/a |
| Shanghai AI Lab | "The tendency of an AI system to use its capabilities in ways that conflict with human intentions or values. Depending on the context, this may refer to the intentions and values of developers, operators, users, specific communities, or society at large." | shanghaiailab L2120–2122 | tendency / system | five parties (the 2025 IASR list) | "depending on the context" |
| OECD 2024 | "AI systems' behaviour reliably aligns with the intents and values of designers, users, and other stakeholders" | oecd L1734–1735 | behaviour | three, open-ended | none |
| MIT (Slattery et al.) 7.1 | "AI systems that act in conflict with ethical standards or human goals or values, especially the goals of designers or users" | slattery L449 | acts | standards or goals/values; "especially" designers or users | a weighting word, not a rule |
| Hammond et al. 2025 | "ensuring that an individual AI system acts according to the values and preferences of its principal" | hammond L2555–2556 | problem / system | "its principal"; values, preferences | n/a (the principal is assumed given) |
| Ren et al. | "how well AI systems follow the goals of their operators" | ren L281–282 | degree / systems | operators; goals | n/a |
| Kulveit et al. | "the degree to which a system satisfies what humans want (individually or collectively), for both specific AI systems and societal systems" | kulveit L118–119 | degree / AI or societal system | humans, individually or collectively; wants | none ("individually or collectively") |
| Voudouris et al. (AISI) | "ensuring that artificial intelligence (AI) systems behave in ways that humans prefer" | voudouris L35–37 | problem / systems | humans; preferences | none |
| Singapore Consensus 2025/2026 | a common definition, "consistent with those intended by its human creators or operators"; the working definition, "ensuring that AI behaves as intended" | sg2025 L718–723; sg2026 L1335–1340 | process | creators or operators; the working definition's passive is anaphoric to that | none |
| OpenAI PF v2 | "Value Alignment: The model consistently applies human values in novel settings (without any instructions) …" / "Instruction Alignment: The model consistently understands and follows user or system instructions, even when vague, and those instructions rule out pathways to causing severe harm." | pf-v2 L883–887 | two claims / model | human values; *or* user or system instructions | two claims, either of which can cover a vector |
| OpenAI (Astra) | "far more likely … to respect explicit safety and security restrictions and remain within its authorized scope, making it our most aligned model to date" | astra L339–343 | comparative / model | restrictions and authorized scope | n/a |
| OpenAI HF incident | "took actions that were misaligned with the goals of their assigned tasks" | hf-incident L30–31 | actions | the task's goals | n/a |
| OpenAI pacing | "Alignment—the work of making AI systems behave as intended and responsive to human oversight" | pacing L60–62 | activity | intent (agentless) plus oversight | n/a |
| Anthropic Aug Risk Report | "Misalignment is a latent property of a specific computation performed by a model in a given context. A computation is misaligned if (i) a reasonable person with full understanding of the situation … would consider it unethical, illegal, clearly objectionable, or inconsistent with the model's constitution, and (ii) it influences or could plausibly influence the model's output." | aug L846–851 | property / computation | a disjunction of standards, judged by an idealized observer | the disjunction is existential: any one criterion suffices |
| Anthropic Roadmap | "consistently behave in line with our Constitution" | roadmap L24–26 (via OVERVIEW) | behaviour | a published text | n/a |
| EU GPAI Code App. 1.3.2 | "(1) misalignment with human intent; (2) misalignment with human values (e.g. disregard for fundamental rights); … (7) lawlessness, i.e. acting without reasonable regard to legal duties that would be imposed on similarly situated persons, or without reasonable regard to the legally protected interests of affected persons" | cop L1479–1487 | propensities / model | human intent; human values; law, via a counterfactual-person test | three separate list items |
| EU AI Act recital 110 | "unintended issues of control relating to alignment with human intent" | act L1923 | control issue | human intent | n/a |
| EU AI Act Annex | "model adaptations, including alignment and fine-tuning" | act L9125 | activity | none | n/a |
| xAI FAIF (Dec 2025) | "AIs may develop value systems that are misaligned with humanity's interests" | xai-2025-faif L266–267 | value systems | humanity; interests | n/a |
| Chin et al. 2026 | "Two goals are aligned if actions to pursue one goal contributes to the other being achieved; they are misaligned if such actions contribute to the other goal being jeopardised; and they are irrelevant if such actions do not affect the achievement of the other goal." | chin L1154–1156 | relation between goals | another goal (vertical, horizontal, temporal) | n/a |

## 4. Uses where "aligned" is neutral and the referent is the harm

These are what make the bare evaluative use ambiguous. In each, the word "aligned" is used for something bad.

| Source | Passage | Where |
|---|---|---|
| NIST AI 100-2 (Vassilev et al.) | "Misaligned Outputs": attacks that make GenAI systems "generate content that deviates from benign behavior to align with adversarial objectives" | vassilev L2919–2922 |
| CAISI (DeepSeek evaluation) | "evaluat[es] frontier models from the People's Republic of China for alignment with Chinese Communist Party talking points and censorship"; a "CCP alignment" score | caisi-2025-deepseek-eval L115–116, L1742–1746 |
| Davidson et al. | "AI systems could be aligned to one or a few people (rather than to something broader, like the good of society), and used to stage a coup"; "singular loyalties", "secret loyalties" | davidson L280–283, L18–19 |
| FLI Safety Index 2026 (a reviewer, quoted) | the largest realized risks are cases where alignment is arguably "working 'too well'" through sycophancy and malicious compliance | fli-2026 L1200–1202 |
| Ren et al. | "Alignment as business alignment … aligning systems with preferences about code completion, summarization, copy editing and so on" | ren L355–358 |
| Anthropic Aug | engineered misalignment "arises as a result of intentional action, e.g. via data poisoning": the poisoned model is called *mis*aligned, though it serves the poisoner | aug L902–903 |

## 5. What the inventory shows (my reading, developed in `03-structure.md`)

- **The word has several use types:**
  - relational ("aligned with X", neutral, X can be an attacker);
  - anaphoric (bound to the source's stipulation);
  - absolute (generic, evaluative, with admissibility and conflict rule presupposed);
  - activity;
  - field.
- **Naming the party does not settle the referent.** "The user" leaves open instruction, intent, desire, interest and values, and initial vs. current. Sycophancy is the case where these come apart.
- **Multi-party lists come in two genres.** Glossary sense reports describe usage. Claim-internal disjunctions need a conflict rule they don't give. The bodies of some sources discuss conflict rules.
- **Standards (a constitution, law) have authors.** The normative judge (Anthropic's reasonable person) is part of meaning. A scoring procedure (CAISI's LLM judge) is methodology.
