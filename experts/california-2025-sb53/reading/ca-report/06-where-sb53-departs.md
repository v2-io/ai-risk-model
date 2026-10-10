# Where SB 53 departs from the California Report on Frontier AI Policy

*Joseph's question, answered after reading the report whole (except the bibliography), with SB 53 freshly read. "The report" means Bommasani, Singer et al., "The California Report on Frontier AI Policy", Joint California Policy Working Group on AI Frontier Models, June 17, 2025 (`bommasani-2025-california`). Cites: report line numbers in `ref/canonical/`, and SB 53 units in `../NNN.md`. **[text]** means both texts say it. **[reading]** is my interpretation. The notes behind this are 01–05 in this folder.*

## In one paragraph

SB 53 is **built from the report**. Its findings copy the report's Key Principles nearly word for word. Its internal-use regime, its "circumventing oversight mechanisms" phrase, its weight-security topic, its whistleblower design (beyond violations of law, good faith, board and anonymous channels), its "comply with your own framework" lever, and its definitions-review criteria all trace to the report. Where it departs, it departs **consistently in one direction**. The report's theory is *trust but verify*. SB 53 enacts the *trust* (self-written frameworks, self-reported compute, self-set parameters, made enforceable) and drops most of the independent *verify*: third-party assessment, researcher safe harbours, metrics beyond compute and revenue, adaptive scope, agencies that can act. SB 53 also deleted the report's motto, "trust but verify".

## What SB 53 takes from the report

| Report | SB 53 | Unit/note |
|---|---|---|
| Principles 1, 4, 5, 6, 7 (L134–162) | Findings (d), (e), (g), (h), (i), near-verbatim | 01 |
| "follow through on stated safety practices … in safety frameworks" (L468) | "comply with" its framework, §22757.12(a) | u67; 03 |
| Governing internal deployment (L472–478) | Framework (a)(10); quarterly internal-use summaries to OES, §22757.12(d) | u77, u96; 03 |
| "circumventing oversight mechanisms" (L472) | the same phrase, (a)(10) | u77; 03 |
| Weight security "from both company-internal and company-external exfiltration" (L556) | (a)(7), "by internal or external parties" | u74; 03 |
| Whistleblowing beyond violations of law, e.g. breaches of the safety policy; "good faith" (L600) | The danger prong, plus "comply with" turning policy breaches into legal violations; good-faith standard for the internal channel | u195–196, u202; 03 |
| Board and anonymous reporting channels (L608) | Anonymous internal process; quarterly board visibility | u202–203; 03 |
| The WPA as the design model (L596) | "specific and substantial danger" | u195; 03 |
| Mandatory developer and voluntary public incident reporting (L712) | §22757.13(a), (c) | u102, u109; 04 |
| An initially narrow incident definition (L710) | A closed list of four | u49–53; 04 |
| Four-part design for incident reporting: events, information, reporters, recipients (L648) | §22757.13's structure | 04 |
| Determination time, measurability, external verifiability (L760–766) | §22757.14(b)(3)–(5) | u136–138; 05 |
| Federal harmonization pathways (L263) | Five federal-deference mechanisms | u221; 02 |
| Foundation-model vocabulary (L229; the CRFM lineage of the lead writer) | "Foundation model" | u56; 01 |

## Where SB 53 departs

Ranked by how much the departure changes what the law does **[the ranking is my reading]**.

1. **Third-party risk assessment.** The report calls it "essential" (L570) and recommends researcher safe harbours (L580), responsible-disclosure infrastructure (L582–590), and standardized evaluations drawing on federal institutions (L576). SB 53 deleted "third-party evaluations" from the report's Principle 6 when it wrote finding (h). It requires only that developers *describe their approach* to third parties and *disclose the extent* of their involvement (u72, u92). There's no safe harbour, no access right and no audit **[text]**.
2. **Thresholds.**
   - The report: "Generic developer-level thresholds seem to be generally undesirable" (L774). SB 53's "large" tier is generic gross revenue over $500M across the whole group (u64) **[text]**.
   - The report: compute "should not be used alone", and is best as "an initial filter" (L776–782). SB 53 uses compute as the decisive scope test (u62) **[text]**.
   - The report wants mechanisms that update values *and metrics* (L770), like the EU's Annex XIII flexibility and scientific-panel alerts (L768). SB 53 has an advisory review only (u129) **[text]**.
   - The report flags derivative models as essential to address (L747, L860). SB 53 leaves it ambiguous (u63) **[text]**.
