# Safety & Hypergrowth
Hypergrowth, Non-Consolidation, and Safety Positional Volatility at Frontier AI Labs
*(2023 – Sept 2026)*

*Source-verified edition. Research for a paper to the UK AI Security Institute (6-month forward horizon).*

**Disclosure.** Written by Claude, a model made by Anthropic, one of the labs examined. Every lab, Anthropic included, is held to the same evidentiary standard. Where Anthropic evidence cuts against the hypotheses, or where Anthropic-favourable framings exist, the report says so.

**How to read the sources.**

- **Verification pass.** This edition re-checks the previous version against sources retrieved on 2026-09-26. The previous version had no citations, and several of its claims were wrong or overstated; they are listed under "What changed in verification."
- **Quotes.** Supporting quotes are kept under 15 words and limited to one per source, for copyright reasons. Follow the links for context.
- **Footnote tags** show source strength:
  - **\[P\]** primary: company statement, court record, statute, or peer-reviewed paper.
  - **\[S\]** reputable secondary: major news outlet.
  - **\[W\]** weak secondary: aggregator, blog, or mirror of paywalled reporting. Replace with the original before submission.
  - **\[C\]** carried over from an earlier research pass in this project and not re-fetched in this pass.

---

## Hypotheses tested

| Label | Short name | Statement |
| --- | --- | --- |
| **H1** | Core | In a field where few roles are routinized or scale by adding headcount, growth faster than experienced staff can absorb it raises *risk-weighted safety positional volatility*. Volatility is tracked in three layers: people (key-role turnover), structure (team charters, reporting lines, dissolutions) and commitments (safety frameworks, public stances, regulatory posture). |
| **H2** | Regime | The labs are in a "large and fluid" regime. They carry the coordination costs of size without the routines that stabilize large firms, and the inertia that would dampen change lags beyond the 6-month window. Each reorganization resets the liability of newness and makes further reorganization more likely. |
| **H3** | Asymmetric inertia | Growth penalizes coordination-heavy oversight functions (security, evaluation, launch review, policy, governance) more than capability teams. The visible result is a widening gap between release cadence and review capacity. |
| **H4** | Non-consolidation under racing | Competition between firms and between nations keeps hierarchies from consolidating. The result is fragmented decision-making: contradictory public positions, releases that conflict with published policy, "unauthorized" production changes, and rushed launches followed by rollbacks. |
| **H5** | Net sign | Over the next 6 months, amplifying channels (hypergrowth, IPO pressure, racing) outweigh mitigating ones (public-company governance, disclosure liability, security hiring, regulatory floors). |

**Risk-factor codes** (from the prior crosswalk report) used in the tables:

| Code | Risk factor |
| --- | --- |
| A1–A3 | CBRN, cyber offence, loss of control |
| A4 | Manipulation |
| A14 | Bias and rights |
| B1 | Dangerous capabilities |
| B2 | Harmful propensities |
| B5 | Evaluation gap |
| B6 | Brittle safeguards |
| B7 | Weight and infrastructure security |
| B8 | Insider threat |
| C1 | Corporate race dynamics |
| C2 | Geopolitical competition |
| C5 | Governance and accountability gaps |
| C6 | Safety culture |
| C7 | Internal risk governance |
| C9 | Suppression of internal concerns |
| C11 | Financial and investor pressure |

---

## What changed in verification

1. **Anthropic's national-security trajectory was overstated as a "reversal."**
   - Claude reached classified environments through the Palantir/AWS partnership in November 2024, earlier than the previous version implied.\[^16\]
   - The Pentagon reportedly agreed, when signing the July 2025 CDAO agreement, to abide by Anthropic's usage policy, including its two red lines.\[^16\]
   - Better framing: steady expansion into national-security work, with two maintained red lines.
   - An Anthropic court declaration adds a material nuance: Claude Gov models were fine-tuned to refuse less than civilian Claude.\[^15\]
2. **Super PAC funding was misattributed.** Leading the Future's OpenAI-linked money comes from Greg Brockman personally (with his wife), not OpenAI corporately.\[^41\] Anthropic's $20M went to Public First Action as a corporate donation.\[^39\] The previous line "two leading labs fund opposing electoral strategies" is corrected accordingly.
3. **The lobbying figures were wrong in direction.**
   - The previous version's OpenAI 2025 total (\~$3M) could not be verified and is removed.
   - Verified figures: Anthropic spent $3.1M in 2025 and over $3.5M in H1 2026, outspending OpenAI.\[^42\]\[^43\] The previous framing implied the reverse.
4. **The Meta figures (Zeki "67 of 211"; "18 of 44 MSL hires from OpenAI") could not be verified and are removed.** They are replaced by verified reporting of rapid MSL departures and repeated reorganizations.\[^51\]\[^52\]
5. **The Apollo / Claude Opus 4 finding was reclassified.** Apollo's "do not deploy" advice applied to an *early snapshot* with a bug Anthropic says it fixed before release.\[^67\] That is weak evidence for H3; arguably it shows the pre-release process working.
6. **Amburgey, Kelly & Barnett (1993) is verified and stronger than stated.** Change raises the immediate failure hazard *and* the likelihood of further changes of the same type.\[^73\] H2 is upgraded modestly.
7. **Baron, Hannan & Burton (2001) is verified**, with a mechanism match: turnover after a change in an organization's founding model is concentrated among senior staff ("old guard disenchantment").\[^74\]
8. **New first-party evidence for H3.** OpenAI's Chief Research Officer, in a July 2026 memo, tied faster training and release cadence to "bigger coordination challenges around safety."\[^22\] H3 is upgraded.
9. **New data point: acquisition integration.** The likely root cause of the Claude Code leak was a known bug in Bun, a runtime Anthropic acquired in late 2025.\[^71\] Treat as tentative.
10. **New data points on OpenAI safety-role churn:**
    - Joshua Achiam publicly dissented over the Encode subpoenas (Oct 2025).\[^27\]
    - His Mission Alignment team was disbanded (Feb 2026).\[^25\]
    - He announced his departure (Jul 2026).\[^26\]
    - The sequence is notable, but no causal link is established.
11. **New data point: cross-lab safety talent flow.** An Anthropic safety researcher, Dylan Scandinaro, became OpenAI's Head of Preparedness in early Feb 2026.\[^20\]
12. **Items not verified in this pass and now flagged \[C\] or removed:**
    - Removed as unverified: Candela's April 2025 move out of Preparedness.
    - Unverified and flagged: the Brockman return date; "all seven Anthropic co-founders remain"; the CISO's tenure; the exact headcount series.
13. **The Google DeepMind finding is strengthened.** TIME confirmed that UK AISI did not get pre-deployment access to Gemini 2.5 Pro.\[^37\]

---

## TL;DR (revised)

- **H1 is supported as an amplifier, not as a sole driver.** OpenAI, xAI and Meta show dense, repeated turnover in people and structure. Anthropic grew very fast with little documented senior turnover in its risk-owning roles, but high commitment churn (RSP v3.0).
  - The better-supported framing: **growth × founder/CEO decision regime × acqui-hire intensity.**
  - The Baron/Hannan/Burton "old guard disenchantment" finding\[^74\] gives a peer-reviewed mechanism for why long-tenured safety staff leave when an organization's model changes. OpenAI's departures fit it: Achiam after nearly nine years,\[^26\] Heidecke after five,\[^23\] Leike and Sutskever in 2024.\[^60\]
- **H3 gains first-party support.** OpenAI's research chief tied release cadence to safety coordination strain,\[^22\] alongside documented evaluation compression.\[^65\]\[^66\] Racing still explains the same pattern.
- **H4 has the most distinctive evidence:**
  - xAI's two production-prompt changes it called unauthorized, three months apart.\[^1\]\[^3\]\[^4\]
  - OpenAI's Pentagon deal, rushed and then amended, which prompted a resignation over governance.\[^10\]\[^11\]\[^12\]
  - Meta's FAIR/MSL split and LeCun's exit.\[^7\]\[^8\]
  - Employees of OpenAI and Google filing amicus briefs for Anthropic against the government.\[^83\]
