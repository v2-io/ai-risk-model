# Verification: US and security sources (NIST, CAISI, RAND, AISP)

*Verifier: Claude (Opus 5.5), 2026-09-27. Scope: NIST AI 600-1; the CAISI Commerce statement plus CAISI's later scope documents; RAND-W (Nevo et al. 2024) and its press release; RAND-G (Mitre & Predd 2025); RAND-ISL (Brass-Gershovich et al. 2026); RAND-SL3 (Aguirre et al. 2026); AISP (Gekker et al. 2026). All are filed in relata (bibkeys in §8). Page cites use the printed page number first, then the PDF page in brackets where they differ, so either can be checked.*

*Epistemic tags used below: **[V]** checked against the primary text by me. **[V-land]** checked, but the text is on the publisher's landing page, not in the report PDF. **[I]** my inference from verified text, marked as inference. **[U]** not checked; a lead.*

---

## 0. The five things that matter most

1. **§4's "every control they recommend involves people-count, vetting or compartmentalization" is false as written.** A narrower claim is well supported, and in one respect it is stronger than the report makes it.
   - *False part.* RAND-SL3's 262 controls are mostly technical. By NIST 800-53 family, 10 are Personnel Security and 8 are Awareness & Training; that is 18/262 ≈ 7%. Counting Access Control (27) and Identification & Authentication (23), whose workload scales with the number of accounts, brings it to about 68/262 ≈ 26%. RAND-ISL's benchmarks also include many headcount-independent controls (protective DNS, disabled macros, SBOM, post-quantum crypto, formally verified kernels).
   - *Supported part.* All three documents name the **human attack surface as the primary threat**. Several controls are **explicitly indexed to headcount or access-count**; the clearest are RAND-W's SL3 caps of 100/50/20 people and its security team of "5 percent of organization headcount."
   - *Missing piece.* "Scale worse under rapid growth" appears in none of these sources. It is the report's inference, and should be labeled as one.
   - *Sharpening.* RAND-W says the headcount/security trade-off for **weights** "can be significantly mitigated" by constrained interfaces. RAND-ISL says **insights** cannot be fully isolated and live in people's heads. The growth mechanism therefore bites **insight security and personnel-program throughput** far harder than weight security.

   Full analysis and a proposed replacement paragraph are in §3.
2. **The RAND-ISL quote in the Executive Summary and fn 19 ("more-intensive personnel security") is not in the report PDF.** It is from RAND's web landing-page summary. Relatedly, "calls for" misstates a report that says of itself it is "descriptive rather than prescriptive."
3. **Several "not found" cells are really "explicitly excluded" or "found under another name."**
   - NIST 600-1 excludes loss of control *by design*: "speculative risks … are not considered".
   - CAISI's statement is silent on loss of control, but its Jan 2026 RFI names "models that … pursue misaligned objectives" as a *security* risk.
   - The crosswalk needs a distinct symbol for "explicitly out of scope." The two cases mean opposite things for the argument.
4. **Evidence directly relevant to the growth/turnover/IPO claim.** This is for the fifth agent and for you. None of my sources names growth rate, hypergrowth or IPO as a risk factor. They do name:
   - former-employee risk, as a new attack vector judged feasible even for amateurs (RAND-ISL);
   - investor vetting (RAND-W SL4);
   - a security-team size indexed to headcount (RAND-W SL3);
   - policy review triggered by "significant changes to … organizational structure" (RAND-SL3 PS-1);
   - "balancing security with operational velocity" as a top implementation barrier (RAND-SL3).

   §4 has the quotes. They move §4's "Turnover: No" and "IPO/investor: commercial yes" rows.
5. **The pooled "RAND" crosswalk column mixes a geopolitics essay (RAND-G) with three security benchmarks** (RAND-W/ISL/SL3). The A3 "E" comes only from RAND-G. I recommend splitting the column. Similarly, **B8 pools human insiders with AI self-exfiltration**, which need different mitigations (vetting does nothing for a model).

Your leads, resolved:
- **AISP date.** Not an error. arXiv records v1 as submitted "Tue, 23 Jun 2026 08:57:30 UTC". The 2607 identifier is, I believe, assigned at announcement, which implies a moderation hold into July. That last step is [I] from arXiv practice, fairly confident. AISP cites RAND-ISL as "Forthcoming", consistent with June authorship.
- **Footnote 17 (RAND-G) and the §5.7 "low tens".** Both verified; the tags can move to [P].

---

## 1. Line-level corrections

Format for each item: **Location** / current text / what the source says / proposed replacement / confidence.

### 1.1 Executive Summary, bullet 2 (and fn 19)

- **Current:** "It treats the attack surface for algorithmic know-how as human-centred and calls for 'more-intensive personnel security' at higher levels.[^19]"
- **Source [V-land]:** RAND landing page, https://www.rand.org/pubs/research_reports/RRA4685-1.html: "Higher levels require increasingly isolated systems and facilities, more-intensive personnel security, and substantial restrictions on ordinary research practices." and "The attack surface is broad and human-centered." The PDF does not contain "more-intensive personnel security" (I searched the full text).
- **Source [V], PDF, About This Report, p. iii:** "The framework is descriptive rather than prescriptive, offering a structured way to assess what level of protection would be required to defend a given insight against a specific adversary capability."
- **Source [V], PDF p. vi (Summary, Key Findings):** "At ISL4 or ISL5, security measures (e.g., isolated compartmented facilities with emanation shielding, government-standard personnel vetting, supply chain compartmentalizing, restricting researcher travel and communication) are likely to reshape how organizations operate."
- **Source [V], p. 5 [PDF 15]:** "Access. Who within an organization needs to know or interact with the insight to do their job? … Broader internal access translates into a larger attack surface for adversaries. Generally, the more employees or contractors who work with a particular insight, the higher the risk of its theft or leakage."
- **Proposed:** "The closest work is RAND's *Securing AI Algorithmic Insights* (Jul 2026). It describes the attack surface for algorithmic know-how as human-centred, states that 'the more employees or contractors who work with a particular insight, the higher the risk of its theft or leakage,' and describes higher insight-security levels as requiring 'government-standard personnel vetting' and compartmentalization.[^19] That is a mechanism through which headcount matters, though RAND does not frame it as growth, and the framework is explicitly 'descriptive rather than prescriptive.'"
- **Confidence:** high.

### 1.2 Footnote 19: new body

> \[P] Brass-Gershovich, Steratore, Hurd, Bradley, Friedman & Nevo, *Securing AI Algorithmic Insights*, RAND RR-A4685-1, published 20 Jul 2026 (web-only, 99 pp.), doi:10.7249/RRA4685-1. PDF: https://www.rand.org/content/dam/rand/pubs/research_reports/RRA4600/RRA4685-1/RAND_RRA4685-1.pdf. p. 5: "Generally, the more employees or contractors who work with a particular insight, the higher the risk of its theft or leakage." p. vi: ISL4–5 measures include "government-standard personnel vetting … restricting researcher travel and communication." p. iii: the framework "is descriptive rather than prescriptive." The phrase "more-intensive personnel security" is from RAND's landing-page summary, not the report. relata: `brassgershovich-2026-algorithmic`.

