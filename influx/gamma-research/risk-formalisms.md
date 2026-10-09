# Risk formalisms in the established literature: a check on the lexicon proposal

> [!NOTE]
> **Line and page references here predate `ref/canonical/`.** They were taken from `pdftotext -layout` extractions of the relata PDFs (the `bin/extract-text` script), before the canonical page-marked texts existed. Page numbers are the PDF's physical pages as pdftotext counted them (by form feeds). For the 84 catalog PDFs that count was checked and holds; for other documents a PDF with stray form feeds would shift it, so check before relying on a page. Line numbers ("L…") are lines of those layout extractions, so they won't match `ref/canonical/`: to re-find a passage, search for its quoted words, or regenerate the layout text with `pdftotext -layout`. References marked "md" are lines of `ref/iasr-2026-full.md`, which is unchanged.

*Research note for the gamma-iteration methodology document, 2026-10-06. Written by a Claude (Opus) research agent at the request of the session synthesizing that document. It is input to a decision Joseph and the lexicon agents will make, not a decision.*

**The question.** The proposal is that the lexicon should (a) define the *components* of risk, (b) declare "risk" a deliberately ambiguous umbrella, and (c) settle the *concepts* that "hazard" names before choosing which one gets the word. Does the established risk literature already decompose "risk" and "hazard" in a way we should adopt rather than reinvent, and where does it disagree with the proposal?

**How to read the markers.**
- **[primary]**: I read the passage in the primary document myself, today. The locator says where.
- **[witness]**: I could not reach the primary. I read the passage reproduced in a named secondary document that attributes it.
- **[memory]**: from training memory and not checked. Treat it as a pointer to check, not as evidence.
- **[my reading]**: my interpretation, kept separate from what the sources say.

**On quoting.** The repo is public, and most of these works are copyrighted (the SEP, the SRA glossary, Kaplan & Garrick, the STPA Handbook, the ISO and IEC texts, IEEE, BMJ, IPCC, ICAO). For those I give a close paraphrase with a locator precise enough to check the exact wording, and I name the structural features that matter (modal verbs, quantifiers, what kind of thing the definiens is). I quote verbatim only from US federal works, UN General Assembly documents, UK government pages under the Open Government Licence, and one CAA document cleared for unrestricted distribution. There is one short exception: ISO 31000's five-word definition of risk, because the whole lineage question turns on its exact words. The lexicon agents should read the locators before writing definitions that lean on these sources.

---

## 0. Short answer

1. **The proposal is not new. It is the Society for Risk Analysis glossary's own method, and it can cite that.** The SRA glossary (2015, updated 2018) was built on the premise that one agreed definition of risk is unrealistic. It therefore separates "overall qualitative definitions" (it gives seven) from "metrics/descriptions" (it gives six families), and it says none of the metrics *is* risk. That is very close to "define the components; let the umbrella word stay plural." Adopting it, with the citation, is better than reinventing it.
2. **The components are close to canonical, and they line up with Joseph's chain.** Kaplan & Garrick's triplet, ISO 31000's Note 3 to entry, the SRA's elements of a "risk description", NIST SP 800-30's risk model, the UN disaster-risk terms and bow-tie analysis all decompose into much the same parts:
   - a source or hazard;
   - a cause or threat;
   - a focal event;
   - consequences, with their severity;
   - likelihood;
   - controls on each side of the event;
   - exposure and vulnerability on the receiving side;
   - the knowledge the judgment rests on.

   Bow-tie analysis is almost exactly the middle of Joseph's chain (§4.2).
3. **The umbrella is not one ambiguity but at least four families of meaning, and some of them cannot be reduced to the components.** P × S, the event, the cause and the expectation value can all be projected from a set of (scenario, likelihood, consequence) triplets. Three other senses cannot:
   - STAMP's risk as **the effectiveness of the controls** (STPA Handbook p. 133);
   - ISO's **effect of uncertainty on objectives**, which counts upside as risk;
   - MIT's unit, which is a **risk description** (a source's presented category), not a risk.

   The umbrella's readings should be named in the lexicon, so that context maps can say which one a source uses (§4.3).
4. **"Hazard": the literature mostly agrees that the word names a *source*.** It also already distinguishes three neighboring concepts, each with its own term:
   - the event in which a hazard manifests (*hazardous event*);
   - exposure to a hazard (*hazardous situation*);
   - the point where control over a hazard is lost (*top event*).

   STPA is the outlier, redefining hazard as a system state. The NRR's "hazard = non-malicious" is a civil-contingencies convention. None of the formal glossaries I checked defines hazard by the absence of intent; they carry intent on a separate axis (safety vs security, or adversarial vs non-adversarial threat sources). This is evidence against the current leaning toward the NRR sense (§4.4).
5. **Corrections to things the repo currently says.** Details are in §5.
   - The probability × severity form comes from **ISO/IEC Guide 51** (product safety), not from ISO 31000.
   - NIST's "Adapted from: ISO 31000:2018" changes the definition's kind.
   - Kasirzadeh's four senses are Hansson's first four (Hansson lists *five*), cited to other authorities.
   - The STPA Handbook does say "provided but not followed", but as a loss-scenario type, not an unsafe-control-action type.
   - Barrett's and Mylius's STPA glossaries paraphrase the Handbook while attributing it, and they drift ("will" → "can").
   - There is an eighth sense of "hazard" in the AI literature: a root cause.

---

## 1. Verification ledger

| Candidate (as named in the brief) | Status | What I read | Misremembered? |
|---|---|---|---|
| Kaplan & Garrick 1981, risk triplet | **primary** | Authors' version hosted by the Garrick Institute (UCLA); equations checked against rendered page images | Holds. There is more in it than the triplet: a risk vs hazard distinction, a formal *hazard* as doublets, a "second-level" definition with probability of frequency, and an explicit "other" (not-yet-thought-of) scenario category |
| Hansson, SEP "Risk" | **primary** | plato.stanford.edu/entries/risk, §1 (substantive revision 8 Dec 2022) | Holds, but there are **five** senses, not four |
| Kasirzadeh's four senses derive from Hansson | **primary** (both texts) | relata `kasirzadeh-2024-types` (arXiv v3) §2.1 | Wording and order match Hansson's senses 1–4 nearly exactly. She cites four *other* works for them and cites Hansson (2010, *J. Risk Research*) only in the preceding sentence. Hansson's fifth sense is dropped |
| ISO 31000:2018 = "effect of uncertainty on objectives" | **witness** (official reproduction) | EU Agency for Railways terminology collection, which reproduces ISO 31000:2018 3.1 with its notes; also IEEE 7009-2024 via ISO/IEC/IEEE 16085:2021; NIST CSRC (via SP 800-160v1r1, citing Guide 73) | Holds. The *probability × severity* form is ISO/IEC **Guide 51**, a different document with a different purpose |
| ISO Guide 73 | **witness** (partial) | its notes as carried by ISO/IEC/IEEE 16085:2021 inside IEEE 7009-2024; CSRC | Same core definition as 31000. Its Note 4 is the bridge to a combination of consequences and likelihood |
| SRA glossary | **primary** | sra.org PDF, "Updated August 2018" (council approval 22 June 2015) | Holds, and is more useful than expected (§2.3) |
| STPA (Leveson & Thomas, *STPA Handbook*, March 2018) | **primary** | psas.scripts.mit.edu PDF | Holds. "Provided but not followed" is verbatim on p. 14, as the second kind of scenario. The Handbook also defines **risk** differently from everyone else (p. 133) |
| Leveson, *Engineering a Safer World* (2011) | **not reached** | MIT Press and OAPEN both sit behind bot checks; Leveson's site was unreachable | ESW's risk formula is [memory] only (§6) |
| Bow-tie | **primary** (regulator) + **witness** (IEC 31010:2019) | UK CAA, *Bowtie Analysis – Aircraft Refuelling* (July 2026) §2.4; Koessler & Schuett 2023 §5.4, summarizing IEC 31010:2019 | Holds. "Threat" in bow-tie means *any* cause, intentional or not |
| Reason, Swiss cheese | **primary** | Reason, "Human error: models and management", *BMJ* 320:768–770 (2000), PMC1117770 | Holds |
| ALARP | **primary** | HSE "ALARP at a glance" (Wayback snapshot 2025-01-12; the live URL returned 404 today); HSE *R2P2* (2001) | Holds, including a 50-fatality societal-risk criterion (§2.8) |
| PHIA yardstick | **primary** | gov.uk, *Explaining uncertainty in UK intelligence assessment* (24 Mar 2025) | Holds. It comes paired with a separate confidence rating (§2.9) |