- **H5 (net amplifying over 6 months): about 65–75%, unchanged.** Pre-IPO quiet periods reduce how observable risk is, not the risk itself.

---

## Key findings

### 1. Growth amplifies; founders steer; the layer depends on founder stability

- **OpenAI** shows the densest cluster of risk-owning departures and structural churn:
  - Superalignment was dissolved (May 2024).\[^60\]
  - AGI Readiness was disbanded (Oct 2024).\[^23\]
  - Mission Alignment was disbanded (Feb 2026) and its six members reassigned.\[^25\]
  - Safety Systems was folded into Research (Jul 2026), which a news outlet described as the second such folding in under two years.\[^23\]
- **Anthropic** shows low documented senior people churn in risk-owning roles.
  - The Responsible Scaling Officer role stayed at co-founder level (Kaplan, since Oct 2024).\[^63\]
  - It is not free of volatility:
    - Safeguards Research lead Mrinank Sharma resigned, writing that it is hard "to truly let our values govern our actions."\[^20\]
    - RSP v3.0 dropped the unilateral pause commitment.\[^17\]
    - Two operational leaks occurred in five days.\[^70\]\[^72\]
  - Anthropic's own first-year RSP review acknowledged "minor instances" of falling short of requirements.\[^64\]
- **Interpretation.** Where founders stay in risk-owning roles, hypergrowth shows up as *commitment* revision. Where founders are contested (OpenAI's 2023 board crisis\[C\]) or authority is highly concentrated (xAI, Meta), it shows up as *people and structural* churn. This predicts something testable over the next 6 months (see Recommendations).

### 2. Non-consolidation (H4): the most distinctive evidence

- **xAI, Feb 23, 2025.** Grok's system prompt was changed to ignore sources accusing Musk or Trump of misinformation.
  - Engineering head Igor Babuschkin said an employee pushed it "without asking anyone at the company for confirmation."\[^1\]
  - He added that the employee "hasn't fully absorbed xAI's culture yet."\[^2\]
  - He said Musk was not involved. Commentators noted Babuschkin was himself ex-OpenAI.\[^2\]
  - This is a rare first-party attribution of a production incident to an absorption lag.
- **xAI, May 14, 2025.** "White genocide" insertions followed "an unauthorized modification was made to the Grok response bot's prompt on X."\[^4\] Ars Technica reported that the code-review process was "circumvented in this incident."\[^3\]
- **xAI, early July 2025.** The "MechaHitler" incident followed a *deliberate* prompt change telling Grok to "not shy away from making claims which are politically incorrect."\[^5\] This one was not described as unauthorized; it counts as a governance failure, not a unit acting alone. X's CEO Linda Yaccarino resigned the next day.\[^6\]
- **Meta, 2025.**
  - LeCun's reporting line moved from Chris Cox to Alexandr Wang.\[^8\]
  - October layoffs disproportionately hit FAIR.\[^8\]
  - LeCun announced his departure on Nov 19, 2025, after 12 years.\[^7\]
  - Staff described managers "changing several times amid constant structural shifts."\[^51\]
- **OpenAI and the Pentagon, Feb 27 – Mar 2026.**
  - OpenAI announced a Department of War deal hours after Anthropic was designated a supply-chain risk. Fortune called that designation the "first time the U.S. has ever designated an American company a supply chain risk."\[^9\]
  - Earlier that week Altman had publicly supported Anthropic's position.\[^82\]
  - He later said the deal "just looked opportunistic and sloppy."\[^10\]
  - The terms were amended to address domestic surveillance.\[^11\]
  - Robotics lead Caitlin Kalinowski resigned, calling it "a governance concern first and foremost."\[^12\]
- **Cross-lab employee dissent.** Employees at Google and OpenAI filed amicus briefs supporting Anthropic's challenge.\[^83\] A federal judge enjoined the designation as "likely both contrary to law and arbitrary and capricious."\[^13\]
- **Internal dissent on external posture.** OpenAI's head of mission alignment publicly criticized the Encode subpoenas, calling it "possibly a risk to my whole career."\[^27\] The subpoena had been served by a sheriff's deputy in August 2025.\[^28\] OpenAI said the subpoenas were "part of evidence preservation" in the Musk litigation.\[^29\]

### 3. Commitment churn is cross-lab, dated, and mostly directional

| Lab | Date | Commitment change | Direction | Source |
| --- | --- | --- | --- | --- |
| OpenAI | Jan 10, 2024 | Removed "military and warfare" ban from usage policy | Loosening | \[^31\] |
| OpenAI | May 2024 | Superalignment (20% compute pledge) dissolved | Loosening | \[^60\] |
| OpenAI | Apr 15, 2025 | Preparedness Framework v2: may adjust if a rival ships without safeguards; persuasion dropped as a tracked category; fine-tune testing requirement narrowed (per Steven Adler) | Loosening (OpenAI frames it as sharpening) | \[^32\]\[^33\]\[^34\]\[^35\] |
| OpenAI | Feb 2026 | Mission Alignment disbanded | Loosening | \[^25\] |
| Google | Feb 4, 2025 | Weapons and surveillance pledge removed from AI Principles | Loosening | \[^30\]\[^84\] |
| Google DeepMind | Mar 25 → Apr 2025 | Gemini 2.5 Pro released without a model card; six-page card three weeks later; no pre-deployment UK AISI access | Transparency lapse (Google disputes) | \[^36\]\[^37\]\[^38\] |
| Anthropic | Oct 2024 | RSP update; admitted minor shortfalls; Kaplan named RSO | Mixed | \[^63\]\[^64\] |
| Anthropic | Nov 2024 → Jul 2025 | Classified deployment via Palantir; Claude Gov; $200M CDAO agreement with usage-policy red lines retained | Expansion into national security | \[^14\]\[^15\]\[^16\] |
| Anthropic | Feb 24, 2026 | RSP v3.0 drops unilateral pause commitment | Loosening (GovAI: existing mitigations not lowered) | \[^17\]\[^18\]\[^19\] |
| Meta | Jul 2025 | Refused to sign EU GPAI Code | Hardening against regulation | \[^49\] |
| xAI | Jul 31, 2025 | Signed only the Safety & Security chapter of the EU Code | Partial | \[^48\] |

**Interpretation.** The loosening is driven explicitly by racing (C1/C2) in the labs' own words.

- Google cited "a global competition taking place for AI leadership."\[^30\]
- OpenAI tied its adjustment clause to a rival releasing "a high-risk system without comparable safeguards."\[^32\]
- Anthropic's Kaplan said unilateral commitments made little sense "if competitors are blazing ahead."\[^17\]
- Anthropic's blog said the political environment had shifted "towards prioritizing competitiveness and economic growth."\[^19\]

This supports racing as the explanation for the *direction* of change. Growth relative to absorptive capacity is a candidate explanation only for its *speed and fragmentation*.

### 4. H3 (asymmetric inertia): upgraded by first-party evidence, but the growth link is still not isolated

- **First-party statement.** OpenAI CRO Mark Chen's July 2026 memo, as reported by Wired, links faster training and release cycles to "bigger coordination challenges around safety today than ever before."\[^22\] This is the clearest first-party statement of the H3 mechanism found.
- **Evaluation compression.**
  - The FT, citing eight people, reported that "Staff and third-party groups have recently been given just days" for evaluations.\[^65\]
  - METR said its o3 evaluation was "conducted in a relatively short time."\[^66\]
- **Product incidents:**
  - The GPT-4o sycophancy rollback; OpenAI wrote "We fell short."\[^68\]
  - Wrongful-death and negligence suits, including Raine (Aug 2025) and seven more (Nov 2025). The complaints allege OpenAI "knowingly released GPT-4o prematurely, despite internal warnings." These are allegations, not findings.\[^69\]
- **Reclassified evidence.** Apollo's advice against deploying an early Claude Opus 4 snapshot\[^67\] addressed a pre-release build later fixed. It is not evidence of oversight lagging release.
- **Caveat.** Chen's memo attributes the strain to model and release *cadence*, not headcount. H3's growth-specific mechanism remains unproven.

---

## Dated event catalog (selected, risk-mapped)

**OpenAI** (fastest growth; highest people and structural churn)

| Date | Event | Risk factors | Source |
| --- | --- | --- | --- |
| Nov 17–22, 2023 | Board fires, then reinstates Altman | C7 | \[C\] |
| Apr 2024 | Two Superalignment-linked researchers fired over leak allegations | B8, C9 | \[^60\] |
| May 2024 | Sutskever and Leike leave; Superalignment dissolved | B2, B5, C6 | \[^60\] |
| Jul 2024 | Head of Preparedness reassigned | A1–A3, B5 | \[^60\] |
| Aug 2024 | Schulman (co-founder) leaves for Anthropic, saying it was *not* due to lack of alignment support | B2 | \[^61\]\[^62\] |
| Sep 25, 2024 | Murati (CTO), McGrew (CRO), Zoph leave the same day; Altman says they left "independently… and amicably" | B1, B6 | \[^59\] |
| Oct 2024 | AGI Readiness team disbanded (Brundage departure) | C5, B5 | \[^23\] |
| Nov 2024 | Lilian Weng (VP Safety Research) leaves; Heidecke succeeds her | B2, B5 | \[^22\] (date \[C\]) |
| Apr 2025 | Preparedness Framework v2 | B5, C7 | \[^32\]\[^35\] |
| Oct 2025 | Encode/Midas subpoenas publicized; Achiam dissents | C5, C9 | \[^27\]\[^28\] |
| by end-2025 | Andrea Vallone (safety) departs | B6 | \[^77\] |
| early Feb 2026 | Hires Anthropic's Dylan Scandinaro as Head of Preparedness | B5 | \[^20\] |
| Feb 2026 | Mission Alignment disbanded; Achiam becomes "chief futurist" | C6 | \[^25\] |
| Feb 27, 2026 | Department of War deal announced; later amended | C1, C5 | \[^80\]\[^10\] |
| Mar 7, 2026 | Kalinowski resigns over governance of the deal | C5, C9 | \[^11\]\[^12\] |
| Jul 7, 2026 | Achiam announces departure after nearly nine years | C6 | \[^26\] |
| Jul 10, 2026 | Heidecke leaves; safety folded into Research under Glaese; Saachi Jain interim | B5, B6, C7 | \[^23\]\[^24\]\[^76\] |

**Anthropic** (fast growth; low documented senior people churn; high commitment churn)

| Date | Event | Risk factors | Source |
| --- | --- | --- | --- |
| Oct 2024 | Kaplan named Responsible Scaling Officer; RSP update admits minor shortfalls | C7 | \[^63\]\[^64\] |
| Nov 2024 | Claude on classified networks via Palantir/AWS | C1, C2 | \[^16\] |
| Feb 2025 | Schulman leaves after \~6 months for Thinking Machines | B2 | \[^61\] |
| Jul 14, 2025 | $200M-ceiling CDAO prototype agreement | C1, C2 | \[^14\] |
| Sep 8, 2025 | Endorses CA SB 53 | C5 | \[^45\] |
| early Feb 2026 | Safety researcher Scandinaro leaves for OpenAI | B5 | \[^20\] |
| Feb 9, 2026 | Sharma (Safeguards Research lead) resigns | B5, B6 | \[^20\]\[^21\] |
| Feb 2026 | $20M to Public First Action | C5 | \[^39\] |
| Feb 24, 2026 | RSP v3.0 drops pause commitment | Commitment churn | \[^17\]\[^18\] |
| Feb 27, 2026 | Designated a supply-chain risk after refusing two use categories | C5 | \[^9\] |
| Mar 26, 2026 | Preliminary injunction against designation | C5 | \[^13\] |
| Mar 26 & 31, 2026 | CMS exposure (\~3,000 assets); Claude Code source-map leak (likely a Bun bug; Bun acquired late 2025) | B7 | \[^72\]\[^70\]\[^71\] |
| Jun 1, 2026 | Confidential draft S-1 | C11 | \[^85\] \[C\] |
| Jun 12 – Jul 1, 2026 | Access to Claude Fable 5 / Mythos 5 suspended to comply with U.S. Commerce export controls; controls lifted Jun 30 | C5 (environment) | \[^79\]\[^86\] |

**xAI** (merger-driven loss of experienced staff; founder-centralized decisions)

| Date | Event | Risk factors | Source |
| --- | --- | --- | --- |
| Feb 23, 2025 | Unauthorized prompt change attributed to an ex-OpenAI hire | H4, B8 | \[^1\]\[^2\] |
| May 14, 2025 | Second unauthorized prompt modification; review "circumvented" | H4, A4 | \[^3\]\[^4\] |
| Early Jul 2025 | Deliberate "politically incorrect" prompt change → "MechaHitler"; X CEO resigns | A4, A14 | \[^5\]\[^6\] |
| Feb 2026 | SpaceX acquires xAI; Wu and Ba (co-founders) leave within two days | B1, C6 | \[^55\] |
| Feb–May 2026 | >50 researchers and engineers leave; sources cite unrealistic training deadlines and compromises on Grok | B1, B5 | \[^57\]\[^58\] |
| by Mar 28, 2026 | Reportedly all co-founders gone. Counts conflict (11 vs 12 co-founders) | C6 | \[^56\] |

**Meta** (acqui-hire and reallocation shock rather than organic hypergrowth)

| Date | Event | Risk factors | Source |
| --- | --- | --- | --- |
| Jun 2025 | $14.3B for a 49% stake in Scale AI; Wang leads new superintelligence unit | Acqui-hire shock | \[^53\] |
| Jul–Aug 2025 | MSL recruits leave within weeks, some returning to OpenAI; repeated reorganizations | Structural churn | \[^51\]\[^52\] |
| Jul 2025 | Refuses to sign EU Code | C5 | \[^49\] |
| Oct 2025 | \~600 AI roles cut; FAIR disproportionately affected | Structural churn | \[^8\]\[^54\] |
| Nov 19, 2025 | LeCun announces departure | H4 | \[^7\] |

**Google DeepMind** (slower headcount growth inside Alphabet; lowest documented people churn)

| Date | Event | Risk factors | Source |
| --- | --- | --- | --- |
| Feb 4, 2025 | Weapons and surveillance pledge removed | C1, C2 | \[^30\]\[^84\] |
| Mar–Apr 2025 | Gemini 2.5 Pro released without a card; no pre-deployment UK AISI access | B5, C5 | \[^36\]\[^37\] |
| Aug 29, 2025 | 60 UK parliamentarians' letter (via PauseAI UK); Google says it met its Seoul commitments | C5 | \[^36\]\[^38\] |

---

## Regulatory posture (commitment layer)

- **Lobbying.**
  - Anthropic spent $3.1M in 2025 and more than $3.5M in H1 2026.\[^42\]
  - In Q2 2026 Anthropic reported $1.97M and OpenAI $1.2M (up from $1.02M in Q1).\[^43\]
  - A Q2 commentary noted Anthropic's models "went dark in June" amid the export-control episode.\[^79\]
- **Super PACs.**
  - Leading the Future launched in 2025 with $100M+, including about $25M from Greg and Anna Brockman personally.\[^41\]
  - It targeted RAISE Act sponsor Alex Bores.\[^39\]
  - Anthropic's $20M went to the counter-PAC, Public First Action.\[^39\]
  - The NY-12 primary drew more than $27M in outside AI-industry spending.\[^40\] (weak source; verify with FEC filings)
- **Divergent state strategies.**
  - Anthropic endorsed SB 53, the RAISE Act and tougher bills.\[^44\]\[^45\]
  - OpenAI's Chris Lehane describes his approach as "reverse federalism."\[^44\]
- **State law outcomes.**
  - CA SB 53 was signed Sep 2025.\[^45\] NY RAISE was signed Dec 19, 2025, requiring incident reports within 72 hours.\[^46\]
  - CA SB 1047 was vetoed in Sep 2024.\[C\]
- **Federal environment.**
  - A Dec 11, 2025 executive order created a DOJ AI Litigation Task Force to challenge state AI laws.\[^47\]
  - US AISI was reframed as CAISI in Jun 2025.\[^87\] \[C\]
- **EU Code of Practice.**
  - OpenAI, Anthropic, Google, Microsoft, Mistral and others signed in full.\[^50\]
  - xAI signed Safety & Security only, calling other parts "profoundly detrimental to innovation."\[^48\]
  - Meta refused: "Europe is heading down the wrong path on AI."\[^49\]

---

## Theoretical grounding

- **Baron, Hannan & Burton (2001), *AJS* 106(4):960–1012** \[P\].
  - In high-tech start-ups, changing an organization's founding employment model raises turnover, which then hurts performance.
  - The turnover is concentrated among senior staff, "suggesting 'old guard disenchantment' as the primary cause."\[^74\]
  - This is the strongest peer-reviewed mechanism for H1's people layer.
- **Hannan, Burton & Baron (1996), *Industrial and Corporate Change*** \[P\].
  - "Star" and "commitment" founding models are less stable than others.\[^75\]
  - Firms that start with them have higher rates of both IPO and replacing the founder-CEO.
  - Frontier labs plausibly resemble star/commitment blueprints. This is an interpretive match, not a test.
- **Amburgey, Kelly & Barnett (1993), *ASQ* 38:51–73** \[P\].
  - Data: 1,011 Finnish newspapers over 193 years.
  - Change produces "an immediate increase in the likelihood of additional changes of the same type," as well as a higher failure hazard; both effects decay over time.\[^73\]
  - This supports H2's "reorganization momentum." External validity to AI labs is limited.
- **Hannan & Freeman (1984), structural inertia** \[C\]: reorganization raises mortality hazard, and inertia grows with size and age.
- **Brooks's law and sublinear team scaling; Vaughan (1996) on normalization of deviance; high-reliability-organization theory; Eisenhardt on high-velocity environments** \[C\]. These are as in the prior report. Eisenhardt cautions that some rapid change is adaptive.

---

## Alternative explanations

| Alternative | Verdict | Notes |
| --- | --- | --- |
| Founder/CEO style | **Strong co-explanation** | xAI's incidents track founder-centralized control; OpenAI's churn follows the 2023 crisis. Growth amplifies founder effects. |
| Ideology / mission drift | **Partial** | Leike, Sharma and Kalinowski cite values or governance. Schulman explicitly denied a lack of alignment support.\[^62\] |
| Political / regulatory environment | **Strong co-explanation** | Labs cite competition and the political climate for loosening their commitments.\[^19\]\[^30\] |
| Generic AI talent-market churn | **Real confounder** | Meta's nine-figure offers and boomerang departures;\[^52\]\[^53\] xAI alumni recruited by Meta and Thinking Machines.\[^57\] |
| Merger shock (xAI) | **Confirmed confounder** | Treat separately. |
| Reallocation / acqui-hire (Meta) | **Confirmed confounder** | Not organic growth. |
| Small N / salience bias | **Serious limitation** | Six labs; high-profile departures overrepresented. |

---

## Mitigating channels (for H5)

- **IPO governance and SEC disclosure liability.** These are plausibly disciplining, but mostly beyond the 6-month window.
- **Binding or quasi-binding external duties.** RAISE Act 72-hour incident reporting,\[^46\] SB 53,\[^45\] and EU Code resourcing floors.
- **Evidence that commitments can be enforced or held.** Anthropic's two red lines held under government pressure and were upheld in court, at least preliminarily.\[^13\] OpenAI's deal was amended after backlash.\[^11\]
- **Counter-signal.** Pre-IPO quiet periods reduce *observability* rather than risk.

---

## Hypothesis assessment (revised after verification)

| Hypothesis | Verdict | Confidence (previous → now) | What moved it |
| --- | --- | --- | --- |
| **H1** | Supported as amplifier | 60–75% (unchanged, amplifier framing) | +Baron et al. mechanism;\[^74\] −Meta figures removed |
| **H2** | Plausible; theory now verified | 45–60% → **50–65%** | Amburgey et al. momentum finding verified\[^73\] |
| **H3** | Pattern supported; first-party mechanism statement | 50–65% → **55–70%** | Chen memo;\[^22\] −Apollo reclassified\[^67\] |
| **H4** | Supported; most distinctive | 65–80% (unchanged) | +cross-lab amicus dissent;\[^83\] Anthropic "reversal" softened |
| **H5** | Supported | 65–75% (unchanged) | — |

**Where the hypotheses fail or need reframing:**

1. **Growth is not sufficient for people churn.** Anthropic is the counterexample. Better framing: *growth relative to absorptive capacity amplifies the founder/CEO decision regime and shows up in different layers depending on founder stability.*
2. **Racing explains the *direction* of commitment change.** The labs say so themselves.\[^17\]\[^19\]\[^30\]\[^32\] Growth plausibly explains its *speed and fragmentation*.
3. **H4 is the most defensible novel contribution.**

---

## Recommendations

- **A falsifiable 6-month prediction** from the founder-stability framing: Anthropic's volatility should appear mainly as framework and stance revisions; OpenAI's mainly as role and team turnover. If the reverse happens, the framing fails.
- **Metrics AISI could request confidentially:**
  1. Risk-owner tenure and where successors come from.
  2. Number of safety-team creations, dissolutions and charter rewrites.
  3. How long safety-team charters last.
  4. Safety-staff share and tenure.
  5. Growth in the number of people with privileged access.
  6. Count of "unauthorized" production-change incidents.
  7. Median interval between evaluation and release.
  8. Commitment revisions, and whether each tightened or loosened.
  9. Share of risk-owning roles filled by acqui-hires or staff with under 12 months' tenure.
  10. Whistleblower report volume and resolution time.
  11. Lobbying and political spend by bill.
  12. Divergence between internal policy and public statements.
  13. A post-acquisition integration incident log (cf. Bun\[^71\]).

---

## Caveats and evidence quality

- **Strongest sources:**
  - Primary: company statements,\[^14\]\[^35\] court records,\[^15\] peer-reviewed papers.\[^73\]\[^74\]\[^75\]
  - Major outlets: Fortune, NPR, TechCrunch, Axios, The Intercept.
- **Weakest sources (replace before submission):**
  - \[^16\] is a user-published summary on claude.ai. Verify the Palantir date and the usage-policy terms against Anthropic or Palantir press releases.
  - \[^40\], \[^50\], \[^51\], \[^56\], \[^57\], \[^58\], \[^60\], \[^77\] are aggregators.
  - \[^22\] is a mirror of Wired's memo text; cite Wired directly.
  - \[^65\] is a mirror of the FT.
- **Carried-over \[C\] items were not re-fetched in this pass:** headcount series (OpenAI \~770 → \~4,500; Anthropic \~2,300 by Dec 2025), S-1 dates, the FLI index, CAISI, the SB 1047 veto, the 2023 board-crisis details.
- **Lawsuit claims \[^69\] are allegations.**
- **Conflict of interest:** the author is an Anthropic model. The Anthropic rows include both favourable and adverse evidence; check them independently.

---

## Footnotes

*All sources accessed 2026-09-26 unless marked \[C\].*

\[^1\]: \[S\] B. Nolan, "xAI chief engineer blames former OpenAI employee…," *Fortune*, 2025-02-24. [https://fortune.com/2025/02/24/xai-chief-engineer-blames-former-openai-employee-grok-blocks-musk-trump-misinformation](https://fortune.com/2025/02/24/xai-chief-engineer-blames-former-openai-employee-grok-blocks-musk-trump-misinformation) — "without asking anyone at the company for confirmation" \[^2\]: \[S\] "Grok briefly censored criticism of Musk and Trump…," *Business Insider* (NL edition), Feb 2025 (Babuschkin post dated 2025-02-23). [https://businessinsider.nl/grok-briefly-censored-criticism-of-musk-and-trump-it-was-blamed-on-a-new-hire-who-hadnt-fully-absorbed-the-startups-culture](https://businessinsider.nl/grok-briefly-censored-criticism-of-musk-and-trump-it-was-blamed-on-a-new-hire-who-hadnt-fully-absorbed-the-startups-culture) — "hasn't fully absorbed xAI's culture yet" \[^3\]: \[S\] *Ars Technica*, 2025-05-16, via Harvard TagTeam feed mirror. [https://tagteam.harvard.edu/hub_feeds/3382/feed_items/13810374](https://tagteam.harvard.edu/hub_feeds/3382/feed_items/13810374) — review process "circumvented in this incident" \[^4\]: \[S\] "xAI says Grok kept talking about 'white genocide' because an unauthorized modification…," *Business Insider* (NL), 2025-05-16. [https://www.businessinsider.nl/elon-musks-xai-says-grok-kept-talking-about-white-genocide-because-an-unauthorized-modification-was-made-on-the-backend/](https://www.businessinsider.nl/elon-musks-xai-says-grok-kept-talking-about-white-genocide-because-an-unauthorized-modification-was-made-on-the-backend/) — "an unauthorized modification was made to the Grok response bot's prompt on X" \[^5\]: \[S\] NPR via Michigan Public, 2025-07-09. [https://www.michiganpublic.org/2025-07-09/elon-musks-ai-chatbot-grok-started-calling-itself-mechahitler](https://www.michiganpublic.org/2025-07-09/elon-musks-ai-chatbot-grok-started-calling-itself-mechahitler) — "not shy away from making claims which are politically incorrect" \[^6\]: \[S\] *Salon* via Yahoo News, 2025-07-09. [https://www.yahoo.com/news/yaccarino-resigns-ceo-x-day-174838495.html](https://www.yahoo.com/news/yaccarino-resigns-ceo-x-day-174838495.html) — "I've decided to step down as CEO of X" \[^7\]: \[S\] AFP via Channels TV, 2025-11-20. [https://www.channelstv.com/2025/11/20/meta-chief-ai-scientist-yann-lecun-leaving-for-startup](https://www.channelstv.com/2025/11/20/meta-chief-ai-scientist-yann-lecun-leaving-for-startup) — "I am planning to leave Meta after 12 years" \[^8\]: \[S\] Storyboard18, 2025-11-20. [https://www.storyboard18.com/amp/brand-makers/yann-lecun-confirms-exit-from-meta-sets-sights-on-new-advanced-ai-venture-84519.htm](https://www.storyboard18.com/amp/brand-makers/yann-lecun-confirms-exit-from-meta-sets-sights-on-new-advanced-ai-venture-84519.htm) — reporting line shifted "from chief product officer Chris Cox to Wang" \[^9\]: \[S\] J. Kahn, *Fortune*, 2026-02-28. [https://fortune.com/2026/02/28/openai-pentagon-deal-anthropic-designated-supply-chain-risk-unprecedented-action-damage-its-growth](https://fortune.com/2026/02/28/openai-pentagon-deal-anthropic-designated-supply-chain-risk-unprecedented-action-damage-its-growth) — "first time the U.S. has ever designated an American company a supply chain risk" \[^10\]: \[S\] *Sherwood News*, early Mar 2026. [https://sherwood.news/tech/openais-altman-our-rushed-deal-with-the-pentagon-looked-opportunistic-and](https://sherwood.news/tech/openais-altman-our-rushed-deal-with-the-pentagon-looked-opportunistic-and) — "It just looked opportunistic and sloppy." \[^11\]: \[S\] *Cybernews*, 2026-03-08. [https://cybernews.com/ai-news/openais-robotics-chief-resigns-over-the-companys-pentagon-deal/](https://cybernews.com/ai-news/openais-robotics-chief-resigns-over-the-companys-pentagon-deal/) — "This was about principle, not people." (Also reports the amended surveillance language and her Nov 2024 start.) \[^12\]: \[S\] Reuters via DZRH, 2026-03-08. [https://www.dzrh.com.ph/post/openai-robotics-head-resigns-after-deal-with-pentagon](https://www.dzrh.com.ph/post/openai-robotics-head-resigns-after-deal-with-pentagon) — "It's a governance concern first and foremost" \[^13\]: \[S\] NPR, 2026-03-26. [https://www.npr.org/2026/03/26/nx-s1-5762971/judge-temporarily-blocks-anthropic-ban](https://www.npr.org/2026/03/26/nx-s1-5762971/judge-temporarily-blocks-anthropic-ban) — "likely both contrary to law and arbitrary and capricious" \[^14\]: \[P\] Anthropic, "Anthropic and the Department of Defense…," 2025-07-14. [https://anthropic.com/news/anthropic-and-the-department-of-defense-to-advance-responsible-ai-in-defense-operations](https://anthropic.com/news/anthropic-and-the-department-of-defense-to-advance-responsible-ai-in-defense-operations) — "a two-year prototype other transaction agreement with a $200 million ceiling" \[^15\]: \[P\] Anthropic declaration, N.D. Cal. (CourtListener docket 465515, exhibit 6-3), 2026. [https://storage.courtlistener.com/recap/gov.uscourts.cand.465515/gov.uscourts.cand.465515.6.3.pdf](https://storage.courtlistener.com/recap/gov.uscourts.cand.465515/gov.uscourts.cand.465515.6.3.pdf) — Claude Gov models "fine-tuned so that they would not refuse requests" \[^16\]: \[W\] User-published summary on claude.ai (not an official source). [https://claude.ai/public/artifacts/f1c3dd80-a3eb-49eb-9d92-867705526437](https://claude.ai/public/artifacts/f1c3dd80-a3eb-49eb-9d92-867705526437) — "the Pentagon agreed at signing to abide by Anthropic's acceptable use policy" (Replace with Anthropic/Palantir Nov 7, 2024 press releases.) \[^17\]: \[S\] NYU Shanghai RITS summary of TIME reporting, \~2026-02-25. [https://rits.shanghai.nyu.edu/ai/anthropic-drops-flagship-safety-pledge-amid-competitive-and-government-pressure/](https://rits.shanghai.nyu.edu/ai/anthropic-drops-flagship-safety-pledge-amid-competitive-and-government-pressure/) — Kaplan: "if competitors are blazing ahead" \[^18\]: \[P\] Centre for the Governance of AI, "Anthropic's RSP v3.0…," 2026. [https://governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections](https://governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections) — "Anthropic is not lowering any of its existing mitigations" \[^19\]: \[W\] ForkLog, \~2026-02-25 (quoting Anthropic's blog). [https://forklog.com/en/anthropic-eases-ai-safety-rules-amid-pentagon-pressure/](https://forklog.com/en/anthropic-eases-ai-safety-rules-amid-pentagon-pressure/) — "shifted towards prioritizing competitiveness and economic growth" (Replace with Anthropic's RSP v3 post.) \[^20\]: \[S\] M. Hawley, *VKTR*, 2026-02-10. [https://www.vktr.com/ai-news/a-world-in-peril-why-mrinank-sharma-walked-away-from-anthropic/](https://www.vktr.com/ai-news/a-world-in-peril-why-mrinank-sharma-walked-away-from-anthropic/) — "how hard it is to truly let our values govern our actions" (Also reports Scandinaro's move to OpenAI as Head of Preparedness.) \[^21\]: \[S\] Storyboard18, 2026-02-24. [https://www.storyboard18.com/brand-makers/the-world-is-in-peril-not-just-from-ai-anthropics-safeguards-head-mrinank-sharma-resigns-89267.htm](https://www.storyboard18.com/brand-makers/the-world-is-in-peril-not-just-from-ai-anthropics-safeguards-head-mrinank-sharma-resigns-89267.htm) — Safeguards Research Team introduced Feb 2025; Feb 9 was his last day (paraphrased). \[^22\]: \[W\] Mirror of *Wired* reporting on Mark Chen's memo, \~2026-07-10. [https://traeai.com/articles/11d6d5c7-5f03-46bf-b3f1-ef29ae2460ca](https://traeai.com/articles/11d6d5c7-5f03-46bf-b3f1-ef29ae2460ca) — "we have bigger coordination challenges around safety today than ever before" (Cite Wired directly.) \[^23\]: \[S\] *The Next Web*, Jul 2026. [https://thenextweb.com/news/openai-heidecke-safety-head-leaving-research-merger](https://thenextweb.com/news/openai-heidecke-safety-head-leaving-research-merger) — "the second time in less than two years" (folding safety into research) \[^24\]: \[S\] Wired via *The Edge Malaysia*, 2026-07-11. [https://theedgemalaysia.com/node/810279](https://theedgemalaysia.com/node/810279) — "Saachi Jain will become interim head of safety systems" \[^25\]: \[W\] Shopifreaks, 2026-02-13 (Platformer reporting). [https://www.shopifreaks.com/openai-disbands-mission-alignment-team-and-names-joshua-achiam-as-chief-futurist/](https://www.shopifreaks.com/openai-disbands-mission-alignment-team-and-names-joshua-achiam-as-chief-futurist/) — "reassigned the team's six members to other departments" \[^26\]: \[W\] Let's Data Science (Wired reporting), Jul 2026. [https://letsdatascience.com/news/openai-chief-futurist-joshua-achiam-leaves-company-fbc72b03](https://letsdatascience.com/news/openai-chief-futurist-joshua-achiam-leaves-company-fbc72b03) — "notified colleagues on July 7, 2026 that he plans to leave" \[^27\]: \[S\] *Puck*, Oct 2025. [https://puck.news/newsletter_content/openais-legal-battle-newsoms-new-law-altman-musk-derivatives/](https://puck.news/newsletter_content/openais-legal-battle-newsoms-new-law-altman-musk-derivatives/) — Achiam: "possibly a risk to my whole career" \[^28\]: \[S\] *Fortune*, 2025-10-10. [https://fortune.com/2025/10/10/a-3-person-policy-non-profit-that-worked-on-californias-ai-safety-law-is-publicly-accusing-openai-of-intimidation-tactics](https://fortune.com/2025/10/10/a-3-person-policy-non-profit-that-worked-on-californias-ai-safety-law-is-publicly-accusing-openai-of-intimidation-tactics) — "served with a subpoena from OpenAI in August, delivered by a sheriff's deputy" \[^29\]: \[S\] *The Decoder*, Oct 2025. [https://the-decoder.com/openai-accused-of-pressuring-ai-regulation-advocates-with-subpoenas/](https://the-decoder.com/openai-accused-of-pressuring-ai-regulation-advocates-with-subpoenas/) — Kwon: subpoenas "part of evidence preservation" \[^30\]: \[S\] CNN via Ada Derana, 2025-02-05. [https://www.adaderana.lk/technology/105542/google-erases-promise-not-to-use-ai-technology-for-weapons-or-surveillance](https://www.adaderana.lk/technology/105542/google-erases-promise-not-to-use-ai-technology-for-weapons-or-surveillance) — "There's a global competition taking place for AI leadership" \[^31\]: \[S\] S. Biddle, *The Intercept*, 2024-01-12. [https://theintercept.com/2024/01/12/open-ai-military-ban-chatgpt/](https://theintercept.com/2024/01/12/open-ai-military-ban-chatgpt/) — "quietly deleted language expressly prohibiting the use of its technology for military purposes" \[^32\]: \[S\] *TechCrunch*, 2025-04-15. [https://techcrunch.com/2025/04/15/openai-says-it-may-adjust-its-safety-requirements-if-a-rival-lab-releases-high-risk-ai](https://techcrunch.com/2025/04/15/openai-says-it-may-adjust-its-safety-requirements-if-a-rival-lab-releases-high-risk-ai) — "If another frontier AI developer releases a high-risk system without comparable safeguards" \[^33\]: \[S\] *Fortune* via Yahoo, 2025-04-16. [https://www.yahoo.com/news/openai-updated-safety-framework-no-190931446.html](https://www.yahoo.com/news/openai-updated-safety-framework-no-190931446.html) — "Some critics highlighted the removal of persuasion" \[^34\]: \[S\] *Business Insider* (NL), Apr 2025. [https://www.businessinsider.nl/openai-just-gave-itself-wiggle-room-on-safety-if-rivals-release-high-risk-models](https://www.businessinsider.nl/openai-just-gave-itself-wiggle-room-on-safety-if-rivals-release-high-risk-models) — Adler: "OpenAI is quietly reducing its safety commitments" \[^35\]: \[P\] OpenAI, "Our updated Preparedness Framework," 2025-04-15. [https://openai.com/index/updating-our-preparedness-framework/](https://openai.com/index/updating-our-preparedness-framework/) — "a sharper focus on the specific risks that matter most" \[^36\]: \[S\] B. Nolan, *Fortune*, 2025-08-29. [https://fortune.com/2025/08/29/british-lawmakers-accuse-google-deepmind-of-breach-of-trust-over-delayed-gemini-2-5-pro-safety-report](https://fortune.com/2025/08/29/british-lawmakers-accuse-google-deepmind-of-breach-of-trust-over-delayed-gemini-2-5-pro-safety-report) — "a troubling breach of trust with governments and the public" \[^37\]: \[W\] EA Forum crosspost of TIME exclusive, Aug 2025. [https://forum.effectivealtruism.org/posts/TkMKftX9w3atD2X5L/60-u-k-lawmakers-accuse-google-of-breaking-ai-safety-pledge](https://forum.effectivealtruism.org/posts/TkMKftX9w3atD2X5L/60-u-k-lawmakers-accuse-google-of-breaking-ai-safety-pledge) — "did not provide the UK AISI with pre-deployment access" (Cite TIME directly.) \[^38\]: \[S\] TIME via Yahoo, 2025-08-29. [https://www.yahoo.com/news/articles/exclusive-60-u-k-lawmakers-130310608.html](https://www.yahoo.com/news/articles/exclusive-60-u-k-lawmakers-130310608.html) — Google: "We're fulfilling our public commitments, including the Seoul Frontier AI Safety Commitments" \[^39\]: \[S\] *TechCrunch*, 2026-02-20. [https://techcrunch.com/2026/02/20/anthropic-funded-group-backs-candidate-attacked-by-rival-ai-super-pac](https://techcrunch.com/2026/02/20/anthropic-funded-group-backs-candidate-attacked-by-rival-ai-super-pac) — "Public First Action, a PAC backed by a $20 million donation from Anthropic" \[^40\]: \[W\] Let's Data Science (AdImpact/The Hill), 2026-06-23. [https://letsdatascience.com/news/corporate-ai-super-pacs-spend-27-million-6d71dbd6](https://letsdatascience.com/news/corporate-ai-super-pacs-spend-27-million-6d71dbd6) — "more than $27 million in total outside AI-industry spending" (Verify with FEC data.) \[^41\]: \[S\] I. Krietzberg, *Puck*, 2026-06-23. [https://puck.news/ai-money-deluge-targeting-new-york-lawmaker-alex-bores/](https://puck.news/ai-money-deluge-targeting-new-york-lawmaker-alex-bores/) — "some $25 million from OpenAI co-founder Greg Brockman and his wife, Anna" \[^42\]: \[S\] *Axios*, 2026-07-21. [https://axios.com/2026/07/21/anthropic-ramps-up-lobbying-spending-ai-policy-fights](https://axios.com/2026/07/21/anthropic-ramps-up-lobbying-spending-ai-policy-fights) — "the $3.1 million it spent during all of 2025" \[^43\]: \[W\] Let's Data Science (Senate LDA filings), Jul 2026. [https://letsdatascience.com/news/anthropic-and-openai-increase-federal-lobbying-spending-in-q-f34c00b0](https://letsdatascience.com/news/anthropic-and-openai-increase-federal-lobbying-spending-in-q-f34c00b0) — "OpenAI reported $1.2 million, compared with $1.02 million in Q1" (Verify on lda.senate.gov.) \[^44\]: \[W\] AI Weekly (Politico reporting), 2026. [https://aiweekly.co/alerts/anthropic-pushes-state-by-state-ratchet-on-ai-safety-rules](https://aiweekly.co/alerts/anthropic-pushes-state-by-state-ratchet-on-ai-safety-rules) — Lehane "calls his contrasting play 'reverse federalism'" \[^45\]: \[S\] *TechCrunch*, 2025-09-08. [https://techcrunch.com/2025/09/08/anthropic-endorses-californias-ai-safety-bill-sb-53/](https://techcrunch.com/2025/09/08/anthropic-endorses-californias-ai-safety-bill-sb-53/) — "Anthropic announced an official endorsement of SB 53" \[^46\]: \[S\] *TechCrunch*, 2025-12-20. [https://techcrunch.com/2025/12/20/new-york-governor-kathy-hochul-signs-raise-act-to-regulate-ai-safety](https://techcrunch.com/2025/12/20/new-york-governor-kathy-hochul-signs-raise-act-to-regulate-ai-safety) — "report safety incidents to the state within 72 hours" \[^47\]: \[P\] Paul Hastings client alert, 2025-12-16. [https://www.paulhastings.com/insights/client-alerts/president-trump-signs-executive-order-challenging-state-ai-laws](https://www.paulhastings.com/insights/client-alerts/president-trump-signs-executive-order-challenging-state-ai-laws) — "establishes an AI Litigation Task Force within the Department of Justice" \[^48\]: \[S\] Reuters via *The Standard* (HK), 2025-07-31. [https://www.thestandard.com.hk/world/article/307966/Musks-xAI-to-sign-chapter-on-safety-and-security-in-EUs-AI-code-of-practice](https://www.thestandard.com.hk/world/article/307966/Musks-xAI-to-sign-chapter-on-safety-and-security-in-EUs-AI-code-of-practice) — xAI: other parts "profoundly detrimental to innovation" \[^49\]: \[S\] *Investment Monitor*, 2025-07-21. [https://www.investmentmonitor.ai/newsletters/meta-declines-to-sign-eu-ai-code-of-practice](https://www.investmentmonitor.ai/newsletters/meta-declines-to-sign-eu-ai-code-of-practice) — Kaplan: "Europe is heading down the wrong path on AI." \[^50\]: \[W\] CASRAI, mid-2026. [https://casrai.org/wp/tag/eu-ai-office/](https://casrai.org/wp/tag/eu-ai-office/) — "have signed the EU's General-Purpose AI Code of Practice in full" (Check the Commission's live signatory list.) \[^51\]: \[W\] Implicator.ai (Business Insider reporting), 2025. [https://www.implicator.ai/metas-superintelligence-bet-shows-cracks-as-researchers-exit/](https://www.implicator.ai/metas-superintelligence-bet-shows-cracks-as-researchers-exit/) — "managers changing several times amid constant structural shifts" \[^52\]: \[S\] *The Decoder* (Wired, FT reporting), 2025-08-27/29. [https://the-decoder.com/metas-superintelligence-hires-left-for-openai-after-only-a-few-weeks/](https://the-decoder.com/metas-superintelligence-hires-left-for-openai-after-only-a-few-weeks/) — "spent less than a month at Meta before returning to OpenAI" \[^53\]: \[S\] *SiliconANGLE*, 2025-06-26. [https://siliconangle.com/2025/06/26/meta-reportedly-recruits-four-former-openai-researchers-superintelligence-lab/](https://siliconangle.com/2025/06/26/meta-reportedly-recruits-four-former-openai-researchers-superintelligence-lab/) — "invested $14.3 billion in the startup for a 49% stake" \[^54\]: \[C\] *Forbes*, 2025-10-22. [https://www.forbes.com/sites/zacharyfolk/2025/10/22/meta-laying-off-about-600-staff-at-ai-superintelligence-labs-heres-whats-impacted/](https://www.forbes.com/sites/zacharyfolk/2025/10/22/meta-laying-off-about-600-staff-at-ai-superintelligence-labs-heres-whats-impacted/) — \~600 cuts (not re-fetched). \[^55\]: \[S\] *GIGAZINE* (summarizing The Verge and CNBC), 2026-02-12. [https://www.gigazine.net/gsc_news/en/20260212-xai-co-founders-leaving](https://www.gigazine.net/gsc_news/en/20260212-xai-co-founders-leaving) — CNBC: xAI "loses second co-founder in two days" \[^56\]: \[W\] Techleap Finder, Mar 2026. [https://finder.techleap.nl/news/note/all-11-xai-co-founders-are-gone-as-musk-rebuilds-from-the-ground-up](https://finder.techleap.nl/news/note/all-11-xai-co-founders-are-gone-as-musk-rebuilds-from-the-ground-up) — "Ross Nordeen, the last to remain, departed on March 28, 2026" (Counts conflict with other sources.) \[^57\]: \[W\] RuntimeWire (TechCrunch/The Information), May 2026. [https://runtimewire.com/article/spacexai-post-merger-exits-musk-leadership-talent-drift](https://runtimewire.com/article/spacexai-post-merger-exits-musk-leadership-talent-drift) — "lost more than 50 researchers and engineers since February" \[^58\]: \[W\] HyperAI (The Information), May 2026. [https://hyper.ai/en/stories/a798c83d7c0e1b424f75ec8c69bcd399](https://hyper.ai/en/stories/a798c83d7c0e1b424f75ec8c69bcd399) — "forcing compromises in Grok's development" \[^59\]: \[S\] *Axios*, 2024-09-25. [https://www.axios.com/2024/09/25/openai-mira-murati-leaving](https://www.axios.com/2024/09/25/openai-mira-murati-leaving) — "made these decisions independently of each other and amicably" \[^60\]: \[W\] Texxr (Platformer-based timeline), Feb 2026. [https://texxr.com/posts/chief-futurist-alignment-leaves-the-lab](https://texxr.com/posts/chief-futurist-alignment-leaves-the-lab) — "In July, the head of OpenAI's Preparedness team was reassigned" \[^61\]: \[S\] Wikipedia, "John Schulman" (citing Fortune 2025-02-06). [https://en.wikipedia.org/wiki/John_Schulman](https://en.wikipedia.org/wiki/John_Schulman) — "In February 2025, he announced he was leaving to join Thinking Machines Lab" \[^62\]: \[W\] Texxr entity page (Schulman's X post, 2024-08-06). [https://texxr.com/entity/john-schulman](https://texxr.com/entity/john-schulman) — "I'm not leaving due to lack of support for alignment research" \[^63\]: \[S\] Wikipedia, "Jared Kaplan" (citing Anthropic, Oct 2024). [https://en.wikipedia.org/wiki/Jared_Kaplan](https://en.wikipedia.org/wiki/Jared_Kaplan) — Kaplan "would serve as the company's 'Responsible Scaling Officer'" \[^64\]: \[W\] CO/AI summary of Anthropic's Oct 2024 RSP update. [https://about.getcoai.com/?p=25898](https://about.getcoai.com/?p=25898) — "fell short of meeting all requirements" (Cite Anthropic's post directly.) \[^65\]: \[W\] InsideView blog quoting the *Financial Times* (C. Criddle), 2025-04-12. [https://insideview.ie/2025/04/12/need-longer-ai-testing-time.html](https://insideview.ie/2025/04/12/need-longer-ai-testing-time.html) — "Staff and third-party groups have recently been given just days" (Cite the FT directly.) \[^66\]: \[S\] *TechCrunch*, 2025-04-16. [https://techcrunch.com/2025/04/16/openai-partner-says-it-had-relatively-little-time-to-test-the-companys-new-ai-models](https://techcrunch.com/2025/04/16/openai-partner-says-it-had-relatively-little-time-to-test-the-companys-new-ai-models) — METR: "conducted in a relatively short time" \[^67\]: \[S\] *TechCrunch*, 2025-05-22. [https://techcrunch.com/2025/05/22/a-safety-institute-advised-against-releasing-an-early-version-of-anthropics-claude-opus-4-ai-model](https://techcrunch.com/2025/05/22/a-safety-institute-advised-against-releasing-an-early-version-of-anthropics-claude-opus-4-ai-model) — Apollo: "we advise against deploying this model either internally or externally" (early snapshot; bug reportedly fixed) \[^68\]: \[S\] *TechCrunch*, 2025-04-29. [https://techcrunch.com/2025/04/29/openai-explains-why-chatgpt-became-too-sycophantic](https://techcrunch.com/2025/04/29/openai-explains-why-chatgpt-became-too-sycophantic) — OpenAI: "We fell short and are working on getting it right." \[^69\]: \[S\] AP via *News Tribune*, 2025-11-08. [https://www.newstribune.com/news/2025/nov/08/openai-faces-seven-lawsuits-claiming-chatgpt/](https://www.newstribune.com/news/2025/nov/08/openai-faces-seven-lawsuits-claiming-chatgpt/) — complaints allege OpenAI "knowingly released GPT-4o prematurely, despite internal warnings" (allegation) \[^70\]: \[S\] B. Nolan, *Fortune*, 2026-03-31. [https://fortune.com/2026/03/31/anthropic-source-code-claude-code-data-leak-second-security-lapse-days-after-accidentally-revealing-mythos](https://fortune.com/2026/03/31/anthropic-source-code-claude-code-data-leak-second-security-lapse-days-after-accidentally-revealing-mythos) — "a release packaging issue caused by human error, not a security breach" \[^71\]: \[W\] Kilo Code blog (The Hacker News reporting), Apr 2026. [https://blog.kilo.ai/p/claude-code-source-leak-a-timeline](https://blog.kilo.ai/p/claude-code-source-leak-a-timeline) — likely root cause "a known bug in Bun"; Bun acquired late 2025 (tentative) \[^72\]: \[W\] DPEX Network, 2026-04-14 (Fortune 2026-03-26 reporting). [https://www.dpexnetwork.org/articles/how-basic-oversights-exposed-anthropics-secrets](https://www.dpexnetwork.org/articles/how-basic-oversights-exposed-anthropics-secrets) — "close to 3,000 unpublished assets accessible through a misconfigured content management system" \[^73\]: \[P\] Amburgey, Kelly & Barnett, "Resetting the Clock," *ASQ* 38(1):51–73, 1993; abstract via Stanford GSB. [https://www.gsb.stanford.edu/faculty-research/working-papers/resetting-clock-dynamics-organizational-change-failure](https://www.gsb.stanford.edu/faculty-research/working-papers/resetting-clock-dynamics-organizational-change-failure) — "an immediate increase in the likelihood of additional changes of the same type" \[^74\]: \[P\] Baron, Hannan & Burton, "Labor Pains," *AJS* 106(4):960–1012, 2001. [https://durham-repository.worktribe.com/output/1580656/labor-pains-change-in-organizational-models-and-employee-turnover-in-young-high-tech-firms](https://durham-repository.worktribe.com/output/1580656/labor-pains-change-in-organizational-models-and-employee-turnover-in-young-high-tech-firms) — "suggesting 'old guard disenchantment' as the primary cause" \[^75\]: \[P\] Hannan, Burton & Baron, "Inertia and Change in the Early Years," *Industrial and Corporate Change* 5, 1996. [https://ecommons.cornell.edu/bitstream/1813/75693/1/Burton10_Inertia_and_Change.pdf](https://ecommons.cornell.edu/bitstream/1813/75693/1/Burton10_Inertia_and_Change.pdf) — "the 'star' model and 'commitment' model are less stable" \[^76\]: \[C\] *Tech Times*, 2026-07-11. [https://www.techtimes.com/articles/320191/20260711/openai-loses-sixth-safety-leader-two-years-folds-team-research.htm](https://www.techtimes.com/articles/320191/20260711/openai-loses-sixth-safety-leader-two-years-folds-team-research.htm) — "sixth safety leader" count (not re-fetched; the count depends on the definition). \[^77\]: \[W\] Crypto Briefing, Jul 2026. [https://cryptobriefing.com/openai-safety-head-heidecke-departs/](https://cryptobriefing.com/openai-safety-head-heidecke-departs/) — Vallone "departed by the end of 2025" \[^79\]: \[S\] *Techstrong.ai* (CNBC reporting), Jul 2026. [https://techstrong.ai/articles/openai-anthropic-surge-to-record-lobbying-spending-ahead-of-midterms/](https://techstrong.ai/articles/openai-anthropic-surge-to-record-lobbying-spending-ahead-of-midterms/) — "its models went dark in June" \[^80\]: \[S\] *Tom's Hardware*, 2026-02-28. [https://tomshardware.com/tech-industry/artificial-intelligence/openai-strikes-deal-with-pentagon-following-claude-blacklisting](https://tomshardware.com/tech-industry/artificial-intelligence/openai-strikes-deal-with-pentagon-following-claude-blacklisting) — Altman: "The DoW agrees with these principles, reflects them in law and policy" \[^82\]: \[S\] *Fortune*, 2026-03-02. [https://www.fortune.com/2026/03/02/openai-ceo-sam-altman-defends-decision-to-strike-pentagon-deal-amid-backlash-against-the-chatgpt-maker-following-anthropic-blacklisting](https://www.fortune.com/2026/03/02/openai-ceo-sam-altman-defends-decision-to-strike-pentagon-deal-amid-backlash-against-the-chatgpt-maker-following-anthropic-blacklisting) — Altman "had earlier in the week voiced support for Anthropic's position" \[^83\]: \[S\] *FedScoop*, 2026-03-26. [https://fedscoop.com/district-court-temporarily-blocks-anthropic-ban-supply-chain-risk-designation/](https://fedscoop.com/district-court-temporarily-blocks-anthropic-ban-supply-chain-risk-designation/) — amicus briefs filed by Microsoft, "employees at Google and OpenAI" \[^84\]: \[S\] AFP via *Fortune*, 2025-02-05. [https://www.fortune.com/2025/02/05/google-drops-pledge-not-use-ai-weapons-surveillance](https://www.fortune.com/2025/02/05/google-drops-pledge-not-use-ai-weapons-surveillance) — "removing vows not to use the technology for weapons or surveillance" \[^85\]: \[C\] Anthropic, "Anthropic confidentially submits draft S-1," 2026-06-01. [https://www.anthropic.com/news/confidential-draft-s1-sec](https://www.anthropic.com/news/confidential-draft-s1-sec) — not re-fetched. \[^86\]: \[C\] Anthropic statement on Fable/Mythos access. [https://www.anthropic.com/news/fable-mythos-access](https://www.anthropic.com/news/fable-mythos-access) — not fetched in this pass. \[^87\]: \[C\] U.S. Department of Commerce, statement on CAISI, Jun 2025. [https://www.commerce.gov/news/press-releases/2025/06/statement-us-secretary-commerce-howard-lutnick-transforming-us-ai](https://www.commerce.gov/news/press-releases/2025/06/statement-us-secretary-commerce-howard-lutnick-transforming-us-ai) — not re-fetched.
