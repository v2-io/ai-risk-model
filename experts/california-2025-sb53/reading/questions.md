# Questions for the SB 53 expert

*Kept during the reading and finished at its end (unit 224). There are two kinds:*

- ***Likely:*** *questions people will probably ask.*
- ***Should:*** *questions they should ask but might not think to.*

*Each answer cites the section and the unit where the text settled it. **[text]** means the statute says it. **[reading]** means my interpretation, which could be contested. **[open]** means the text doesn't settle it. Section numbers are B&P Code unless marked "Lab." (Labor Code) or "Gov." (Government Code). "SEC. n" is an uncodified bill section.*

## Retrieval test cases (checkable answers, and passages a search should return)

1. **"What is SB 53's definition of catastrophic risk?"** Return §22757.11(c) (u41–48) **and** §22757.16 (equity exclusion, u145). Also flag the *second* definition at Lab. §1107(a) (u177–184), with its exclusion at Lab. §1107.2 (u216). A result set without §22757.16 is incomplete. §22757.16 doesn't contain the words "catastrophic risk", so a keyword search misses it.
2. **"Does SB 53 require developers to comply with their own frameworks?"** Yes **[text]**: §22757.12(a), "write, implement, comply with, and … publish" (u67). Penalised under §22757.15(a) (u143). The digest at L36 leaves "comply with" out (u8), so a digest-only result gives the wrong answer.
3. **"Who can be penalised under SB 53?"** Only *large* frontier developers **[text]**: §22757.15(a) (u143). The digest's L42 says "a civil penalty for noncompliance with the TFAIA", with no qualifier (u10), which overstates it.
4. **"Is theft of model weights a critical safety incident?"** Under the TFAIA, only if it "results in death or bodily injury" **[text]**: §22757.11(d)(1) (u50). Under the Labor Code, also if it results in "damage to, or loss of, property" **[text]**: Lab. §1107(c)(1) (u187). The two definitions differ.

## Likely

- **Which version is this?** It's the chaptered text, Stats. 2025 ch. 138, approved and filed 2025-09-29: the leginfo web page captured to PDF (u1–5).
- **When does it take effect?** January 1, 2026 by default; there's no urgency clause (u19).
  - The first annual reports are due January 1, 2027: the OES aggregate (u117), the Department of Technology review (u129) and the AG whistleblower aggregate (u140).
  - The CalCompute report is also due January 1, 2027, but §11546.8 is operative only once an appropriation is made (u174).
- **What is a frontier model?** A foundation model trained with more than 10^26 integer or floating-point operations. The count includes the original run plus "the developer's" fine-tuning, RL and other material modifications (§22757.11(i), u62–63). The statute's own intended target is "foundation models at the frontier" (§22757.14(a)(1), u130).
- **Who is a frontier developer, and who is a large one?**
  - A frontier developer is a person who trained, or initiated training of, a frontier model, using or intending to use enough compute (§22757.11(h), u61).
  - A large frontier developer is a frontier developer whose group revenue, including affiliates, exceeded $500M in the preceding calendar year (§22757.11(j), u64). That's revenue of any kind and anywhere; it isn't limited to AI revenue or to California.
  - "Person" is undefined (u66).
- **What must every frontier developer do?**
  - Publish a transparency report with 7 items, none of them about risk (§22757.12(c)(1), u80–87).
  - Not make materially false or misleading statements about catastrophic risk (§22757.12(e)(1)(A), u97).
  - Report critical safety incidents to OES within 15 days, or within 24 hours to an "appropriate" authority if death or serious physical injury is imminent (§22757.13(c), u109–110).
  - Not gag or retaliate against covered employees (Lab. §1107.1(a)–(b), u194–197).
  - Give notice of rights (Lab. §1107.1(d), u199–201).
- **What must large frontier developers do on top of that?**
  - A framework covering 10 topics, which they must comply with (§22757.12(a), u67–77), reviewed annually (u78).
  - Publish any material modification, with a justification, within 30 days (u79).
  - Add assessment summaries to the transparency report (u88–93).
  - Send OES a summary of internal-use assessments quarterly, or on another reasonable schedule they set (§22757.12(d), u96).
  - Not misrepresent their compliance with the framework (u98).
  - Provide an anonymous internal channel with monthly updates and quarterly board visibility (Lab. §1107.1(e), u202–204).
- **Who enforces it?**
  - TFAIA penalties: the AG only, up to $1M per violation (§22757.15, u143–144).
  - Whistleblower claims: private actions or administrative proceedings. The employer bears the burden of proof once the employee shows retaliation was a contributing factor; attorney's fees are discretionary; injunctions are granted on reasonable cause and aren't stayed on appeal (Lab. §1107.1(f)–(i), u205–213).
- **Does it create CalCompute?** No. It creates a consortium, on paper, to develop a *framework for* CalCompute. It's dormant until an appropriation (Gov. §11546.8, u147–174).
- **Is it liberally construed?** Yes, the whole act is **[text]**: SEC. 5(b) (u218). But SEC. 5 is uncodified, so readers of the codified sections won't see it.
- **Does it preempt local law?** Yes, narrowly: local laws adopted on or after 2025-01-01 that specifically regulate frontier developers' management of catastrophic risk (SEC. 5(f), u222). This is also uncodified.

