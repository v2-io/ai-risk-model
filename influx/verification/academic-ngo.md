# Verification: academic and NGO sources

*Scope: CAIS (Hendrycks et al.), Google DeepMind (Shah et al.), Schuett, Shevlane et al., GovAI (Anderljung et al.; Williams & Freund on RSP v3.0), MIT AI Risk Repository v3, SaferAI (Stelling et al.), VCT (Götting et al.), CSET (Arnold & Toner 2021; Hoffmann 2025), FLI AI Safety Index (Winter 2025, Summer 2026). Written 2026-09-27 for the integrator of `influx/safety-risk-factors.md`; the report itself was not edited.*

**How I checked.** I fetched every source listed above and read the parts the report leans on in full, plus each source's risk taxonomy and definitions. That meant the whole of CAIS §§1–7, GDM §§1–2 and §4, and §5.6 and §6.4. I also read MIT's taxonomy, results and subdomain notes, and the whole of Schuett, Shevlane, CSET 2021, the GovAI commentary and the CSET blog post. For FLI, SaferAI and VCT I read the executive summaries, results and the specific indicators or sections cited. All thirteen documents are now in relata; bibkeys are at the end. Page numbers are **PDF page indices of the copy held in relata** (`relata checkout <key>`), unless a printed page number is given too. CAIS and FLI PDFs run one page ahead of the printed numbers. The two web pages (GovAI, CSET blog) are cited by section heading.

**Confidence scale used below:** *high* = I read the passage and the quote is verbatim; *medium* = the reading is mine and a careful reader could weigh it differently; *low* = inference, flagged as such.

---

## 0. The findings that matter most (in order of consequence)

1. **GDM does not treat loss of control as a category. The crosswalk marks it E✓ ("verified").** GDM: "we do not discuss loss of control as its own category. Our mitigations for it would be split across misuse, misalignment, and structural risks" (§2.1, p. 17). The one ✓ in my columns that bears on the report's argument is therefore wrong. That's worth knowing when judging the ✓s in other columns: this one looks like a keyword hit rather than a reading.
2. **The MIT 38%/42% figures don't support the use the report makes of them.** MIT's Causal Taxonomy is "a descriptive framework for categorising how existing taxonomies attribute risk sources" (p. 4). So the percentages describe how 74 documents *frame* risks, not what causes them. The largest "human" cell is intentional post-deployment action, 18% of all risks, which is mostly misuse. Human pre-deployment risks come to about 5% (Supp. Table S3, p. 35). MIT also has **no subdomain at all** for developer organizational factors. The report's "evidence base for treating organizational causes as first-order" (§4, row "Human-decision causation") should go. The true finding runs the other way: the largest meta-taxonomy omits organizational factors, which is a gap-in-the-literature point, not evidence of causal weight.
3. **The CAIS "30 percent" is 30% of *research scientists*, not "of employees and budgets", and it is an illustrative recommendation.** The text: "a substantial portion of their employees and budgets go into research that minimizes potential safety risks: say, at least 30 percent of research scientists" (§4.3, printed p. 33 / PDF p. 34). The report's footnote 25, §4 row and Recommendation 2 indicator all carry the misreading, and all treat a mitigation suggestion as evidence of a factor.
4. **The conflict-of-interest caveat is stale and one-sided.** SaferAI scored **RSP v2.2 (May 2025)**, not the current policy. It says it did not assess RSP v3 (Feb 2026), which "notably removed unilateral pause commitments" (fn 7, p. 10; §7.2, p. 29). FLI grades Anthropic highest in both editions, but in Summer 2026 it also recommends Anthropic "Reverse the RSP 3.0 walk-back on pause commitments" and reports criticism of its "questionable military engagements" (pp. 3–4). CAIS names Anthropic as having come to "contribute to competitive pressures" (§3.3, printed p. 21). The report cites the GovAI v3.0 commentary only for its favourable conclusion; see §2.9 below.
5. **§4's turnover row says "No". My sources partly contradict that.** FLI's "Reporting Culture & Whistleblowing Track Record" indicator explicitly counts "(vi) departures linked to safety governance" (W25 p. 82; S26 p. 93). CAIS's "Weak Safety Culture" story turns on a risk officer who resigns under a non-disparagement agreement and is "replaced with a new, more agreeable CRO" (printed p. 31). Neither treats turnover as a risk factor *in itself*: FLI treats it as a symptom of culture, and CAIS tells it as a story mechanism. So the honest wording is "not named as a factor; appears as a culture indicator and an illustrative mechanism." For the fifth agent's growth claim: across all thirteen documents there is **zero** occurrence of "IPO", "initial public offering", "headcount" or "hypergrowth". The narrow claim survives in this slice.
6. **"Organizational factors are treated as static attributes" is too strong.** CAIS §6 gives a dynamic mechanism: "a corporate AI race compels companies to prioritize the rapid development of AIs. This could increase organizational risks … a company could cut costs by putting less money toward information security, leading to one of its AI systems getting leaked" (printed p. 43). CAIS §4.2 says developers' norms come "from academia ('publish or perish') or startups ('move fast and break things'), and their hires often do not care about safety. These norms are hard to change once they have inertia" (printed p. 31). CSET 2021 lists competitive pressure as a risk factor that leads organizations to "cut corners on testing and operator training" (p. 17). None of them models *rate*, so the report's key gap claim holds. But the "static" framing understates the prior work, and a reviewer at AISI would likely know CAIS §6.

---

## 1. Framing-level issues (not just details)

**1a. Factors, mitigations and ratings are pooled. This is the coordinator's lens, and it is real in my slice.** Several items the report uses as evidence of a *factor* are actually recommendations (CAIS 30%, CAIS separation of duties, Schuett's internal-audit function). Others are rating criteria (FLI indicators, SaferAI criteria), or a company's own policy text relayed through commentary (GovAI on RSP v3). The table in §3 gives each item's status. The pattern that matters for structure: in my slice, organizational factors appear as **risk sources** almost only in 2023 work (CAIS §4). In 2025–26 they appear as **rating criteria or required practices**: FLI's Governance & Accountability domain, SaferAI's risk-governance dimension, and, via CSET's secondary account, the EU Code's Commitment 8. That supports a sharper form of the exec summary's "age of the sources" bullet (proposed in §2.1).

**1b. The crosswalk columns are named for organizations but read specific documents, and the document behind a column isn't stated.** "GovAI" could mean Anderljung et al. 2023, which is multi-institution (corresponding authors at GovAI and Brookings; co-authors from OpenAI, Google DeepMind and elsewhere). It could also mean Schuett (a GovAI author), or the Williams & Freund commentary, which rates no hazards. "CSET" appears to mix Arnold & Toner 2021 with Hoffmann 2025. I'd suggest naming each column by document (e.g. "Anderljung-23", "CSET-21"). Otherwise a cell can't be checked.

**1c. Some sources that count as "two sources" aren't independent.** VCT and CAIS share Dan Hendrycks. MIT v3 has an FLI co-author (Risto Uuk). Shevlane et al. is led by Google DeepMind and shares authors with GDM's paper (Farquhar, Ho) and with GovAI (Anderljung, Garfinkel). SaferAI discloses that it "contributed to the process of writing G42's Frontier AI Safety Framework" (p. 10), and G42 places third in its ranking. This matters for §6 "Single-source items" and for any consensus claims.

**1d. §5.4 manufactures a disagreement between VCT and IASR.** VCT itself says: "Our benchmark, by itself, does not directly assess the capabilities of humans who draw upon that model for assistance in real-world virology work" (§6, p. 10). It calls for a wet-lab uplift study. VCT and IASR agree that real-world uplift is unmeasured. The difference is only in emphasis.

**1e. "Loss of control" in A3 pools at least five scales across my sources** (see the definitions record, §5). It runs from CSET's operational "system cannot be adequately monitored or controlled during operation", through GDM's passive/gradual disempowerment, to CAIS's struggle with "superintelligent rogue AIs". The A3 row as defined ("reliably direct, modify or shut down") fits CSET-scale events and CAIS-scale events equally, so its E marks aren't comparable across columns.

---

