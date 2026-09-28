# Source atlas: other companies' frontier safety frameworks, and analyses of the genre

Family: frameworks from Google DeepMind, Meta, Microsoft, Amazon, xAI, NAVER, G42, Cohere, NVIDIA, Magic and Shanghai AI Lab (several in successive versions), plus five analyses of frameworks as a genre (METR, Buhl et al., Stelling et al., Coggins et al., Zhu).

**How to read the references.** `L51–106` means lines 51–106 of `scratchpad/src-text/<key>.txt`. `p. 2` is the PDF page, computed by counting form-feeds: a line that begins with `\f` is the first line of the next page. A file that begins with `\f` has no text on its PDF page 1 (Shanghai). Page numbers printed in running footers usually agree with these; where a document has its own printed line numbers (Amazon 2026), those are not the file's line numbers.

**Garble conventions.** "2-col garble" means `pdftotext -layout` has interleaved two table or sidebar columns line by line. The words are all present, but a row reads across both columns. Nearly every threshold table in this family is garbled this way, so read those ranges from the PDF, or read the columns separately.

**Coverage, stated plainly.** I read these whole or nearly whole: GDM v1, v2, v3.0 and v3.1, the GDM blog, Meta 2025, Microsoft 2026, Amazon 2026, all three xAI texts (the 2025 FAIF through a word-level diff against the RMF plus targeted reads), both NAVER texts, G42, and Magic. I sampled the Gemini 3.7 Flash report (about half), Meta 2026 (about half), Microsoft 2025 and Amazon 2025 (read for differences from their successors), Cohere and NVIDIA (most), Shanghai (about a quarter), METR (about an eighth), Buhl (about a third), Coggins (most), Zhu (about half) and Stelling (front matter, method, parts of the results, discussion, glossary, and appendix samples; well under a tenth of its 15.6k lines). Where I say something changed between versions, I compared both texts myself.

---

## Google DeepMind / Google

### gdm-2024-fsf-v1-0 — Frontier Safety Framework, Version 1.0 (May 2024) — 342 lines, 7 pp.
- **TOC:** L34–41 (p. 1).
- **Glossary:** none. Definitions sit inline and in footnotes. CCL: L55–58 (p. 2). "Autonomy" and "effective compute": footnotes L96–105 (p. 2). "Capabilities include reasonably foreseeable fine-tuning and scaffolding": L209–211 (p. 4).
- **Passages:**
  - L51–106 (p. 2) — the three-part machinery (CCLs, early-warning evaluations every 6x effective compute or 3 months, response plans), with a hold clause at L84–88. The whole genre's skeleton in about 50 lines.
  - L111–198 (pp. 3–4) — security levels 0–4 mapped to RAND L3–L5, and deployment levels 0–3. Level 3 is "currently an open research problem" (L193–194): a commitment level with nothing behind it yet. 2-col garble.
  - L202–285 (pp. 4–6) — CCL table: domain / CCL / rationale. The rationale column carries the causal claims ("could significantly increase society's vulnerability to fatal attacks by malicious amateurs"). 3-col garble.
  - L289–323 (p. 6) — future work. "Misaligned AI" appears only as a future candidate (L311–313).

### gdm-2025-fsf-v2-0 — Frontier Safety Framework, Version 2.0 (4 Feb 2025) — 467 lines, 9 pp.
- **TOC:** L55–69 (p. 2).
- **Glossary:** none. Footnote definitions: misuse risk L50–51 and deceptive-alignment risk L53–54 (p. 1); safety case L216–218 and "general availability deployment" L220–221 (p. 4).
- **Passages:**
  - L1–54 (p. 1) — intro. L27–34 makes the commitment conditional on the rest of the industry: "our adoption of the protocols described in this Framework may depend on whether such organizations across the field adopt similar protocols." This sentence is gone from v3.0 (compare v3.0 L39–44).
  - L73–155 (pp. 2–3) — components. The "hold" is now hedged: "may involve putting deployment or further development on hold" (L144–149).
  - L222–318 (pp. 5–6) — Table 1: misuse CCLs with RAND security levels and a rationale that weighs "costs to innovation". Footnote 9 (L271–275) explains why the Autonomy domain was removed. The ML R&D CCL is anchored to "(e.g. 2x) from 2020-2024 rates" (L296–297); that anchor is gone in v3.0. 3-col garble.
  - L322–385 (pp. 6–7) — deceptive alignment: defined at L324; "we do not express any opinion here about how likely it is" (L325–326); Instrumental Reasoning levels 1 and 2; two safety-case claims (L377–384).
  - L388–463 (pp. 7–9) — governance, disclosure, future work, change note. The 21 March 2025 link-fix page (L457–463) marks this copy as a later re-upload (see Zhu App. K).

### gdm-2025-fsf-v3-0 — Frontier Safety Framework, Version 3.0 (22 Sep 2025) — 739 lines, 16 pp.
- **TOC:** L72–91 (p. 3).
- **Glossary:** none. Footnote definitions: misuse L60–61 and misalignment L63–65 (p. 2); safety case L261–262 (p. 6); "security level N" L368–373 (p. 8); "relative to a baseline without generative AI" L486 (p. 10).
- **Passages:**
  - L99–215 (pp. 4–6) — scope, CCL definition, the risk-assessment process. The ML R&D note (L198–215) argues the company may use its own internal progress as the information source, because "we do not expect other groups to put significantly more effort into ML R&D than we do ourselves."
  - L250–316 (pp. 6–7) — §1.6 risk acceptance criteria: a model "will be deemed to pose an acceptable level of risk ... if, for example:", with marginal-risk reasoning against other public models (L274–285). Closes with a frank note (L302–307): "our assessments will often involve some level of subjective analysis."
  - L339–425 (pp. 8–9) — deployment-mitigation safety-case factors i–v. Factor iv makes acceptability depend on what other developers' models do (L386–390). L404–409: "reliably prevent models posing unacceptable levels of risk from being deployed" (v3.1 drops "reliably").
  - L469–508 (pp. 10–11) — Harmful Manipulation CCL (exploratory). Garbled.
  - L593–692 (pp. 13–15) — ML R&D CCLs (now "from historical rates", L604–608), and the misalignment section labelled "illustrative only".
  - L700–735 (p. 16) — updates (annual, and "appropriateness for the management of systemic risk", EU-flavoured) and disclosures.