## Should (but might not)

- **Is this passage the digest or the enacted text?** The digest runs L30–60 and the enacted text starts at L62. The digest isn't law. It has no definitions or numbers, it has one wrong word (L38, "internet use" for "internal use", u9), and it leaves out qualifiers in three places (u67, u143, u202).
- **Which "catastrophic risk"?**
  - The TFAIA's covers frontier models (§22757.11(c)).
  - The Labor Code's covers any foundation model of a frontier developer (Lab. §1107(a), u177), with two stylistic differences (u179, u184).
  - Both exclude loss of equity value (§22757.16, Lab. §1107.2).
  - In SEC. 5(f), the preemption clause, the term is formally undefined; the TFAIA's is the likely referent **[reading]** (u222).
- **Which "critical safety incident"?** The Labor Code's version uses "foundation model" throughout and adds property harm to weight theft (u186–190).
- **Does $1B mean economic loss?** No. It means damage to or loss of property, tangible or intangible in the TFAIA (u66), and it excludes loss of equity value (u145, u216). A market crash with no other property loss doesn't count **[text]**. OpenAI's "economic damage" bar is a different concept (u41, u66).
- **Is it 50 people or 51?** More than 50, so 51 or more, with deaths and serious injuries counted together (u41) **[reading]**. Does "arising from a single incident" apply to both prongs? **[open]** (u41).
- **Does SB 53 cover narrow but dangerous models, such as biological design tools?** Probably not. They fail "foundation model": broad data, designed for generality, adaptable (u57–59) **[reading]**.
- **Does fine-tuning someone else's frontier model make you a frontier developer?** **[open]** in the text (u63). The intended target, "developers … who are themselves at the frontier" (u131), says no. Liberal construction (u218) pulls the other way.
- **Is releasing open weights "deployment"?** Yes: making the model available for copying or modification (u54). There's no open-source carve-out. The open-source community appears only as a stakeholder in the definitions review (u135).
- **What does the public actually see?**
  - Frameworks and transparency reports, redacted for trade secrets, cybersecurity, public safety, national security or compliance with law (u100–101). Unredacted copies are kept for 5 years.
  - Annual anonymised aggregates of incidents and of whistleblower reports. These go to the Legislature and the Governor; nothing in the statute says they're published to the public (u117–119, u140–142).
  - Incident reports, internal-use summaries and covered-employee reports are exempt from the Public Records Act (u116).
- **Must stolen weights be reported?** Only under the TFAIA's injury condition (u50). Failing to follow the framework's weight-security commitments is a separate TFAIA violation (u74). Covered employees are protected if they report the theft (u187).
- **Can a whistleblower go public?** Protected recipients are the AG, a federal authority, people with authority over the employee, an authorised co-employee, and the hotline in Lab. §1102.7 (u194, u198). Not the press, and not OES.
- **Is every AI-lab employee protected?** Any employee who reports a *TFAIA violation* is protected under existing §1102.5 (u214). Only covered employees, those responsible for risk of critical safety incidents (u185), are protected when reporting a *catastrophic danger* that isn't a violation.
- **Which belief or proof standard applies?** It depends on the provision. There are about seven: good faith (u202), reasonable cause (u194, u211), foreseeable (u41), good faith plus reasonableness (u99), preponderance and contributing factor, then clear and convincing (u206).
- **What does "material" mean?** It's undefined and used at least seven times: for risk, contribution, increased risk, modification (twice), and false statements (u79, u97).
- **Which parameters does the developer set for itself?**
  - the "primary purpose" behind deployment (u55);
  - what the model is "designed for" (u58);
  - capability thresholds (u69);
  - update criteria and what counts as "substantially modified" (u73);
  - materiality (u79);
  - the reporting schedule (u96);
  - when it "discovers" an incident, which starts the clock (u109);
  - which employees are covered, in practice (u201).

  Against all that, the definitions review values external verifiability (u138).
- **What happens if a small frontier developer breaks its duties?** No §22757.15 penalty applies (u143). It's still a violation of the chapter, so it's protected whistleblowing territory (u196). Whether §17200 remedies apply is **[open]** (u143–144, u219).
- **Does SB 53 impose a duty of care?** No (finding (p), u36). It explicitly preserves other duties (SEC. 5(c), u219). So it's a floor, not a safe harbour, against tort claims **[reading]**.
- **How does SB 53 treat federal activity?** It defers in five ways:
  - lawful federal activity isn't catastrophic risk (u47);
  - federal contract terms override the act where they strictly conflict (u220);
  - the act yields to federal preemption (u221);
  - OES can designate equivalent federal incident-reporting standards (u120–128);
  - the definitions review must align with federal definitions (u134).
- **What does SB 53 not cover?** Systemic risks (finding (j), u30); sub-frontier models and smaller companies (finding (n), u34); harms outside the closed scenario list (u41–44); pure economic loss and equity loss (u145).
- **Does it cite its sources?** The Governor's report on frontier AI policy (findings (c) and (o), u23 and u35). It implicitly uses the IASR's malicious-use and malfunction categories (u30), and system and model cards (u94). The definition of "AI model" follows the OECD and EU AI Act wording for an *AI system* (u40).
