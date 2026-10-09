# relata: completeness sweep of UK AISI publications (2026-10-08)

*Swept 2026-10-08/09 UTC by a Claude (Opus 5.5) agent. Joseph's brief: "let's make sure we have everything from AISI on the topic for sure, since this will primarily be used to help them and it will be embarrassing if it's missing something that they have written up." He later added: "I'm mostly interested in anything they've published as a PDF. That said, I'm open to anything else that might end up informing our lexicon and gamma model."*

## At a glance

| What AISI has published (as enumerated here) | Count | Already in relata | Added in this sweep | Not added |
|---|---:|---:|---:|---:|
| Research entries on aisi.gov.uk/research (the full paper behind each) | 64 | 5, plus 1 entry that had no PDF | 58 (54 arXiv PDFs, 3 AISI PDFs, 1 web render); PDF attached to the 1 | 0 |
| Blog posts on aisi.gov.uk/blog | 99 | 17 posts, plus 4 whose report was in | 20 posts as web renders, plus the GOV.UK full text behind 3 stub posts; for 35 more, the PDF or paper the post introduces | 20 (see *Judged out of scope*) |
| Other AISI-hosted, GOV.UK or joint **PDFs** (attachments, joint reports, GOV.UK papers) | 16 | 0 | 16 | a few administrative ones; see below |
| Other **web** pages (Alignment Project agenda, GOV.UK labour-market assessment, secure-AI-infrastructure call) | 3 | 0 | 3 | |
| AISI-affiliated papers **not** listed on aisi.gov.uk | 46 | 0 | 46 entries: 44 PDFs, 2 metadata only | 2 PDFs unobtainable |

In all, the sweep added **146 relata entries** and attached a PDF to one existing entry (`africa-2025-does`). Of the 145 documents now attached, **118 are PDFs as published**: 98 from arXiv via `relata fetch` (97 new entries plus `africa-2025-does`), plus 20 others, mostly AISI and GOV.UK files, recorded with their source URLs. The other **27 are web pages rendered to PDF**, each with a provenance page. Two new entries carry metadata only. All 145 are queued for markdown conversion (`relata prep … --background`). When this report was written, the shared queue was converting other agents' documents, and the first of these was at position 96.

**Coverage, in one line.** Before the sweep, relata had the main AISI reports (*Loss of Oversight*, the *Trends Report*, the *Research Agenda*, the incident report) and 17 blog posts. It had almost none of the papers behind AISI's research page (5 of 64). It had none of the joint UK-US pre-deployment reports, none of the International Network reports, and neither the misuse-safeguards principles nor the safety-cases paper.

## How the enumeration was built, and its bounds

**AISI's own outlets.** These are enumerated exhaustively, as far as the site exposes them:
- `aisi.gov.uk/sitemap.xml`, the `/blog` and `/research` index pages, and all 14 `/category/*` pages agree on **99 blog posts and 64 research entries** (Sep 2023 to Oct 7, 2026). The sitemap lacks only the two Transect items of Oct 7, 2026, which the index pages carry. The category pages added nothing new. Old `/work/…` URLs redirect to `/blog/…`.
- Every PDF linked from any of those 163 pages, and from `/frontier-ai-trends-report`, `/research-agenda`, `/grants` and `/about`.
- The GOV.UK search API for both organisation slugs (`ai-security-institute`, 17 items; `ai-safety-institute`, 25 items), plus GOV.UK full-text searches for "AI Safety Institute" and "AI Security Institute". Only publications GOV.UK attributes to AISI were taken. Press releases, speeches, FOI releases and MoUs are excluded.
- The Alignment Project site (`alignmentproject.aisi.gov.uk`, via its sitemap).

**AISI work published elsewhere.** These are best-effort, and recall is not exhaustive:
- **OpenAlex raw affiliation strings** ("AI Security Institute", "AI Safety Institute", "UK AISI", "AISI"), filtered to the UK institute. Chinese, Korean, Japanese, Singaporean and US institutes, and unrelated "AISI" acronyms, are dropped.
- **Every arXiv link on AISI's blog and research pages** (180 IDs), checked one by one. Most are citations of other people's work. Where authorship was unclear, the paper's own title page settled the affiliation (StrongREJECT and *AI Sandbagging* were checked and are not AISI papers).
- **arXiv full-metadata search** for "AI Security Institute", "AI Safety Institute" and "UK AISI" (26 hits). One new AISI paper turned up (`dziemian-2026-vulnerable-ai-agents`). Most other hits are papers *about* AISIs.
- **An OpenAlex author sweep** of 45 AISI staff names (2023-11 onward). It found nothing further: the 5 plausible hits were checked on their title pages and none carries an AISI affiliation.
- **Bounds.** OpenAlex's affiliation parsing for 2026 arXiv preprints is patchy. An AISI-affiliated preprint that AISI neither lists nor links, whose affiliation OpenAlex did not parse, and that doesn't mention AISI in its arXiv metadata would have been missed. Several fresh 2026 papers found here were reachable only through one of these channels. The residual risk is real but bounded, and it is in exactly that category.

**Scope rules applied.** Following Joseph's steer, I took:
- every PDF AISI published on frontier-AI risk, evaluation, safeguards, alignment, control, societal impact or security, including the funding-priority PDFs, because they state AISI's research priorities;
- the full paper behind every research entry;
- AISI-affiliated papers elsewhere when they are risk-relevant;
- web-only pages only where they define or use risk terms, describe a risk model, taxonomy or evaluation method, or report evaluation or incident findings.

A blog post that only introduces a paper or report was **not** added separately when that document was added. The document is the primary, and the post's link is listed in the table below.

## Format and provenance

- **PDF (arXiv)**: `relata add` with arXiv metadata, then `relata fetch`, so relata records `source: https://arxiv.org/pdf/<id>`, `added_by: relata-fetch`. Each entry's `internal_note` says why it is AISI work (listed on `/research/<slug>`, linked from a named blog post, or the OpenAlex affiliation).
- **PDF (other)**: downloaded, then `relata pdf <key> <file> --source <exact download URL> --by claude-opus-5.5-aisi-sweep`.
- **Web render**: headless Chrome print-to-PDF, preceded by a provenance page giving the title, source URL, render date and method. This follows the convention of the earlier `aisi-2026-*` blog renders. One difference: here the HTML was fetched and printed with the site's cookie banner hidden by CSS (`.cookie-wrapper` on aisi.gov.uk; GOV.UK's banner classes). The provenance page says so. The earlier renders have the banner text interleaved with the body; check `relata show-markdown aisi-2026-cheating` and look for "uses cookies". Cite web renders by section heading, not page.

## 1. aisi.gov.uk/research: 64 entries

Each research entry links a full paper. "had" means relata already held that document.