Not named in the brief, and checked: UN A/71/644 (UNDRR terminology), IPCC AR6 WGII glossary, NIST SP 800-30 Rev. 1, NIST AI RMF 1.0 (local copy), ICAO Doc 9859 (local copy), Salem et al. 2024 and Nolte et al. 2025 (automated driving), Schnitzer et al. 2023 (AI Hazard Management), Barrett 2025 and Mylius 2025 (local copies).

---

## 2. The sources

### 2.1 Hansson (SEP) and Kasirzadeh: the senses of "risk"

**Hansson** [primary]: Sven Ove Hansson, "Risk", *Stanford Encyclopedia of Philosophy*, first published 13 Mar 2007, substantive revision 8 Dec 2022, §1 "Defining risk". <https://plato.stanford.edu/entries/risk/>

Five technical senses, each with an example sentence. In paraphrase:
1. an unwanted event that may or may not occur;
2. the cause of such an event;
3. the probability of such an event;
4. the statistical expectation value of such an event (probability times a measure of severity);
5. the fact that a decision is made under *known* probabilities ("decision under risk", as opposed to under uncertainty).

Hansson calls 1–2 qualitative and 3–4 quantitative. He says sense 4 entered risk analysis through WASH-1400 (1975), is now the standard technical meaning in many disciplines, and is regarded by some analysts as the only correct one. He also notes evidence that technical definitions have had almost no effect on ordinary usage.

**Kasirzadeh** [primary]: "Two types of AI existential risk: decisive and accumulative", *Philosophical Studies* (2025); arXiv 2401.07836v3, §2.1, pp. 2–3 (relata `kasirzadeh-2024-types`). She gives "at least four distinct, though not mutually exclusive" interpretations. They are Hansson's senses 1–4, in the same order and in nearly the same words, each with an AI-flavored example. She cites a different authority for each: Carlsmith 2022, Weidinger et al. 2022, Lowrance 1976, and UNISDR 2009. The SEP entry is not cited. Hansson appears only as "Hansson, 2010" (*Journal of Risk Research* 13(2)) in the sentence before. The same paragraph quotes ISO 31000, the SRA (its qualitative definition 5) and the EPA.

**What it implies.**
- For the repo's correlation discipline, "Kasirzadeh's four senses" and "Hansson's senses" are **one lineage**, not two corroborating analyses. I cannot tell from the text whether she drew on the SEP directly. The wording ("statistical expectation value", "unwanted event") is Hansson's, though. The model should cite Hansson (SEP) as the origin and Kasirzadeh as a restatement.
- Hansson's dropped **sense 5** matters to us. "Under risk" vs "under uncertainty" (known vs unknown probabilities) is exactly the line along which the NRR, CRA and STPA disagree about whether likelihood can be assessed at all (OVERVIEW §2.5; STPA Handbook p. 57 and pp. 133–134).
- [my reading] Hansson's list is a list of *what the word picks out*, not a decomposition. Senses 1–4 pick out different nodes and quantities in one causal–probabilistic structure, which is what the schema draft already says (SCHEMA-SYNTHESIS: "a node, a node at a different stage, a qualifier and a product"). Sense 5 picks out a property of the *epistemic situation*, which no node carries. The lexicon will need somewhere to put that, as a knowledge or uncertainty-regime qualifier (§4.5).

### 2.2 Kaplan & Garrick (1981): the triplet, and much more

[primary] Stanley Kaplan and B. John Garrick, "On the quantitative definition of risk", *Risk Analysis* 1(1):11–27 (1981). I read the authors' version posted by the B. John Garrick Institute for the Risk Sciences, UCLA: <https://www.risksciences.ucla.edu/s/On-the-Quantitative-Definition-of-Risk.pdf>. Page numbers below are that version's own, not the journal's.

What it says, in paraphrase, with the formulas as printed:
- **Risk involves both uncertainty and possible damage**, written symbolically as *risk = uncertainty + damage* (§2.1, p. 2).
- **Risk vs hazard** (§2.2, p. 2). Following a dictionary, a hazard is a *source of danger* that simply exists. Risk adds the likelihood that the source is converted into actual loss. Example: the ocean is a hazard; crossing it by rowboat is high risk and by ocean liner low risk, because the liner is a safeguard. Symbolically, *risk = hazard / safeguards*. Safeguards can make risk small but never zero, and *awareness* of a hazard counts as a safeguard.
- **Risk is relative to the observer**: it depends on what the observer knows (§2.3).
- **First-level definition** (§3.1, p. 4). Risk analysis answers three questions: what can go wrong; how likely is it; and what are the consequences if it does? Each answer is a triplet ⟨sᵢ, pᵢ, xᵢ⟩ (scenario, probability, consequence or damage measure). Risk *is* the set R = {⟨sᵢ, pᵢ, xᵢ⟩}, i = 1…N.
- **Hazard, formally** (p. 4, footnote 3). Having defined risk as triplets, they define hazard as the set of **doublets** H = {⟨sᵢ, xᵢ⟩}, i.e. scenarios and their consequences *without likelihood*.
- **Against "probability times consequence"** (§3.3). They call it misleading. Risk is probability *and* consequence. Multiplying equates a low-probability, high-damage scenario with a high-probability, low-damage one, and a single number is "not a big enough concept". The risk is the whole risk curve, not its mean.
- **Second level** (§5.3, p. 15). Uncertainty about frequency is folded in: R = {⟨sᵢ, pᵢ(φᵢ), xᵢ⟩}, where pᵢ(φᵢ) is a probability density over the *frequency* φᵢ of scenario i. With uncertainty in damage as well, this becomes R = {⟨sᵢ, pᵢ(φᵢ), ζᵢ(xᵢ)⟩}. This is the "probability of frequency" framework.
- **Completeness** (§§3.5, 6.3). The scenario list includes a category of scenarios *not yet thought of*. It is assessed like any other, with Bayes' theorem, using as evidence that no such scenario has yet occurred.
- **Acceptability** (§7). No risk is acceptable in isolation. It is acceptable only as part of the best option once costs and benefits are weighed.

**What it implies.**
- [my reading] This is the strongest precedent for **defining the components and treating the scalar as derived**. Hansson's senses 1, 3 and 4 are each a *projection* of R: the event is sᵢ; the probability is pᵢ; the expectation is Σpᵢxᵢ. Sense 2 is a node upstream of sᵢ. The NRR's unit is *one* triplet, the reasonable worst case with banded p and x, plus a confidence rating, which K&G's level 2 would put inside pᵢ(φᵢ). Anthropic's "expected total unmitigated harm" is the mean of the curve, which K&G warn against treating *as* the risk.
- **K&G's hazard is a set of scenario–consequence doublets, not a physical object.** Their prose says "source"; their formal definition says doublets. So even inside one canonical paper, "hazard" spans *the thing* and *what could happen with it, ignoring likelihood*. The second reading is close to IASR's "event or activity that has the potential to cause harm", which has no likelihood in it.
- **The "other" scenario is a precedent for Joseph's "risk events [recorded, ideated, unknown]".** K&G treat the unknown category as a first-class row with its own evidence. That supports giving "unknown" an explicit place in the event list rather than leaving it as a caveat.
- **Safeguards divide risk, not hazard.** Controls live between hazard and risk. That is the same picture as bow-tie barriers and STPA control structures.

### 2.3 The Society for Risk Analysis glossary

[primary] SRA Committee on Foundations of Risk Analysis (T. Aven, leader; Y. Ben-Haim, H. B. Andersen, T. Cox, E. López Droguett, M. Greenberg, S. Guikema, W. Kröger, O. Renn, K. M. Thompson, E. Zio), *Society for Risk Analysis Glossary*, updated August 2018 (council approval 22 June 2015). <https://www.sra.org/wp-content/uploads/2020/04/SRA-Glossary-FINAL.pdf>

**Its method (p. 3, "Preparing the glossary").** Earlier attempts at one agreed set of definitions failed. The committee's answer is to allow different perspectives and to separate overall *qualitative definitions* from their *measurements*. It claims this makes the glossary unique among risk glossaries, ISO 31000's included.

**Risk (§1.1, p. 4).** The scope is a future activity (natural phenomena included), and risk concerns its consequences for something humans value, often relative to reference values, with at least one outcome negative. Then come **seven** overall qualitative definitions, in paraphrase:
1. the possibility of an unfortunate occurrence;
2. the potential for unwanted negative consequences of an event to be realized;
3. exposure to a proposition, such as a loss occurring, about which one is uncertain;
4. the consequences of the activity together with the associated uncertainties;
5. uncertainty about, and severity of, the consequences of an activity, with respect to something humans value;
6. the occurrence of specified consequences of the activity, with the associated uncertainties;
7. deviation from a reference value, with the associated uncertainties.