### gdm-2026-fsf-v3-1 — Frontier Safety Framework, Version 3.1 (17 Apr 2026) — 960 lines, 20 pp.
- **TOC:** L74–105 (p. 3).
- **Glossary:** L822–957 (pp. 18–20), the first in the series. Grouped under Model / Risk Domains / Thresholds / Inherent Risk Assessment / Risk Mitigation / Residual Risk Assessment. "Frontier AI Models" (L824–831) is defined partly relative to "other Google models".
- **Passages:**
  - L127–160 (p. 4) — CCLs plus the new Tracked Capability Levels: "significant but not severe".
  - L167–243 (pp. 5–6) — risk identification, inherent risk assessment and material-capability-change assessment. ISO-style vocabulary now structures the document. Footnote 4 (L215–218) exempts "low-risk external deployments".
  - L290–359 (pp. 7–8) — risk acceptance determination. v3.0's "if, for example:" is now "if:". A TCL can also be accepted if "the model is very unlikely to possess the propensities" (L345–346).
  - L664–690 (p. 14) — the Stealth and Situational Awareness TCL, which replaces Instrumental Reasoning L1. Misalignment is folded into "ML R&D and Misalignment".
  - L800–814 (p. 17) — the in-document change list for 3.1.

### gdm-2026-strengthening-fsf-blog — "Strengthening our Frontier Safety Framework" (22 Sep 2025, updated 17 Apr 2026) — 179 lines, 8 pp.
- **TOC / glossary:** none. The CCL footnote is at L108–110.
- **Read whole:** L1–110 (pp. 1–4). L111–179 is site navigation.
- **What's distinctive:** the announcement's own gloss of the framework. It paraphrases misalignment as "interfere with operators' ability to direct, modify or shut down" (L45–47) and the instrumental-reasoning CCLs as "when an AI model starts to think deceptively" (L49–51), neither of which is the framework's wording. It says CCL definitions were "sharpened" (L68–70), which is the same revision that dropped the "2x" anchor (Zhu L433–436). The 2026 update is appended in place (L79–85).

### gdm-2026-gemini-3-7-flash-fsf-report — Gemini 3.7 Flash Frontier Safety Framework Report (Aug 2026) — 1703 lines, 41 pp.
- **TOC:** none.
- **Glossary:** none. Each domain opens with a box quoting the threshold definitions verbatim: L218–230, L751–754, L1336–1351.
- **Passages** (the only document in this family that reports measurements and narrates model behaviour):
  - L9–130 (pp. 2–4) — framing, the results table (4-col garble), and the determination rule: a safety margin (the ML R&D bar is 100% "but we conservatively set our safety margin at 90%"), and the category "cannot rule out being at the T/CCL" (L121–129).
  - L135–211 (pp. 5–6) — elicitation and sandbagging checks. The model mistook a sabotage task for an "alignment" evaluation and refused (L173–186). External evaluators "have their own taxonomies of harm ... Our subject matter experts review, translate, and integrate these results" (L202–206).
  - L234–330 and L395–474 (pp. 7–12) — CBRN threat modelling (threat-actor profiles, Delphi, harm journeys, web-only baselines), results (+8.0 and +12.1 points over web baselines), an RCT (n=153) used as a "lower-bound", and the real-world bottlenecks not measured (L314–320).
  - L750–900 (pp. 19–22) — harmful manipulation: three-phase threat model, human-behaviour RCT (n=1596, odds ratios), ethics committee, statistical-power caveat.
  - L1335–1461 (pp. 34–36) — ML R&D and misalignment threat models. "Due to a lack of an empirical evidence base ... we brainstormed" (L1387–1394). Instrumental vs intrinsic risk (L1443–1444). "Scheming (also known as deceptive alignment)" (L1447–1449).
  - L1596–1698 (pp. 39–41) — stealth and situational-awareness results. A refusal is scored as propensity rather than capability. Failure narratives (faulty_tool, read_logs). Stated limitations include "severe disanalogies between AIs and humans" (L1672–1675).

### google-2026-ai-responsibility-update — Google Responsible AI Progress Report (Feb 2026) — 656 lines, 16 pp.
- **Badly garbled.** A magazine layout: 2–4 columns interleaved line by line through most pages (e.g. L6–39, L45–85, L199–230, L355–370, L465–540). Read it from the PDF.
- **TOC / glossary:** none.
- **Register:** a promotional progress report. It asserts process quality ("rigorous", "most secure model yet") and gives counts, not measurements (e.g. the red team completed "over 350 exercises", around L258).
- **Passages** (ranges are approximate because of the interleaving):
  - L136–182 (p. 5) — the Chrome-agent safeguards. The right-hand column is fairly clean. It introduces a "User Alignment Critic ... vetoing actions that do not align with the user's specific intent" (L147–151): "alignment" in the user-intent sense.
  - L106–131 (p. 4) — Gemini 3 / FSF case study (2-col).
  - L192–230 (p. 6) — AGI and agents research summary (3-col).

---

## Meta

