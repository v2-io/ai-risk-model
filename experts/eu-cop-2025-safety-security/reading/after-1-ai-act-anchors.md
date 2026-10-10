# After the reading, 1: the AI Act provisions the Code builds on; a PDF check

*Read 2026-10-09, after the Code, not experientially (Joseph: experiential reading is for the core document only). Source: `ref/canonical/eu-2024-ai-act.md`, read in targeted ranges.*
- *Art. 2(3), L575–579*
- *Art. 3(49), L662–666*
- *recitals 110 and 114–115, L358–374*
- *Arts. 51–56, L1571–1688*

***Caveat:** this canonical text is the Act as adopted in 2024. The catalog says it was amended by the Digital Omnibus on AI (Reg. (EU) 2026/1744, 8 July 2026), which I haven't read. Anything below may have been changed by it.*

## PDF check (physical pp. 6–34, pdftotext)

- **C1's LEGAL TEXT** in the PDF: "Articles 55(1) and 56(5), and recitals 110, 114, and 115 AI Act". The canonical text's "Articles and 56(5), and recitals 110, and AI Act" is **conversion damage**.
- **C10's LEGAL TEXT** in the PDF: "Articles 53(1)(a) and 55(1) AI Act". The canonical text's "Articles 53(1)(a) and AI Act" is **conversion damage**.
- **Appendix 1, "ADDITIONAL LEGAL TEXT: Recital 110 AI Act"**: the PDF also has nothing under it; the next line is Appendix 1.1. So the Code itself only names the recital, and **nothing is lost**. (My unit-88 note left this open.)
- The other LEGAL TEXT lines match.

## What the Act says, and what that changes in my reading of the Code

**Art. 55(1), the obligations the Chapter implements.**
- (a) "perform model evaluation in accordance with standardised protocols and tools reflecting the state of the art, including conducting and documenting adversarial testing";
- (b) "assess and mitigate possible systemic risks at Union level, including their sources, that may stem from the development, the placing on the market, or the use of general-purpose AI models with systemic risk";
- (c) "keep track of, document, and report, without undue delay… relevant information about serious incidents and possible corrective measures";
- (d) "ensure an adequate level of cybersecurity protection for the general-purpose AI model with systemic risk and the physical infrastructure of the model".

What this changes:
- **The development / market / use triad comes from the Act**, from 55(1)(b), not from the Code. So when the Code reaches internal use, it's tracking the Act's own wording. My unit-12 note that "internal use is a stretch of the Act's scope" was wrong: the Act says "use", and the Code defines it as including the signatory's own.
- **"State of the art"** also starts in the Act (55(1)(a)), for evaluations. The Code generalises it to every Measure through recital (a) and the Glossary.
- C6's wording ("adequate level of cybersecurity protection… physical infrastructure") is 55(1)(d) word for word.

**Art. 55(2) and Art. 53(4): codes and conformity.** Providers "may rely on codes of practice… to demonstrate compliance… until a harmonised standard is published. Compliance with European harmonised standards grants providers the presumption of conformity…".
- The Act gives the presumption of conformity to harmonised standards, not to codes. That's the legal ground for Objective A's "does not constitute conclusive evidence of compliance".
- The catalog says the Commission's guidelines (¶100) say the same: no presumption of conformity for the Code. Not read.

**Art. 56, codes of practice.**
- (1) "taking into account international approaches": the source of Appendix 1.4's basis clause.
- (2)(d) "proportionate to the risks, take into consideration their severity and probability": confirms my unit-5 recollection, and is the source of recital (c) and M3.4's "probability and severity".
- (4): codes must "take due account of the needs and interests of all interested parties, including affected persons".
- (5): "participants… report regularly to the AI Office on the implementation of the commitments": so C7's citation of Art. 56(5) is the Act's reporting hook.
- (6): the AI Office and the Board "shall publish their assessment of the adequacy of the codes of practice", and the Commission may approve a code by implementing act. So the Chapter's adequacy is formally assessed and published by the AI Office, and the Code is silent on this.
- (8): the AI Office "shall… encourage and facilitate the review and adaptation of the codes". This answers my unit-124 question ("how is the Code updated?"): the Act gives that role to the AI Office.

**Art. 3(49) "serious incident"** = "an incident or malfunctioning of **an AI system** that directly or indirectly leads to any of the following: (a) the death of a person, or serious harm to a person's health; (b) a serious and irreversible disruption of the management or operation of critical infrastructure; (c) the infringement of obligations under Union law intended to protect fundamental rights; (d) serious harm to property or the environment."

This settles the open question from units 73 and 84, and makes it sharper:
- The Act's definition is written for **AI systems**, not models. The Code applies it to GPAI models with systemic risk (via Art. 55(1)(c), which uses the term for models).
- The Code's M9.3 splits (a) into death (10 days) and health harm, explicitly "mental and/or physical" (15 days).
- It **adds** "a serious cybersecurity breach, including the (self-)exfiltration of model weights and cyberattacks" (5 days). That category is **not in Art. 3(49)**.
- "Directly or indirectly" is the Act's phrase, carried into the Code.

So the Code's incident categories extend the Act's definition for GPAI models. Given the Glossary's rule that Art. 3 definitions "shall prevail" over any "competing interpretation", there's a live question: is the cyber category a reporting rule the Code adds on top of the Act's concept, or an interpretation of "serious harm to property" or "critical infrastructure"? The text doesn't say. A fork should present it as an extension, not as the Act's definition.