ISO's definition is noted as one that can be read as a special case. **Metrics/descriptions** (examples) follow:
- the combination of probability and magnitude or severity of consequences;
- probability of a hazard combined with a vulnerability metric;
- the triplet (sᵢ, pᵢ, cᵢ), i.e. Kaplan & Garrick;
- the triplet (C′, Q, K): specified consequences, a measure of uncertainty, and the **background knowledge** supporting both, including a judgment of its strength;
- expected consequences: PLL, FAR, the product P(hazard) × P(exposure | hazard) × E[damage | hazard, exposure], or expected disutility;
- a possibility distribution.

The glossary then states that **none of these metrics can be viewed as risk itself**, and that each one's appropriateness can always be questioned.

**Other terms (§§1.6–1.19, pp. 6–7), paraphrased:**
- **Hazard** (1.9): a *risk source* whose potential consequences relate to harm. Examples are given by energy, material, biota and *information*.
- **Risk source / risk agent** (1.14): an element (action, sub-activity, component, system, event, …) that, alone or with others, can give rise to specified, typically undesirable, consequences.
- **Threat** (1.18): a risk source, commonly in security applications but also elsewhere ("the threat of an earthquake"). *In relation to an attack* it has a second sense: a stated or inferred intention to attack in order to inflict harm.
- **Safe / safety** (1.16): without unacceptable risk. Safety is *sometimes limited* to risk from non-intentional events.
- **Secure / security** (1.17): without unacceptable risk *when risk is restricted to intentional acts by intelligent actors*.
- **Vulnerability** (1.19): among other readings, risk *conditional on* the occurrence of a risk source or event.
- **Exposure** (1.6): being subject to a risk source.
- **Event** (1.7): the occurrence or change of a particular set of circumstances. This matches ISO's wording; see §2.4.
- **Consequences** (1.7): effects of the activity on the values defined, covering the totality of states, events, barriers and outcomes.
- **Harm** (1.8): physical or psychological injury or damage.
- **Severity** (1.8): the magnitude of the damage or harm.
- **Impacts** (1.8): the effects the consequences have on specified values.
- **Resilience** (1.13), with its own qualitative definitions and metrics.
- **Risk characterization / risk description** (2.9, p. 8): a qualitative and/or quantitative picture of the risk, i.e. a structured statement usually containing risk sources, causes, events, consequences, uncertainty representations, and the knowledge the judgments rest on.

**What it implies.**
- **Adopt the method and cite it.** "Plural qualitative definitions plus named metrics, none of which is the risk" is the proposal's shape, already ratified by the field's main professional society. The lexicon can say it follows the SRA's concept/measurement separation.
- **(C′, Q, K) puts *knowledge strength* inside the risk description.** The corpus needs this. The NRR rates confidence separately; PHIA pairs probability with an Analytical Confidence Rating; Anthropic's Risk Reports hedge; IASR marks evidence. A component "strength of knowledge" (or "confidence") distinct from "likelihood" is standard SRA practice, not an invention. It also matches the repo's principle that soft evidence stays in, marked.
- **MIT's definition is SRA qualitative definition 1, nearly verbatim.** MIT's *rows*, though, are what the SRA calls **risk descriptions**: structured statements about a risk, authored by someone. That is a different kind of thing from a risk, and it deserves its own term (§4.3).
- **Hazard ⊂ risk source.** The SRA makes hazard a *subtype* of risk source (those relating to harm), not a separate category, and threat another subtype or near-synonym used in security. Intent is carried by safety vs security and by the attack sense of threat, *not* by hazard vs threat. This bears directly on the NRR question (§4.4).
- Vulnerability as "risk conditional on the source occurring" gives a clean, verified definition for the receiver side of the impact radius.

### 2.4 The ISO family: ISO 31000 / Guide 73 against ISO/IEC Guide 51

There are two ISO lineages, and the corpus conflates them.

**(a) Management-system lineage: ISO 31000:2018 and ISO Guide 73:2009.** [witness]
- ISO 31000:2018 §3.1 defines risk as "effect of uncertainty on objectives". This is my one verbatim ISO quotation; the five-word definition is decisive for the lineage claim.
- Notes to entry, paraphrased:
  - Note 1: an effect is a deviation from the expected. It may be positive, negative or both, and may address, create or result in opportunities and threats.
  - Note 2: objectives have different aspects and levels.
  - Note 3: risk is *usually expressed in terms of risk sources (3.4), potential events (3.5), their consequences (3.6) and their likelihood (3.7)*.
- Witness: the EU Agency for Railways (ERA) Railway Terminology Collection, which reproduces the entry with origin "ISO 31000:2018(en)" and a link to the ISO OBP (release dated 1 March 2026): <https://www.era.europa.eu/era-railway-terminology-collection/risk/term_2/sms_safety_culture_human_and_organisational_factor>.
- Guide 73's form [witness, via ISO/IEC/IEEE 16085:2021 as reproduced in IEEE Std 7009-2024 §3.1, relata `ieee-7009-2024-fail-safe-autonomous`, p. 17; that 16085's notes follow Guide 73's is [memory]] has the same core definition, with notes saying that risk is often characterized by reference to potential events and consequences. **Its Note 4** says risk is often expressed as a combination of an event's consequences and the associated likelihood of occurrence.
- **Note 5** in that entry defines uncertainty as a state, even partial, of deficiency of information about an event, its consequence or its likelihood.
- NIST CSRC independently attributes the core definition to ISO Guide 73 (via SP 800-160v1r1): <https://csrc.nist.gov/glossary/term/risk>.
- The same IEEE entry gives **event**, from 16085, with notes, paraphrased: an event can be a change of status; can comprise several occurrences and causes; can consist of something *not* happening; can be called an incident or accident; is a "near miss" if it causes no harm; and *its cause can itself be an event in a chain of events*. **Likelihood** is the chance of something happening, deliberately broader than mathematical probability.

**(b) Product-safety lineage: ISO/IEC Guide 51:2014** (*Safety aspects — Guidelines for their inclusion in standards*). [witness ×2]

Definitions, paraphrased:
- **harm** (3.1): injury or damage to people's health, or damage to property or the environment;
- **hazard**: a potential *source* of harm;
- **hazardous event**: an event that can cause harm;
- **hazardous situation**: a circumstance in which people, property or the environment are *exposed* to one or more hazards;
- **risk** (3.9): the combination of the *probability of occurrence of harm* and the *severity of that harm*.

Guide 51 also treats tolerable and acceptable as synonyms for risk, and safety as freedom from risk that is not tolerable [memory for the safety wording].

Witnesses:
- IEEE Std 7009-2024 §3.1, p. 17, reproducing harm, hazard, hazardous event and hazardous situation "with permission" from ISO/IEC Guide 51:2014.
- Nolte et al. 2025 (arXiv 2502.06594) §III, quoting Guide 51 def. 3.9 (p. 2) and def. 3.1 (p. 1).
- A third, weaker witness for the risk wording: the IEC Electropedia entry 903-01-07, seen only as a search-result title. I could not open it.

IEEE 7009 notes (fn. 11) that Guide 51 is freely available from ISO. I did not reach that copy.

**What it implies.**
- **The probability × severity definitions in the corpus are Guide 51's.** The EU AI Act's "combination of the probability of an occurrence of harm and the severity of that harm" is Guide 51 with one article added. That fits the Act's New-Legislative-Framework, product-safety architecture. IASR's "combination of the probability and severity of a harm" is the same form. **OVERVIEW §2.2's "It comes from ISO 31000 and allied texts" should say Guide 51** (§5).
- **ISO 31000 is a different kind of definition.**
  - Its definiens is an *effect on objectives*, relative to someone's objectives.
  - It includes upside: positive effects are risk.
  - It decomposes risk into sources, events, consequences and likelihood (Note 3) instead of collapsing it into a product.
  - [my reading] It is the ISO analogue of the SRA's qualitative definition 7, deviation from a reference value, and the SRA glossary says the same.