### meta-2025-frontier-ai-framework — Frontier AI Framework, Version 1.1 (Feb 2025) — 1179 lines, 21 pp.
- **TOC:** "How to read this document" L50–85 (p. 3), section names without page numbers.
- **Glossary:** Appendix – terminology, L1063–1174 (pp. 20–21). It opens with a disclaimer that "there is a lack of consensus as to how to define some of these terms" (L1065–1069). The load-bearing entry is "Uniquely enabling" (L1094–1097).
- **Formatting:** several pages are double-spaced (a blank line between every text line); tables are 3-col garbled with letter-spaced headers.
- **Passages:**
  - L422–545 (pp. 9–11) — the outcomes-led approach: catastrophic outcomes, causal pathways, "uniquely enable". Footnote 4 at L438 reads "OpenAI former, GDM latter", a drafting note left in the published text. Footnote 5 (L486–488) admits "unknown unknowns".
  - L550–706 (pp. 12–13) — four inclusion criteria (Plausible / Catastrophic / Net new / Instantaneous or irremediable) and Table 1 (thresholds → security → measures; garbled). Footnote 7 (L699–705): "the science of evaluation is not sufficiently robust as to provide definitive quantitative metrics for uplift", so senior decision-makers decide.
  - L711–863 (pp. 14–15) — outcome / threat scenario / enabling-capability tables for cyber and chemical/biological. 3-col garble, but these tables are the document's core ontology.
  - L881–1020 (pp. 16–18) — the "absence validation test", evaluation in release context, and the benefits assessment ("impossible to eliminate subjectivity", L1008).
- **Version note:** this copy is Meta's 28 Mar 2025 re-upload, still labelled v1.1: "closed deployment" at L296 and "e.g." at L567 match Zhu App. K.

### meta-2026-advanced-ai-scaling-framework — Advanced AI Scaling Framework, Version 2 (7 Apr 2026) — 1705 lines, 44 pp.
- **TOC:** "How to read" L34–56 (p. 2).
- **Glossary:** Appendix I – Terminology, L1573–1661 (pp. 41–43). "Frontier AI" now means capability-based or ≥10^26 FLOP. "Substantially contribute" (a "material factor") sits beside "Uniquely enabling" (an "essential controlling factor") at L1616–1620. The change log (Appendix II, L1667–1700, p. 44) says plainly that the critical threshold went from "Stop" to "Develop with Mitigations" and that "uniquely enable" was replaced by "substantially contribute to".
- **Opening:** L4–6 (p. 1), "personal superintelligence to everyone".
- **Passages:**
  - L252–337 (pp. 7–9) — the commitments about preparedness reports. They include disclosing "evidence that the training process may cause obfuscation of a model's reasoning" and behaviours such as "reward hacking or scheming" (L315–321).
  - L507–570 (pp. 15–16) — Table 1, the new thresholds (garbled 3-col), and aggregation "across a diverse set of threat scenarios".
  - L794–902 (pp. 22–24) — Loss of Control as a risk domain, defined through failures of control mechanisms. Footnote 4 (L825–830) is the definition: "humans lose—and cannot feasibly regain—the ability to direct, modify, contain, or shut down". Footnote 5 (L832–836) is a stipulated premise: "we assume that catastrophic harm would eventually materialize". The LoC1/LoC2 scenario table is garbled.
  - L1285–1397 (pp. 33–36) — LoC evaluation: capability checkpoint, then enhanced evaluation. Propensity acceptance criteria "at least 40% on MASK and at most 50% on Agent Misalignment" (L1358–1359). Footnote 8 (L1365–1373) makes "substantially accelerating" operational as benchmark saturation within six months.
  - L1398–1496 (pp. 36–38) — "emerging" outcomes. Radiological/nuclear is set aside because "materials access is a strong bottleneck". Physical autonomy gets a proposed rule-out test. Gradual loss of human oversight through "skill atrophy", and loss of containment.

---

## Microsoft

### microsoft-2025-frontier-governance-framework — Frontier Governance Framework, Version 1 (Feb 2025) — 597 lines, 15 pp.
- **TOC:** L3–32 (p. 2).
- **Glossary:** none. Footnote 2 (L194–195, p. 6) defines "frontier capabilities". Capability thresholds are Appendix I, L429–590 (pp. 12–14): CBRN, cyber and autonomy only.
- **Read it for its differences from 2026:** a 10^26-FLOP pre-training trigger (L155–161, p. 5); deeper assessment "at least once every six months" (L238–240, p. 7); framework review "Every six months" (L388, p. 10). The change log (L591–592) is one line. This copy has no broken text runs, so it is the 26 Feb 2025 re-upload (Zhu App. K).

### microsoft-2026-frontier-governance-framework — Frontier Governance Framework (Feb 2026) — 681 lines, 16 pp.
- **TOC:** L3–34 (p. 2).
- **Glossary:** none. The tracked capabilities are defined as a list at L90–106 (p. 4). "Loss of control" is defined as a model *ability*: "such that ... a model can no longer be reliably directed, modified, or shut down" (L101–103).
- **Passages:**
  - L35–112 (pp. 3–4) — principles and the tracked-capability definitions.
  - L156–266 (pp. 5–7) — leading indicators. Scope is now set by law: models "in scope ... under applicable laws, such as the EU AI Act, ... TFAIA, ... RAISE" (L171–173). Fine-tuning at 1/3 of base compute. Benchmark inclusion criteria (footnote, L201–204). A "holistic risk assessment" that credits marginal uplift over open-weight models (L248–254). Deeper assessment now happens only "if there are material changes" (L256–259).
  - L272–367 (pp. 8–9) — security and safety mitigations, and a pause clause (L363–367).
  - L371–411 (p. 10) — deployment governance. The case has three claims, one of them "the marginal benefits of a model outweigh any residual risk" (L376–378). Executives attest to a "good faith attempt" (L380–384). Review cadence is "at least every twelve months" (L405–411).
  - L468–649 (pp. 12–15) — Appendix I thresholds as a grid of actor skill × uplift (garbled). LoC and manipulation are "we are studying" placeholders (L631–649).
  - L655–677 (p. 16) — the change log names the EU Code of Practice, RAISE and TFAIA as drivers. It lists the cadence changes but gives no direction for them.

---

## Amazon

