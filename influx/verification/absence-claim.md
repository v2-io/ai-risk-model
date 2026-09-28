# Verification: the growth / turnover / IPO absence claim

*Verifier: Claude (Opus 5.5), 2026-09-27. Scope: the executive-summary bullet "No authoritative body names lab headcount growth rate, hypergrowth, turnover or IPO pressure as a risk factor", the §4 rows that repeat it, row C15, and Recommendations 1–5. Sibling files `eu.md`, `uk.md` and `us-security.md` cover the AI-specific EU, UK and RAND near-misses in depth; this file cross-references them rather than repeating their quote work, except where a quote is load-bearing here.*

*Tags follow the report's scheme: **[P]** primary, text-searched by me; **[S]** reputable secondary; **[U]** not verified against the source text. Two extra marks: **[F]**: read through a web-fetch tool that returns extracted quotes, so the quote is probably verbatim but should be re-checked before it is quoted externally; **[commentary]**: an opinion or analysis piece, cited as such.*

---

## 1. Verdict

**The claim is true only under a narrower scope than it states, and it is false under the scope it actually states.**

- **As written ("no authoritative body") it is false.** Aviation, major-hazard and nuclear safety regulators all name organisational change as a source of new hazards, and they list expansion, staffing levels, changes to key personnel and key-personnel turnover among the changes that count:
  - ICAO lists "organizational expansion or contraction" as a source of change that "may affect the effectiveness of existing safety risk controls". It tells regulators to profile service providers by the "turnover rate of the key personnel such as the accountable executive and safety manager."[^icao]
  - UK HSE,[^hse] the US Chemical Safety Board[^csb] and the IAEA[^iaea] make similar statements.
  - Security authorities say the same about growth and security:
    - UK NPSA/NCSC tell growing tech firms that their risks "may well have changed, for example because your team has grown".[^npsa]
    - The UK government's 2023 frontier-AI safety-processes paper points frontier developers to that guidance.[^dsit-ep]
    - CISA lists "Recent merger/acquisition" and "Pattern of overwork" as organisational insider-risk indicators.[^cisa]

  Neither ICAO nor HSE is about AI. But the report's phrase is "authoritative body", with no AI qualifier, and that scoping is doing a great deal of work.
- **Scoped to AI-specific bodies and instruments, the claim holds for the word "factor".** I found no AI-specific government, intergovernmental, standards or statutory document, and no frontier-AI risk taxonomy, that names lab headcount growth rate, hypergrowth, staff turnover or IPO pressure as a risk factor. That covers:
  - the report's primary instruments. The exceptions, which I did not text-search, are CSET's two pieces, GovAI's RSP v3 analysis, FLI Winter 2025 and the VCT paper. Hacker et al. was searched, with 0 relevant hits;
  - the bodies the report lists as not covered;
  - a full-text scan of all 2,574 rows of the MIT AI Risk Repository database (75 source documents).

  §3 gives the search record. My confidence in this narrower statement is about 90% for the set searched. The residual doubt is mostly about documents I could not text-search: the HAIP questionnaire, ISO/IEC 42001/23894, anything from the Canadian institute, and non-English sources.
- **"Factor" is doing a lot of work too.** The coordinator's lens (factor vs. trigger vs. mitigation) is the right one, and it needs a fourth category, *indicator*. The AI-specific literature does touch growth, turnover and investors, but never in the "factor" slot:

| Role | What it means | AI-specific instances found | Non-AI instances |
| --- | --- | --- | --- |
| **Factor** (a condition that raises likelihood or severity) | named as a cause | **Industry-level** growth only: IASR 2025, "rapid growth and consolidation in the AI industry" → firms "more inclined to … cut corners".[^iasr25c] No lab-internal growth, turnover or IPO factor. | ICAO 9.5.5.1–2 (expansion); CSB (turnover; "little organizational stability"); HSE (key-personnel changes, M&A) |
| **Trigger** (a change that must prompt review) | a dynamic that re-opens assessment | RAND-SL3 PS-1: review personnel-security policy after "significant changes to … organizational structure";[^sl3ps1] Gomez et al.: ad hoc audit "when rapid organizational change introduces risks";[^gomez] EU-CoP Measure 1.3 (only by interpretation; see §4.4) | ICAO 9.5.5.5 ("significant changes in staffing levels"); CSB R9 ("changes in staffing levels or staff experience"); IAEA GSR Part 2 ¶4.13 |
| **Mitigation / control** (scales with or constrains headcount or investors) | the mechanism is implied by a control | RAND-W: security team ≥ "two dozen people or 5 percent of organization headcount" (SL3), "vetting of investors" (SL4);[^randw] EU-CoP App. 4.3(4) access-count limit; RAND-ISL offboarding and former-employee controls;[^isl] CA AG MOU (stockholder interests excluded from safety decisions)[^mou] | NPSA pre-employment screening "as your workforce grows" |
| **Indicator** (observable evidence of a latent condition) | turnover as a symptom | FLI AI Safety Index: "departures linked to safety governance"; "High turnover on the safety team" cited in OpenAI's grade[^fli25] | ICAO 8.5.3.8(c) uses turnover as a regulator risk-profile input |

**What this means for the report.** The honest claim is about a *transfer gap*, not an unrecognized mechanism. Other safety-regulated industries already treat organisational change, including growth and turnover, as a hazard source. AI instruments have not imported that framing: they regulate the organisation only as a *lever* (governance mitigations), never as a *source* of risk.[^eu-src] The report's proposal (C15, a rate-dependent moderator) is therefore an import of established practice. That is a *stronger* position than claiming novelty, because it comes with precedent language, indicator designs and incident evidence. Texas City is the canonical case: nine plant managers since 1997, and "little organizational stability".[^csb]

**On IPO specifically**, the absence holds in every sector I searched. No regulator names an IPO as a safety risk factor. What exists:
- **A binding instrument that treats investor pressure as something safety decisions must be insulated from:** the California AG's MOU with OpenAI.[^mou]
- **A security benchmark that treats investors as a pressure channel:** RAND-W SL4.[^randw]
- **A lab CEO tying IPO timing to safety.** In September 2026 Altman said that "given everything happening with safety, right now would be an ill-advised moment to go public."[^altman]
- **Commentary that an IPO strains Anthropic's safety mission.**[^san][^axios]
- **An op-ed asking the SEC to address OpenAI's governance ahead of its IPO.**[^aguilar]

That is evidence the concern is live in 2026. It is not evidence that an authoritative body has named it.

---

## 2. What the report currently says, and where each part lands

| Report text | Status | Note |
| --- | --- | --- |
| Exec summary: "No authoritative body names lab headcount growth rate, hypergrowth, turnover or IPO pressure as a risk factor (about 85% confidence…)" | **False as scoped; true if scoped to AI-specific bodies and to the "factor" role** | The 85% has no stated basis; the search set was never named. Replace it with a named search (§5.1). |
| Exec summary: "The search covered 2026 publications." | **Inconsistent** | §4 says "2023–Sep 2026". My search covered 2003–Sep 2026, deliberately including older non-AI regulators. |
| Exec summary: "The 2025–26 instruments operationalize them, but none adds dynamics such as growth or churn." | **Mostly true; one exception** | RAND-SL3 (Aug 2026) adds an organisational-structure *change trigger* (PS-1).[^sl3ps1] It adds no growth or churn *factor*. |
| §4 "Lab growth rate / headcount scaling: No … Closest: RAND-W … EU-CoP App. 4.3(4) … RAND-ISL" | **True for AI; closest items are mitigations, not factors** | The strongest AI-specific anchor is missing: RAND-W's headcount-indexed security-team rule (see `us-security.md` §4(c)). IASR 2025 §3.2.2(C) industry growth should be named and distinguished (`uk.md` §4). |
| §4 "Turnover / key-person risk: No. Closest: CAIS separation of duties" | **Too strong** | Turnover appears as an *indicator* (FLI)[^fli25] and as a *security vector* (RAND-ISL former employees; "employee-departure policies" are a consensus investment area).[^isl] ICAO names key-personnel turnover as a regulator risk-profile factor.[^icao] |
| §4 "IPO / commercial / investor pressure: Commercial yes; IPO no" | **IPO no: holds. Investor pressure: understated** | Add the CA AG MOU ¶8[^mou] and RAND-W SL4 investor vetting.[^randw] Add IPO commentary as live-concern evidence (§1). |
| §4 Interpretation: "The literature treats organizational factors as *static attributes* … None models how fast they degrade under hypergrowth." | **True for AI; false for safety regulation generally** | Management-of-change regimes are precisely models of how controls degrade under organisational change (HSE: effects "can be subtle or delayed eg six months to a year afterwards").[^hse] |
| C15 "Not found (see §4)" | **Needs rewording** | See §5.3. |
| Rec 1: "State plainly that none of them models growth *rate*." | **True, keep; add the precedent** | Add that other regulated industries do, and cite them. |
| Rec 3: "A material change in *how models are developed* includes rapid organizational change" | **Interpretive stretch** | The Code's text is conditional and model-centred (§4.4). `eu.md` §2.9 proposes the adherence prong instead; I agree, and add non-AI precedent wording. |
| Rec 5: "The uncovered Penrose-type mechanism" | **"Uncovered" only within AI instruments** | See §5.4. |