### 1.3 §1 table rows (dates, codes, tags)

| Row | Current | Proposed | Basis |
| --- | --- | --- | --- |
| RAND-SL3 | Aug 2026 | Aug 25, 2026 | Landing page, "Published Aug 25, 2026" [V-land] |
| AISP | Jun 23, 2026 | "Jun 23, 2026 (submitted; announced Jul 2026)" | arXiv submission history [V]; ID timing [I] |
| CAISI | Jun 2025 | Jun 3, 2025 | Statement header "Tuesday, June 3, 2025" [V, via Wayback] |
| RAND-G | tag U | tag P | Full text read [V] |
| NIST | Jul 2024 | Jul 2024 (approved by NIST ERB 25 Jul 2024) | PDF p. [3] [V] |

Add a DOI column or fold DOIs into the links. They exist for all four RAND items: 10.7249/RRA2849-1, 10.7249/PEA3691-4, 10.7249/RRA4685-1, 10.7249/RRA4704-1. NIST's is 10.6028/NIST.AI.600-1.

### 1.4 Footnote 12 (NIST): confirm and enrich

- The "12 risks confirmed" claim is correct [V]. The list is at pp. 4–5 [PDF 8–9].
- **Proposed body:** "\[P] NIST AI 600-1, *AI RMF: Generative AI Profile*, Jul 2024, doi:10.6028/NIST.AI.600-1. The 12 GAI risks are listed at pp. 4–5. Scope, p. 3: 'This document focuses on risks for which there is an existing empirical evidence base at the time this profile was written; for example, speculative risks that may potentially arise in more advanced, future GAI systems are not considered.' relata: `nationalinstituteofstandardsandtechnologyus-2024-artificial`."
- **Confidence:** high.

### 1.5 Footnote 13 (CAISI): verified; add context

- **Quote [V]:** "In conducting these evaluations, CAISI will focus on demonstrable risks, such as cybersecurity, biosecurity, and chemical weapons."
- **Access note.** The live commerce.gov page returns a Cloudflare 403 to scripts. The text was captured from Wayback snapshot 20260505045511. The same sentence appears on https://www.nist.gov/caisi (retrieved 2026-09-27).
- **Nuance for the body.** The statement says Lutnick "announced his plans to reform the agency formerly known as the U.S. AI Safety Institute into the Center for AI Standards and Innovation (CAISI)." It is a statement of plans, not a founding instrument.
- **Missing from the report.** The statement's framing sentence: "For far too long, censorship and regulations have been used under the guise of national security. Innovators will no longer be limited by these standards." This matters for §5.8 "US posture": CAISI's scope is framed against regulation, not only as a hazard ranking.
- **Proposed body:** "\[P] U.S. Dept. of Commerce, press release, 3 Jun 2025 (text via Wayback 2026-05-05; also mirrored on nist.gov/caisi). '…CAISI will focus on demonstrable risks, such as cybersecurity, biosecurity, and chemical weapons.' It also tasks CAISI to assess 'potential security vulnerabilities and malign foreign influence arising from use of adversaries' AI systems, including the possibility of backdoors and other covert, malicious behavior.' relata: `commerce-2025-caisi`; see also `nist-caisi-page-2026`."
- **Confidence:** high.

### 1.6 Footnote 15 (RAND-W): verified; pin and lengthen

- **Quote [V], p. 18 [PDF 28], "Notable Areas of Disagreement and Consensus":** "Concern around the feasibility of threats from organization insiders (which span many of the categories and are not limited to the Human Intelligence category) was an emerging point of consensus. Experts generally agreed that this is a significant source of risk and that significant efforts should be dedicated to mitigating it."
- **Proposed body:** add "p. 18" and the full sentence above. Also add doi:10.7249/RRA2849-1 and relata `nevo-2024-securing`.
- **Note.** The PDF was revised June 2024 (p. [2]: "revised in June 2024 to add acknowledgments, correct formatting, and make an addition to Appendix A").

### 1.7 Footnote 16 (RAND press release): verified

- **Quote [V]:** the release lists priorities including "centralizing all copies of weights to a limited number of access-controlled and monitored systems; reducing the number of people with authorization; hardening interfaces against weight exfiltration; … implementing insider threat programs … None of these are widely implemented, but all are feasible to achieve within a year, according to the report."
- **Suggestion.** Cite the report itself as primary. Summary p. vi [PDF 6]: "Reduce the number of people authorized to access the weights." Keep the press release as secondary.
- **Confidence:** high.

### 1.8 Footnote 17 (RAND-G): upgrade \[U] → \[P]

> \[P] Mitre & Predd, *Artificial General Intelligence's Five Hard National Security Problems*, RAND Expert Insights PE-A3691-4, Feb 2025, doi:10.7249/PEA3691-4. p. iii: the five problems are "(1) wonder weapons; (2) systemic shifts in power; (3) nonexperts empowered to develop weapons of mass destruction; (4) artificial entities with agency; and (5) instability." relata: `mitre-2025-agi`.

### 1.9 Footnote 18 (RAND-SL3): verified; pin to the PDF

- **Quote [V], PDF Summary p. v:** "RAND SL3 encompasses 140 standard security controls and 122 supplemental controls drawn from NIST SP 800-53 that address 31 high-feasibility attack vectors … RAND SL3 is designed for feasible implementation within 6 to 12 months by frontier AI research labs."
- **Also on p. v:** "The most severe barriers to implementing AI model weight security are organizational rather than technical, including resource allocation, cross-functional coordination, and balancing security with operational velocity."
- **Caveats worth a clause.** The report was "not professionally copyedited" (p. [2]). The workshop had "5 external participants and an equal number of RAND attendees" and "a total of 9 voters" (pp. 14–15).
- **Controls.** The full control list is at https://github.com/RANDCorporation/achieving-AI-model-weight-sl3 (data v1.5, 2026-06-03).
- **relata:** `aguirre-2026-sl3`.

### 1.10 Footnote 34 (AISP): the quote supports nothing it is attached to

- **Current quote:** "the gap between AI adoption and AI security readiness continues to widen." This is the abstract [V]. fn 34 is cited for the insider-threat and vetting claims (B8, §4). The quote does not support them.
- **Source [V], p. 43:** "Insider threats are among the most significant risks for AI model weight theft and intellectual property compromise … A single compromised insider – whether compromised through financial pressure, foreign recruitment, or ideological motivations – could exfiltrate years of research in minutes."
- **Source [V], p. 42:** "Government personnel security practices … can be adapted for private AI labs … Formal programs – including Facility Clearances (FCL) and Personnel Security Clearances (PCL)."
- **Proposed body:**

  > \[P] Gekker, Steratore, Smith, Brass-Gershovich, Gandhi, Nichols, Bolina, Shlegeris, Einstein, Lahav, O. Nevo & S. Nevo, *AI Security Priorities: A Field-Wide Agenda*, arXiv 2607.26069 (v1 submitted 23 Jun 2026). p. 43: "Insider threats are among the most significant risks for AI model weight theft and intellectual property compromise." p. 45 (elements of success): "Overly restrictive personnel security can create single points of failure, slow research, and make organizations less attractive to top talent." The vetting priority entered the agenda as the *eleventh*-ranked cost-effectiveness item (pp. 95–96). Authors include RAND (3) and Irregular (3). The paper discloses that several recommendations align with Irregular's commercial services (p. 3). relata: `gekker-2026-aisp`.