- **NIST AI RMF's "Adapted from: ISO 31000:2018" adapts the *notes*, not the definition** [primary, relata `nist-2023-ai-rmf`, §1.1, p. 4]. NIST's sentence is: "risk refers to the composite measure of an event's probability of occurring and the magnitude or degree of the consequences of the corresponding event." The positive/negative clause is ISO's Note 1. The core is Guide-51-like, and the next sentence is "Adapted from: OMB Circular A-130:2016" (the same form as SP 800-30; §2.10). So NIST's "positive consequences" sense, which OVERVIEW notes as unique, is the trace of ISO 31000's Note 1 grafted onto a P × M core.
- **Guide 51's hazard / hazardous event / hazardous situation triad is the established decomposition of "hazard"** (§4.4). Salem et al. 2024 build their automated-driving risk ontology on it (§2.10).

### 2.5 STPA: the Handbook itself, and drift in the AI papers

[primary] Nancy G. Leveson and John P. Thomas, *STPA Handbook*, March 2018 (copyright the authors; non-commercial use permitted). <https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf>. Page numbers are the Handbook's printed numbers.

**Definitions, paraphrased, with the features that matter:**
- **Loss** (p. 16): involves something of value to stakeholders, such as life, injury, property, environment, mission, reputation or sensitive information, or anything else unacceptable to them. "Loss" is chosen deliberately, to replace accident, mishap and adverse event.
- **Hazard** (p. 17): a *system state or set of conditions* which, *together with a particular set of worst-case environmental conditions*, **will** lead to a loss. Three criteria (pp. 17–18):
  - hazards are system states, not component-level causes or environmental states;
  - they lead to loss in *some* worst-case environment;
  - they must be states *to be prevented*. "Aircraft in flight" is not a hazard.

  The system boundary is drawn around what the designers can control, which is the reason for separating hazards from losses (p. 17). Hazards must not be confused with their causes, for example "brake failure" (p. 18), or with failures (p. 19). They are stated at a level that does not distinguish technical, design, requirement or human causes (p. 19).
- **Unsafe control action (UCA)** (p. 35): a control action that, in a particular context and worst-case environment, **will** lead to a hazard. Four types (pp. 35–36):
  1. not providing it leads to a hazard;
  2. providing it leads to a hazard;
  3. providing a potentially safe action too early, too late or out of order;
  4. a continuous action lasting too long or stopped too soon.
- **Loss scenario** (p. 42): describes the causal factors that can lead to UCAs *and to hazards*. Two types must be considered (p. 43):
  - (a) why UCAs would occur;
  - (b) why control actions would be **improperly executed or not executed**, leading to hazards.

  The overview on p. 14 says it in the brief's words: scenarios explain how safe control actions "might be provided but not followed or executed properly". Type (b) covers both the control path (p. 49: sent but not received; received but no actuator response; inadequate response; actuators acting as if a command was sent when it was not) and the controlled process (pp. 50–51: the command reaches the process but the process does not respond, responds improperly, or is overridden by other controllers).
- **Security is folded in** (pp. 48–51). Each scenario type adds the question of how an *adversary* could inject, spoof, tamper with, intercept or disclose the control action or feedback.
- **Risk, in STAMP** (pp. 133–134). The Handbook says STAMP implies a different definition from the traditional "severity and likelihood of hazards or accidents occurring": risk is defined in terms of **the effectiveness of the controls used to enforce safe system behavior**, i.e. the design and operation of the safety control structure. This does *not* require estimating likelihood. Likelihood estimates are criticized elsewhere: p. 57 (early-concept PHA), p. 115 (Ch. 6, leading indicators) and pp. 120–121 (Ch. 7).

**Drift in the AI-corpus STPA papers.** Both attribute definitions to Leveson & Thomas (2018) and paraphrase them.

| Term | Handbook | Barrett 2025 glossary (relata `barrett-2025-stampstpa` L1062–1101) | Mylius 2025 glossary (relata `mylius-2025-systematic` L870–907) |
|---|---|---|---|
| hazard | worst-case environment, **will** lead to a loss | matches, with the three criteria | "specific" environmental conditions, **can** lead to an incident or loss (worst-case dropped) |
| UCA | **will** lead to a hazard | **can** lead to a hazard | **will** (matches) |
| UCA types 3–4 | too early / too late / out of order; too long / too soon | "wrong time or wrong order"; "wrong duration" | — |
| loss scenario | causal factors leading to UCAs **and to hazards**; two types | a real-world *situation* describing causal factors leading to UCAs, hazards and losses | causal factors leading to a UCA (**type (b) gone**) |
| loss | involves something of value to stakeholders | a harm, damage or cost unacceptable to stakeholders | an outcome with unwanted harm, damage or cost |
| vulnerability | — | — | treated as the security-domain synonym of hazard |

**What it implies.**
- The earlier agent was right that "provided but not followed" is in the Handbook. **It is a loss-scenario type, (b), not a fifth UCA type.** A lexicon that carries the four UCA types needs loss-scenario type (b) beside them, or the shutdown-resistance case has nowhere to live. That case is a correctly issued shutdown command, not followed by the controlled process; it falls under p. 50's process-side "does not respond / responds improperly / overridden" bullets. Mylius's glossary would lose it.
- **Bind the lexicon to the Handbook, not to the AI papers' glossaries.** The "will" → "can" drift changes the concept. "Will, given the worst case" is a *necessity-under-an-assumption* modal. "Can" is a *possibility* modal, and it moves STPA's hazard toward Guide 51's.
- **STAMP's risk (p. 133) is a fourth kind of thing, beside an event, a probability-weighted quantity and an effect on objectives: a property of a control structure.** [my reading] It is the established precedent for AISI's *Loss of Oversight* "severity" (how badly a pathway undermines an oversight channel) and for Anthropic-style "control" framings. Those collide with P × S in OVERVIEW §2.4 and §2.9. They are not idiosyncratic; they are STAMP's sense.
- SCHEMA-SYNTHESIS §8 says STPA makes "no adversary distinction". The Handbook does fold adversaries into loss-scenario generation. What it lacks is adversary-hood as a *classifying axis* for hazards or losses. Hazards are cause-agnostic by design (p. 19).

### 2.6 Bow-tie analysis

[primary, regulator] UK Civil Aviation Authority, *CAA Hydrogen Challenge: Bowtie Analysis – Aircraft Refuelling*, July 2026, §§2.2–2.4, pp. 5–6. "OFFICIAL – Public… cleared for unrestricted distribution." <https://www.caa.co.uk/publication/download/29369>. The method steps, verbatim:

> a. Identify the Hazard: Define the source of potential harm within the system, activity, or process.
> b. Define the Top Event: Describe the point at which control of the hazard is lost, creating the potential for adverse outcomes.
> c. Identify Threats: List all conditions or factors that could cause the top event to occur.
> d. Identify Consequences: Outline the potential impacts that may result if the top event happens.
> e. Identify Preventive Controls: Specify the measures in place to prevent each threat from leading to the top event.
> f. Identify Mitigative Controls: Specify the measures designed to reduce or limit the consequences should the top event occur.
> g. Identify Escalation Factors and Controls: Determine any conditions that could undermine the effectiveness of the preventive or mitigative controls, along with the actions needed to manage these weaknesses.

[witness] Koessler & Schuett, "Risk assessment at AGI companies: a review of popular risk assessment techniques from other safety-critical industries", arXiv 2307.08823 (2023), §5.4, pp. 19–20, summarizing IEC 31010:2019, Book (2012), and McConnell & Davies (2006). They describe the same structure: causes on the left, the undesired event at the knot, consequences on the right, preventive controls on the left and reactive controls on the right. They add escalation factors with their own controls, and ongoing activities (maintenance, audits, training) that keep all controls effective. They apply it to a model copying itself during training, which is a loss-of-control focal event. IASR 2026's glossary entry "Bowtie method" cites this paper (IASR ref. 1019; relata `bengio-2026-international`). Buhl et al. 2025 also recommend bow-tie (relata `buhl-2025-emerging` L268). IEC 31010:2019 itself was not reached.

**What it implies.**
- [my reading] **Bow-tie is the closest established match to Joseph's chain**, and it already treats stage as a role relative to a focal event. The repo's CLAUDE.md asks for exactly that.

  | Joseph's chain | Bow-tie |
  |---|---|
  | sources & causes | hazard + threats |
  | preventions & controls | preventive controls |
  | risk events | top event |
  | × impact radius | consequences |
  | mitigations & recovery | mitigative / recovery controls |
  | (degradation of controls) | escalation factors + their controls |
  | policies & decision-making | the management activities sustaining the controls; bow-tie represents these only thinly, and STAMP's control structure goes further |