### amazon-2025-frontier-model-safety-framework — Frontier Model Safety Framework (Feb 2025) — 455 lines, 8 pp.
- **TOC / glossary:** none. Uplift is defined in footnote 2, L100–105 (p. 2).
- **Passages:**
  - L1–106 (pp. 1–2) — intro and three Critical Capability Thresholds (CBRN, cyber, Automated AI R&D). The counterfactual for uplift is "other publicly available research or existing tools, such as internet search" (L59, L64).
  - L107–171 (pp. 3–4) — evaluation types ("maximal capability evaluations", then a "safeguards evaluation") and mitigations.
  - Most of the rest is the Appendix A security boilerplate.

### amazon-2026-frontier-model-safety-framework — Frontier Model Safety Framework (2026) — 621 lines, 11 pp.
- **Note:** the PDF prints its own line numbers (1–415) at the start of lines. The references here are file lines.
- **TOC / glossary:** none. "Harness" is defined inline at L72–73 (p. 2).
- **Passages:**
  - L1–137 (pp. 1–3) — four domains (CBRN, cyber, harmful manipulation, loss of control). The uplift baseline has become "beyond other publicly available models in known harnesses" (L71–72, L79). In 2025 it was internet search: the counterfactual moved. LoC is L122–137.
  - L194–299 (pp. 4–6) — abuse, security, and new "Misalignment Safeguards" (L274–288): "we identify a model persona that ensures that the model emphasizes ethical practices."
  - L349–378 (pp. 6–7) — governance: a go/no-go decision by the SVP and the CSO.
  - L385–~600 (pp. 8–11) — Appendix A, security practices.

---

## xAI

### xai-2025-rmf — Risk Management Framework (20 Aug 2025) — 428 lines, 9 pp. Read whole.
- **TOC / glossary:** none.
- **What's distinctive:**
  - Risk is organised by model *behaviours* in three buckets: abuse potential, concerning propensities, dual-use capabilities (L30–38).
  - Public deployment on X is cited as monitoring (L64–68, L304–309).
  - The acceptance criteria are numeric: fewer than 1 answer in 20 on restricted bio/chem queries (L220–223, p. 5), and a dishonesty rate under 1 in 2 on MASK (L311–313, p. 7).
  - "Catastrophic" is defined as more than 100 deaths or more than $1B (L95–98).
  - "Incidental alignment ... our models naturally tend to refuse" (L227–232).
  - Loss of control is framed as "speculative", with a "superintelligent AI ... wreak havoc" example (L53–62, L254–267).
  - Radiological and nuclear risk is dismissed on the strength of the nonproliferation regime (L204–210).
  - Benefits can outweigh risks for defenders (L415–423).
- **Version note:** "AISI" is absent at L198–199, so this is the 22 Aug re-upload (Zhu App. K).

### xai-2025-faif — Frontier Artificial Intelligence Framework (30 Dec 2025) — 480 lines, 11 pp.
- **What it is:** a word-level diff shows this is the RMF relabelled for California compliance: "This FAIF complies with ... TFAIA" (L11–12).
- **What changed:** TFAIA's definition of Catastrophic Risk is quoted in footnote 1 (L31–44, p. 1): more than 50 people or $1B, and clause (C) "Evading the control of its frontier developer or user". It replaces xAI's own "more than 100 deaths". NIST and ISO references are added (L60–63). A "Governance Approach" section with risk owners and X-platform monitoring (L376–405, p. 9). An AB-2013 "Data Disclosure" is appended (L435–480, pp. 10–11).
- **Retained:** the numeric thresholds.

### xai-2026-faif — Frontier Artificial Intelligence Framework (effective 30 Jun 2026) — 410 lines, 9 pp.
- **What it is:** a rewrite in numbered sections using the EU Code of Practice's vocabulary ("systemic risk", "making available on the market", "post-market monitoring"). Footnotes 1 and 2 (L40–42, L90–92) name the Code as the source of the terminology.
- **What's gone** (checked with grep): every named benchmark, both numeric thresholds, and the TFAIA definition. The law-enforcement-notification step is also gone from the incident list (L373–397). "Risk tiers" are mentioned (L253) but never given. There is no change log. A typo, "CRBN", at L314.
- **Passages:**
  - L1–112 (pp. 1–3) — intro and risk identification: four domains, and a taxonomy procedure (a–d).
  - L113–200 (pp. 3–5) — per-domain paragraphs. A present-tense capability claim sits inside a policy: "Frontier models embodied in agentic harnesses are already capable of ... meaningful uplift" (L175–182).
  - L203–275 (pp. 5–6) — systemic-risk analysis (five information sources) and acceptance, with no numbers.

---

## NAVER

### naver-2024-asf — NAVER AI Safety Framework (web page, Jun/Aug 2024) — 408 lines, 13 pp.
- **Note:** L1–3 are a relata PROVENANCE header, not source text. The page body is double-spaced; L354–408 is site navigation.
- **TOC / glossary:** none. Read whole: L4–350 (pp. 2–9).
- **What's distinctive:**
  - Loss of control is defined as "AI systems causing severe disempowerment of the human species" (L69–78, pp. 3–4).
  - A three-tier AI typology (hyper-scale / frontier / future) with a "6x performance" re-evaluation trigger (L124–169; the table is garbled).
  - A use-case × need-for-guardrails matrix (L173–272, pp. 5–7; garbled 2×2).
  - Korean-language safety datasets (L273–293).

### naver-2026-asf2 — AI Safety Framework 2.0 (7 Jul 2026) — 446 lines, 14 pp.
- **TOC:** L11–45 (p. 2).
- **Glossary:** none.
- **Garble:** pages 4–6, 8–9 and 12 are 2-col garbled (sidebars).
- **What's distinctive:** a reframing away from frontier-model catastrophic risk towards "service-centered" safety for "On-Service AI" (L62–69, L77–104). The taxonomy is 3 subjects of protection (users, members of society, AI service ecosystem) × 3 protected values (life and physical safety, economic value, preventing unjust discrimination) (L147–219, pp. 6–7). The "special domain" is "High-Impact AI" under Korea's AI Basic Act (L258–260). A three-layer governance table (L360–384).
- **What's absent** (grep): "loss of control", "catastrophic", and "disempowerment" no longer appear. "Frontier" appears once, looking back (L58).