- **Confidence:** high.
- **Why the extra clauses matter.** AISP is not independent of RAND-ISL: Steratore, Brass-Gershovich and S. Nevo co-author both. And the vetting area was a marginal inclusion. When §4 counts "three 2026 RAND and field-agenda documents" as convergent, they are correlated sources.

### 1.11 §5 item 2 (Loss of control): "Absent from CAISI's stated focus"

- The claim is true of the June 2025 statement [V]. It is incomplete for CAISI's later scope.
- **Source [V], CAISI RFI, 91 Fed. Reg. 698–701 (8 Jan 2026), p. 699:** the RFI focuses on "novel risks that arise from the use of machine learning models embedded within AI agent systems," including "(3) the risk that the behavior of uncompromised models may nonetheless pose a threat to confidentiality, availability, or integrity (e.g., models that exhibit specification gaming or otherwise pursue misaligned objectives)."
- **Proposed:** "Absent from CAISI's June 2025 statement of focus.[^13] By January 2026, CAISI framed misaligned-objective behavior by agents as a *security* risk to confidentiality, integrity and availability, not as loss of control.[^new-RFI]"
- This is a clean instance of Joseph's scale point: the same phenomenon is named at incident scale in the US and at systemic scale in the EU.
- **Confidence:** high on the text; the interpretation is [I].

### 1.12 §5 item 6 (Open weights): the contrast with RAND is overdrawn

- **Current:** the EU exemption "resets the security baseline in a way RAND's actor-based threat model does not."
- **Source [V], RAND-W p. 4 [PDF 14]:** "We exclude models whose weights are not deemed critical to secure … Once a model has been made publicly available (which is often referred to as 'open-sourcing' it), there is no longer value in securing specific copies of it. The decision of whether to 'open-source' future models should be informed by whether their risks justify controlling access to them."
- **Source [V], RAND-W p. vi:** "There is an ongoing, lively debate regarding the extent to which different models need to be secured (if at all)."
- **Proposed:** "The EU Code exempts models weaker than the best open-weight model from Commitment 6.[^2] RAND's framework is conditional: it defines what each security level takes against each actor class. It leaves to others which models warrant securing, noting only that once weights are public 'there is no longer value in securing specific copies.'[^15] The two are compatible. The EU instrument makes the which-models decision that RAND explicitly declines to make."
- **Confidence:** high.

### 1.13 §5 item 7: remove \[U] from "low tens"

- **Source [V], RAND-W p. 32 [PDF 42]:** "A particular point of disagreement was the number of people who should have authorization to access the weights. Some experts strongly asserted that the model weights cannot be secure if this number is not aggressively reduced (e.g., to the low tens); others claimed that such a reduction would not be necessary, feasible, or justified. – The trade-off between security and productivity that this number of people points to can be significantly mitigated by implementing more constrained and secure interfaces for model weight access."
- **Also relevant [V], SL3 benchmark, Appendix B p. 80 [PDF 90]:** "Output-limited arbitrary access is limited to 100 people, access to an isolated network with direct access is limited to 50 people, and the ability to make copies of the weights is limited to 20 people."
- **Proposed:** "RAND-W's interviewed experts disagreed on how aggressively to reduce authorized access to weights. Some said it must fall 'to the low tens'; others called that unnecessary. RAND adds that constrained interfaces can 'significantly mitigate' the trade-off. Its SL3 benchmark nonetheless sets absolute caps of 100 / 50 / 20 people for output-limited, isolated-network and copy access respectively.[^15] RAND-SL3 operationalizes SL3 as 262 NIST 800-53-derived controls implementable in 6–12 months.[^18]"
- **Style note.** "Panel" slightly overstates. RAND-W used 32 interviews plus iterative feedback and workshops (p. 5). Its conclusion says "31 leading global experts" (p. 35), an internal inconsistency in RAND-W.
- **Confidence:** high.

### 1.14 §6: single-source list

- **"'Wonder weapons' (RAND-G) \[U]":** now [V], p. 3 [PDF 8]. Change the tag to [^17].
- **"Algorithmic-insight leakage (RAND-ISL)" is not single-source.** AISP names it twice.
  - p. 26: "Parallel standards could address protection of algorithmic insights (training methodologies, architectural innovations, evaluation results)."
  - p. 68: red-teaming specifications "could help prevent the theft of model weights and algorithmic insights."
  - Caveat: the sources are correlated (shared authors). Suggest "RAND-ISL; echoed by AISP (shared authors)".
- **"Single points of failure (DSIT, IASR)":** add NIST as a third source.
  - NIST p. 9 [PDF 13]: foundation models act "as 'bottlenecks,' or single points of failure."
  - NIST p. 2 fn 3: "'Algorithmic monocultures' refers to the phenomenon in which repeated use of the same model or algorithm in consequential decision-making settings … can result in increased susceptibility by systems to correlated failures."
  - So the row moves from "two sources" to three.

### 1.15 §7 table (priorities)

- **US CAISI row:** add "evaluation of US vs. adversary (PRC) models; agent hijacking and backdoors."
  - Source: NIST news release 30 Sep 2025 [V]. CAISI "responds to President Donald Trump's America's AI Action Plan, which directs CAISI to conduct research and publish evaluations of frontier models from the PRC."
  - Source: RFI Jan 2026 [V].
  - relata: `nist-2025-caisi-deepseek`, `nist-2026-rfi-agents`.
- **RAND row:** split into two.
  - "RAND security (W/ISL/SL3): weight and insight theft, OC1–OC5 actors."
  - "RAND-G: five unranked 'hard problems' (wonder weapons, power shifts, non-expert WMD, AI agency, instability)." Mitre & Predd say proposals on one "can undermine progress on – if not outright ignore – another" (p. iii).

---

## 2. Crosswalk cells I own

### 2.1 Method note: add a symbol for "explicitly out of scope"

NIST 600-1's "—" for A3 is a deliberate scope exclusion. The document says so on p. 3. For the report's argument that difference matters: an exclusion is a finding about the source, while "—" per the legend is "not found." I suggest a distinct mark for exclusions, e.g. **X**.

### 2.2 NIST column