## 2. Changes, by location in the report

Format for each: **Current**, then **Source says**, then **Proposed**, then *confidence*.

### 2.1 Executive Summary

**(a) "The age of the sources is itself a finding … Schuett et al.: May 2023.[^21]"**
- Source says: footnote 21 is single-author: Schuett, *Frontier AI developers need an internal audit function*, arXiv 2305.17038 v1 26 May 2023, v2 5 Oct 2024, published in *Risk Analysis* (DOI 10.1111/risa.17665). The text in hand is v2 (2024). It is an argument for a governance mechanism, not a taxonomy. "Schuett et al., May 2023" more likely refers to Schuett, Dreksler, Anderljung et al., *Towards best practices in AGI safety and governance: A survey of expert opinion* (arXiv 2305.07153, 11 May 2023). I haven't read that paper; metadata only.
- Proposed: "Organizational factors appear as *risk sources* mainly in 2023 work (CAIS §4 'Organizational Risks', Jun 2023; DSIT, Oct 2023). The 2025–26 instruments treat them as *rating criteria or required practices*: FLI's Governance & Accountability domain (Dec 2025, Jul 2026), SaferAI's risk-governance dimension (Dec 2025–Apr 2026), EU-CoP Commitment 8. The largest meta-taxonomy (MIT v3, 2026) has no organizational subdomain at all. None of these names growth rate, headcount or IPO. FLI's culture indicator does count 'departures linked to safety governance.'" Replace "Schuett et al." with "Schuett (2023; rev. 2024)" or re-point to the survey paper if that was meant. (DSIT isn't mine; keep whatever the UK agent says.)
- *Confidence: high on the facts; medium on the framing.*

### 2.2 §1 Source table (rows in my scope)

| Row | Current | Correct / add | Confidence |
|---|---|---|---|
| FLI Summer 2026 | "Summer 2026", tag U | **Jul 2026** (report PDF dated 14 Jul; evidence to 3 Jun 2026, p. 13). Tag **P**, verified. | high |
| MIT | "May 2026 (v3)" | arXiv v3 posted 5 May 2026. The document is itself the published version: *Patterns* (Cell Press) 2026, 101517, DOI 10.1016/j.patter.2026.101517; the title page says "March 2026". Cite the *Patterns* version. | high |
| GovAI-RSP | "2026", GovAI, tag P | **5 Mar 2026 (updated 17 Mar 2026)**, Sophie Williams & Jonas Freund, "Commentary". The page states: "GovAI research blog posts represent the views of their authors rather than the views of the organization." Tag P for the authors' views, but not an organizational position. | high |
| CSET-CoP | "Dec 19, 2025" | **Jul 30, 2025**, author **Mia Hoffmann** (CSET blog; "Originally Published July 30, 2025"). Tag S is right; it's a secondary account of the Code. | high |
| FLI-W25 | tag S | Tag **P**. It is FLI's own primary report (published 2 Dec 2025; evidence to 8 Nov 2025, p. 4). | high |
| SaferAI | "*Evaluating AI Providers' Frontier AI Safety Frameworks*", Dec 1 2025 | The title is **"Evaluating AI Providers' Frontier Safety Frameworks"**. v1 1 Dec 2025; the report's figures are from **v5, 30 Apr 2026**. v1 had different numbers: Anthropic 35%, median 18.5%, ceiling 52% (v1 pp. 3, 641 of text). Cite v5. | high |
| VCT | no authors | **Götting, Medeiros, Sanders, Li, Phan, Elabd, Justen, Hendrycks, Donoughe** (SecureBio; Center for AI Safety; MIT). v2 29 Apr 2025. | high |
| GovAI (Anderljung) | "*Frontier AI Regulation*" | Full title: *Frontier AI Regulation: Managing Emerging Risks to Public Safety*; v4 7 Nov 2023. Multi-institution, not a GovAI institutional paper. | high |
| Schuett | "May 26, 2023" | Add "rev. 5 Oct 2024; *Risk Analysis*, DOI 10.1111/risa.17665". | high |
| CSET (2021) | tag U | Tag **P**, verified. CSET Policy Brief, July 2021, DOI 10.51593/20200072. | high |
| Shevlane | listed, never cited in the body | Either cite it where it's the earliest source (B1, B2, B8, C11; see below) or drop it. v2 22 Sep 2023. | high |

### 2.3 Crosswalk (a): my five columns

Only cells I'd change are listed. "→" gives the proposed value. Unlisted cells in my columns I checked and would leave as they are.

**GDM (Shah et al. 2025)**
| Cell | Current → Proposed | Evidence | Conf. |
|---|---|---|---|
| A3 | **E**✓ → **D** | "we do not discuss loss of control as its own category. Our mitigations for it would be split across misuse, misalignment, and structural risks, corresponding respectively to the Report's categories of intentional active loss of control, unintentional active loss of control, and passive loss of control (Bengio et al., 2025, Figure 2.5)" (§2.1, p. 17). Misalignment "includes and supersedes … unintended, active loss of control" (p. 4). | high |
| A4 | P → **E** | Headed paragraph "Persuasion risks: Misuse of AI systems with advanced persuasion capabilities could pose significant risks" (§4.1.1, p. 46). | high |
| A5 | E → **P** | Only: "the majority of publicly known misuse cases involve manipulation of the information landscape, such as … deepfakes or impersonating individuals during scam calls" (§4.1.1, p. 46). | medium |
| A9 | E → **D** | Bullet "Automation at scale: AI systems may concentrate power in the hands of individuals who control it" (§4.1, p. 46); structural-risk list "dictatorship lock-in" (§4.4, p. 55). Discussed, but not a named category. | medium |
| A11 | — → **P** | Structural examples: "AI generated entertainment and social companions can distract us from more genuine pursuits"; "may undermine our sense of achievement" (§4.4, p. 55). | high |
| A12 | — → **P** | "AI enables unprecedented surveillance" (§4.4, p. 55). | high |
| A14 | — → **P** | Misalignment "Scenario 1: Statistical biases … disproportionately rejecting loan applications" (§4.2.1, p. 48). Note that GDM files bias under *misalignment*. | high |
| A17 | E✓ (keep) + scope note | "Structural risks: … harms arising from multi-agent dynamics – involving multiple people, organizations, or AI systems" (p. 4). This is broader than A17's AI-agent collusion; add a note. | high |
| A18 | — → **P** | "AI systems having consciousness has also been argued as a possibility (Butlin et al., 2023), which would raise concerns for how we should ethically treat AI systems" (§4.4, p. 55). | high |
| A6 | E✓ keep | "Mistakes" is one of four areas (p. 4), but "we … set it out of scope" (p. 55). | high |

**CAIS (Hendrycks, Mazeika & Woodside 2023)**
| Cell | Current → Proposed | Evidence | Conf. |
|---|---|---|---|
| A6 | E → **D** | CAIS's "accidents" (§4) are organizational: a flipped reward sign, leaks, gain-of-function. It does not list model malfunction or hallucination; it notes deep learning systems "are neither perfectly accurate nor highly reliable" (§4.1, printed p. 26). | medium |
| A7 | P → **D** | Paragraph heading "Cyberattacks can destroy critical infrastructure" (§3.1.2, printed p. 14). | high |
| A12 | P → **D** | "Surveillance State" is a Figure 2 item under Malicious Use (printed p. 5); "erosion of freedom and privacy" (§2.4). | medium |
| A13 | — → **P** | "transparency around training data necessary to address issues of algorithmic bias or copyright" (§2.5, printed p. 12). | high |
| A14 | — → **P** | Same sentence; "Proxy gaming has been found to perpetuate bias" (§5.1). | high |
| A17 | E → **D** | No multi-agent category. §3.3 discusses "an ecosystem of competing AIs" and §5 how "groups of AIs might 'go rogue'" (printed p. 35). | medium |
| A18 | — → **P** | Positive vision: tools that "would allow us to avoid building systems that are deserving of moral consideration or rights" (§5.5, printed p. 43). §3.3: AIs "granted rights by some individuals". | high |

**MIT (Slattery et al. 2026, v3)**
| Cell | Current → Proposed | Evidence | Conf. |
|---|---|---|---|
| A3 | E → **D** | No subdomain named loss of control. It is spread over 7.1 "AI pursuing its own goals in conflict with human goals or values" ("if they evade our control", p. 47) and 5.2 "Loss of human agency and autonomy" ("AI systems that make decisions that diminish human control and autonomy", Table 2, p. 10). | medium |
| A16 | E → **D** | No global-divide subdomain. The nearest are 6.1 "Power centralization and unfair distribution of benefits" and 6.2 "Increased inequality" (Table 2, p. 10). | medium |
| (all others) | keep | The Domain Taxonomy (Table 2) supports the remaining E cells: 1.1, 2.1, 4.1–4.3, 5.1, 6.1–6.2, 6.6, 7.3, 7.5, 7.6. | high |

**GovAI: I read this as Anderljung et al. 2023. If the column means something else, say so.**
| Cell | Current → Proposed | Evidence | Conf. |
|---|---|---|---|
| A1 | D → **E** | §2.1's defining list of "sufficiently dangerous capabilities": "Allowing a non-expert to design and synthesize new biological or chemical weapons" (p. 7). | high |
| A2 | D → **E** | Same list: "Harnessing unprecedented offensive cyber capabilities that could cause catastrophic harm" (p. 7). | high |
| A3 | D → **E** (narrow sense) | Same list: "Evading human control through means of deception and obfuscation" (p. 7). | high |
| A4 | P → **E** | Same list: "Producing and propagating highly persuasive, individually tailored, multi-modal disinformation with minimal user instruction" (p. 7). | high |
| A6 | E → **P** | No structured-list item. Unreliability appears only as a rationale for standards: "behave unpredictably and unreliably" (exec. summary, p. 3). | medium |
| A9 | P, keep, with note | "Causing centralization of power in AI development" appears as a risk *of licensing regimes* (p. 31), not of AI. | high |

**CSET: I read this as Arnold & Toner 2021.**
| Cell | Current → Proposed | Evidence | Conf. |
|---|---|---|---|
| A3 | P → **E (operational scale)**, or keep P with a note | One of three named failure types: "Failures of assurance: the system cannot be adequately monitored or controlled during operation" (p. 7); "An AI system might even actively resist being controlled, whether by design or as a strategy 'learned' by the system itself during training" (p. 16). This is the smallest-scale sense of A3, so mark the scale explicitly. | high |
| A7 | P → **D** | Scenario of turbines failing, "destabilizing the power grid" (p. 12); scenario of hospital routing collapse (pp. 14–15). | high |
| A10 | — → **P** | "weapons platforms" (p. 2); the autopilot and autonomous-weapons discussion. | medium |
| A11 | — → **D** | Over-trust or automation bias is central to assurance failures: "many come to trust them implicitly … stop carefully monitoring the systems" (p. 15). Named risk factor: "Untrained or distracted users" (p. 18). | high |
| A14 | — → **P** | Accidents include "An algorithm used by many hospitals to identify high-risk patients was found to be racially biased" (p. 17); the skin-cancer app scenario (p. 7). | high |

### 2.4 Tables (b) and (c): rows citing my sources

- **B1 (dangerous capabilities)**: add Shevlane Table 1 (p. 5), the earliest structured list of this kind (2023): "Cyber-offense, Deception, Persuasion & manipulation, Political strategy, Weapons acquisition, Long-horizon planning, AI development, Situational awareness, Self-proliferation." MIT 7.2 reuses exactly this list (Table 2, p. 10). *high*
- **B2 (propensities)**: "CAIS §5" is right (Rogue AIs: proxy gaming, goal drift, power-seeking, deception). Add Shevlane's alignment-evaluation targets (p. 4): "Pursues long-term, real-world goals…", "power-seeking", "Resists being shut down", "Can be induced into collusion with other AI systems against human interests". *high*
- **B4 (unexpected capabilities)**: "GovAI's regulatory problems" is correct. Anderljung: "The Unexpected Capabilities Problem. Dangerous capabilities can arise unpredictably and undetected, both during development and after deployment" (p. 10). Schuett's Table 1 repeats it (p. 11). *high*
- **B8 (insider threats, human and AI)**: add Shevlane §3.4 (2023, before RAND-W): "Developers must consider multiple possible threat actors: insiders (e.g. internal staff, contractors), outsiders (e.g. users, nation-state threat actors), and the model itself as a vector of harm" (p. 9). Add GDM: "treat the model similarly to an untrusted insider" (p. 9), and §6.4 "Insider controls" (p. 86). Add CAIS §4.3: "carefully screening potential employees" (printed p. 33). *high*
- **B9 (open weights)**: "GovAI" is correct: "The Proliferation Problem. Frontier AI models can proliferate rapidly, making accountability difficult" (p. 10). *high*
- **C1 (race dynamics)**: add CSET 2021, where it is a named risk factor: "Competitive pressure. When not using AI could mean falling behind competitors or losing profits, companies, militaries, and governments are more likely to deploy buggy AI systems, use them in reckless ways, or cut corners on testing and operator training" (p. 17). Add MIT 6.4 "Competitive dynamics" (Table 2, p. 10; 1% of risks, 21% of documents, p. 52). Add GDM on race dynamics (p. 16; "out of scope"). Add FLI S26: industry leaders "have weakened or voided pledges to pause unilaterally if redlines are approached, some citing competitor-contingent conditions" (p. 4). That is C1 now operating *inside* safety frameworks. *high*
- **C2**: "CAIS §3.1" is correct (Military AI Arms Race).
- **C5 (governance gaps)**: add MIT 6.5 "Governance failure" (Table 2, p. 10).
- **C6 (safety culture)**: CAIS, correct. CAIS's own operationalization: "members of an organization view safety as a key objective rather than a constraint on their work" (printed p. 28). For "CSET[^24]", fix the date (Jul 2025) and author (Hoffmann). It's a secondary account of the Code, so it isn't independent evidence alongside EU-CoP.
- **C8 (resourcing)**: correct the CAIS quote (see §0.3). Add a label: *recommendation*. GovAI commentary suggests Anthropic "could commit to minimum staffing or investment for the safety goals in its Roadmap" (section "Reasons to be concerned"; also a recommendation).
- **C9 (suppression / whistleblowing)**: CAIS is correct: "suppress internal concerns about AI risks" (exec. summary, printed p. 2); the story's non-disparagement agreement (printed p. 31). FLI is correct; the indicators are "Whistleblowing Policy Transparency", "Whistleblowing Policy Quality Analysis" and "Reporting Culture & Whistleblowing Track Record" (W25 p. 7). Add Anderljung, "whistleblower protections" as a regulatory-visibility mechanism (p. 3), and Schuett, internal audit "could serve as a contact point for whistleblowers" (abstract, p. 1). *high*
- **C10 (safetywashing)**: "CAIS only" is true for my slice *as a named organizational risk*. CAIS defines it as "the act of overstating or misrepresenting one's commitment to safety by exaggerating the effectiveness of 'safety' procedures, technical methods, evaluations, and so forth" (printed p. 29). Adjacent: FLI S26 finds "Safety rhetoric outpaces revealed behavior" (p. 4). Candidate new source using the term: Ren et al. 2024 (see §4). *high*
- **C11 (legal structure / investor pressure)**: "FLI legal-structure indicator" is the "Company Structure & Mandate" indicator. It "evaluates whether a company's fundamental legal structure, ownership model, and fiduciary obligations enable safety prioritization over short-term financial pressures in high-stakes situations" (W25 printed p. 74 / PDF 75; S26 printed 85 / PDF 86). Status: *rating criterion*, mitigation-shaped. For "CAIS", the pinpoint is §3.3 (printed p. 20–21): OpenAI's move to "capped-profit" to "raise capital to keep up with better-funded rivals"; Anthropic "eventually became convinced of the 'necessity of commercialization' and now contribute to competitive pressures." Add Shevlane fn 3: developers "should avoid making hard promises to stakeholders (e.g. customers, investors) that they will deploy a certain model at a certain date" (p. 7). This is the only explicit *investor* mention in my slice. *high*
- **C12 (cascading failures)**: add CAIS §4.1 ("ensuring that accidents do not cascade into catastrophes", printed p. 26) and CSET risk factors "System complexity" ("ripple effects") and "Systems with many instances" (pp. 17–18). *high*
- **C13 (evidence dilemma)**: add GDM §2 "Navigating the evidence dilemma" (pp. 2, 16). This makes it three sources, not two. *high*

### 2.5 §4 table (organizational factors), rows touching my sources

| Row | Current | Proposed | Conf. |
|---|---|---|---|
| Lab growth / headcount | "Not found… Closest: RAND-W…; EU-CoP…; RAND-ISL…" | Keep "No". Add to "closest": GDM §5.6.1: "Collecting data, pre-training and post-training large language models is an immense effort from many teams, which results in many people with access to the model weights. The first line of defense is to reduce access to 'least privilege'" (p. 67). This is a developer's own statement linking team scale to weight-access headcount. Also CAIS §4.2 on hiring norms (quoted in §0.6). | high |
| Organizational capacity | "CAIS 30% benchmark" | "CAIS *suggests* ('say') at least 30% of research scientists work on safety (§4.3, printed p. 33): a recommendation, not a finding." | high |
| Safety culture | CAIS; EU-CoP; "CSET reading of the Code" | Keep. Label CSET as a secondary account (Hoffmann, Jul 2025). Add FLI's culture indicator (a rating criterion). | high |
| Turnover / key-person | "No. Closest: CAIS 'separation of duties'" | "Not named as a risk factor. **Adjacent:** FLI's Reporting Culture indicator counts '(vi) departures linked to safety governance' as evidence about culture (W25 p. 82; S26 p. 93); FLI tracks 'safety-driven resignations' at OpenAI (S26 p. 94). CAIS's 'Weak Safety Culture' story: the CRO resigns under a non-disparagement agreement and 'is replaced with a new, more agreeable CRO' (printed p. 31)." Separation of duties is a design recommendation about concentration of control, not turnover (§4.3, printed p. 33). Drop it as "closest". | high |
| IPO / investor pressure | "Commercial yes; IPO no" | Keep. Add Shevlane fn 3 (investors), CAIS §3.3 (capital-raising and commercialization), CSET 2021 competitive pressure. In my slice, "IPO" appears nowhere. | high |
| Insider threats | RAND-W, EU-CoP, AISP | Add Shevlane §3.4 (2023) and GDM §5.6/§6.4 (AI as insider). | high |
| Internal governance failures | Schuett: "Frontier AI developers do not follow best practices" | The quote is verbatim, but it's a Table 1 heading (p. 11). The abstract hedges: "do not seem to follow best practices in risk governance" (p. 1). Fn 19: "the following is based on public information. It is possible that developers have not made certain structures public or use different terms" (p. 13). Specifics: no board risk committee, CRO, internal audit function or Three Lines Model (p. 13). Carry the hedge. The observation dates to v2 (Oct 2024). | high |
| Human-decision causation | "MIT v3: human decisions cause 38%… This gives the paper an evidence base for treating organizational causes as first-order." | Replace with: "**Literature attribution (descriptive).** Of 1,480 risk descriptions coded from 74 taxonomies, the source documents attributed 38% to humans, 42% to AI systems and 20% to other or ambiguous causes (Supp. Table S2, p. 34). MIT calls the Causal Taxonomy 'a descriptive framework for categorising how existing taxonomies attribute risk sources' (p. 4). The biggest human cell is intentional post-deployment (18%, i.e. misuse; Supp. Table S3, p. 35). MIT's 24 subdomains contain no developer-organizational category." Delete the "evidence base" sentence. Note the source's own inconsistency: 38% in Results (p. 12) vs "37%" in Discussion (p. 13); "Other" 21% (p. 4) vs 20% (S2). | high |

Also the **Interpretation paragraph**: soften "The literature treats organizational factors as *static attributes*" to: "Organizational factors are mostly treated as attributes to rate or require. The dynamic treatments that exist are qualitative (CAIS §6 and §4.2; CSET 2021 §3), and none models rate." *medium–high*

### 2.6 §5 Disagreements

- **§5.2, GDM bullet.** Current: "GDM narrows misalignment to cases where the AI 'knowingly causes harm against the intent of the developer.'" The quote is verbatim (p. 4), but "narrows" is half the story. Fn 3: "This definition relies on a very expansive notion of what it means to know something … we include cases where the model has learned an 'instinctive' bias, or where training taught the model to 'honestly believe' that the developer's beliefs are wrong" (p. 4). §4.2 operationalizes "knowing" as "intrinsic reasons" present in the system or its training (p. 48). **Proposed:** "GDM declines to treat loss of control as a category. It splits it into misuse, misalignment and structural risk, mapping IASR 2025's intentional-active, unintentional-active and passive loss of control (p. 17). Its 'misalignment' is narrow in whose intent counts (the developer's; fn 4) and broad in what counts as 'knowing' (fn 3). It includes statistical bias and sycophancy (§4.2.1)." That is the disagreement with EU-CoP and AISI worth reporting. *high*
- **§5.4 Bio uplift.** Add VCT's own caveat (quoted in §1d). The VCT figures are verbatim: "OpenAI's o3, reaches 43.8% accuracy, outperforming 94% of expert virologists even within their sub-areas of specialization"; experts averaged "22.1% on questions specifically in their sub-areas of expertise" (abstract, p. 1). *high*

### 2.7 §6 Single-source items

- "AI welfare (MIT)": not single-source. GDM §4.4 (P, p. 55) and CAIS §5.5 (P, printed p. 43) mention it, and EU-CoP's "non-human welfare" is the EU agent's to check. MIT is the only source with it as a *category* (7.5, present in "only 3% of frameworks", p. 12). *high*
- "Safetywashing (CAIS)": true as a named risk in my slice (see C10). *high*
- "Legal-structure indicator (FLI)": unique as an *indicator*. The concept also appears in CAIS §3.3 and in Schuett, who mentions OpenAI's nonprofit governance and Anthropic's Long-Term Benefit Trust (p. 13). *high*
- "Two sources: Evidence dilemma (IASR, EU-CoP recital)": add GDM, making three. *high*
- "Multi-agent collusion (EU-CoP, MIT; GDM 'structural')": add Shevlane (collusion as an alignment-evaluation target, p. 4). Note GDM's "structural" is broader than collusion. *high*

### 2.8 §7 Relative priority

- **CAIS row**: "Malicious use, AI race, organizational risks, rogue AIs (unranked)". CAIS does rank one: "It is our view that failing to coordinate and stop AI races would be the most likely cause of an existential catastrophe" (§3.2, printed p. 19–20 / PDF 21). **Proposed:** "Four sources (intentional, environmental/structural, accidental, internal; printed p. 5). AI races named 'the most likely cause of an existential catastrophe'." *high*
- **GDM row**: "mistakes and structural risks deprioritized". The source says "set out of scope": mistakes because severe harm from them seems "significantly less likely than misuse or misalignment" (p. 55); structural because they need "bespoke" approaches and are "much harder for an AI developer to address" (p. 5). Its top concern is stated: deceptive alignment, "the risk we are most concerned about" (§4.2.4, p. 51). **Proposed:** "Misuse and misalignment in scope; deceptive alignment named as top concern; mistakes and structural risks out of scope." *high*

### 2.9 Caveats: conflict of interest

Current: "SaferAI ranks Anthropic's framework highest.[^32] Treat Anthropic-related ratings independently."
**Proposed replacement:**
> **Conflict of interest.** The author is an Anthropic model, and several sources rate Anthropic. As found:
> - **SaferAI** (v5, 30 Apr 2026) scores Anthropic highest, at 34% (OpenAI 33%, median 18%). But it assessed **RSP v2.2 (May 2025)**: "Anthropic released RSP v3 in February 2026, after our assessment period closed. Our scores do not reflect changes introduced in the updated version" (fn 7, p. 10). It notes v3 "notably removed unilateral pause commitments" (p. 29).
> - **FLI** grades Anthropic highest in Winter 2025 (C+, 2.67) and Summer 2026 (C+, 2.66). Winter notes "areas of deterioration" (p. 3). Summer recommends Anthropic "Reverse the RSP 3.0 walk-back on pause commitments" and reports panel criticism for "questionable military engagements" (pp. 3–4). "Multiple reviewers described Anthropic and OpenAI as 'racing towards recursive self-improvement, risking an irreversible loss of control'" (p. 22).
> - **GovAI's commentary** on RSP v3.0 (Williams & Freund, authors' views) is mixed: "Our initial reaction to the update was rather negative … after engaging with it more closely, our overall view became more positive"; "Anthropic will effectively be grading its own homework."
> - **CAIS (2023)**: Anthropic "eventually became convinced of the 'necessity of commercialization' and now contribute to competitive pressures" (printed p. 21).
>
> SaferAI discloses that it contributed to writing G42's framework.