---

## G42

### g42-2025-frontier — Frontier AI Safety Framework (Feb 2025) — 523 lines, 14 pp.
- **TOC:** L2–16 (p. 2).
- **Glossary:** none.
- **Passages:**
  - L53–130 (pp. 4–5) — how the thresholds were chosen (with METR and SaferAI). "Near miss" incidents are an input for review (L84–86). **Presumption by comparison** (L88–94): if a G42 model scores below an outside model that has been judged to be below the threshold, it is presumed below. It relies on upstream evaluations when fine-tuning open models (L104–110). Testing in Arabic and Hindi (L101–102).
  - L132–196 (pp. 5–7) — the threshold table (bio, including biological design tools; cyber). 3-col garble.
  - L199–302 (pp. 7–9) — Deployment Mitigation Levels, each with an adversary-strength objective ("even a determined actor", "support from state programs"). Garbled.
  - L400–518 (pp. 11–14) — governance and audits; disclosure to the UAE Government (L444–447); a phased implementation with time horizons; a self-promotional conclusion ("pioneering force").

---

## Cohere

### cohere-2025-secure — The Cohere Secure AI Frontier Model Framework, V1.0 — 784 lines, 19 pp.
- **TOC:** none. The "framework at a glance" table (L100–143, pp. 4–5; 2-col garble) serves as one.
- **Glossary:** none. "Model capabilities" has an idiosyncratic definition (L174–176, p. 6): risks that are likely given what LLMs do well, plus their limitations.
- **Passages:**
  - L52–86 (p. 3) — boxed text: enterprise risk vs consumer risk, and "safe for use" = safe + secure.
  - L157–290 (pp. 5–8) — risk identification and a likelihood/severity table judged in enterprise context (e.g. CSAM is "Low in enterprise contexts"). 4-col garble.
  - L561–615 (pp. 14–15) — **an explicit argument against the genre's catastrophic-threshold approach.** It calls those risks "speculated"; says the studies are "limited in their methodological maturity"; says biorisk studies "fail to account for entire risk chains". Cohere instead focuses on risks "known, measurable, or observable today". Final authority is delegated by the CEO to the Chief Scientist.
  - L621–644 (p. 16) — the acceptance "bright line" is no significant regression against the previous model (L632–638): a relative criterion. The paragraph at L640–643 repeats L623–628, a drafting duplicate.

---

## NVIDIA

### nvidia-2025-frontier — Frontier AI Risk Assessment (applicable from Aug 2025; named authors) — 630 lines, 15 pp.
- **TOC / glossary:** none. Inline definitions: frontier model L23–25 (p. 1); system L143–145 (p. 5); ODD L177–183 (p. 5); risk L203–205 (p. 6). It reads like a paper, with 55 literature footnotes.
- **Passages:**
  - L10–94 (pp. 1–3) — the abstract says frontier models are "not currently under development at NVIDIA" (L14–15). The Preliminary Risk Assessment uses an MR1–MR5 grid over use case × capability × autonomy (L56–69, garbled), argued to be a better proxy than compute thresholds (L89–94).
  - L175–212 (pp. 5–6) — ODD; MR5 can be lowered by restricting the use case (L184–190). That sits uneasily with L89 ("should not be reduced through typical risk mitigation"). The risk formula follows (L203–212).
  - L220–295 (pp. 7–8) — Table 1: multiplicative scoring on a 1–64 scale. Hazards include "at-scale discrimination" as a frontier hazard (L261–268). Table 2 works an example: disinformation risk 49 → 5.
  - L460–534 (pp. 12–13) — benchmarks repurposed (MoleculeNet for toxic compounds, ARC for unintended capabilities) and Garak.
  - L576–617 (pp. 14–15) — "an assessment with 50% confidence" during development vs 95–99% for the model card (L578–581); interviews as qualitative governance.

---

## Magic

### magic-2024-agi-readiness — AGI Readiness Policy, v1.0 (2 Jul 2024; web snapshot) — 263 lines, 8 pp. Read whole.
- **Note:** L1–3 are the relata PROVENANCE header. The live page carries "This policy is outdated. We're working on an update." (L9).
- **TOC / glossary:** none. "Threat models" is defined at L128–129 (p. 5). Read whole: L14–257.
- **What's distinctive:**
  - It is a commitment to *write* commitments: exceeding 50% on LiveCodeBench triggers "a full system of dangerous capabilities evaluations" (L65–69, p. 3). The threshold is calibrated against named competitors' scores as of May 2024 (L53–63): a threshold indexed to a moment in time.
  - A private-benchmark trigger relative to other companies' public models (L71–80).
  - Development halts if the evaluations aren't ready (L100–105).
  - The threshold "may [be] update[d] upward" if evidence shows it is "safe ... to freely proliferate" (L116–124).
  - A threat-model table with quantified uplift ("reduced by at least 10x", "3 months and $1m in compute") at L160–190 (p. 6), 2-col garble.

---

## Shanghai AI Lab

### shanghaiailab-2025-frontier — Frontier AI Risk Management Framework v1.0 (Jul 2025, with Concordia AI) — 2719 lines, 54 pp.
- **Note:** the file begins with `\f`, so L1 is on p. 2.
- **TOC:** "Table of Content" L131–189 (pp. 5–6).
- **Glossary:** Appendix I Key Definitions, L2038–2136 (pp. 42–43); footnote 73 says it is "primarily based on the International AI Safety Report". Appendix III (L2529–2719, pp. 50–54) is a second definitions list: capabilities, propensities, deployment characteristics.
- **Register:** guidance addressed to *other* developers ("we recommend that model developers ..."). It cites ISO 31000, GB/T 24353 and TC260.
- **Passages:**
  - L195–283 (pp. 7–8) — six stages, and the E-T-C dimensions (Deployment Environment, Threat Source, Enabling Capability).
  - L294–423 (pp. 9–11) — scope criteria, named example models, and a four-domain table keyed by *threat source* (misuse / loss of control / accident / systemic). "Tech-Institutional Misalignment" is the threat source for systemic risk; LoC distinguishes passive from active (L375–380). Garbled.
  - L698–768 (pp. 16–17) — red lines ("absolute", set by "expert consensus") vs yellow lines. Footnote 25 gives the expert-evaluation criteria.
  - L1025–1105 (pp. 23–24) — hypothetical LoC red-line scenarios L1/L2 (a 5-col table, heavily garbled).
  - L1373–1445 (pp. 30–31) — green / yellow / red zones mapped to ISO risk-treatment options.
  - L2529–2620 (pp. 50–51) — capability and propensity definitions (scheming, self-preservation, goal expansion).