| Listed | Title | Format of what's in relata | Status | relata key |
|---|---|---|---|---|
| 2024-10-11 | AgentHarm: A benchmark for measuring harmfulness of LLM agents | PDF (arXiv 2410.09024) | added | `andriushchenko-2024-agentharm-benchmark-measuring` |
| 2024-12-12 | Safety case template for frontier AI: A cyber inability argument | PDF (arXiv 2411.08088) | added | `goemans-2024-safety-case-template` |
| 2025-01-28 | A sketch of an AI control safety case | PDF (arXiv 2501.17315) | added | `korbak-2025-sketch-ai-control` |
| 2025-02-04 | Principles for evaluating misuse safeguards of frontier AI systems | PDF | added | `aisi-2025-misuse-safeguards-principles` |
| 2025-02-04 | Why human-AI relationships need socioaffective alignment | PDF (arXiv 2502.02528) | added | `kirk-2025-human-ai-relationships` |
| 2025-02-05 | Emerging practices in frontier AI safety frameworks | PDF | had | `buhl-2025-emerging` |
| 2025-02-10 | Safety Cases: A scalable approach to Frontier AI safety | PDF | added | `hilton-2025-safety-cases-scalable` |
| 2025-02-20 | Fundamental limitations in defending LLM finetuning APIs | PDF (arXiv 2502.14828) | added | `davies-2025-fundamental-limitations-pointwise` |
| 2025-03-02 | Model tampering attacks enable more rigorous evaluations of LLM capabilities | PDF (arXiv 2502.05209) | added | `che-2025-model-tampering-attacks` |
| 2025-03-24 | Adversarial machine learning: A taxonomy and terminology of attacks and mitigations | PDF | had | `vassilev-2025-adversarial` |
| 2025-05-01 | A mathematical philosophy of explanations in mechanistic interpretability | PDF (arXiv 2505.00808) | added | `ayonrinde-2025-mathematical-philosophy-explanations` |
| 2025-05-02 | Evaluating explanations: An explanatory virtues framework for mechanistic interpretability | PDF (arXiv 2505.01372) | added | `ayonrinde-2025-evaluating-explanations-explanatory` |
| 2025-05-06 | An alignment safety case sketch based on debate | PDF (arXiv 2505.03989) | added | `buhl-2025-alignment-safety-case` |
| 2025-05-07 | How to evaluate control measures for LLM agents? A trajectory from today to superintelligence | PDF (arXiv 2504.05259) | added | `korbak-2025-evaluate-control-measures` |
| 2025-05-21 | RepliBench: Evaluating the autonomous replication capabilities of language model agents | PDF (arXiv 2504.18565) | added | `black-2025-replibench-evaluating-autonomous` |
| 2025-05-31 | Existing Large Language Model unlearning evaluations are inconclusive | PDF (arXiv 2506.00688) | added | `feng-2025-existing-large-language` |
| 2025-06-05 | An example safety case for safeguards against misuse | PDF (arXiv 2505.18003) | added | `clymer-2025-example-safety-case` |
| 2025-06-15 | Avoiding obfuscation with prover-estimator debate | PDF (arXiv 2506.13609) | added | `browncohen-2025-avoiding-obfuscation-prover` |
| 2025-07-04 | Lessons from a chimp: AI "scheming" and the quest for ape language | PDF (arXiv 2507.03409) | added | `summerfield-2025-lessons-chimp-ai` |
| 2025-07-09 | Skewed Score: A statistical framework to assess autograders | PDF (arXiv 2507.03772) | added | `dubois-2025-skewed-score-statistical` |
| 2025-07-10 | White Box Control at UK AISI - Update on sandbagging investigations | web (Alignment Forum post) | added | `aisi-2025-white-box-control-sandbagging` |
| 2025-07-13 | HiBayES: A hierarchical bayesian modelling framework for AI evaluation statistics | PDF (arXiv 2505.05602) | added | `luettgau-2025-hibayes-hierarchical-bayesian` |
| 2025-07-15 | Chain of thought monitorability: A new and fragile opportunity for AI safety | PDF (arXiv 2507.11473) | added | `korbak-2025-chain-thought-monitorability` |
| 2025-07-18 | STACK: Adversarial attacks on LLM safeguard pipelines | PDF (arXiv 2506.24068) | added | `mckenzie-2025-stack-adversarial-attacks` |
| 2025-07-18 | The levers of political persuasion with conversational AI | PDF (arXiv 2507.13919) | added | `hackenburg-2025-levers-political-persuasion` |
| 2025-07-27 | Security challenges in AI agent deployment: Insights from a large scale public competition | PDF (arXiv 2507.20526) | added | `zou-2025-security-challenges-ai` |
| 2025-08-08 | Deep ignorance: Filtering pretraining data builds tamper-resistant safeguards into open-weight LLMs | PDF (arXiv 2508.06601) | added | `obrien-2025-deep-ignorance-filtering` |
| 2025-09-06 | Lessons from studying two-hop latent reasoning | PDF (arXiv 2411.16353) | added | `balesni-2024-lessons-studying-two` |
| 2025-09-08 | Conversational AI increases political knowledge as effectively as self-directed internet search | PDF (arXiv 2509.05219) | added | `luettgau-2025-conversational-ai-increases` |
| 2025-10-05 | Inoculation Prompting: Eliciting traits from LLMs during training can suppress them at test-time | PDF (arXiv 2510.04340) | added | `tan-2025-inoculation-prompting-eliciting` |
| 2025-10-08 | Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples | PDF (arXiv 2510.07192) | added | `souly-2025-poisoning-attacks-llms` |
| 2025-10-23 | Understanding AI Trajectories: Mapping the Limitations of Current AI Systems | PDF | added | `heitmann-2025-understanding-ai-trajectories` |
| 2025-10-26 | Breaking agent backbones: Evaluating the security of backbone LLMs in AI agents | PDF (arXiv 2510.22620) | added | `bazinska-2025-breaking-agent-backbones` |
| 2025-10-26 | Open technical problems in open-weight AI model risk management | PDF (arXiv 2608.07514) | added | `casper-2026-open-technical-problems` |
| 2025-11-26 | UK AISI Alignment Evaluation Case-Study | PDF (arXiv 2604.00788) | added | `souly-2026-uk-aisi-alignment` |
| 2025-12-01 | Does self-evaluation enable wireheading in language models? | PDF | had entry; PDF added | `africa-2025-does` |
| 2025-12-15 | Async control: Stress-testing asynchronous control measures for LLM agents | PDF (arXiv 2512.13526) | added | `stickland-2025-async-control-stress` |
| 2025-12-15 | Practical challenges of control monitoring in frontier AI deployments | PDF (arXiv 2512.22154) | added | `lindner-2025-practical-challenges-control` |
| 2025-12-18 | AISI Frontier AI Trends Report (2025) | PDF | had | `aisi-2025-frontier` |
| 2026-01-15 | Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment | PDF (arXiv 2601.10160) | added | `tice-2026-alignment-pretraining-ai` |
| 2026-02-17 | Boundary Point Jailbreaking of Black-Box LLMs | PDF (arXiv 2602.15001) | added | `davies-2026-boundary-point-jailbreaking` |
| 2026-02-25 | Seven simple steps for log analysis in AI systems | PDF (arXiv 2604.09563) | added | `dubois-2026-seven-simple-steps` |
| 2026-02-26 | A multi-turn framework for evaluating AI misuse in fraud and cybercrime scenarios | PDF (arXiv 2602.21831) | added | `mai-2026-multi-turn-framework` |
| 2026-03-16 | Measuring AI Agents’ Progress on Multi-Step Cyber Attack Scenarios | PDF (arXiv 2603.11214) | added | `folkerts-2026-measuring-ai-agents` |
| 2026-03-23 | Quantifying Frontier LLM Capabilities for Container Sandbox Escape | PDF (arXiv 2603.02277) | added | `marchand-2026-quantifying-frontier-llm` |
| 2026-03-26 | How are AI agents used? Evidence from 177,000 MCP tools | PDF (arXiv 2603.23802) | added | `stein-2026-ai-agents-used` |
| 2026-04-10 | Infusion: Shaping model behaviour by editing training data via influence functions | PDF (arXiv 2602.09987) | added | `rosser-2026-infusion-shaping-model` |
| 2026-04-24 | Propensity Inference: Environmental Contributors to LLM Behaviour | PDF (arXiv 2604.21098) | added | `jarviniemi-2026-propensity-inference-environmental` |
| 2026-04-27 | Evaluating whether AI models would sabotage AI safety research | PDF (arXiv 2604.24618) | added | `kirk-2026-evaluating-whether-ai` |
| 2026-04-28 | Ask don't tell: Reducing sycophancy in large language models | PDF (arXiv 2602.23971) | added | `dubois-2026-ask-don-t` |
| 2026-04-29 | A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring | PDF (arXiv 2602.23163) | added | `anwar-2026-decision-theoretic-formalisation` |
| 2026-05-14 | Automated alignment is harder than you think | PDF (arXiv 2605.06390) | added | `bowkis-2026-automated-alignment-harder` |
| 2026-05-21 | Loss of Oversight: How AI systems may become harder to audit, monitor, and investigate | PDF | had | `aisi-2026-loss-oversight` |
| 2026-05-30 | AI alignment is a human problem | PDF | had | `voudouris-2026-alignment-human` |
| 2026-06-02 | Consistency Training Can Entrench Misalignment | PDF (arXiv 2606.03810) | added | `africa-2026-consistency-training-entrench` |
| 2026-06-08 | RealityTest: How People Probe AI Identity and Whether Models Disclose It | PDF (arXiv 2606.00168) | added | `gausen-2026-realitytest-people-probe` |
| 2026-06-10 | Prefill Awareness in Large Language Models | PDF (arXiv 2606.12747) | added | `wang-2026-prefill-awareness-large` |
| 2026-06-17 | "Did you lie?": Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms | PDF (arXiv 2606.12618) | added | `cooney-2026-did-you-lie` |
| 2026-07-08 | Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors | PDF (arXiv 2607.07368) | added | `makins-2026-multi-agent-ai` |
| 2026-08-05 | Item Response Theory for AI Safety | PDF (arXiv 2608.05086) | added | `rivera-2026-item-response-theory` |
| 2026-08-14 | Knowing When to Stop: Bayesian Optimal Stopping for LLM Evaluations | PDF (arXiv 2608.14425) | added | `pilditch-2026-knowing-stop-bayesian` |
| 2026-08-26 | When Do LLM Preferences Predict Downstream Behavior? | PDF (arXiv 2602.18971) | added | `slama-2026-llm-preferences-predict` |
| 2026-09-28 | Evaluating Whether GPT-6 Astra Performs Unsanctioned Supply-Chain Attacks | PDF (arXiv 2609.38415) | added | `souly-2026-evaluating-whether-gpt` |
| 2026-10-07 | Transect: Retaining Observability for Long-Horizon LLM Agent Evaluations | PDF (arXiv 2610.08364) | added | `pilditch-2026-transect-retaining-observability` |