- **Bow-tie's "threat" means any cause** ("conditions or factors"), intentional or not. This is a third sense of "threat" against the NRR's "malicious" and the SRA's "risk source, mostly in security".
- **Bow-tie's "hazard" is the source; its "top event" is the loss of control.** [my reading] STPA's system-level hazards ("aircraft violate minimum separation") are much closer to bow-tie top events than to bow-tie hazards. This correspondence may help the "hazard" decision (§4.4).

### 2.7 Reason's Swiss cheese model

[primary] James Reason, "Human error: models and management", *BMJ* 320(7237):768–770 (18 Mar 2000), doi:10.1136/bmj.320.7237.768; PMC1117770, section "The Swiss cheese model of system accidents". In paraphrase:
- Systems have layered defenses: engineered, human and procedural.
- Each layer has holes that keep opening, closing and shifting.
- Harm needs the holes in many layers to line up momentarily, so that a trajectory brings hazards into damaging contact with victims.
- Holes come from **active failures** (unsafe acts at the sharp end, short-lived) and **latent conditions** ("resident pathogens" from design, management and procedure decisions, long-lived, and identifiable before the event).

ICAO's SMM adopts the model (relata `icao-2018-doc9859-smm`, §§2.3.5–2.3.7, p. 2-6). Hendrycks et al. 2023, Stix 2025 and IASR 2026 (Figure 3.5) use it for AI.

**What it implies.** Two components the lexicon may need on the control side:
1. a **barrier's state** (intact or holed, time-varying), distinct from the barrier;
2. **latent condition vs active failure** as a basis of division over causes, by persistence and by distance from the focal event.

STAMP defines itself against this model, as SCHEMA-SYNTHESIS §8 already notes. Carrying both as *source* models is fine; adopting both as *our* vocabulary would need a resolution.

### 2.8 HSE: hazard vs risk, ALARP, tolerability, and a 50-fatality line

[primary; UK government web content, Open Government Licence] HSE, "ALARP 'at a glance'". The live URL <https://www.hse.gov.uk/enforce/expert/alarpglance.htm> returned 404 on 2026-10-06; I read the Internet Archive snapshot of 2025-01-12, section "Hazard or risk?":

> A hazard is something (eg an object, a property of a substance, a phenomenon or an activity) that can cause adverse effects.

> A risk is the likelihood that a hazard will actually cause its adverse effects, together with a measure of the effect. It is a two-part concept and you have to have both parts to make sense of it.

Its worked examples tag each part, e.g. "The annual risk of a worker in Great Britain experiencing a fatal accident [effect] at work [hazard] is less than one in 100,000 [likelihood]".

On ALARP, the same page quotes the Court of Appeal in *Edwards v National Coal Board* [1949] 1 All ER 743:

> "'Reasonably practicable' is a narrower term than 'physically possible' … a computation must be made by the owner in which the quantum of risk is placed on one scale and the sacrifice involved in the measures necessary for averting the risk (whether in money, time or trouble) is placed in the other, and that, if it be shown that there is a gross disproportion between them – the risk being insignificant in relation to the sacrifice – the defendants discharge the onus on them."

The page also says ALARP is "not one of balancing the costs and benefits of measures but, rather, of adopting measures except where they are ruled out because they involve grossly disproportionate sacrifices", and that "ALARP does not represent zero risk."