| Cell | Current | Proposed | Evidence (NIST AI 600-1) | Conf. |
| --- | --- | --- | --- | --- |
| A1 | E✓ | E✓ | §2.1, p. 5; risk #1 p. 4 | high |
| A2 | E✓ | E✓ | risk #9 "Information Security: Lowered barriers for offensive cyber capabilities…", pp. 4–5; §2.9 p. 10 | high |
| A3 | — | **X** (explicitly excluded) | p. 3: "speculative risks … are not considered" | high |
| A4 | E✓ | **E✓ with a definitions flag** | NIST's category is "Information Integrity" (mis/disinformation, risk #8, p. 4; §2.8 pp. 9–10), not "manipulation" in the EU sense. p. 10: "Even very subtle changes to text or images can manipulate human and machine perception." | medium |
| A5 | E✓ | E✓ | risk #11 (CSAM/NCII), §2.11 p. 11; fraudulent impersonation §2.8 p. 10 | high |
| A6 | E✓ | E✓ | risk #2 Confabulation, §2.2 p. 6 | high |
| A7 | — | **P** | App. A.1.8 p. 52: AI incidents include "disruption of the management and operation of critical infrastructure" (definition only) | medium |
| A8 | — | **P** | p. 2: ecosystem-level risks include "impacts on access to opportunity, labor markets, and the creative economies"; fn 4 | high |
| A9, A10, A17, A18 | — | — | searched: no "concentrat*", "military", "multi-agent" | high |
| A11 | E✓ | E✓ | risk #7 Human-AI Configuration, §2.7 p. 9 ("automation bias, over-reliance, or emotional entanglement") | high |
| A12–A15 | E✓ | E✓ | risks #4, #10, #6, #5 | high |
| A16 | — | **P** (optional) | §2.6 p. 8: "Disparate or reduced performance for lower-resource languages also presents challenges to model adoption, inclusion, and accessibility" | low–med |

Additional NIST entries for the (b) and (c) tables. These are not in the crosswalk grid, but the "Key sources" columns omit NIST where it applies.

- **B7 (weight security):** §2.9 p. 10: security includes "the integrity and (when applicable) the confidentiality of the GAI code, training data, and model weights". MS-2.7-001 p. 33 [PDF 37]: assess threats including "model theft or exposure of model weights".
- **B14:** already cited. Pin to §2.9 pp. 10–11: "GAI itself is vulnerable to attacks like prompt injection or data poisoning". Add NIST AI 100-2e2025 as the definitional source (§7).
- **C3 / C12:** algorithmic monoculture, p. 2 fn 3 and p. 9 (quoted in §1.14).
- **C6:** GV-1.3-006, p. 15: reevaluate risk tolerances for "broad GAI negative risks, including: Immature safety or risk cultures related to AI and GAI design, development and deployment". Rate P.
- **C9:** GV-2.1-005, p. 17: "Create mechanisms to provide protections for whistleblowers who report, based on reasonable belief, when the organization violates relevant laws or poses a specific and empirically well-substantiated negative risk to public safety." Also App. A.1.2 p. 48, "Whistleblower protections". Note the "empirically well-substantiated" qualifier, consistent with NIST's evidence-based scope.

### 2.3 CAISI column

**Recommendation.** Widen the column's source set from the June 2025 statement to CAISI's own later scope documents, all [V]:
- the NIST CAISI page;
- the Sept 2025 DeepSeek evaluation release;
- the Jan 2026 agent-security RFI.

Otherwise the column describes CAISI as of a single press release.

| Cell | Current | Proposed | Evidence | Conf. |
| --- | --- | --- | --- | --- |
| A1 | E | E | statement: "biosecurity, and chemical weapons"; RFI p. 699: "(CBRNE) weapons development and use" | high |
| A2 | E | E | statement "cybersecurity"; DeepSeek release: hijacked agents "sent phishing emails, downloaded and ran malware, and exfiltrated user login credentials" | high |
| A3 | — | — for the statement; **P for CAISI overall** | RFI p. 699: "models that exhibit specification gaming or otherwise pursue misaligned objectives", framed as a threat to confidentiality, availability, integrity | high (text) |
| A4 | P | **P, with a definitions flag** | statement: "malign foreign influence arising from use of adversaries' AI systems"; DeepSeek release: models "echoed four times as many inaccurate and misleading CCP narratives". This is *adversary-state influence via model outputs*, a different construct from EU "harmful manipulation." | medium |
| A7 | P | P | RFI p. 699: "security vulnerabilities may pose future risks to critical infrastructure" | high |
| A10 | P | P | statement: assess "the state of international AI competition" | high |
| B14 (table b) | cited | keep; pin | statement: "backdoors and other covert, malicious behavior"; RFI p. 699 lists indirect prompt injection, data poisoning, intentionally placed backdoors | high |

Lead, not checked: CAISI's Dec 2025 blog "Cheating On AI Agent Evaluations" (on nist.gov/caisi) is likely relevant to **B5 (evaluation gap / test-awareness)** and worth a look by whoever owns B5 [U].

### 2.4 RAND column: recommend splitting into RAND-G and RAND-Sec

If kept pooled, the cells should at least reflect RAND-G. All evidence in this table is from RAND-G, which I read in full.

| Cell | Current | Proposed | Evidence (page [PDF]) | Conf. |
| --- | --- | --- | --- | --- |
| A1 | E | E | problem 3, p. 5 [10]: "AGI might empower nonexperts to develop weapons of mass destruction" | high |
| A2 | E | E | p. 4 [9]: "a splendid first cyber strike"; p. 5: "virulent cyber malware" | high |
| A3 | E | E (RAND-G only) | p. 6 [11]: "In the extreme, a loss-of-control scenario could result, wherein AGI's pursuit of its desired objectives incentivizes the machine to resist being turned off, counter to human efforts." | high |
| A4 | — | **P** | p. 4 [9]: "AGI could be used to manipulate public opinion through advanced propaganda techniques, threatening democratic decisionmaking." | high |
| A6 | — | **P** | p. 6 [11]: AGI "could be misaligned … causing unintentional harm … institute rolling blackouts to increase the cost-effectiveness of energy distribution networks" | medium |
| A7 | P | P | same rolling-blackouts example | high |
| A8 | P | **D** | p. 5 [10]: "automated workers could rapidly displace labor across industries, causing national gross domestic product to skyrocket but wages to collapse … Labor disruption of such scale and speed could spark social unrest" | medium |
| A9 | E | E, with a note: *inter-state* power | problem 2, p. 4 [9]: "a systemic shift … that alters the balance of global power" | high |
| A10 | E | E | problem 5, p. 7 [12] | high |
| A11 | — | **P** | p. 6 [11]: "the erosion of human agency as humans become increasingly reliant on the technology" | high |
| A17 | — | **P** | p. 6 [11]: "A singular AGI or communities of AI agents could also become actors on the world stage." | medium |

RAND-Sec (W/ISL/SL3) has no hazard-row content beyond theft of weights and insights. One exception: RAND-ISL's codebook defines "Misaligned AI exfiltration" (p. 34 [44]), which is relevant to B8.