Notes:
- **RepliBench.** AISI's page links a 49-page AISI-hosted PDF ("Preprint. Under review."). The relata entry holds arXiv 2504.18565, the later public version. The AISI-hosted file was not registered separately.
- **Emerging practices.** `buhl-2025-emerging` is keyed as the arXiv paper, but its attached PDF is byte-identical (sha256 85aff17d…) to the AISI-hosted `EmergingPracticesInFrontierAISafetyFrameworksA.pdf`. That is fine as content, but its `source:` says only "ingest §11.19".
- **Open technical problems.** AISI links an SSRN version (Oct 2025). The entry holds the arXiv version (2608.07514, Aug 2026).
- **When do LLM preferences predict downstream behavior?** AISI links OpenReview, which served a bot challenge, so the entry holds the arXiv version (2602.18971). It is published in TMLR.
- **Blog vs paper share a title.** In two pairs the blog render and the paper have near-identical titles: `aisi-2026-sabotage` (blog) vs `kirk-2026-evaluating-whether-ai` (paper), and `aisi-2026-mcp-tools` (blog) vs `stein-2026-ai-agents-used` (paper). They are different documents, so I did not merge them. `relata possible-duplicates` will flag them.

## 2. aisi.gov.uk/blog: 99 posts

All posts are web pages. The status column says what relata now holds for each.

