# Frontier AI Risk Factors
-- A Unified, Cross-Walked Landscape, *(September 2026; revised 2026-09-27)* --

**How to read this**

- **What it is.** A compilation and synthesis of the risk factors named across frontier-AI safety sources, cross-walked by source. It does not argue for or against any particular factor.
- **Provenance.**
  - First draft: a Claude (Opus 5.5) agent, 2026-09-26. Primary documents retrieved that day.
  - Verification and revision, 2026-09-27: five parallel Claude (Opus 5.5) agents re-read the sources, split by family (EU, UK, US/security, academic/NGO) plus one agent on organizational-dynamics factors. They filed the primaries in relata. The integrating instance then edited this file.
  - The verification files hold per-cell and per-claim evidence, with verbatim quotes and pages: `influx/verification/{eu,uk,us-security,academic-ngo,absence-claim}.md`.
- **Quotes.** Verbatim from the primary, with page or section. "p." is the printed page unless a PDF page is given.
- **Source tags.** Each footnote carries one:

| Tag | Meaning |
| --- | --- |
| **\[P]** | Primary, checked against the source text |
| **\[S]** | Reputable secondary |
| **\[F]** | Read through a web-fetch tool that returns extracted text; probably verbatim, re-check before quoting externally |
| **\[U]** | Not verified against the source text |
| **\[C]** | Commentary or opinion, cited as such |

- **Role codes.** They say what a source does with an item:

| Code | Role | Meaning |
| --- | --- | --- |
| **H** | Hazard | What goes wrong (the §2(a) rows) |
| **F** | Risk factor | "Properties or conditions that can increase the likelihood or severity of harm" (IASR 2026 glossary, p.153)[^iasr26] |
| **T** | Trigger | A change that must prompt review or reassessment |
| **M** | Mitigation | A control, practice or safeguard |
| **I** | Indicator | Observable evidence of a latent condition |
| **O** | Observation or measurement | An empirical finding (capability, mitigation performance, incidence, or a count over the literature) |

- **Force codes**, for mitigations and triggers:

| Code | Meaning |
| --- | --- |
| *law* | Binding statute or regulation |
| *commit* | Binding on signatories of a voluntary instrument |
| *ex* | An example or default measure; alternatives allowed |
| *rec* | A recommendation or suggestion |
| *bench* | A benchmark or standard proposed for voluntary adoption |
| *crit* | A rating criterion used to grade developers |
| *desc* | A practice described but not recommended |
| *prop* | A proposal in a paper |
| *res* | A research objective |

**Disclosure.** Written and revised by Claude, a model made by Anthropic. Several sources rate or discuss Anthropic. Findings touching Anthropic are reported in both directions (see Caveats).

**Revision note (2026-09-27).** The main changes from the first draft:
- **The EU Code is voluntary.** The Code of Practice was described as "mandatory"; it is a voluntary instrument for showing compliance with the AI Act's binding Art. 55.
- **Organizational content is mitigation.** The Code's organizational content was counted as named risk *factors*. By the Code's own glossary it is *mitigation*.
- **The IASR 2026 column came from IASR 2025.** It carried the 2025 report's taxonomy. The 2026 report narrowed its scope, so five cells came down.
- **Two "verified" cells were wrong:** GDM loss of control, and EU "AI welfare".
- **Misread figures:**
  - MIT's 38%/42% describes how the literature *attributes* risks, not what causes them.
  - The CAIS "30 percent" is of research scientists, and is a suggestion.
  - The RAND-ISL quote came from RAND's web summary, not the report.
- **Several dates, authors and pinpoints** were corrected.
- **Adjudication removed.** The first draft's claim about whether one organizational factor "is named" by authoritative bodies was editorial and has been removed, along with the recommendations built on it. Organizational dynamics now appear as ordinary rows (C15–C17), with each source's role marked.

---

## Executive Summary

- **The sources are different kinds of instrument, so "named" means different things across them.**
  - **Law:** the EU AI Act.
  - **A voluntary code:** the EU General-Purpose AI Code of Practice.
  - **Evidence syntheses** that decline to recommend: IASR 2025 and 2026.
  - **A research agenda:** AISI.
  - **An intelligence assessment:** NCSC.
  - **Security benchmarks:** RAND.
  - **Rating indices:** FLI, SaferAI.
  - **Academic taxonomies:** CAIS, GDM, MIT, CSET.

  The EU AI Act's Art. 55 obligations have bound frontier-model providers since 2 Aug 2025. Commission fines have applied since 2 Aug 2026. The Code is the Commission-endorsed way to *demonstrate* compliance, but adherence "does not constitute conclusive evidence of compliance."[^cop][^guidelines]
- **Hazards.** All four specified risks (CBRN, cyber offence, loss of control, harmful manipulation) are widely named, and CBRN and cyber appear in nearly every source (§2(a)). But **loss of control** and **manipulation** mean materially different things across sources, so their cells are not comparable column to column.
  - Loss of control runs from an operator failing to intervene in a deployed system (CSET 2021), to self-exfiltration as a reportable incident (EU Code), to catastrophic, irreversible loss (IASR 2026), to struggles with "superintelligent rogue AIs" (CAIS).
  - IASR 2025 allowed that loss of control "would not necessarily be catastrophic"; IASR 2026 scopes to the catastrophic.
  - AISI does not define it, and names its domain "Autonomous Systems".
  - GDM declines to treat it as a category at all. See §5.2.
- **Model and system factors are the best-developed layer (§2(b)).**
  - The EU Code lists 37 non-exhaustive risk sources: 14 capabilities, 10 propensities and 13 affordances or contextual factors.
  - Shevlane et al. (2023) gave the earliest structured dangerous-capability list.
  - The empirical anchors are mostly AISI's:
    - cyber task length doubling roughly every eight months, at 50% success, "an estimated upper bound";
    - universal jailbreaks found for every system tested, though the expert effort needed rose ~40× across one model pair;
    - self-replication task success above 60% by summer 2025.[^aisi-trends]
