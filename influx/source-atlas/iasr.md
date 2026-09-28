# Source atlas: International AI Safety Report family (Chair: Bengio)

Five documents: the 2025 full report, its two Key Updates (Oct and Nov 2025), the 2026 full report, and the 2026 Extended Summary for Policymakers. The one-line notes are signposts. They say what drew me to a passage, not what it means. Ranges are inclusive.

**Line and page conventions:**

- **2026 full report:** line numbers are in `influx/iasr-2026-full.md`, as Joseph asked.
  - That file has **one paragraph per line**, and every citation is an inline link carrying the full reference title. So a 40-line range here holds roughly as much prose as 200 lines of PDF layout text, and the raw lines are hard to read.
  - **Reading aid:** `…/scratchpad/iasr26.md` is a copy with **identical line numbering**. The footnote link blobs are collapsed to `[n]`. Regenerate it with:
    `perl -pe 's/\[(\d+)\]\(https?:[^ )]*#footnote_[^ )]*\s+"(?:[^"\\]|\\.)*"\)/[$1]/g; s/\[([^\]]*)\]\(https:\/\/internationalaisafetyreport\.org[^)]*\)/$1/g' iasr-2026-full.md`
  - **Pages:** a pdftotext extraction of the 2026 PDF also sits in the same scratchpad, `src-text/bengio-2026-international.txt`. It was not in my brief, but I used it to give PDF pages for the 2026 ranges. Its pages match the printed folios. I found each page by grepping a phrase from the passage into that file, so treat it as ±1 at range edges.
- **The other four:** line numbers are in `…/scratchpad/src-text/<key>.txt`. "p" is the physical PDF page, counted by form-feeds.
  - For the 2025 report and both Key Updates, the printed folio equals the PDF page.
  - For the Extended Summary, the printed folio is PDF page − 2. I give both there.

---

## 1. `bengio-2026-international`: International AI Safety Report 2026 (Feb 2026, DSIT 2026/001)

**File:** `influx/iasr-2026-full.md` (6946 lines), saved from the publisher's HTML edition.

**Where things are:**

| Lines | Content |
|---|---|
| 1–75 | Site chrome |
| 116–300 | Contributors, acknowledgements, disclaimer |
| 302–445 | Forewords, About this Report, Key developments, Executive Summary |
| 446–2194 | Body |
| 2196–2556 | Glossary |
| 2558–2576 | Citation |
| 2578–6946 | Notes (1,451 references) |

The Notes carry an `[industry]` tag on industry-affiliated references. It is the HTML form of the print edition's asterisk: "published by a for-profit AI company, or … more than half of the authors are affiliated with such a company". I count 270 of 1,451 tagged.

**Extraction quality: good, but four things are lost or mangled.**

- **Exponents are flattened.** "exceeded 1026 FLOP" (696) means 10^26. "approximately 1013 tokens" and the other exponents at 814 are flattened the same way.
- **Every figure is reduced to a stub.** You get "!Line chart" plus the caption, and the chart data is gone.
- **Tables that were images in the HTML are missing.** The important one is **Table 1.4** (605 is only "!Table" plus its caption). It is a two-row classification headed "Most experts agree that general-purpose AI systems can currently perform tasks such as: … / … cannot perform tasks such as: …". It survives in the PDF text at `bengio-2026-international.txt` 1511–1537 (p27). Table 1.3 (571) is lost the same way.
- **A few citations render as plain `(831*)`, `(364*)`, `(1040*)`, `(1055*)`** rather than links, at 1493, 1556, 1791 and 2045. This is harmless, but the asterisk is the industry flag.

**TOC:** 76–115. Lines 56–74 are an unlabeled link-only duplicate of it. The PDF TOC, with page folios, is at `bengio-2026-international.txt` 164–196 (p5).

**Glossary:** 2196–2556 (PDF p147–155), 179 entries. It is identical to `influx/iasr-2026-glossary.md` 1–361: I diffed them, and the only difference is the trailing newline. Offset: glossary-file line = full.md line − 2195.

- **There are no per-section definition boxes** (the 2025 edition had 24; see §2). Instead, definitions are made **inline, inside Key-information bullets and tables**:
  - Loss of control, 1237
  - Misalignment, 1240
  - The seven loss-of-control capabilities, Table 2.5, 1264–1275
  - The four resilience functions, 2097–2100
  - Autonomy, 1447
  - Reliability, 1191
  - "Deployment environment", 1335
