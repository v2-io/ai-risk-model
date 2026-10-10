# The Sept 5 amendment, read as one package

*I read the whole of `history/diffs/lc-marked/08-2025-09-05-amended-assembly.marked.txt`: Legislative Counsel's own insert and strike marks, version 7 (Sept 2) to version 8 (Sept 5). After that I read lines 20–55 of the Sept 10 Assembly Privacy & Consumer Protection analysis, and the section file for the Jul 17-only audit clause. The final text that comes out of these marks matches the chaptered text I read. What follows is from the primaries, except where marked **[reading]** or **[agent]**.*

## In one sentence

**Before Sept 5, SB 53 was much closer to the California Report. The Sept 5 amendment is where most of the departures I listed in `ca-report/06` were made.** The Sept 10 analysis says the narrowing was done "to address opposition concerns", while opening with "This bill seeks to implement the report's recommendations."

## What Sept 5 removed (struck text, verbatim)

**The framework (then the "safety and security protocol")**
- The protocol had to "describe[] **in specific detail**". That became "describes how the large frontier developer **approaches**". New York's RAISE restored "in detail how … handles", so RAISE is closer to the pre-Sept 5 SB 53.
- Struck protocol items:
  - "(5) The degree to which the large developer's assessments of catastrophic risk and dangerous capabilities and the effectiveness of catastrophic risk mitigations are **reproducible by external entities**";
  - "(3)(C) The actions the large developer will take if each threshold is attained";
  - "(8) … whether the large developer has the **ability to promptly shut down copies** of foundation models … who the large developer will notify, and the timeline";
  - (1), on how it excludes models from coverage;
  - "the schedule, specified in days", for reporting on internal use.

**The transparency report**
- These items were struck (they applied to large developers):
  - "The results of any risk assessment … **why the information gathered … leads to the stated results**, and the steps taken to address any identified risks";
  - "**the time and extent of predeployment access** provided to any third party …, **whether or not the third party was independent**, and **the nature of any constraints** the large developer placed on the assessment or on the third party's ability to disclose information";
  - "Whether a catastrophic risk threshold or dangerous capability threshold has been attained … and any actions taken";
  - "The reasoning behind the large developer's decision to deploy …, and any limitations in the assessments".
- What replaced them: "summaries of … The extent to which third-party evaluators were involved", and so on.
- **The struck access, independence and constraints item is almost exactly the California Report's pre-deployment-testing recommendation** (report L558: "the time and depth of pre-deployment access provided … if the external party is paid … whether they are constrained in what they can disclose"). SB 53 had it, and Sept 5 took it out.

**Internal-use assessments went from public to confidential**
- Struck: "shall **clearly and conspicuously publish on its internet website** any assessment of catastrophic risk or dangerous capabilities resulting from internal use".
- Inserted: "shall transmit to the Office of Emergency Services a summary". So the confidential internal-use channel I treated as a design feature (u96, u108) was until Sept 5 a *public* duty to publish **full assessments**.

**Critical safety incidents**
- (1): weight access or exfiltration "of a foundation model". Previously **with no harm condition at all**. Sept 5 added "**that results in death or bodily injury**". (The Labor Code restatement, also new on Sept 5, kept a looser harm condition: "death, bodily injury, or damage to, or loss of, property".)
- (3): loss of control "causing death, bodily injury, **or damage to, or loss of, property**". The property clause was struck.
- (4), deception: "and in a manner that demonstrates materially increased catastrophic risk" was added.
- **(5) was struck entirely**: "**Attaining a dangerous capability or catastrophic risk threshold**, as defined in the large developer's safety and security protocol …, **for the first time**." Until Sept 5, crossing one of your own capability thresholds was a reportable incident.
- The Sept 10 analysis's own summary: "Reducing the scope of certain categories of critical safety incidents to those that actually result in harm."

**Catastrophic risk**
- "arising from a single **incident, scheme, or course of conduct**" became "a single incident". **The counting rule was narrowed here.**
- "involving a **dangerous capability**" (a separately defined *capacity*) became "involving a frontier model **doing** any of the following". From what the model *can* do to what it *does* **[reading, but the text is plain]**.
- The struck "Dangerous capability" list had "(2) **Conduct or assist in** a cyberattack". The new (B) is only autonomous cyberattack ("with no meaningful human oversight"). **A model that helps a human carry out a cyberattack is no longer a catastrophic-risk scenario.** That's a big narrowing, and I couldn't have seen it from the final text alone.
- "with **limited** human intervention" became "with **no meaningful** human oversight, intervention, or supervision", which is stricter.
- New on Sept 5: the three exclusions (public information, federal activity, combination with other software) and the equity sections, §22757.16 and Lab. §1107.2.

**Scope and adaptivity**
- Struck: the Attorney General's power to redefine "large developer" **by regulation** from 2027. That was adaptive scope, close to the California Report's L710/L770. It was replaced by the Department of Technology's recommend-only report.
- Struck: the old §22757.14(c). If the AG found that less well-resourced developers "may create substantial catastrophic risk", it had to report to the Legislature with a proposal. Finding (n) is what remains of it.
- New: the "frontier developer" tier (compute only), with duties but no penalty (u143). The Sept 10 analysis: "subjecting frontier developers that make less than $500 million to a less stringent transparency report."