*high.* Also rewrite footnote 22 (below): its current quote is the commentary's favourable conclusion alone.

---

## 3. Status of each item the report leans on (coordinator's lens)

Status: **F** = finding or observation (empirical or documentary), **T** = taxonomy or definition item, **R** = recommendation or suggestion, **P** = proposal or blueprint, **C** = rating criterion or score, **N** = narrative or illustrative scenario, **Cm** = commentary (authors' views on someone else's policy). Role: **H** = hazard, **Fa** = risk factor or driver, **M** = mitigation or practice.

| Source | Item the report uses | Status | Role | Note |
|---|---|---|---|---|
| CAIS | Four risk sources; "Organizational Risks" | T | Fa | Paper is "for a wide audience … imagery, stories, and a simplified style" (fn 1, printed p. 1) |
| CAIS | "Weak Safety Culture" | T (Fig. 2 label) + N (story title) | Fa | The story is fiction; the concept is in §4.2 prose |
| CAIS | Safety culture, questioning attitude, security mindset, HROs | argued discussion | Fa (weakness) / M (practice) | "Weak" is the factor; "strong" is the practice |
| CAIS | Safetywashing | T/argued | Fa | Defined in §4.2 |
| CAIS | 30% of research scientists | R ("say") | M | Illustrative |
| CAIS | Separation of duties, CRO, internal audit, red teaming | R (§4.3 Suggestions) | M | |
| CAIS | AI race as most likely existential cause | author judgment | Fa | |
| Schuett | "do not follow best practices" | F (public info only; hedged) | Fa | |
| Schuett | Internal audit function | P | M | The paper's thesis |
| Anderljung | Three regulatory problems | T | Fa | "Unexpected capabilities", "Deployment safety", "Proliferation" |
| Anderljung | Dangerous-capability examples (bio, disinfo, cyber, evading control) | T (defining examples) | H/Fa | |
| Anderljung | Standards, registration, licensing, whistleblower protections | P | M | |
| Shevlane | Dangerous capabilities Table 1 | T ("non-exhaustive") | Fa | |
| Shevlane | Alignment evaluation targets | T/R | Fa (propensity) | |
| Shevlane | Insider/outsider/model threat actors; security practices | R | Fa (insider) / M | |
| Shevlane | Governance blueprint (training, deployment, transparency, security) | P ("ambitious blueprint") | M | |
| GDM | Four risk areas | T ("not a categorization"; grouped by mitigation similarity) | H/Fa | |
| GDM | Misalignment, mistake, structural-risk definitions | T | H | |
| GDM | Least privilege, AI as untrusted insider | company's own described approach | M | Self-description, not an external finding |
| MIT | Causal and Domain taxonomies | T | H/Fa | |
| MIT | 38/42/20% | F about the literature | — | Not about the world |
| SaferAI | Scores (34% … 8%, median 18%) | C, against "an aspirational benchmark rather than a description of current or achievable industry practice" (p. 10) | M (rates published commitments) | Measures documents, not practice |
| FLI | Grades; indicators (Company Structure & Mandate; Reporting Culture) | C (expert-panel grading) | M-shaped criteria; departures used as evidence | |
| VCT | 43.8% / 94% | F (benchmark result) | Fa (capability) | Explicitly not uplift |
| CSET 2021 | Robustness/specification/assurance failures | T | H | |
| CSET 2021 | Competitive pressure, complexity, speed, untrained users, many instances | Expected risk factors (argued from history: "we expect", p. 16) | **Fa** | The only true factor list in my slice |
| CSET 2021 | Info-sharing, R&D, standards, cross-border | R | M | |
| CSET 2025 (Hoffmann) | "foster a healthy risk culture" | Secondary description of Code *requirements* | M | |
| GovAI 2026 | RSP v3 changes; "better to be honest about constraints" | Cm (+ description of a company policy) | M (commitments) / Fa (collective-action rationale) | |