---

## 3. Search record

An absence claim is only as strong as its named search, so here is mine.

**Method.**
- Full-text sources were downloaded and converted with `pdftotext -layout`.
- Each was grepped with one regex (below). Every hit was read in context. Page numbers were pinned from the PDF's own page breaks.
- Web search was used to find candidates, including 2026 material, and to reach the bodies the report did not cover.
- Search-engine summaries were never treated as evidence. Anything cited below was fetched.

**Core regex** (case-insensitive), with synonyms added per source family:

`turnover|headcount|head count|hypergrowth|hyper-growth|rapid(ly)? (growth|growing|expan|scal|hir)|fast[- ]growing|number of (employees|staff)|staff (growth|numbers)|attrition|key[- ]person|\bIPO\b|initial public offering|going public|public offering|investor|shareholder|stockholder|new (hires|employees|staff)|onboard|retention|organi[sz]ational change|reorgani[sz]|departure|brain drain|tenure|hiring`

Family-specific additions:
- Organisational-culture terms: `safety culture|risk culture|organi[sz]ational (risk|culture|factor)`.
- Competition terms: `competitive pressure|commercial pressure|race to the bottom|consolidation|cut corners`.
- For high-hazard regulators: `expan|grow|staffing|key personnel|merger|downsiz`.

### 3.1 AI-specific authoritative, intergovernmental and statutory sources

**Result: no source names lab growth rate, turnover or IPO as a risk factor.** The notable non-factor hits:

