# My developing picture of SB 53

*A running outline, revised at strategic-loop moments. Each revision notes the unit it was written at. Older states are kept in git history, not here.*

## As of unit 20 (end of the digest)

**Edition.** SB 53 as chaptered: Stats. 2025, ch. 138. Approved and filed 2025-09-29. A leginfo web page captured to PDF. Units 1–2 are site chrome.

**Two authors in one document.**
- L30–60: the Legislative Counsel's Digest. A summary, not law; written in the conditional ("would"); no definitions or numbers. It has at least one wrong word: unit 9, "internet use" for "internal use".
- From L62: the enacted text.

**Architecture (from the digest; still to be confirmed in the text).**
1. **B&P Code, new Ch. 25.1, from §22757.10: the TFAIA.**
   - A large frontier developer writes, implements and publishes a frontier AI framework. The digest does *not* say "comply with" (open).
   - It sends summaries of internal-use catastrophic-risk assessments to OES.
   - OES runs two mechanisms: one for critical safety incident reports from frontier developers *or members of the public*, and one for confidential internal-use assessment summaries.
   - These reports are exempt from the California Public Records Act, along with covered-employee reports.
   - Civil penalty, enforced by the AG.
2. **Government Code §11546.8: CalCompute.** A consortium in the Government Operations Agency develops a *framework for* a public cloud cluster. Its report is due 2027-01-01, and the consortium dissolves when it reports. **Operative only upon appropriation.**
3. **Labor Code, new Ch. 5.1, from §1107: whistleblowers.**
   - A frontier developer may not make rules or contracts that prevent a covered employee's disclosure to the AG, a federal authority, a supervisor or an authorised co-employee. The trigger is reasonable cause to believe either a specific and substantial danger from catastrophic risk, or a TFAIA violation.
   - A *large* frontier developer must provide an anonymous internal channel. Its trigger is good-faith belief.
   - Attorney's fees for successful plaintiffs.
4. **Local preemption (location TBD):** local laws adopted on or after 2025-01-01 that specifically regulate frontier developers' management of catastrophic risk.
5. **PRA findings section** (expected).

**Tiered actors (a hypothesis).** Foundation model → frontier model (compute) → frontier developer (trained one) → large frontier developer (revenue). Obligations attach at different tiers:
- framework and internal process: *large* frontier developers;
- incident reporting and the anti-retaliation rule: all *frontier developers*.

**Other actors:** OES, the AG, the Government Operations Agency, the Department of Technology, members of the public, covered employees, "a federal authority".

**Two vocabularies of good:**
- aspirational, for CalCompute: "safe, ethical, equitable, and sustainable";
- threshold, for the TFAIA: "catastrophic", "critical".

**Regulatory theory:** information channels (disclosure, incident reporting, whistleblowing). The only conduct mandate so far is "implement" the framework. Whether self-commitments are enforceable is the hinge (see questions).

## As of unit 102 (start of §22757.13, the OES mechanism)

**SEC. 1, findings (a)–(p)**, L64–84. It moves from boosterish (a–h) to risk-aware (j–o) to an honest limit (p).
- Risk is never asserted in the Legislature's own voice: "there is concern that" (j); "could pose potential" (o).
- (j) borrows two of the IASR's three risk categories (malicious use, malfunctions) and leaves out systemic risk.
- (l): frontier AI frameworks are an existing voluntary industry practice, now made mandatory.
- (n): sub-frontier and smaller-company models are a declared gap.
- (p): intent is transparency only; safety also needs "due care … proportional to … foreseeable risks", which the act doesn't impose.
- No finding for CalCompute.

**SEC. 2 = B&P Ch. 25.1 = the TFAIA** (the TFAIA is this chapter only; SB 53 is broader).
- §22757.10: short title.
- §22757.11: twelve definitions, (a)–(l). "Person" is undefined; "property" is tangible or intangible.
  - Catastrophic risk ((c)) carries about eleven separable concepts: unit 48 has the inventory.
  - Critical safety incident ((d)) is a closed list of four. Three need harm, and (4), deception against the developer, needs none.
  - Deploy covers third-party availability, so open-weight release counts; access for evaluation doesn't.
  - Foundation model: broad data, *designed* for generality, adaptable.
  - Frontier model: >10^26 integer or floating-point operations, cumulative over original training plus "the developer's" modifications. Whether that crosses developers is a hinge.
  - Frontier developer: trained, or started training, with the compute actually used or intended.
  - Large frontier developer: group revenue over $500M in the preceding calendar year.
- §22757.12, the obligations:
  - (a) A *large* developer must write, implement, **comply with** and publish a framework that "describes how [it] approaches" 10 topics. It's a mandatory table of contents with an enforceable promise to follow it. **The digest omits "comply with".**
  - (b) Annual review; a material modification must be published with a justification within 30 days.
  - (c)(1) *Every* frontier developer publishes a transparency report at deployment, before or at the same time. Its 7 required items contain **no risk content**.
  - (c)(2) A *large* developer adds summaries of assessments, results, third-party involvement and other framework steps.
  - (c)(3) A system card or model card counts as compliance. (c)(4) Better-than-best-practice disclosure is encouraged, not required.
  - (d) A *large* developer sends OES quarterly summaries of internal-use catastrophic-risk assessments, or on another reasonable schedule it chooses.
  - (e) No materially false or misleading statements: about catastrophic risk (all developers), or about framework compliance (large developers). Safe harbour if made in good faith **and** reasonable.
  - (f) Redaction is allowed on 5 grounds. The character and justification of each redaction must be described, and the unredacted version kept 5 years.

**Recurring structural features:**
1. The developer sets its own parameters: primary purpose; designed for; thresholds; update criteria; "substantially modified"; materiality of modifications; the reporting schedule.
2. "Material(ly)" appears at least 7 times and is never defined.
3. There are four epistemic standards, depending on the provision.
4. There are four control phrasings (evade / lose / subvert / circumvent), none defined.
5. Enumerations aren't type-consistent: (c)(2)(C) is a harm, not a source; (d)(4) is a model, not an event.
6. Every outward interface carries summaries, not full assessments.

## Open hinges (to settle from the text)
- Does the TFAIA require compliance with one's own framework? This sets how wide whistleblower prong (b) reaches.
- Does the Labor Code chapter define "catastrophic risk" again, or cross-reference the B&P definition?
- Where is preemption codified?
- Are the digest's two belief standards ("reasonable cause" vs "good faith") in the statute too?