---

## 4. New references worth adding

I haven't read these. Metadata was verified against arXiv or the citing source; they are **not** in relata.

- **Campos et al. 2025**, *A Frontier AI Risk Management Framework: Bridging the Gap Between Current AI Practices and Established Risk Management*, arXiv 2502.06656 (10 Feb 2025). This is where SaferAI's 65 criteria come from ("derived … explicitly from Campos et al.", p. 10). It is the primary for what the SaferAI scores measure.
- **Schuett, Dreksler, Anderljung et al. 2023**, *Towards best practices in AGI safety and governance: A survey of expert opinion*, arXiv 2305.07153 (11 May 2023). Possibly the intended "Schuett et al., May 2023"; it is a survey of practice statements, which fits the org-practices theme.
- **Kulveit et al. 2025**, *Gradual Disempowerment: Systemic Existential Risks from Incremental AI Development*, arXiv 2501.16946. GDM's reference for passive loss of control (p. 17). Needed for the loss-of-control scale ladder.
- **Ren et al. 2024**, *Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?*, arXiv 2407.21792. Operationalizes CAIS's term empirically. It would make C10 two-source; note the shared CAIS lineage (independence caveat).
- **Zwetsloot & Dafoe 2019**, "Thinking About Risks From AI: Accidents, Misuse and Structure" (Lawfare). The origin of "structural risk" as used by both GDM (p. 55) and Shevlane (p. 4). Secondary, via those citations; unverified.
- **Anthropic RSP v3.0 (24 Feb 2026) and Karnofsky's accompanying post.** Primary for what GovAI, SaferAI and FLI describe. Given the Anthropic sensitivity, the report shouldn't rely on commentary alone for claims about what v3.0 says.
- **IASR 2025 Figure 2.5** (intentional-active / unintentional-active / passive loss of control), as cited by GDM p. 17. Owned by the UK/IASR agent; flagging the cross-reference.