| Source (bibkey) | Searched | Result |
| --- | --- | --- |
| IASR 2025 full report (`bengio-2025-international`) | full text | **Industry** growth as a factor, §3.2.2(C) p.176.[^iasr25c] Organisational culture and incentives, p.165. Talent "recruitment and retention" as a cost barrier (`uk.md`). |
| IASR 2025 Key Updates, Oct and Nov 2025 (`bengio-2025-iasr-key-update-1`, `-2`) | full text | 0 hits |
| IASR 2026 full report (`bengio-2026-international`) | full text + glossary | Competitive pressure, p.97. "Organisational culture, leadership structure, and incentives", p.114. Glossary defines "Risk factors" and "Systemic risks" (§6). No growth, turnover or IPO. |
| EU GPAI CoP, S&S chapter (`eu-cop-2025-safety-security`) | full text (EU agent's copy) | Measure 1.3 grounds, p.9. Measure 8.3 risk-culture indicators, p.25. App. 4.3(4) access count. No growth or turnover. The App. 1.3 risk-source taxonomy has no organisational source at all (`eu.md` §3.1). |
| UK DSIT *Emerging processes for frontier AI safety* (Oct 2023) (`dsit-2023-emerging-processes`) | full text | Personnel security and insider risk. Points developers to NPSA/NCSC "Secure Innovation" guidance, p.26. No growth factor. |
| UK DSIT *Capabilities and risks* + Annexes; AISI Trends; AISI agenda; NCSC | full text (UK agent's copies) | No lab-internal growth, turnover or IPO (`uk.md` §4) |
| NIST AI 100-1 (AI RMF 1.0) (`nist-2023-ai-rmf`) | full text | "managing organizational change" appears only as a generic RMF-profile use case (p.35). No factor. |
| NIST AI 600-1; NIST AI 800-1 2pd (`nist-2025-managing`) | full text | 0 relevant hits. 800-1's "headcount requirements" refers to a *malicious actor's* operational barrier. |
| DHS *Roles and Responsibilities Framework for AI in Critical Infrastructure* (Nov 2024) (`dhs-2024-ai-roles-framework`) | full text | "culture of safety, security, and accountability". No growth or turnover. |
| UN HLAB *Governing AI for Humanity* (Sep 2024) (`unhlab-2024-governing`) | full text | 0 relevant hits |
| OECD *Assessing potential future AI risks…* (Nov 2024) (`oecd-2024-future-ai-risks`) | full text | 0 relevant hits |
| OECD HAIP Reporting Framework | **questionnaire text not obtained** (only a 4-page explainer) | not searched; open gap |
| Japan AISI *National Status Report 2025* (`jaisi-2025-national-status`) | full text | 0 relevant hits |
| Canadian AISI | web search only | no relevant document found; open gap |
| California SB 53 (chaptered text, leginfo) | full text | "Frontier AI framework" = "technical and organizational protocols" (§22757.11(g)). Size enters only as a scope threshold ($500M revenue, §22757.11(j)). No growth, turnover or IPO. |
| California Report on Frontier AI Policy (Jun 2025) (`bommasani-2025-california`) | full text | **Headcount appears only as a regulatory scoping variable, and the report cautions against using it**: Anthropic, OpenAI and xAI "may be relatively small according to some conventional metrics of businesses (e.g., head count)" (§5.1, PDF p.39). Level, not rate. |
| NY RAISE Act; Illinois SB 315 | METR's regulatory digest only [F] | METR reports no headcount, investor, IPO or org-change provisions.[^metr-regs] Statute text not searched. |
| International Network / Singapore Consensus 2025 & 2026 (`ecosystem-2025-singapore`, `ecosystem-2026-2026`) | full text | "organizational risk management" as a research area. No growth or turnover. |
| RAND-W, RAND-SL3, RAND-ISL, AISP (US agent's copies) | full text | Mitigations and triggers only (`us-security.md` §4). Key items quoted in §4.1 below. |

### 3.2 Industry bodies, evaluators and NGO indices (the report's "not covered" list, plus neighbours)

| Source | Searched | Result |
| --- | --- | --- |
| Frontier Model Forum: *Foundational Security Practices* (Jul 2024), *Components of Frontier AI Safety Frameworks* (Nov 2024) | web pages [F] | Insider-threat controls ("Firm personnel can pose threats…"); framework-update triggers. No growth, turnover or investor content. |
| METR *Common Elements of Frontier AI Safety Policies* (Dec 2025; 12 company frameworks) (`metr-2025-common-elements`) | full text | 0 relevant hits. This is the best evidence that **no lab's own safety framework** names growth or turnover. |
| Apollo *AI Behind Closed Doors* (internal deployment) (`stix-2025-behind`) | full text | Insider threat; access scoping by employee subsets. No growth. |
| Epoch AI | data + one analysis [F] | **Data, not a risk claim.** Epoch keeps a staff-count dataset (`ai_companies_staff_reports.csv`, 48 records). Its Mar 2026 job-postings analysis found research "now makes up only 12% of open roles at Anthropic and only 7% at OpenAI", while go-to-market rose from 17% to 31% and from 18% to 28%.[^epoch] Useful for indicators (§5.4), silent on safety. |
| FLI AI Safety Index, Summer 2025 (`fli-2025-ai-safety-index-summer`), Summer 2026 (`fli-2026-ai-safety-index-summer`) | full text | **Turnover as indicator**[^fli25] and a structure-and-mandate indicator on shareholder pressure. No growth or IPO factor. |
| SaferAI: *Frontier AI Risk Management Framework* (`campos-2025-frontier`), *Evaluating … Frameworks* (`stelling-2025-evaluating`) | full text | 0 relevant hits |
| MIT AI Risk Repository **database v4** (updated 3 Dec 2025; 2,574 rows from 75 documents; CC BY 4.0; [sheet](https://docs.google.com/spreadsheets/d/15LeHcpeuZC9txkvcaMoh3sUhkMvdMMry69xxXL46DT0)) | every row's category, subcategory, description and evidence fields | 17 regex hits, none on point. Hits include the CAIS "Organizational Risks" rows, labour-market "job turnover", environmental "rapid growth" of compute, and fiduciary duties "towards shareholders" (Gabriel 2024, re AI assistants). **No row names lab growth, internal turnover or IPO.** This is the closest thing to a full-corpus search of risk taxonomies that exists. |
| CAIS *Overview of Catastrophic AI Risks* (`hendrycks-2023-overview`) | full text | Organisational risks are framed statically (safety culture, HROs, the Swiss-cheese model). No growth or turnover. |

### 3.3 Academic and near-AI governance papers

| Source | Result |
| --- | --- |
| Gomez et al., *How frontier AI companies could implement an internal audit function* (Dec 2025) (`gomez-2025-frontier`) | **Closest AI-specific "trigger"**: ad hoc reviews "when rapid organizational change introduces risks not anticipated during planning" (p.11). It also attributes to Schuett (2024) the challenge of "preserving genuine independence within fast-moving, founder-led organizations" (p.5).[^gomez] I did not find that phrase in Schuett's arXiv 2305.17038 (`schuett-2024-frontier`), which instead frames the "transition from startups to more mature companies" as an opportunity (p.23). The attribution may point to a different Schuett 2024 text. [U] |
| Buhl et al., *Safety cases for frontier AI* (`buhl-2024-safety`); *Emerging Practices in Frontier AI Safety Frameworks* (`buhl-2025-emerging`); Kierans et al., *Catastrophic Liability* (`kierans-2025-catastrophic`); Mylius, *STPA for frontier AI* (`mylius-2025-systematic`); Brundage et al., *Frontier AI Auditing* (`brundage-2026-frontier`); Zhu et al., *Silent Revision* (`zhu-2026-silent`) | 0 relevant hits. The last is relevant to the sibling hypergrowth report's commitment-churn layer, not to this claim. |
| Organisational sociology (Baron, Hannan & Burton 2001; Hannan, Burton & Baron 1996; Amburgey, Kelly & Barnett 1993) | Already verified in the sibling report `safety-and-hypergrowth.md`. **These are the academic "factor" literature** for growth, change and turnover in young high-tech firms. They are not AI-specific and not "authoritative bodies". |

### 3.4 Non-AI regulators and security authorities (added because the report's phrase has no AI qualifier)

| Source (bibkey) | Searched | Result |
| --- | --- | --- |
| ICAO Doc 9859 *Safety Management Manual*, 4th ed. (2018, advance unedited) (`icao-2018-doc9859-smm`) | full text | **Factor + trigger + regulator risk-profile.**[^icao] |
| UK HSE CHIS7 *Organisational change and major accident hazards* (2003) (`hse-2003-chis7`) | full text | **Factor + trigger**; key personnel, M&A, downsizing, staffing levels; delayed effects.[^hse] |
| US CSB *BP Texas City* final report (2007) (`csb-2007-bp-texas-city`) | full text | **Incident evidence + recommendation**: leadership turnover; R9 on staffing levels and staff experience.[^csb] |
| IAEA GSR Part 2 *Leadership and Management for Safety* (2016) (`iaea-2016-gsr-part2`) | full text | **Requirement**: identify and analyse "organizational changes and the cumulative effects of minor changes".[^iaea] |
| UK NPSA/NCSC *Secure Innovation* (2024 booklet) (`npsa-2024-secure-innovation`) | full text | **Team growth changes security risk.**[^npsa] |
| CISA *Insider Threat Mitigation Guide*, 2026 ed. (Sep 2026) (`cisa-2026-insider-threat-guide`) | full text | **Organisational indicators** including M&A, overwork, under-trained staff.[^cisa] |

### 3.5 IPO and investor pressure (2025–26 news and commentary)

| Source | Result |
| --- | --- |
| California AG–OpenAI MOU (27 Oct 2025) (`caag-2025-openai-mou`) | Binding exclusion of "the pecuniary interests of stockholders" from safety and security decisions.[^mou] |
| Fortune, 12 Sep 2026 | Altman rules out a 2026 IPO, citing safety.[^altman] |
| Axios (via Yahoo), 14 Sep 2026 | Anthropic IPO likely in 2026. Frames the public-company "transparency" argument.[^axios] |
| Straight Arrow News, 1 Jun 2026 [commentary] | IPO puts Anthropic's safety mission "under new pressure".[^san] |
| Fortune op-ed (Aguilar & Bracy), 22 Jul 2026 [commentary] | Asks the SEC to address OpenAI's governance ahead of its IPO.[^aguilar] |
| Crypto Briefing / Bitget, "California intervenes in OpenAI's IPO" | **Misleading headline.** It restates the Oct 2025 MOU and cites no new AG action [F]. Do not cite it. |
| TechTimes, 5 Aug 2026 | Reports Amodei's concern about mission dilution in hiring (via Axios, 3 Aug 2026).[^techtimes] |

### 3.6 What I did not search

- ISO/IEC 42001 and 23894 (paywalled).
- The HAIP questionnaire.
- Canadian institute documents.
- Non-English sources.
- The EU AI Office's non-CoP guidance, beyond what `eu.md` covers.
- Company S-1s. Anthropic's is confidential; no public prospectus was found as of 27 Sep 2026.
- AI Lab Watch's "2024 OpenAI departures" tracker (seen in search results, not fetched).
- Kokotajlo's reported "about 30 → about 16" AGI-safety staff count (search summary only). [U]

---

## 4. Evidence detail

### 4.1 AI-specific: what comes closest, by role

- **Industry growth as a factor (IASR 2025).** "C. The rapid growth and consolidation in the AI industry raises concerns about certain AI companies becoming particularly powerful because critical sectors in society are dependent on their products. Such companies may become more inclined to take excessive risks or cut corners on safety standards if they expect that it would be costly for governments to let the company fail."[^iasr25c] The mechanism is moral hazard ("too big to fail"). It is not absorptive capacity. This is the only authoritative AI document I found that names *growth* in the factor slot, and it is about the industry, not about headcount.
- **Headcount-indexed mitigation (RAND-W, SL3).** Security team capacity "of at least two dozen people or 5 percent of organization headcount, whichever is larger" (p.85). This is the strongest AI-specific evidence that headcount *matters*: the control is defined to grow with the organisation. It does not say growth is a risk. It makes growth a *cost*.[^randw]
- **Investor channel (RAND-W, SL4).** "Vetting of investors and other positions of influence. Investors are thoroughly vetted to prevent inappropriate pressure undermining the security of the organization's assets." (p.90)[^randw] In RAND-ISL, "Organizational Leverage Attacks" covers adversaries building "financial or legal leverage over an organization through investments or grants" (p.44).[^isl] These are hostile-investor channels, not market or IPO pressure.
- **Organisational-change trigger (RAND-SL3, PS-1).** "Review and update policies and procedures at an organization-defined frequency and following personnel security incidents or significant changes to model weight infrastructure, access patterns, or organizational structure."[^sl3ps1] This is the one AI-specific instrument with a change trigger that growth would plausibly pull. The same report's executive summary names "balancing security with operational velocity" among the most severe barriers (p.v), and on p.15 notes that fragmented ownership is "particularly severe in startups where personnel may have multiple roles and responsibilities."
- **Turnover as a security vector (RAND-ISL).**
  - Experts agreed that "personnel security measures, behavioral monitoring, and employee-departure policies represent critical areas of investment" (p.27).
  - "Former employees present a risk because of the information they possess … insights exist substantially as knowledge in researchers' minds" (p.44).[^isl]

  Turnover here is an *exfiltration* channel. Growth multiplies the number of future former employees; that last step is my inference.
- **Turnover as an evidence indicator (FLI).**
  - FLI's "Reporting Culture & Whistleblowing Track Record" indicator draws evidence from "(vi) departures linked to safety governance".
  - Its Summer 2025 grade for OpenAI cites "High turnover on the safety team" as "an indication of a concerning shift in priorities".[^fli25]

  FLI is an NGO index, not an authoritative body. It treats turnover as a *symptom* of culture, not a *cause* of risk.
- **Investor pressure insulated by a binding instrument (California AG MOU).** The PBC certificate must require the board "to consider only the Mission (and may not consider the pecuniary interests of stockholders or any other interest) in respect of safety and security issues related to the OpenAI enterprise" (¶8, p.3). The Safety and Security Committee sits in the nonprofit and can require mitigations "up to and including halting the release of models" (¶¶9–11).[^mou] It never says "risk factor". But this is a state regulator writing investor pressure out of safety decisions, which is stronger than any "commercial pressure" row in the report.
- **Change trigger in the AI-governance literature (Gomez et al.).** Ad hoc internal-audit reviews "are appropriate when an area encounters an unexpected shock … or when rapid organizational change introduces risks not anticipated during planning" (p.11).[^gomez]
- **Headcount as a scoping variable (California Report).** Headcount appears only in the scope discussion, and the Working Group cautions against it.[^carpt]

### 4.2 Outside AI: the factor is established

- **ICAO Doc 9859 (4th ed.)**, §9.5.5 "The management of change"[^icao]:
  - §9.5.5.1: "Service providers experience change due to a number of factors including, but not limited to: a) organizational expansion or contraction; …"
  - §9.5.5.2: "Change may affect the effectiveness of existing safety risk controls. In addition, new hazards, and related safety risks may be inadvertently introduced into an operation when change occurs."
  - §9.5.5.5 lists changes that should trigger formal change management, including "c) changes in key personnel; d) significant changes in staffing levels; … f) significant restructuring of the organization".
  - §8.5.3.8, on how a *State regulator* can profile service providers to set surveillance intensity, lists "b) number of years in operation; c) turnover rate of the key personnel such as the accountable executive and safety manager".

  That last item is the closest analogue anywhere to what the report wants AISI to do: a regulator using organisational age and key-person turnover as risk-profile inputs.
- **UK HSE CHIS7 (2003).**[^hse]
  - The listed changes include "staffing levels", "mergers, de-mergers and acquisitions", "downsizing" and "changes to key personnel" (p.1).
  - The Hickson & Welch fire killed five; "Because of a recent company reorganisation, the cleaning task had been organised by inexperienced team leaders reporting to an overworked area manager" (p.1).
  - On knowledge loss: "One danger that is easy to overlook is the loss to the business of informal knowledge and processes" (p.5).
  - On timing: "the effects of change can be subtle or delayed eg six months to a year afterwards" (p.6). This bears directly on the sibling report's 6-month window.
  - **Caveat:** HSE's list is contraction-heavy. It does not say "growth" or "rapid hiring"; expansion enters via "staffing levels" and "staff disposition".
- **US CSB, BP Texas City (2007).**[^csb]
  - "The Baker Panel Report concluded that Texas City refinery senior leadership turnover had been high with nine plant managers since 1997; five from 2001 to 2003" (pp.192–193).
  - A consultant's pre-incident assessment: "We have never seen an organization with such a history of leadership changes over such short period of time … there has been little organizational stability. This makes the management of protection very difficult" (p.193).
  - Recommendation 2005-4-I-TX-R9, to OSHA: require MOC review "for organizational changes that may impact process safety including a. major organizational changes such as mergers, acquisitions, or reorganizations; b. personnel changes, including changes in staffing levels or staff experience; and c. policy changes such as budget cutting" (p.213).
- **IAEA GSR Part 2 (2016)**, ¶4.13, a Safety *Requirement*: "Provision shall be made in the management system to identify any changes (including organizational changes and the cumulative effects of minor changes) that could have significant implications for safety and to ensure that they are appropriately analysed" (p.10).[^iaea]
- **UK NPSA/NCSC Secure Innovation (2024).**[^npsa]
  - On reviewing risks: "As your company continues to evolve, so too should your security measures. The risks you face may well have changed, for example because your team has grown, you have moved to more or larger premises, you are collaborating with more partners, or because you are looking for investment." (p.26)
  - "As your workforce grows, you may no longer be able to rely primarily on personal relationships to ensure trust. Fostering a positive security culture is even more important." (p.30)

  The UK's frontier-AI processes paper routes developers to this guidance: "Secure Innovation guidance from NCSC and NPSA is available to help companies and investors to protect their technology" (p.26).[^dsit-ep] So there is a documentary chain from UK frontier-AI guidance to a UK authority that names team growth as a risk changer. It is thin but real.
- **CISA Insider Threat Mitigation Guide (Sep 2026).**[^cisa]
  - "Organizational Indicator Examples" (p.67) include "High stress environment", "Pattern of overwork", "Heightened uncertainty, either financial or contractual", "Recent merger/acquisition" and "Under-trained staff (particularly in cybersecurity)".
  - Professional stressors (p.63) include "Loss of seniority or status in merger or acquisition".

  DHS was on the report's "not covered" list; this is its most relevant document.

### 4.3 First-party lab statements and commentary (live-concern evidence, not authority)

- **Altman, 12 Sep 2026:** "I actually think that, given everything happening with safety, right now would be an ill-advised moment to go public." [F][^altman]
- **Anthropic, 2023.** The Long-Term Benefit Trust rationale names first-to-market pressure: the LTBT "can ensure that the organizational leadership is incentivized to carefully evaluate future models for catastrophic risks … rather than prioritizing being the first to market above all other objectives." It adds that externalities grow as the company "becomes more mature". [F][^ltbt]
- **Amodei.** In Feb 2026 he said: "I probably spend a third, maybe 40%, of my time making sure the culture of Anthropic is good" (Dwarkesh Podcast, as quoted by TechTimes). Axios (3 Aug 2026, via TechTimes) reported his concern "that new talent is joining for the money rather than the mission". TechTimes adds its own inference that screening via "interpersonal familiarity and founder networks has fallen sharply" as headcount passed 2,500; that is the writer's claim, not Amodei's. [F][^techtimes]
- **Aschenbrenner (Jun 2024)** [commentary]: "Between the labs, there are thousands of people with access to the most important secrets; there is basically no background-checking, silo'ing, controls, basic infosec, etc." [F][^leopold]
- **SAN, 1 Jun 2026** [commentary]: "An IPO would likely compel the company to choose between prioritizing shareholder interests over its current mission and implementing a dual-class share structure." [F][^san] This is questionable as stated: public benefit corporations can list, so the dichotomy is the writer's.

### 4.4 Recommendation 3 (the EU-CoP Measure 1.3 hook) against the text

Measure 1.3 (p.9) says Signatories reassess "if they have reasonable grounds to believe that the adequacy of their Framework and/or their adherence thereto has been or will be materially undermined". The first example ground is: "(1) how the Signatories develop models will change materially, which can be reasonably foreseen to lead to the systemic risks stemming from at least one of their models not being acceptable".

- Ground (1) is about *model development*, and it is conditional on foreseeably unacceptable risk. Reading "rapid organizational change" into it is a proposal, not the Code's meaning.
- `eu.md` §2.9 recommends the **adherence prong** instead, and I agree. The strongest external support for that reading is non-AI regulatory wording that does exactly what the report wants:
  - ICAO §9.5.5.5(d), "significant changes in staffing levels";
  - CSB R9(b), "changes in staffing levels or staff experience";
  - RAND-SL3 PS-1, "significant changes to … organizational structure".

---

## 5. Proposed replacement text

The drafts keep the report's voice and tags. Footnote labels are mine (`[^abs-…]`); renumber as you integrate.

### 5.1 Executive-summary bullet (replaces lines 27–28)

> - **No AI-specific authoritative body we searched names lab growth rate, headcount scaling, staff turnover or IPO pressure as a risk *factor*.**
>   - The search covered: the IASR 2025 and 2026 reports and their Key Updates; the EU Code; the UK DSIT, AISI and NCSC documents; NIST AI 100-1, 600-1 and 800-1; the DHS/CISA guidance; the UN HLAB; the OECD; Japan's AISI; California SB 53 and the California Report; the FMF, METR, Apollo, FLI, SaferAI and Epoch; and all 2,574 rows of the MIT AI Risk Repository. The search record is in `verification/absence-claim.md`.
>   - These dynamics appear only in other roles:
>     - as mitigations that scale with headcount or investors: RAND sizes the security team at "5 percent of organization headcount" and requires "vetting of investors";[^abs-randw]
>     - as a change trigger: RAND-SL3 reviews personnel-security policy after "significant changes to … organizational structure";[^abs-sl3]
>     - as an indicator: FLI scores "departures linked to safety governance";[^abs-fli]
>     - as a binding safeguard: California's MOU bars OpenAI's board from weighing "the pecuniary interests of stockholders" on safety and security decisions.[^abs-mou]
>   - Only *industry-level* growth is named as a factor, in IASR 2025: "rapid growth and consolidation" may make firms "more inclined to … cut corners."[^abs-iasr25]
> - **Outside AI, this factor is established.** Aviation, major-hazard and nuclear regulators require management of *organisational* change:
>   - ICAO names "organizational expansion or contraction" and "significant changes in staffing levels", and profiles operators by key-personnel "turnover rate".[^abs-icao]
>   - UK HSE, the US CSB (after Texas City) and the IAEA do likewise.[^abs-hse][^abs-csb][^abs-iaea]
>   - UK NPSA/NCSC tell growing tech firms their risks change "because your team has grown."[^abs-npsa]
>
>   The gap is one of transfer into AI instruments, not an unrecognised mechanism.
> - **IPO pressure is named by no authoritative body in any sector.** It is a live 2026 concern in lab-leader statements and commentary.[^abs-altman][^abs-san]

If a shorter bullet is wanted, the first sentence of each bullet plus the parenthetical search list carries the claim honestly.

### 5.2 §4 table: revised rows

| Factor | Named? | Evidence |
| --- | --- | --- |
| **Lab growth rate / headcount scaling** | **Not as a factor in any AI-specific source searched.** Present as mitigations and one change trigger. Named as a factor by non-AI safety regulators. | *AI, mitigation:* RAND-W sizes the SL3 security team at ≥ "two dozen people or 5 percent of organization headcount";[^abs-randw] EU-CoP App. 4.3(4) caps parameter-access headcount;[^2] RAND-ISL's human-centred attack surface.[^19] *AI, trigger:* RAND-SL3 PS-1 ("significant changes to … organizational structure");[^abs-sl3] Gomez et al. (ad hoc audit on "rapid organizational change").[^abs-gomez] *AI, industry level:* IASR 2025 §3.2.2(C).[^abs-iasr25] *Non-AI:* ICAO §9.5.5 ("organizational expansion or contraction"; "significant changes in staffing levels");[^abs-icao] NPSA/NCSC ("because your team has grown").[^abs-npsa] |
| **Turnover / key-person risk** | **Not as a factor in AI sources.** Present as an indicator (FLI) and a security vector (RAND-ISL). Named as a regulator risk-profile factor in aviation. | FLI: "departures linked to safety governance"; OpenAI's "High turnover on the safety team";[^abs-fli] RAND-ISL: "Former employees present a risk…" and "employee-departure policies" are a consensus investment area;[^abs-isl] ICAO §8.5.3.8(c): "turnover rate of the key personnel";[^abs-icao] CSB Texas City: "nine plant managers since 1997".[^abs-csb] |
| **Commercial / investor / IPO pressure** | **Commercial: yes. Investor: operationalised (binding in one case). IPO: no.** | Commercial: IASR 2026 p.97;[^4] FLI structure indicator.[^30] Investor: California AG–OpenAI MOU ¶8;[^abs-mou] RAND-W SL4 "vetting of investors".[^abs-randw] IPO: no body. Commentary and lab statements only.[^abs-altman][^abs-san][^abs-aguilar] |
| **Organisational change (general)** *(new row)* | **AI: triggers only. Non-AI: required.** | RAND-SL3 PS-1;[^abs-sl3] EU-CoP Measure 1.3 (adherence prong, by interpretation);[^2] IAEA GSR Part 2 ¶4.13;[^abs-iaea] HSE CHIS7;[^abs-hse] CSB R9.[^abs-csb] |

**Interpretation paragraph (replacement):**

> AI-specific instruments treat organisational factors as *static attributes* and as *levers* (culture, structure, resourcing, access control). None names the organisation's own rate of change as a *source* of risk; the EU Code's risk-source taxonomy contains no organisational source at all. Growth enters only through controls that must scale with it. Other safety-regulated industries have long treated organisational change, including expansion, staffing levels and key-personnel turnover, as a hazard source requiring management of change, with delayed effects "six months to a year afterwards".[^abs-hse] A growth or absorptive-capacity factor is therefore best framed as an **import of established management-of-change practice**: a moderator of C6–C9 and B7–B8, not a new hazard. That framing comes with precedent wording, indicator designs and incident evidence. The one AI-specific foothold is RAND-SL3's organisational-structure change trigger.[^abs-sl3] *(Inference, labelled: that people-count controls "scale worse" under rapid growth is this report's reasoning. The sources supply the ingredients, not the conclusion; see `us-security.md` §4(d).)*

### 5.3 Row C15

> | C15 | Lab growth rate, headcount scaling, turnover, IPO pressure | **Not named as a factor in AI instruments** (§4). Mitigation-side: RAND-W, RAND-SL3, EU-CoP App. 4.3(4). Indicator: FLI. Investor safeguard: CA AG MOU. **Factor-side precedent outside AI:** ICAO, HSE, CSB, IAEA, NPSA. |

### 5.4 Recommendations

- **Rec 1.** Keep "State plainly that none of them models growth *rate*." Add: "…and anchor the proposal in management-of-change regimes that do: ICAO Doc 9859 §9.5.5, HSE CHIS7, CSB R9 and IAEA GSR Part 2 ¶4.13. Cite RAND-SL3 PS-1 as the one AI-specific precedent."[^abs-icao][^abs-hse][^abs-csb][^abs-iaea][^abs-sl3]
- **Rec 2 (indicators).** Give each indicator its precedent, and distinguish level caps from growth indicators:
  - **Year-on-year growth in privileged-access headcount.** EU-CoP App. 4.3(4) is a *level* limit; growth is the proposal (see `eu.md` for the narrower access scope).
  - **Security-team size as a share of headcount.** Precedent: RAND-W SL3 (≥ 5% or 24).[^abs-randw]
  - **Key-person turnover rate for risk-owning roles.** Precedent: ICAO §8.5.3.8(c), turnover of the accountable executive and safety manager.[^abs-icao] This replaces "tenure of risk-owning staff (Measure 8.1)": Measure 8.1 allocates responsibilities but says nothing about tenure.
  - **Composition of hiring:** research and safety vs. go-to-market share of open roles. Data exists: Epoch, Mar 2026.[^abs-epoch]
  - **Safety staff share.** Keep, with the CAIS benchmark.
  - **Anonymous-survey trends.** Measure 8.3(4); keep.
  - **Departures linked to safety governance.** Precedent: FLI indicator (vi).[^abs-fli]
- **Rec 3.** Recast it as a proposed reading, and quote Measure 1.3's text. Prefer the adherence prong (per `eu.md` §2.9). Offer non-AI trigger wording ("significant changes in staffing levels"; "changes in staffing levels or staff experience") as model language.
- **Rec 4.** No change from this verification.
- **Rec 5.** Replace "The uncovered Penrose-type mechanism" with "The mechanism uncovered *in AI instruments*, though standard in management-of-change regulation elsewhere, …". Keep the incentive/capacity separation: it is sound, and ICAO's own list separates financial health (8.5.3.8(a)) from key-personnel turnover (c).

### 5.5 "Not covered" line (§1)

> **Not covered in the original pass; since searched for the growth/turnover/IPO claim only:** FMF (two issue briefs), METR (Common Elements, Dec 2025), Apollo (internal deployment), Epoch (staff data, job postings), DHS/CISA, UN HLAB, OECD (2024 future-risks report), Japan AISI (2025 status report). **Still not covered:** the OECD HAIP questionnaire, the Canadian AISI, ISO/IEC 42001/23894, company frameworks except through METR's synthesis.

### 5.6 Caveats (add)

> - **"Authoritative body" scope.** The absence claims in this report are scoped to AI-specific bodies. Non-AI safety regulators (ICAO, HSE, CSB, IAEA) and security authorities (NPSA/NCSC, CISA) do name organisational change, staffing and turnover.
> - **Factor, trigger, mitigation, indicator.** "Named?" in §4 refers to the *factor* role. Mitigations that scale with a variable are evidence that the variable matters, not that a body has named it as a risk.

---

## 6. Definitions met (for the phase-2 terminology map)

Verbatim, with location. The collisions are noted, because Joseph suspected pooling across senses, and it shows up here.

- **Risk factor.** IASR 2026 glossary (p.153): "Risk factors: Properties or conditions that can increase the likelihood or severity of harm. In AI, for example, poor cybersecurity is a risk factor that could make it easier for malicious actors to obtain and misuse an AI system." *By this definition, growth or turnover could qualify. The report never defines "risk factor" and should adopt this.*
- **Systemic risk source.** EU-CoP glossary (p.33, per `eu.md` §3.1): "a factor which alone or in combination with other factors might give rise to systemic risk".
  - In practice the EU enumerates only *model-level* sources.
- **Systemic risks.** IASR 2026 glossary (p.154): "Risks that arise from how AI development and deployment changes human behaviour, organisational practices, or societal structures, rather than directly from AI capabilities." It then adds a note: "(Note that this is different from how 'systemic risk' is defined by the AI Act of the European Union. There, the term refers to 'risk that is specific to the high-impact capabilities of general-purpose AI models, having a significant impact'.)"
  - **Direct collision.** Under IASR's sense, organisational change is a *source* of systemic risk. Under the EU's sense, organisational matters sit only among the mitigations.
- **Risk.** IASR 2026 (p.153): "The combination of the probability and severity of a harm."
- **Hazard.** IASR 2026 (p.150): "Any event or activity that has the potential to cause harm, such as loss of life or injury."
- **Race to the bottom.** IASR 2026 (p.153): "A situation where competition drives actors to progressively reduce safety precautions, quality standards, or oversight to gain an advantage."
- **Loss of control scenario.** IASR 2026 (p.151): "A scenario in which one or more general-purpose AI systems come to operate outside of anyone's control, with no clear path to regaining control."
- **Misalignment.** IASR 2026 (p.151): "An AI's propensity to use its capabilities in ways that conflict with human intentions, values, or norms. Depending on the context, this can refer to the intentions and values of various entities, such as developers, users, specific communities, or society as a whole."
  - Contrast GDM's narrower "knowingly causes harm against the intent of the developer" (report fn 26).
- **Healthy risk culture.** EU-CoP Measure 8.3 (p.25) gives no definition. It gives seven "indicators", for example "(4) anonymous surveys find that staff are comfortable raising concerns about systemic risks…".
  - Contrast CAIS's "safety culture" (HRO-derived) and FLI's "Reporting Culture". These are three different constructs sharing one row (C6).
- **Organisational change (enumerated definitions).**
  - HSE CHIS7 (p.1): "changes to roles and responsibilities, organisational structure, staffing levels, staff disposition or any other change that may directly or indirectly affect the control of the hazard".
  - CSB R9 (p.213): (a) "major organizational changes such as mergers, acquisitions, or reorganizations", (b) "personnel changes, including changes in staffing levels or staff experience", (c) "policy changes such as budget cutting".
  - IAEA ¶4.13: "organizational changes and the cumulative effects of minor changes".
- **Frontier AI framework.** California SB 53 §22757.11(g): "documented technical and organizational protocols to manage, assess, and mitigate catastrophic risks." Compare IASR 2026's "Frontier AI Safety Framework" (p.150): "A set of protocols created by an AI developer, typically structured as if-then commitments, that specifies safety or security measures that they will take when their AI systems reach predefined thresholds." SB 53 includes the *organisational*; IASR's is threshold-centred.
- **Insider threat (as threat class).** RAND-SL3 report, OC3 row: "Hacker groups, terrorist organizations, industrial espionage organizations and disgruntled employees (insider threats)" (p.2; PDF p.10).
  - The EU-CoP glossary definition is in `eu.md`.
  - Note that the report's B8 pools human insiders with AI self-exfiltration (`us-security.md` item 5).

---

## 7. New references worth adding to the report

In priority order for the growth/C15 argument:
1. ICAO Doc 9859, 4th ed. (`icao-2018-doc9859-smm`): the cleanest factor + trigger + regulator-profile precedent.
2. US CSB, BP Texas City final report (`csb-2007-bp-texas-city`): incident evidence and recommendation wording.
3. UK HSE CHIS7 (`hse-2003-chis7`): a UK authority, with the delayed-effects point.
4. UK NPSA/NCSC Secure Innovation (`npsa-2024-secure-innovation`) + DSIT Emerging Processes (`dsit-2023-emerging-processes`): the UK chain linking team growth to frontier AI.
5. California AG–OpenAI MOU (`caag-2025-openai-mou`): binding investor-pressure safeguard.
6. IASR 2025 §3.2.2(C) (`bengio-2025-international`): industry-growth factor. Already in the report, but not for this.
7. FLI Summer 2025 (`fli-2025-ai-safety-index-summer`): the turnover indicator.
8. RAND-SL3 Appendix B PS-1 (`aguirre-2026-sl3`) and RAND-W p.85/p.90 (`nevo-2024-securing`).
9. IAEA GSR Part 2 (`iaea-2016-gsr-part2`); CISA 2026 guide (`cisa-2026-insider-threat-guide`).
10. Gomez et al. 2025 (`gomez-2025-frontier`); Epoch job postings (web); METR Common Elements (`metr-2025-common-elements`) as the negative result for company frameworks.

---

## 8. Bibkeys I created in relata

- **Created with PDF attached:**
  - `hse-2003-chis7`, `csb-2007-bp-texas-city`, `iaea-2016-gsr-part2`, `icao-2018-doc9859-smm`
  - `cisa-2026-insider-threat-guide`, `npsa-2024-secure-innovation`, `dsit-2023-emerging-processes`, `caag-2025-openai-mou`
  - `fli-2025-ai-safety-index-summer`, `oecd-2024-future-ai-risks`, `metr-2025-common-elements`, `unhlab-2024-governing`
  - `dhs-2024-ai-roles-framework`, `jaisi-2025-national-status`, `nist-2023-ai-rmf`
  - `bengio-2025-iasr-key-update-1`, `bengio-2025-iasr-key-update-2`, `buhl-2025-emerging`
  - `gomez-2025-frontier`, `bommasani-2025-california`, `stix-2025-behind`, `campos-2025-frontier`, `buhl-2024-safety`
  - `kierans-2025-catastrophic`, `mylius-2025-systematic`, `brundage-2026-frontier`, `zhu-2026-silent`
  - `ecosystem-2025-singapore`, `ecosystem-2026-2026`
- **Created by relata's scaffold with poor metadata; needs a fix:**
  - `ecosystem-2025-singapore`: title "The Singapore Consensus on", author "Ecosystem, Secure AI".
  - `ecosystem-2026-2026`: same problem.

  The proper records are arXiv 2506.20702 and 2608.14611. I did not hand-edit the canonical tree.
- **Relied on other agents' keys:** `bengio-2025-international`, `bengio-2026-international`, `eu-cop-2025-safety-security`, `nevo-2024-securing`, `aguirre-2026-sl3`, `brassgershovich-2026-algorithmic`, `gekker-2026-aisp`, `hendrycks-2023-overview`, `schuett-2024-frontier`, `slattery-2026-risk`, `stelling-2025-evaluating`, `fli-2026-ai-safety-index-summer`, `nist-2025-managing`.
- **Not filed (web-only news or commentary; URLs in the footnotes):** Fortune (Altman), Axios, SAN, the Fortune op-ed, TechTimes, Aschenbrenner, Anthropic LTBT post, Epoch analysis, FMF briefs, METR regulations note. Also the MIT database (Google Sheet, not a PDF).

---

## 9. Feedback

**On the report (adjacent to my claim).**
- **"85% confidence" without a named search is the shape of the problem.** The other absence claims in the report ("single-source items", the "—" cells) have the same structure. The crosswalk legend already says "— = not proof of absence"; the same honesty should apply to the executive summary.
- **The report never defines "risk factor",** yet its whole C-section and its positioning rest on it. IASR 2026's glossary definition (§6) is citable and would let §4 say precisely which role (factor, trigger, mitigation, indicator) each piece of evidence plays. That also answers Joseph's factor/mitigation question structurally rather than row by row.
- **C6 pools three constructs:** CAIS "safety culture", EU "healthy risk culture" and FLI "reporting culture". Phase 2 should split them.
- **For Joseph's EOI specifically:** ICAO §8.5.3.8 is a ready-made template for "what a regulator could ask for". Organisational age, key-person turnover and financial health are used there as *surveillance-intensity* inputs. That is concrete, precedented, and not a new theory. It fits his "theory-deficient and poorly scoped" concern: the AI field has been re-deriving organisational safety without the management-of-change layer that other industries learned from Texas City and Hickson & Welch.

**On the brief.** It was clear and let me choose the structure. Two things made the work sharper:
- "An answer either way is useful; a counterexample worth more" licensed the scoping finding.
- The mid-task factor/mitigation lens arrived at the right time.

One thing I would add next time: say explicitly whether "authoritative body" was meant as "AI-specific". I resolved it by reporting both scopes, and I think that is the honest answer anyway.

**On relata (for Joseph or the tool's maintainer).**
- `relata ingest --help` does not print help. It runs a spool drain (it printed `promoted=0 … skipped=355`).
- `relata ingest --retry <file>` retries **the whole spool**, not the named file. On my run it auto-promoted five unrelated items (`aguilera-2021-particular`, `coatleven-2024-large`, `russel-2019-short`, `parr-2022-active-inference`, `wu-2019-learning`) and re-parked others (e.g. `Pearl_2009_Causality.pdf`). All were identifier-grade under relata's own ladder, but they were outside my scope. Worth knowing for multi-agent use.
- The arXiv PDFs for the Singapore Consensus did not resolve to their arXiv records and scaffolded poor titles and authors.
- `relata add` with BibTeX, followed by `ingest`, then attaching by content match, worked well for identifier-less government PDFs.
- Three spool copies (`ca-ag-openai-mou-2025.pdf`, `fli-summer-2025.pdf`, `jaisi-report-2025.pdf`) show as "rejected" in `relata pending`. They are duplicates of PDFs I registered directly with `relata pdf`, not lost documents.

**Scratchpad collision (FYI).** At the start I briefly downloaded arXiv PDFs into `scratchpad/src/`, which the academic/NGO agent was using. I overwrote eight of its PDFs with byte-for-byte re-downloads of the same URLs, then moved my own additions to `scratchpad/absence/`. If that agent saw unexpected PDFs appear in `src/` around 15:32, that was me.

I'm staying on the line for follow-ups.

---

## Footnotes

[^icao]: \[P] ICAO, *Safety Management Manual (SMM)*, Doc 9859, 4th ed. (advance unedited), 2018. Mirror PDF: <https://aviation-insight.aero/wp-content/uploads/2021/05/9859_4th_ed_unedited_en.pdf> (official edition via the ICAO store). §8.5.3.8, p.8-22: States' "organizational safety risk profiles … may include factors such as: a) the financial health of the organization; b) number of years in operation; c) turnover rate of the key personnel such as the accountable executive and safety manager; d) competence and performance of the accountable executive…". §9.5.5.1–9.5.5.2, p.9-21: "Service providers experience change due to a number of factors including, but not limited to: a) organizational expansion or contraction; … Change may affect the effectiveness of existing safety risk controls. In addition, new hazards, and related safety risks may be inadvertently introduced into an operation when change occurs." §9.5.5.5: formal change management triggers include "c) changes in key personnel; d) significant changes in staffing levels; … f) significant restructuring of the organization". relata: `icao-2018-doc9859-smm`. Unedited edition: check the final 4th-edition paragraph numbers before external citation.

[^hse]: \[P] UK Health and Safety Executive, *Organisational change and major accident hazards*, Chemical Information Sheet No. CHIS7, first published 06/2003. <https://www.hse.gov.uk/pubns/chis7.pdf>. p.1: "Changes could include: changes to roles and responsibilities, organisational structure, staffing levels, staff disposition or any other change that may directly or indirectly affect the control of the hazard", with a listed set of change types including "mergers, de-mergers and acquisitions; downsizing; changes to key personnel". p.1 (Hickson & Welch, 1992, five killed): "Because of a recent company reorganisation, the cleaning task had been organised by inexperienced team leaders reporting to an overworked area manager." p.5: "One danger that is easy to overlook is the loss to the business of informal knowledge and processes." p.6: "the effects of change can be subtle or delayed eg six months to a year afterwards." relata: `hse-2003-chis7`.

[^csb]: \[P] U.S. Chemical Safety and Hazard Investigation Board, *Investigation Report: Refinery Explosion and Fire, BP Texas City*, Report No. 2005-04-I-TX, March 2007. <https://www.csb.gov/assets/1/20/csbfinalreportbp.pdf>. §10.3 "Safety Implications of Organizational Change", pp.191–193: "The Baker Panel Report concluded that Texas City refinery senior leadership turnover had been high with nine plant managers since 1997; five from 2001 to 2003." Telos consultants, quoted p.193: "We have never seen an organization with such a history of leadership changes over such short period of time. Even if the rapid turnover of senior leadership were the norm elsewhere in the BP system, it seems to have a particularly strong effect at Texas City. … there has been little organizational stability. This makes the management of protection very difficult." Recommendation 2005-4-I-TX-R9, p.213: "Amend the OSHA PSM standard to require that a management of change (MOC) review be conducted for organizational changes that may impact process safety including a. major organizational changes such as mergers, acquisitions, or reorganizations; b. personnel changes, including changes in staffing levels or staff experience; and c. policy changes such as budget cutting." relata: `csb-2007-bp-texas-city`.

[^iaea]: \[P] IAEA, *Leadership and Management for Safety*, General Safety Requirements GSR Part 2, Vienna, 2016. <https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1750web.pdf>. Under Requirement 6 (Integration of the management system), ¶4.13, p.10: "Provision shall be made in the management system to identify any changes (including organizational changes and the cumulative effects of minor changes) that could have significant implications for safety and to ensure that they are appropriately analysed." relata: `iaea-2016-gsr-part2`.

[^npsa]: \[P] UK National Protective Security Authority and National Cyber Security Centre, *Secure Innovation: Security Advice for Emerging Technology Companies*, booklet v4 (PDF dated Jul 2024; campaign launched Oct 2023). <https://www.npsa.gov.uk/system/files/2024-07/secure_innovation_booklet_packaged-npsa-v4.pdf>. "Secure Your Growth", p.26: "As your company continues to evolve, so too should your security measures. The risks you face may well have changed, for example because your team has grown, you have moved to more or larger premises, you are collaborating with more partners, or because you are looking for investment." "Security for a Growing Team", p.30: "As your workforce grows, you may no longer be able to rely primarily on personal relationships to ensure trust. Fostering a positive security culture is even more important." (The PDF is two-page spreads; printed pp.26 and 30 are PDF pp.14 and 16.) relata: `npsa-2024-secure-innovation`.

[^dsit-ep]: \[P] UK DSIT, *Emerging Processes for Frontier AI Safety*, 27 Oct 2023. <https://assets.publishing.service.gov.uk/media/653aabbd80884d000df71bdc/emerging-processes-frontier-ai-safety.pdf>. p.26 (security section): "Ensure security is factored into all business decisions and AI-related assets are identified and protected with proportionate cyber, physical and personnel security measures. Secure Innovation guidance from NCSC and NPSA is available to help companies and investors to protect their technology." relata: `dsit-2023-emerging-processes`.

[^cisa]: \[P] CISA (U.S. DHS), *Insider Threat Mitigation Guide*, September 2026 edition. <https://www.cisa.gov/sites/default/files/2026-09/cisa-insider-threat-mitigation-guide-2026.pdf>. p.67, "Organizational Indicator Examples": "High stress environment … Pattern of overwork … Heightened uncertainty, either financial or contractual … Recent merger/acquisition … Under-trained staff (particularly in cybersecurity)". p.63, professional stressors: "Loss of seniority or status in merger or acquisition". relata: `cisa-2026-insider-threat-guide`.

[^iasr25c]: \[P] International AI Safety Report 2025 (Bengio et al.), arXiv 2501.17805, §3.2.2 "Societal challenges for risk management and policymaking", Key Information, p.176 (body p.178 per `uk.md`): "C. The rapid growth and consolidation in the AI industry raises concerns about certain AI companies becoming particularly powerful because critical sectors in society are dependent on their products. Such companies may become more inclined to take excessive risks or cut corners on safety standards if they expect that it would be costly for governments to let the company fail." Also p.165: "Risk management practices require commitment from organisational leadership and aligned organisational incentives. Organisational culture and structure impact the effectiveness of responsible AI initiatives and AI risk management in numerous ways." relata: `bengio-2025-international`.

[^sl3ps1]: \[P] RAND, *Achieving AI Model Weight Security Level 3 (SL3)*, RR-A4704-1, Aug 2026, Appendix B (SL3 controls; RAND supporting-materials file `Appendix-B_SL3-controls-20260616.xlsx`; the US/security verifier holds the copy). Control PS-1 "Policy and Procedures", enhanced control text: "Review and update policies and procedures at an organization-defined frequency and following personnel security incidents or significant changes to model weight infrastructure, access patterns, or organizational structure." Report p.v (exec summary): "The most severe barriers to implementing AI model weight security are organizational rather than technical, including resource allocation, cross-functional coordination, and balancing security with operational velocity." p.15: fragmented ownership "was discussed as particularly severe in startups where personnel may have multiple roles and responsibilities." relata: `aguirre-2026-sl3`.

[^gomez]: \[P] Gomez, Buick, Ferentinos, Kim & Lee, *How frontier AI companies could implement an internal audit function*, arXiv 2512.14902v2, 18 Dec 2025. p.11: "Ad hoc reviews are unscheduled assurance engagements initiated in response to emerging risks, incidents, or material changes outside the normal audit plan. They are appropriate when an area encounters an unexpected shock, such as a safety incident, model-behavior anomaly, or governance breakdown, or when rapid organizational change introduces risks not anticipated during planning." p.5, attributing to Schuett (2024): "the challenge of preserving genuine independence within fast-moving, founder-led organizations." relata: `gomez-2025-frontier`.

[^randw]: \[P] Nevo et al., *Securing AI Model Weights*, RAND RR-A2849-1, 2024. <https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf>. SL3 benchmark, "Security Team Capacity (ID.RM)", p.85 (PDF 95): "General increased capacity (compared with SL2). The team has a capacity of at least two dozen people or 5 percent of organization headcount, whichever is larger." SL4 "Other Organization Policies (ID.RM)", p.90 (PDF 100): "Vetting of investors and other positions of influence. Investors are thoroughly vetted to prevent inappropriate pressure undermining the security of the organization's assets." p.32 (PDF 42): "A particular point of disagreement was the number of people who should have authorization to access the weights. Some experts strongly asserted that the model weights cannot be secure if this number is not aggressively reduced (e.g., to the low tens)". relata: `nevo-2024-securing`.

[^isl]: \[P] Brass-Gershovich et al., *Securing AI Algorithmic Insights*, RAND RR-A4685-1, Jul 2026. <https://www.rand.org/pubs/research_reports/RRA4685-1.html>. "Areas of Consensus", p.27: "Experts overwhelmingly agreed that insider threats and HUMINT operations represent primary risks for insight security. The consensus was that personnel security measures, behavioral monitoring, and employee-departure policies represent critical areas of investment given the central role that human judgment and access play in insight security." p.44: "Risks from Former Employees. Former employees present a risk because of the information they possess … For algorithmic insights, this vector is particularly significant because insights exist substantially as knowledge in researchers' minds. In many cases, former employees might not even recognize that the knowledge they carry constitutes a proprietary insight." p.44, "Organizational Leverage Attacks": "An adversary can build financial or legal leverage over an organization through investments or grants that initially appear innocent but are then used to force access." (Printed pages; PDF = printed + 10, one page-marker gap near p.27.) relata: `brassgershovich-2026-algorithmic`.

[^mou]: \[P] California Department of Justice (Attorney General) and OpenAI, *Memorandum of Understanding re Notice of Conditions of Non-Objection*, executed 27 Oct 2025. <https://oag.ca.gov/system/files/attachments/press-docs/Final%20Executed%20MOU%20Between%20OpenAI%20and%20California%20AG%20re%20Notice%20of%20Conditions%20of%20Non-Objection%20%2810.27.2025%29%20%28Signed%20by%20OpenAI%29%20%28Signed%20by%20CA%20DOJ%29.pdf>. ¶8, p.3: "The PBC Certificate of Incorporation contains a provision consistent with Section 141(a) of the Delaware General Corporation Law requiring the PBC Board to consider only the Mission (and may not consider the pecuniary interests of stockholders or any other interest) in respect of safety and security issues related to the OpenAI enterprise…". ¶11: the SSC "has and will continue to have the authority to require mitigation measures—up to and including halting the release of models or AI systems". relata: `caag-2025-openai-mou`.

[^fli25]: \[P] Future of Life Institute, *AI Safety Index: Summer 2025*, Jul 2025. <https://futureoflife.org/wp-content/uploads/2025/07/FLI-AI-Safety-Index-Report-Summer-2025.pdf>. p.18: "OpenAI's deteriorating safety culture drew particular concern, leading to a grade drop to an F. 'OpenAI's focus on safety has decreased over the last year, and it has lost most of its researchers in this area,' a reviewer noted. High turnover on the safety team and failure to meet Superalignment commitments were taken as an indication of a concerning shift in priorities." Indicator "Reporting Culture & Whistleblowing Track Record", p.67: "Evidence is drawn from (i) the organisation's track-record of documented whistleblowing cases, … (v) patterns of safety information leaking externally (vi) departures linked to safety governance." Indicator "Company Structure & Mandate", p.61: "During competitive pressures or deployment races, traditional for-profit structures may legally compel management to prioritize shareholder returns even when activities may pose significant societal risks." The same indicator text appears in the Summer 2026 Index, p.92 (`fli-2026-ai-safety-index-summer`). Printed pages; PDF = printed + 1. relata: `fli-2025-ai-safety-index-summer`.

[^eu-src]: \[P] EU GPAI Code of Practice, Safety & Security chapter, glossary, p.33: "systemic risk source" = "a factor which alone or in combination with other factors might give rise to systemic risk"; App. 1.3 enumerates only model capabilities, propensities and affordances. Per `eu.md` §3.1 (EU verifier's reading; I confirmed Measures 1.3 and 8.3 in the same PDF). relata: `eu-cop-2025-safety-security`.

[^altman]: \[S]\[F] J. Ma, "Sam Altman confirms OpenAI won't go public this year…," *Fortune*, 12 Sep 2026. <https://fortune.com/2026/09/12/sam-altman-openai-ipo-delay-ill-advised-moment-safety-concerns/>. Altman: "I actually think that, given everything happening with safety, right now would be an ill-advised moment to go public." Also: "I would say not 2026."

[^axios]: \[S]\[F] D. Primack, "Anthropic IPO won't be slowed by safety uproar," *Axios*, 14 Sep 2026 (read via Yahoo Finance mirror: <https://finance.yahoo.com/technology/ai/articles/anthropic-ipo-wont-slowed-safety-141851836.html>; original <https://www.axios.com/2026/09/14/anthropic-ipo-safety-openai> returned 403). "Anthropic is still likely to go public in 2026, even as AI safety rockets into the zeitgeist"; "arguing that safety is improved via the transparency of being a public company."

[^san]: \[S]\[F]\[commentary] D. Pavlou, "Going public puts Anthropic's safety mission under new pressure," *Straight Arrow News*, 1 Jun 2026. <https://san.com/cc/going-public-puts-anthropics-safety-mission-under-new-pressure/>. "If its biggest competitor, OpenAI, releases a more powerful chatbot, analysts could consider Anthropic slow and too safe, even if the company believes it made the right call. This could result in some brutal quarterly earnings calls with aggressive investors upset."

[^aguilar]: \[S]\[F]\[commentary] O. Aguilar & C. Bracy, "We got California to intervene about OpenAI's corporate switch from nonprofit status. It's time for the SEC to come to the table," *Fortune*, 22 Jul 2026. <https://fortune.com/2026/07/22/openai-foundation-class-n-stock-board-control-ipo/>. "The SEC has a clear responsibility to ensure investors are aware of the unprecedented nature of OpenAI's governance structure." The nonprofit holds "sole authority over all 'safety and security decisions'".

[^techtimes]: \[S]\[F] T. Hill, "Anthropic Leads AI Labs on Retention; CEO Amodei Privately Fears Mission Is Losing to Money," *Tech Times*, 5 Aug 2026. <https://www.techtimes.com/articles/323189/20260805/anthropic-leads-ai-labs-retention-ceo-amodei-privately-fears-mission-losing-money.htm>. Citing Axios (3 Aug 2026): Amodei "has expressed concern that new talent is joining for the money rather than the mission". Citing the Dwarkesh Podcast (Feb 2026): "I probably spend a third, maybe 40%, of my time making sure the culture of Anthropic is good." Retention figures (80% two-year; 2.68× hire/loss ratio) are from SignalFire's 2025 State of Talent report. \[U] at source.

[^leopold]: \[commentary]\[F] L. Aschenbrenner, "IIIb. Lock Down the Labs," *Situational Awareness*, Jun 2024. <https://situational-awareness.ai/lock-down-the-labs/>. "Between the labs, there are thousands of people with access to the most important secrets; there is basically no background-checking, silo'ing, controls, basic infosec, etc."

[^ltbt]: \[P]\[F] Anthropic, "The Long-Term Benefit Trust," 19 Sep 2023. <https://www.anthropic.com/news/the-long-term-benefit-trust>. "the LTBT can ensure that the organizational leadership is incentivized to carefully evaluate future models for catastrophic risks … rather than prioritizing being the first to market above all other objectives"; "as it becomes more mature and has more profound effects on society, externalities tend to manifest themselves progressively more, making checks and balances more critical". First-party, Anthropic.

[^epoch]: \[S]\[F] J.-S. Denain & C. Hutcheson, "What do frontier AI companies' job postings reveal about their plans?", *Epoch AI Gradient Updates*, 24 Mar 2026. <https://epoch.ai/gradient-updates/ai-lab-job-postings>. "Anthropic's go-to-market share of open roles grew from 17% to 31% and OpenAI's from 18% to 28%"; "Research … now makes up only 12% of open roles at Anthropic and only 7% at OpenAI". Staff-count dataset: <https://epoch.ai/data/ai_companies_staff_reports.csv> (48 records, each with source links).

[^carpt]: \[P] Joint California Policy Working Group on AI Frontier Models (Bommasani, Singer et al.), *The California Report on Frontier AI Policy*, 17 Jun 2025, arXiv 2506.17303, §5.1 (PDF pp.37–39). "Supply chain monitoring … documents significant variation in the organizational profile of model developers, including their corporate status, employee head count, and geographic location." "Generic developer-level thresholds seem to be generally undesirable … major players in the space, such as Anthropic, OpenAI, and xAI, may be relatively small according to some conventional metrics of businesses (e.g., head count)." relata: `bommasani-2025-california`.

[^metr-regs]: \[S]\[F] METR, "Frontier AI safety regulations: A reference for lab staff," 29 Jan 2026. <https://metr.org/notes/2026-01-29-frontier-ai-safety-regulations/>. Covers CA SB 53, the EU CoP, NY RAISE and IL SB 315. The fetch tool reported no provisions on headcount, investors, IPOs or organisational-change triggers. I did not verify the statute texts of RAISE or SB 315.

<!-- Proposed report-side footnote labels used in §5 drafts map to the footnotes above as follows:
abs-randw→randw; abs-sl3→sl3ps1; abs-fli→fli25; abs-mou→mou; abs-iasr25→iasr25c; abs-icao→icao; abs-hse→hse; abs-csb→csb; abs-iaea→iaea; abs-npsa→npsa; abs-altman→altman; abs-san→san; abs-aguilar→aguilar; abs-gomez→gomez; abs-isl→isl; abs-epoch→epoch -->