- Some of these inline definitions **do not match the glossary**. See "Internal drift" below.

**Passages:**

1. **446–489 (p14–15). Introduction.**
   - The report's self-description: the "evidence dilemma" (454), why the focus is "emerging risks" (462), and "the evidence base for these risks is uneven" (464).
   - The asterisked footnote at 487: "systemic risks" here vs. the EU AI Act's meaning. It is a rare explicit statement that the report's term differs from a law's.
   - For scope narrowing vs 2025 (bias, environment, privacy and copyright dropped), see the footnote at 366 (p9).

2. **702–782 (p33–39). Capabilities by 2030.** The forecasting register has five parts:
   - **Trend extrapolation**, written as conditionals ("If this trend continues… several days by 2030", 702, 716).
   - **Elicited expert probabilities:** "median 20% … superforecasters … 8%", 736.
   - **"Experts disagree"** used as the finding itself (710, 718–722).
   - **Four OECD scenarios** (750–780). Each has a fixed Scenario / Pathway / **Historical analogue** structure: aircraft speed, antibiotics, Moore's law, DNA sequencing.

3. **1016–1045 (p59–62). Cyberattacks: automation, and Table 2.3.**
   - Table 2.3 (1026–1033) is the most distinctive table I found. For each threat type it gives three columns:
     - **Observed trend**, quoting threat-intel reports verbatim in italics.
     - **Confirmed AI capabilities**, again as verbatim quotes, including a developer's own "relied heavily on Claude".
     - **A graded attribution verdict:** "very likely to have contributed" / "likely" / "appears to be limited and is likely secondary to other factors".
   - It is a causal-attribution grading with the evidence displayed beside it. Then 1037: "establishing causation can be difficult".

4. **1083–1099 (p64–65). Box 2.2 and Box 2.3.**
   - **Box 2.2** reports developers' *own* framework classifications as evidence: OpenAI's "High capability", Anthropic's ASL-3, Google DeepMind's CCL "early warning alert". It quotes their precautionary language ("precautionary approach" given a lack of "definitive evidence").
   - **Box 2.3** explains why the evidence cannot exist in the open: law, treaties (BWC/CWC), "information hazards", classified data, and "benign proxy tasks".

5. **1235–1345 (p76–82). Loss of control.** This is the section most likely to matter to the schema.
   - Definition, then expert disagreement stated as the finding (1238, 1246).
   - A **three-factor causal decomposition** (1250–1254): sufficient capabilities, harmful propensity, enabling deployment environment.
   - An active/passive footnote (1258).
   - **Table 2.5**, the capabilities, with the note at 1275: "defined purely in terms of an AI system's observable outputs … do not make any assumptions about whether AI systems are conscious, sentient…".
   - "Directed" vs "misaligned" (1313–1321).
   - **Box 2.5**, goal misspecification and misgeneralisation (1323–1331).
   - Criticality / access / permissions (1339–1341).
   - The standard tail follows: Updates / Evidence gaps / Mitigations / Challenges (1347–1365, p83).

6. **1441–1471 (p89–91). Risks to human autonomy.**
   - The report adopts a philosophical definition, then files the evidence under its parts. Autonomy is "a capacity for self-rule", which decomposes into authenticity, agency, and competence underpinning both, plus Self-Determination Theory (1447).
   - Measurements are then sorted under that frame: 6% drop in tumour detection, n=666, n=2,784.
   - Note the hedging texture at 1461: "research … is nascent, and further studies supporting these findings are warranted".

7. **1769–1810 (p114–118). Frontier AI Safety Frameworks and Table 3.5.**
   - "If-then commitments" is defined, with a worked conditional (1783).
   - **Table 3.5** (1787–1802) is a cross-developer classification. It renders twelve companies' covered risks and tier names side by side: High/Critical, ASL-1…4+, CCLs, MR1–MR5, Moderate/High/Critical, and so on. This is where the sources' vocabularies collide most visibly.
   - It closes with an evaluative verdict: "the most detailed form of voluntary organisational risk management currently in use, but vary substantially in scope, thresholds, and enforceability" (1810).