[primary] HSE, *Reducing risks, protecting people: HSE's decision-making process* (R2P2), 2001, ISBN 0 7176 2151 0 (Crown copyright; read via the Internet Archive copy of <https://www.hse.gov.uk/risk/theory/r2p2.pdf>). Paraphrased:
- **¶39**: HSE finds it useful to describe a hazard as the potential for harm arising from an *intrinsic property or disposition* of something to cause detriment, and risk as the *chance* that someone or something valued will be adversely affected in a stipulated way by the hazard.
- **The Tolerability of Risk (TOR) framework** sorts risks into unacceptable, tolerable and broadly acceptable regions. "Tolerable" means a willingness to live with a risk for its benefits, *not* acceptability.
- **¶25** defines **societal risk** as the subset of societal concerns arising from multiple fatalities in a single event.
- **¶136** (pp. 46–47 per the book's index) proposes that a single major industrial activity's risk of an accident killing **50 people or more in a single event** be regarded as *intolerable* if its estimated frequency exceeds **one in five thousand per year**.

**What it implies.**
- HSE's definitions carry the *disposition* reading of hazard: a property or disposition, not an event. That is close to "capability" and "propensity" in the EU Code's source vocabulary. [my reading] A model's dangerous capability or propensity is a hazard in exactly HSE's sense, so this lineage reaches frontier-AI usage.
- **The 50-fatality, single-event bar has a 2001 UK precedent.** SB 53's threshold is more than 50 deaths "arising from a single incident". Whether SB 53 drew on R2P2, or both drew on a common source in the major-hazards literature, I have not checked. I note it as a lead, not a lineage claim.
- ALARP and TOR give the lexicon an established vocabulary for **risk tolerance** (OVERVIEW §2.17–2.28). It includes "tolerable ≠ acceptable" (HSE) against Guide 51's "tolerable = acceptable" (as relayed by IEEE 7009 §5.2). That is a real collision to record.

### 2.9 The PHIA probability yardstick and confidence

[primary; gov.uk, OGL] Cabinet Office / PHIA, *Explaining uncertainty in UK intelligence assessment*, published 24 March 2025. <https://www.gov.uk/government/publications/explaining-uncertainty-in-uk-intelligence-assessment/explaining-uncertainty-in-uk-intelligence-assessment>

> The Professional Head of Intelligence Assessment (PHIA) Probability Yardstick splits the probability scale into seven ranges.

| Range | Term |
|---|---|
| >0% – ≈5% | Remote Chance |
| ≈10% – ≈20% | Highly Unlikely |
| ≈25% – ≈35% | Unlikely |
| ≈40% – <50% | Realistic Possibility |
| ≈55% – ≈75% | Likely or Probable |
| ≈80% – ≈90% | Highly Likely |
| ≈95% – <100% | Almost Certain |

The yardstick expresses "our assessed likelihood that a statement is true or that an event will occur, is occurring or has occurred". It is paired with **Analytical Confidence Ratings** (High / Moderate / Low), assessed on Information Base, Analytical Rigour, and Complexity & Volatility:

> Whereas probability reflects the likelihood that a statement is true, analytical confidence reflects the soundness and stability of the foundations on which the assessment of likelihood has been made.

**What it implies.**
- PHIA probability applies to **propositions**, past and present ones included, not only to future events. That makes it fit the EU Code's "likelihood that a causal link exists" (an attribution judgment) as well as occurrence likelihood. The lexicon can treat the EU's attribution likelihood as the same *instrument* applied to a different *proposition*, which may dissolve part of the OVERVIEW §2.5 collision.
- **Probability and confidence are separate axes in UK government practice.** That is a second independent precedent, after the SRA's (C′, Q, K), for the knowledge component.
- The gaps in the yardstick are deliberate. The NRR collapses every band from "Unlikely" upward into score 5 (OVERVIEW §2.5).

### 2.10 Not named in the brief, and useful

**UN / UNDRR disaster-risk terminology** [primary; UN General Assembly document]. *Report of the open-ended intergovernmental expert working group on indicators and terminology relating to disaster risk reduction*, A/71/644, 1 Dec 2016. <https://documents.un.org/doc/undoc/gen/n16/410/23/pdf/n1641023.pdf>
- **Disaster risk** (p. 14): "The potential loss of life, injury, or destroyed or damaged assets which could occur to a system, society or a community in a specific period of time, determined probabilistically as a function of hazard, exposure, vulnerability and capacity."
- **Hazard** (p. 18): "A process, phenomenon or human activity that may cause loss of life, injury or other health impacts, property damage, social and economic disruption or environmental degradation." The annotations add that hazards may be natural, anthropogenic or socionatural, and that the term excludes armed conflict and social instability governed by international humanitarian law and national legislation.
- **Hazardous event** (p. 20): "The manifestation of a hazard in a particular place during a particular period of time."
- **Exposure** (p. 18): "The situation of people, infrastructure, housing, production capacities and other tangible human assets located in hazard-prone areas."
- **Vulnerability** (p. 24): "The conditions determined by physical, social, economic and environmental factors or processes which increase the susceptibility of an individual, a community, assets or systems to the impacts of hazards."
- **Capacity** (p. 12): "The combination of all the strengths, attributes and resources available within an organization, community or society to manage and reduce disaster risks and strengthen resilience."
- The disaster-risk annotation (p. 14) also defines **acceptable or tolerable risk** and **residual risk**. "Extensive" and "intensive" disaster risk (pp. 18, 20) distinguish low-severity, high-frequency risk from high-severity, low-frequency risk.
- This is the 2017 update of the "2009 UNISDR Terminology" that Kasirzadeh cites for her expectation-value sense.

**IPCC AR6 WGII glossary** [primary]. IPCC 2022, Annex II: Glossary [Möller, van Diemen, Matthews et al. (eds.)], in *Climate Change 2022: Impacts, Adaptation and Vulnerability*. <https://www.ipcc.ch/report/ar6/wg2/downloads/report/IPCC_AR6_WGII_Annex-II.pdf>, entries "Risk", "Hazard", "Exposure", "Vulnerability". In paraphrase:
- **Risk** is the *potential for adverse consequences* for human or ecological systems, recognizing diverse values and objectives.
  - For *impacts*, it arises from the interaction of hazards with the exposure and vulnerability of the affected system, each of which may be uncertain.
  - For *responses*, it arises from responses failing to achieve their objectives, or from trade-offs and negative side-effects on other objectives.
- **Hazard** is the potential *occurrence* of a natural or human-induced physical event or trend that may cause loss.
- **Vulnerability** is the propensity or predisposition to be adversely affected.

**NIST SP 800-30 Rev. 1** [primary; US federal work]. *Guide for Conducting Risk Assessments* (Sept 2012), §2.3, pp. 6–11. <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf>
- **Risk** (p. 6): "a measure of the extent to which an entity is threatened by a potential circumstance or event, and is typically a function of: (i) the adverse impacts that would arise if the circumstance or event occurs; and (ii) the likelihood of occurrence."
- **Threat** (p. 8): "any circumstance or event with the potential to adversely impact organizational operations and assets, individuals, other organizations, or the Nation…". Also: "Threat events are caused by threat sources. A threat source is characterized as: (i) the intent and method targeted at the exploitation of a vulnerability; or (ii) a situation and method that may accidentally exploit a vulnerability." Its types include human errors, structural failures, and natural and man-made disasters.
- **Vulnerability** (p. 9): "a weakness in an information system, system security procedures, internal controls, or implementation that could be exploited by a threat source."
- **Predisposing condition** (p. 10): "a condition that exists within an organization, a mission or business process, enterprise architecture, information system, or environment of operation, which affects (i.e., increases or decreases) the likelihood that threat events, once initiated, result in adverse impacts…".
- **Likelihood** (p. 10) combines the likelihood that a threat event is initiated with the likelihood that it results in adverse impacts. For adversarial threats it is assessed from adversary intent, capability and targeting, and always relative to a stated time frame.
- **Impact** (p. 11): "the magnitude of harm that can be expected to result from the consequences of" the loss of confidentiality, integrity or availability.

**Automated driving: the closest neighboring precedent for an explicit risk ontology.**
- Salem, Kirschbaum, Nolte, Lalitsch-Schneider, Graubohm, Reich & Maurer, "Risk Management Core – Towards an Explicit Representation of Risk in Automated Driving", *IEEE Access* 12:33200–33217 (2024), doi:10.1109/ACCESS.2024.3372860; arXiv 2302.07715 [primary]. It builds a risk-assessment and risk-treatment ontology merging the terminology of ISO 26262, ISO 21448, UL 4600, IEC 61508, Guide 51 and ISO 31000. It takes Guide 51's risk as the base, and from ISO 31000's "effect on objectives" it adds an **agent** who holds the objectives and is endangered by a hazard (§IV.A). It treats acceptable, tolerable and reasonable as synonyms.
- Nolte et al., "A Review of Conceptualizations of Safety and Risk in Current Automated Driving Regulation", arXiv 2502.06594 (2025) [primary]. It reviews UN, EU, UK and German regulatory notions against Guide 51 and ISO 31000. Drawing on cited literature, it calls "safety" and "risk" "empty signifiers". It cites Fischhoff et al. on defining risk as "inherently controversial", and Christensen et al. (2003) on a cross-stakeholder risk terminology. I did not read those two.

**AI Hazard Management** [primary, abstract]. Schnitzer, Hapfelmeier, Gaube & Zillner, arXiv 2310.16727 (2023/2024). It defines AI hazards as the *root causes* of AI risks. This is a **"hazard" sense not in OVERVIEW §2.1's seven**: hazard = root cause (a technical cause class), which is neither the source object, the system state, the intent class nor the harm category.

**ICAO Doc 9859, *Safety Management Manual*, 4th ed. (2018, advance unedited)** [primary; relata `icao-2018-doc9859-smm`], "Definitions", pp. (x)–(xi), and §2.5.2.3, p. 2-9. In paraphrase:
- **hazard**: a condition or an object that has the potential to cause, *or contribute to*, an aircraft incident or accident (an Annex 19 definition);
- **safety risk**: the predicted probability and severity of a hazard's consequences;
- **defences**: mitigating actions, preventive controls or recovery measures.

It warns that people confuse hazards with their consequences. This is already in SCHEMA-SYNTHESIS.

---

## 3. Where the corpus's senses sit in this literature

The second column is [my reading]; the evidence for each corpus definition is in OVERVIEW §2.2, and SB 53's is in the brief.

| Corpus usage | In the literature's terms |
|---|---|
| **SB 53**: catastrophic risk = a "foreseeable and material risk" that a developer's conduct "will materially contribute to" more than 50 deaths or >$1B "from a single incident" | The defined term uses "risk" undefined in its own definiens. Read structurally, it is Hansson's sense 1 or the SRA's definition 1 (a *possibility*), qualified by an **epistemic standard** (foreseeable), a **materiality threshold**, a **causal-contribution standard** and a **single-incident severity bar** (cf. R2P2 ¶136). No probability or expectation is involved |
| **IASR, EU AI Act, Shanghai** | Guide 51 (P and S of harm), i.e. the SRA metric "probability and magnitude/severity". As OVERVIEW notes, never computed |
| **NIST AI RMF** | Guide-51-like P × M core, ISO 31000 Note 1 (positive effects) grafted on, A-130 / SP 800-30 function form |
| **NVIDIA** | P × S with a third factor (controllability or detectability); severity redefined as *duration + onset speed*. The SRA would call the latter different quantities, not severity |
| **Anthropic Risk Report**: misalignment risk = expected total unmitigated harm | Hansson's sense 4, the SRA's "expected consequences" metric, with a counterfactual harm baseline. K&G would call it the *mean of the risk curve*, not the risk |
| **UK NRR**: the scored reasonable worst case | *One* K&G triplet (a representative scenario with banded likelihood and banded impact) plus a separate confidence rating, i.e. the SRA's K and PHIA's AnCR |
| **MIT AI Risk Repository** | Definition = SRA definition 1. Unit = an SRA **risk description** written by another source |
| **CAIS** | Hansson's senses 1, 2 and 3 at once |
| **AISI *Loss of Oversight* severity** | STAMP risk: damage to a control or oversight structure |
| **IASR / Shanghai hazard**: an event or activity with potential to harm | Between Guide 51's *hazard* (source) and *hazardous event*. IPCC's hazard (a potential *occurrence* of an event or trend) is the nearest established match |
| **NRR hazard**: non-malicious, opposed to threat | Intent is carried by safety vs security (SRA), adversarial vs non-adversarial threat sources (SP 800-30), or the attack sense of threat (SRA). No formal glossary I checked puts it on hazard vs threat |

---

## 4. What this implies for the lexicon

### 4.1 The proposal agrees with the field's own glossary

The SRA did what the proposal suggests, for the same reason, and documented its rationale. I recommend saying so in the lexicon's preamble and taking two things from it:
- the **concept vs metric/description** separation, with the rule that no metric *is* the risk;
- the **knowledge component** (the K in (C′, Q, K)), so that confidence, evidence strength and the "soft evidence stays in, marked" discipline sit inside the formal object instead of beside it.

### 4.2 The components are close to canonical

Read together, these give nearly the same parts, under different names:
- ISO 31000's Note 3 (sources, potential events, consequences, likelihood);
- K&G (scenario, probability, consequence, plus hazard and safeguards);
- the SRA's risk-description elements (sources, causes, events, consequences, uncertainty representations, knowledge);
- SP 800-30 (threat source, threat event, vulnerability or predisposing condition, likelihood, impact);
- UNDRR (hazard, exposure, vulnerability, capacity);
- bow-tie (hazard, threats, top event, consequences, preventive and mitigative controls, escalation factors);
- Reason (barriers, holes, active and latent failures).

The convergent component set, [my reading]:

| Component | Established terms for it | Disagreements to settle |
|---|---|---|
| source | hazard (Guide 51, HSE, SRA, bow-tie, ICAO, UNDRR); risk source (ISO, SRA); threat source (SP 800-30) | object or disposition vs process or activity vs state (STPA) |
| cause / initiating condition | threat (bow-tie: any cause); cause; risk factor; latent condition | whether intent is part of the term |
| focal event | event (ISO / SRA, which allows "something not happening"); hazardous event (Guide 51, UNDRR); top event (bow-tie); threat event (SP 800-30); scenario sᵢ (K&G); hazard (STPA, as a *state*) | event vs state; one event vs a scenario set |
| controls / barriers | preventive & mitigative controls (bow-tie); safeguards (K&G); defenses (Reason, ICAO); control structure (STAMP) | a barrier vs its effectiveness vs its state (holes) |
| control degradation | escalation factors (bow-tie); latent conditions (Reason); STPA scenario type (b) | — |
| consequence / harm | consequence (ISO, SRA, K&G xᵢ); harm (Guide 51, SRA); loss (STPA); impact (SRA, SP 800-30) | harm to whom and to what (§4.5); positive consequences (ISO) |
| magnitude | severity (SRA: magnitude of damage); impact level (SP 800-30); xᵢ or ζᵢ(xᵢ) (K&G) | severity as magnitude vs duration or speed (NVIDIA) vs damage to oversight (AISI) |
| likelihood | likelihood (ISO: broader than probability); probability; frequency; probability of frequency (K&G) | over what proposition, window and conditioning (§4.5) |
| receiver side | exposure, vulnerability, capacity (UNDRR, IPCC, SRA); hazardous situation (Guide 51); predisposing condition (SP 800-30) | — |
| knowledge | K (SRA); confidence (NRR, PHIA AnCR); pᵢ(φᵢ) (K&G level 2) | — |

This lines up with Joseph's chain, mostly through the bow-tie (§2.6). The established literature already has role-relative staging. ISO's event notes say the cause of an event can itself be an event in a chain, and bow-tie's hazard, threat and top event are positions relative to a chosen top event. So "stage is a role relative to a focal event" has precedent too.

### 4.3 Where the literature pushes against "risk is just an ambiguous umbrella"

There are two different pushes, and they point opposite ways.

**(a) Kaplan & Garrick push for *less* ambiguity.** They would give "risk" one structured meaning, the set of triplets with knowledge folded in at level 2. Each corpus sense is then a *projection* of that set: the event is a scenario; the probability is pᵢ; P × S or the expectation is a summary statistic of the curve; the NRR is one representative triplet. If the lexicon takes this route, "risk" stays a precise word, and the context maps record *which projection* a source reports. That works in the project's favor ("our reading kept beside the source's words"). The cost is that the lexicon commits to one formal object, and it does not cover the senses in (b).

**(b) Some corpus senses cannot be projected from the triplet set.** These make a single structured meaning insufficient, so some umbrella is needed:
- **control effectiveness** (STAMP, p. 133; AISI LoO severity): a property of a control structure, not of an outcome distribution;
- **effect of uncertainty on objectives** (ISO 31000): relative to someone's objectives, and including upside;
- **risk from responses** (IPCC AR6): risk that arises from the controls and policies themselves. Joseph's chain ends in "policies & decision-making", and those can be risk sources too;
- **a risk description** (MIT; SRA 2.9): a document-level claim about a risk, not a risk;
- **decision under known probabilities** (Hansson 5): a property of the epistemic situation.

[my reading] A middle path, offered as an option:
- keep "risk" as the umbrella, as proposed, but **enumerate its readings as named lexicon entries**. For example: *risk-as-event*, *risk-as-source*, *risk-as-likelihood*, *risk-as-expectation*, *risk-as-scenario-set* (K&G), *risk-as-objective-deviation* (ISO), *risk-as-control-inadequacy* (STAMP), *risk description* (MIT/SRA). The names are illustrative; naming is the lexicon's job.
- let each context map then resolve a source's "risk" to one of these readings, or to "ambiguous among …".

This is what SCHEMA-SYNTHESIS already does for Kasirzadeh's four. The literature shows the list must be longer than four, and that two members (control inadequacy, risk description) are kinds of thing the risk side of the schema does not yet hold.

### 4.4 "Hazard": the concepts first, then the word

The established concepts, each with its established term:
- **H1, source**: an object, substance, energy, phenomenon, activity or *disposition* with the potential to cause harm. Guide 51 "potential source of harm"; HSE (with "intrinsic property or disposition" in R2P2 ¶39); SRA (a risk source relating to harm); bow-tie; ICAO (condition or object; "cause or contribute"); UNDRR (process, phenomenon or human activity); K&G in prose.
- **H2, hazard as potential occurrence**: IPCC (the potential occurrence of an event or trend); IASR and Shanghai (an event or activity with potential to harm); K&G's formal doublets {⟨sᵢ, xᵢ⟩} (what could happen and how bad, without likelihood).
- **H3, hazardous event**: the manifestation of a hazard in a place and time (UNDRR), an event that can cause harm (Guide 51). It plays the role of a threat event in SP 800-30.
- **H4, hazardous situation / exposure**: people, property or environment exposed to a hazard (Guide 51); exposure (UNDRR, IPCC, SRA).
- **H5, loss-of-control state**: the bow-tie top event (control of the hazard lost); STPA's system-level hazard (a system state that leads to loss under the worst-case environment, defined relative to a boundary drawn around what designers control).
- **H6, cause class by intent**: NRR hazard vs threat.
- **H7, root cause**: AIHM.
- Plus OVERVIEW's harm-category (MIT) and information-hazard senses, which are labels for kinds of H1.

**Which concept gets the word.** On the evidence here, **H1 has broad consensus**: ISO/IEC, the SRA, HSE, ICAO, the UN, bow-tie practice, and K&G's prose. It is also the sense that frontier-AI usage drifts toward when it calls capabilities or propensities "hazardous" (HSE's disposition reading). H3, H4 and H5 already have their own established names. Giving "hazard" to H1, and the others their established compound terms, would collide least with the literature. It would still collide with STPA and the NRR, as OVERVIEW §2.1 says any choice must.