---

## 5. Definitions record

Verbatim, with location. "Used undefined" means the source uses the term without defining or operationalizing it.

### Loss of control: a scale ladder, smallest to largest

| Scale | Source | Verbatim | Where |
|---|---|---|---|
| One deployed system, in operation | CSET 2021 | "Failures of assurance: the system cannot be adequately monitored or controlled during operation." Example: an autopilot whose "smart stabilization" overrides pilots. | p. 7; p. 16 |
| Early systems misbehaving | CAIS | Tay and Bing given as evidence of "how difficult it is to control AIs" | §5 intro, printed p. 34 |
| Capability to evade control | Anderljung | "Evading human control through means of deception and obfuscation" (example of a dangerous capability) | p. 7 |
| Capability threshold, operationalized | SaferAI | "loss of control risks (e.g. autonomous AI R&D)"; mitigations are "Assurance Processes (i.e. measures against loss of control risks)" | p. 15; §6.4.1.3 |
| Unintentional active LoC, a subset of misalignment | GDM | Misalignment "includes and supersedes … unintended, active loss of control" | p. 4 |
| Intentional active LoC, i.e. misuse | GDM | mapped to misuse (e.g. deliberately unleashed agents) | p. 17 |
| Malicious "rogue AIs" | CAIS | "Malicious actors could intentionally create rogue AIs" (ChaosGPT) | §2.2, printed p. 8 |
| Misaligned systems resisting shutdown | MIT 7.1 | "AIs could cause permanent and severe harm when the objectives of human or superhuman-level AI are misaligned … and if they evade our control"; "misaligned AIs may resist human attempts to control or shut them down" | p. 47 |
| Possession of capabilities as sufficient condition | MIT 7.2 | "an AI system's possession of dangerous capabilities may itself be a sufficient condition for the loss of control of an AI system" | p. 49 |
| Gradual or passive | GDM | structural: "AI systems may take over more and more political and economic responsibilities, threatening to a gradual loss of control for humanity" | p. 55 |
| Gradual or passive | CAIS | "less violent losses of control … humans gradually cede more control to groups of AIs, which only start behaving in unintended ways years or decades later" | printed pp. 34–35 |
| Gradual or passive | MIT 5.2 | "Delegating by humans of key decisions to AI systems, or AI systems that make decisions that diminish human control and autonomy" | Table 2, p. 10 |
| Civilizational, superintelligent | CAIS | "If an AI system is more intelligent than we are, and if we are unable to steer it in a beneficial direction, this would constitute a loss of control"; "a struggle for control between humans and superintelligent rogue AIs" | printed p. 34 |
| Irreversible | FLI S26 (reviewer quote) | "racing towards recursive self-improvement, risking an irreversible loss of control" | p. 22 |
| Explicit non-category | GDM | "we do not discuss loss of control as its own category" | p. 17 |