---

## Analyses of frameworks as a genre

### metr-2025-common-elements — Common Elements of Frontier AI Safety Policies (Dec 2025 update of Aug 2024) — 3266 lines, 64 pp.
- **TOC:** none. Section starts: Bio L425, Cyber L656, AI R&D L892, Additional threat models L1058, Weight security L1215, Deployment mitigations L1540, Halting deployment L1940, Halting development L2124, Elicitation L2262, Timing L2408, Accountability L2622, Updating L3045, Conclusion L3250.
- **Glossary:** none. The nine elements are defined at L83–122 (pp. 3–4); threat-model glosses, including "Deceptive alignment", are at L330–364 (pp. 8–9).
- **Mode:** mostly verbatim excerpts from the policies, with page citations, stacked by element and followed by "Relevant regulatory guidance" boxes (EU Code of Practice, SB 53). METR's own voice is thin.
- **Passages:**
  - L12–56 (p. 2) — summary. Footnote 1 (L51–56): "descriptive, not prescriptive ... a gap ... does not necessarily indicate noncompliance". L44 still says "all three policies", a leftover from the 2024 original.
  - L63–185 (pp. 3–5) — the 12 policies and the versions cited (GDM v3.0, Meta v1.1, xAI RMF), and Table 1 presence counts (garbled).
  - L373–470 (pp. 10–11) — Table 2, METR's own classification of each policy's threat models, and the bio intro. METR's claims about present-day capability ("Current language models are able to provide detailed advice relevant to creating a biological weapon", L426–433) come framed as background.
  - L596–652 (p. 14) — a typical excerpt stack plus the CoP and SB 53 boxes.
  - L1058–1110 (p. 22) — additional threat models (manipulation, misalignment, ARA, LoC), all through quotation.

### buhl-2025-emerging — Emerging Practices in Frontier AI Safety Frameworks (Buhl, Bucknall, Masterson; UK AISI; pre-Paris 2025) — 1588 lines, 38 pp.
- **TOC:** none. Table 1 (L86–186, pp. 3–5; 4-col garble) maps area → component → FAISC quote → practices.
- **Glossary:** List of acronyms only (L1281–1305, p. 32). "Frontier AI" is defined in footnote 1 (L78–81). Threshold types are at L333–364 (p. 9): risk vs capability thresholds, plus a footnote on outcome, compute and benchmark thresholds.
- **Mode:** normative synthesis in "can", "could", "may be useful". Each component follows the same pattern: Description / Emerging practices / Examples, with a table of verbatim quotes from pre-2025 framework versions.
- **Passages:**
  - L1–81 (pp. 1–2) — purpose, and the "if-then commitments" framing (L65–67).
  - L196–320 (pp. 6–8) — risk-domain identification and risk modelling (fishbone, bow-tie, counterfactual contribution of AI), with quoted examples.
  - L326–435 (pp. 9–11) — thresholds: "no currently published safety framework sets explicit risk thresholds" (L373). Pre-committing prevents thresholds being "retroactively fit" (L378–382). Risk thresholds are "a normative question in the interest of all of society" (L383–385).
  - L823–870 (pp. 20–21) — conditions for safe development, safety cases, and a quoted governance chain.

### stelling-2025-evaluating — Evaluating AI Providers' Frontier Safety Frameworks (SaferAI; arXiv v5, 30 Apr 2026) — 15619 lines, 231 pp.
- **TOC:** L149–213 (pp. 5–6). Also "How To Read This Report", L48–56 (p. 2).
- **Glossary:** L1862–1931 (pp. 35–36). It includes KRI/KCI, risk tolerance ("probability × severity per unit time"), and assurance processes. Appendix B, Criteria in Full Detail (from L2414, p. 45), defines each of the 65 criteria.
- **Structure:** main text L1–1861 (pp. 1–34). Appendix A score tables start at L2138 (p. 41); the provider column headers did not survive extraction. C.1 summaries start at L2817 (p. 51). **C.2 full scores**, organised per provider with score, rationale, quote and page:
  - Amazon L3167 (p. 58)
  - Anthropic L4189 (p. 72)
  - Cohere L5282 (p. 87)
  - G42 L6208 (p. 100)
  - Google DeepMind L7254 (p. 115)
  - Magic L8636 (p. 134)
  - Meta L9560 (p. 147)
  - Microsoft L10621 (p. 162)
  - Naver L11570 (p. 175)
  - NVIDIA L12236 (p. 185)
  - OpenAI L13251 (p. 199)
  - xAI L14526 (p. 217)
- **Passages:**
  - L19–133 (pp. 1–4) — abstract and executive summary: median 18%, "peer ceiling" 54%, and the claim that discretionary language limits accountability.
  - L490–545 (pp. 11–12) — the scoring scale (0/10/25/50/75/90/100) and the rule that "discretionary language (e.g. 'we may consider' rather than 'we will') scores lower". This is how commitment strength becomes a number.
  - L854–900 (pp. 17–18) — risk tolerance results. xAI is credited for ">100 deaths", which was already superseded in xAI's Dec 2025 FAIF: the analysis is pinned to earlier versions.
  - L1553–1603 (pp. 29–30) — "commitments have sometimes weakened": Table 9, xAI Feb→Aug 2025 changes, with quotes.
  - L1696–1731 (p. 32) — discretion; thresholds measured "relative to competitors"; "developing" mitigations rather than specifying them.
  - L3167–3290 (pp. 58–59) — a sample of C.2 (Amazon): the grain of the 780 provider-criterion pairs.