### 2.5 Row B7 (weight / infrastructure security)

Current key sources: RAND-W, RAND-SL3, EU-CoP. Add NIST 600-1 §2.9 and NIST AI 800-1 2pd Practice 3.2. For 800-1, p. 13 [PDF 18]: "Apply appropriate protections against insider threats, such as limiting access to model weights within the organization or implementing two-party control systems."

Also add AISP pp. 38, 64. p. 38 (SL timelines; this is AISP's reading of RAND): "AI labs can reasonably achieve SL-3 … within approximately one year and SL-4 … within 2-3 years through private investment. However, achieving SL-5 … requires an estimated minimum of five years and necessitates active support from national security communities."

### 2.6 Row B8 (insider threats): verified; recommend a split

**Human insiders, all [V]:**
- RAND-W p. 18 (consensus quote above) and OC3 definition p. 10.
- RAND-ISL p. 22 [32]: "An insider-threat program becomes essential. Because a single knowledgeable employee can constitute a complete vector for insight theft…"
- RAND-SL3 p. v: "Human intelligence threats, including insider threats and extortion represent the top concern of representatives from frontier AI research labs and government." pp. 14–15: HUMINT "had almost twice the votes of the next concerning attack category" (9 voters).
- AISP p. 43.
- NIST AI 800-1 2pd p. 12, Practice 3.1: "Consider the threat posed by insiders, such as an individual involved in developing or deploying the model who may behave maliciously or collaborate with an external attacker."

**AI as insider / self-exfiltration, all [V]:**
- AISP p. 82: "AI systems deployed internally combine 'the hard parts of both' insider and outsider threats. Like insiders, AI agents receive broad access with granular permissions, while, like outsiders, they could act at significant scale and potentially overpower labor-intensive insider security techniques." It cites Shlegeris, Redwood blog 2025.
- AISP p. 98: priority "Provable prevention of capabilities … for the prevention of specific actions by unaligned AI (e.g., self-exfiltration)".
- RAND-ISL codebook p. 34 [44]: "Misaligned AI exfiltration: Scenarios in which an AI system, because of misalignment or unintended behavior, leads to the unauthorized exfiltration of data or insights."

**Why split.** The human-insider mitigations (vetting, clearances, relationship reporting, mandatory vacations) are inapplicable to a model. AISP's phrase "overpower labor-intensive insider security techniques" is the reason. Suggest **B8a Human insiders** and **B8b AI systems as insiders (incl. self-exfiltration)**, with B8b cross-referenced to A3.

### 2.7 Row B14 (attacks on AI systems)

This row is verified for NIST and CAISI (above). Add NIST AI 100-2e2025 as the terminology source (definitions in §7). Add the CAISI DeepSeek release for measured agent hijacking: "12 times more likely than evaluated U.S. frontier models to follow malicious instructions".

### 2.8 Row B15 (algorithmic-insight leakage): verified

- **Source [V], RAND-ISL p. iii:** "Unlike model weights, which can be centralized and secured, insights are distributed across code, documentation, communications, and human expertise, making them far harder to contain."
- **Also p. 26 [36]:** "a complete isolation of insights is extremely difficult, possibly even infeasible."
- Add AISP (correlated) as a second source. See §1.14.

---

## 3. §4 interpretation: framing assessment and proposed replacement

**Current text:** "Three 2026 RAND and field-agenda documents (RAND-ISL, RAND-SL3, AISP) sharpen the mechanism: every control they recommend involves people-count, vetting or compartmentalization, and those scale worse as headcount grows quickly."

**What the sources support.**

(a) **"Every control" is false.**
- RAND-SL3 family counts, from the RAND control dataset (`sl3-controls-data.js`, 262 controls) [V]:

  | Family | Count |
  | --- | --- |
  | System & Information Integrity | 37 |
  | System & Communications Protection | 31 |
  | Access Control | 27 |
  | Configuration Management | 25 |
  | Identification & Authentication | 23 |
  | System & Services Acquisition | 23 |
  | Maintenance | 11 |
  | Risk Assessment | 11 |
  | Audit | 10 |
  | Security Assessment | 10 |
  | **Personnel Security** | **10** |
  | **Awareness & Training** | **8** |
  | Supply Chain | 8 |
  | Incident Response | 7 |
  | Media Protection | 7 |
  | Physical | 7 |
  | Contingency Planning | 5 |
  | Program Management (PM-12 Insider Threat Program) | 1 |
  | Unlabeled | 1 |

  Family is a proxy, and I did not read all 262 enhanced texts. Still, personnel and training controls are about 7%, and about 26% if you add account-based access and identity controls.
- RAND-ISL itself says ISL1–2 "impose a minimal operational burden" (p. vi). Its tables include protective DNS, macro disabling, SBOM, post-quantum crypto and formally verified kernels.

(b) **The human attack surface is primary in all three.** [V]
- ISL p. 16 [26]: "HUMINT vectors dominate experts' concerns."
- ISL p. 16 [26]: universally exploitable vectors, including "former employee risks", "succeed primarily because of human and process failures on the defender's side."
- ISL p. 27 [37]: "Experts overwhelmingly agreed that insider threats and HUMINT operations represent primary risks for insight security."
- SL3: HUMINT top concern (above). Workshop participants "overwhelmingly stressed humans as the biggest threats" (p. 18).

(c) **Several controls are explicitly indexed to headcount or access-count.** This is the strongest anchor and is not in the report. [V]
- **RAND-W SL3 (App. B):**
  - Access caps of 100 / 50 / 20 people (p. 80 [90]).
  - "Background checks are conducted for all employees. Employees with access to the weights or any sensitive systems go through extensive screening every six months" (p. 83 [93]).
  - Security team capacity "of at least two dozen people or 5 percent of organization headcount, whichever is larger" (p. 85 [95]).
- **RAND-ISL:**
  - "the more employees or contractors who work with a particular insight, the higher the risk" (p. 5).
  - Compartmentalization aims to reduce "the number of individuals with complete knowledge" (p. vi).
  - ISL5: "No cross-compartment personnel for top compartments," with the note that this "is particularly challenging with AI research because researchers often need to integrate insights across multiple domains" (p. 26 [36]).
- **RAND-SL3 enhanced controls:**
  - PS-1: review personnel security policies "following personnel security incidents or significant changes to model weight infrastructure, access patterns, or organizational structure."
  - PS-3: rescreening triggers on "a change in role, significant expansion of access scope."
  - PS-4 and PS-5: termination and transfer revocation.

(d) **"Scale worse under rapid growth" is the report's inference.** None of the three says it. The ingredients the sources supply:
- per-person work (screening, six-monthly rescreening, access reviews, offboarding, compartment NDAs);
- fixed absolute caps against rising access demand;
- a security team that must grow in proportion to headcount;
- cross-compartment requests that need owner approval, and at ISL4 "dual approval";
- SL3's reported barrier "balancing security with operational velocity."

The closest counter-evidence:
- RAND-W p. 32: the headcount/security trade-off "can be significantly mitigated by implementing more constrained and secure interfaces for model weight access."
- AISP p. 45: heavy vetting "can create single points of failure, slow research, and make organizations less attractive to top talent." This cuts both ways: it is also a pressure *against* keeping the controls under growth.

(e) **Sharpening the report can use [I].** For weights, RAND designs controls to be headcount-*independent*: caps plus hardened interfaces. For insights, RAND says isolation is "possibly even infeasible" and the asset lives in people. So the growth → degradation mechanism has its best source support for **algorithmic-insight security and personnel-security throughput**, not weight security.

**Proposed replacement paragraph:**

> **Interpretation.** The literature treats organizational factors as *static attributes*: culture, structure, resourcing, access control. None of the sources models how fast they degrade under hypergrowth. A growth or absorptive-capacity factor is therefore a **moderator** of C6–C9 and B7–B8, not a new hazard. The 2026 RAND work supplies the mechanism's ingredients, though not the mechanism itself.
>
> - It treats the human attack surface as primary. HUMINT and insider threats top expert concern in RAND-ISL and RAND-SL3.
> - Several of its controls are explicitly indexed to headcount:
>   - RAND-W's SL3 benchmark caps weight access at 100 / 50 / 20 people and sizes the security team at "5 percent of organization headcount";
>   - RAND-ISL states that "the more employees or contractors who work with a particular insight, the higher the risk";
>   - RAND-SL3 triggers policy review on "significant changes to … organizational structure."
> - Most of the 262 SL3 controls are technical and headcount-independent. RAND argues that for *weights*, constrained interfaces can decouple security from headcount. For *algorithmic insights* it says isolation is "possibly even infeasible."
>
> Our inference, not RAND's claim: under rapid growth, the per-person controls (screening, rescreening, access review, offboarding, compartment approvals) and the fixed access caps come under strain. The effect should bite hardest on insight security. AISP (which shares authors with RAND-ISL) adds the counter-pressure: heavy vetting can "slow research, and make organizations less attractive to top talent."

Confidence: high on (a)–(c); the paragraph's inference is clearly marked.

---

## 4. Evidence bearing on the growth / turnover / IPO question

This is for the fifth agent and for the integrator. I swept all eight texts for growth/hypergrowth/headcount/turnover/attrition/IPO/investor/hiring/onboard/velocity/talent. **No source names lab growth rate, hypergrowth, or IPO as a risk factor.** That supports the exec-summary claim for my slice. But several adjacent items should change §4's rows:

- **"Turnover / key-person risk: No" → "Partly (departure as an attack vector; not rate).**" [V]
  - RAND-ISL p. 44 [54], a **new vector not in RAND-W**: "Risks from Former Employees. Former employees present a risk because of the information they possess … For algorithmic insights, this vector is particularly significant because insights exist substantially as knowledge in researchers' minds. In many cases, former employees might not even recognize that the knowledge they carry constitutes a proprietary insight."
  - It is rated feasible for all actor classes, even OC1 (p. 16 [26]).
  - ISL2 benchmark: "Structured offboarding and exit procedures for departing employees" (p. 21 [31]; detail p. 57 [67]).
  - RAND-SL3 PS-4 (termination) and PS-5 (transfer).
  - None models *rates* of turnover. But turnover × access is exactly the exposure this vector names.
- **"IPO / commercial / investor pressure: Commercial yes; IPO no" → add investor influence as a named security risk.** [V]
  - RAND-W SL4, Other Organization Policies, p. 90 [100]: "Vetting of investors and other positions of influence. Investors are thoroughly vetted to prevent inappropriate pressure undermining the security of the organization's assets."
  - Same page: "Prioritizing leak prevention over other organizational goals … the security team has veto … over network, product, and work environment decisions that may undermine security (even if changes are important from a product or commercial perspective)."
  - HUMINT vector "Organizational leverage attacks" (p. 68–69 [78–79]): "An adversary can build financial or legal leverage over an organization – for example, through investments or grants that appear innocent initially but are then used to force the organization into giving access."
  - This is investor *influence as a vector*, not IPO market pressure. It is still the nearest named factor.
- **Operational velocity.** RAND-SL3 p. v: "balancing security with operational velocity" is among "the most severe barriers." pp. 15: "Fragmented ownership of systems across teams … was discussed as particularly severe in startups where personnel may have multiple roles and responsibilities." Note the small n (9 voters).
- **Organizational change as a trigger.** RAND-SL3 PS-1 (quoted in §3). It is a US-side analogue of EU Measure 1.3 and strengthens Recommendation 3.
- **Candidate indicators (for Recommendation 2), grounded in the sources:**
  - security-team headcount ÷ org headcount against RAND-W's 5% SL3 floor;
  - privileged-access headcount against RAND-W's 100/50/20 caps;
  - rescreening cadence against RAND-W's six months;
  - time-to-revoke on termination (SL3 PS-4);
  - count of former staff who held insight-compartment access (RAND-ISL former-employee vector).

---

## 5. Other things I noticed

- **The RAND security framework's own vocabulary collides with lab RSP vocabulary.**
  - RAND-W p. 22 notes that responsible scaling policies use "AI safety levels or risk levels … often defined by which threat actors the model should be secured against."
  - AISP p. 54 cites "models assessed at ASL-4."
  - RAND-ISL distinguishes WSL from ISL (p. 1).
  - "SL3", "WSL3", "ISL3" and "ASL-3" are four different things. The report uses "SL3" loosely in Recommendation 2; I would pin it to "RAND-W SL3."
- **AISP explicitly documents the terminology problem Joseph suspects.** p. 34: "'control' can refer to a very general problem of steering AI systems, or to a specific set of guardrails for artificial general intelligence." Also "'AI Security' may refer to protecting AI systems from cyber threats – as in cybersecurity – or describing national security implications of advanced AI." That is a citable anchor for the phase-2 terminology map.
- **AISP's point on correlated reviewers bears on Joseph's `bs-correlated-watchers` card.** p. 72: "Simply delegating both an action and its review to separate AI agents provides weaker security guarantees than if using separate humans … AI agents trained on similar data are likely to share systematic blind spots." p. 74: "Reduce reliance on agent-to-agent review as a safeguard." Mentioned in passing; out of this report's scope.
- **Crossref metadata for the auto-created NIST entries is thin.**
  - `nationalinstituteofstandardsandtechnologyus-2024-artificial` has the truncated title "Artificial intelligence risk management framework :".
  - `nist-2025-managing` shows author "NIST, G. M.".
  - The PDFs are correct; the entry fields may want a later `relata` touch-up. I did not hand-edit canonical entries.
- **NIST AI 800-1 is still a draft.** The second public draft is January 2025, by the then-US AISI. I found no final version. Cite it as a draft.
- **Its dual-use definition comes from EO 14110.** My general knowledge is that EO 14110 was rescinded in January 2025 [U]. So the definition persists in NIST text but its executive-order anchor may be gone.

---

## 6. New references worth adding

All are filed in relata and [V] for the quotes used.

1. **CAISI RFI on AI agent security**, 91 FR 698–701, 8 Jan 2026 (`nist-2026-rfi-agents`). It is CAISI's most substantive public scope statement I found. It covers A3 (misaligned objectives as security risk), B14, and the definition of "AI agent system."
2. **NIST news release on CAISI's DeepSeek evaluation**, 30 Sep 2025 (`nist-2025-caisi-deepseek`). Secondary. The full report at https://www.nist.gov/document/caisi-evaluation-deepseek-ai-models-report was not retrieved [U]. It shows CAISI's operational priorities: adversary models, hijacking, jailbreaks, CCP narratives, adoption.
3. **NIST CAISI program page**, retrieved 27 Sep 2026 (`nist-caisi-page-2026`). It lists 2026 outputs, including joint UK AISI / CAISI cyber assessments (Kimi K3, Jul 2026). Useful for the AISI EOI context [V: titles only].
4. **NIST AI 800-1 2pd**, *Managing Misuse Risk for Dual-Use Foundation Models*, US AISI, Jan 2025 (`nist-2025-managing`). The best US source for defining **misuse** (§7). Its Practice 3.1/3.2 add to B7/B8.
5. **NIST AI 100-2e2025**, *Adversarial Machine Learning: A Taxonomy and Terminology* (`vassilev-2025-adversarial`). The definitional source for B14 terms. The CAISI RFI cites it.
6. **RAND-SL3 controls repository**, https://github.com/RANDCorporation/achieving-AI-model-weight-sl3 (control data v1.5). Not filed separately; referenced in the `aguirre-2026-sl3` note. It is the basis for the family counts in §3.

---

## 7. Definitions record (raw, not reconciled)

Format: term → source, location, verbatim. "Undefined" means the source uses the term load-bearingly without defining it.

### Loss of control / AI acting outside human direction

This is the scale spectrum Joseph asked about. Five distinct scales appear in my set alone.

- **NIST 600-1, p. 3:** not addressed. "speculative risks that may potentially arise in more advanced, future GAI systems are not considered."
- **NIST AI 800-1 2pd, Glossary p. 22** (from EO 14110), as a *capability criterion* for "dual-use foundation model": "permitting the evasion of human control or oversight through means of deception or obfuscation." Scope note, p. 1 fn vii: "This document also does not cover risks from accidental AI harms to public safety."
- **CAISI RFI, p. 699** (agent/system security scale): "the risk that the behavior of uncompromised models may nonetheless pose a threat to confidentiality, availability, or integrity (e.g., models that exhibit specification gaming or otherwise pursue misaligned objectives)."
- **AISP, p. 82** (host-infrastructure scale): "AI systems – particularly autonomous agents with broad system access – could be used to attack the infrastructure that hosts them … Note: the vast majority of work on this would also have benefits if an AI model started behaving as an attacker even without a separate threat actor directing it to do so." p. 98: "prevention of specific actions by unaligned AI (e.g., self-exfiltration)."
- **RAND-ISL, codebook p. 34 [44]** (data-exfiltration scale): "Misaligned AI exfiltration: Scenarios in which an AI system, because of misalignment or unintended behavior, leads to the unauthorized exfiltration of data or insights."
- **RAND-G, p. 6 [11]** (global/strategic scale): "In the extreme, a loss-of-control scenario could result, wherein AGI's pursuit of its desired objectives incentivizes the machine to resist being turned off, counter to human efforts … AGI might achieve enough autonomy and behave with enough agency … to be considered practically an independent actor on the global stage." "Misaligned" (p. 6): "operate in ways that are inconsistent with the intentions of its human designers or operators, causing unintentional harm."

### Insider threat

- **RAND-W, OC3 definition, p. 10 [20]:** "attempts by insider threats within the organization, who will have significantly less resources and expertise than the previous operations described as part of this category but significant access to sensitive organization resources (e.g., a senior member of the organization's research team)."
- **RAND-W, p. 67 [77]:** "while this category focuses on human intelligence and intentional insider threats, a large portion of insider risk results from nonmalicious insiders."
- **RAND-W, p. 67 [77]** (on how recruitment works): "the adversary need not tell the employee who they are and can easily pretend to be any other actor."
- **RAND-ISL, p. 13 fn 1 [23]:** "An insider with legitimate access to insights who transfers those insights to an unauthorized party is acting without authorization under this framework, and insider threats are addressed as a distinct attack vector category."
- **NIST AI 800-1 2pd, p. 12:** "an individual involved in developing or deploying the model who may behave maliciously or collaborate with an external attacker."
- **AISP, p. 43:** insiders "compromised through financial pressure, foreign recruitment, or ideological motivations." AISP p. 82 extends the concept to AI agents ("combine … insider and outsider threats").
- **RAND-SL3:** undefined beyond inheriting OC3. PM-12 scopes an insider-threat program.
- **NIST 600-1:** term absent.

### Security level

- **RAND-W, Fig. 6.1, p. 22 [32]:** SL1–SL5 are each defined as "a system that can likely thwart" OC1…OC4; SL5 "could plausibly be claimed to thwart most top-priority operations by the top cyber-capable institutions (OC5)." p. 21: "not meant to be used as a standard."
- **RAND-W, OC1–OC5, Fig. 4.1, p. 10 [20].** Budget/team/time bands, e.g. OC4 "comparable to 100 individuals … spending a year with a total budget of up to $10 million."
- **RAND-W, feasibility scores, Table 5.2 note, p. 17 [27]:** "A score of 1 represents up to a 20 percent chance of success … 5 represents more than 80 percent chance of success." The victim is assumed to be at SL1 (Box 5.1).
- **RAND-ISL, p. 1 [11]:** "we refer to SLs for protecting algorithmic insights as insight SLs (ISLs 1 through 5), distinguishing them from the weight SLs (WSLs 1 through 5)."
- **RAND-SL3, p. v:** SL3 = "140 standard security controls and 122 supplemental controls drawn from NIST SP 800-53." p. 17 recommends it be "voluntary in its whole and its parts."
- **AISP, p. 38:** SL-3/4/5 are glossed as "moderately sophisticated attackers" / "highly sophisticated attackers" / "nation-state adversaries with billion-dollar budgets". These glosses differ in wording from RAND-W's OC definitions.

### Misuse

- **NIST AI 800-1 2pd, Glossary p. 22:** "Misuse Risk: A risk that an AI model will be deliberately misused to cause harm." p. 12 fn x: "unauthorized use, which here refers to an entity misusing technical access that they have been granted legitimately … such as by jailbreaking a model or violating its terms of service." This is distinct from "Unauthorized Access" (Glossary p. 23).
- **NIST 600-1:** undefined. It uses "the abuse, misuse, and unsafe repurposing by humans (adversarial or not)" (pp. 2–3).
- **RAND-W:** undefined. The title's "Misuse" refers to misuse of *stolen* weights.
- **CAISI statement:** term absent.

### AI security / frontier AI

- **AISP, p. 12:** "'AI security' has come to encompass the security challenges, capabilities, and practices that arise at the intersection of cybersecurity and AI … This is the definition of AI security we adopt throughout this paper." "frontier AI to refer to the most capable general-purpose AI systems at or near the leading edge of current development."
- **RAND-W, p. iii:** "frontier artificial intelligence (AI) models – that is, models that match or exceed the capabilities of the most advanced AI models at the time of their development."
- **CAISI statement:** "demonstrable risks" is undefined, given only by example (cyber, bio, chem). "national security standards" is undefined.

### Algorithmic insights

- **RAND-ISL, p. 4 [14]:** "Algorithmic insights are the novel techniques, methods, or design know-how that materially improve the efficiency, performance, deployability, or similar desirable features of AI systems." Exclusions (p. 5): "model weights and raw datasets … general machine learning (ML) knowledge that is already public."

### Weights

- **RAND-W, p. v:** "its weights, a term used here to refer to all learnable parameters derived by training the model on massive datasets."

### Agent / agentic AI

- **CAISI RFI, p. 699:** "AI agent systems consist of at least one generative AI model and scaffolding software that equips the model with tools to take a range of discretionary actions … They can be deployed with little to no human oversight. Other terms used to refer to AI agent systems include AI agents and agentic AI." The RFI is scoped to systems "capable of taking actions that affect external state, i.e., persistent changes outside of the AI agent system itself."

### Attacks on AI systems (B14)

All from NIST AI 100-2e2025, Glossary.
- **Prompt injection:** "An attack which exploits the concatenation of untrusted input with a prompt constructed by a higher-trust party such as the application designer."
- **Indirect prompt injection:** "A type of PROMPT INJECTION executed through RESOURCE CONTROL rather than through user-provided input."
- **Jailbreak:** "A DIRECT PROMPTING ATTACK intended to circumvent restrictions placed on model outputs, such as circumventing refusal behaviour to enable misuse."
- **Data poisoning:** "A POISONING ATTACKS in which an adversary controls part of the training data." [sic]
- **Backdoor poisoning attack:** "A poisoning attack that causes a model to perform an adversary-selected behaviour in response to inputs that follow a particular BACKDOOR PATTERN."

### Other NIST 600-1 terms

- **Risk, p. 2:** "the composite measure of an event's probability (or likelihood) of occurring and the magnitude or degree of the consequences."
- **Confabulation, p. 6:** "GAI systems generate and confidently present erroneous or false content."
- **Information integrity, p. 9:** quoted from the 2022 White House Roadmap.
- **Algorithmic monoculture, p. 2 fn 3:** quoted in §1.14.
- **AI incident, p. 52:** the full definition, incl. "disruption of the management and operation of critical infrastructure."
- **AI red-teaming, p. 49:** "A structured testing exercise used to probe an AI system to find flaws and vulnerabilities."

### Manipulation

The pooling risk here is between NIST's "Information Integrity" (mis/disinformation at scale, p. 9) and CAISI's "malign foreign influence arising from use of adversaries' AI systems" (statement). Neither defines "manipulation." RAND-G uses "manipulate public opinion through advanced propaganda techniques" (p. 4). All three differ from the EU's harmful manipulation, whose definition is not in my set.

---

## 8. relata bibkeys created (13)

All have the document attached and byte-verified in the store (`relata show <key>`).

| Bibkey | Work | Kind |
| --- | --- | --- |
| `nevo-2024-securing` | RAND-W, RR-A2849-1 | primary PDF |
| `rand-2024-weights-press` | RAND press release 30 May 2024 | secondary; rendered from HTML |
| `mitre-2025-agi` | RAND-G, PE-A3691-4 | primary PDF |
| `brassgershovich-2026-algorithmic` | RAND-ISL, RR-A4685-1 | primary PDF |
| `aguirre-2026-sl3` | RAND-SL3, RR-A4704-1 | primary PDF |
| `gekker-2026-aisp` | AISP, arXiv 2607.26069 | primary PDF |
| `nationalinstituteofstandardsandtechnologyus-2024-artificial` | NIST AI 600-1 | primary PDF; auto-created via Crossref; title field truncated |
| `nist-2025-managing` | NIST AI 800-1 2pd | primary PDF; auto-created; author field odd |
| `vassilev-2025-adversarial` | NIST AI 100-2e2025 | primary PDF; auto-created |
| `commerce-2025-caisi` | Commerce CAISI statement, 3 Jun 2025 | primary text via Wayback, rendered to PDF with a provenance header |
| `nist-caisi-page-2026` | nist.gov/caisi | primary web page, rendered |
| `nist-2025-caisi-deepseek` | NIST release on DeepSeek eval | secondary to the unretrieved full report; rendered |
| `nist-2026-rfi-agents` | CAISI RFI, 91 FR 698 | primary PDF (govinfo) |

The RAND-ISL landing-page summary is the actual origin of the report's current fn 19 quote. It is not a separate entry; its text is quoted verbatim in §1.1. The web-derived PDFs are plain-text renderings of extracted page text, each headed with the source URL and retrieval date.

---

## 9. Coverage: what I read and how

- **Read whole:**
  - RAND-ISL: body and Appendices A–D in full; Appendix E and references skimmed.
  - RAND-SL3: all.
  - AISP: all, including appendices.
  - RAND-G: all.
  - Commerce statement, CAISI page, DeepSeek release, CAISI RFI: all.
- **Read in part:**
  - RAND-W: body (chs. 1–7) in full. Appendix A's HUMINT section in full; the other attack-vector appendices by search. Appendix B's SL3/SL4 personnel, access and organizational sections in full.
  - NIST 600-1: §§1–2 (all 12 risks) and Appendix A in full. The §3 action tables were read for Govern 1.3–6.2 and searched for the rest.
  - NIST AI 800-1: scope, Practices 3.1–3.2, and glossary.
  - NIST AI 100-2e2025: glossary entries only.
- **Searched across all eight texts:** the growth/turnover/IPO sweep, loss-of-control terms, and the crosswalk terms quoted above. So "not found" in my cells means not found in full text for these documents.
- **Not done:**
  - the full CAISI DeepSeek report;
  - CAISI blog posts;
  - America's AI Action Plan (July 2025), which assigns CAISI tasks. It is linked from the NIST release and is a likely next source for "US posture."

---

## 10. Feedback on the brief

The brief worked well. Three things helped most:
- naming §4's interpretation as the claim worth judging, not just checking;
- Joseph's loss-of-control illustration, which turned the definitions record from a chore into a search with a target;
- the explicit license to quote at length.

One friction point: the crosswalk has no stated rule for which documents feed a pooled column (RAND, CAISI). I had to infer it, and the answer changes cell values. A one-line column-provenance note in the report would help future checkers.

I'm available for follow-ups.