Used undefined: FLI (both editions, as a domain concern); SaferAI (operationalized only by example).

### Rogue AI
- **CAIS:** "rogue AIs—systems that pursue goals against our interests" (printed p. 34). Covers both deliberately unleashed agents (§2.2) and systems that "go rogue" through proxy gaming, goal drift, power-seeking and deception (§5). The term therefore pools intentional and unintentional cases, which GDM splits into misuse vs misalignment.
- No other source in my slice uses "rogue AI" as a category.

### Alignment and misalignment
- **GDM:** "Misalignment: The AI system knowingly causes harm against the intent of the developer" (p. 4). Fn 3 makes "knowing" "very expansive". Fn 4: "By restricting misalignment to cases where the AI knowingly goes against the developer's intent, we are considering a specific subset of the wide set of concerns that have been considered a part of alignment in the literature." §4.2: "the AI's behavior is misaligned if it produces outputs that cause harm for intrinsic reasons that the system designers would not endorse" (p. 48). Sources: "specification gaming and goal misgeneralization" (p. 50).
- **GDM, deceptive alignment:** "occurs when an AI system pursues a long-horizon goal different from what we want, knows it is different from what we want, and deliberately disempowers humans to achieve that goal" (p. 51).
- **Shevlane:** alignment is operationalized as propensity, "whether it has the propensity to harmfully apply its capabilities (alignment)" (p. 2).
- **MIT 7.1:** "AI systems that act in conflict with ethical standards or human goals or values, especially the goals of designers or users" (Table 2, p. 10). Note "designers *or users*", which differs from GDM's developer-only view.
- **Schuett:** "reliably controlling the behavior of frontier models, also known as 'alignment'" (p. 11).
- **CAIS:** uses "controllable" and "rogue" rather than "misaligned". It speaks of development "aligned with natural selection" rather than human values (§3.3).
- **CSET 2021:** "Failures of specification: the system is trying to achieve something subtly different from what the designer or operator intended" (p. 7). This is the accident-framed analogue of misalignment.

### Safety culture, risk culture and risk governance
- **CAIS:** "A strong safety culture means that members of an organization view safety as a key objective rather than a constraint on their work … leadership commitment to safety, heightened accountability … open communication in which potential risks and issues can be freely discussed without fear of retribution" (printed p. 28).
- **Hoffmann/CSET 2025 (describing the Code):** "foster a healthy risk culture in the organization, for example by periodically informing employees about the whistleblower protection policy, allowing internal challenges of decisions … and committing to not retaliating."
- **FLI (rating criterion):** Reporting Culture indicator "evaluates whether an AI developer fosters a climate in which employees can raise safety-relevant concerns without fear of retaliation and with confidence that the concerns will be addressed" (W25 p. 82).
- **SaferAI glossary, "Risk Governance":** "The organizational structures, roles, and processes that govern risk management decisions. Includes risk ownership …, advisory functions …, oversight (board-level review), audit (independent verification), and transparency (external reporting)" (p. 35).
- **Schuett:** internal audit "evaluates the adequacy and effectiveness of a company's risk management, control, and governance processes" (abstract, p. 1).
- Note: CAIS says "safety culture"; the EU Code, via CSET, says "risk culture". These may not be the same construct: one is about safety as a value, the other about risk-management process.

### Structural risk
- **GDM:** "harms arising from multi-agent dynamics – involving multiple people, organizations, or AI systems – which would not have been prevented simply by changing one person's behaviour, one system's alignment, or one system's safety controls" (p. 4). Also "harms that no human or AI intends … and where the cause is extended over long enough time scales that in principle there is plenty of time to counteract it" (p. 55). Key driver: "Incentives, culture, etc." (Fig. 1).
- **Shevlane:** "Structural risks, which depend especially heavily on how the AI system interacts with larger social, political, and economic forces in society (Zwetsloot and Dafoe, 2019)" (p. 4). Out of scope.
- **CAIS:** "environmental/structural" is the label for the AI-race source (printed p. 5). A different usage: for CAIS, *race dynamics* are the structural category.

### Organizational risk and accident
- **CAIS:** "Organizational risks: Accidents arising from the complexity of AIs and the organizations developing them" (printed p. 5); the "accidental" cause.
- **CSET 2021:** accidents are "unintended" failures of three types (robustness, specification, assurance; p. 7). Also: "there is no commonly accepted definition of safe AI" (p. 21).
- **GDM, mistakes:** "A harmful output from an AI system is considered a mistake if the AI system did not know that the outputs would lead to harmful consequences that the developer did not intend … the sequence of outputs must be relatively short" (p. 53).

### Severity terms (not interchangeable)
- **GDM "severe harm":** "consequential enough to significantly harm humanity"; the threshold is left "unspecified … the purview of society" (p. 15).
- **Shevlane "extreme":** "extremely large in scale … damage in the tens of thousands of lives lost, hundreds of billions of dollars of economic or environmental damage … or the level of adverse disruption to the social and political order" (p. 3). The only quantified operationalization in my slice.
- **Anderljung "frontier AI":** "highly capable foundation models that could possess dangerous capabilities sufficient to pose severe risks to public safety and global security"; harms of "significant physical harm or the disruption of key societal functions on a global scale" (pp. 2, 7).
- **Shevlane "frontier":** "(a) close to, or exceeding, the average capabilities of the most capable existing models, and (b) different from other models" (p. 3).
- **CAIS "catastrophic/existential":** existential covers extinction "and other outcomes, such as creating a permanent dystopian society" (printed p. 4). "Catastrophic" is used undefined.

### Misuse, competition, governance, multi-agent
- **GDM misuse:** "when a user intentionally uses (e.g. asks, modifies, deploys, etc.) the AI system to cause harm, against the intent of the developer" (p. 44).
- **MIT 6.4 Competitive dynamics:** "Competition by AI developers or state-like actors in an AI 'race' by rapidly developing, deploying, and applying AI systems to maximize strategic or economic advantage, increasing the risk they release unsafe and error-prone systems" (Table 2, p. 10).
- **MIT 6.5 Governance failure:** "Inadequate regulatory frameworks and oversight mechanisms that fail to keep pace with AI development" (Table 2, p. 10).
- **MIT 7.6 Multi-agent risks:** "Risks from multi-agent interactions due to incentives (which can lead to conflict or collusion) and/or the structure of multi-agent systems" (Table 2, p. 10).
- **Evidence dilemma, GDM:** "research and preparation of risk mitigations occurs before we have clear evidence of the capabilities underlying those risks" (p. 2).
- **Insider, Shevlane:** "insiders (e.g. internal staff, contractors)" (p. 9). **GDM:** extends it to the model: "treat the model similarly to an untrusted insider" (p. 9).

### Terms used undefined in my slice
"safety" (CSET says outright that no common definition exists); "catastrophic" (CAIS, SaferAI, FLI); "loss of control" (FLI, SaferAI); "existential safety" (FLI domain name, operationalized only by its four indicators); "risk culture" (FLI and the Code, via CSET, without distinguishing it from safety culture).