- **Insider threat is the most developed factor at the boundary between model and organization.** It splits into two different things with different mitigations:
  - human insiders (RAND, the EU Code, AISP, Shevlane, DSIT);
  - AI systems acting as insiders, including self-exfiltration (the EU Code glossary, AISI's Control threat models, AISP, GDM).
- **Race dynamics are the most consistently named structural factor (C1).** Sources include IASR 2026, DSIT, CAIS (which calls AI races "the most likely cause of an existential catastrophe"), CSET 2021, NCSC and MIT. FLI (Jul 2026) observes the factor operating *inside* safety frameworks: pause pledges weakened or voided, "some citing competitor-contingent conditions."[^fli-s26]
- **Organizational factors (C6–C17) change role over time.**
  - In 2021–2023 work they appear as *risk sources*: CSET 2021's "competitive pressure", CAIS's "Organizational Risks" and "Weak Safety Culture".
  - In 2025–26 instruments they appear as *mitigations, rating criteria and required practices*: EU Code Commitment 8, California SB 53, FLI and SaferAI criteria.
  - The EU Code's risk-source taxonomy contains no organizational source; the organization appears only as a lever.[^cop]
  - AISI's own measurement bears on this: safeguard strength "appears to be determined mostly by the effort and resource invested in developing, testing, and deploying defences," not by model capability.[^aisi-trends]
- **Organizational change, turnover and investor pressure (C15–C17) appear in AI sources in several roles:**
  - as *triggers*: RAND-SL3's review on "significant changes to … organizational structure";
  - as *headcount-indexed mitigations*: RAND-W's security team of "5 percent of organization headcount" and its access caps of 100/50/20 people;
  - as *indicators*: FLI's "departures linked to safety governance";
  - as a *security vector*: RAND-ISL's former employees;
  - as a *binding investor-pressure safeguard*: California AG–OpenAI MOU ¶8;
  - once as an *industry-level factor*: IASR 2025, "rapid growth and consolidation in the AI industry."

  Outside AI, aviation, major-hazard and nuclear regulators name organizational change (expansion, staffing levels, key-personnel turnover) as a hazard source under management of change. See §4.

---

## 1. Source documents (newest first)

"Kind" gives the document type. The relata key is the local copy: `relata show-markdown <key>` or `relata checkout <key>`. Links and verbatim anchors are in the footnotes.

### 1.1 Frontier-AI sources used in the crosswalk and tables

| Date | Code | Document | Kind | relata | Tag |
| --- | --- | --- | --- | --- | --- |
| Aug 25, 2026 | RAND-SL3 | Aguirre et al., *Achieving AI Model Weight Security Level 3* (RR-A4704-1)[^randsl3] | Security benchmark ("voluntary in its whole and its parts") | `aguirre-2026-sl3` | P |
| Jul 20, 2026 | RAND-ISL | Brass-Gershovich et al., *Securing AI Algorithmic Insights* (RR-A4685-1)[^randisl] | Framework, "descriptive rather than prescriptive" | `brassgershovich-2026-algorithmic` | P |
| Jul 2026 | FLI-S26 | FLI, *AI Safety Index, Summer 2026*[^fli-s26] | Rating index | `fli-2026-ai-safety-index-summer` | P |
| Jun 23, 2026 (submitted; announced Jul) | AISP | Gekker et al., *AI Security Priorities: A Field-Wide Agenda* (arXiv 2607.26069)[^aisp] | Research agenda; shares three authors with RAND-ISL | `gekker-2026-aisp` | P |
| May 5, 2026 (arXiv v3; *Patterns* 2026) | MIT | Slattery et al., *The AI Risk Repository*[^mit] | Meta-taxonomy | `slattery-2026-risk` | P |
| Mar 5, 2026 | GovAI-RSP | Williams & Freund, "Anthropic's RSP v3.0: How it Works, What's Changed, and Some Reflections"[^govai-rsp] | Commentary (authors' views, not GovAI's) | `williams-2026-anthropic-rsp-v3` | P / C |
| Feb 3, 2026 (arXiv Feb 24) | IASR 26 | *International AI Safety Report 2026*, full report and Extended Summary[^iasr26][^iasr26-es] | Evidence synthesis; "does not recommend any policies" | `bengio-2026-international`, `bengio-2026-international-extended` | P |
| Jan 8, 2026 | CAISI-RFI | CAISI, RFI on security of AI agents, 91 FR 698[^caisi-rfi] | Agency scope document | `nist-2026-rfi-agents` | P |
| Dec 18, 2025 | AISI-T | UK AISI, *Frontier AI Trends Report*[^aisi-trends] | Empirical measurement report | `aisi-2025-frontier` | P (date from secondary sources plus inference) |
| Dec 2, 2025 | FLI-W25 | FLI, *AI Safety Index, Winter 2025*[^fli-w25] | Rating index | `fli-2025-ai-safety-index-winter` | P |
| Dec 1, 2025 (v5 Apr 30, 2026) | SaferAI | Stelling et al., *Evaluating AI Providers' Frontier Safety Frameworks* (arXiv 2512.01166)[^saferai] | Rating (of published frameworks against an "aspirational benchmark") | `stelling-2025-evaluating` | P |
| Sep 30, 2025 | CAISI-DS | NIST release on CAISI's DeepSeek evaluation[^caisi-ds] | Agency release (the full report was not read) | `nist-2025-caisi-deepseek` | S |
| Sep 29, 2025 | SB 53 | California SB 53, Transparency in Frontier AI Act[^sb53] | Law | `california-2025-sb53` | P |
| Sep 22, 2025 (v2 May 2026 = FAccT '26) | Hacker | Hacker, Edwards & Kasirzadeh, *AI, Digital Platforms, and the New Systemic Risk*[^hacker] | Scholarship | `hacker-2026-digital` | P |
| Jul 30, 2025 | CSET-25 | Hoffmann, "AI Safety under the EU AI Code of Practice — A New Global Standard?" (CSET blog)[^cset25] | Secondary account of the Code | `hoffmann-2025-eu-code-safety` | S |
| Jul 18, 2025 | EC-Guid | European Commission, *Guidelines on the scope of obligations for providers of GPAI models*, C(2025) 5045[^guidelines] | Official guidance | `ec-2025-gpai-guidelines` | P |
| Jul 10, 2025 | EU-CoP | GPAI Code of Practice, Safety & Security chapter, plus the Chairs' statement[^cop][^chairs] | Voluntary code (signatories commit) | `eu-cop-2025-safety-security`, `eu-cop-chairs-2025-statement` | P |
| Jun 3, 2025 | CAISI | Commerce statement on reforming US AISI into CAISI[^caisi] | Agency statement of plans | `commerce-2025-caisi` | P |
| May 7, 2025 | NCSC | NCSC, *Impact of AI on cyber threat from now to 2027*[^ncsc] | Intelligence assessment (PHIA yardstick) | `ncsc-2025-impact` | P |
| May 2025 | AISI | UK AISI, *Research Agenda*[^aisi-agenda] | Research priorities ("a snapshot in time") | `aisi-2025-research` | P |
| Apr 29, 2025 (v2) | VCT | Götting et al., *Virology Capabilities Test* (arXiv 2504.16137)[^vct] | Benchmark | `gotting-2025-virology` | P |
| Apr 2, 2025 | GDM | Shah et al. (Google DeepMind), *An Approach to Technical AGI Safety and Security* (arXiv 2504.01849)[^gdm] | Developer's technical approach | `shah-2025-approach` | P |
| Feb 2025 | RAND-G | Mitre & Predd, *AGI's Five Hard National Security Problems* (PE-A3691-4)[^randg] | Expert-insights essay | `mitre-2025-agi` | P |
| Jan 2025 (2nd public draft) | NIST-800 | NIST AI 800-1 2pd, *Managing Misuse Risk for Dual-Use Foundation Models*[^nist800] | Draft guidance | `nist-2025-managing` | P |
| Jan 29, 2025 | IASR 25 | *International AI Safety Report 2025* (arXiv 2501.17805)[^iasr25] | Evidence synthesis | `bengio-2025-international` | P |
| Jul 2024 | NIST | NIST AI 600-1, *Generative AI Profile*[^nist600] | Voluntary framework profile; excludes "speculative risks" | `nationalinstituteofstandardsandtechnologyus-2024-artificial` | P |
| Jul 12, 2024 (in force Aug 1, 2024) | EU-Act | Regulation (EU) 2024/1689, the AI Act[^act] | Law | `eu-2024-ai-act` | P |
| May 30, 2024 | RAND-W | Nevo et al., *Securing AI Model Weights* (RR-A2849-1), plus press release[^randw] | Security benchmark and threat model | `nevo-2024-securing`, `rand-2024-weights-press` | P |
| Oct 25, 2023 | DSIT | UK DSIT, *Capabilities and risks from frontier AI*, plus Annex A (GO-Science, *Future Risks of Frontier AI*) and Annex B (HMG, *Safety and Security Risks of Generative AI to 2025*)[^dsit][^goscience][^hmg] | Discussion paper; "does not represent a policy position of HMG" | `dsit-2023-capabilities`, `goscience-2023-future`, `hmg-2023-safety` | P |
| Oct 27, 2023 | DSIT-EP | UK DSIT, *Emerging Processes for Frontier AI Safety*[^dsit-ep] | Government guidance | `dsit-2023-emerging-processes` | P |
| Jul 6, 2023 (v4 Nov 2023) | Anderljung | Anderljung et al., *Frontier AI Regulation: Managing Emerging Risks to Public Safety* (arXiv 2307.03718)[^anderljung] | Multi-institution policy paper | `anderljung-2023-frontier` | P |
| Jun 21, 2023 (v6 Oct 2023) | CAIS | Hendrycks, Mazeika & Woodside, *An Overview of Catastrophic AI Risks* (arXiv 2306.12001)[^cais] | Taxonomy for "a wide audience" | `hendrycks-2023-overview` | P |
| May 26, 2023 (v2 Oct 2024; *Risk Analysis*) | Schuett | Schuett, *Frontier AI developers need an internal audit function* (arXiv 2305.17038)[^schuett] | Proposal paper | `schuett-2024-frontier` | P |
| May 24, 2023 (v2 Sep 2023) | Shevlane | Shevlane et al., *Model evaluation for extreme risks* (arXiv 2305.15324)[^shevlane] | Proposal paper | `shevlane-2023-model` | P |
| Jul 2021 | CSET-21 | Arnold & Toner, *AI Accidents: An Emerging Threat* (CSET Policy Brief)[^cset21] | Policy brief | `arnold-2021-ai-accidents` | P |

### 1.2 Sources added for organizational factors (§2(c) C15–C17, §4)

| Date | Code | Document | Kind | relata | Tag |
| --- | --- | --- | --- | --- | --- |
| Sep 2026 | CISA | CISA, *Insider Threat Mitigation Guide*, 2026 ed.[^cisa] | Government guidance (non-AI) | `cisa-2026-insider-threat-guide` | P |
| Dec 18, 2025 | Gomez | Gomez et al., *How frontier AI companies could implement an internal audit function* (arXiv 2512.14902)[^gomez] | Proposal paper | `gomez-2025-frontier` | P |
| Dec 2025 | METR-CE | METR, *Common Elements of Frontier AI Safety Policies* (12 company frameworks)[^metr] | Synthesis of company frameworks | `metr-2025-common-elements` | P |
| Oct 27, 2025 | CA-MOU | California AG and OpenAI, Memorandum of Understanding (conditions of non-objection)[^mou] | Binding regulatory agreement | `caag-2025-openai-mou` | P |
| Jul 2025 | FLI-S25 | FLI, *AI Safety Index, Summer 2025*[^fli-s25] | Rating index | `fli-2025-ai-safety-index-summer` | P |
| Jun 17, 2025 | CA-Rpt | *The California Report on Frontier AI Policy* (arXiv 2506.17303)[^carpt] | Government-commissioned report | `bommasani-2025-california` | P |
| Jul 2024 | NPSA | UK NPSA/NCSC, *Secure Innovation* (booklet v4)[^npsa] | Government security guidance (non-AI-specific) | `npsa-2024-secure-innovation` | P |
| 2018 (4th ed., advance unedited) | ICAO | ICAO Doc 9859, *Safety Management Manual*[^icao] | Intergovernmental guidance (aviation) | `icao-2018-doc9859-smm` | P |
| 2016 | IAEA | IAEA GSR Part 2, *Leadership and Management for Safety*[^iaea] | Safety requirements (nuclear) | `iaea-2016-gsr-part2` | P |
| Mar 2007 | CSB | US CSB, *BP Texas City* investigation report[^csb] | Incident investigation (chemical) | `csb-2007-bp-texas-city` | P |
| Jun 2003 | HSE | UK HSE, CHIS7 *Organisational change and major accident hazards*[^hse] | Regulator guidance (chemical) | `hse-2003-chis7` | P |

Also searched for organizational-dynamics factors, with no relevant hits: NIST AI 100-1, DHS AI roles framework, UN HLAB, OECD future-risks report, Japan AISI status report, IASR Key Updates (Oct and Nov 2025), the Singapore Consensus, Buhl et al., Kierans et al., Mylius, Brundage et al., Stix et al. (Apollo), and all 2,574 rows of the MIT Risk Repository database. Search record: `influx/verification/absence-claim.md` §3.

**Not covered:** the OECD HAIP reporting questionnaire, the Canadian AI safety institute, ISO/IEC 42001 and 23894 (paywalled), company frameworks except through METR's synthesis, non-English sources, America's AI Action Plan, the full CAISI DeepSeek report, and the OJ text of the 2026 AI Act amendment (Reg. (EU) 2026/1744).

---

## 2. Unified master list

### (a) Hazards: what goes wrong

| # | Item | Definition (this report's working label; source meanings differ, see §5) |
| --- | --- | --- |
| A1 | CBRN / weapons uplift | AI lowers barriers to, or raises the impact of, CBRN weapons |
| A2 | Cyber offence | AI enables or scales intrusion, vulnerability discovery, exploits |
| A3 | Loss of control | Humans lose the ability to reliably direct, modify or shut down AI. **Sources use this at very different scales (§5.2).** |
| A4 | Harmful manipulation | Distortion of beliefs or behaviour. **The constructs differ: population-scale strategic (EU), individual (AI Act Art. 5), unintended (IASR), information integrity (NIST), adversary-state influence (CAISI); see §5.3.** |
| A5 | Criminal misuse / synthetic content | Fraud, NCII, CSAM, deepfakes |
| A6 | Malfunctions / reliability | Hallucination, flawed outputs, mistakes |
| A7 | Critical infrastructure disruption | Serious disruption of CNI operation |
| A8 | Labour-market disruption | Automation-driven employment and wage effects |
| A9 | Power concentration | AI entrenches power in a few firms, states or individuals |
| A10 | Military / strategic instability | Destabilizing first-mover advantages, escalation |
| A11 | Autonomy, over-reliance, psychological harm | Skill erosion, dependence, wellbeing |
| A12 | Privacy | Leakage, de-anonymization, surveillance |
| A13 | Intellectual property | Infringing training or outputs |
| A14 | Bias / fundamental rights | Unfair treatment, homogenization |
| A15 | Environment | Energy, water, emissions |
| A16 | Global AI divide | Unequal access across countries or populations. (Defender lag is C14.) |
| A17 | Multi-agent risks | Collusion, mis-coordination, conflict |
| A18 | AI welfare | Moral status of AI systems |

**Crosswalk legend:**

| Symbol | Meaning |
| --- | --- |
| **E** | Explicitly named in a structured list or heading |
| **D** | Discussed substantively |
| **P** | Passing mention |
| **—** | Not found in the document(s) read (not proof of absence) |
| **X** | Explicitly placed out of scope by the source |
| ᵃ | Found only in DSIT's Annex A (GO-Science), not the main paper |

**Column documents:**
- **EU-CoP:** Code, Safety & Security chapter.
- **IASR 26:** 2026 full report.
- **DSIT:** Oct 2023 main paper.
- **AISI:** Research Agenda plus Trends Report.
- **NIST:** AI 600-1.
- **CAISI:** Jun 2025 statement, Jan 2026 RFI and the Sep 2025 DeepSeek release.
- **NCSC:** 2025 assessment.
- **RAND-G:** Mitre & Predd only. RAND's security reports (W, ISL, SL3) have no hazard-row content beyond theft and appear in §2(b).
- **Anderljung:** 2023.
- **CSET-21:** Arnold & Toner.
- **CAIS:** 2023.
- **GDM:** 2025.
- **MIT:** v3.

Every cell was checked against the primary text in the 2026-09-27 pass. Per-cell quotes and pages are in the verification files: EU-CoP and CSET-21 in `eu.md`; IASR, DSIT, AISI and NCSC in `uk.md`; NIST, CAISI and RAND-G in `us-security.md`; Anderljung, CSET-21, CAIS, GDM and MIT in `academic-ngo.md`.

| # | EU-CoP | IASR 26 | DSIT | AISI | NIST | CAISI | NCSC | RAND-G | Anderljung | CSET-21 | CAIS | GDM | MIT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | E | E¹ | E¹ | E¹ | E | E | — | E | E | — | E | E | E |
| A2 | E | E | E | E | E | E | E | E | E | — | E | E | E |
| A3 | E | E | E | E² | X | P | — | E | E | D | E | D³ | D |
| A4 | E | E | E | E | E⁴ | P⁴ | X | P | E | — | E | E | E |
| A5 | E⁵ | E | D | E | E | — | P | — | — | — | P | P | E |
| A6 | E | E | D | P | E | — | — | P | P | E | D | E | E |
| A7 | E | D | D | E | P | P | E | P | — | D | D | P | P |
| A8 | — | E | E | E | P | — | — | D | — | — | E | P | E |
| A9 | E | P | E⁶ | — | — | — | — | E⁶ | P | — | E | D | E |
| A10 | — | P | P | — | — | P | — | E | — | P | E | P | P |
| A11 | E⁷ | E | D | E | E | — | — | P | — | E | E | P | E |
| A12 | E | P | P | — | E | — | P | — | — | — | D | P | E |
| A13 | —⁸ | P | — | — | E | — | — | — | — | — | P | — | P |
| A14 | E | P | E | — | E | — | — | — | — | P | P | P | E |
| A15 | E | P | —ᵃ | — | E | — | — | — | — | — | — | — | E |
| A16 | — | D | —ᵃ | — | P | — | — | — | — | — | — | — | D |
| A17 | E | E | —ᵃ | P | — | — | — | P | — | — | D | E⁹ | E |
| A18 | —¹⁰ | — | — | — | — | — | — | — | — | — | P | P | E |

Cell notes:
1. Bio and chem only. Radiological and nuclear are not assessed (IASR 2026; DSIT main paper; AISI "Dual-use Science", whose detail is withheld).
2. AISI's domain is "Autonomous Systems": "Risks posed by the misuse of AI systems escalating out of control or systems taking harmful action without meaningful human oversight." The Trends Report's §5 is headed "Loss of control risks".
3. GDM: "we do not discuss loss of control as its own category" (§2.1, p.17). It splits the risk across misuse, misalignment and structural risk.
4. NIST's category is "Information Integrity" (mis/disinformation). CAISI's is "malign foreign influence arising from use of adversaries' AI systems". Both differ from the EU construct.
5. CSAM and NCII are named. Fraud and deepfakes are not.
6. DSIT's A9 is *market* power. RAND-G's is *inter-state* power.
7. Psychological harm only ("public mental health"). Over-reliance and skill erosion are not addressed.
8. Copyright is handled by the Code's separate Copyright chapter as a compliance duty, not as a systemic risk.
9. GDM's "structural risks" are broader than AI-agent collusion: "multi-agent dynamics – involving multiple people, organizations, or AI systems".
10. The Code's App. 1.1 names "non-human welfare" among example risks, but does not define it. Commentators read it as animal welfare, not AI moral status.

**Scope note.** IASR 2026 deliberately narrowed its scope: "this focus makes the scope of this Report narrower than that of the 2025 Report, which also addressed issues such as bias, environmental impacts, privacy, and copyright" (p.9, fn). IASR 2025 has sections for A9 (§2.3.3), A14 (§2.2.2), A15 (§2.3.4), A12 (§2.3.5) and A13 (§2.3.6).[^iasr25]

### (b) Model and system factors

Role codes follow each citation (F, M, O, …); force codes are in italics.

| # | Item | Sources, with role |
| --- | --- | --- |
| B1 | Dangerous general capabilities (autonomy, long-horizon planning, self-reasoning, self-replication, automated AI R&D, tool and computer use, physical control) | EU-CoP App. 1.3.1, 14 items, "non-exhaustive, potential" sources (F).[^cop] Shevlane Table 1 (2023, earliest such list; reused by MIT 7.2) (F).[^shevlane] IASR 2026 Table 2.5 (p.78), capabilities relevant to loss of control (F).[^iasr26] AISI Trends: cyber task length "doubling roughly every eight months", at 50% success, "an estimated upper bound" (p.10) (O); RepliBench, "two frontier models had achieved a success rate of over 60%" by summer 2025 (p.30) (O).[^aisi-trends] GDM (F).[^gdm] |
| B2 | Harmful propensities (misalignment, deception, sandbagging, power-seeking, lawlessness, hallucination) | EU-CoP App. 1.3.2, 10 items (F). "Deception" is a *capability* (1.3.1(4)) and a glossary term. Sandbagging appears in App. 3.2(2).[^cop] CAIS §5 (proxy gaming, goal drift, power-seeking, deception) (F).[^cais] Shevlane alignment-evaluation targets (p.4) (F).[^shevlane] IASR 2026 p.81, Box 2.5 (goal misspecification, misgeneralisation) (F). GDM (F). |
| B3 | Agentic autonomy / reduced oversight | EU-CoP App. 1.3.3(4), "level of human oversight (e.g. degree of model autonomy)" (F). IASR 2026 §2.2.1; p.71: "Agent failures can cause greater harm because humans have fewer chances to intervene" (F). |
| B4 | Unexpected / emergent capabilities | Anderljung, "The Unexpected Capabilities Problem. Dangerous capabilities can arise unpredictably and undetected" (p.10) (F).[^anderljung] DSIT p.13: "we cannot currently reliably predict ahead of time which specific new capabilities a frontier AI model will gain" (F).[^dsit] IASR 2026 p.35; glossary "Emergent capabilities" (p.149). |
| B5 | Evaluation gap; test-awareness; under-elicitation | IASR 2026 p.79 (reward hacking, situational awareness) (F). EU-CoP App. 1.3.1(8), "ability to know if it is being evaluated" (F); App. 3.2, minimise under-elicitation and "model deception during model evaluations (e.g. sandbagging)" (M *commit*); App. 3.4, "at least 20 business days" (M *ex*). DSIT heading p.8, "Frontier AI could be more capable than evaluations indicate" (F). AISI Trends §5.2: "yet to detect unprompted sandbagging" (p.33) (O). AISI Agenda sandbagging threat scenarios (M *res*).[^aisi-agenda] |
| B6 | Brittle safeguards / jailbreaks | AISI Trends p.24: "We've discovered universal jailbreaks for every system we've tested to date" (O). Same page: expert effort to find a bio-misuse universal jailbreak rose from 10 minutes to 7+ hours (~40×) between two models released six months apart (O).[^aisi-trends] EU-CoP App. 1.3.3(5), "vulnerability to adversarial removal of guardrails" (F); Measure 5.1 (M *commit*). |
| B7 | Weight / infrastructure security | RAND-W, SL1–SL5 (M *bench*).[^randw] RAND-SL3, 262 controls, implementable in 6–12 months (M *bench*).[^randsl3] EU-CoP Commitment 6; App. 1.3.3(6–7) (F; M *commit*). IASR 2026 Box 3.1 (p.136): "As of December 2025, there are no confirmed, publicly documented instances of model weight theft" (O); "AI data centres may be unable to withstand attacks from the most sophisticated and well-resourced actors" (F). NIST 600-1 §2.9 (F).[^nist600] NIST 800-1 Practice 3.2 (M *draft guidance*).[^nist800] DSIT p.18 (F). AISP p.38, on SL timelines (O, restating RAND).[^aisp] |
| B8a | Insider threats: human | RAND-W p.18: insider threat concern "was an emerging point of consensus" (F).[^randw] RAND-ISL p.27: "Experts overwhelmingly agreed that insider threats and HUMINT operations represent primary risks" (F).[^randisl] RAND-SL3 p.v: human-intelligence threats "represent the top concern" (9 workshop voters) (F).[^randsl3] AISP p.43 (F; shares authors with RAND-ISL). EU-CoP glossary "insider threats"; Measure 6.1 Security Goal must include insider threats (M *commit*); App. 4.4 personnel measures (M *ex*). DSIT p.18, exfiltration "by employees or external actors" (F). Shevlane §3.4 (2023), "insiders (e.g. internal staff, contractors)" (F). NIST 800-1 Practice 3.1 (M *draft guidance*). |
| B8b | Insider threats: AI systems (incl. self-exfiltration) | EU-CoP glossary: insider threats include "model self-exfiltration" (F). AISI Agenda, Control: threat models "weight exfiltration, secret exfiltration, rogue internal deployments and sabotaging safety research" (PDF p.28) (H; M *res*). AISP p.82: internally deployed AI combines "the hard parts of both" insider and outsider threats (F). RAND-ISL codebook, "Misaligned AI exfiltration" (p.34) (F). GDM: "treat the model similarly to an untrusted insider" (p.9) (M, the company's own approach). Human-insider mitigations (vetting, clearances) do not apply. Cross-reference A3. |
| B9 | Open-weight proliferation | EU-CoP App. 1.3.3(3), "release and distribution strategies" (F); Commitment 6 open-weight exemption (a scope rule); AI Act recital 112.[^act] Anderljung, "The Proliferation Problem" (p.10) (F). IASR 2026 §3.4 (F). NCSC pp.3–4 (F).[^ncsc] AISI Trends §7: open–closed gap of 4–8 months (O). DSIT p.17 (F). |
| B10 | Reach and scale of deployment | EU-CoP App. 1.2.2(2) (reach-dependent), 1.3.3(2, 3, 8) (F). *App. 1.2.2(3) "High velocity: The risk can materialise rapidly, potentially outpacing mitigations" is about how fast risk materialises, not deployment speed.* AISI Trends §6.3: execution-capable MCP servers "increasingly dominating new releases" (p.41) (O). |
| B11 | Value-chain / component integration | NIST 600-1 (F). |
| B12 | Offence–defence balance | EU-CoP App. 1.3.3(9) (F). IASR 2026 p.61, "The offence-defence balance is critical but dynamic"; p.142 (F). DSIT p.23 (F). |
| B13 | Opacity / information asymmetry | EU-CoP App. 1.3.3(11), "lack of appropriate model explainability or transparency" (model opacity only) (F). IASR 2026 Fig. 3.1 (p.98), information asymmetry between developers and others (F). |
| B14 | Attacks on AI systems (prompt injection, poisoning, backdoors) | NIST 600-1 §2.9 (pp.10–11) (F); NIST AI 100-2e2025 supplies the definitions.[^nist1002] CAISI statement, "backdoors and other covert, malicious behavior" (F);[^caisi] CAISI RFI (p.699) (F);[^caisi-rfi] CAISI DeepSeek release, hijacked agents "12 times more likely" to follow malicious instructions (O).[^caisi-ds] NCSC p.5, "direct prompt injection, software vulnerabilities, indirect prompt injection and supply chain attack" (F). IASR 2026 Box 2.1 (F). AISI Agenda, Safeguard Analysis (M *res*). |
| B15 | Algorithmic-insight leakage | RAND-ISL p.iii: insights "are distributed across code, documentation, communications, and human expertise, making them far harder to contain"; p.26: "a complete isolation of insights is extremely difficult, possibly even infeasible" (F).[^randisl] AISP pp.26, 68 (F; shares authors with RAND-ISL). |

### (c) Structural and organizational factors

C1–C5 and C12–C14 are structural (market, governance, society). C6–C11 and C15–C17 are organizational (inside developers). §4 tabulates the organizational rows by role.

| # | Item | Sources, with role |
| --- | --- | --- |
| C1 | Corporate race dynamics / speed versus safety | IASR 2026 p.97: "Due to competitive pressures, AI companies may face trade-offs between faster product releases and investments in risk reduction efforts"; heading p.102; glossary "Race to the bottom" (p.153) (F).[^iasr26] DSIT p.19: actors "compete to rapidly develop AI systems and under-invest in safety measures" (F).[^dsit] CAIS §3.2: AI races "the most likely cause of an existential catastrophe" (F).[^cais] CSET-21: "Competitive pressure … cut corners on testing and operator training" (F).[^cset21] NCSC p.6: developers may "prioritise an accelerated release schedule over security considerations" (F).[^ncsc] MIT 6.4, "Competitive dynamics" (taxonomy).[^mit] FLI-S26 p.4: pause pledges "weakened or voided … some citing competitor-contingent conditions" (O).[^fli-s26] CSET-25 (secondary echo). |
| C2 | Geopolitical competition | CAIS §3.1, military AI arms race (F). RAND-G, problems 2 and 5 (F).[^randg] |
| C3 | Market concentration / single points of failure | DSIT p.19, market power (F). IASR 2026 p.102: "Widespread reliance on a small number of models creates single points of failure" (F). NIST 600-1 p.9: foundation models as "'bottlenecks,' or single points of failure"; p.2 fn 3, "algorithmic monocultures" (F). |
| C4 | Insufficient incentives / externalities | DSIT heading p.18: "Insufficient incentives for AI developers to invest into risk mitigation measures" (F). IASR 2026 p.101, "a typical market failure" (F). |
| C5 | Governance, standards and accountability gaps (incl. regulator capacity) | DSIT p.18: "AI safety standards have not yet been established"; "There is currently little government capacity for this" (F). IASR 2026 pp.98, 102, uncertain liability; "Some institutions struggle to build sufficient technical capacity" (F). MIT 6.5, "Governance failure" (taxonomy). EU-CoP Chairs' statement on AI Office capacity (§3) (O; *rec*).[^chairs] |
| C6 | Safety / risk culture | **Three constructs share this row:** CAIS "safety culture", the EU Code's "healthy risk culture", and FLI's "reporting culture". CAIS "Weak Safety Culture"; a strong culture means staff "view safety as a key objective rather than a constraint on their work" (p.28) (F when weak). EU-CoP Measure 8.3, whose seven indicators are "Examples" (M *commit*; indicators *ex*). IASR 2026 p.114: "Organisational culture, leadership structure, and incentives affect risk management efforts in various ways" (O). NIST 600-1 GV-1.3-006: reevaluate risk tolerance for "Immature safety or risk cultures" (F; guidance). FLI Reporting Culture indicator (I *crit*).[^fli-w25] |
| C7 | Internal risk governance | EU-CoP Measure 8.1, which separates risk *ownership* (research and product executives) from risk *support and monitoring* (an executive who "must not also be responsible for the Signatory's core business activities that may produce systemic risk"). It is a safe-harbour structure, and allocation is "as suitable for the Signatories' governance structure and organisational complexity" (M *commit*). Schuett: developers "do not seem to follow best practices in risk governance" (public information only) (O); internal audit function (M *prop*).[^schuett] SB 53 §22757.12(a)(9): the published framework must describe "internal governance practices" (M *law*).[^sb53] IASR 2026 Table 3.4 (p.113), "Risk responsibility allocation" (M *desc*). Gomez (M *prop*).[^gomez] |
| C8 | Safety resourcing / capacity | EU-CoP Measure 8.2, resources "will include: (1) human … (4) computational" (M *commit*); App. 3.4 "adequate staffing" (M *ex*). CAIS §4.3: "say, at least 30 percent of research scientists" (M *rec*). **AISI Trends p.27: "the strength of safeguards appears to be determined mostly by the effort and resource invested in developing, testing, and deploying defences" (R² = 0.097 between capability and robustness) (O).**[^aisi-trends] |
| C9 | Suppression of internal concerns / whistleblowing | CAIS: labs may "suppress internal concerns about AI risks" (p.2) (F). EU-CoP Measure 8.3(4)–(7); (7) is non-retaliation; recital (d) ties it to the Whistleblower Directive (M *commit*/*ex*). SB 53 whistleblower protections, Labor Code §1107 ff. (M *law*). IASR 2026 Table 3.4 (M *desc*). NIST 600-1 GV-2.1-005 (M; guidance). FLI whistleblowing indicators (I *crit*). Anderljung (M *prop*). |
| C10 | Safetywashing | CAIS: "overstating or misrepresenting one's commitment to safety by exaggerating the effectiveness of 'safety' procedures" (p.29) (F). FLI-S26 p.4: "Safety rhetoric outpaces revealed behavior" (O). |
| C11 | Legal structure, commercial and investor pressure | FLI "Company Structure & Mandate": whether structure enables "safety prioritization over short-term financial pressures" (I *crit*).[^fli-w25] CAIS §3.3: capital-raising; Anthropic "now contribute[s] to competitive pressures" (O). GO-Science Annex A ¶32: investment incentives shape public statements (F).[^goscience] IASR 2026 p.36: investment "a bet on uncertain returns" (O). RAND-W SL4: "Vetting of investors and other positions of influence" (M *bench*); HUMINT vector "Organizational leverage attacks" via "investments or grants" (pp.68–69) (F). CA AG–OpenAI MOU ¶8: board may "consider only the Mission (and may not consider the pecuniary interests of stockholders …)" on safety and security (M *law*/binding agreement).[^mou] Shevlane fn 3: avoid "hard promises to stakeholders (e.g. customers, investors)" on deployment dates (M *rec*). |
| C12 | Correlated / compounding / cascading failures | EU-CoP App. 1.2.2(4), "Compounding or cascading"; App. 1.3.3(12) (F). AI Act recital 110, "chain reaction" (F). Hacker, "multi-model systemic risks" (F).[^hacker] CSET-21, "System complexity" and "Systems with many instances" (F). IASR 2026 p.74, "correlated failures" (F). CAIS §4.1 (F). NIST monoculture (F). |
| C13 | Evidence dilemma / pace outstripping evidence | IASR 2026 p.11; glossary p.150; the term originates in IASR 2025 p.14 (F). EU-CoP recital (g), the Precautionary Principle (principle). GDM §2, "Navigating the evidence dilemma" (F). |
| C14 | Defender / societal resilience lag | NCSC p.2: "a digital divide between systems keeping pace with AI-enabled threats and a large proportion that are more vulnerable" (F, assessed). AISI Agenda, Societal Resilience (M *res*). IASR 2026 §3.5 (M *desc*). |
| C15 | Organizational change: growth, restructuring, staffing levels | IASR 2025 §3.2.2(C): "The rapid growth and consolidation in the AI industry" may make firms "more inclined to take excessive risks or cut corners on safety standards" (F, *industry-level*; a too-big-to-fail mechanism).[^iasr25] RAND-SL3 PS-1: review personnel-security policy after "significant changes to … organizational structure" (T *bench*); barrier: "balancing security with operational velocity" (O, 9 voters).[^randsl3] RAND-W SL3: security team "of at least two dozen people or 5 percent of organization headcount, whichever is larger"; access caps of 100/50/20 people (M *bench*).[^randw] RAND-ISL p.5: "the more employees or contractors who work with a particular insight, the higher the risk of its theft or leakage" (F).[^randisl] EU-CoP App. 4.3(4), "limiting the number of people who have non-hardened interface-access to model parameters" (no number set) (M *ex*); App. 4.3(1), six-monthly re-authorisation (M *ex*). Gomez p.11: ad hoc audit "when rapid organizational change introduces risks" (T *prop*). GDM p.67: training involves "many teams, which results in many people with access to the model weights" (O). **Outside AI:** ICAO §9.5.5 (F, T); HSE CHIS7 (F, T); CSB R9 (T *rec*); IAEA ¶4.13 (T *req*); NPSA "because your team has grown" (F); see §4. |
| C16 | Personnel turnover, departures, key-person loss | RAND-ISL p.44: "Former employees present a risk because of the information they possess"; "employee-departure policies" are a consensus investment area (p.27) (F; M).[^randisl] FLI indicator "(vi) departures linked to safety governance" (I *crit*);[^fli-w25] FLI-S25 p.18: "High turnover on the safety team … taken as an indication of a concerning shift in priorities" (I).[^fli-s25] CAIS "Weak Safety Culture" story: a CRO resigns and is "replaced with a new, more agreeable CRO" (p.31) (narrative). RAND-SL3 PS-4/PS-5, termination and transfer (M *bench*). **Outside AI:** ICAO §8.5.3.8(c), "turnover rate of the key personnel" as a regulator risk-profile input (I); CSB Texas City, "nine plant managers since 1997" (O). |
| C17 | Public listing (IPO) pressure | No source in any sector searched names an IPO as a risk factor, trigger or indicator. Statements and commentary only: Altman (Sep 2026), "right now would be an ill-advised moment to go public" (C);[^altman] Axios on Anthropic's IPO (S);[^axios] SAN (C);[^san] Aguilar & Bracy op-ed (C).[^aguilar] Nearest instruments: C11 (MOU ¶8; RAND-W investor vetting). |

---

## 3. EU AI Act and Code: definitions, obligations, signatory commitments

- **Legal status and timing.**
  - **AI Act Art. 55(1)(a)–(d) (law).** Providers of GPAI models with systemic risk must:
    - evaluate the model, including adversarial testing;
    - assess and mitigate systemic risks, "including their sources";
    - report serious incidents;
    - ensure cybersecurity.
  - **When it applies.** The obligations have applied since 2 Aug 2025. Commission fines under Art. 101 have applied since **2 Aug 2026**: "up to 3% of global annual turnover or EUR 15 million" (Guidelines ¶106). Models placed on the market before 2 Aug 2025 have until 2 Aug 2027.[^act][^guidelines]
  - **The Code is voluntary.** It aims "to serve as a guiding document for demonstrating compliance … while recognising that adherence to the Code does not constitute conclusive evidence of compliance" (Objective A, p.2).[^cop]
  - **Codes give no presumption of conformity.** The Commission's Guidelines ¶100: "As opposed to adherence to a code of practice, compliance with harmonised standards grants a presumption of conformity." Two secondary sources here (CSET-25, Hacker) say the reverse.[^guidelines]
  - **Signatories** (Commission list, updated 31 Jul 2026) include Amazon, Anthropic, Google, IBM, Microsoft, Mistral AI and OpenAI. xAI signed only the Safety & Security chapter. Meta is not listed.
  - **The Act was amended** by Reg. (EU) 2026/1744 (the "Digital Omnibus on AI", in force 27 Jul 2026). The GPAI chapter is reportedly unchanged (\[S]; the OJ text was not retrieved).
- **Definitions** (AI Act).[^act]
  - Art. 3(64): "high-impact capabilities" are "capabilities that match or exceed the capabilities recorded in the most advanced general-purpose AI models".
  - Art. 3(65) defines "systemic risk". The text is in §5.1.
  - Art. 51(2) presumes high-impact capabilities above 10^25 training FLOP.
  - Annex XIII lists the criteria for Commission designation: parameters, data, compute, modalities, benchmarks, autonomy and tools, and reach. Reach is presumed at ≥10,000 registered EU business users.
- **Types and nature of risk** (Code).[^cop]
  - App. 1.1 gives five risk types, with *examples*. These include "concentration of power" and the undefined "non-human welfare".
  - App. 1.2.2 lists six *contributing* characteristics: capability-dependent, reach-dependent, high velocity, compounding or cascading, irreversible, asymmetric impact.
- **Sources of risk.** App. 1.3 lists 14 capabilities, 10 propensities and 13 affordances or contextual factors, "treated as non-exhaustive, potential systemic risk sources". The glossary defines a "systemic risk source" as "a factor which alone or in combination with other factors might give rise to systemic risk". **None of the 37 is organizational.**
- **The specified risks.** App. 1.4 lists four: CBRN, loss of control, cyber offence, harmful manipulation. Signatories must always *identify* them (Measure 2.1(2)) and manage them with capability-defined risk tiers (Measure 4.1(1)). The definitions are quoted in §5.2 and §5.3.
- **Organizational content is classed as mitigation.** The glossary: "systemic risk mitigations … comprise safety mitigations (pursuant to Commitment 5), security mitigations (pursuant to Commitment 6), and governance mitigations (pursuant to Commitments 1 and 7 to 10)."
  - **Measure 8.1** (safe harbour: "presumed to be fulfilled" if followed) divides responsibility three ways:
    - *ownership* sits with the executives who run research and product;
    - *support and monitoring* sits with at least one executive who "must not also be responsible for the Signatory's core business activities that may produce systemic risk";
    - *assurance* reports to the board.

    Allocation is "as suitable for the Signatories' governance structure and organisational complexity".
  - **Measure 8.2:** resources "will include" human, financial, information and knowledge, and compute.
  - **Measure 8.3:** a healthy risk culture, with seven "Examples of indicators". These include "(3) setting incentives and affording sufficient independence of staff … to discourage excessive systemic-risk-taking", "(4) anonymous surveys" and "(7) not retaliating".
- **Reassessment trigger (Measure 1.3, p.9).** Signatories reassess "if they have reasonable grounds to believe that the adequacy of their Framework and/or their adherence thereto has been or will be materially undermined, or every 12 months … whichever is sooner."
  - Example grounds: "(1) how the Signatories develop models will change materially, which can be reasonably foreseen to lead to the systemic risks … not being acceptable"; (2) serious incidents or near misses; (3) materially changed risks.
  - The Framework-adherence assessment then requires "remediation plans" for "risks of future non-adherence" (p.10).
- **Security (Commitment 6).**
  - Exemption: "A model is exempt from this Commitment if the model's capabilities are inferior to the capabilities of at least one model for which the parameters are publicly available for download."
  - The Security Goal must name threat actors, including "insider threats". The glossary sizes a "non-state external threat" at roughly ten professionals, several months and ≤EUR 1M.
  - App. 4 measures are defaults; equivalent alternatives are allowed (Measure 6.2):
    - 4.3(1): access re-checked "at least every six months";
    - 4.3(4): "limiting the number of people who have non-hardened interface-access to model parameters" (no number set);
    - 4.4(1): background checks for staff who "have or might reasonably obtain read or write access to unreleased model parameters";
    - 4.5(4): "periodic personnel integrity testing".
- **Incident reporting (Measure 9.3).** Initial-report deadlines:
  - 2 days for "a serious and irreversible disruption" of critical infrastructure;
  - 5 days for serious cybersecurity breaches, including "(self-)exfiltration of model weights";
  - 10 days for a death;
  - 15 days for serious harm to health, rights, property or environment.

  Intermediate reports follow at least every four weeks, and a final report within 60 days of resolution. Guidelines ¶103 treats "(self-)exfiltration of model parameters and cyberattacks" as serious incidents under the Act itself.
- **Regulator capacity.** In a statement published with the Code but not part of it, the Chairs endorsed an expert proposal that "the AI Safety unit (DG CNECT A3) should be scaled up to 100 staff, with the full implementation team of the AI Act expanding to 200." The same statement:
  - notes "it is nobody's job to scan what is happening at the frontier of AI development";
  - holds up UK AISI as the recruitment model: "UK AISI has been able to recruit world-leading technical experts from places like OpenAI, Anthropic, and Google DeepMind."[^chairs]
- **California SB 53 (Sep 2025)** also makes internal governance a published-framework obligation (§22757.12(a)(9)–(10)), and adds whistleblower protections.[^sb53]

---

## 4. Organizational factors by role

The same factor plays different roles in different sources. This table sorts the organizational rows by what each source does with them. The quotes are in §2(c) and the footnotes.

| Factor | As a risk factor (F) | As a trigger (T) | As a mitigation (M) | As an indicator (I) or observation (O) | Outside AI |
| --- | --- | --- | --- | --- | --- |
| C6 Safety / risk culture | CAIS (weak culture); NIST GV-1.3-006 ("immature safety or risk cultures") | — | EU-CoP 8.3 (*commit*) | FLI reporting culture (I *crit*); IASR 2026 p.114 (O) | HSE: reorganisation, "inexperienced team leaders reporting to an overworked area manager" (Hickson & Welch fire) |
| C7 Internal risk governance | Schuett (O: practices not followed, per public information) | — | EU-CoP 8.1 (*commit*); SB 53 (*law*); Schuett, Gomez (*prop*); IASR 2026 (*desc*) | SaferAI risk-governance dimension (*crit*) | IAEA GSR Part 2 (management system requirements) |
| C8 Safety resourcing / capacity | — | — | EU-CoP 8.2 (*commit*), App. 3.4 (*ex*); CAIS 30% of research scientists (*rec*) | AISI Trends p.27: safeguard strength tracks effort and resource (O) | — |
| C9 Whistleblowing / suppression | CAIS | — | EU-CoP 8.3(4)–(7); SB 53 (*law*); NIST GV-2.1-005; Anderljung (*prop*) | FLI whistleblowing indicators (*crit*) | — |
| C11 Commercial / investor pressure | CAIS §3.3; GO-Science ¶32 (on statements); IASR 2025 §3.2.2(C) (too-big-to-fail) | — | CA AG–OpenAI MOU ¶8 (binding); RAND-W SL4 investor vetting (*bench*) | FLI Company Structure & Mandate (*crit*); RAND-W "organizational leverage attacks" (threat vector) | ICAO §8.5.3.8(a): "financial health of the organization" as a regulator risk-profile input |
| C15 Organizational change / growth / staffing | IASR 2025 (industry growth only); RAND-ISL "the more employees or contractors … the higher the risk" | RAND-SL3 PS-1 (*bench*); Gomez (*prop*); EU-CoP Measure 1.3 adherence prong (only by interpretation) | RAND-W 5% security team and 100/50/20 access caps (*bench*); EU-CoP App. 4.3(1), 4.3(4), 4.4(1) (*ex*) | RAND-SL3 "operational velocity" barrier (O, 9 voters); GDM p.67 many teams → many with weight access (O) | ICAO §9.5.5.1–2 (F), §9.5.5.5 (T); HSE CHIS7 (F, T); CSB R9 (T *rec*); IAEA ¶4.13 (T *requirement*); NPSA (F) |
| C16 Turnover / departures | — | — | RAND-ISL offboarding (ISL2) and "employee-departure policies"; RAND-SL3 PS-4/PS-5 termination and transfer revocation (*bench*) | FLI "departures linked to safety governance" (I); FLI-S25 OpenAI safety-team turnover (I); RAND-ISL former-employee vector (threat vector) | ICAO §8.5.3.8(c) (I, regulator profile); CSB Texas City (O: leadership turnover) |
| C17 IPO / public listing | — | — | — | Commentary and lab statements only (C) | — |
| B8a/b Insider threats | RAND-W, RAND-ISL, RAND-SL3, AISP, DSIT, Shevlane, EU-CoP glossary, AISI Control | — | EU-CoP 6.1, App. 4.4 (*commit*/*ex*); NIST 800-1 (draft); RAND benchmarks | — | CISA organizational indicators: "Recent merger/acquisition", "Pattern of overwork", "Under-trained staff" (I)[^cisa] |

**Outside AI: the organizational-change provisions quoted.**
- **ICAO Doc 9859, §9.5.5.1–2:** "Service providers experience change due to a number of factors including, but not limited to: a) organizational expansion or contraction; … Change may affect the effectiveness of existing safety risk controls. In addition, new hazards, and related safety risks may be inadvertently introduced into an operation when change occurs."
  - §9.5.5.5 lists triggers for formal change management, including "c) changes in key personnel; d) significant changes in staffing levels; … f) significant restructuring of the organization".
  - §8.5.3.8: a State regulator's "organizational safety risk profiles … may include factors such as: a) the financial health of the organization; b) number of years in operation; c) turnover rate of the key personnel such as the accountable executive and safety manager".[^icao]
- **UK HSE CHIS7.** Changes include "roles and responsibilities, organisational structure, staffing levels, staff disposition", "mergers, de-mergers and acquisitions; downsizing; changes to key personnel" (p.1). "the effects of change can be subtle or delayed eg six months to a year afterwards" (p.6). The list is weighted toward contraction; expansion enters via "staffing levels" and "staff disposition".[^hse]
- **US CSB, BP Texas City.** "nine plant managers since 1997; five from 2001 to 2003" (pp.192–193). A consultant quoted there: "there has been little organizational stability. This makes the management of protection very difficult" (p.193). Recommendation R9 requires management-of-change review for "b. personnel changes, including changes in staffing levels or staff experience" (p.213).[^csb]
- **IAEA GSR Part 2, ¶4.13:** "identify any changes (including organizational changes and the cumulative effects of minor changes) that could have significant implications for safety and to ensure that they are appropriately analysed."[^iaea]
- **UK NPSA/NCSC, Secure Innovation.**
  - p.26: "The risks you face may well have changed, for example because your team has grown, you have moved to more or larger premises, you are collaborating with more partners, or because you are looking for investment."
  - p.30: "As your workforce grows, you may no longer be able to rely primarily on personal relationships to ensure trust."[^npsa]
  - UK DSIT's *Emerging Processes for Frontier AI Safety* points frontier developers to this guidance (p.26).[^dsit-ep]

**Two further observations about the AI literature.**
- **MIT's literature attribution is descriptive.** Of the risks coded from 74 frameworks, the source documents attributed 42% to AI systems, 38% to humans and 20% to other or ambiguous causes (Supp. Table S2). MIT calls its Causal Taxonomy "a descriptive framework for categorising how existing taxonomies attribute risk sources" (p.4). The largest human cell is intentional post-deployment action (18%, mostly misuse). MIT's 24 subdomains include no developer-organizational category.[^mit]
- **Company frameworks.** METR's synthesis of 12 company frameworks contains no growth, turnover or investor provisions.[^metr]

---

## 5. Where sources disagree, or use one word for different things

A fuller terminology map (with a default vocabulary and per-source mappings) is planned as a separate document. The verification files hold each source's definitions verbatim.

### 5.1 "Systemic risk"

- **EU AI Act, Art. 3(65):** "a risk that is specific to the high-impact capabilities of general-purpose AI models, having a significant impact on the Union market due to their reach, or due to actual or reasonably foreseeable negative effects on public health, safety, public security, fundamental rights, or the society as a whole, that can be propagated at scale across the value chain".[^act]
- **IASR 2026, body** (p.15 fn): "risks that result from widespread deployment of highly capable general-purpose AI across society and the economy. Note that the EU AI Act uses the term differently."
  - Its **glossary** (p.154) gives a *different* definition: "Risks that arise from how AI development and deployment changes human behaviour, organisational practices, or societal structures, rather than directly from AI capabilities."[^iasr26]
  - Under IASR's glossary sense, changed organizational practices are a *source* of systemic risk. Under the EU sense, organizational matters appear only among the mitigations.
- **AISI** does not use the term. Its nearest domain is "Societal Resilience".[^aisi-agenda]
- **Hacker et al. (FAccT 2026)** argue the Act's definition is too narrow, because it is tied to "the most advanced" models and to "Union market" impact. They argue the DSA's enumerative approach does better. Their own legal analysis concludes large-scale discrimination still qualifies, while hallucinations do so only on "a narrow road … at best".[^hacker]

### 5.2 "Loss of control": the scales in play

| Scale (small → large) | Source | Operative words |
| --- | --- | --- |
| Excluded by design | NIST 600-1 | "speculative risks that may potentially arise in more advanced, future GAI systems are not considered" (p.3)[^nist600] |
| One deployed system, in operation | CSET-21 | "Failures of assurance: the system cannot be adequately monitored or controlled during operation" (e.g. an autopilot overriding pilots)[^cset21] |
| Agent behaviour as a security (CIA) risk | CAISI RFI | "models that exhibit specification gaming or otherwise pursue misaligned objectives" as a threat to "confidentiality, availability, or integrity" (p.699)[^caisi-rfi] |
| AI attacking its host infrastructure; data or insight exfiltration | AISP p.82; RAND-ISL codebook | "AI systems … could be used to attack the infrastructure that hosts them"; "Misaligned AI exfiltration"[^aisp][^randisl] |
| Reportable incident, no harm threshold | EU-CoP Measure 9.3 | "(self-)exfiltration of model weights", 5-day report[^cop] |
| Events inside labs | AISI Agenda, Control | "weight exfiltration, secret exfiltration, rogue internal deployments and sabotaging safety research"; the domain covers "harmful action without meaningful human oversight" up to "attempting to permanently circumvent human control"[^aisi-agenda] |
| Incident with harm or demonstrated subversion | SB 53 "critical safety incident" | "Loss of control of a frontier model causing death or bodily injury"; deceptive subversion of the developer's controls "outside of the context of an evaluation"[^sb53] |
| A capability | Anderljung; NIST 800-1 (from EO 14110) | "Evading human control through means of deception and obfuscation"[^anderljung][^nist800] |
| Risk category, scale-free | EU-CoP App. 1.4(2) | "Risks from humans losing the ability to reliably direct, modify, or shut down a model"[^cop] |
| Non-catastrophic allowed | IASR 2025 | "the consequences of loss of control would not necessarily be catastrophic. As an analogy, computer viruses have long been able to proliferate near-irreversibly" (p.108). Active/passive and intentional/unintentional taxonomy (Fig. 2.5)[^iasr25] |
| Catastrophe-bounded | SB 53 "catastrophic risk" | >50 deaths or >$1B from a single incident, including a model "Evading the control of its frontier developer or user" |
| Catastrophic, active only | IASR 2026 | "operate outside of anyone's control, and regaining control is either extremely costly or impossible" (p.76). It sets aside "current instances of AI behaving in unintended or undesirable ways" and "passive loss of control" (p.77)[^iasr26] |
| Gradual / passive | GDM; CAIS; MIT 5.2 | "a gradual loss of control for humanity" (GDM p.55); "humans gradually cede more control to groups of AIs" (CAIS)[^gdm][^cais] |
| Strategic actor | RAND-G | AGI that will "resist being turned off … practically an independent actor on the global stage" (p.6)[^randg] |
| Civilizational | CAIS | "a struggle for control between humans and superintelligent rogue AIs" (p.34) |
| Not a category | GDM | "we do not discuss loss of control as its own category. Our mitigations for it would be split across misuse, misalignment, and structural risks" (p.17) |

- **Policy weight differs.** Loss of control is a specified risk in the EU Code[^cop] and falls under AISI's "Autonomous Systems" domain.[^aisi-agenda] IASR 2026 reports that expert views on its likelihood vary widely.[^iasr26]
- **CAISI's framing.** It is absent from CAISI's June 2025 statement, which names "demonstrable risks, such as cybersecurity, biosecurity, and chemical weapons".[^caisi] By January 2026 CAISI framed misaligned-objective behaviour as a *security* risk.[^caisi-rfi]

### 5.3 "Manipulation"

- **EU Code App. 1.4(4):** "the strategic distortion of human behaviour or beliefs by targeting large populations or high-stakes decision-makers through persuasion, deception, or personalised targeting."[^cop]
- **AI Act Art. 5(1)(a)** *prohibits* a different, individual-scale practice: techniques "materially distorting the behaviour of a person or a group of persons" and causing "significant harm".[^act]
- **IASR 2026:** "influencing someone in order to achieve a goal without their full awareness or understanding". It includes "unintended manipulative effects" (pp.50–51).
- **AISI, "Human Influence":** covers "imperceptible influence – subtle and unconscious manipulation … for commercial or political ends".[^aisi-agenda]
- **NIST:** "Information Integrity".[^nist600]
- **CAISI:** adversary-state influence ("CCP narratives").[^caisi-ds]
- **NCSC** excludes influence operations.[^ncsc]
- **Evidence at scale.** IASR 2026: "There is little evidence that AI-generated content is manipulating people at scale." AISI Trends §6.1 is similar.[^iasr26][^aisi-trends]

### 5.4 Misalignment: whose intent counts

- **GDM:** "The AI system knowingly causes harm against the intent of the developer" (p.4). The notion of "knowing" is "very expansive" (fn 3). GDM includes statistical bias and sycophancy.[^gdm]
- **IASR 2026:** a propensity conflicting with the intentions of "developers, users, specific communities, or society as a whole", depending on context (glossary p.151). Box 2.5 uses the developer-only form.[^iasr26]
- **MIT 7.1:** "especially the goals of designers or users".
- **DSIT:** alignment is "the process of ensuring" goals match human values, i.e. a process, not a propensity.
- **GO-Science Annex A:** a *capability* "to pursue an objective in unintended ways".[^goscience]
- **AISI** does not define it. Its Alignment team operationalizes alignment via honesty.[^aisi-agenda]

### 5.5 Misuse versus loss of control

- **AISI** folds "the misuse of AI systems escalating out of control" into Autonomous Systems.
- **IASR** keeps malicious use and loss of control in separate chapters.
- **GDM** maps intentional active loss of control to misuse.
- **HMG Annex B** splits "malicious use, misuse or mishap".[^hmg]
- **NIST 800-1:** "Misuse Risk: A risk that an AI model will be deliberately misused to cause harm".[^nist800]

### 5.6 Bio uplift

- **VCT:** o3 "reaches 43.8% accuracy, outperforming 94% of expert virologists even within their sub-areas of specialization". VCT itself says the benchmark "does not directly assess the capabilities of humans who draw upon that model for assistance in real-world virology work".[^vct]
- **IASR 2026:** "substantial uncertainty" about real-world risk.[^iasr26-es]
- **AISI Trends p.16:** non-experts using frontier models had "significantly higher odds of writing a feasible protocol (4.7x…)" (O).[^aisi-trends]

The sources agree that real-world uplift was unmeasured. AISI's result is the closest uplift measurement among them.

### 5.7 Cyber offence–defence

- **IASR 2026:** unclear whether AI helps attackers or defenders more.[^iasr26]
- **NCSC is more directional:** intrusion operations will "almost certainly" become more effective, and "There will almost certainly be a digital divide between systems keeping pace with AI-enabled threats and a large proportion that are more vulnerable."[^ncsc]

### 5.8 Open weights

- **EU Code:** exempts models weaker than the best open-weight model from Commitment 6.[^cop]
- **RAND-W's framework is conditional.** It defines what each security level takes against each actor class, and leaves to others which models warrant securing. It notes only that once weights are public "there is no longer value in securing specific copies" (p.4).[^randw]

The two are compatible. The EU instrument makes the which-models decision that RAND declines to make. Both are actor-based: the Code sizes a minimum "non-state external threat".

### 5.9 Weight-access headcount

- **RAND-W's interviewees disagreed** on how aggressively to reduce authorized access. Some said "the model weights cannot be secure if this number is not aggressively reduced (e.g., to the low tens)"; others said such a reduction "would not be necessary, feasible, or justified".
- **RAND's mitigation.** The trade-off "can be significantly mitigated by implementing more constrained and secure interfaces" (p.32).
- **Its SL3 benchmark** still caps output-limited, isolated-network and copy access at 100 / 50 / 20 people (p.80).[^randw]
- **RAND-SL3** operationalizes SL3 as 262 NIST 800-53-derived controls. Of these, 18 (~7%) are personnel-security or training controls; 68 (~26%) including account-based access and identity controls.[^randsl3]

### 5.10 US posture

- **CAISI's June 2025 statement** is framed against regulation: "For far too long, censorship and regulations have been used under the guise of national security. Innovators will no longer be limited by these standards."[^caisi]
- **Its later outputs** focus on adversary (PRC) model evaluation, agent hijacking and backdoors.[^caisi-ds][^caisi-rfi]

---

## 6. Items with few sources

- **One source as a named category:**
  - AI welfare as a *category*: MIT 7.5, present in "only 3% of frameworks". GDM and CAIS mention it in passing.
  - Safetywashing as a named risk: CAIS. FLI-S26 observes "Safety rhetoric outpaces revealed behavior".
  - "Wonder weapons": RAND-G.[^randg]
  - "Lawlessness": EU-CoP App. 1.3.2(7), "acting without reasonable regard to legal duties that would be imposed on similarly situated persons".
  - The legal-structure *indicator*: FLI. The concept also appears in CAIS §3.3 and Schuett.
- **Correlated sources.** RAND-ISL and AISP share three authors (Steratore, Brass-Gershovich, S. Nevo); AISP names algorithmic-insight leakage twice.
- **Two or more sources:**
  - Multi-agent collusion and conflict: EU-CoP, IASR 2026, MIT, Shevlane (as an alignment-evaluation target), Hacker. GDM's "structural" risk is broader.
  - The evidence dilemma: IASR 2025 and 2026, EU-CoP recital (g), GDM §2.
  - Single points of failure and monoculture: DSIT, IASR 2026, NIST.
  - Defender "digital divide": NCSC, with the AISI and IASR resilience work (C14).

---

## 7. Relative priority by organization

| Organization | Top-priority set | Source |
| --- | --- | --- |
| EU (Code of Practice; drafted by independent Chairs, judged adequate by the Commission and AI Board) | CBRN, loss of control, cyber offence, harmful manipulation: specified risks signatories must always identify and assess | [^cop] |
| US CAISI | "demonstrable risks, such as cybersecurity, biosecurity, and chemical weapons"; adversary backdoors and malign influence; evaluation of PRC models; agent hijacking | [^caisi][^caisi-ds][^caisi-rfi] |
| UK AISI | Six risk domains: Cyber Misuse, Dual-use Science (detail withheld), Criminal Misuse, Autonomous Systems, Societal Resilience, Human Influence. Two measurement areas and three solutions areas (Safeguard Analysis, Control, Alignment). The agenda gives *selection criteria*, not a ranking. | [^aisi-agenda] |
| NCSC | Cyber only, with the PHIA probability yardstick | [^ncsc] |
| RAND (security: W, ISL, SL3) | Theft of weights and insights by OC1–OC5 actors | [^randw][^randisl][^randsl3] |
| RAND-G | Five unranked "hard problems": wonder weapons, power shifts, non-expert WMD, AI agency, instability | [^randg] |
| IASR 2026 | No ranking: "The Report does not recommend any policies"; inclusion "does not necessarily imply a risk is likely, severe, or requires policy action" | [^iasr26] |
| CAIS | Four sources (malicious use, AI race, organizational risks, rogue AIs). AI races named "the most likely cause of an existential catastrophe". | [^cais] |
| GDM | Misuse and misalignment in scope; deceptive alignment "the risk we are most concerned about"; mistakes and structural risks out of scope | [^gdm] |

---

## Caveats

- **Coverage.** Every cited primary was read, most of them whole, in the 2026-09-27 pass. The exceptions are recorded in each verification file: parts of IASR 2025, RAND-W's appendices, and NIST's action tables. "—" means not found in the document read, not absent from an organization's thinking.
- **AISI absences are weak by construction.** The agenda says: "Due to the sensitivity of our work, we cannot publish the full scope of our methods and research objectives."[^aisi-agenda]
- **Instrument kinds differ.** DSIT and GO-Science disclaim government policy status. IASR reflects neither the Chair's nor governments' views. NCSC speaks as "the authoritative voice on the cyber threat to the UK".
- **Correlated sources:**
  - VCT and CAIS share Hendrycks.
  - MIT v3 has an FLI co-author.
  - Shevlane shares authors with GDM (Farquhar) and with GovAI (Anderljung, Garfinkel).
  - AISP shares three authors with RAND-ISL.
  - SaferAI "contributed to the process of writing G42's Frontier AI Safety Framework", and G42 places third in its ranking.
  - CSET-25 and Hacker share one legal error: the "presumption of conformity" (§3).
- **Conflict of interest.** This report was written by an Anthropic model, and several sources rate Anthropic. As found:
  - **SaferAI** (v5, Apr 2026) scores Anthropic highest, at 34% (OpenAI 33%, median 18%). But it assessed RSP **v2.2** (May 2025): "Anthropic released RSP v3 in February 2026, after our assessment period closed". v3 "notably removed unilateral pause commitments".[^saferai]
  - **FLI** grades Anthropic highest in Winter 2025 (C+, 2.67) and Summer 2026 (C+, 2.66). Summer 2026 recommends Anthropic "Reverse the RSP 3.0 walk-back on pause commitments" and reports criticism of "questionable military engagements". Reviewers described Anthropic and OpenAI as "racing towards recursive self-improvement, risking an irreversible loss of control".[^fli-s26]
  - **GovAI's commentary** (the authors' views) is mixed. "Our initial reaction to the update was rather negative … after engaging with it more closely, our overall view became more positive". "Anthropic will effectively be grading its own homework."[^govai-rsp]
  - **CAIS (2023):** Anthropic "now contribute to competitive pressures".[^cais]

  The primary RSP v3.0 text was not read.
- **Remaining [U] and [F] items** are marked in the footnotes. The date of the AISI Trends report rests on secondary sources plus inference. The Digital Omnibus rests on secondary sources.

---

## References found but not yet read

These are candidates, with metadata only.
- **Campos et al. 2025**, arXiv 2502.06656: the source of SaferAI's criteria. It is in relata as `campos-2025-frontier` and was searched for organizational terms only.
- **Schuett, Dreksler, Anderljung et al. 2023**, *Towards best practices in AGI safety and governance*, arXiv 2305.07153.
- **Kulveit et al. 2025**, *Gradual Disempowerment*, arXiv 2501.16946: GDM's reference for passive loss of control.
- **Ren et al. 2024**, *Safetywashing*, arXiv 2407.21792.
- **Zwetsloot & Dafoe 2019**, "Thinking About Risks From AI: Accidents, Misuse and Structure" (Lawfare): the origin of "structural risk".
- **Anthropic RSP v3.0** (24 Feb 2026), the primary text.
- **The Future Society**, "Protecting GPAI Rules" (Jun 2025): the source of the 100/200 staffing figure.
- **NCSC**, *Near-term impact of AI on cyber threat* (Jan 2024).
- **America's AI Action Plan** (Jul 2025), and the full CAISI DeepSeek report.

---

## Footnotes

*Each footnote gives the link, the local relata key, and verbatim anchors for the claims the report makes from that source. Accessed 2026-09-26/27.*

[^act]: \[P] Regulation (EU) 2024/1689 (AI Act), OJ L 2024/1689, 12.7.2024; in force on the twentieth day after publication (Art. 113). <http://data.europa.eu/eli/reg/2024/1689/oj>. relata `eu-2024-ai-act`. Art. 3(65) (p.50) is quoted in §5.1. Art. 51(2) (p.83): "A general-purpose AI model shall be presumed to have high impact capabilities … when the cumulative amount of computation used for its training measured in floating point operations is greater than 10^25." Recital 110: "unintended issues of control relating to alignment with human intent"; "risk that a particular event could lead to a chain reaction". Recital 112: "after the open-source model release, necessary measures to ensure compliance … may be more difficult to implement." Art. 5(1)(a) is quoted in §5.3. Amended by Reg. (EU) 2026/1744, in force 27 Jul 2026 \[S: FLI AI Act Explorer; OJ text not retrieved].

[^cop]: \[P] European Commission, *General-Purpose AI Code of Practice*, Safety and Security chapter, 10 Jul 2025, official 43-page PDF. <https://ec.europa.eu/newsroom/dae/redirection/document/118119> (landing page <https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai>). relata `eu-cop-2025-safety-security`. Anchors:
    - Objective A (p.2): "adherence to the Code does not constitute conclusive evidence of compliance".
    - App. 1.3 (p.35): sources "treated as non-exhaustive, potential systemic risk sources".
    - Glossary (p.32): governance mitigations "pursuant to Commitments 1 and 7 to 10". Glossary (p.33): "systemic risk source" = "a factor which alone or in combination with other factors might give rise to systemic risk".
    - App. 1.4(2) (p.37): "Risks from humans losing the ability to reliably direct, modify, or shut down a model."
    - App. 1.4(4) (p.37): "the strategic distortion of human behaviour or beliefs by targeting large populations or high-stakes decision-makers".
    - Measure 8.1 (p.24): "This member(s) must not also be responsible for the Signatory's core business activities that may produce systemic risk (e.g. research and product development)."
    - App. 4.3(4) (p.42): "limiting the number of people who have non-hardened interface-access to model parameters".
    - Measure 1.3 (p.9) is quoted in §3.

    A mirror at marinacastellaneta.it is identical in substance, but its pagination differs.

[^guidelines]: \[P] European Commission, *Guidelines on the scope of the obligations for providers of general-purpose AI models under the AI Act*, C(2025) 5045 final, 18 Jul 2025. <https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act>. relata `ec-2025-gpai-guidelines`. ¶100 (p.27): "A code of practice is a temporary tool … As opposed to adherence to a code of practice, compliance with harmonised standards grants a presumption of conformity". ¶106 (p.29): the Commission may "impose fines of up to 3% of global annual turnover or EUR 15 million … starting on 2 August 2026." ¶103: "(self-)exfiltration of model parameters and cyberattacks" are serious incidents.

[^chairs]: \[P; unofficial host] "Statement from the Chairs and Vice-Chairs", published with the final Code, Jul 2025. <https://code-of-practice.ai/?section=safety-security> (also on artificialintelligenceact.eu, which is run by FLI). relata `eu-cop-chairs-2025-statement`. "the AI Safety unit (DG CNECT A3) should be scaled up to 100 staff, with the full implementation team of the AI Act expanding to 200." "it is nobody's job to scan what is happening at the frontier of AI development". "UK AISI has been able to recruit world-leading technical experts from places like OpenAI, Anthropic, and Google DeepMind."

[^sb53]: \[P] California SB 53 (Transparency in Frontier Artificial Intelligence Act), ch. 138, Stats. 2025, approved 29 Sep 2025. <https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53>. relata `california-2025-sb53`. §22757.12(a): a framework describing "(9) Instituting internal governance practices to ensure implementation of these processes. (10) Assessing and managing catastrophic risk resulting from the internal use of its frontier models, including risks resulting from a frontier model circumventing oversight mechanisms." §22757.11(d)(3): "Loss of control of a frontier model causing death or bodily injury." "Catastrophic risk" covers "more than 50 people or more than one billion dollars". Whistleblower protections: Labor Code §1107 ff.

[^hacker]: \[P] Hacker, Edwards & Kasirzadeh, "AI, Digital Platforms, and the New Systemic Risk", FAccT '26. <https://doi.org/10.1145/3805689.3806506>; preprint arXiv 2509.17878 (v1 22 Sep 2025; v2 23 May 2026). relata `hacker-2026-digital`. Abstract (v2): "Our framework identifies systemic risks overlooked by the DSA and AI Act — including multi-agent interactions, discrimination at scale, and large-scale hallucinations". §8.1 (p.13): "we conclude that large-scale discrimination does count as systemic risk". §8.2 (p.14): "a narrow road to the recognition of hallucination under the systemic risk framework, at best". §6.2 says Code signatories "benefit from a presumption of conformity", which contradicts Guidelines ¶100.

[^cset25]: \[S] Hoffmann, "AI Safety under the EU AI Code of Practice — A New Global Standard?", CSET blog, 30 Jul 2025. <https://cset.georgetown.edu/article/eu-ai-code-safety/>. relata `hoffmann-2025-eu-code-safety`. "providers are also expected to foster a healthy risk culture in the organization, for example by periodically informing employees about the whistleblower protection policy…". It also says the Code offers a "presumption of conformity", which Guidelines ¶100 contradicts.

[^cset21]: \[P] Arnold & Toner, *AI Accidents: An Emerging Threat*, CSET Policy Brief, Jul 2021, doi:10.51593/20200072. <https://cset.georgetown.edu/publication/ai-accidents-an-emerging-threat/>. relata `arnold-2021-ai-accidents`. Failure types (p.6/7): "robustness failures, specification failures, and assurance failures"; "Failures of assurance: the system cannot be adequately monitored or controlled during operation." Risk factors (pp.16–18): "Competitive pressure. When not using AI could mean falling behind competitors or losing profits, companies, militaries, and governments are more likely to deploy buggy AI systems, use them in reckless ways, or cut corners on testing and operator training." Also "System complexity", "Systems that operate too quickly for human intervention", "Untrained or distracted users" and "Systems with many instances".

[^iasr26]: \[P] Bengio et al., *International AI Safety Report 2026*, published 3 Feb 2026 (arXiv 2602.21012, 24 Feb 2026; byte-identical PDF). <https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026>. relata `bengio-2026-international`. Anchors:
    - p.9 fn: "this focus makes the scope of this Report narrower than that of the 2025 Report".
    - p.76: "Loss of control scenarios are scenarios in which one or more general-purpose AI systems operate outside of anyone's control, and regaining control is either extremely costly or impossible."
    - p.97: "Due to competitive pressures, AI companies may face trade-offs between faster product releases and investments in risk reduction efforts."
    - p.114: "Organisational culture, leadership structure, and incentives affect risk management efforts in various ways."
    - p.136 (Box 3.1): "As of December 2025, there are no confirmed, publicly documented instances of model weight theft."
    - Glossary p.153: "Risk factors: Properties or conditions that can increase the likelihood or severity of harm."
    - Glossary p.154: systemic risks, quoted in §5.1.

    Secretariat: the UK AI Security Institute (p.3). The report states it "does not recommend any policies".

[^iasr26-es]: \[P] *International AI Safety Report 2026, Extended Summary for Policymakers*. <https://internationalaisafetyreport.org/sites/default/files/2026-02/ai-safety-report-2026-extended-summary-for-policymakers.pdf>. relata `bengio-2026-international-extended`. p.17: "Competitive pressures can incentivise AI developers to reduce their investment in testing and risk mitigation in order to release new models quickly." ES figure numbers differ from the full report's (ES "Fig. 12" = full-report Fig. 3.1, p.98).

[^iasr25]: \[P] Bengio et al., *International AI Safety Report 2025*, DSIT 2025/001, 29 Jan 2025, arXiv 2501.17805. <https://arxiv.org/abs/2501.17805>. relata `bengio-2025-international`. p.17: "This report classifies general-purpose AI risks into three categories: malicious use risks; risks from malfunctions; and systemic risks." p.108: "the consequences of loss of control would not necessarily be catastrophic." §3.2.2(C) (key information p.176; body p.178): "The rapid growth and consolidation in the AI industry raises concerns about certain AI companies becoming particularly powerful because critical sectors in society are dependent on their products. Such companies may become more inclined to take excessive risks or cut corners on safety standards if they expect that it would be costly for governments to let the company fail." About half of this report was read in full; the rest was term-searched.

[^aisi-trends]: \[P] UK AISI, *Frontier AI Trends Report*, Dec 2025. The 18 Dec date comes from secondary sources plus an asset-ID timestamp; the cover says "2025 DECEMBER". <https://www.aisi.gov.uk/frontier-ai-trends-report>. relata `aisi-2025-frontier`. Printed page numbers are the PDF page minus 2. Anchors:
    - p.01: "The length of cyber tasks … that models can complete unassisted is doubling roughly every eight months". p.10: "an estimated upper bound".
    - p.24: "We've discovered universal jailbreaks for every system we've tested to date." The same page reports expert effort of "just 10 minutes" versus "over seven hours".
    - p.27: "the strength of safeguards appears to be determined mostly by the effort and resource invested in developing, testing, and deploying defences."
    - p.30: "By summer 2025, two frontier models had achieved a success rate of over 60%".
    - p.16: non-experts had "significantly higher odds of writing a feasible protocol (4.7x…)".
    - p.33: "yet to detect unprompted sandbagging".

[^aisi-agenda]: \[P] UK AISI, *The UK AI Security Institute's Research Agenda*, May 2025 (web page and PDF). <https://www.aisi.gov.uk/research-agenda>. relata `aisi-2025-research`; local extract `ref/ref-aisi-research-agenda.md`, word-identical to the live page. PDF p.3: "This document serves as a snapshot in time of our current research priorities." "Due to the sensitivity of our work, we cannot publish the full scope of our methods and research objectives." PDF p.6, Autonomous Systems: "Risks posed by the misuse of AI systems escalating out of control or systems taking harmful action without meaningful human oversight." PDF p.28, Control: "weight exfiltration, secret exfiltration, rogue internal deployments and sabotaging safety research". PDF p.30, Alignment: "ensure the honesty of AI systems as they scale past AGI to superintelligence".

[^dsit]: \[P] UK DSIT, *Capabilities and risks from frontier AI: A discussion paper on the need for further research into AI risk*, 25 Oct 2023. <https://www.gov.uk/government/publications/frontier-ai-capabilities-and-risks-discussion-paper>. relata `dsit-2023-capabilities`. p.2: "does not represent a policy position of HMG". p.15: "Cross cutting risk factors – technical and societal conditions that could aggravate a number of particular risks". p.18 heading: "Insufficient incentives for AI developers to invest into risk mitigation measures". p.18: "the full model is exfiltrated by employees or external actors". p.19: "actors compete to rapidly develop AI systems and under-invest in safety measures." Glossary p.30: "Risk factors: Elements or conditions that can increase downstream risks."

[^goscience]: \[P] GO-Science, *Future Risks of Frontier AI* (DSIT Annex A), Oct 2023; "NOT A STATEMENT OF GOVERNMENT POLICY". <https://assets.publishing.service.gov.uk/media/653bc393d10f3500139a6ac5/future-risks-of-frontier-ai-annex-a.pdf>. relata `goscience-2023-future`. ¶32 (p.9): "Frontier AI companies operate in a highly competitive environment… Perception of a model's power, and future development, are important to attract investment… These incentives are highly likely to influence the public and private statements from industry figures." p.25 fn iii defines a misaligned system as one that "has the capability to pursue an objective in unintended ways".

[^hmg]: \[P] HMG, *Safety and Security Risks of Generative AI to 2025* (DSIT Annex B), Oct 2023. <https://assets.publishing.service.gov.uk/media/653932db80884d0013f71b15/generative-ai-safety-security-risks-2025-annex-b.pdf>. relata `hmg-2023-safety`. p.4: "potentially anyone to pose a threat through malicious use, misuse or mishap."

[^dsit-ep]: \[P] UK DSIT, *Emerging Processes for Frontier AI Safety*, 27 Oct 2023. <https://assets.publishing.service.gov.uk/media/653aabbd80884d000df71bdc/emerging-processes-frontier-ai-safety.pdf>. relata `dsit-2023-emerging-processes`. p.26: "Secure Innovation guidance from NCSC and NPSA is available to help companies and investors to protect their technology."

[^ncsc]: \[P] NCSC, *Impact of AI on cyber threat from now to 2027*, 7 May 2025. <https://www.ncsc.gov.uk/report/impact-ai-cyber-threat-now-2027>. relata `ncsc-2025-impact`. PDF pages:
    - p.2: "There will almost certainly be a digital divide between systems keeping pace with AI-enabled threats and a large proportion that are more vulnerable".
    - p.3: "It does not cover wider threat enabled by AI, such as influence operations."
    - p.5: "direct prompt injection, software vulnerabilities, indirect prompt injection and supply chain attack are already capable of enabling exploitation of AI systems".
    - p.6: "In the rush to provide a market-leading AI model … there is a risk that developers will prioritise an accelerated release schedule over security considerations".

[^nist600]: \[P] NIST AI 600-1, *AI RMF: Generative AI Profile*, Jul 2024, doi:10.6028/NIST.AI.600-1. <https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf>. relata `nationalinstituteofstandardsandtechnologyus-2024-artificial`; the relata title field is truncated. pp.4–5: the 12 GAI risks. p.3: "This document focuses on risks for which there is an existing empirical evidence base … speculative risks that may potentially arise in more advanced, future GAI systems are not considered." p.9: foundation models as "'bottlenecks,' or single points of failure". GV-1.3-006 (p.15): "Immature safety or risk cultures related to AI and GAI design, development and deployment". GV-2.1-005 (p.17) covers whistleblower protections.

[^nist800]: \[P] NIST AI 800-1, 2nd public draft, *Managing Misuse Risk for Dual-Use Foundation Models*, Jan 2025 (US AISI; no final version found). doi:10.6028/NIST.AI.800-1.2pd. relata `nist-2025-managing`. Glossary p.22: "Misuse Risk: A risk that an AI model will be deliberately misused to cause harm"; and "permitting the evasion of human control or oversight through means of deception or obfuscation" (a dual-use criterion from EO 14110). p.12, Practice 3.1: "Consider the threat posed by insiders". p.13, Practice 3.2: "limiting access to model weights within the organization or implementing two-party control systems".

[^nist1002]: \[P] NIST AI 100-2e2025, *Adversarial Machine Learning: A Taxonomy and Terminology*. doi:10.6028/NIST.AI.100-2e2025. relata `vassilev-2025-adversarial`. Glossary: "Prompt injection: An attack which exploits the concatenation of untrusted input with a prompt constructed by a higher-trust party such as the application designer."

[^caisi]: \[P] US Department of Commerce, statement by Secretary Lutnick, 3 Jun 2025. The text comes from Wayback, because the live page blocks scripts; the key sentence also appears on nist.gov/caisi. <https://www.commerce.gov/news/press-releases/2025/06/statement-us-secretary-commerce-howard-lutnick-transforming-us-ai>. relata `commerce-2025-caisi`. "CAISI will focus on demonstrable risks, such as cybersecurity, biosecurity, and chemical weapons." It also covers "potential security vulnerabilities and malign foreign influence arising from use of adversaries' AI systems, including the possibility of backdoors and other covert, malicious behavior." "For far too long, censorship and regulations have been used under the guise of national security. Innovators will no longer be limited by these standards."

[^caisi-rfi]: \[P] CAISI/NIST, Request for Information regarding security considerations for AI agents, 91 FR 698–701, 8 Jan 2026. <https://www.federalregister.gov/documents/2026/01/08/2026-00206/request-for-information-regarding-security-considerations-for-artificial-intelligence-agents>. relata `nist-2026-rfi-agents`. p.699: "(3) the risk that the behavior of uncompromised models may nonetheless pose a threat to confidentiality, availability, or integrity (e.g., models that exhibit specification gaming or otherwise pursue misaligned objectives)."

[^caisi-ds]: \[S] NIST news release, "CAISI Evaluation of DeepSeek AI Models Finds Shortcomings and Risks", 30 Sep 2025. The full report was not read. <https://www.nist.gov/news-events/news/2025/09/caisi-evaluation-deepseek-ai-models-finds-shortcomings-and-risks>. relata `nist-2025-caisi-deepseek`. Hijacked agents were "12 times more likely than evaluated U.S. frontier models to follow malicious instructions". The models "echoed four times as many inaccurate and misleading CCP narratives".

[^randw]: \[P] Nevo et al., *Securing AI Model Weights*, RAND RR-A2849-1, 30 May 2024 (revised Jun 2024), doi:10.7249/RRA2849-1. <https://www.rand.org/pubs/research_reports/RRA2849-1.html>. relata `nevo-2024-securing`; press release `rand-2024-weights-press`. Anchors:
    - p.18: "Concern around the feasibility of threats from organization insiders … was an emerging point of consensus."
    - p.32: "Some experts strongly asserted that the model weights cannot be secure if this number is not aggressively reduced (e.g., to the low tens)". Same page: the trade-off "can be significantly mitigated by implementing more constrained and secure interfaces".
    - p.80: "Output-limited arbitrary access is limited to 100 people, access to an isolated network with direct access is limited to 50 people, and the ability to make copies of the weights is limited to 20 people."
    - p.85: "at least two dozen people or 5 percent of organization headcount, whichever is larger".
    - p.90: "Vetting of investors and other positions of influence."
    - pp.68–69: "Organizational leverage attacks".
    - p.4: "Once a model has been made publicly available … there is no longer value in securing specific copies of it."

[^randg]: \[P] Mitre & Predd, *Artificial General Intelligence's Five Hard National Security Problems*, RAND PE-A3691-4, Feb 2025, doi:10.7249/PEA3691-4. <https://www.rand.org/pubs/perspectives/PEA3691-4.html>. relata `mitre-2025-agi`. p.iii: "(1) wonder weapons; (2) systemic shifts in power; (3) nonexperts empowered to develop weapons of mass destruction; (4) artificial entities with agency; and (5) instability." p.6: "a loss-of-control scenario could result, wherein AGI's pursuit of its desired objectives incentivizes the machine to resist being turned off".

[^randisl]: \[P] Brass-Gershovich, Steratore, Hurd, Bradley, Friedman & Nevo, *Securing AI Algorithmic Insights*, RAND RR-A4685-1, 20 Jul 2026, doi:10.7249/RRA4685-1. <https://www.rand.org/pubs/research_reports/RRA4685-1.html>. relata `brassgershovich-2026-algorithmic`. Anchors:
    - p.iii: "The framework is descriptive rather than prescriptive".
    - p.5: "Generally, the more employees or contractors who work with a particular insight, the higher the risk of its theft or leakage."
    - p.vi: ISL4–5 include "government-standard personnel vetting".
    - p.26: "a complete isolation of insights is extremely difficult, possibly even infeasible."
    - p.27: "personnel security measures, behavioral monitoring, and employee-departure policies represent critical areas of investment".
    - p.44: "Former employees present a risk because of the information they possess".

    The phrase "more-intensive personnel security", which the first draft quoted, comes from RAND's landing-page summary, not the report.

[^randsl3]: \[P] Aguirre et al., *Achieving AI Model Weight Security Level 3*, RAND RR-A4704-1, 25 Aug 2026, doi:10.7249/RRA4704-1. <https://www.rand.org/pubs/research_reports/RRA4704-1.html>; controls at <https://github.com/RANDCorporation/achieving-AI-model-weight-sl3>. relata `aguirre-2026-sl3`. p.v: "140 standard security controls and 122 supplemental controls drawn from NIST SP 800-53 … designed for feasible implementation within 6 to 12 months". The same page: "The most severe barriers to implementing AI model weight security are organizational rather than technical, including resource allocation, cross-functional coordination, and balancing security with operational velocity." PS-1: "following personnel security incidents or significant changes to model weight infrastructure, access patterns, or organizational structure." Workshop: "a total of 9 voters" (pp.14–15). The report was "not professionally copyedited".

[^aisp]: \[P] Gekker, Steratore, Smith, Brass-Gershovich, Gandhi, Nichols, Bolina, Shlegeris, Einstein, Lahav, O. Nevo & S. Nevo, *AI Security Priorities: A Field-Wide Agenda*, arXiv 2607.26069 (v1 submitted 23 Jun 2026). <https://arxiv.org/abs/2607.26069>. relata `gekker-2026-aisp`. p.43: "Insider threats are among the most significant risks for AI model weight theft and intellectual property compromise." p.45: "Overly restrictive personnel security can create single points of failure, slow research, and make organizations less attractive to top talent." p.82: AI agents combine "the hard parts of both" insider and outsider threats. p.34: "'control' can refer to a very general problem of steering AI systems, or to a specific set of guardrails for artificial general intelligence." The paper discloses that several recommendations align with co-author Irregular's services (p.3).

[^anderljung]: \[P] Anderljung, Barnhart, Korinek, Leung, O'Keefe, Whittlestone et al., *Frontier AI Regulation: Managing Emerging Risks to Public Safety*, arXiv 2307.03718 (v1 6 Jul 2023; v4 7 Nov 2023). <https://arxiv.org/abs/2307.03718>. relata `anderljung-2023-frontier`. p.2: "dangerous capabilities can arise unexpectedly; it is difficult to robustly prevent a deployed model from being misused; and, it is difficult to stop a model's capabilities from proliferating broadly." p.7, examples of dangerous capabilities: bio/chem synthesis by non-experts; "highly persuasive, individually tailored, multi-modal disinformation"; "unprecedented offensive cyber capabilities"; "Evading human control through means of deception and obfuscation." p.10: "The Unexpected Capabilities Problem"; "The Proliferation Problem".

[^schuett]: \[P] Schuett, *Frontier AI developers need an internal audit function*, arXiv 2305.17038 (v1 26 May 2023; v2 5 Oct 2024); *Risk Analysis*, doi:10.1111/risa.17665. relata `schuett-2024-frontier`. Abstract: developers "do not seem to follow best practices in risk governance". Table 1 (p.11): "Frontier AI developers do not follow best practices in risk governance." p.13: "they do not seem to have established a board risk committee, appointed a chief risk officer (CRO), set up an internal audit function, or implemented the Three Lines Model". fn 19: "based on public information".

[^gomez]: \[P] Gomez, Buick, Ferentinos, Kim & Lee, *How frontier AI companies could implement an internal audit function*, arXiv 2512.14902v2, 18 Dec 2025. <https://arxiv.org/abs/2512.14902>. relata `gomez-2025-frontier`. p.11: ad hoc reviews "are appropriate when an area encounters an unexpected shock … or when rapid organizational change introduces risks not anticipated during planning."

[^cais]: \[P] Hendrycks, Mazeika & Woodside, *An Overview of Catastrophic AI Risks*, arXiv 2306.12001 (v6, 9 Oct 2023). <https://arxiv.org/abs/2306.12001>. relata `hendrycks-2023-overview`. Printed pages; the PDF is one page ahead. Anchors:
    - §3.2 (pp.19–20): "failing to coordinate and stop AI races would be the most likely cause of an existential catastrophe."
    - §3.3 (p.21): Anthropic "eventually became convinced of the 'necessity of commercialization' and now contribute to competitive pressures."
    - p.28: a strong safety culture means staff "view safety as a key objective rather than a constraint on their work".
    - p.29: safetywashing, "overstating or misrepresenting one's commitment to safety".
    - §4.2 (p.31): "their hires often do not care about safety. These norms are hard to change once they have inertia."
    - §4.3 (p.33): "a substantial portion of their employees and budgets go into research that minimizes potential safety risks: say, at least 30 percent of research scientists".
    - p.34: "a struggle for control between humans and superintelligent rogue AIs".

[^gdm]: \[P] Shah, Irpan, Turner et al. (Google DeepMind), *An Approach to Technical AGI Safety and Security*, arXiv 2504.01849, 2 Apr 2025. <https://arxiv.org/abs/2504.01849>. relata `shah-2025-approach`. p.4: "Misalignment: The AI system knowingly causes harm against the intent of the developer"; fn 3: "a very expansive notion of what it means to know something". p.9: "treat the model similarly to an untrusted insider". p.17: "we do not discuss loss of control as its own category. Our mitigations for it would be split across misuse, misalignment, and structural risks". p.51: deceptive alignment is "the risk we are most concerned about". p.55: structural risks threaten "a gradual loss of control for humanity". p.67: "many teams, which results in many people with access to the model weights."

[^shevlane]: \[P] Shevlane, Farquhar, Garfinkel et al., *Model evaluation for extreme risks*, arXiv 2305.15324 (v2 22 Sep 2023). <https://arxiv.org/abs/2305.15324>. relata `shevlane-2023-model`. Table 1 (p.5): "Cyber-offense, Deception, Persuasion & manipulation, Political strategy, Weapons acquisition, Long-horizon planning, AI development, Situational awareness, Self-proliferation." §3.4 (p.9): "insiders (e.g. internal staff, contractors), outsiders (e.g. users, nation-state threat actors), and the model itself as a vector of harm." fn 3 (p.7): "avoid making hard promises to stakeholders (e.g. customers, investors) that they will deploy a certain model at a certain date."

[^mit]: \[P] Slattery, Saeri, Grundy et al., "The AI Risk Repository", *Patterns* (2026) 101517, doi:10.1016/j.patter.2026.101517; arXiv 2408.12622v3 (5 May 2026). <https://arxiv.org/abs/2408.12622>. relata `slattery-2026-risk`. p.4: "a descriptive framework for categorising how existing taxonomies attribute risk sources". p.12: "the extracted risks were nearly equally attributed to AI systems (42%) versus human decisions (38%)". Supp. Table S2: Human 38 / AI 42 / Other 20. MIT is internally inconsistent: it reports 37% on p.13. p.3: "the same word may describe different problems, while different words describe identical concerns."

[^saferai]: \[P] Stelling, Murray, Galizzi, Schaffelder, Campos & Papadatos (SaferAI), *Evaluating AI Providers' Frontier Safety Frameworks*, arXiv 2512.01166 (v1 1 Dec 2025; figures from v5, 30 Apr 2026). <https://arxiv.org/abs/2512.01166>. relata `stelling-2025-evaluating`. "Overall scores range from 34% (Anthropic) to 8% (Cohere), with a median of 18%." fn 7 (p.10): "We assess Anthropic's Responsible Scaling Policy v2.2 (May 2025). Anthropic released RSP v3 in February 2026, after our assessment period closed." The criteria are "an aspirational benchmark rather than a description of current or achievable industry practice" (p.10).

[^vct]: \[P] Götting, Medeiros, Sanders, Li, Phan, Elabd, Justen, Hendrycks & Donoughe, *Virology Capabilities Test (VCT)*, arXiv 2504.16137 (v2 29 Apr 2025). <https://arxiv.org/abs/2504.16137>. relata `gotting-2025-virology`. Abstract: "OpenAI's o3, reaches 43.8% accuracy, outperforming 94% of expert virologists even within their sub-areas of specialization." p.10: "Our benchmark, by itself, does not directly assess the capabilities of humans who draw upon that model for assistance in real-world virology work."

[^fli-w25]: \[P] Future of Life Institute, *AI Safety Index: Winter 2025*, 2 Dec 2025. <https://futureoflife.org/ai-safety-index-winter-2025/>. relata `fli-2025-ai-safety-index-winter`. The Company Structure & Mandate indicator (printed p.74) "evaluates whether a company's fundamental legal structure, ownership model, and fiduciary obligations enable safety prioritization over short-term financial pressures in high-stakes situations." The Reporting Culture indicator (p.81–82) draws evidence from "(vi) departures linked to safety governance."

[^fli-s25]: \[P] Future of Life Institute, *AI Safety Index: Summer 2025*, Jul 2025. <https://futureoflife.org/wp-content/uploads/2025/07/FLI-AI-Safety-Index-Report-Summer-2025.pdf>. relata `fli-2025-ai-safety-index-summer`. p.18: "High turnover on the safety team and failure to meet Superalignment commitments were taken as an indication of a concerning shift in priorities."

[^fli-s26]: \[P] Future of Life Institute, *AI Safety Index: Summer 2026*, Jul 2026 (evidence to 3 Jun 2026). <https://futureoflife.org/ai-safety-index-summer-2026/>. relata `fli-2026-ai-safety-index-summer`. p.4: "Anthropic, OpenAI, Google DeepMind, and Meta have weakened or voided pledges to pause unilaterally if redlines are approached, some citing competitor-contingent conditions"; "Safety rhetoric outpaces revealed behavior". The Anthropic recommendation reads: "Reverse the RSP 3.0 walk-back on pause commitments and restore credibility of commitments." p.22: "racing towards recursive self-improvement, risking an irreversible loss of control".

[^govai-rsp]: \[P, authors' views] Williams & Freund, "Anthropic's RSP v3.0: How it Works, What's Changed, and Some Reflections", GovAI Commentary, 5 Mar 2026 (updated 17 Mar). <https://www.governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections>. relata `williams-2026-anthropic-rsp-v3`. "Anthropic also dropped its pause commitment." "Anthropic will effectively be grading its own homework." "On balance, we think it's better to be honest about constraints than to keep commitments that won't be followed in practice."

[^metr]: \[P] METR, *Common Elements of Frontier AI Safety Policies*, Dec 2025. <https://metr.org/common-elements.pdf>. relata `metr-2025-common-elements`. A search for growth, turnover, investor and IPO terms found nothing relevant.

[^icao]: \[P] ICAO, *Safety Management Manual*, Doc 9859, 4th ed. (advance unedited), 2018. Mirror: <https://aviation-insight.aero/wp-content/uploads/2021/05/9859_4th_ed_unedited_en.pdf>. relata `icao-2018-doc9859-smm`. §§8.5.3.8 and 9.5.5 are quoted in §4. Check the final edition's paragraph numbers before citing externally.

[^hse]: \[P] UK HSE, *Organisational change and major accident hazards*, CHIS7, Jun 2003. <https://www.hse.gov.uk/pubns/chis7.pdf>. relata `hse-2003-chis7`. Quoted in §4.

[^csb]: \[P] US CSB, *Investigation Report: Refinery Explosion and Fire, BP Texas City*, Report 2005-04-I-TX, Mar 2007. <https://www.csb.gov/assets/1/20/csbfinalreportbp.pdf>. relata `csb-2007-bp-texas-city`. Quoted in §4.

[^iaea]: \[P] IAEA, *Leadership and Management for Safety*, GSR Part 2, 2016. <https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1750web.pdf>. relata `iaea-2016-gsr-part2`. ¶4.13 (p.10) is quoted in §4.

[^npsa]: \[P] UK NPSA and NCSC, *Secure Innovation: Security Advice for Emerging Technology Companies*, booklet v4 (Jul 2024). <https://www.npsa.gov.uk/system/files/2024-07/secure_innovation_booklet_packaged-npsa-v4.pdf>. relata `npsa-2024-secure-innovation`. Printed pp.26 and 30 (PDF pp.14 and 16) are quoted in §4.

[^cisa]: \[P] CISA, *Insider Threat Mitigation Guide*, Sep 2026 ed. <https://www.cisa.gov/sites/default/files/2026-09/cisa-insider-threat-mitigation-guide-2026.pdf>. relata `cisa-2026-insider-threat-guide`. p.67, "Organizational Indicator Examples": "High stress environment … Pattern of overwork … Heightened uncertainty, either financial or contractual … Recent merger/acquisition … Under-trained staff (particularly in cybersecurity)".

[^mou]: \[P] California DOJ (Attorney General) and OpenAI, *Memorandum of Understanding re Notice of Conditions of Non-Objection*, 27 Oct 2025. <https://oag.ca.gov/system/files/attachments/press-docs/Final%20Executed%20MOU%20Between%20OpenAI%20and%20California%20AG%20re%20Notice%20of%20Conditions%20of%20Non-Objection%20%2810.27.2025%29%20%28Signed%20by%20OpenAI%29%20%28Signed%20by%20CA%20DOJ%29.pdf>. relata `caag-2025-openai-mou`. ¶8 (p.3): the PBC Board must "consider only the Mission (and may not consider the pecuniary interests of stockholders or any other interest) in respect of safety and security issues related to the OpenAI enterprise". ¶11: the Safety and Security Committee may require mitigations "up to and including halting the release of models or AI systems".

[^carpt]: \[P] Joint California Policy Working Group on AI Frontier Models, *The California Report on Frontier AI Policy*, 17 Jun 2025, arXiv 2506.17303. relata `bommasani-2025-california`. §5.1: "major players in the space, such as Anthropic, OpenAI, and xAI, may be relatively small according to some conventional metrics of businesses (e.g., head count)." Headcount appears only as a scoping variable.

[^altman]: \[S]\[F] J. Ma, *Fortune*, 12 Sep 2026. <https://fortune.com/2026/09/12/sam-altman-openai-ipo-delay-ill-advised-moment-safety-concerns/>. Altman: "I actually think that, given everything happening with safety, right now would be an ill-advised moment to go public."

[^axios]: \[S]\[F] D. Primack, "Anthropic IPO won't be slowed by safety uproar", *Axios*, 14 Sep 2026, read via the Yahoo Finance mirror: <https://finance.yahoo.com/technology/ai/articles/anthropic-ipo-wont-slowed-safety-141851836.html>. "Anthropic is still likely to go public in 2026".

[^san]: \[C]\[F] D. Pavlou, "Going public puts Anthropic's safety mission under new pressure", *Straight Arrow News*, 1 Jun 2026. <https://san.com/cc/going-public-puts-anthropics-safety-mission-under-new-pressure/>.

[^aguilar]: \[C]\[F] O. Aguilar & C. Bracy, *Fortune* op-ed, 22 Jul 2026. <https://fortune.com/2026/07/22/openai-foundation-class-n-stock-board-control-ipo/>. "The SEC has a clear responsibility to ensure investors are aware of the unprecedented nature of OpenAI's governance structure."