**Penalties**
- The tiered schedule was struck:
  - an unknowing violation without material risk: ≤$10,000, with a **30-day cure** for a first violation;
  - knowing, or with material risk: ≤$100,000;
  - knowing *and* creating material risk of death, serious injury or catastrophic risk: ≤$1M for a first violation and **≤$10M for subsequent ones**.
- It was replaced by a flat "≤$1M per violation, dependent upon the severity". The new list of four violation types appears here too. So repeat or severe violations lost the $10M tier, and minor ones lost the cure period **[reading: on balance a weakening at the top]**.

**Whistleblowers**
- "Employee" was struck. It had covered "A contractor, subcontractor, or an unpaid advisor …, an independent contractor, a freelance worker, a person employed by a labor contractor, a board member" and "Corporate officers". It was replaced by the role-gated, employee-only "covered employee". **The California Report's final version added non-employees (L852). SB 53 had them until Sept 5.**
- Struck: protection for *vendor organizations* (the old §1107.1(c)) that provide catastrophic-risk services.
- Prong (1) "pose a catastrophic risk" became "pose a **specific and substantial danger** to the public health or safety resulting from a catastrophic risk", which is narrower.

**Regulator.** The whole incident regime moved from the **Attorney General to OES** on Sept 5. That's the emergency-management framing I wondered about at u8: it's a late choice.

**Findings**
- "(k) **There is growing evidence that**, unless …" became "(j) Unless …, **there is concern that** …". **The one agentless hedge I singled out at u30 was put in on Sept 5, replacing an assertion of evidence.**
- Struck: "(e) Artificial intelligence developers have already voluntarily committed to creating safety and security protocols and **releasing the results of risk assessments**."
- "(g) … **a significant information asymmetry can develop** between those with privileged access to data and the broader public" (the California Report's own phrase, L468) became the trust-framed "(f) … public trust … would significantly benefit".
- "given current information deficits" was struck (the report's Principle 5 wording).
- "Adverse event" became "Incident".
- Added: (l) the voluntary-frameworks finding, (m) timely incident reporting, (o) the report and the hearings.

**Digest.** The "internet use" error (u9) was **inserted** in this amendment, along with the rest of the internal-use sentence.

**Local preemption** (SEC. 5(f)) was added on Sept 5.

## Before Sept 5: the Jul 17 audit clause (one version only)

"Beginning January 1, 2030, and at least annually thereafter, a large developer shall retain an **independent third-party auditor**" to assess "(1) Whether the large developer has substantially complied with its safety and security protocol and any instances of substantial noncompliance" and "(2) Any instances in which [the protocol] has not been stated clearly enough to determine whether the large developer has complied". The auditor would have had access to all materials, at least one compliance expert and one technical safety expert, a summary sent to the AG within 30 days, and a duty not to misrepresent. The Sept 10 analysis lists the first narrowing as "Omitting the requirement for independent audits starting in 2030."

This would have answered the EU expert's question ("does SB 53 require any self-assessment of adherence?"). For one version, SB 53 had an *external* annual audit of adherence. **[agent]:** the history agent places its removal before Sept 5 (it exists in v06 only). The Sept 10 analysis counts it among the narrowings since the committee's earlier vote.

## Who, per the Sept 10 analysis

- Sponsors: Encode Justice, Secure AI Project, Economic Security California Action.
- Support: "a large coalition of civil society, labor, AI safety groups, and Anthropic".
- Opposed: the Silicon Valley Leadership Group and the Chamber of Progress.
- Oppose unless amended: CalChamber, CCIA, TechNet.
- The analysis says some positions may not have been updated after the late amendments.

**Conflict of interest, per the repo's principle:** Anthropic supported the final, narrowed text. That doesn't tell us which narrowings Anthropic wanted. A positions survey is running separately.

## What this changes in my earlier notes

- `ca-report/06`: the departures are real in the final text. **Historically, most were made on Sept 5, after the bill had carried the report's approach.** The precise statement is "SB 53 enacted the report's approach and then narrowed it in its last substantive amendment, to address opposition."
- u30 (the "there is concern that" hedge), u50 (weight theft needs injury), u53 (deception), u96/u108 (confidential internal use), u143 (penalties for large developers only), u185 (role-gated whistleblowers): all of these features arrived on Sept 5, and most replaced stronger text.
- u41 (the counting rule) and u43 ((B) crimes and cyber): "single incident" and autonomous-only cyber were both Sept 5 narrowings. Assisting a human cyberattack had been in scope.
- u123 ("the catastrophic risk", with a stray "the"): it arrived with the whole federal-equivalence section on Sept 5. It isn't a leftover from earlier SB 53 text. Whether it's a leftover from wherever that section was drafted is open **[agent's finding, consistent with the marks I read]**.