**Against the current NRR leaning (H6).** The intent distinction matters, and the repo already treats adversary-hood as structural. But in every formal glossary I checked, intent is carried by a *separate axis*: safety vs security (SRA 1.16–1.17), adversarial vs accidental threat sources (SP 800-30 p. 8), and the attack sense of threat (SRA 1.18). It is not carried by hazard vs threat, and in two bodies of practice "threat" explicitly *includes* the non-intentional (bow-tie, SP 800-30). Binding "hazard" to "non-malicious" would make the lexicon's central word mean something different from the safety literature and from IASR's own glossary. One alternative is an orthogonal **intent attribute** on causes and sources. Its values (for example none, negligent, adversarial, or the AI-as-adversary case Shah uses) are for the lexicon to decide. The NRR's pair would then map cleanly onto (H1 or a cause) × intent.

**If STPA's vocabulary is adopted for the chain** (an open decision). STPA's "hazard" is H5. Binding "hazard" to H5 would isolate the lexicon from the majority sense. The STPA concept could live under the bow-tie name ("top event") or a compound of the lexicon's choosing, with STPA kept as a mapped source. That is consistent with the Handbook's own reason for the state sense: hazards are what designers can control, as opposed to losses, which they cannot. It is a design-boundary choice, not a claim about what hazards are.

### 4.5 Things the components must carry that the corpus collisions already demand

Each has an established precedent:
- **Knowledge / confidence**, separate from likelihood: SRA K; PHIA AnCR; NRR confidence; K&G level 2.
- **Likelihood's proposition, window and conditioning**: PHIA (propositions, past and present ones included); SP 800-30 (always relative to a time frame; initiation × impact); the NRR's 2- and 5-year windows; AISI's conditioning on absent effort.
- **The completeness row**: K&G's "other" scenario category, for Joseph's "unknown" risk events.
- **Positive effects**: ISO 31000 Note 1 and NIST. Our lexicon should mark whether a reading admits upside, because most of the corpus does not.
- **Harm baseline**: counterfactual in NIST 600-1 and Anthropic (OVERVIEW §2.3); none in Guide 51. This is a difference in kind between "harm" readings, and it needs marking.
- **Receiver-side structure for the impact radius**: exposure, vulnerability and capacity (UNDRR, IPCC); vulnerability as risk conditional on the source (SRA 1.19). These are verified and well-tested concepts for Joseph's "harmed groups, degree/scale".
- **Tolerability vocabulary**: ALARP / gross disproportion; TOR regions; "tolerable ≠ acceptable" (HSE) vs "tolerable = acceptable" (Guide 51 per IEEE 7009). The R2P2 50-fatality single-event criterion bears on OVERVIEW §2.6.
- **Risks from responses**: IPCC AR6. They let a policy or control be a source in the chain without a special case.