### coggins-2025-preparedness — "The 2025 OpenAI Preparedness Framework does not guarantee any AI risk mitigation practices" (Coggins et al.) — 840 lines, 19 pp.
- **Scope:** it analyses only OpenAI's Preparedness Framework v2 (Apr 2025). It is in this family because of its method.
- **TOC / glossary:** none. Table 1 (L214–236, p. 5) defines the vocabulary of modal force: allow / encourage–discourage / request / demand / refuse ("demand" and "refuse" "cannot be worked around"). Actors are defined by quoting the PF (L246–259).
- **Mode:** an adversarial reading through affordance theory from science and technology studies. It codes each PF clause by force, with some rhetoric ("materially nothing more ... than a PDF file", L290, L364, L517).
- **Passages:**
  - L1–92 (pp. 1–2) — abstract, key findings, plain-language summary.
  - L155–236 (pp. 4–5) — method: the MIT AI Risk Repository (7 domains / 24 subdomains) and the Mechanisms & Conditions model.
  - L293–428 (pp. 7–10) — Table 2, PF priorities mapped onto the MIT taxonomy ("Allows evaluation" for 21 of 24). Tables 3 and 4 code clauses by mechanism (garbled 2–3 col).
  - L430–520 (pp. 10–12) — results 2–3 and discussion. It links persuasion capability to alleged deaths (L504–508) and cites Article 5 of the EU AI Act.

### zhu-2026-silent — Silent Revision: Measuring Undisclosed Change in the Safety Frameworks of Frontier AI Developers (Zhu; arXiv 8 Sep 2026) — 1490 lines, 27 pp.
- **TOC:** none.
- **Glossary:** Appendix A, L696–735 (p. 13). **Codebook** Appendix B, L737–828 (pp. 13–15):
  - the inclusion rule: present-tense descriptions count as commitments "at the strongest rung"; statements "describing the risk landscape, defining terms" are excluded (L747–752);
  - categories EC1–EC6 and G/S/M;
  - outcomes R/S/W/X/L/A;
  - six dimensions of materiality;
  - the modal ladder "must / will / commit to / present-tense > intend / aim / expect > may / could / consider > recommend / encourage" (L781–788).
- **Passages:**
  - L13–139 (pp. 1–2) — abstract, intro, Figure 1 (the diagram is garbled, L56–99).
  - L200–260 (pp. 4–5) — corpus (hash-pinned, 9 silent same-label re-uploads) and method (the unit is the commitment).
  - L356–440 (pp. 6–7) — results: 67% of material changes silent on the strict reading; 77% weakening; weakenings silent at 0.75 vs strengthenings at 0.50. GDM's "e.g. 2x from 2020–2024 rates" became "historical rates" while its blog said the CCLs were "sharpened" (L433–436). I checked this: GDM v2 L296–297, v3.0 L604–608, blog L68–70.
  - L442–477 (pp. 7–8) — discussion: structural secrecy vs decoupling; a justification duty vs an enumeration duty.
  - L976–1060 (pp. 17–19) — Appendix F, verbatim before/after pairs with adjudication notes. The best specimen of how a commitment drifts.
  - L1310–1346 (p. 24) — Appendix K, silent re-uploads. **The relata copies of Meta v1.1, xAI RMF, GDM v2.0 and Microsoft v1 are the re-uploaded variants**; see the version notes above.

---

## Across the set: how these documents make their claims

**1. Commitment strength is carried by modal verbs, and three analyses measure it independently.**
- Zhu has a modal ladder with present-tense practice at the top (L781–788, L820).
- Coggins has allow / encourage / request / demand / refuse (L214–236).
- Stelling scores "may consider" below "will" (L527–531).

The frameworks themselves slide between "will", "aim", "may" and "as appropriate" within a single paragraph (xAI RMF L377–405; GDM v2 L144–149). One pattern your current guess list may not cover: descriptive-present statements ("we conduct", "Models are trained ...") work as the strongest commitments, according to Zhu's codebook, yet they read like reports of fact. I would expect a schema to need both a force slot on each commitment and a way to mark a present-tense sentence that is ambiguous between "is the case" and "we undertake".

**2. The core definitional form is a relation with a slot for its counterfactual baseline, and the baseline moves.**
Thresholds read "capability X gives actor Y uplift of size Z relative to baseline B, leading to harm W". The documents fill B differently:
- internet search (Amazon 2025 L59);
- "other publicly available models in known harnesses" (Amazon 2026 L71–72);
- "a baseline without generative AI" (GDM v3.0 L486);
- "2024 AI technology and tooling" (GDM v2 footnote 13, L285);
- "currently available open-weights models" (Microsoft 2026 L253–254);
- an outside model judged to be below threshold (G42 L88–94);
- competitors' LiveCodeBench scores in May 2024 (Magic L53–63);
- "the previous model version" (Cohere L632–638).

Stelling's remark about thresholds "relative to competitors" (L1709–1719) is the analyst's version of this. "Uplift" without its B is underspecified, and B changes silently across versions.