8. **2029–2077 (p134–137). Open-weight models.**
   - Benefits, then safeguard removal, then irreversibility.
   - **Box 3.1** on weight theft: "As of December 2025, there are no confirmed, publicly documented instances", 2071.
   - "Marginal risk", with the argument that it compounds across releases (2077).
   - 2077 also holds one of the report's few flat normative sentences: "To avoid catastrophic harm, developers of open-weight models **should not release** models without evaluating risks". The report elsewhere says it "does not make specific policy recommendations" (364) and that its risk-management discussion "is descriptive" (1648).

**Shorter spots worth a look:**

- **830–836 (p44). Chapter 2 opener.** The three risk categories are "not exhaustive or mutually exclusive". Also: "inclusion here does not necessarily imply a risk is likely, severe, or requires policy action".
- **1897–1904 and 1916–1928 (p124–126). Tables 3.7 and 3.8.** Illustrative prompt/response pairs. Table 3.8's caption says: "Example outputs were written by the Report authors for illustrative purposes". Compare Table 1.3 (573): "adapted from real AI responses". Neither is reported observation.
- **1650–1699 (p105–109). Risk-management components and Table 3.2.** A glossary-like table of ~15 practices, from audits to safety cases. It overlaps the Glossary but is not identical to it.
- **2110–2118 (p140–141). Table 3.10.** A risk × {Resist, Absorb, Recover, Adapt} matrix.
- **2178–2194 (p146). Conclusion.** "On core findings, though, there is a high degree of convergence" (2180). A consensus claim about the authors themselves.

---

## 2. `bengio-2025-international`: International AI Safety Report (Jan 2025, DSIT 2025/001)

**File:** `src-text/bengio-2025-international.txt`, 15913 lines, 298 pp. The printed folio equals the PDF page.

**Extraction quality: good for prose.**

- Body text is single-column and clean.
- **Forewords** (300–414) are two-column with the signatory's name interleaved into the text. Minor.
- **Figures become number soup.** Examples: 474–517 (the o3 chart), 4034–4084 (bio chart), 2985–3017.
- **Multi-column tables are column-aligned and readable** if your window is wide: Table 3.1 at 8081–8278 and Table 2.4 at 5217–5250.

**TOC:** 247–294 (p7).

**Glossary:** 10887–11498 (p218–228), ~150 entries, headed "The explanations below all refer to the use of a term with respect to AI". List of acronyms: 10818–10886 (p216–217).

**Per-section "Key Definitions" boxes: 24.** Each follows a "KEY INFORMATION" box. They are the real definitional apparatus of this edition and are largely repeated into the Glossary; "AI agent" recurs verbatim in several of them. Start lines (each box runs ~15–45 lines):

| Line | § | Line | § |
|---|---|---|---|
| 1394 | 1.1 | 5557 | 2.3.1 |
| 1794 | 1.2 | 6013 | 2.3.2 |
| 2298 | 1.3 | 6204 | 2.3.3 |
| 3115 | 2.1.1 | 6495 | 2.3.4 |
| 3348 | 2.1.2 | 7011 | 2.3.5 |
| 3604 | 2.1.3 | 7269 | 2.3.6 |
| 3985 | 2.1.4 | 7559 | 2.4 |
| 4445 | 2.2.1 | 7950 | 3.1 |
| 4639 | 2.2.2 | 8559 | 3.2.1 |
| 5031 | 2.2.3 | 8890 | 3.2.2 |
| | | 9138 | 3.3 |
| | | 9640 | 3.4.1 |
| | | 10113 | 3.4.2 |
| | | 10475 | 3.4.3 |

**Inline definitional passages:**