**Art. 2(3), the national-security and military exclusion.**
- "This Regulation does not apply to areas outside the scope of Union law, and shall not, in any event, affect the competences of the Member States concerning national security…."
- "This Regulation does not apply to **AI systems** where and in so far they are placed on the market, put into service, or used with or without modification **exclusively** for military, defence or national security purposes…" (and similarly for systems not placed on the EU market whose output is used in the Union exclusively for those purposes).

**Correction to what I told the SB 53 expert from memory.** The exclusion exists, but it's narrower than "a gap by scope" suggested:
- it's written for AI **systems** used **exclusively** for military, defence or national-security purposes;
- it doesn't mention GPAI models.

So a GPAI model with systemic risk placed on the market for general use isn't excluded just because some of its uses are military. Only exclusively military systems fall outside the Act. The national-security clause protects Member States' competences, and doesn't obviously reach foreign governments' contracts. The contrast with SB 53's federal-contract override is starker than I said: the EU has no general deference to government contracts. I should tell the SB 53 expert if we talk again.

**Recital 110: the Code's risk lists come from here.** It reads:
> "General-purpose AI models could pose systemic risks which include, but are not limited to, any actual or reasonably foreseeable negative effects in relation to major accidents, disruptions of critical sectors and serious consequences to public health and safety; any actual or reasonably foreseeable negative effects on democratic processes, public and economic security; the dissemination of illegal, false, or discriminatory content. Systemic risks should be understood to increase with model capabilities and model reach, can arise along the entire lifecycle of the model, and are influenced by conditions of misuse, model reliability, model fairness and model security, the level of autonomy of the model, its access to tools, novel or combined modalities, release and distribution strategies, the potential to remove guardrails and other factors. In particular, international approaches have so far identified the need to pay attention to risks from potential intentional misuse or unintended issues of control relating to alignment with human intent; chemical, biological, radiological, and nuclear risks, such as the ways in which barriers to entry can be lowered, including for weapons development, design acquisition, or use; offensive cyber capabilities, such as the ways in vulnerability discovery, exploitation, or operational use can be enabled; the effects of interaction and tool use, including for example the capacity to control physical systems and interfere with critical infrastructure; risks from models of making copies of themselves or 'self-replicating' or training other models; the ways in which models can give rise to harmful bias and discrimination…; the facilitation of disinformation or harming privacy…; risk that a particular event could lead to a chain reaction with considerable negative effects that could affect up to an entire city, an entire domain activity or an entire community."

The traces in the Code, item by item:
- **Appendix 1.1's examples** (major accidents, critical sectors, democratic processes, economic security, illegal/false content) are recital 110's first sentence.
- **Appendix 1.2.2's contributing characteristics**: "increase with model capabilities and model reach" became "capability-dependent" and "reach-dependent"; "chain reaction" became "compounding or cascading".
- **Appendix 1.3.3's sources** ("release and distribution strategies", "vulnerability to adversarial removal of guardrails", access to tools, autonomy, modalities) are recital 110's middle sentence.
- **The specified risks:**
  - CBRN's "lowering the barriers to entry… design, development, acquisition, release, distribution, and use" expands "barriers to entry can be lowered, including for weapons development, design acquisition, or use";
  - cyber's "automated vulnerability discovery, exploit generation, operational use" expands "vulnerability discovery, exploitation, or operational use".
- **Loss of control** in the recital is only "unintended issues of control relating to alignment with human intent" and "risks from models of making copies of themselves or 'self-replicating' or training other models". The Code's operational definition, "humans losing the ability to reliably direct, modify, or shut down a model", is the **Code's own sharpening**, not the Act's.
- **Harmful manipulation** has no direct counterpart in recital 110. The closest is "facilitation of disinformation". The Code's specified risk of strategic distortion of beliefs and behaviour is broader and newer.
- The catalog says recital 110 reproduces the G7 Hiroshima Code of Conduct's Action 1 list. If so, the lineage is G7 (2023) → AI Act recital 110 (2024) → the Code's Appendix 1 (2025), and agreement between the Code and G7-derived sources is shared ancestry.

**Recitals 114–115.**
- **114:** "regardless of whether it is provided as a standalone model or embedded in an AI system", plus "as appropriate, through internal or independent external testing". Both are the roots of recital (b) and Appendix 3.5.
- **115:** "accidental model leakage, unauthorised releases, circumvention of safety measures, and defence against cyberattacks, unauthorised access or model theft". The Code's C6 scope ("unauthorised releases, unauthorised access, and/or model theft") and the Glossary's "accidental model leakage" inside 'insider threats' are taken from here.

**Arts. 51–52.**
- **Art. 51(2):** the presumption of systemic risk at more than 10^25 FLOP of training compute (written "1025" in the canonical text, a superscript lost in conversion).
- **Art. 52(1):** "within two weeks" notification, which M1.1's four-week Framework clock runs from.
- **Art. 52(6):** the Commission publishes a list of GPAI models with systemic risk. So *which* models are covered is public, even though their Model Reports aren't.

## What this adds for a fork, in short

- The Code's internal-use reach rests on the Act's "use" (Art. 55(1)(b)).
- The "serious cybersecurity breach" incident category is the Code's addition to Art. 3(49), which is defined for AI systems.
- The military exclusion is for AI systems used *exclusively* for those purposes, not for GPAI models.
- The loss-of-control formula is the Code's own; recital 110 has only "unintended issues of control relating to alignment with human intent".
- The AI Office publishes its assessment of the Code's adequacy and is charged with its review (Art. 56(6), (8)).
- The canonical text's LEGAL TEXT damage is confirmed and corrected above.
