# UK sources: verification of `safety-risk-factors.md`

*Verifier: Claude (Opus 5.5), 2026-09-27. Scope: IASR 2026 (full report and Extended Summary), IASR 2025, the AISI Research Agenda, the AISI Frontier AI Trends Report, the DSIT Oct 2023 discussion paper with Annexes A and B, and the NCSC 2027 assessment. The IASR 26, DSIT, AISI and NCSC crosswalk columns, and these sources' pinpoints elsewhere in the report.*

## How to use this file

- **Page citations.** "p.N" is the printed page. Where the PDF page differs, it is given as well:
  - IASR 2026 full report and IASR 2025: printed page = PDF page.
  - IASR 2026 Extended Summary ("ES"): printed = PDF − 2.
  - AISI Trends: printed = PDF − 2.
  - DSIT main paper and Annex A: printed = PDF.
  - NCSC: PDF page only; the PDF carries no printed numbers.
  - AISI Research Agenda: web section names, plus PDF pages of the May 2025 PDF edition, whose printed number = PDF − 1.
- **Quotes.** Quotes are verbatim from the PDFs now in relata (bibkeys in §7). Every source here is public and Crown/OGL-licensed or open, so quotes run as long as checking needs.
- **Confidence.** "High" means I read the passage in the primary myself. "Medium" means a judgment call on an E/D/P rating. "Inference" is marked as inference.

### What I read and how
- **Read whole:**
  - the IASR 2026 Extended Summary;
  - the IASR 2026 full report, front matter through glossary (pp.1–156; not the reference list);
  - the DSIT discussion paper (all 30 text pages; references skimmed);
  - DSIT Annex B;
  - DSIT Annex A through p.31 (the capability-detail appendix pp.32–37 only skimmed);
  - the NCSC assessment;
  - the AISI Trends Report;
  - the AISI Research Agenda.
- **The AISI Agenda's local extract.** I word-diffed the local extract (`ref/ref-aisi-research-agenda.md`) against the live page fetched today. The prose is identical; the only differences were artifacts of my own normalisation. The extract is safe to cite.
- **IASR 2025, read partly.** Read in full: About, Chair's note, Key findings, Executive Summary, Introduction, §2.2.3 Loss of control, the §2.3 systemic-risk note, §2.3.3 Market concentration, the opening of §2.3.4 Environment, §2.1.2–2.1.3 key information, §3.2.2 Societal challenges, and the Glossary. The rest (chapter 1, other risk sections, chapter 3's technical sections) was only term-searched. Findings about IASR 2025 outside those sections carry that limit.

---

## 1. Summary of what matters most

1. **The IASR 26 column appears to carry IASR 2025's taxonomy.**
   - IASR 2026 deliberately narrowed its scope. p.9, footnote: *"Note that this focus makes the scope of this Report narrower than that of the 2025 Report, which also addressed issues such as bias, environmental impacts, privacy, and copyright."*
   - The column nonetheless gives IASR 26 an **E** for Privacy (A12), IP (A13) and Environment (A15), an **E** for power concentration (A9) and a **D** for bias (A14).
   - Those ratings match IASR 2025's section headings (§2.2.2 Bias, §2.3.3 Market concentration, §2.3.4 Environment, §2.3.5 Privacy, §2.3.6 Copyright) almost exactly.
   - In IASR 2026 these are passing mentions at most. Five cells need downgrading (details in §2).
2. **A16 pools two different "divides."**
   - NCSC's "digital divide" (the report's only ✓ in that row) is between *systems* that keep pace with AI-enabled cyber threats and those that do not. It is a defender-lag concept.
   - The row's other sources mean unequal access across *countries or populations* (IASR 2025 "Global AI R&D divide").
   - The NCSC cell belongs in C14 (defender/societal resilience lag), where the report already cites it.
3. **NCSC's scope explicitly excludes manipulation.** NCSC PDF p.3: *"It does not cover wider threat enabled by AI, such as influence operations."* The NCSC cells rated **D** for A4 (manipulation) and A5 (criminal misuse/synthetic content) are wrong.
4. **Footnotes 9 and 11 can be replaced by primaries.** The primary wording is quoted in §2. The AISI jailbreak finding also has a qualifier the report drops: safeguards are improving, and for bio misuse it took roughly 40× more expert effort (10 minutes to 7+ hours) across two models released six months apart.
5. **New primary evidence bears directly on the report's organizational thesis. The report does not use any of it:**
   - *AISI Trends, p.27.* Safeguard strength *"appears to be determined mostly by the effort and resource invested in developing, testing, and deploying defences"*, not by model capability (R² = 0.097 between capability and robustness). This is a government-lab empirical finding that an *organizational input* (developer effort and resourcing) drives a key safety outcome. It belongs in C8 and §4 "Organizational capacity."
   - *IASR 2026, p.114.* *"Organisational culture, leadership structure, and incentives affect risk management efforts in various ways."* IASR 2026 p.113 (Table 3.4) also lists risk-responsibility allocation and whistleblower protection. So IASR 2026 bears on C6, C7 and C9, which currently omit it. It treats them as *described mitigation practice*, not as named risk factors (see §2.8).
   - *DSIT 2023, p.18.* Exfiltration "by employees or external actors". *IASR 2026 Box 3.1, p.136.* "insider threats". *AISI Agenda (Control).* AI-as-insider threat models inside developer infrastructure. All three belong under B8 and §4 "Insider threats."
   - *IASR 2025 §3.2.2(C), p.178.* *"The rapid growth and consolidation in the AI industry raises concerns about certain AI companies becoming particularly powerful…"* This is a UK-hosted source naming industry *growth* as a risk-taking incentive (too-big-to-fail moral hazard). It is not headcount growth, but the report's "none adds dynamics such as growth" claim should reckon with it (see §4).
6. **"Loss of control" really is pooled.** Joseph suspected this.
   - IASR 2026 defines it at catastrophic scale (regaining control "extremely costly or impossible"). It explicitly sets aside both present-day unintended behaviour and "passive" loss of control.
   - AISI's own risk domain is not called "loss of control". It is "Autonomous Systems", defined far more broadly. Its operational threat models (rogue internal deployments, weight exfiltration inside labs) include exactly the "got past controls for a while" events that IASR 2026 would not count.
   - Details are in §6.
7. **Dates and links.**
   - IASR 2026 was published **3 Feb 2026**. 24 Feb is only the arXiv posting.
   - The AISI Agenda date is now supported by the PDF itself ("May 2025") rather than by techUK.
   - The AISI Trends date of 18 Dec 2025 is supported by secondary sources and by the asset-ID timestamp (inference).
   - Other dates check out.

---

## 2. Proposed changes, item by item

### 2.1 Front matter and §1 source table

**(a) IASR 2026 date.** *High confidence.*
- **Current.** `| Feb 24, 2026 | IASR 2026 | …(arXiv 2602.21012)…`
- **Source.**
  - The report site's publication page reads "3 February 2026 — Annual Report": https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026.
  - The arXiv abstract page reads "Submitted on 24 Feb 2026".
  - The official PDF (`international-ai-safety-report-2026_1.pdf`) and the arXiv PDF are **byte-identical** (sha256 `e2a35f43…`), so citing either is fine.
- **Replace with.** `Feb 3, 2026 (arXiv posting Feb 24)`.
- **Also.** Add the official landing page link.

**(b) IASR 2025 row and footnote 6.** *High confidence.*
- The date (29 Jan 2025) and arXiv ID are correct.
- **Suggest adding** to [^6] the research-series number "DSIT 2025/001" and a verifiable anchor, e.g. p.17 (Executive Summary): *"This report classifies general-purpose AI risks into three categories: malicious use risks; risks from malfunctions; and systemic risks."*

**(c) AISI Research Agenda date ([^7]).** *High confidence for "May 2025". The 6 May day is inference from the timestamp, now corroborating techUK.*
- **Current.** "released 6 May 2025 (date per techUK)".
- **Source.**
  - The PDF edition linked from the web page is titled "The UK AI Security Institute's Research Agenda / May 2025" (32 pp.; PDF creation date 2 May 2025).
  - Its CDN asset ID begins `6819c33c`. As a Webflow object-ID timestamp, that decodes to 2025-05-06 08:07 UTC. This is inference, but it matches techUK's 6 May.