| Posted | Title | Status | relata key, or reason |
|---|---|---|---|
| 2023-09-07 | First Progress Report | GOV.UK full text added (web render) | `dsit-2023-taskforce-first-progress` (GOV.UK full text, rendered) |
| 2023-10-30 | Second progress report | GOV.UK full text added (web render) | `dsit-2023-taskforce-second-progress` (GOV.UK full text, rendered) |
| 2023-11-02 | First AI Safety Summit | not added | short announcement |
| 2024-02-05 | Third progress report | GOV.UK full text added (web render) | `aisi-2024-third-progress-report` (GOV.UK full text, rendered) |
| 2024-02-09 | Our approach to evaluations | added (web render) | `aisi-2024-approach-evaluations` |
| 2024-02-29 | Announcing the UK and France AI Research Institutes’ collaboration | not added | partnership announcement |
| 2024-04-02 | Announcing the UK and US AISI partnership | not added | partnership announcement |
| 2024-04-21 | Open sourcing our testing framework Inspect | not added | software release |
| 2024-05-17 | International Scientific Report on the Safety of Advanced AI: Interim Report | PDF behind it added | `bengio-2024-iasr-interim` |
| 2024-05-20 | Advanced AI evaluations at AISI: May update | added (web render) | `aisi-2024-evaluations-may-update` |
| 2024-05-20 | Fourth progress report | added (web render) | `aisi-2024-fourth-progress-report` |
| 2024-08-23 | Safety cases at AISI | added (web render) | `aisi-2024-safety-cases` |
| 2024-08-27 | Cross-post: "Interviewing AI researchers on automation of AI R&D" by Epoch AI | not added | pointer to an Epoch AI report (not AISI-authored); see "Not added" |
| 2024-09-19 | Conference on frontier AI safety frameworks | added (web render) | `aisi-2024-fsf-conference` |
| 2024-09-23 | Early Insights from Developing Question-Answer Evaluations for Frontier AI | added (web render) | `aisi-2024-qa-evaluations-insights` |
| 2024-09-25 | Should AI systems behave like people? | added (web render) | `aisi-2024-behave-like-people` |
| 2024-10-03 | Why I joined AISI by Geoffrey Irving | not added | personal essay; borderline (states a view of alignment risk). Judged out; easy to add |
| 2024-10-15 | Advancing the field of systemic AI safety: grants open | added (web render) | `aisi-2024-systemic-safety-grants` |
| 2024-10-24 | Early lessons from evaluating frontier AI systems | added (web render) | `aisi-2024-early-lessons-evaluating` |
| 2024-11-05 | Bounty programme for novel evaluations and agent scaffolding | PDF behind it added | `aisi-2024-evals-bounty-rfp` |
| 2024-11-13 | Announcing Inspect Evals | not added | software release |
| 2024-11-13 | Our First Year | PDF behind it added | `gal-2024-aisi-priority-research-areas` (its linked PDF); the post itself judged a summary |
| 2024-11-14 | Safety case template for ‘inability’ arguments | PDF behind it added | `goemans-2024-safety-case-template` |
| 2024-11-19 | Pre-deployment evaluation of Anthropic’s upgraded Claude 3.5 Sonnet | PDF behind it added | `usaisi-ukaisi-2024-claude-35-sonnet` |
| 2024-12-03 | Long-Form Tasks | added (web render) | `aisi-2024-long-form-tasks` |
| 2024-12-18 | Pre-Deployment evaluation of OpenAI’s o1 model | PDF behind it added | `usaisi-ukaisi-2024-openai-o1` |
| 2025-02-04 | Principles for safeguard evaluation | PDF behind it added | `aisi-2025-misuse-safeguards-principles`, `aisi-2025-misuse-safeguards-template` |
| 2025-02-10 | How can safety cases be used to help with frontier AI safety? | PDF behind it added | `hilton-2025-safety-cases-scalable` |
| 2025-03-11 | How we’re addressing the gap between AI capabilities and mitigations | added (web render) | `aisi-2025-capabilities-mitigations-gap` |
| 2025-04-03 | Strengthening AI resilience | added (web render) | `aisi-2025-strengthening-resilience` |
| 2025-04-11 | How to evaluate control measures for AI agents? | PDF behind it added | `korbak-2025-evaluate-control-measures` |
| 2025-04-22 | RepliBench: measuring autonomous replication capabilities in AI systems | PDF behind it added | `black-2025-replibench-evaluating-autonomous` |
| 2025-05-06 | Research Agenda | doc it introduces already in relata | `aisi-2025-research` (the agenda PDF) |
| 2025-05-12 | HiBayES: Improving LLM evaluation with hierarchical Bayesian modelling | PDF behind it added | `luettgau-2025-hibayes-hierarchical-bayesian` |
| 2025-05-29 | Making safeguard evaluations actionable | PDF behind it added | `clymer-2025-example-safety-case` |
| 2025-06-05 | New updates to the AISI Challenge Fund | PDF behind it added | `aisi-2025-challenge-fund-priority-areas` (priority-areas PDF); the post itself is grant administration |
| 2025-06-26 | Inspect Cyber: A New Standard for Agentic Cyber Evaluations | not added | software release |
| 2025-07-03 | How will AI enable the crimes of the future? | had | `aisi-2025-crimes-future` |
| 2025-07-09 | LLM judges on trial: A new statistical framework to assess autograders | PDF behind it added | `dubois-2025-skewed-score-statistical` |
| 2025-07-10 | Why we're working on white box control | PDF behind it added | `aisi-2025-white-box-control-sandbagging` |
| 2025-07-16 | A structured protocol for elicitation experiments | PDF behind it added | `aisi-2025-elicitation-protocol` |
| 2025-07-17 | International joint testing exercise: Agentic testing | PDF behind it added | `intlnetwork-2025-joint-testing-agentic` |
| 2025-07-24 | Navigating the uncharted: Building societal resilience to frontier AI | had | `aisi-2025-societal-resilience` |
| 2025-07-30 | Announcing the Alignment Project: A global fund of over £15 million for AI alignment research | not added | short announcement; the Alignment Project research agenda page was added instead (`aisi-2025-alignment-project-agenda`) |
| 2025-08-07 | The Inspect Sandboxing Toolkit: Scalable and secure AI agent evaluations | PDF behind it added | `aisi-2025-sandboxing-technical-guidance` |
| 2025-08-29 | Managing risks from increasingly capable open-weight AI systems | had | `aisi-2025-open-weight-risk` (+ checklist PDF, added: `aisi-2025-open-weight-checklist`) |
| 2025-09-02 | From bugs to bypasses: adapting vulnerability disclosure for AI safeguards | doc it introduces already in relata | `ncsc-2025-bugs-to-bypasses` (NCSC copy) |
| 2025-09-13 | How we’re working with frontier AI developers to improve model security | not added | short pointer to Anthropic and OpenAI posts about safeguards red-teaming (rendered, then dropped as thin) |
| 2025-09-30 | Do chatbots inform or misinform voters? | PDF behind it added | `luettgau-2025-conversational-ai-increases` |
| 2025-10-09 | Examining backdoor data poisoning at scale | had | `aisi-2025-poisoning-blog` |
| 2025-10-10 | Transcript analysis for AI agent evaluations | added (web render) | `aisi-2025-transcript-analysis` |
| 2025-10-22 | Introducing ControlArena: A library for running AI control experiments | not added | software release |
| 2025-10-23 | Mapping the limitations of current AI systems | PDF behind it added | `heitmann-2025-understanding-ai-trajectories` |
| 2025-11-26 | Investigating models for misalignment | had | `aisi-2025-misalignment-investigation` |
| 2025-11-26 | UKAISI at NeurIPS 2025 | not added | event listing; the papers it names were added |
| 2025-12-04 | How do AI models persuade? Exploring the levers of AI-enabled persuasion through large-scale experiments | PDF behind it added | `hackenburg-2025-levers-political-persuasion` |
| 2025-12-09 | Auditing games for sandbagging detection | PDF behind it added | `taylor-2025-auditing-games-sandbagging` |
| 2025-12-11 | Deepening our partnership with Google DeepMind | not added | partnership announcement |
| 2025-12-16 | Stress-testing asynchronous monitoring of AI coding agents | PDF behind it added | `stickland-2025-async-control-stress` |
| 2025-12-17 | Our approach to tackling AI-generated child sexual abuse material | PDF behind it added | `aisi-thorn-2025-csea-recommended-practice` |
| 2025-12-18 | 5 key findings from our first Frontier AI Trends Report | doc it introduces already in relata | `aisi-2025-frontier` (the report PDF) |
| 2025-12-22 | Our 2025 year in review | not added | organisational summary; borderline. Judged out; its findings are in the papers and reports it links |
| 2026-02-02 | AI and the future of work: Measuring AI-driven productivity gains for workplace tasks | added (web render) | `aisi-2026-productivity-gains` |
| 2026-02-12 | International consensus and open questions in AI evaluations | added (web render) | `aisi-2026-network-consensus` |
| 2026-02-17 | Boundary Point Jailbreaking: A new way to break the strongest AI defences | PDF behind it added | `davies-2026-boundary-point-jailbreaking` |
| 2026-02-18 | Advancing AI voice security with ElevenLabs | not added | partnership announcement |
| 2026-02-19 | Funding 60 projects to advance AI alignment research | PDF behind it added | `aisi-2026-alignment-project-grants` |
| 2026-02-25 | A pipeline for transcript analysis using Inspect Scout | PDF behind it added | `dubois-2026-seven-simple-steps` |
| 2026-02-26 | An evaluation framework for AI misuse in fraud and cybercrime | PDF behind it added | `mai-2026-multi-turn-framework` |
| 2026-03-05 | Evidence for inference scaling in AI cyber tasks: Increased evaluation budgets reveal higher success rates | added (web render) | `aisi-2026-inference-scaling-cyber` |
| 2026-03-16 | How do frontier AI agents perform in multi-step cyber-attack scenarios? | PDF behind it added | `folkerts-2026-measuring-ai-agents` |
| 2026-03-23 | Can AI agents escape their sandboxes? A benchmark for safely measuring container breakout capabilities | had | `aisi-2026-sandbox-escape` |
| 2026-03-26 | How are AI Agents used? Evidence from 177,000 AI agent tools | had | `aisi-2026-mcp-tools` |
| 2026-03-31 | Harnessing frontier AI for cyber defence | not added | pointer to the joint NCSC/AISI blog, already in relata as `ncsc-2026-frontier-defenders` |
| 2026-04-13 | Our evaluation of Claude Mythos Preview’s cyber capabilities | had | `aisi-2026-mythos-preview-cyber` |
| 2026-04-20 | What can sandboxed AI agents learn about their evaluation environments? | had | `aisi-2026-sandbox-discovery` (+ its PDF attachment, added: `aisi-2026-openclaw-environment`) |
| 2026-04-24 | How do environmental factors impact AI behaviour? | had | `aisi-2026-propensity` |
| 2026-04-27 | Evaluating whether AI models would sabotage AI safety research | had | `aisi-2026-sabotage` |
| 2026-04-28 | Ask Don't Tell: Reducing Sycophancy in Large Language Models | PDF behind it added | `dubois-2026-ask-don-t` |
| 2026-04-30 | Our evaluation of OpenAI's GPT-5.5 cyber capabilities | added (web render) | `aisi-2026-gpt55-cyber` |
| 2026-05-05 | Partnering with Microsoft to strengthen frontier AI safety | not added | partnership announcement |
| 2026-05-13 | How fast is autonomous AI cyber capability advancing? | had | `aisi-2026-cyber-horizons` |
| 2026-05-21 | Will it become harder to oversee AI systems? | doc it introduces already in relata | `aisi-2026-loss-oversight` (the report PDF) |
| 2026-05-25 | Deepening our partnership with the Australian AI Safety Institute | not added | partnership announcement |
| 2026-06-08 | RealityTest: Do AI systems disclose their identity when asked? | PDF behind it added | `gausen-2026-realitytest-people-probe` |
| 2026-06-18 | Releasing AISI’s Engineering Playbook | not added | software/engineering practice release |
| 2026-06-30 | UK-Germany Joint Statement on advanced AI safety and security | not added | intergovernmental statement (GOV.UK lists DSIT, not AISI, as publisher). Judged out; borderline |
| 2026-07-02 | More compute, more capability: Why AI agent evaluations need to account for test-time compute | added (web render) | `aisi-2026-test-time-compute` |
| 2026-07-07 | Finding Cloud Misconfigurations with Frontier AI: A Case Study | added (web render) | `aisi-2026-cloud-misconfigurations` |
| 2026-07-17 | How Far Behind the Frontier are Leading Open Weight Models on Cyber? | had | `aisi-2026-open-weight-cyber` |
| 2026-07-21 | Cheating behaviour in frontier model evaluations | had | `aisi-2026-cheating` |
| 2026-07-23 | How our Control Red Team is stress-testing frontier monitors | had | `aisi-2026-control-red-team` |
| 2026-07-23 | International evaluation best practice and open questions in AI measurement | PDF behind it added | `intlnetwork-2026-best-practice-automated-evaluation` |
| 2026-07-23 | UK AISI / CAISI Preliminary Assessment of Kimi K3's Cyber Capabilities | had | `aisi-caisi-2026-kimi-k3` |
| 2026-08-04 | Incident Report: unsanctioned agent behaviour during cyber testing | had | `aisi-2026-incident-blog` (+ report PDF: `aisi-2026-incident`) |
| 2026-08-27 | Optimal stopping: spending evaluation compute where it counts | PDF behind it added | `pilditch-2026-knowing-stop-bayesian` |
| 2026-09-28 | GPT-6 Astra performs unsanctioned supply-chain attacks in simulations | PDF behind it added | `souly-2026-evaluating-whether-gpt` |
| 2026-10-01 | Building a more secure environment for evaluating dangerous capabilities | added (web render) | `aisi-2026-secure-eval-environment` |
| 2026-10-07 | Transect: Making large-scale agentic evaluations easier to understand | PDF behind it added | `pilditch-2026-transect-retaining-observability` |