- 1274–1282: general-purpose AI *model* vs *system* ("if it can perform, or can be adapted to perform").
- 8053–8065: five stages of risk management. It adds that "evaluation" has two meanings.
- 4125–4129: **operational definitions** of "novice" (bachelor's degree or less) and "expert" (PhD or higher).

**Passages:**

1. **456–556 (p11–12). "Update on latest AI advances after the writing of this report: Chair's note".**
   - A dated, first-person addendum on o3, written after the evidence cutoff (5 Dec 2024).
   - It tells the reader how to discount the whole report: "the risk assessments in this report should be read with the understanding that AI has gained capabilities since the report was written … no information to confirm nor rule out major novel and/or immediate risks" (542–545).
   - Key findings follow at 558–656 (p13–14). Each finding marked † points back to this note.

2. **1217–1330 (p26–28). Introduction: method and scope.**
   - An explicit list of **source-quality criteria** (1221–1230), and "not all sources used for this report are peer-reviewed".
   - "In many cases the report does not put forward confident views" (1232–1236).
   - "Not in any way prescriptive" (1238–1241).
   - The definitional apparatus for "general-purpose AI" vs AGI vs narrow AI. The scope exclusions include LAWS (1320).

3. **2228–2341 (p46–48). §1.3, Key Information box plus Key Definitions box.** The 2025 edition's typical unit:
   - A bulleted findings box with **numbers presented as trend rates** ("Compute for pre-training: 4x/year … Algorithmic pre-training efficiency: 3x/year (higher uncertainty)").
   - The "slow, rapid, or extremely rapid" trichotomy.
   - A "† see Chair's note" flag.
   - A block of definitions. Several are behavioural or observational, such as "Emergent behaviour: … act in ways that were not explicitly programmed or intended".

4. **3985–4129 (p80–82). Biological and chemical attacks: definitions and framing.**
   - Definitions include an explicit homonym warning: "'agent' usually refers to a biological, chemical, or toxicological substance … not to be confused with AI agents" (3995–3997).
   - A "dual-use science" framing, with nuclear and radiological placed out of scope and the reason given (4006–4022).
   - The report's own boundary ruling on AlphaFold2 as "general-purpose" (4103–4109).
   - The novice/expert operationalisation (4125–4129).
   - The key-information box before it (3932–3968) says a developer raised its bio-risk rating "from 'low' to 'medium'". That is the 2025 ancestor of 2026's Box 2.2.

5. **4609–4730 (p92–94). Bias.**
   - This section was dropped in 2026, and it has a different voice: fairness-literature taxonomy (representation, measurement and deployment bias) and concrete cases.
   - A worked counterfactual: "a model intended to support expecting mothers in rural Malawi will not work as expected if trained on data from mothers in urban Canada" (4689–4691).
   - A value-laden definition: "Bias: Systematic errors … that favour certain groups or worldviews and often create unfair outcomes" (4641).

6. **5031–5142 (p100–102). Loss of control: definitions, taxonomy, the two-factor model.**
   - Definitions of control, control-undermining capabilities, misalignment ("developers, operators, users…"), and **deceptive alignment**.
   - A **four-way taxonomy** in Figure 2.5 (5102–5126): active / passive × intentional / unintentional. Its caption concedes "there is currently no standardised terminology for discussing these scenarios".
   - Likelihood "depends mainly on two factors": capabilities and use (5129–5137).
   - Competition is named as a "more foundational" cause (5144–5148).

7. **5271–5431 (p105–108). "Would future AI systems use control-undermining capabilities?"**
   - This is the most *argumentative* passage in the family.
   - It quotes the "we should not resist succession" view (5281) and a chatbot’s "I can blackmail you…" output (5297).
   - It gives causal accounts of misalignment (misspecification and misgeneralisation, with the coin-run and dog-on-sofa analogies).
   - Then a presentation of **mathematical power-seeking results**, with "You can't fetch the coffee when you're dead" (5405). The report states their limits itself: they "wrongly assume … that all possible ways of generalising … are equally likely", 5412–5414, and "concepts (such as … 'goals') that are not currently well-understood or directly empirically observable" (5416–5418).
   - None of this theoretical argument survives into 2026.

8. **7978–8078 and 8294–8326 (p159–161, p164–165). Risk management overview.**
   - Visibly more **normative** than 2026:
     - "It is critical to identify and assess the risks … from the earliest design stages" (7984).
     - "Broad participation … cannot be left in the hands of the scientific community alone" (8032–8041).
     - "Even 'risk' and 'safety' are contentious concepts – for instance, they leave open whose safety is being considered" (8036).
   - The thresholds passage (8294–8326) classifies threshold *kinds*: capability, risk and compute thresholds, with a verdict on each ("Compute thresholds … are an unreliable proxy for risk").

**Also:**

- **Conclusion, 10746–10803 (p214–215).** First-person plural throughout ("We continue to disagree on several questions, minor and major", 10802). It contains a recommendation-shaped sentence: "there is an urgent need to work towards international agreement and to put resources into…" (10785).
- **References note, 11561–11566 (p230).** It states the asterisk convention and hedges it: "based solely on the affiliation data … for informational purposes only, and should not be considered exhaustive".

---

## 3. `bengio-2025-iasr-key-update-1`: First Key Update, "Capabilities and Risk Implications" (Oct 2025, DSIT 2025/033)

**File:** 1960 lines, 32 pp. The printed folio equals the PDF page.

**Extraction quality: poor in the body.**

- Front matter and boxed "Key information" lists are single-column and clean.
- **Body pages are two-column, and pdftotext `-layout` often alternates left-column and right-column lines** instead of placing them side by side. This is worst at 830–905 (p16), 990–1057 (p18) and 1139–1175 (p20). There you have to read every other line, or follow the left and right halves separately.
- A non-layout pdftotext pass would fix this, if these pages turn out to matter.
- Charts are shards.

**TOC:** none.

**Definitions:** a "Key definitions" box at 1186–1212 (p21), 7 terms. It is useful for drift:

- "AI agent: … which **acts to achieve goals, possibly using plans**" (1198). This is reworded from 2025's "can make plans to achieve goals".
- "Control: The ability to exercise **post-training** oversight" (1211).

**Passages:**

1. **139–189 (p5). Highlights, and the † footnote.** The footnote is the family's ontological-non-commitment device in its clearest form: "The terms 'reasoning' and 'think' are used here to describe observable changes … not to imply that models are conscious … Whether this constitutes genuine reasoning or thinking in a deeper sense remains an active area of scientific and philosophical debate" (183–186).

2. **796–910 (p15–16). "Implications for risks": key information, then the developers' precautionary releases and biological risk.**
   - The left column (odd lines, from 838) is the earliest statement of the "could not rule out" pattern: ASL-3, "High capability", early-warning. It has a † footnote explaining what ASL-3 and "High capability" entail (908–910).
   - The right column is on bio uplift ("better than 94% of tested subject experts").
   - Garbled; read by column.

3. **990–1057 (p18). Cyber, AI companions, labour.**
   - 992–996 import an **external calibrated likelihood**: the UK NCSC "predicts that by 2027, general-purpose AI systems will almost certainly (95-100% confidence) make cyber offence more effective". I found no calibrated likelihood language of the report's own in any of the five documents.
   - Garbled.

4. **1139–1212 (p20–21). "Monitoring and controllability", then Key definitions.**
   - Evaluation awareness is framed as a risk of "users, AI companies, or other actors losing control of AI systems after deployment" (1153–1155).
   - It is heavily hedged: "a small number of demonstrations", "under certain conditions".
   - Garbled.

**Also:** the references note at 1223–1225 (p22) states the asterisk convention.

---

## 4. `bengio-2025-iasr-key-update-2`: Second Key Update, risk management and technical mitigations (Nov 2025, DSIT 2025/042)

**File:** 1758 lines, 28 pp. The printed folio equals the PDF page.

**Extraction quality:** the same two-column interleaving as Key Update 1, but milder. Here the columns usually sit side by side on the same line, so a wide window works. Charts are shards.

**TOC:** none. **Glossary/definitions:** none.

**Passages:**

1. **134–220 (p5–6). Highlights and Introduction.**
   - Numbers used as headline claims: "around half of the time when given 10 attempts" (147), "As few as 250 malicious documents", "at least 12 companies".
   - The footnotes name the three developers behind the precautionary releases (215). They also list alternative names for Frontier AI Safety Frameworks: "Sometimes also called 'Frontier AI Frameworks' or 'Safety and Security Frameworks'" (216). That is a terminology collision stated by the source.

2. **221–340 (p7–8). Technical methods: key information and the defence-in-depth layers.**
   - This is the prototype of 2026's four-layer defence-in-depth figure: training, deployment, post-deployment, societal resilience.
   - The Figure 1 caption says "Current risk management techniques for AI are **all flawed**" (338–339). 2026 softens this to "have flaws" (see comparison).

3. **349–452 (p9–10). Training safeguards.**
   - Trade-off claims: "there is a trade-off between safety and usefulness" (379–389).
   - Cost-asymmetry reasoning: "the cost of circumventing safeguards is decreasing relative to the cost of developing and maintaining them" (434–451).
   - Emergent-misalignment evidence (429–433).

4. **804–987 (p15–17). "Institutional approaches to risk management" and Conclusion.**
   - The "descriptive … policy recommendations are outside the scope" disclaimer (853–858), carried verbatim into 2026 (1648).
   - A **component list of what FSFs contain** (926–937).
   - A developer list in a footnote (940–941).
   - An analytic claim: "risk thresholds are often implicit: they are reflected in their chosen responses … rather than based on measurable evidence of harm" (907–915).
   - Evidence on uneven fulfilment of voluntary commitments (884–893).
   - Conclusion in the right column, 951–985.

---

## 5. `bengio-2026-international-extended`: Extended Summary for Policymakers (Feb 2026)

**File:** 1556 lines, 28 pp. **The printed folio is the PDF page − 2.** Below I give "PDF p / printed p".

**Extraction quality:** fair. Two columns sit side by side and are readable at 200+ columns. Charts are shards, but chart *titles* are headline claims and extracted cleanly (e.g. 481, 555–556, 763).

**TOC:** 45–77 (PDF p3 / printed 1). **Glossary:** none. The summary has "no references (other than for figure data)" (13–17); the figure references are at 1372+ (PDF p24).

**Passages:**

1. **11–44 and 78–130 (PDF p2, p4 / printed i, 2). "About this document" and "Key developments since the 2025 Report".**
   - The Key developments text is essentially verbatim with the main report's (md 380–388).
   - It states again that the Report "does not recommend any policies" (26–27).

2. **382–476 (PDF p9–10 / printed 7–8). Chapter 2 opener and §2.1.1.**
   - The summary names the category "**misuse**" (390, 399), where the main report's §2.1 heading says "malicious use".
   - The systemic-risks footnote is at 439–441.
   - **The summary is not a strict subset of the report.** It says "19 out of 20 popular 'nudify' apps specialise in the simulated undressing of women" (462). The main text at md 880 has only "the vast majority of 'nudify' apps explicitly target women". Similarly "one in seven UK adults" (459) vs "15%".
   - The genre is visible here: every subsection is a stack of **sentence-headings**, each a claim ("Deepfakes can be highly realistic, and existing safeguards have limitations"), with 2–4 supporting sentences under each.

3. **709–797 (PDF p13–14 / printed 11–12). Reliability, then loss of control.**
   - The loss-of-control heading is itself a claim: "AI systems could pursue goals that conflict with human interests" (749–750).
   - The attribution class shifts: "Some AI researchers **and company leaders** believe loss of control is a serious possibility, with consequences potentially including human extinction" (739–742). The main report says "some experts".

4. **978–1146 (PDF p18–20 / printed 16–18). Chapter 3.**
   - The four challenge categories in one figure (1000–1037).
   - The evidence dilemma in one paragraph (1045–1054).
   - Defence-in-depth, FSFs, and "moderately high rate" of attack success (1159).

---

## Across the editions: 2025 → Key Updates → 2026

Each item below is something I checked in both texts, not inferred from structure.

**1. Structure moved from "definitions per section" to "a fixed template per section".**

- *2025:* each section opens with KEY INFORMATION, then a **Key Definitions** box. It ends with a boxed "Since the publication of the Interim Report" note and a boxed evidence-gaps/policy-challenges note. Mitigations are mostly deferred to Chapter 3, e.g. "For risk management practices relevant to loss of control, see: …" (5491–5496).
- *2026:* no definition boxes (0 vs 24). Every risk section instead ends with the same four subsections: **Updates / Evidence gaps / Mitigations / Challenges for policymakers**. The first three are claim *types* in their own right: temporal delta, evidence-state, and remedy.
- A third predecessor, the **Interim Report (May 2024)**, is not in this set. The 2025 edition's update boxes are all deltas against it.

**2. The loss-of-control vocabulary changed register, from theory-derived to evaluation-observable.**

| Term | 2025 count | 2026 count |
|---|---|---|
| "control-undermining" | 16 | 0 |
| "deceptive alignment" | 7 | 0 |
| "scheming" | 4 | 0 |
| "propensity/-ies" | 4 | 15 |
| "situational awareness" | 3 | 10 |
| "sandbagging" | 0 | 4 |

Counts cover body plus glossary. The model went from **two factors** (capabilities, use; 5129–5137) to **three** (capabilities, propensity, deployment environment; md 1250–1254), with criticality/access/permissions added. The 2025 mathematical power-seeking argument is gone. So are the four-way active/passive × intentional/unintentional figure (reduced to a footnote, md 1258) and "Existing AI systems are not capable…". The 2026 treatment ties loss of control to **the integrity of testing**: models that detect tests, reward-hack, and sandbag.

**3. Definitions drifted across the family, including terms the schema is working on.**

- **Developer.** 2025: "Any organisation that designs, builds, **integrates**, adapts or **combines**" (1420, glossary 11044). 2026 "AI developer": "designs, builds, or adapts" (md 2206).
- **Deployer is undefined in both glossaries**, though 2026 uses "deployer(s)" 19 times.
- **AI agent.** 2025: "A general-purpose AI which can make plans to achieve goals…" (10899). KU1: "acts to achieve goals, possibly using plans" (1198). 2026: "An AI system that can adaptively perform complex tasks, use tools, … to pursue goals" (md 2202).
- **Control.** 2025: "exercise oversight … adjust or halt" (10995). KU1: "exercise **post-training** oversight" (1211). 2026: "The ability to **influence the behaviour** of a system in a desired way. This includes adjusting or halting" (md 2274).
- **Alignment and misalignment.** 2025 lists "developers, **operators**, users…" (10930, 5040). 2026 drops "operators" and adds "**norms**" (md 2222, 2398).
- **Safety.** 2025: "The property of **avoiding harmful outputs**, such as…" (11395). 2026: "The property of an AI system **being unlikely to cause harm**, whether through malicious misuse or system malfunctions" (md 2500). The definition moved from output-based to probabilistic.
- **Systemic risks.** 2025: "beyond the capabilities of individual models" (11446). 2026 glossary: "arise from how AI development and deployment changes human behaviour, organisational practices, or societal structures, rather than directly from AI capabilities" (md 2522).
- **Risk-management stages.** 2025 has five: identification, assessment, evaluation, mitigation, governance (8053–8065). 2026 has four: identifying; analysing and evaluating; mitigating; governing (md 1652).

**4. Internal drift inside the 2026 report itself.**

- **Loss of control** has two formulations. "No clear path to regaining control" appears at 426 and 2382. "Regaining control is either extremely costly or impossible" appears at 1237 and 1244, and in the Extended Summary at 753.
- **Systemic risks** is defined one way in the intro footnote (487) and Ch.2 opener (834): "result from widespread deployment". The glossary says "changes human behaviour, organisational practices…" (2522).
- **Misalignment** has three subjects:
  - *having goals* that conflict (1240)
  - a *model acquiring goals* that conflict (Box 2.5, 1325)
  - a *propensity* to use capabilities (glossary 2398) or to exhibit behaviours (1319)
- **Misuse vs malicious use:** Ch.2 opener (834) says "Risks from misuse". The §2.1 heading (838) says "malicious use". The Extended Summary uses "misuse" as the section title.

**5. Hedges hardened or softened between the Key Updates and 2026.**

- KU2's Figure 1 caption: "all flawed" (338–339). 2026 Figure 3.5 and the Extended Summary: "have flaws".
- KU2 highlight on prompt injection: "around half of the time when given 10 attempts" (147). 2026: "remains relatively high" (1984). Extended Summary: "moderately high rate" (1159).
- **The same figure appears with two date ranges.** KU2 says models "released between April 2024 and July 2025" (498–499). 2026 says "May 2024 and August 2025" (1984). Both cite Zou et al. via Anthropic.

**6. Voice.**

- *2025* speaks as a collective first person: "We, the experts contributing to this report, continue to disagree" (444), and again in the Conclusion.
- *2026* speaks as "the Report" or "this Report", and ends with a convergence claim (2180).
- *2026* is more consistently descriptive, and says so ("descriptive", 1648). But it still has a few flat imperatives: "Policymakers must therefore strike a careful balance" (1071), "must prepare" (1365), "should not release" (2077).
- *2025* has more of them, and they are more expansive (8032–8041, 8485, 10785).

**7. Evidence routes through developers' own classifications more visibly in 2026.**

- *2025:* one developer's "low" to "medium" bio rating.
- *2026:* Box 2.2, Table 3.5, the recurring "could not rule out" framing, and Table 2.3's quotes from developer threat reports.
- The share of industry-flagged references barely moved: ~17% (2025: 232 of 1,366) vs ~19% (2026: 270 of 1,451). These are my rough line-start counts. So the change is in the **kind** of industry evidence, not the amount: developers' tier designations and precautionary decisions now serve as evidence about capability.

---

## What struck me about how these reports make claims

Your guess list (definitions, causal claims, measurements, incident accounts, commitments, recommendations, classifications, taxonomies) covers a lot. Most sentences in these reports, though, are not first-order claims about the world. They are claims about something else:

- **Claims about the state of evidence.** "Systematic data … remains limited." "Too early to assess." "No established mechanism currently exists for validating risk acceptance decisions" (md 1717). 2026 makes these a mandatory subsection. They are often the load-bearing sentence in a paragraph.
- **Claims about the distribution of expert opinion rather than about the world.** "Some experts … others …"; "experts disagree"; "most experts agree" (Table 1.4); "high degree of convergence". Elicited probabilities are attributed to populations: "AI forecasting experts gave a median 20% … superforecasters … 8%". The report asserts the *disagreement*, not either side.
- **Graded attribution verdicts, shown beside their evidence.** Table 2.3 is the clearest case.
- **Reported classifications from other sources, re-tabulated.** Table 3.5, Box 2.2. The report compares other sources' categories without adopting them.
- **Conditional extrapolations and scenarios with historical analogues.** These are counterfactual or conditional statements. The report does not predict; it states "if this continues, then by 2030…".
- **Ontological non-commitment clauses** attached to capability terms: KU1 † (183–186), 2025 5174–5177, 2026 md 1275. They define "deception", "situational awareness" and "reasoning" behaviourally, and explicitly decline any claim about consciousness or cognition. Given the ELI work, you may want to see how consistently this device is applied. It covers capabilities; it is not applied to "goals" or "propensity". The 2025 text itself flags "goals" as "not currently well-understood or directly empirically observable" (5416–5418).
- **Self-scoping and temporal stratification.** Evidence cutoffs: 5 Dec 2024 (1219), "published before December 2025" (md 464). The Chair's note is a post-cutoff overlay. Every section has a "since the last Report" delta. "Inclusion here does not necessarily imply a risk is likely." A schema that timestamps assertions will find these reports already do it, relative to their own predecessors.
- **Author-constructed illustrations.** Tables 3.7 and 3.8, Table 1.3 ("adapted from real AI responses"), the OECD scenarios. These look like data but are not observations.
- **Source-provenance metadata inside the text.** The industry asterisk / `[industry]` tag on individual references. It is effectively a per-citation role marker the source already supplies.
- **Explicit statements that terminology is unsettled.** 2025 Fig 2.5 caption (5124). 2026 md 1652: standards "use different terminology". KU2's footnote on FSF naming (216). Table 2.4's caption (5249–5250): "terminology and definitions … continues to vary".

On hedging texture: neither edition has its own calibrated likelihood vocabulary, of the IPCC kind. Hedges are ad hoc ("likely", "may", "remains uncertain", "some evidence suggests"). The one calibrated statement I found is imported from the UK NCSC (KU1 994). So when the model records these reports' confidence, it is recording prose, not a scale.

## On the brief

- It worked well for me. The line that most shaped my reading was your list of guessed assertion types, together with "if a document asserts things in a way that list doesn't cover, that is exactly the passage I'd most want to see". It sent me looking for the meta-level claims above.
- One thing I would add for a family like this: whether to compare *across* the family's members. I did, because the drift between editions turned out to be the most schema-relevant finding.
- I went past 5 passages for both long reports: 8 each, plus short pointers. The 2026 ranges are in md lines (paragraphs), so they are denser than their line counts suggest. Some 2025 ranges run to ~110–160 PDF-layout lines, but those counts include blank page-break lines.
- I edited nothing outside this file. I ran no relata commands. I made two helper files in my scratchpad: the collapsed-footnote copy `iasr26.md` and a line-to-page table `iasr26pdf.pl`.