---

## 5. Corrections and additions to things the repo currently says

1. **OVERVIEW §2.2**: "It comes from ISO 31000 and allied texts". The probability × severity form is **ISO/IEC Guide 51**'s (product safety). ISO 31000 and Guide 73 define risk as an effect of uncertainty on objectives; their notes allow it to be *expressed* through consequences and likelihood. The EU wording tracks Guide 51 almost exactly. NIST's "Adapted from: ISO 31000:2018" takes the positive/negative note and keeps a P × M core of different lineage (OMB A-130).
2. **OVERVIEW §2.1** lists seven senses of hazard. There are at least eight: add **root cause of AI risk** (Schnitzer et al., AIHM). It may also help to note that IASR's sense sits between Guide 51's *hazard* and *hazardous event*, and is closest to IPCC's.
3. **SCHEMA-SYNTHESIS §6 and §8, and source-models/mit-cais.md L148**: "Kasirzadeh's four senses". They are Hansson's (SEP) senses 1–4, nearly verbatim, and Hansson has a fifth. Cite Hansson as the origin, and record the shared lineage so the two are not counted as corroboration.
4. **SCHEMA-SYNTHESIS §8, STPA row**:
   - "Type B scenarios: a control action executed improperly or not followed" is right in substance, and the Handbook's own words are "improperly executed or not executed" (p. 43) and "provided but not followed or executed properly" (p. 14).
   - "No adversary distinction" is too strong. The Handbook builds adversaries into scenario generation (pp. 48–51); what it lacks is intent as a *classifying* axis.
   - Barrett's and Mylius's glossaries paraphrase the Handbook while attributing it. The drifts in modality ("can" vs "will"), in the worst-case clause, and in the loss-scenario scope are listed in §2.5. Bind the lexicon to the Handbook.
5. **STAMP's risk definition** (Handbook p. 133) is not recorded anywhere I found in the repo. It is the precedent for the control-adequacy readings in AISI and Anthropic.

---

## 6. Not reached, and memory-only

- **Leveson, *Engineering a Safer World* (MIT Press 2011, open access)**: not reached. MIT Press and OAPEN served bot checks, and sunnyday.mit.edu timed out. [memory] ESW and *Safeware* (1995) define risk as the hazard level combined with the likelihood of the hazard leading to an accident ("danger") and the hazard's exposure or duration ("latency"), with "hazard level" as hazard severity combined with the hazard's likelihood. If that is right, it is a *third* STAMP-family risk notion, distinct from the Handbook's control-effectiveness one. Worth checking against ESW ch. 7 before any lexicon text relies on it.
- **IEC 31010:2019** (bow-tie, FTA, ETA and others): only Koessler & Schuett's summary.
- **ISO/IEC Guide 51:2014 itself**: two reproductions (IEEE 7009, Nolte et al.), not the document. IEEE says ISO makes it freely available; the ISO OBP is JavaScript-only, and I had no browser this session.
- **ISO 31000:2018 §§3.4–3.8** (risk source, event, consequence, likelihood, control): [memory] for 31000's own wording. Event and likelihood are verified only in the 16085 form via IEEE 7009. [memory] 31000 defines *control* as a measure that maintains and/or modifies risk, which bears on OVERVIEW §2.9.
- **Christensen et al. 2003**, *J. Hazardous Materials* 103:181–203, and **Fischhoff, Watson & Hope 1984**, *Policy Sciences* 17:123–139 ("Defining risk"): known only through Nolte et al. [memory] Fischhoff et al. argue that choosing a definition of risk is a political act, because it decides which consequences count. That is the strongest argument *for* a deliberately plural umbrella, and worth reading before the methodology document cites a position.
- **Aven's later work** (e.g. *Risk Analysis* 2012, "The risk concept — historical and recent development trends", RESS 99:33–44, cited by Kasirzadeh) and **Aven & Renn (2009)** on risk as an event with uncertain outcome: [memory]. These are the SRA committee lead's own arguments for (C′, Q, K).
- **UK CAA bowtie *templates* and training glossary**, which define escalation factors more strictly: seen only in a search summary, not read.

---

## 7. Notes on the brief, and adjacent things

- The brief's candidates were well chosen. Only two were misremembered: Hansson's count (five, not four), and the ISO lineage of P × S, where the brief's instinct was right and the repo's claim is the thing to correct.
- The biggest find was not on the list. STAMP's own *risk* definition (Handbook p. 133) belongs in the methodology's account of why "risk" cannot be one formal object.
- **Bow-tie deserves more weight than a bullet.** It is the established method whose structure *is* Joseph's chain around a focal event. IASR's glossary, Buhl et al. and Koessler & Schuett already carry it into the corpus.
- The HSE R2P2 50-fatality single-event criterion (2001) beside SB 53's >50 single-incident bar may be worth one line in the lineage section once someone checks whether SB 53's drafting history cites it.
- Practical note: the HSE "ALARP at a glance" and R2P2 URLs now 404 on hse.gov.uk. Cite the archived copies or the National Archives.

## Sources (as read on 2026-10-06)

- Hansson, S. O., "Risk", SEP (rev. 8 Dec 2022): <https://plato.stanford.edu/entries/risk/>
- Kaplan, S. & Garrick, B. J. (1981), *Risk Analysis* 1(1):11–27; authors' version: <https://www.risksciences.ucla.edu/s/On-the-Quantitative-Definition-of-Risk.pdf>
- SRA Glossary (Aug 2018): <https://www.sra.org/wp-content/uploads/2020/04/SRA-Glossary-FINAL.pdf>
- ISO 31000:2018 §3.1, as reproduced by ERA: <https://www.era.europa.eu/era-railway-terminology-collection/risk/term_2/sms_safety_culture_human_and_organisational_factor>
- NIST CSRC glossary, "risk": <https://csrc.nist.gov/glossary/term/risk>
- IEEE Std 7009-2024 (relata `ieee-7009-2024-fail-safe-autonomous`), §3.1, pp. 16–17; §§5.2–5.4
- Leveson, N. G. & Thomas, J. P., *STPA Handbook* (2018): <https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf>
- Barrett 2025 (relata `barrett-2025-stampstpa`); Mylius 2025 (relata `mylius-2025-systematic`)
- UK CAA, *Bowtie Analysis – Aircraft Refuelling* (July 2026): <https://www.caa.co.uk/publication/download/29369>
- Koessler, L. & Schuett, J. (2023), arXiv 2307.08823: <https://arxiv.org/abs/2307.08823>
- Reason, J. (2000), *BMJ* 320:768–770: <https://pmc.ncbi.nlm.nih.gov/articles/PMC1117770/>
- HSE, "ALARP at a glance" (archived 2025-01-12): <https://web.archive.org/web/20250112221314/https://www.hse.gov.uk/enforce/expert/alarpglance.htm>
- HSE, *R2P2* (2001), archived: <https://web.archive.org/web/20201210181413/https://www.hse.gov.uk/risk/theory/r2p2.pdf>
- PHIA, *Explaining uncertainty in UK intelligence assessment* (2025): <https://www.gov.uk/government/publications/explaining-uncertainty-in-uk-intelligence-assessment/explaining-uncertainty-in-uk-intelligence-assessment>
- UN A/71/644 (2016): <https://documents.un.org/doc/undoc/gen/n16/410/23/pdf/n1641023.pdf>
- IPCC AR6 WGII Annex II, Glossary (2022): <https://www.ipcc.ch/report/ar6/wg2/downloads/report/IPCC_AR6_WGII_Annex-II.pdf>
- NIST SP 800-30 Rev. 1 (2012): <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf>
- NIST AI RMF 1.0 (relata `nist-2023-ai-rmf`), §1.1, p. 4
- ICAO Doc 9859, 4th ed. (relata `icao-2018-doc9859-smm`)
- Salem et al. (2024), arXiv 2302.07715: <https://arxiv.org/abs/2302.07715>
- Nolte et al. (2025), arXiv 2502.06594: <https://arxiv.org/abs/2502.06594>
- Schnitzer et al. (2023/24), arXiv 2310.16727: <https://arxiv.org/abs/2310.16727>
- Kasirzadeh (2025), arXiv 2401.07836v3 (relata `kasirzadeh-2024-types`)