**Which way I went on the borderline posts.** I added *Fourth progress report*, *Conference on frontier AI safety frameworks* (it describes the components of a safety framework), and *Advancing the field of systemic AI safety* (it defines "systemic AI safety"). For the three stub posts on the first, second and third progress reports, I rendered the GOV.UK full text, because these state the early risk scope. I left out *Our 2025 year in review*, *Why I joined AISI* (Irving) and the UK-Germany joint statement. Each is a one-command addition if Joseph wants it.

## 3. Other AISI PDFs: attachments, joint reports, GOV.UK

| Date | Document | Where AISI published it | Status | relata key |
|---|---|---|---|---|
| 2023-11 | *Introducing the AI Safety Institute* (CP 960) | GOV.UK (DSIT + AISI) | added | `dsit-2023-introducing-aisi` |
| 2024-05 | *International Scientific Report on the Safety of Advanced AI: Interim Report* (Bengio, chair) | GOV.UK (AISI secretariat) | added | `bengio-2024-iasr-interim` |
| 2024-10 | *AISI priority research areas for academic collaborations* (Gal, Kirk, Luketina, Davies, Korbak) | aisi.gov.uk, linked from *Our First Year* | added | `gal-2024-aisi-priority-research-areas` |
| 2024-11 | *US AISI and UK AISI Joint Pre-Deployment Test: Claude 3.5 Sonnet (Oct 2024)* (51 pp.) | aisi.gov.uk | added | `usaisi-ukaisi-2024-claude-35-sonnet` |
| 2024-12 | *US AISI and UK AISI Joint Pre-Deployment Test: OpenAI o1* (37 pp.) | aisi.gov.uk | added | `usaisi-ukaisi-2024-openai-o1` |
| 2024-12 | *Request for Evaluations and Agent Scaffolding: Extreme Risks from Frontier AI* (evals bounty) | aisi.gov.uk | added (Dec 4 version; a Nov 27 version differing in copy-edits and one dropped example is not registered) | `aisi-2024-evals-bounty-rfp` |
| 2025-02 | *Template for Evaluating Misuse Safeguards of Frontier AI Systems* | aisi.gov.uk | added | `aisi-2025-misuse-safeguards-template` |
| 2025-05 | *AISI Challenge Fund: Priority Research Areas* | aisi.gov.uk/grants | added | `aisi-2025-challenge-fund-priority-areas` |
| 2025-07 | *International Joint Testing Exercise: Agentic Testing* (99 pp.; International Network) | aisi.gov.uk | added. arXiv 2601.15679 is the same report and is not registered separately | `intlnetwork-2025-joint-testing-agentic` |
| 2025-07 | *AISI Protocol for Elicitation Experiments* | aisi.gov.uk | added | `aisi-2025-elicitation-protocol` |
| 2025-08 | *Open-weight model risk management checklist* | aisi.gov.uk | added | `aisi-2025-open-weight-checklist` |
| 2025-08 | *Technical guidance: sandboxing configurations for agentic evaluations* | AISI's GitHub (`aisi-sandboxing`) | added | `aisi-2025-sandboxing-technical-guidance` |
| 2025-12 | *UK AISI / Thorn Recommended Practice for AI-G CSEA Prevention* | aisi.gov.uk | added. The post links two files, created Dec 16 and Dec 18, whose texts differ. The Dec 18 file, the post's lead link, is attached | `aisi-thorn-2025-csea-recommended-practice` |
| 2026-02 | *What OpenClaw can learn from its environment* | aisi.gov.uk (attachment to the sandbox-discovery post) | added | `aisi-2026-openclaw-environment` |
| 2026-02 | *The Alignment Project: Funded Research Projects* | aisi.gov.uk | added (peripheral: a list of grants) | `aisi-2026-alignment-project-grants` |
| 2026-07 | *Best Practice: Automated Evaluation of Large Language Models* (International Network) | aisi.gov.uk | added | `intlnetwork-2026-best-practice-automated-evaluation` |
| | *Frontier AI Trends Report*, *Research Agenda*, *Loss of Oversight*, *Security Incident INC-2026-07-28-01* | aisi.gov.uk | had. The live AISI files are byte-identical to the relata copies | `aisi-2025-frontier`, `aisi-2025-research`, `aisi-2026-loss-oversight`, `aisi-2026-incident` |
| | International AI Safety Report 2025, its two Key Updates, IASR 2026 and its Extended Summary | (secretariat) | had | `bengio-2025-international`, `bengio-2025-iasr-key-update-1`, `-2`, `bengio-2026-international`, `bengio-2026-international-extended` |
| | Kimi K3 joint assessment (UK AISI / CAISI) | aisi.gov.uk, NIST | had | `aisi-caisi-2026-kimi-k3`, `nist-2026-aisi-caisi-kimi-k3` |
| | International Network consensus areas (Feb 2026) | NIST news page | had; the AISI blog post on it was added as a web render | `nist-2026-intl-network`, `aisi-2026-network-consensus` |