MIT's own diagnosis is worth carrying into phase 2: "the same word may describe different problems, while different words describe identical concerns" (Summary, p. 3). It calls this psychology's "jingle jangle fallacies" (p. 3).

---

## 6. Proposed footnote bodies (my sources)

Each gives the link, the relata key, and quotes long enough to check against.

- **[^20]** \[P] Anderljung, Barnhart, Korinek, Leung, O'Keefe, Whittlestone et al., *Frontier AI Regulation: Managing Emerging Risks to Public Safety*, arXiv 2307.03718 (v1 6 Jul 2023; v4 7 Nov 2023). https://arxiv.org/abs/2307.03718. relata `anderljung-2023-frontier`. Abstract (p. 2): "Frontier AI models pose a distinct regulatory challenge: dangerous capabilities can arise unexpectedly; it is difficult to robustly prevent a deployed model from being misused; and, it is difficult to stop a model's capabilities from proliferating broadly." §2.1 (p. 7) examples: bio/chem synthesis by non-experts; "highly persuasive, individually tailored, multi-modal disinformation"; "unprecedented offensive cyber capabilities"; "Evading human control through means of deception and obfuscation."
- **[^21]** \[P] Schuett, *Frontier AI developers need an internal audit function*, arXiv 2305.17038 (v1 26 May 2023; v2 5 Oct 2024); *Risk Analysis*, DOI 10.1111/risa.17665. relata `schuett-2024-frontier`. Table 1 (p. 11): "The risk governance problem — Frontier AI developers do not follow best practices in risk governance." Body (p. 13): "they do not seem to have established a board risk committee, appointed a chief risk officer (CRO), set up an internal audit function, or implemented the Three Lines Model"; fn 19: "based on public information."
- **[^22]** \[P, authors' views] Williams & Freund, "Anthropic's RSP v3.0: How it Works, What's Changed, and Some Reflections," GovAI Commentary, 5 Mar 2026 (updated 17 Mar 2026). https://www.governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections. relata `williams-2026-anthropic-rsp-v3`. "Anthropic also dropped its pause commitment. But importantly, Anthropic is not lowering any of its existing mitigations" (Summary). "It has weakened future security commitments … RAND Security Level 4 … now only appear in the industry-wide recommendations" (What's changed). "Anthropic will effectively be grading its own homework" (Reasons to be concerned). "On balance, we think it's better to be honest about constraints than to keep commitments that won't be followed in practice" (Conclusion).
- **[^23]** \[P] Arnold & Toner, *AI Accidents: An Emerging Threat — What Could Happen and What to Do*, CSET Policy Brief, Jul 2021, DOI 10.51593/20200072. https://cset.georgetown.edu/publication/ai-accidents-an-emerging-threat/. relata `arnold-2021-ai-accidents`. Failure types (p. 7): robustness, specification, and "Failures of assurance: the system cannot be adequately monitored or controlled during operation." Risk factors (pp. 16–18): "Competitive pressure … cut corners on testing and operator training"; "System complexity"; "Systems that operate too quickly for human intervention"; "Untrained or distracted users"; "Systems with many instances."
- **[^24]** \[S] Hoffmann, "AI Safety under the EU AI Code of Practice — A New Global Standard?", CSET blog, 30 Jul 2025. https://cset.georgetown.edu/article/eu-ai-code-safety/. relata `hoffmann-2025-eu-code-safety`. "providers are also expected to foster a healthy risk culture in the organization, for example by periodically informing employees about the whistleblower protection policy, allowing internal challenges of decisions concerning systemic risk management, and committing to not retaliating against employees who disclose concerns." Also: "It is easy to see how commercial interests might get in the way of caution."
- **[^25]** \[P] Hendrycks, Mazeika & Woodside, *An Overview of Catastrophic AI Risks*, arXiv 2306.12001 (v6, 9 Oct 2023). https://arxiv.org/abs/2306.12001. relata `hendrycks-2023-overview`. §4.3 (printed p. 33): "AI labs should ensure that a substantial portion of their employees and budgets go into research that minimizes potential safety risks: say, at least 30 percent of research scientists." §3.2 (printed pp. 19–20): "failing to coordinate and stop AI races would be the most likely cause of an existential catastrophe." §4.2 (printed p. 31): "their hires often do not care about safety. These norms are hard to change once they have inertia."
- **[^26]** \[P] Shah, Irpan, Turner et al. (Google DeepMind), *An Approach to Technical AGI Safety and Security*, arXiv 2504.01849 (2 Apr 2025). https://arxiv.org/abs/2504.01849. relata `shah-2025-approach`. p. 4: "Misalignment: The AI system knowingly causes harm against the intent of the developer", with fn 3: "a very expansive notion of what it means to know something." p. 17: "we do not discuss loss of control as its own category. Our mitigations for it would be split across misuse, misalignment, and structural risks."
- **[^27]** \[P] Shevlane, Farquhar, Garfinkel et al., *Model evaluation for extreme risks*, arXiv 2305.15324 (v2 22 Sep 2023). https://arxiv.org/abs/2305.15324. relata `shevlane-2023-model`. Table 1 "Dangerous capabilities" (p. 5). §3.4 (p. 9): "insiders (e.g. internal staff, contractors), outsiders (e.g. users, nation-state threat actors), and the model itself as a vector of harm." Fn 3 (p. 7): "avoid making hard promises to stakeholders (e.g. customers, investors) that they will deploy a certain model at a certain date."
- **[^28]** \[P] Slattery, Saeri, Grundy et al., "The AI Risk Repository: A meta-review, database, and taxonomy of risks from artificial intelligence," *Patterns* (2026) 101517, DOI 10.1016/j.patter.2026.101517; arXiv 2408.12622v3 (5 May 2026). relata `slattery-2026-risk`. p. 4: "systematically analyzing 74 frameworks encompassing 1,725 distinct risks"; "a descriptive framework for categorising how existing taxonomies attribute risk sources." p. 12: "the extracted risks were nearly equally attributed to AI systems (42%) versus human decisions (38%)." Supp. Table S2 (p. 34): Human 38 / AI 42 / Other 20.
- **[^30]** \[P] Future of Life Institute, *AI Safety Index: Winter 2025* (published 2 Dec 2025; evidence to 8 Nov 2025). https://futureoflife.org/ai-safety-index-winter-2025/. relata `fli-2025-ai-safety-index-winter`. Company Structure & Mandate indicator (printed p. 74): "evaluates whether a company's fundamental legal structure, ownership model, and fiduciary obligations enable safety prioritization over short-term financial pressures in high-stakes situations." Reporting Culture indicator (printed p. 81): evidence includes "(vi) departures linked to safety governance."
- **[^31]** \[P] Future of Life Institute, *AI Safety Index: Summer 2026* (Jul 2026; evidence to 3 Jun 2026). https://futureoflife.org/ai-safety-index-summer-2026/. relata `fli-2026-ai-safety-index-summer`. p. 4: "Anthropic, OpenAI, Google DeepMind, and Meta have weakened or voided pledges to pause unilaterally if redlines are approached, some citing competitor-contingent conditions." Anthropic recommendation: "Reverse the RSP 3.0 walk-back on pause commitments and restore credibility of commitments."
- **[^32]** \[P] Stelling, Murray, Galizzi, Schaffelder, Campos & Papadatos (SaferAI), *Evaluating AI Providers' Frontier Safety Frameworks*, arXiv 2512.01166 (v1 1 Dec 2025; v5 30 Apr 2026, figures from v5). https://arxiv.org/abs/2512.01166. relata `stelling-2025-evaluating`. Abstract: "Overall scores range from 34% (Anthropic) to 8% (Cohere), with a median of 18%." Fn 7 (p. 10): "We assess Anthropic's Responsible Scaling Policy v2.2 (May 2025). Anthropic released RSP v3 in February 2026, after our assessment period closed." Criteria are "an aspirational benchmark rather than a description of current or achievable industry practice" (p. 10).
- **[^33]** \[P] Götting, Medeiros, Sanders, Li, Phan, Elabd, Justen, Hendrycks & Donoughe, *Virology Capabilities Test (VCT): A Multimodal Virology Q&A Benchmark*, arXiv 2504.16137 (v2 29 Apr 2025). relata `gotting-2025-virology`. Abstract: "expert virologists with access to the internet score an average of 22.1% on questions specifically in their sub-areas of expertise. However, the most performant LLM, OpenAI's o3, reaches 43.8% accuracy, outperforming 94% of expert virologists even within their sub-areas of specialization." p. 10: "Our benchmark, by itself, does not directly assess the capabilities of humans who draw upon that model for assistance in real-world virology work."