**3. Acceptance criteria are mostly assignments of judgment, not criteria.**
"Will be deemed acceptable if, for example" (GDM v3.0 L256–257). "A final assessment of uplift is approved by senior-level decision-makers" (Meta 2025 L699–705). "Executive Officers ... will make the final decision" (Microsoft 2026 L380–384). "Delegated by Cohere's CEO to Cohere's Chief Scientist" (Cohere L609–611). The assertion type is roughly "actor R decides P using considerations C1…Cn". It is not "if metric > t then action". Numbers do occur (xAI RMF, Meta 2026 L1358–1359, the Gemini report's 90% margin, Magic's 50%, NVIDIA's 1–64), but they tend to disappear in later versions (xAI 2026).

**4. Stipulated premises are a distinct kind of assertion.** They are neither causal claims nor measurements:
- "we assume that catastrophic harm would eventually materialize" (Meta 2026 L832–836);
- "our safety case ... assumes that AI deployments will feature oversight similar to that of human employees" (Gemini report L1665–1666);
- "we assume that the models are used in AI systems in ways comparable to the publicly known state of the art" (Gemini report L152–154);
- "we do not expect other groups to put significantly more effort into ML R&D than we do" (GDM v3.0 L200–201).

Everything downstream rests on them. I'd give them their own place in the schema: premise or assumption, marked as adopted rather than argued.

**5. Some commitments are conditioned on other actors.** Examples:
- GDM v2: adoption "may depend on whether such organizations across the field adopt similar protocols" (L31–34). v3.0 softens this to "most effective when adopted by industry as a whole" (L39–44).
- GDM v3.0 L386–390: risk acceptability depends on what other developers' public models can do and how well they are mitigated.
- Coggins finding 3: "especially if other AI developers do so" (L36–37).
- Cohere: acceptability is measured against its own prior model.

**6. Vocabulary is increasingly borrowed by citation.**
- xAI 2025 incorporates TFAIA's definition verbatim; xAI 2026 declares its terms to be the EU Code of Practice's (L40–42).
- Microsoft 2026 sets its scope by statute (L171–173).
- NAVER 2.0 uses the Korean AI Basic Act's "High-Impact AI" (L258–260).
- Shanghai's glossary is the IASR's (footnote 73) and its process is ISO/GB/T.

A term's meaning is often "whatever instrument X says", which calls for a provenance slot for definitions made by reference.

**7. The same words, different ontological categories.** "Loss of control" alone is defined as:
- a species-level harm: "severe disempowerment of the human species" (NAVER 2024 L69–71);
- a situation humans are in: "humans lose—and cannot feasibly regain—the ability to direct, modify, contain, or shut down" (Meta 2026 L826–828); "operate outside of anyone's control, with no clear path to regaining control" (Shanghai L2116–2117, from the IASR), with passive and active forms (L375–380);
- a model capability: "a model's ability to undermine effective human control ... such that ... a model can no longer be reliably directed, modified, or shut down" (Microsoft 2026 L101–103);
- a risk domain grounded in a capability to act autonomously (Amazon 2026 L122–125);
- a risk of humans losing the ability to direct a model (xAI 2026 L25–26);
- one clause of a legal harm definition: "(C) Evading the control of its frontier developer or user" (TFAIA via xAI 2025 L44).

GDM avoids the term as a domain name ("undermining human control"). Its blog glosses it as "interfere with operators' ability to direct, modify or shut down" (L45–47).

"Alignment" ranges widely too:
- training toward responsible-AI objectives (Amazon 2025 L152–155);
- "a model persona that ... emphasizes ethical practices" (Amazon 2026 L276–277);
- refusing by default ("incidental alignment", xAI RMF L228–229);
- serving the user's intent (Google's "User Alignment Critic", L147–151);
- misalignment as conflict with the intentions or values of "developers, operators, users, specific communities, or society at large" (Shanghai L2120–2122);
- "deceptive alignment", defined as purposeful undermining of control (GDM v2 L324), as appearing aligned while pursuing hidden goals (METR L362–364), and equated with scheming (Gemini report L1447–1449).

**8. Versions are not stable objects, so assertions need version pinning.**
My own comparisons, beyond Zhu's:
- GDM v3.0→v3.1 dropped "reliably" from "reliably prevent" (L408 → L661) and turned "if, for example:" into "if:".
- GDM v2→v3.0 dropped the conditional-adoption sentence.
- Amazon moved its uplift baseline.
- Microsoft loosened its cadences: six months became "material changes" and twelve months. The change log lists these without direction.
- xAI 2026 removed all numeric criteria and has no change log.
- NAVER dropped loss of control altogether.
- Meta's change log is unusually explicit: "Stop" became "Develop with Mitigations".

Analyses freeze earlier versions: Stelling quotes xAI's ">100 deaths", and METR's table still lists NAVER under loss of control. And the relata copies are specific re-uploads (Zhu App. K). An assertion row probably needs (document, version label, file hash or variant), not just the key.

**9. What is nearly absent.**
- **Incident accounts:** none of the frameworks reports an incident. The closest are the Gemini report's narratives of model behaviour during evaluation (L173–186, L1597–1650), which are a real sub-genre: behaviour observed under test. Coggins cites press reports of harms (L504–508).
- **Measurements:** only in the Gemini report.
- **Taxonomies:** they are everywhere, but most analysts bring their own: METR's 9 elements, Buhl's 3 areas / 13 components / 56 practices, Stelling's 4 dimensions / 65 criteria, Coggins's affordance coding × the MIT repository, Zhu's EC1–6. These analyses are doing to the frameworks what your project does to every source, and their codebooks (Zhu App. B especially) are ready-made schema proposals worth comparing against.

**10. Two small textual oddities show drafting in the published record.** Meta's footnote "OpenAI former, GDM latter" (L438), and Cohere's duplicated paragraph (L640–643). METR's "all three policies" (L44) is a third. They matter only as evidence that these are edited, living documents, not settled legal texts.

---

## On the brief (feedback, as invited)

- The relata texts are specific *variants*. For at least four documents they are the re-uploads, not the first publications (Zhu App. K). If the schema will record which version an assertion comes from, relata's identity for a key may need a variant or hash field.
- For the table-heavy documents (Meta, Microsoft, G42, Shanghai, Coggins, the Gemini summary table), `pdftotext -layout` interleaves columns. A second extraction without `-layout` (or with `-raw`) kept alongside might make the tables readable by line offset. That is a guess; I haven't tested it here.
- Several analyses in my set (Coggins entirely; Zhu's headline examples; Stelling's top scorer) are really *about* Anthropic and OpenAI, whose frameworks belong to another family (`co-anthropic-openai.md`). Whoever reads the two atlases together may want to pair them.