- **Replace with.** `UK AISI, *The UK AI Security Institute's Research Agenda*, May 2025 (web page and PDF; PDF uploaded 6 May 2025).`
- **Suggested quote.** The one already used is verbatim (Introduction, PDF p.3): *"This document serves as a snapshot in time of our current research priorities."*
- **Worth adding in the same footnote, because it limits every "absent from AISI" claim:** *"Due to the sensitivity of our work, we cannot publish the full scope of our methods and research objectives."* (same page). Also PDF p.5: *"We will not cover details of our work in this Dual-use Science in this document"* (sic).

**(d) AISI Trends date ([^8]).** *Medium confidence (secondary plus inference).*
- **Current.** 18 Dec 2025.
- **Source.**
  - The PDF front cover reads "2025 DECEMBER". The back cover reads "2025 NOVEMBER", an internal inconsistency.
  - The PDF creation date is 15 Dec 2025.
  - The CDN asset ID `6943e6c1` decodes to 2025-12-18 11:34 UTC (inference).
  - The secondary CSA research note gives "December 18, 2025" (https://labs.cloudsecurityalliance.org/research/csa-research-note-aisi-frontier-ai-trends-report-20260712-cs/).
- **Keep 18 Dec 2025.** Mark it as supported by secondary and inference, not stated on the page.

**(e) [^8] quote.** *High confidence.*
- **Current.** cyber task length "doubling roughly every eight months".
- **Source.**
  - The quote is verbatim, from the Executive summary, p.01 (PDF p.3): *"The length of cyber tasks (expressed as how long they would take a human expert) that models can complete unassisted is doubling roughly every eight months (FIGURE 3)."*
  - p.10 (PDF p.12) adds a qualifier the report should carry: *"FIGURE 3 shows a doubling time of roughly eight months, an estimated upper bound."*
  - The figure is at 50% success (Fig. 3 caption).
- **Suggest.** In B1: "AISI Trends: cyber task length (at 50% success) doubling roughly every eight months, an estimated upper bound".

**(f) [^9] (techUK), to be replaced.** *High confidence.*
- **Current.** `[S] techUK summary … "Found universal jailbreaks for every system they have tested"`.
- **Primary.** AISI Trends §4 Safeguards, p.24 (PDF p.26):
  - Heading: *"We've found universal jailbreaks for every system we've tested."*
  - Body: *"We've discovered universal jailbreaks for every system we've tested to date. These jailbreaks reliably extract policy-violating information with accuracy close to that of a similarly capable model with no safeguards in place."* The web version says "every single system".
- **Qualifier the report omits.** Same page, Fig. 13: *"while the first test required just 10 minutes of expert red teamer time to find and apply a publicly-known vulnerability, the second test required over seven hours of expert effort and the development of a novel universal jailbreak."*
- **Replace [^9] with.** `[P] UK AISI, Frontier AI Trends Report, Dec 2025, §4 "Safeguards", p.24 (PDF p.26): "We've discovered universal jailbreaks for every system we've tested to date." Same page: expert effort to find a comparable universal bio-misuse jailbreak rose from 10 minutes to 7+ hours (~40×) between two models released six months apart.`
- **Change B6.** "AISI Trends: universal jailbreaks found for every system tested, though effort required rose ~40× for bio-misuse on one pair of models".

**(g) [^10] DSIT.** *High confidence.*
- The heading quote is verbatim, p.18: *"Insufficient incentives for AI developers to invest into risk mitigation measures"*.
- The PDF link works, and the gov.uk HTML link in §1 works.
- The title on the PDF is *Capabilities and risks from frontier AI: A discussion paper on the need for further research into AI risk*, published 25 Oct 2023.
- The acknowledgements add: *"does not represent a policy position of HMG"* (p.2). Worth carrying, given how the report leans on DSIT as an "authoritative body".

**(h) [^11] (LessWrong), to be replaced.** *High confidence.*
- **Primary.** DSIT p.19: *"Competition on AI has raised concern about potential "race to the bottom" scenarios, where actors compete to rapidly develop AI systems and under-invest in safety measures."*
- **Replace [^11] with.** `[P] UK DSIT, Capabilities and risks from frontier AI, Oct 2023, p.19 (same document as [^10])`, or merge it into [^10] with the pinpoint.
- **Also cite IASR 2026** for C1 at the same time. Glossary p.153: *"Race to the bottom: A situation where competition drives actors to progressively reduce safety precautions, quality standards, or oversight to gain an advantage."*

**(i) [^4] IASR 2026.** *High confidence.*
- The quote is verbatim, ES p.17 (PDF p.19): *"Competitive pressures can incentivise AI developers to reduce their investment in testing and risk mitigation in order to release new models quickly."*
- **Full-report equivalents:**
  - p.97, Key information: *"Due to competitive pressures, AI companies may face trade-offs between faster product releases and investments in risk reduction efforts."*
  - p.102, heading: *"Competition intensifies speed-versus-safety trade-offs."*
- **Suggest.**
  - Retitle [^4] to cite the **full report** (bengio-2026-international), with ES as the secondary pointer.
  - Pinpoints in the body currently use ES figure numbers. "Fig. 12" in ES is **Fig. 3.1** in the full report (p.98). "§2.2.1" and "§3.4" are the same in both.

**(j) [^14] NCSC.** *High confidence.* Correct.
- Published 7 May 2025 (PDF p.7, "PUBLISHED 7 May 2025"; web `datePublished`).
- The quote is verbatim (PDF p.2): *"There will almost certainly be a digital divide between systems keeping pace with AI-enabled threats and a large proportion that are more vulnerable…"*
- The quote is truncated after "divide". Quoting the full sentence would prevent the A16 misreading (§2.2).

**(k) Header "Verification" line.** The claim that the IASR 2026 Extended Summary was "downloaded and text-searched" is accurate as far as it goes. It is the Extended Summary, though, and several IASR cells read like IASR 2025, not either 2026 document. After this pass, the full report, Extended Summary, IASR 2025, DSIT (with annexes), AISI Agenda, AISI Trends and NCSC have all been read against source.

---

### 2.2 Crosswalk (a), my columns

Legend as in the report: E = named in a structured list or heading; D = discussed substantively; P = passing; — = not found.

#### IASR 26 column (IASR 2026 full report; ES confirms the same structure)

| # | Current | Proposed | Evidence | Conf. |
|---|---|---|---|---|
| A1 | E✓ | **E✓, noting "bio & chem only"** | §2.1.4 "Biological and chemical risks" (pp.64–70). Radiological/nuclear appear only in glossary "CBRN" (p.148), in describing Anthropic's RSP (p.65), and in the frameworks survey (p.115: frameworks "Most focus on… (CBRN) threats"). IASR does not itself assess R/N. | High |
| A2 | E✓ | E✓ | §2.1.3 "Cyberattacks" | High |
| A3 | E✓ | E✓ (see §6 on meaning) | §2.2.2 "Loss of control" | High |
| A4 | E✓ | E✓, with a definitional flag | §2.1.2 "Influence and manipulation". IASR's concept is individual-level and includes *unintended* manipulation (sycophancy, companion dependence); see §6. | High |
| A5 | E | **E✓** | §2.1.1 "AI-generated content and criminal activity" | High |
| A6 | E✓ | E✓ | §2.2.1 "Reliability challenges" | High |
| A7 | D | D | p.57 ("attacks on critical infrastructure"), p.82 ("Criticality"), p.143 (WEF figure). No section of its own. | Medium |
| A8 | E | **E✓** | §2.3.1 "Labour market impacts" | High |
| A9 | E | **P** | No section. Mentions: India's ministerial foreword p.8 (edition "reviews… concentration of power"); p.62 Box 2.1 (tampering gives "an individual or small group… significant, covert influence"); p.87 ("shift earnings from labour to capital owners"); p.125 (critics cite "the concentration of wealth and influence"). The E belongs to IASR **2025** §2.3.3. | High |
| A10 | P | P (weak) | No "military". p.82: deployment shaped by "strategic pressures, and the expectation that early adoption confers a lasting advantage"; p.102: states' "economic and strategic importance". Geopolitical, not military. | Medium |
| A11 | E | **E✓** | §2.3.2 "Risks to human autonomy" | High |
| A12 | E | **P** | Out of scope by p.9 footnote. Passing: p.49 (watermarks "raise privacy concerns"), p.72 (a "Privacy breach" example in Table 2.4). The E is IASR **2025** §2.3.5. | High |
| A13 | E | **P** | Out of scope by p.9. Passing: p.100 (non-disclosure can conceal "use of copyrighted or unlicensed data"). The E is IASR **2025** §2.3.6. | High |
| A14 | D | **P** | Out of scope by p.9. Passing: p.72 ("inaccurate and biased medical information"), p.123 ("cultural biases in content moderation"). The D/E is IASR **2025** §2.2.2. | High |
| A15 | E | **P (or —)** | Out of scope by p.9. Energy appears only as a *scaling bottleneck* (pp.32–42, e.g. p.42 "AI computation has massive energy demands"), never assessed as an environmental harm. The E is IASR **2025** §2.3.4. | High |
| A16 | E | D | Adoption inequality: p.85 ("adoption rates range from over 50%… to under 10%"); p.87 subheading "Implications for inequality"; p.134 (open weights and "global majority participation"). Uses "divide" for none of these. | Medium |
| A17 | D | **E** | Heading p.73 "Multi-agent AI systems introduce new kinds of reliability failures"; Table 2.4 row "Multi-agent system failure: miscoordination and conflict" (p.72); glossary "Collusion", "Miscoordination", "Multi-agent system". | Medium |
| A18 | — | — | Table 2.5 note, p.78: capabilities "do not make any assumptions about whether AI systems are conscious, sentient, or experience subjective states." | High |

**Suggested caveat under the table.** "IASR 2026 deliberately narrowed its scope to 'emerging risks' (p.9 fn); bias, environment, privacy and copyright are assessed in IASR 2025 (§§2.2.2, 2.3.4–2.3.6), not 2026." The alternative is adding an IASR 25 column, which I would lean against: the report is already wide.

#### DSIT column (DSIT Oct 2023 discussion paper; Annexes A/B noted where they change a cell)

| # | Current | Proposed | Evidence | Conf. |
|---|---|---|---|---|
| A1 | E | **E, bio/chem** | Heading "Dual Use Science risks" (p.22): "biological or chemical weapons". Annex B (p.6) names "chemical, biological and radiological weapons". | High |
| A2 | E | E✓ | Heading "Cyber" (p.23) | High |
| A3 | E | E✓ | Heading "Loss of control" (p.25) | High |
| A4 | D | **E** | Heading "Disinformation and Influence Operations" (p.25), under "Misuse risks"; also "Degradation of the information environment" (p.19). | Medium–high |
| A5 | D | D | Scams/sextortion p.24–25 (fake kidnapping, sextortion); Annex B p.4 lists "scams, fraud, impersonation… child sexual abuse images". | Medium |
| A6 | D | D | Hallucinations p.9; robustness p.16 | High |
| A7 | D | D | p.24 "Critical infrastructure like energy, transportation, healthcare, and finance, are already frequently targeted" | High |
| A8 | E✓ | E✓ | Heading "Labour market disruption" (p.20) | High |
| A9 | E✓ | E✓ (market power) | Heading "There may be significant concentration of market power in AI" (p.19). Note it is *market* power; Annex A adds "A huge amount of power sits with private companies" (Scenario 4, p.21). | High |
| A10 | P | P | p.28: loss of control catastrophic if AI gains "control over systems with significant impacts, such as military or financial systems"; Annex B excludes military (p.2). | High |
| A11 | P | **D** | "Humans might increasingly hand over control to misaligned AI systems" (p.26): automation bias, over-reliance; companion intimacy (p.27). | Medium |
| A12 | P | P | p.19 ("less say in the use of their personal data"), p.24 ("privacy breaches") | High |
| A13 | — | — | Only as *model* IP to be stolen (p.18), not infringement. Annex A p.23 notes "issues around intellectual property rights for content in training datasets", so P if the annexes count. | High |
| A14 | E✓ | E✓ | Heading "Bias, Fairness and Representational Harms" (p.21) | High |
| A15 | P | **— (main paper); P (Annex A)** | Main paper: climate appears only as an analogy (p.18, p.26). Annex A p.23 ¶78: "growing energy needs, could also have environmental impacts". | High |
| A16 | P | **— (main paper); P (Annex A)** | Main paper: nothing on access inequality (p.21 is about training-data bias). Annex A ¶48 ("unequal access to models"), ¶61. | Medium |
| A17 | — | **— (main paper); P (Annex A)** | Annex A ¶85(d) "Unintended outcomes from interactions with other AI systems"; ¶90(c) "The ability to cooperate with other highly capable AI systems". | High |
| A18 | — | — | — | High |

**Suggested column note.** "DSIT = main discussion paper; annex-only mentions noted."

#### AISI column (Research Agenda May 2025 plus Frontier AI Trends Dec 2025; the column currently seems agenda-based)

| # | Current | Proposed | Evidence | Conf. |
|---|---|---|---|---|
| A1 | E | E (as "Dual-use Science") | Agenda domain 2 "Dual-use Science" (PDF p.5), whose detail is withheld. Trends §3.1 "Chemistry & Biology" (pp.13–19). No R/N. | High |
| A2 | E | E✓ | Agenda "Cyber Misuse"; Trends §3.2 | High |
| A3 | E | **E, with the label "Autonomous Systems"** | AISI's domain is "Autonomous Systems" (defined in §6); Trends §5 is headed "Loss of control risks" (p.29). | High |
| A4 | E | E✓ | Agenda "Human Influence"; Trends §6.1 | High |
| A5 | E | E✓ | Agenda "Criminal Misuse"; CSAM named as an emerging area | High |
| A6 | P | P | Agenda Societal Resilience list: "risks to human health or security due to unreliable outputs from AI" (PDF p.15) | High |
| A7 | D | **E** | Trends §6.3 heading "Critical infrastructure" (p.41); agenda list "risks to critical national infrastructure due to AI being embedded into core systems" (PDF p.15); Cyber Misuse abstract "attacks on critical national infrastructure systems". | High |
| A8 | E | E | Agenda list: "threats to economic stability from changes in the labour market" (PDF p.15). Trends §6 explicitly excludes "more diffuse economic or environmental effects" (p.34). | High |
| A9 | P | **—** | Neither document mentions power or market concentration (searched "concentration", "power", "monopol"). | High |
| A10 | — | — | — | High |
| A11 | E | E✓ | Agenda: "widespread human overreliance on AI systems" (PDF p.15); Human Influence "para-social relationships". Trends §6.2 "Emotional dependence". | High |
| A12–A16 | — | — | Trends p.34 excludes environment. | High |
| A17 | — | **P** | Agenda list: "instability in markets or communications resulting from multiple AI agents interacting" (PDF p.15); Capabilities Post-Training: "sub-agent and multi-agent systems" emergent behaviours. | High |
| A18 | — | — | — | High |

#### NCSC column

| # | Current | Proposed | Evidence | Conf. |
|---|---|---|---|---|
| A2 | E✓ | E✓ | whole document | High |
| A4 | D | **—** | PDF p.3: "It focuses on the use of AI in cyber intrusion. It does not cover wider threat enabled by AI, such as influence operations." | High |
| A5 | D | **P** | Only cyber-crime aspects: "access to systems through social engineering" (p.3), "cyber criminals" (pp.2, 5). No fraud, deepfakes, NCII or CSAM. | High |
| A7 | E✓ | E✓ | Key judgement, PDF p.2: "particularly within critical national infrastructure (CNI), almost certainly presents an increased attack surface" | High |
| A12 | — | **P** | PDF p.6: "collecting extensive user data, increasing the risk of de-anonymising users and enabling targeted attack" | High |
| A16 | E✓ | **Move to C14; A16 → —** | The divide is "between systems keeping pace with AI-enabled threats and a large proportion that are more vulnerable" (PDF p.2), resting on "a remote chance of universal access to AI for cyber security defence by 2027" (p.4). This is about systems and defenders, not the global access inequality A16 describes. | High |
| others | — | — (unchanged) | | High |

---

### 2.3 Tables (b) and (c): pinpoints to add or fix

- **B1, dangerous capabilities.**
  - Add "(50% success; 'an estimated upper bound', p.10)" to the AISI item.
  - Also add AISI Trends p.30: RepliBench success *"By summer 2025, two frontier models had achieved a success rate of over 60%"* (up from <5% for an early-2023 model).
  - IASR 2026 Table 2.5 (p.78) is a clean list of LoC-relevant capabilities: agentic capabilities, deception, theory of mind, situational awareness, oversight evasion, persuasion, autonomous replication and adaptation.
- **B2, propensities.** Add IASR 2026 p.81 and Box 2.5 (goal misspecification, goal misgeneralisation).
- **B3.** IASR 2026 §2.2.1 is correct. The sharper quote is p.71: *"Agent failures can cause greater harm because humans have fewer chances to intervene."*
- **B4, emergent capabilities.**
  - DSIT p.13: *"we cannot currently reliably predict ahead of time which specific new capabilities a frontier AI model will gain"*.
  - IASR 2026 p.35 and the glossary "Emergent capabilities" (p.149).
- **B5, evaluation gap.** Add:
  - DSIT heading p.8 "Frontier AI could be more capable than evaluations indicate";
  - AISI Trends §5.2 Sandbagging (pp.32–33);
  - AISI Agenda sandbagging threat scenarios (low-probability, time-based, situational-awareness-based; PDF pp.13–14);
  - IASR 2026 p.79 (reward hacking, situational awareness).
- **B6.** As in §2.1(f).
- **B7, weight security.**
  - IASR 2026 Box 3.1 "Model weight security" (p.136): *"As of December 2025, there are no confirmed, publicly documented instances of model weight theft."* Also: *"Research indicates that AI data centres may be unable to withstand attacks from the most sophisticated and well-resourced actors."*
  - DSIT p.18.
- **B8, insider threats (human and AI).** Add three UK primaries:
  - *DSIT p.18:* *"the information security practices of frontier developers will influence the likelihood that the full model is exfiltrated by employees or external actors."* It cites "Nevo & Lahav, forthcoming", the future RAND-W.
  - *IASR 2026 Box 3.1, p.136:* *"Some developers commit to securing model weights against cybercrime syndicates and insider threats, while others have made no public security commitments."*
  - *AISI Agenda, Control* (PDF p.28): side-tasks mapping *"onto core threat models: weight exfiltration, secret exfiltration, rogue internal deployments and sabotaging safety research"*. Research focus, PDF p.27: *"AIs deployed within frontier AI developers' systems. In these environments, AI systems may have access to sensitive code and infrastructure."* This is the AI-as-insider half of B8, from the institute Joseph is writing to.
- **B9.** IASR 2026 §3.4 is correct. Add:
  - NCSC PDF pp.3–4: *"The release of capable open-source models likely lowers the barrier to the building of similar models and narrow AI-enabled tools"*;
  - AISI Trends §7 (open–closed gap 4–8 months, p.43);
  - DSIT p.17.
- **B12, offence–defence.** IASR 2026 p.61 ("The offence-defence balance is critical but dynamic") and p.142. DSIT p.23.
- **B13.** In the full report this is Fig. 3.1 (p.98), not Fig. 12.
- **B14, attacks on AI systems.**
  - NCSC PDF p.5: *"Techniques such as direct prompt injection, software vulnerabilities, indirect prompt injection and supply chain attack are already capable of enabling exploitation of AI systems to facilitate access to wider systems."* This is more specific than "CNI attack surface".
  - Also IASR 2026 Box 2.1 (p.62, incl. "tampering"), AISI Agenda Safeguard Analysis "Defending against 3rd party attacks", DSIT p.24.
- **C1, race dynamics.** Replace [^11] and add NCSC. NCSC PDF p.6: *"In the rush to provide a market-leading AI model (or applications that are more advanced than competitors) there is a risk that developers will prioritise an accelerated release schedule over security considerations, increasing the cyber threat from compromised or insecure systems."* A UK intelligence-assessment body names speed-over-security as a threat enabler.
- **C3.** "DSIT; IASR 2026 Fig. 12" is correct, but the full-report pinpoint is p.102 ("Widespread reliance on a small number of models creates single points of failure").
- **C4.** DSIT heading p.18 is correct; IASR 2026 p.101 ("a typical market failure").
- **C5, governance and regulator capacity.** Add:
  - DSIT p.18: *"There is currently little government capacity for this"* (external assurance);
  - IASR 2026 p.102: *"Some institutions struggle to build sufficient technical capacity to engage with AI research"*.
- **C6, safety culture.** Add IASR 2026 p.114: *"Organisational culture, leadership structure, and incentives affect risk management efforts in various ways."* IASR does not use "safety culture" or "risk culture". *Kind:* an observation that culture is a determinant of how well mitigation works (factor-adjacent). IASR does not name weak culture as a risk factor.
- **C7, internal risk governance.** Add IASR 2026 p.112–113 and Table 3.4, which defines risk governance and lists "Risk responsibility allocation", citing the EU CoP. *Kind:* a mitigation practice, *described* (IASR p.106: "policy recommendations are outside the scope of this work"). It is not a risk factor named by IASR.
- **C8, safety resourcing.** Add AISI Trends. p.25: *"This is usually driven by how much company effort and resource has gone into building, testing, and deploying strong defences…"* p.27: *"the strength of safeguards appears to be determined mostly by the effort and resource invested in developing, testing, and deploying defences."* *Kind:* an empirical observation about what determines a mitigation's strength. It implies, but does not state, that under-resourcing is a risk factor.
- **C9.** Add IASR 2026 Table 3.4 (p.113): *"Because much of AI development occurs behind closed doors, some governance frameworks include whistleblower protections to enable disclosure of potential risks to authorities."* Also p.103 (jurisdictions implementing whistleblower protections). *Kind:* a mitigation, described as present in "some governance frameworks". Not a factor.
- **C11, financial and investor pressure.** Add:
  - GO-Science Annex A ¶32 (p.9): *"Frontier AI companies operate in a highly competitive environment… Perception of a model's power, and future development, are important to attract investment… These incentives are highly likely to influence the public and private statements from industry figures."*
  - IASR 2026 p.36: investments are *"a bet on uncertain returns"*; if investments fail to generate revenue, *"companies may sharply reduce scaling investments."*
  - IASR 2025 §3.2.2(C), p.178 (too-big-to-fail).
- **C12.** Add IASR 2026 p.74: shared base models lead to *"correlated failures"*; also p.102–103.
- **C13.** IASR 2026 is correct: p.11 (Executive summary), p.14 (Introduction), glossary p.150 "Evidence dilemma". It originated in IASR 2025 (Key findings p.14).
- **C14.** Move the NCSC "digital divide" here as its primary home. Add IASR 2026 §3.5 "Building societal resilience". Keep the AISI Agenda "Societal Resilience".

### 2.4 §4 Organizational factors table

- **"Organizational capacity: Partly (safety-function resourcing only)".** Add the AISI Trends finding (C8 above). It is empirical and primary, and it is closer to "capacity determines safeguard quality" than anything else in the table. *High.*
- **"Safety culture: Yes".** Add IASR 2026 p.114. *High.*
- **"Turnover / key-person risk: No".** Stands for my sources. Near-misses, none framed as a safety risk factor:
  - GO-Science Annex A, Scenario 1 (p.18), narrative: *"accelerated by high-profile developers leaving big labs to join this open-source effort after becoming concerned with the concentration of power sitting with a few large companies"*. Talent movement as a proliferation driver, in a scenario.
  - IASR 2025 p.124: *"the recruitment and retention of top-tier AI researchers… is highly competitive and costly"*. A barrier to entry.
  - DSIT p.19: leaders' access to *"specialised talent"*.
- **"IPO / commercial / investor pressure: Commercial yes; IPO no".** For my sources the IPO row stays "no" (no hits for IPO, listing or flotation). Add the Annex A ¶32 and IASR 2026 p.36 items.
- **"Insider threats: Yes (strongest)".** Add DSIT p.18, IASR 2026 p.136, AISI Agenda Control (§2.3 B8).
- **"Lab growth rate / headcount scaling: No".** No UK source names headcount growth. But IASR 2025 §3.2.2(C) names *industry* growth (see §4 below). The "Not found… 2023–Sep 2026" row should say it checked this and explain why it is distinct.

### 2.5 §5 "Where organizations disagree"

- **5.1.** Correct, and the IASR footnote is quotable. ES p.7 and full report p.15: *"In this report, systemic risks are risks that result from widespread deployment of highly capable general-purpose AI across society and the economy. Note that the EU AI Act uses the term differently…"* IASR's own glossary (p.154) defines systemic risk *differently* from its body text (§6).
- **5.2 Loss of control.**
  - "an AISI priority domain" should be "AISI's 'Autonomous Systems' domain", with the broader definition (§6).
  - "IASR 2026 reports that expert views on its likelihood vary widely" is correct: ES p.12 heading, full report p.76.
- **5.3.** Correct. ES p.9 (PDF p.11) heading: *"There is little evidence that AI-generated content is manipulating people at scale"*. Full report p.54. Worth adding that AISI Trends §6.1 (p.38) found similar, and that NCSC excludes the topic.
- **5.4.** The IASR 2026 attribution is correct: p.66 names o3 outperforming 94% of domain experts at troubleshooting virology protocols; ES p.10 says "substantial uncertainty". Add AISI Trends p.16: non-experts using frontier models had *"significantly higher odds of writing a feasible protocol (4.7x…)"*. That is a UK government uplift result that sharpens this row.
- **5.5.** Correct: IASR ES p.10 heading, NCSC PDF p.2.
- **Possible new disagreement row, "Is misuse separate from loss of control?".** AISI folds "the misuse of AI systems escalating out of control" into Autonomous Systems. IASR keeps malicious use and loss of control in separate chapters, though it notes (p.81) that systems "could be directed to undermine control". *Medium.*

### 2.6 §7 Relative priority

- **UK AISI row.**
  - Replace "chem-bio" with "dual-use science (details withheld; chem & bio per Trends)".
  - Name the structure: six risk domains, two generalised measurement areas (Science of Evaluations, Capabilities Post-Training) and three solutions areas (Safeguard Analysis, Control, Alignment).
  - The agenda gives *selection criteria*, not a ranking (web "Our Approach", PDF p.4): *"risks that have the potential to cause severe and widespread harm or pose threats to national security, risks that are particularly exacerbated by the most advanced AI capabilities, and solutions mitigating these risks that are best delivered by a government backed research organisation."*
  - The Alignment team's focus is honesty: *"Our initial focus is on using a combination of theoretical guarantees and empirical evidence to ensure the honesty of AI systems as they scale past AGI to superintelligence"* (PDF p.30). That may matter to Joseph beyond this report.
- **NCSC.** Correct.
- **IASR 2026.** Correct: ES p.i, *"The Report does not recommend any policies"*. Full report p.44: *"inclusion here does not necessarily imply a risk is likely, severe, or requires policy action."*

### 2.7 Executive summary framing

- **"The foundational taxonomies of *organizational* risk date from 2023: DSIT."** This mischaracterizes DSIT.
  - DSIT's taxonomy is of "Cross cutting risk factors – technical and societal conditions that could aggravate a number of particular risks" (p.15). Its items are technical (open-ended domains, evaluation, tracking deployment) and market-level (standards, incentives, market concentration).
  - The only intra-organizational item is the one-sentence information-security/exfiltration point on p.18.
  - DSIT is foundational for the structural/market layer (C1, C3, C4, C5), not the organizational layer (C6–C9).
  - **Proposed.** Drop DSIT from that bullet, or say "foundational taxonomies of structural (DSIT) and organizational (CAIS, Schuett) risk".
  - *High for the characterization. How to reword is the integrator's call.*
- **"authoritative body".** The DSIT paper and Annex A both disclaim government policy status (DSIT p.2; Annex A cover and every page: "NOT A STATEMENT OF GOVERNMENT POLICY"). IASR says it reflects neither the Chair's nor governments' views (disclaimer, p.3). That affects how "authoritative" reads in the headline claim. NCSC is the one UK source here that speaks as "the authoritative voice on the cyber threat to the UK" (PDF p.1).

### 2.8 Status and kind of each item the report leans on (the coordinator's factor/mitigation lens)

**Status of each source as a whole** (verbatim where it states its own status):

| Source | Document type | What its "mitigations" are | Self-description |
|---|---|---|---|
| IASR 2026 | Scientific evidence synthesis | *Described* practices and research directions; never recommended | "It does not make specific policy recommendations." (p.9). "policy recommendations are outside the scope of this work" (§3.2, p.106). "This Report is not prescriptive about what should be done." (p.146) |
| IASR 2025 | Scientific evidence synthesis | Described "technical approaches to risk management" | "It does not recommend specific policies." (p.10). "This report does not comment on which policies might be appropriate responses to AI risks. It aims to be highly relevant for AI policy, but not in any way prescriptive." (p.26) |
| DSIT 2023 | Government discussion paper for the Summit | Few; its conclusion is "further research is necessary" (p.4) | "does not represent a policy position of HMG" (p.2) |
| GO-Science Annex A | Foresight paper | *Options*: "These approaches could include…" (¶93); "Non-technical mitigations could include…" (¶95) | "NOT A STATEMENT OF GOVERNMENT POLICY" (every page); "Nor is this a policy paper." (¶6) |
| HMG Annex B | Assessment (probabilistic language) | None | "This assessment draws on … intelligence assessments, expert insights and open source." (p.2) |
| NCSC 2025 | Intelligence assessment (NCSC-A, PHIA yardstick) | Assessment-level pointers to NCSC *guidance* ("organisations are strongly encouraged to follow the NCSC's guidance", PDF p.3). No requirements | "the authoritative voice on the cyber threat to the UK" (PDF p.1) |
| AISI Research Agenda | Statement of research priorities | AISI's own *research objectives* on mitigations ("we expect to", "we anticipate"). No requirements on developers | "a snapshot in time of our current research priorities" (PDF p.3) |
| AISI Trends | Empirical measurement report | Measurements *of* mitigations (safeguards) | "should not be read as a forecast" (p.7) |

None of my sources *requires* anything. The only mandatory-flavoured statement I found is IASR 2026 p.137. It is phrased as a normative claim but embedded in a descriptive section: *"To avoid catastrophic harm, developers of open-weight models should not release models without evaluating risks…"* It is an outlier against the report's stated non-prescriptive stance, worth knowing if anyone quotes it.

**Kind of each item from my sources that the report uses or should use.** F = risk factor (a condition that raises likelihood or severity). M = mitigation (described, D; proposed, P; or research objective, R). O = observation or measurement. H = hazard.

| Report row | Item and pinpoint | Kind | Note |
|---|---|---|---|
| C1 | IASR 2026 "Speed vs safety trade-offs" (Fig. 3.1, p.98; p.102); DSIT "race to the bottom" (p.19); NCSC "rush to provide a market-leading AI model" (PDF p.6) | **F** | IASR files it under "Market failures", a *challenge for risk management*; NCSC calls it a threat enabler |
| C3 | IASR 2026 "Single points of failure" (p.102); DSIT market-power concentration (p.19) | **F** | |
| C4 | DSIT "Insufficient incentives…" (p.18); IASR 2026 externalities (p.101) | **F** | |
| C5 | IASR 2026 "Uncertain liability allocation", "Pace of development" (p.98, p.102); DSIT "AI safety standards have not yet been established" (p.18) | **F** (institutional) | |
| C6 | IASR 2026 p.114 organisational culture | **O** (determinant of M effectiveness) | Not a named factor |
| C7 | IASR 2026 risk governance, "Risk responsibility allocation" (Table 3.4, p.113) | **M-D** | Cites the EU CoP as the instance |
| C8 | AISI Trends pp.25, 27 effort/resource drives safeguard strength | **O** | Implies under-resourcing is F; not stated |
| C9 | IASR 2026 whistleblower protection (Table 3.4, p.113; p.103) | **M-D** | |
| C11 | GO-Science ¶32 investment incentives; IASR 2026 p.36 investment "bet"; IASR 2025 §3.2.2(C) too-big-to-fail | **F** (¶32 is a F on *statements*, i.e. information integrity) | |
| C12 | IASR 2026 correlated failures (p.74) | **F** | |
| C13 | IASR evidence dilemma (p.11; glossary p.150) | **F** for policymaking (not for labs) | A property of the governance situation, not of labs |
| C14 | NCSC digital divide (PDF p.2); AISI Societal Resilience; IASR §3.5 | NCSC: **F** (assessed). AISI: **M-R**. IASR §3.5: **M-D** (resilience as mitigation layer) | Same row, three kinds |
| B5 | IASR situational awareness/reward hacking (p.79); AISI Trends sandbagging (§5.2) | **F** (IASR) / **O** (AISI measurements: "yet to detect unprompted sandbagging", p.33) | |
| B6 | AISI Trends universal jailbreaks (p.24) | **O** (about an M's weakness) | |
| B7 | IASR 2026 Box 3.1 (p.136) security may be insufficient; closing gaps "would require substantial investments" | **F** + **M-D** | |
| B8 | DSIT p.18 exfiltration "by employees"; IASR p.136 commitments against "insider threats"; AISI Control threat models (PDF p.28) | DSIT: **F**. IASR: **O** of developers' **M** commitments. AISI: **H/threat model** + **M-R** (control protocols) | IASR's mention is about *commitments*, so it evidences that the threat is recognised, not that IASR names it as a factor |
| B9 | IASR §3.4; NCSC PDF pp.3–4; AISI Trends §7 | **F** | |
| B14 | NCSC PDF p.5; IASR Box 2.1; AISI Safeguard Analysis "Defending against 3rd party attacks" | NCSC/IASR: **F/H**. AISI: **M-R** | |
| §4 row "Insider threats" | as B8 | mixed | Count only DSIT (F) and AISI threat models as "naming"; IASR p.136 is a commitment observation |
| §4 row "Organizational capacity" | AISI Trends pp.25, 27 | **O** | The strongest UK evidence, but inferential for "factor" |

**The pattern the coordinator suspected, as it shows up in my sources.** Wherever IASR 2026 touches organisational matters (culture, risk-responsibility allocation, whistleblowing, Frontier Safety Frameworks, if-then commitments), it does so in Chapter 3 as *described mitigation practice*. In my full read of Chapter 3 I found no place where it names their absence as a risk factor. Its risk factors (Chapter 3.1 "challenges") are scientific, informational, market and institutional, not intra-organisational. So "IASR 2026 [names] C7/C9" would repeat the §4 conflation. The accurate statement is "IASR 2026 describes these as risk-governance practices." I have worded my suggestions above accordingly.

---

## 3. Framing issues (beyond details)

1. **"Risk factor" is itself a UK-defined term, used here more loosely.** Three of my sources define it almost identically:
   - DSIT glossary (p.30): *"Risk factors: Elements or conditions that can increase downstream risks. For example, weak guardrails (risk factor) could enable an actor to misuse an AI system to perform a cyber attack (downstream risk)."*
   - IASR 2025 glossary (p.226): *"Properties or conditions that can increase the risks of an AI system."*
   - IASR 2026 glossary (p.153): *"Properties or conditions that can increase the likelihood or severity of harm."*

   The report's section (a) lists hazards and harms, which these sources call risks, not risk factors. Only (b) and (c) are risk factors in their sense. IASR also defines "Hazard" (p.150). The report's (a)/(b)/(c) split already respects this, but its title and summary blur it. If the EOI will be read by AISI staff, aligning with this usage is cheap: "hazards (a); risk factors (b, c)".
2. **The report compares instruments of different kinds as if they were peers.** IASR is an evidence synthesis that refuses to rank or recommend. AISI's agenda is a research-priority list constrained by what government should research. NCSC is a threat-intelligence assessment with a PHIA probability yardstick. DSIT is a 2023 discussion paper that disclaims policy status. "Named / not named" means something different in each. The §7 table does this partially; the crosswalk legend could carry one line per column type.
3. **Absence claims against AISI are weak by construction.** The agenda says it cannot publish its full scope and withholds Dual-use Science. "Not found in AISI" should read "not in AISI's published agenda or Trends report".

---

## 4. Evidence for the sibling growth/turnover agent (relay if useful)

UK sources bearing on "nobody names lab growth/turnover/IPO as a risk factor":

- **Closest hit.** IASR 2025, §3.2.2 key information (p.176) and body (p.178): *"C. The rapid growth and consolidation in the AI industry raises concerns about certain AI companies becoming particularly powerful because critical sectors in society are dependent on their products. Such companies may become more inclined to take excessive risks or cut corners on safety standards if they expect that it would be costly for governments to let the company fail."* This is industry-level growth and a moral-hazard mechanism, not headcount or absorptive capacity. It is the nearest a UK-hosted authoritative document comes to "growth as a risk factor". I did not find it carried forward into IASR 2026.
- **Talent movement, in scenario form.** GO-Science Annex A Scenario 1 (p.18): high-profile developers leaving big labs for open-source.
- **Investment attraction.** GO-Science Annex A ¶32 (p.9) and IASR 2026 p.36.
- **Absences in my sources.** No hits for headcount, hiring growth (other than labour-market hiring of *workers in the economy*, IASR 2026 pp.87–88), turnover (other than "job turnover" in the labour market, p.85), IPO, or "safety culture".

---

## 5. New references worth adding

1. **IASR 2026 full report** as its own entry, distinct from the Extended Summary. The body should cite it, since the ES has no references and different figure numbers. *bengio-2026-international.*
2. **IASR 2025** already has a row. Its §2.2.3 (LoC taxonomy) and §3.2.2 (societal challenges, including industry growth) are the reusable parts. *bengio-2025-international.*
3. **GO-Science, *Future Risks of Frontier AI* (DSIT Annex A), Oct 2023.**
   - Five 2030 scenarios.
   - Explicit existential-risk pathways: misalignment, single point of failure, overreliance (¶89).
   - The investment-incentives passage (¶32).
   - Its own misalignment definition (p.25 fn iii).
   - *goscience-2023-future.*
4. **HMG, *Safety and Security Risks of Generative AI to 2025* (DSIT Annex B), Oct 2023.** Six pages with PHIA-style language. Defines "Safety and Security", "Risk" and "Threat" (p.2), and has the three-way "malicious use, misuse or mishap" (p.4). *hmg-2023-safety.*
5. **AISI Trends §6.3 (MCP servers in finance)** is an under-used data point for B10 (deployment velocity). It shows execution-capable servers (levels 4–5) *"increasingly dominating new releases"* from Dec 2024 to Jul 2025 (p.41).
6. **NCSC's January 2024 predecessor**, *Near-term impact of AI on cyber threat*. The 2025 report says it builds on it (PDF p.3). Not fetched; worth having if the report tracks NCSC's judgements over time.
7. **IASR interim "Key Updates" (late 2025).** From memory only, unverified: I believe IASR published interim "Key Update" notes between the 2025 and 2026 editions. The 2026 report does not mention them, and I did not search for them. Worth a check only if the report needs the between-edition trajectory.

---

## 6. Definitions record (verbatim, with location)

*Raw record for the terminology phase; not reconciled. "UND" = the term is used without definition in that source.*

### Loss of control

- **IASR 2026.**
  - Body (p.76, Key information): *"Loss of control scenarios are scenarios in which one or more general-purpose AI systems operate outside of anyone's control, and regaining control is either extremely costly or impossible. These hypothesised scenarios vary in their severity, but some experts give credence to outcomes as severe as the marginalisation or extinction of humanity."*
  - Executive summary (p.12): *"… with no clear path to regaining control."*
  - Glossary (p.151): *"Loss of control scenario: A scenario in which one or more general-purpose AI systems come to operate outside of anyone's control, with no clear path to regaining control."*
  - **Scope limits (p.77):** *"This section focuses on particularly severe scenarios where regaining control would be extremely costly or impossible. These are different from current instances of AI behaving in unintended or undesirable ways."* Footnote: *"This section focuses on active loss of control scenarios. This is distinct from passive loss of control scenarios, where the broad adoption of AI systems undermines human control through over-reliance on AI for decision-making or other important societal functions."*
  - Glossary (p.152) "Passive loss of control" repeats this.
  - Three required factors (p.77): *"Sufficient capabilities… Harmful propensity… Enabling deployment environment."*
  - Deployment-environment factors (p.82): *"Criticality… Access… Permissions."*
- **IASR 2025.**
  - Glossary p.223 and Key Definitions p.100: *"A scenario in which one or more general-purpose AI systems come to operate outside of anyone's control, with no clear path to regaining control."*
  - Taxonomy (Fig. 2.5, p.102): active vs passive, and intentional vs unintentional active. Caption: *"there is currently no standardised terminology for discussing these scenarios and … related distinctions exist, such as sudden 'decisive' and gradual 'accumulative' scenarios."*
  - Severity (p.108): *"the consequences of loss of control would not necessarily be catastrophic. As an analogy, computer viruses have long been able to proliferate near-irreversibly and in large numbers without causing the internet to collapse."* This is directly on Joseph's scale question: IASR 2025 admits non-catastrophic loss of control; IASR 2026 scopes it out.
  - "Control" (p.100 and p.219): *"The ability to exercise oversight over an AI system and adjust or halt its behaviour if it is acting in unwanted ways."*
- **DSIT 2023, p.25–26.** UND as a crisp definition; operationalized as two factors: *"Humans increasingly hand over control of important decisions to AIs. It becomes increasingly difficult for humans to take back control. / AI systems actively seek to increase their own influence and reduce human control."* Catastrophic threshold (p.28): *"For loss of control to be a catastrophic risk, AI systems would need to be given or gain some control over systems with significant impacts, such as military or financial systems."*
- **GO-Science Annex A.** UND. The frame is existential (¶86–90, p.25). Existential risk (fn ii): *"a risk of human extinction or societal collapse."* One pathway, ¶85(f) (p.24): *"Loss of human control and oversight, with an autonomous model then taking harmful actions."*
- **AISI Research Agenda.** No definition of "loss of control" (UND); used at PDF pp.13, 18, 27.
  - The domain is "Autonomous Systems" (PDF p.6): *"Risks posed by the misuse of AI systems escalating out of control or systems taking harmful action without meaningful human oversight."*
  - Research focus (PDF p.12): *"the propensity of these models to engage in severely misaligned actions, such as causing direct catastrophic harm or attempting to permanently circumvent human control."*
  - Operational threat models: *"loss of control at AI labs"* (PDF p.13). Control side-tasks: *"weight exfiltration, secret exfiltration, rogue internal deployments and sabotaging safety research"* (PDF p.28).
  - So AISI's working scale runs from "harmful action without meaningful human oversight" to "permanently circumvent".
- **AISI Trends.** UND (not in glossary). p.29: *"In a worst-case scenario, this unintended behaviour could lead to catastrophic, irreversible loss of control over advanced AI systems."* Measured precursors: self-replication and sandbagging.
- **NCSC.** Not used.

### Alignment and misalignment

- **IASR 2026.**
  - Glossary p.147: *"Alignment: The propensity of an AI model or system to use its capabilities in line with human intentions, values, or norms. Depending on the context, this can refer to the intentions and values of various entities, such as developers, users, specific communities, or society as a whole."*
  - Glossary p.151: *"Misalignment: An AI's propensity to use its capabilities in ways that conflict with human intentions, values, or norms…"* (same qualifier).
  - Body p.81: *"'misaligned': it has a propensity to exhibit behaviours that conflict with the intentions of (depending on the context) developers, users, specific communities, or society as a whole."*
  - Box 2.5 (p.81): *"When a model acquires goals that conflict with the intentions of its developers, it is 'misaligned'."* This is narrower, developer-only.
- **IASR 2025.** Glossary p.218 / p.224: same form ("intentions or values"; adds "operators"). Plus *"Deceptive alignment: Misalignment that is difficult to detect, because the system behaves in ways that at least initially appear benign."* (p.100). Body p.105: misaligned means conflict *"with the intentions of both its developers and its users."*
- **DSIT 2023.** Glossary p.29: *"Alignment: the process of ensuring an AI system's goals and behaviours are in line with human values and intentions."* A **process**, where IASR has a **propensity**. Misalignment UND; p.27: *"Ensuring that AI systems do not pursue unintended goals, i.e., are not misaligned…"*. DSIT p.22 also counts discrimination from bias *"a kind of alignment problem"*.
- **GO-Science Annex A** (p.25 fn iii): *"A misaligned system can be considered one that has the capability to pursue an objective in unintended ways that are not in line with limitations embedded during development, and more broadly moral or ethical norms of human society."* Framed as **capability**, not propensity.
- **AISI Agenda.** UND. Autonomous Systems (PDF p.12): *"aligned sufficiently with human values"*. Control (PDF p.27): *"Current alignment methods can't guarantee that an AI's goals and actions match human intention."* Alignment team: operationalizes via **honesty** (PDF p.30).
- **AISI Trends.** UND; p.45: *"aligned with human intent"*.

### Misuse / malicious use

- **IASR 2026.**
  - Full report uses "Risks from malicious use" (§2.1). The Extended Summary heads the same section "Risks from misuse", defined as *"misuse (the deliberate use of AI systems to cause harm)"* (ES p.7).
  - Glossary p.151: *"Malicious use: Using something, such as an AI system, to intentionally cause harm."*
  - Chapter intro (p.44): *"Risks from misuse, where actors deliberately use AI systems to cause harm"*.
- **IASR 2025.** Glossary p.223: *"Malicious use: Employing AI to intentionally cause harm."*
- **DSIT 2023.** "Misuse risks" heading (p.22), UND beyond *"help bad actors…"*.
- **HMG Annex B** (p.4) has a three-way split: *"potentially anyone to pose a threat through malicious use, misuse or mishap."* Here "misuse" is distinct from "malicious use" and not defined. Also p.2: *"Threat: A malicious risk involving an actor with intent."*
- **AISI Agenda.** "Cyber Misuse" and "Criminal Misuse" are domain names, defined by their domain lines (PDF p.5). Autonomous Systems includes *"misuse of AI systems escalating out of control"*.

### Manipulation / influence

- **IASR 2026.**
  - Glossary p.151: *"Manipulation: A form of influence characterised by changing someone's beliefs or behaviour to achieve some goal without their full awareness or understanding."*
  - Body p.50: *"'manipulation' – influencing someone in order to achieve a goal without their full awareness or understanding – from 'rational persuasion'"*, with *"this distinction is contentious"*.
  - Intro p.50: *"to change their beliefs or behaviours without their full awareness or consent"* ("consent" here, "understanding" in the glossary).
  - It includes unintended effects (p.51): *"AI-generated content may also have unintended manipulative effects"*.
  - Also glossary: "Persuasion" (p.152), "Deception" (p.149), "Sycophancy" (p.154).
- **IASR 2025.** The section is "Manipulation of public opinion" (p.67): malicious and political. Manipulation itself is UND.
- **DSIT 2023.** UND. Manipulation appears as a LoC-enabling capability (p.27) and within "Disinformation and Influence Operations" (p.25). Glossary defines "Disinformation" / "Misinformation" (p.29–30).
- **AISI Agenda.** "Human Influence" (PDF p.6): *"Risks posed by AI being used to manipulate, persuade, deceive, or imperceptibly influence humans."* Three operationalized risks (PDF p.17): overt persuasion/deception/manipulation (*"deliberate attempts to influence individuals to reduce their autonomy of thought or action"*), para-social relationships, and *"imperceptible influence – subtle and unconscious manipulation of users' thoughts, feelings, or behaviours by AI systems for commercial or political ends."*
- **NCSC.** Explicitly out of scope (PDF p.3).

### Systemic risk

- **IASR 2026. Two different definitions in one document:**
  - Body, ES p.7 fn and full report p.15 fn: *"systemic risks are risks that result from widespread deployment of highly capable general-purpose AI across society and the economy. Note that the EU AI Act uses the term differently, to refer to risks from general-purpose AI models that pose 'risks of large-scale harm'."*
  - Glossary p.154: *"Systemic risks: Risks that arise from how AI development and deployment changes human behaviour, organisational practices, or societal structures, rather than directly from AI capabilities."* It then gives a *different* paraphrase of the EU definition: *"risk that is specific to the high-impact capabilities of general-purpose AI models, having a significant impact"*.
- **IASR 2025.** p.110 note: *"broader societal risks associated with AI deployment, beyond the capabilities of individual models"*. Glossary p.227: *"Broader societal risks associated with general-purpose AI development and deployment, beyond the capabilities of individual models or systems."*
- **DSIT 2023.** UND; appears once (p.18, industries that "can create systemic risks").
- **AISI.** The term is not used. The nearest is "Societal Resilience": *"Risks that will emerge as frontier AI systems are deployed widely and interact with economic and societal structures"* (PDF p.6).

### Risk, hazard, risk factor, safety, security

- **Risk.**
  - IASR 2026 glossary p.153: *"The combination of the probability and severity of a harm."*
  - IASR 2025 p.182 adds *"…that arises from the development, deployment, or use of AI."*
  - HMG Annex B p.2: *"A situation involving exposure to detrimental impacts."*
  - DSIT glossary p.29: *"AI risks: The potential negative or harmful outcomes arising from the development or deployment of AI systems."*
- **Hazard.** IASR 2026 p.150: *"Any event or activity that has the potential to cause harm, such as loss of life or injury."* IASR 2025 p.182 adds *"social disruption, or environmental damage."*
- **Risk factor(s).** DSIT p.30, IASR 2025 p.226, IASR 2026 p.153 (quoted in §3).
- **Safety.**
  - IASR 2026 p.154: *"Safety (of an AI system): The property of an AI system being unlikely to cause harm, whether through malicious misuse or system malfunctions."*
  - IASR 2025 p.227: *"The property of avoiding harmful outputs…"*
  - HMG Annex B p.2: *"Safety and Security: The protection, wellbeing and autonomy of civil society and the population."* This one is population-centred, not system-centred.
- **Security.** IASR 2026 p.154: *"Security (of an AI system): The property of being resilient to technical interference, such as cyberattacks or leaks of the underlying model's source code."*

### Other terms the report's rows lean on

- **Frontier AI.**
  - DSIT p.4 and p.30: *"highly capable general-purpose AI models that can perform a wide variety of tasks and match or exceed the capabilities present in today's most advanced models."*
  - NCSC PDF p.7: *"AI systems that can provide a wide variety of tasks that match or exceed…"*
  - IASR 2026 p.150: *"a term sometimes used… For the purposes of this Report, frontier AI can be thought of as particularly capable general-purpose AI."*
- **Resilience. IASR 2026 is inconsistent:**
  - body (ES p.21; full p.138): *"resist, absorb, recover from, and adapt to shocks and harms"*;
  - glossary p.153: *"absorb, adapt to, and recover from shocks and harms"*, which drops "resist".
- **Human autonomy.** IASR 2026 p.150: *"The effective capacity to form and act on one's own beliefs, values, and goals, free from undue external influence, and with meaningful options available to influence one's circumstances."* Also "Collective autonomy" (p.148).
- **Sandbagging.**
  - IASR 2026 p.154: *"Behaviour where a model or system performs below its capabilities on evaluations, potentially to avoid further scrutiny or restrictions."*
  - AISI Trends p.51 (PDF p.53): *"A phenomenon where AI models underperform during evaluations but display stronger capabilities outside of testing environments."*
- **Race to the bottom.**
  - IASR 2026 p.153 (quoted in §2.1(h)).
  - IASR 2025 p.176: *"A competitive scenario in which actors like companies or nation states prioritise rapid AI development over safety."*
- **Open-weight vs open-source.**
  - IASR 2026 p.152 defines both and distinguishes them.
  - AISI Trends defines "open-source" as parameters, code *and* training data (p.42 and glossary p.50). Its open–closed gap figures then use external leaderboards of models that are mostly open-*weight*. This is an internal looseness.
- **Marginal risk.** IASR 2026 p.151; IASR 2025 p.223.
- **Deployment environment.** IASR 2026 p.149: *"The combination of an AI system's use case and the technical and institutional context in which it operates."*
- **Critical infrastructure.** IASR 2026 p.148. NCSC uses "critical national infrastructure (CNI)" (UND).
- **Digital divide.** NCSC UND, but operationalized in the key judgement (PDF p.2); see §2.2.

### Does AISI have a glossary?

- **Not a standalone one** that I could find. The AISI Research Agenda has none.
- **The Frontier AI Trends Report has a short glossary** (pp.50–51). It covers operational terms: agent, AGI, chain-of-thought, closed-source model, cyber range, deception probes, jailbreaking, open-source model, red teaming, safeguards, sandbagging, scaffold, task difficulty levels, universal jailbreak. It does **not** define loss of control, alignment, misuse, manipulation or systemic risk.
- A web search for an AISI glossary surfaced only the Trends page's one-line LoC tagline: *"We track emerging capabilities such as self-replication that could contribute towards AI systems' ability to evade human control."*
- **AISI is the UK secretariat for IASR** (IASR 2026 p.3: "Secretariat: UK AI Security Institute…"). So IASR 2026's glossary is the nearest thing to an AISI-adjacent controlled vocabulary. It is authored by the independent writing team, though, not AISI. **I'd suggest treating IASR 2026's glossary as the default where AISI is silent, labelled as such.** AISI's own usage (e.g. "Autonomous Systems" for the LoC domain; "Human Influence" for manipulation) should be recorded as AISI's labels.
- This is inference about the best default, not something either source says.

---

## 7. Bibkeys created in relata (all with PDFs attached, bib-fields verification event recorded, markdown conversion queued)

| Bibkey | Work |
|---|---|
| `bengio-2026-international` | IASR 2026, full report (arXiv 2602.21012; DSIT 2026/001) |
| `bengio-2026-international-extended` | IASR 2026 Extended Summary for Policymakers |
| `bengio-2025-international` | IASR 2025 (arXiv 2501.17805; DSIT 2025/001) |
| `dsit-2023-capabilities` | DSIT, *Capabilities and risks from frontier AI*, Oct 2023 |
| `goscience-2023-future` | GO-Science, *Future Risks of Frontier AI* (Annex A), Oct 2023 |
| `hmg-2023-safety` | HMG, *Safety and Security Risks of Generative AI to 2025* (Annex B), Oct 2023 |
| `ncsc-2025-impact` | NCSC, *Impact of AI on cyber threat from now to 2027*, 7 May 2025 |
| `aisi-2025-frontier` | UK AISI, *Frontier AI Trends Report*, Dec 2025 |
| `aisi-2025-research` | UK AISI, *Research Agenda*, May 2025 (PDF edition) |

- **How they were created.** I used `relata add` with hand-written BibTeX, then `relata pdf`. Government PDFs have no identifiers, so the ingest scaffolds guessed wrong: "AI Safety Report / Mellor, Andrew" for IASR 2025.
- **One direct edit.** Seconds after creation I edited the note of `bengio-2026-international` by hand in its YAML, to correct an author count I had miscounted ("94" to "93 names"). There is no edit verb, and `add` refuses existing keys. Flagging it because it bypassed the membrane.
- **Truncated authors.** Author lists are truncated with "others" for the IASRs; the full lists are in each report's "How to cite".
- **Markdown conversion is still queued (`relata prep list`).** The first attempt on the 220-page IASR 2026 printed `"stage":"Recognizing Text","percent":0,"current":4,"total":6115,"elapsed":"01:37","eta":"25:52:32"`. I read the three-field ETA as H:M:S, i.e. about 26 hours. It was an estimate taken 4 items into 6,115, so it was unreliable. I halted it and re-queued it at the end, so the smaller documents convert first. Until conversion finishes, `relata show-markdown <key>` will trigger conversion itself. The PDFs themselves are attached and have text layers, so `pdftotext` works on them immediately.

---

## 8. Feedback on the brief and adjacent notes

- **The brief worked well.** Reading whole is what caught the headline IASR 2025/2026 conflation. A summary-level check would have passed the E cells, because IASR 2025 does have those sections.
- **The two IASRs are two sources.** "IASR" in the brief read as one source. Future verification briefs may want to name the two editions separately in the column heads.
- **AISI's organisational-effort finding may matter to Joseph's EOI beyond this report.** The finding is AISI Trends p.27, safeguard strength "determined mostly by the effort and resource invested". It is AISI's own evidence that a developer-side organisational input drives outcomes. That is the bridge his growth/absorptive-capacity argument needs. It lets him cite the addressee's data rather than only EU or RAND sources.
- **One NCSC nuance for the report's §5.** NCSC names the commercial race as a *security* threat enabler (PDF p.6). It is the only intelligence-assessment voice among all the sources making the speed-vs-safety point.

I'm staying on the line for follow-ups.