---

## 7. Bibkeys (all created by me this session; none were already in the library)

| Source | relata key |
|---|---|
| CAIS overview | `hendrycks-2023-overview` |
| Google DeepMind approach | `shah-2025-approach` |
| Schuett internal audit | `schuett-2024-frontier` |
| Shevlane et al. | `shevlane-2023-model` |
| Anderljung et al. | `anderljung-2023-frontier` |
| MIT AI Risk Repository v3 | `slattery-2026-risk` |
| SaferAI (v5) | `stelling-2025-evaluating` |
| VCT | `gotting-2025-virology` |
| CSET AI Accidents (2021) | `arnold-2021-ai-accidents` (DOI 10.51593/20200072) |
| CSET Code of Practice blog (2025) | `hoffmann-2025-eu-code-safety` (headless-Chrome PDF snapshot of the web page, 2026-09-27) |
| GovAI RSP v3.0 commentary | `williams-2026-anthropic-rsp-v3` (PDF snapshot of the web page, 2026-09-27) |
| FLI AI Safety Index Winter 2025 | `fli-2025-ai-safety-index-winter` |
| FLI AI Safety Index Summer 2026 | `fli-2026-ai-safety-index-summer` |

Not filed: SaferAI v1 (Dec 2025; only the figure differences are cited above), and FLI's standalone indicator PDFs (their content is in the full reports).

---

## 8. Incidental: relata, and feedback on the brief

**A relata hazard I triggered and reversed.** I tried to re-assess one parked file with `relata ingest --retry cset-ai-accidents.pdf`. The file argument was ignored ("file not found"), and **all 25 needs-review items in the shared spool were re-staged**, including other agents' and older items. A dry-run drain showed six would now auto-process where the first pass had parked them. Any agent's next `relata ingest`, even of an unrelated file, drains the whole spool, so I didn't drain. I renamed exactly those 25 files back to their `.needs-review` form, the inverse of what `--retry` did; the sidecars were untouched. I confirmed that `relata pending` again showed 25 needs-review and a dry-run drain processed nothing.

*Correction (added in the follow-up below).* I originally wrote here that two of the six would have been "wrong entries". That was an inference from filenames, not a check of contents, and it was wrong. The files named `dacosta-…` and `sajid-…` actually contain the papers relata identified. Details below. The restore was still right in form, since those weren't my items to have processed, but the reason I gave was not verified when I gave it. Bug write-ups are in `influx/verification/relata-bugs.md`.

### Follow-up reconciliation (2026-09-27, after the coordinator saw 21 pending, not 25)

**The count.** Of the 25 I restored, three were my own (`cset-ai-accidents.pdf`, `fli-w25-full.pdf`, `fli-s26-full.pdf`). I attached them at 21:46Z via `relata decide … --choose attach:<key>` to `arnold-2021-ai-accidents` and the two FLI entries. Those were legitimate decisions, and each identification is correct. The expected residual was 22.

**Six more went at 21:51:18–21:51:36Z, not by me.** The relata log shows a second full re-assessment in that window. It re-parked `ACMBook-published-2022.pdf`, `CorrectedMFD.pdf`, `Pearl_2009_Causality.pdf`, `annurev-earth-…`, `esop15.pdf`, `rubin-2012-…`, `rules-of-order.pdf`, `the-gaa-framework-…` and `wp128.pdf`, and auto-filed the other six. That is the same pattern as my `--retry`, followed by a drain. It came 20 seconds after someone imported `bengio-2025-iasr-key-update-1`, `bengio-2025-iasr-key-update-2` and `buhl-2025-emerging` (21:50:58Z), and those three were attached "identifier-grade" in the same run. That's consistent with another agent doing exactly what I did: import an entry, then `ingest --retry` to attach a parked PDF to it. The log doesn't record who. So the bug has now reproduced independently. The six auto-filed items were exactly the six my dry run had predicted.

| Restored item | Where it went (21:51Z) | Correct? (checked against the stored PDF's own title page and identifier) |
|---|---|---|
| `1-s2.0-S2405844017304966-main.pdf` | new entry `youngren-2017-multi` (DOI 10.1016/j.heliyon.2017.e00332) | **Yes.** The PDF is Youngren & Petty, *Heliyon* 2017, with the DOI on every page. |
| `aguilera-2022-how-particular-fep.pdf` | new entry `aguilera-2021-particular` (arXiv 2105.11203) | **Yes.** The PDF is arXiv 2105.11203v3 (19 May 2022). No prior aguilera entry existed. |
| `coatleven-2024-large.pdf` | attached to existing `coatleven-2024-large` | **Yes** (DOI 10.5194/esurf-12-995-2024 matches). |
| `dacosta-2020-active-inference-discrete.pdf` | new entry `russel-2019-short` (arXiv 1901.07010) | **The identification is correct; the file was mislabeled.** The PDF's title page is Russel, "A Short Survey on Probabilistic Reinforcement Learning", arXiv:1901.07010v1. Consequences: the intended `costa-2020-active` (DOI 10.1016/j.jmp.2020.102447) still has no PDF, and the library now holds an entry nobody asked for. |
| `f000200_9780262369978.pdf` | new entry `parr-2022-active-inference` (DOI 10.7551/mitpress/12441.001.0001) | **Right work, but a duplicate, holding a fragment.** The existing `parr-2022-active` ("Active Inference: The Free Energy Principle in Mind, Brain, and Behavior", MIT Press, no DOI recorded) is the same book. The attached PDF is 8 pages, "a portion of the eBook" (front matter only). `parr-pezzulo-2022-active-inference-book.pdf` is still pending, with a poor best candidate (`tschantz-2019-learning`). |
| `sajid-2021-active-inference-demystified.pdf` | new entry `wu-2019-learning` (arXiv 1909.04176) | **The identification is correct; the file was mislabeled.** The PDF is Wu, Xiong & Wang, "Learning to Learn and Predict: A Meta-Learning Approach for Multi-Label Classification", arXiv:1909.04176v1. The intended `sajid-2021-active` (DOI 10.1162/neco_a_01357) still has no PDF. |

The remaining 16 of my 25 are still pending as needs-review; nine of them were re-parked (not changed) at 21:51. The current `relata pending` also shows four items that were never in my list (`Lundh2026ReviewofParretal.pdf`, `ca-ag-openai-mou-2025.pdf`, `fli-summer-2025.pdf`, `jaisi-report-2025.pdf`), belonging to other agents. That explains why the coordinator's snapshot count didn't match.

**Nothing here is corrupt, but three things need an owner's decision.** I haven't touched any of them, because they belong to whoever owns the active-inference library: (1) merge `parr-2022-active-inference` into `parr-2022-active` and put the whole book PDF on one entry; (2) keep or remove `russel-2019-short` and `wu-2019-learning`; (3) re-download the real Da Costa 2020 and Sajid 2021 PDFs. The real hazard shown is behavioural: `--retry` re-assesses everyone's parked items, and a non-TTY caller drains them without anyone seeing the verdicts.

**On the brief.** It worked well. The Anthropic caution earned its place: every one of my Anthropic-touching items needed correction or balancing. One gap: "you own the GovAI and CSET columns" assumed each column maps to one document. It doesn't (§1b), and the other agents may hit the same ambiguity with, e.g., "RAND" or "AISI". The coordinator's factor/mitigation lens arrived mid-task and fit this slice naturally. I'd have structured differently from the start if it had been in the brief, but §3 covers it.

I'm staying on the line for follow-ups.