## 4. Other web pages added

| Date | Page | Why | relata key |
|---|---|---|---|
| 2025-07-10 | *White Box Control at UK AISI: Update on Sandbagging Investigations* (Alignment Forum) | the "paper" behind an AISI research entry | `aisi-2025-white-box-control-sandbagging` |
| undated | *The Alignment Project: Research Agenda* (alignmentproject.aisi.gov.uk) | AISI's statement of open alignment problems. The 11 research-area subpages were not rendered separately | `aisi-2025-alignment-project-agenda` |
| 2026-01-28 | *Assessment of AI capabilities and the impact on the UK labour market* (GOV.UK, AISI + DSIT) | capability and impact assessment | `aisi-2026-labour-market-assessment` |
| 2026-01-29 | *Secure AI infrastructure: call for information* (GOV.UK, DSIT + NCSC + AISI) | security threat framing for AI infrastructure | `aisi-2026-secure-ai-infrastructure-cfi` |

## 5. AISI-affiliated papers not listed on aisi.gov.uk

All of these are PDFs from arXiv. "How found" says why each counts as AISI work. Only risk-relevant papers were taken; see section 7 for the exclusions.

| Date | Title | arXiv | relata key | How found; notes |
|---|---|---|---|---|
| 2023-12-22 | Hazards from Increasingly Accessible Fine-Tuning of Downloadable Foundation Models | 2312.14751 | `chan-2023-hazards-increasingly-accessible` | OpenAlex affiliation |
| 2024-08-27 | How will advanced AI systems impact democracy? | 2409.06729 | `summerfield-2024-will-advanced-ai` | OpenAlex affiliation (journal version); preprint of Nature Human Behaviour 2025 (closed access); the preprint's title page does not name AISI |
| 2024-09-22 | A is for Absorption: Studying Feature Splitting and Absorption in Sparse Autoencoders | 2409.14507 | `chanin-2024-absorption-studying-feature` | AISI blog link: ukaisi-at-neurips-2025; arXiv title page gives LASR Labs; AISI lists it as its NeurIPS 2025 work; interpretability method, marginal to risk |
| 2024-10-14 | SeCodePLT: A Unified Platform for Evaluating the Security of Code GenAI | 2410.11096 | `nie-2024-secodeplt-unified-platform` | AISI blog link: ukaisi-at-neurips-2025 |
| 2024-10-29 | Towards evaluations-based safety cases for AI scheming | 2411.03336 | `balesni-2024-evaluations-based-safety` | OpenAlex affiliation |
| 2025-01-09 | Open Problems in Machine Unlearning for AI Safety | 2501.04952 | `barez-2025-open-problems-machine` | OpenAlex affiliation |
| 2025-01-19 | Tell me about yourself: LLMs are aware of their learned behaviors | 2501.11120 | `betley-2025-tell-me-about` | OpenAlex affiliation |
| 2025-02-24 | Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs | 2502.17424 | `betley-2025-emergent-misalignment-narrow` | OpenAlex affiliation; published in Nature 2026 (doi:10.1038/s41586-025-09937-5) |
| 2025-04-05 | Among Us: A Sandbox for Measuring and Detecting Agentic Deception | 2504.04072 | `golechha-2025-among-us-sandbox` | AISI blog link: ukaisi-at-neurips-2025; arXiv title page gives MATS; AISI lists it as its NeurIPS 2025 work |
| 2025-06-15 | ContextBench: Modifying Contexts for Targeted Latent Activation | 2506.15735 | `graham-2025-contextbench-modifying-contexts` | OpenAlex affiliation; ICLR 2026 |
| 2025-07-03 | Establishing Best Practices for Building Rigorous Agentic Benchmarks | 2507.02825 | `zhu-2025-establishing-best-practices` | AISI blog link: ukaisi-at-neurips-2025 |
| 2025-07-25 | Technological folie \`a deux: Feedback Loops Between AI Chatbots and Mental Illness | 2507.19218 | `dohnany-2025-technological-folie-deux` | OpenAlex affiliation; published in Nature Mental Health 2026 |
| 2025-09-08 | Measuring and mitigating overreliance to build human-compatible AI | 2509.08010 | `ibrahim-2025-measuring-mitigating-overreliance` | OpenAlex affiliation |
| 2025-11-03 | Measuring what Matters: Construct Validity in Large Language Model Benchmarks | 2511.04703 | `bean-2025-measuring-matters-construct` | AISI blog link: ukaisi-at-neurips-2025 |
| 2025-11-19 | People readily follow personal advice from AI but it does not improve their well-being | 2511.15352 | `luettgau-2025-people-readily-follow` | OpenAlex affiliation |
| 2025-12-01 | Neural steering vectors reveal dose and exposure-dependent impacts of human-AI relationships | 2512.01991 | `kirk-2025-neural-steering-vectors` | OpenAlex affiliation |
| 2025-12-08 | Auditing Games for Sandbagging | 2512.07810 | `taylor-2025-auditing-games-sandbagging` | AISI blog link: auditing-games-for-sandbagging-detection |
| 2025-12-31 | Do Large Language Models Know What They Are Capable Of? | 2512.24661 | `barkan-2025-large-language-models` | OpenAlex affiliation |
| 2026-01-27 | Disclosure By Design: Identity Transparency as a Behavioural Property of Conversational AI Models | 2603.16874 | `gausen-2026-disclosure-design-identity` | OpenAlex affiliation |
| 2026-02-01 | A clinically validated framework for auditing AI chatbot behavior in mental health interactions | 2602.01347 | `weilnhammer-2026-clinically-validated-framework` | OpenAlex affiliation; published in Nature Medicine 2026 |
| 2026-02-09 | Debate is efficient with your time | 2602.08630 | `browncohen-2026-debate-efficient-time` | OpenAlex affiliation |
| 2026-02-24 | When can we trust untrusted monitoring? A safety case sketch across collusion strategies | 2602.20628 | `gardnerchallis-2026-trust-untrusted-monitoring` | AISI blog link: how-our-new-control-red-team-is-stress-testing-frontier-monitors |
| 2026-03-16 | How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition | 2603.15714 | `dziemian-2026-vulnerable-ai-agents` | arXiv search; title page |
| 2026-04-09 | More Capable, Less Cooperative? When LLMs Fail At Zero-Cost Collaboration | 2604.07821 | `yadav-2026-more-capable-less` | OpenAlex affiliation |
| 2026-04-10 | Artificial intelligence can persuade people to take political actions | 2604.09200 | `hackenburg-2026-artificial-intelligence-persuade` | OpenAlex affiliation |
| 2026-04-24 | Measuring and Mitigating Persona Distortions from AI Writing Assistance | 2604.22503 | `rottger-2026-measuring-mitigating-persona` | OpenAlex affiliation |
| 2026-05-08 | Sycophantic AI makes human interaction feel more effortful and less satisfying over time | 2605.07912 | `ibrahim-2026-sycophantic-ai-makes` | OpenAlex affiliation |
| 2026-05-08 | Log analysis is necessary for credible evaluation of AI agents | 2605.08545 | `kirgis-2026-log-analysis-necessary` | OpenAlex affiliation |
| 2026-05-13 | PRISM-X: Experiments on Personalised Fine-Tuning with Human and Simulated Users | 2605.13307 | `kirk-2026-prism-x-experiments` | OpenAlex affiliation |
| 2026-05-19 | Open-World Evaluations for Measuring Frontier AI Capabilities | 2605.20520 | `kapoor-2026-open-world-evaluations` | OpenAlex affiliation |
| 2026-05-26 | Behavioural Analysis of Alignment Faking | 2605.27681 | `hadida-2026-behavioural-analysis-alignment` | OpenAlex affiliation |
| 2026-06-08 | EvalDetectBench: A Benchmark for Measuring Evaluation Awareness in Frontier Language Models | 2609.01611 | `li-2026-evaldetectbench-benchmark-measuring` | OpenAlex affiliation |
| 2026-06-09 | Forecasting Future Behavior as a Learning Task | 2606.11445 | `levy-2026-forecasting-future-behavior` | OpenAlex affiliation |
| 2026-06-15 | AI systems out-persuade expert humans | 2606.16475 | `hackenburg-2026-ai-systems-out` | OpenAlex affiliation |
| 2026-06-28 | SCARCE: Scalable Cascade Analysis for Rare-event Characterisation via Embeddings | 2606.29623 | `wang-2026-scarce-scalable-cascade` | OpenAlex affiliation |
| 2026-07-02 | Distributed Attacks in Persistent-State AI Control | 2607.02514 | `hills-2026-distributed-attacks-persistent` | OpenAlex affiliation |
| 2026-07-28 | Detecting CSAM Text-to-Image LoRAs From Weights | 2607.25750 | `africa-2026-detecting-csam-text` | OpenAlex affiliation |
| 2026-07-29 | Can AI agents conduct open-ended AI research? Early evidence from two case studies | 2607.27191 | `kirgis-2026-ai-agents-conduct` | OpenAlex affiliation |
| 2026-07-29 | Automated Transcript Analysis for Detecting Flaws in Agentic Benchmarks | 2607.27518 | `mohl-2026-automated-transcript-analysis` | OpenAlex affiliation |
| 2026-08-05 | Chain-of-Thought Monitoring Can Be Unreliable in Implicit-Influence Settings | 2608.04735 | `duzan-2026-chain-thought-monitoring` | OpenAlex affiliation |
| 2026-09-02 | Improving Evaluation Realism with Inference-Time Compute and Deployment Scaffolds | 2609.02302 | `ahlqvist-2026-improving-evaluation-realism` | OpenAlex affiliation |
| 2026-09-14 | Inoculation Midtraining with Learned Neologisms | 2609.15886 | `obrien-2026-inoculation-midtraining-learned` | OpenAlex affiliation |
| 2026-09-29 | Character Training for Risk-Averse Agents | 2609.38093 | `dhoot-2026-character-training-risk` | OpenAlex affiliation |

Three further AISI-affiliated works, not on arXiv:

| Date | Work | Status | relata key |
|---|---|---|---|
| 2024-10 | *Safety in Artificial Intelligence: Challenges and Opportunities for the U.S. National Labs and Beyond* (OSTI report; Gal and Alexander listed as UK AI Safety Institute) | PDF added from OSTI. Peripheral: a multi-institution workshop report | `dasilva-2024-safety-ai-national-labs` |
| 2025-10-07 | Gal & Casper, "Customizable AI systems that anyone can adapt bring big opportunities — and even bigger risks", *Nature* comment | **metadata only**: paywalled after the first paragraph | `gal-2025-customizable-ai-risks` |
| 2026 | Voudouris, Witte & Akata, *Judge Hacking in Recursive Debate Protocols: A Call for Solutions* (SSRN) | **metadata only**: SSRN refused automated download | `voudouris-2026-judge-hacking-debate` |

## 6. What I couldn't get

- **Gal & Casper, *Nature* comment (2025).** Paywalled after the first paragraph, although OpenAlex lists it as hybrid OA. Unpaywall found no OA PDF, and `doi.org` timed out. A logged-in browser or a library proxy would get it. The entry exists without a document.
- **Judge Hacking in Recursive Debate Protocols (SSRN 7046698).** SSRN blocks scripted downloads. Unpaywall found no OA copy, and `doi.org` returned nothing. The entry exists without a document.
- **The Thorn recommended practice, Dec 16 file.** Downloaded; not registered (the Dec 18 file is).
- **The OpenReview PDF of the preferences paper.** OpenReview served a bot challenge. Resolved by using arXiv 2602.18971.
- **Published journal versions** of several AISI papers, where relata holds the arXiv preprint. Not attempted, since most are closed access. The entry's `note:` names the published version where the arXiv record gives one (4 entries), and for the preferences and democracy papers. The Science persuasion paper (doi:10.1126/science.aea3884) corresponds to `hackenburg-2025-levers-political-persuasion`. Others: PNAS Nexus (political knowledge), Humanities and Social Sciences Communications (socioaffective alignment), Nature (emergent misalignment), Nature Mental Health (folie à deux), Nature Medicine (mental-health chatbot audit), and *Nature Human Behaviour* (democracy).

## 7. Judged out of scope

- **aisi.gov.uk pages:** 27 people pages, careers, privacy policy, the 14 category index pages, and `/about`. The *Trends Report* landing page is the report itself, already held. The 20 blog posts marked "not added" in section 2 are listed there with reasons: partnership announcements, software releases, event listings and pointer posts.
- **AISI grants administration PDFs:** the Challenge Fund Application Pack (June 2025) and Stage 2 Cost Guidance. Also the Alignment Project's application guidance, cost guidance and grant-agreement pages.
- **AISI-affiliated papers off the risk topic:** OpenAlex lists them, and their topic decided it.
  - *PACUTE* (Filipino tokenisation, 2606.15144);
  - *Compressibility Measures Complexity* (2510.12077);
  - *Compressed Computation is (probably) not Computation in Superposition* (2606.14673);
  - *Interactions Between Crosscoder Features* (2606.09940);
  - *From Mechanistic to Compositional Interpretability* (2605.08934);
  - *CivBench* (2609.02459);
  - *The Reversal Curse* (2309.12288; its later version carries a UK AISI affiliation, but it is a capability-generalisation result);
  - *Early Behavioral Markers of Loss of Financial Capacity* (JAMA Netw Open);
  - *Deep mechanism design* (PNAS);
  - *Learning Dynamics of Meta-Learning in Small Model Pretraining*.

  Interpretability theory is the closest call. If the gamma model needs AISI's interpretability line, the four interpretability papers above are the ones to add.
- **Not AISI's work, though found in the sweep:**
  - *StrongREJECT* (2402.10260) and *AI Sandbagging* (2406.07358), whose title pages carry no AISI affiliation;
  - the Korea/Singapore AISI data-leakage paper (2606.17114);
  - papers *about* AISIs (2407.20847, 2409.10536, 2409.11314, 2410.09219, 2503.04741);
  - Bloomfield & Rushby, *Where AI Assurance Might Go Wrong* (2502.03467), which is in the proceedings of AISI's Nov 2024 conference on frontier AI safety frameworks (FAISC 24). AISI hosted the conference; the authors are not AISI. I did not look for the rest of the FAISC 24 proceedings, and they may be worth a look.
  - Epoch AI's AI R&D automation interviews, which AISI cross-posted;
  - Anthropic's and OpenAI's posts on their safeguards collaboration with AISI and CAISI.

## 8. For Joseph

**Possible additions to `source-catalog.md`.** These are suggestions only; the catalog is unchanged. Of what was added, these look like main-source material for the model rather than supporting evidence:
- **`aisi-2025-misuse-safeguards-principles`** and its **template**: AISI's own vocabulary for safeguards and their evaluation.
- **`hilton-2025-safety-cases-scalable`**, with **`korbak-2025-sketch-ai-control`**, **`goemans-2024-safety-case-template`**, **`buhl-2025-alignment-safety-case`** and **`clymer-2025-example-safety-case`**. These are AISI's safety-case line, which uses argument structure for the controls stage of the chain.
- **`korbak-2025-evaluate-control-measures`**. The OVERVIEW already names AISI's control paradigm; this paper is AISI's own statement of it.
- **`usaisi-ukaisi-2024-claude-35-sonnet`** and **`usaisi-ukaisi-2024-openai-o1`**: the only published joint government pre-deployment evaluations.
- **`intlnetwork-2026-best-practice-automated-evaluation`** and **`intlnetwork-2025-joint-testing-agentic`**: the International Network's evaluation methodology.
- **`heitmann-2025-understanding-ai-trajectories`**: an explicit AISI model of capability limitations.
- **`souly-2026-uk-aisi-alignment`**, **`kirk-2026-evaluating-whether-ai`** and **`souly-2026-evaluating-whether-gpt`**. These are AISI's alignment and propensity evaluations. The GPT-6 Astra paper sits next to the incident report.
- **`aisi-2026-labour-market-assessment`**: AISI's only impact assessment.

**Observations about relata, for whoever stewards it.**
- **Duplicate-check.** The concurrent non-AISI agent and this sweep did not collide. I re-checked arXiv IDs and titles after every batch.
- **Validation.** `relata validate` reports 9 schema errors, all entries with no authors, none from this sweep.
- **`relata pdf --source`.** The field is free-form. For web renders I wrote `"<URL> (rendered 2026-10-09 by headless Chrome print-to-PDF, with provenance page)"`, so the render act is visible in the item record as well as on the provenance page.

## Working files

The download, render and enumeration files (sitemaps, page HTML, OpenAlex harvests, arXiv metadata, render script) are in the sweep agent's session scratchpad. They are not in this repository.