3. **Incident and adverse-event scope.** SB 53 follows the report's "initially narrow" advice. But it gives **no agency authority to widen the criteria**, which the same paragraph recommends (L710) **[text]**. Also missing:
   - a pathway for existing regulators to act on reports (L722);
   - authority to share findings with other developers (L708);
   - reporting immunity, as in aviation's ASRS (L700, L858);
   - pre-market testing as a substitute for reporting (L718).

   SB 53 also excludes evaluation-elicited deception from incidents (u53). The report's evidence of evaluation awareness (L327) cuts both ways on that choice **[reading]**.
4. **What gets disclosed.** Of the report's five transparency areas (L552–562):
   - data acquisition: **absent** from SB 53 (left to AB 2013, which the report says is insufficient);
   - downstream impact: **absent**;
   - safety and security practices: present;
   - pre-deployment testing: weak. Only "the extent" of third-party involvement is disclosed, with none of the rigor or independence fields the report lists, such as access time and depth, payment, and disclosure constraints (L558).

   The report's distribution-channel reporting (model hosts and inference providers; L562) has no counterpart: SB 53 regulates developers only **[text]**.
5. **Who is protected as a whistleblower.** The final report *added* protection for non-employees (L852) and notes that most protections cover all employees (L598). SB 53 covers employees only, and only role-gated "covered employees" for the danger prong (u185, u214) **[text]**. (In one place SB 53 goes further: it bars gag contracts, which the report deliberately left aside, fn 6, L604.)
6. **Public-facing against confidential.** The report's default is public transparency (L550), with disclosure to government only "in some cases" (L540). SB 53's main risk channels (incidents, internal-use assessments, whistleblower reports) are confidential and exempt from the Public Records Act (u116). What's public is self-description plus an anonymized annual aggregate sent to the Legislature (u117–119) **[text]**.
7. **No plan to use what's disclosed.** The report says transparency without "a concrete plan of action for how to analyze and base future decisions on disclosed information" risks "transparency washing" (L616, L634). SB 53 assigns no one to analyse published frameworks or transparency reports **[text: none found]; the "washing" risk is [reading]**.
8. **The carrot.** The report argues that verified transparency *reduces developers' liability exposure* (L452, L576, L632). SB 53 preserves every other remedy (SEC. 5(c), u219) and offers no liability benefit for compliance **[text]**.
9. **Framing of risk.**
   - SB 53's findings never assert risk in the Legislature's own voice ("there is concern that", u30). The report's executive summary does: "powerful AI could induce severe and, in some cases, potentially irreversible harms" (L136). That sentence never made it into SB 53.
   - The report recommends "marginal risk" (L309). SB 53 uses a binary exclusion for publicly available information (u46).
   - The report's CBRN evidence is framed as novice uplift (L319–321). SB 53's scenario is "expert-level assistance" (u42).

   **[text for each; the significance is my reading]**

## The pattern, stated once

SB 53 keeps the report's **disclosure and self-commitment** half, and keeps or strengthens its **whistleblower** half within employment. It drops or weakens the **independent verification** half: third parties, adaptive and multi-metric scope, agency authority, public analysis. It even deletes the report's motto. A reader who takes SB 53's own claim at face value ("The Joint California Policy Working Group … has recommended sound principles", finding (c)) would assume SB 53 implements those principles. **It implements the principles it copied into its findings, and leaves out the one it cut from Principle 6.**

## What I'd still like to check (open)

- Whether the amendment history shows third-party provisions that existed in an earlier SB 53 draft and were later removed. The background agent is fetching the versions.
- Whether the Governor's signing message frames SB 53 as implementing the report, and how.
- How RAISE's choices line up against the report's. For example, RAISE's rulemaking power to add reporting (§1429) is closer to the report's L710 than SB 53 is.
