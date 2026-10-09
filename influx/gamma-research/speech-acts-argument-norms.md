# Speech acts, argument and norms: established vocabulary for the assertion layer

> [!NOTE]
> **Line and page references here predate `ref/canonical/`.** They were taken from `pdftotext -layout` extractions of the relata PDFs (the `bin/extract-text` script), before the canonical page-marked texts existed. Page numbers are the PDF's physical pages and still hold. Line numbers ("L…") are lines of those layout extractions, so they won't match `ref/canonical/`: to re-find a passage, search for its quoted words, or regenerate the layout text with `pdftotext -layout`. References marked "md" are lines of `ref/iasr-2026-full.md`, which is unchanged.

*Research for the model-gamma methodology. Claude Opus 5.5, 2026-10-06, briefed by the methodology coordinator. Question: for the assertion-layer problems that `influx/model-beta/SCHEMA-SYNTHESIS.md` (draft 2) §3–§4 and §6.4 solved with its own coinages, is there established vocabulary to adopt? For each candidate: its core definitions from the primary source (or the best accessible authoritative one), how well it fits, and where it strains. Also: what was misremembered, and what is better that wasn't named.*

**Verification marks.** These are what this file is for.

- **[P]**: I read the primary text this session. Quotations marked [P] are from it.
- **[S]**: I read a named secondary source that quotes the primary, with page numbers where given. I did not see the primary.
- **[s]**: I have only a search-engine summary, or a secondary that summarises without quoting. Weak.
- **[M]**: from training memory. Not checked this session. Treat it as a lead, not a fact.

Copyright: Hohfeld (1913) is public domain. The Gifford Archives say *Norm and Action* is public domain in the US. Quotations from everything else are kept short.

---

## 1. Summary

| Named in the brief | Holds up? | Corrections | Fit to draft 2 |
|---|---|---|---|
| Searle 1976, five classes and direction of fit; Austin behind it | **Yes [P].** The 1975 chapter was read whole | In the 1975/76 text the first class is **"Representatives"**. "Assertives" is the 1979 name [S]. Searle exempts *definitions* from needing an institution [P]. | **Strong** for assertion *kind*, *strength* and *force*. **Strong** for statutory definitions and role conferral, via Searle's *declarations*, *assertive declarations* and constitutive rules. **Strains** where draft 2 treats a commitment as a norm with imposer = bearer. |
| Pollock, rebutting vs undercutting | **Yes [S].** | Two kinds is incomplete. The established set is **three**: rebutting, undercutting, and **undermining** (Prakken, ASPIC+) [P]. Draft 2's "defeats, attached to the premise it defeats" is *undermining*. | **Strong.** Safety-case practice has already adopted all three (SEI eliminative argumentation [P]). |
| Toulmin | **Yes [S]**, with page numbers via Verheij 2005 | Toulmin's **qualifier** is narrow: the force of the conclusion ("presumably"). Draft 2's "qualifier" is much broader. Toulmin's **rebuttal** ≠ Pollock's *rebutting*: it loosely covers both overturning the conclusion and setting the warrant aside. | **Moderate.** *Warrant* and *backing* are useful. Adopting "qualifier" with draft 2's breadth would misuse it. |
| Hohfeld, and deontic logic (von Wright) | **Yes [P]** for both | The pairs you gave are Hohfeld's **correlatives**, correctly. Hohfeld uses "**exemption**" as a synonym for **immunity**, which collides with draft 2's "exemption". | **Strong.** Hohfeld's *power / immunity* is exactly what a must/should ladder misses. Von Wright's *Norm and Action* gives an anatomy of a norm close to §6.4. |
| Walton, argumentation schemes | **Yes.** [S] for the expert-opinion scheme; [M] for the analogy scheme | None found | **Moderate–strong** for argument kinds (analogy, expert opinion) and their *critical questions*. Walton has no independence notion; that comes from elsewhere (§9.4). |
| CAE and GSN | **Yes.** [S] for CAE; [P]/[s] for GSN | GSN v3 (2021) added **Dialectics**: a challenge relation and *defeated* decorators [P]. OMG **SACM 2.2** is the formal metamodel under both, and it carries a stance-like enumeration [P]. | **Strong** for argument structure and contest *standing*. **Strains** because it is built to construct one's own case, not to compile what others said. |
| Evidentiality and epistemic modality | **Yes [P]** (WALS, de Haan) | In the typological sense, evidentiality is *grammatical*, and **English has none**. It is kept **distinct from epistemic modality**. Draft 2's stance question 1 mixes the two axes. | **Strong as a distinction.** For English text, what applies is FactBank / PDTB-style *attribution and factuality* annotation (§9.1). |

**Not named, and better or complementary** (each in §9):

1. **Institutional Grammar** (Crawford & Ostrom 1995; IG 2.0 codebook, Frantz & Siddiki) [P/S]. A coding grammar *for policy and legal text*, used on legislation, with **regulative and constitutive** statement types. The nearest thing to an off-the-shelf §6.4.
2. **Norm vs normative proposition** (von Wright; Alchourrón & Bulygin) [P]. The compilation principle in deontic-logic terms.
3. **Technical norms and anankastic statements** (von Wright) [P]. They resolve one of draft 2's flagged conflicts (IASR, §7.3).
4. **FactBank** (Saurí & Pustejovsky) [P] and **PDTB attribution** [P]. Factuality values relative to **nested sources**, with annotated corpora behind them. This is draft 2's "nested voices stay nested".
5. **Goffman's production format**: animator / author / principal [S]. This is draft 2's §3.1 authorship roles.
6. **OMG SACM** `assertionDeclaration` [P]: asserted / needsSupport / assumed / axiomatic / defeated / asCited.
7. **ASPIC+ attack vs defeat** [P]. Attacks are facts about what was argued; defeat needs a preference ordering, which is adjudication.
8. **LegalRuleML** (OASIS Standard 2021) [P]. Legal status over time (applicable / in force / efficacy / valid), strong vs weak permission, constitutive vs prescriptive, override, and multiple interpretations each with provenance.
9. **Searle's constitutive rules** ("X counts as Y in C"), **Hart's** secondary rules, and **Hohfeld's operative vs evidential facts** [P/S]. Together they cover role conferral (§6.2).
10. **Appraisal / ENGAGEMENT** (Martin & White 2005) [s]. A ready-made typology of how a text positions itself towards other voices; nearly item-for-item with stance question 1.
11. **Source reliability × information credibility**, the NATO "Admiralty" grading [S]. Two separate axes; "confirmed by *independent* sources".
12. **Linked vs convergent premises** [S]. The established names for draft 2's "conjunctive / convergent" aggregation.

---

## 2. Speech-act theory: Austin, Searle, Searle & Vanderveken

**Sources.**
- Searle, J. R. 1975. "A taxonomy of illocutionary acts." In K. Gunderson (ed.), *Language, Mind and Knowledge*, Minnesota Studies in the Philosophy of Science 7, pp. 344–369. **[P]**: complete chapter, openly hosted OCR scan, <https://conservancy.umn.edu/server/api/core/bitstreams/f1857cae-5ee1-453c-803e-4e11854b2bf6/content>.
  - The scan puts two book pages on each PDF page, so page numbers below are accurate to about ±1.
  - OCR damage is silently corrected in quotations only where the reading is unambiguous.
- Same paper, revised: Searle 1976, "A classification of illocutionary acts," *Language in Society* 5(1):1–23. Reprinted as "A taxonomy of illocutionary acts" in *Expression and Meaning* (CUP 1979), pp. 1–29. 1976: [S] via a 1977 review in *Lexis* (PUCP) quoting p. 10. 1979: [S] via Kloosterhuis 1998.
- Austin, J. L. 1962. *How to Do Things with Words*. [S] via SEP "John Langshaw Austin" (Longworth, rev. 2025) and SEP "Speech Acts" (Green, rev. 2020).
- Searle & Vanderveken 1985, *Foundations of Illocutionary Logic*. [S] via SEP "Speech Acts" §2.3.

### 2.1 Core definitions

**Illocutionary point vs force.** [P] Searle 1975, pp. 345–346:
> "The point or purpose of a type of illocution I shall call its illocutionary point. Illocutionary point is part of but not the same as illocutionary force. … the illocutionary point of a request is the same as that of a command … But the illocutionary forces are clearly different."

**Direction of fit.** [P] pp. 345–346, with Anscombe's shopping list:
> "Some illocutions have as part of their illocutionary point to get the words (more strictly, their propositional content) to match the world, others to get the world to match the words."

**Strength is a separate dimension.** [P] pp. 347–348, feature 4:
> "Both 'I suggest we go to the movies' and 'I insist that we go to the movies' have the same illocutionary point, but it is presented with different strengths, analogously with 'I solemnly swear that Bill stole the money' and 'I guess Bill stole the money.'"

**Authority and institutions.** [P] pp. 348–349, feature 10. Some acts need "an extra-linguistic institution, and generally a special position by the speaker and the hearer within that institution": to excommunicate, "pronounce guilty, call the base runner out, … declare war". Searle separates this from *status* in general: "an armed robber in virtue of his possession of a gun may order".

**The five classes** [P], pp. 353–360:
- **Representatives**: the point is "to commit the speaker (in varying degrees) to something's being the case, to the truth of the expressed proposition". Words-to-world fit. Belief is expressed. Searle stresses that "belief" and "commitment" mark *dimensions*:
  > "hypothesizing that p and flatly stating that p are in the same line of business".

  The test: "can you literally characterize it (inter alia) as true or false."
- **Directives**: "attempts (of varying degrees …) by the speaker to get the hearer to do something". They range from "very modest 'attempts', as when I invite you to do it or suggest that you do it" to "very fierce attempts as when I insist". World-to-words fit. Footnote 6: "Questions are directives".
- **Commissives**: "illocutionary acts whose point is to commit the speaker (again in varying degrees) to some future course of action". World-to-words fit. Intention is expressed.
- **Expressives**: express "the psychological state specified in the sincerity condition about a state of affairs". "there is no direction of fit": the truth of the content is *presupposed*.
- **Declarations**:
  > "the successful performance of one of its members brings about the correspondence between the propositional content and reality; successful performance guarantees that the propositional content corresponds to the world"

  Examples: appoint, nominate, declare war, fire, resign. And:
  > "Declarations bring about some alteration [OCR of the scan reads "alternation"] in the status or condition of the referred to object or objects solely in virtue of the fact that the declaration has been successfully performed."

  Declarations need "an extra-linguistic institution, a system of constitutive rules in addition to the constitutive rules of language".

  **Except** (p. 359): "The only exceptions to the principle that every declaration requires an extra-linguistic institution are those declarations that concern language itself, as for example when one says, 'I define, abbreviate, name, call, or dub.'"

**Searle on commissives vs directives** [P], p. 355. This matters for §6.4:
> "I am unable to do this, because whereas the point of a promise is to commit the speaker to doing something (and not necessarily to try to get himself to do it), the point of a request is to try to get the hearer to do something (and not necessarily to commit or obligate him to do it)."

He tried to treat promises as requests to oneself, or requests as placing the hearer under an obligation, and failed both ways.

**Representative declarations.** [P] Searle 1975, pp. 359–360.
> "Some members of the class of declarations overlap with members of the class of representatives. This is because in certain institutional situations we not only ascertain the facts but we need an authority to lay down a decision as to what the facts are after the fact-finding procedure"

Institutions require "representative claims to be issued with the force of declarations in order that the argument over the truth of the claim can come to an end somewhere and the next institutional steps which wait on the settling of the factual issue can proceed".

Unlike other declarations, "they share with representatives a sincerity condition. The judge, jury, and umpire can, logically speaking, lie".

The 1979 version calls them "assertive declarations": [S] Kloosterhuis, "Final but not infallible: two dimensions of judicial decisions," ISSA Proceedings 1998, <https://rozenbergquarterly.com/?p=14018>, quoting Searle 1979 with "assertive" in place of "representative". The same paper gives:
- Hart (*Concept of Law*, 1961), via the umpire: decisions are "final but not also infallible", and "for the purposes of the game 'the score is what the scorer says it is'";
- Austin (1962: 21): a verdict reached "properly and in good faith" can still be assessed as to "whether the verdict was just, or fair".

**Austin's infelicities.** [S] SEP Austin, quoting Austin 1962: 15–16. *Misfires*: the act "is not successfully performed at all", as when "it is the purser and not the captain who is conducting the ceremony". *Abuses*: "the act is performed, but insincerely".

**Austin's five classes** [S], SEP Speech Acts §3:
- verdictives ("a speaker gives a verdict, e.g. acquitting and diagnosing");
- exercitives ("speakers exercise powers, rights or influence");
- commissives;
- behabitives;
- expositives ("how their utterances fit into lines of reasoning, e.g., postulating and defining").

Searle's critique [P]: Austin's lists are of English *verbs*, not acts, and the categories overlap. Most verdictives and expositives are representatives. Exercitives split between directives and declarations.

**Searle & Vanderveken's seven components of force** [S], SEP Speech Acts §2.3:
1. illocutionary point;
2. degree of strength of the point;
3. **mode of achievement**: "To testify is to assert in one's capacity as a witness";
4. propositional content conditions;
5. preparatory conditions ("all other conditions that must be met for the speech act not to misfire");
6. sincerity conditions;
7. degree of strength of the sincerity conditions.

SEP Speech Acts §3.4 [S] on indirect force: a remark that you are on my foot "is normally taken as, in addition, a demand that you move". Green is sceptical that genuine indirect speech acts are as common as they seem, and folds many into conversational implicature.

**Constitutive rules and status functions.** [S] SEP "Social Ontology" (Epstein), on Searle 1995/2010: status functions carry "deontic powers", meaning "rights, permissions, entitlements, duties, obligations, etc.". They are expressed in constitutive rules of the form "**X counts as Y in C**". They are put in place by "a particular kind of speech act—a declaration". Searle 2010 p. 13, quoted there: "all of human institutional reality is created and maintained in existence by (representations that have the same logical form as) Status Function Declarations".

### 2.2 How it fits draft 2

- **"An assertion is one speech act, over one content"** (draft 2 §3) is speech-act theory already, without the vocabulary. *Illocutionary point / force / propositional content* names the parts. *Representative / directive / commissive / expressive / declaration* is the first cut of §4's "kinds", one level above them. Most of §4's "About the world" and "About knowledge" families are representatives with different contents. "Normative" is directives and commissives. "Definitional" is declarations, *when made by an institution*.
- **Strength.** Searle treats "speculates" and "asserts" as the *same point at different strengths*, not different stances. SEP gives the scale's norm: assert ≻ conjecture ≻ guess, by what challenge is in order. An assertion invites "How do you know that?". A conjecture owes only "some reason". A guess owes nothing. Zhu's obligation ladder is the *directive-side* strength scale, so one dimension covers both. My suggestion: separate *strength* out of draft 2's stance list.
- **"Grammatical mood is not a safe guide"** (§4: NCSC writes norms in the indicative) is the problem of **indirect** illocutionary force. The term exists. Green's caution applies: attribute indirect force only when the evidence "mandates" it. That is draft 2's "ambiguous among named candidates" rule.
- **Force as an attributed assertion** (§2: four authors on the Code's legal effect, one wrong) is a claim about a *preparatory condition* or the *institution*. Austin's *misfire* names what a wrong claim of force describes: the act did not come off as that act.
- **Definitions.** A legislature defining "frontier developer" is a **declaration**: it creates the status it names, in an institution. In Searle 1995 it is a **constitutive rule**, "X counts as Y in C". C is draft 2's scope ("for the purposes of this article"). This is where "a role is conferred by an instrument under stated conditions" (§6.2) gets its established name.
  - A researcher's "I consider them an auditor for the purposes of this article" is *also* a declaration. Searle names "I define, abbreviate, name, call, or dub" as the one kind that needs no extra-linguistic institution (p. 359). In SEP's terms ("Definitions", Gupta & Mackereth) it is a *stipulative definition*: one that "imparts a meaning to the defined term, and involves no commitment that the assigned meaning agrees with prior uses (if any) of the term" [S].
  - So the definitional family splits two ways, both Searlean:
    - **institutional** declarations create statuses with deontic powers in an institution (statute, regulation; arguably a company's internal policy);
    - **linguistic** declarations fix a term within a text and create no status beyond it.

    The difference is what the definition can *do* downstream. A statutory definition changes every obligation that uses the term (draft 2's "depends-on-definition" links). A paper's stipulation changes only how that paper is to be read.
- **Determinations, verdicts and classifications** (§4 "assessment/verdict", §6.5 "determinations with procedural standing", the AI Act's Commission designation, an Anthropic ASL determination) are **representative (assertive) declarations**.
  - They are truth-apt *and* status-creating.
  - Searle's sincerity point matters: they can be insincere, and wrong, as ordinary declarations cannot.
  - Hart's "final but not infallible" is the precise standing.

  The compilation can record the declaration as effective *and* record another source's claim that its representative content is false, without contradiction. My reading: this is the cleanest available treatment of "the AI Act presumption is rebuttable but the designation stands".
- **Mode of achievement** ("assert in one's capacity as a witness") is the established slot for draft 2 §3.1's "who, *in what capacity*".
- **Expressives** are rare in the corpus [my impression, not counted] but real: "we welcome", "we are concerned". Without the class they would be forced into representatives.
- **Questions** are directives in Searle. Draft 2's "open question" items in the corpus are usually *representatives about the state of knowledge*, not questions. The distinction stops misfiling.

### 2.3 Where it strains

- **Commitment ≠ self-directed norm.** Draft 2 §6.4 defines a commitment as "a norm where imposer = bearer". Searle tried that assimilation and could not make it work (quoted above). Von Wright likewise treats self-commands as prescriptions "only in an analogical or secondary sense" (§4.1).
  - The established analysis keeps two things apart: the **commissive act** (evidence plane) and the **normative position it creates** (model plane; Hohfeld, §4).
  - It then asks who holds the *correlative claim*. For a voluntary framework the answer may be "no one with a jural claim". That is the materiality question the corpus keeps asking. The reframing makes it a field to fill.
- **One sentence, several points.** Searle's classes are *points*. Corpus sentences often carry two: RSP v3 App. A is a recommendation to industry and a competitor-contingent commitment (draft 2 §3). Assertive declarations carry two by design. Draft 2's "several speech acts can share a content" already handles this; keep it.
- **Institutions of uncertain standing.** Is a company framework an "extra-linguistic institution" in Searle's sense? For acts *inside* the company (ASL activation, a Responsible Scaling Officer's determination) plausibly yes. For acts *towards the public*, no. I'd treat this as an assertion to record per source, not a property to fix.
- Searle's taxonomy is for **utterances**. Documents layer acts: a statute's recital vs its article; an annex's force. Draft 2 §2's "force belongs to a part" is a document-structure addition the theory doesn't supply. LegalRuleML and Akoma Ntoso do (§9.6).

---

## 3. Defeasible argument: Pollock, ASPIC+, Dung

**Sources.**
- SEP "Defeasible Reasoning" (Koons, rev. 2025). [S]
- Modgil & Prakken, "A general account of argumentation with preferences," *Artificial Intelligence* 195 (2013); arXiv:1804.06763. [P]
- Pollock 1987, "Defeasible reasoning," *Cognitive Science* 11:481–518. [S], quoted p. 481 by Goodenough et al. 2015 (§6). The publisher PDF was not fetchable.

### 3.1 Definitions

**Pollock.** SEP [S]: Pollock distinguished:
> "rebutting defeaters (which give one a prima facie reason for believing the denial of the original conclusion) and undercutting defeaters (which give one a reason for doubting that the usual relationship between the premises and the conclusion hold in the given case)"

and held that "a conclusion is warranted … if it is supported by an ultimately undefeated argument". Pollock 1987 p. 481, via SEI [S]: reasoning is defeasible "in the sense that the premises taken by themselves may justify us in accepting the conclusion, but when additional information is added, that conclusion may no longer be justified."

**ASPIC+, three attacks.** [P] Modgil & Prakken §3.2:
> "An argument A attacks an argument A′ if the conclusion of A … is a contrary or contradictory of: an ordinary premise in A′; the consequent of a defeasible rule in A′, or; a defeasible inference step in A′. These three kinds of attack are respectively called undermining, rebutting and undercutting attacks."

The knowledge base splits into **axioms** (unattackable) and **ordinary premises** (attackable). An *attack* succeeds as a **defeat** only given a preference ordering over arguments; undercuts are "preference independent".

SEP [S]: Dung's abstract frameworks don't distinguish attack types, "although this additional information can be added".

### 3.2 Fit

- Draft 2 §3.4's `defeats`, "attached to the premise it defeats" (Kierans' hedge defeating premise 4), is **undermining**. The handoff's todo asks for "rebutting vs undercutting", from logos. The established set is three. Keep all three.
- Several draft 2 stance-question-1 values are **argument relations, not commitment values**:
  - "holds insufficient but not false" (Kasirzadeh on the decisive view) is an *undercutting* stance towards an inference, not a stance towards a proposition;
  - "rejects or rebuts" is *rebutting*;
  - "discounts as a class" (Ren's "Dubious Intuitive Arguments") undercuts every argument of a type. In scheme terms (§5) it attacks the scheme's warrant;
  - "rules out on evidence" is a rebutting or undermining argument the source *makes*.

  Moving these into §3.4 shortens the stance list and makes it more precise.
- **Attack vs defeat is the compilation principle in argumentation terms.** That A attacks B is a fact about what was said; recording it is compilation. That A *defeats* B needs preferences; computing it is adjudication.
  - So: record attacks, with type. Treat "standing" as a *view* computed under a declared preference ordering, or as a standing *some source asserts*: the source's own reply, a court's finding, a review.
  - The logos standings (refuted / burden-shifted / standoff / open / conceded) are then **attributed assertions about a contest**, not fields we fill.
- **Axioms vs ordinary premises** match SACM's *axiomatic* vs *asserted* (§6) and draft 2's "assumption with its stated fallback".

### 3.3 Strains

- ASPIC+ and Dung are for **evaluating** arguments, which the project declines to do. Their value here is the *typology of relations*, not the semantics. The project may still want Dung-style views ("under source S's own preferences, which of S's claims stand?") as computed views. That is optional.
- Defeasible-reasoning formalisms assume one reasoner's knowledge base. A compilation holds many speakers' arguments, so every argument node needs its speaker (§9.1). AIF/IAT (§5.2) were built for that.

---

## 4. Normative positions: Hohfeld, Hart, von Wright, deontic logic, LegalRuleML

### 4.1 Hohfeld (1913)

**Source.** Hohfeld, W. N. 1913. "Some Fundamental Legal Conceptions as Applied in Judicial Reasoning." *Yale Law Journal* 23:16–59. **[P]**, full text at <https://persweb.wabash.edu/facstaff/helmang/phi213-1314S/phi213-txtbrwsr/Hohfeld/Hohfeld1913.html>.

The scheme, verbatim layout [P]:
```
Jural Opposites      rights     privilege   power       immunity
                     no-rights  duty        disability  liability

Jural Correlatives   right      privilege   power       immunity
                     duty       no-right    liability   disability
```

Definitions [P]:
- *Right as claim*: "if X has a right against Y that he shall stay off the former's land, the correlative (and equivalent) is that Y is under a duty toward X to stay off the place. … perhaps the word 'claim' would prove the best."
- *Privilege*: "a privilege is the opposite of a duty, and the correlative of a 'no-right.'"
- *Power*:
  > "A change in a given legal relation may result (1) from some superadded fact or group of facts not under the volitional control of a human being …; or (2) from some superadded fact or group of facts which are under the volitional control of one or more human beings. As regards the second class of cases, the person (or persons) whose volitional control is paramount may be said to have the (legal) power to effect the particular change of legal relations that is involved in the problem."
- *Immunity*: "a power is one's affirmative 'control' over a given legal relation as against another; whereas an immunity is one's freedom from the legal power or 'control' of another as regards some legal relation."
- **Terminology hazard.** Hohfeld writes "the very opposite of immunity (or exemption)". In Hohfeld, **exemption = immunity**.
- **Operative vs evidential facts** [P]:
  > "Operative, constitutive, causal, or 'dispositive' facts are those which, under the general legal rules that are applicable, suffice to change legal relations"

  > "An evidential fact is one which, on being ascertained, affords some logical basis—not conclusive—for inferring some other fact."
- *Authority*: "the term 'authority,' so frequently used in agency cases, is very ambiguous and slippery". Properly, "authorization" is the operative facts, and authority their effect.
- The eight are "the lowest common denominators of the law".

**Hart via SEP "Rights"** (Wenar, rev. 2025) [S]:
- claims and privileges "define what Hart called 'primary rules'";
- power and immunity define "secondary rules: rules that specify how agents can introduce and change primary rules";
- "A has a power if and only if A has the ability to alter her own or another's Hohfeldian incidents";
- powers can alter "'higher-order' incidents as well", for example to relieve a captain of her power to command.

### 4.2 Von Wright, *Norm and Action* (1963) and "Deontic Logic" (1951)

**Sources.**
- von Wright, G. H. 1963. *Norm and Action: A Logical Enquiry*. Gifford Lectures 1959–60. **[P]**, Gifford Archives full text:
  - ch. I <https://giffordarchives.org/books/norm-and-action/i-norms-general>;
  - ch. V <https://giffordarchives.org/node/1514>;
  - ch. VII <https://giffordarchives.org/books/norm-and-action/vii-norms-and-existence>.
- von Wright 1951, "Deontic Logic," *Mind* 60:1–15: cited via SEP "Deontic Logic" (McNamara & Van De Putte, rev. 2021). [S]

**Kinds of norm** [P], ch. I:
- *rules* (of a game, of grammar);
- *prescriptions or regulations*:
  > "Prescriptions are given or issued by someone. They 'flow' from or have their 'source' in the will of a norm-giver or as we shall also say a norm-authority. They are moreover addressed or directed to some agent or agents whom we shall call norm-subject(s). … the authority promulgates the norm. … the authority attaches a sanction"
- *customs* ("implicit prescriptions");
- *directives or technical norms*;
- moral norms;
- ideal rules.

**Technical norms and anankastic statements** [P], ch. I §7:
> "I shall regard as the standard formulation of technical norms conditional sentences in whose antecedent there is mention of some wanted thing and in whose consequent there is mention of something that must (has to ought to) or must not be done. An example would be 'If you want to make the hut habitable you ought to heat it'."

> "A statement to the effect that something is (or is not) a necessary condition of something else I shall call an anankastic statement."

> "It would be a mistake I think to identify technical norms with anankastic propositions. There is however an essential (logical) connexion between the two."

He distinguishes these from **hypothetical norms**: prescriptions for a contingency ("If the dog barks don't run").

**The anatomy of a prescription** [P], ch. V §1:
> "the character the content the condition of application the authority the subject(s) and the occasion"

> "There are two more things which essentially belong to every prescription without however being 'components' … These two we call promulgation and sanction."

> "The character the content and the condition of application constitute what I propose to call the norm-kernel."

Further, from ch. V:
- Character is ought / may / must-not.
- The condition of application is "the condition which must be satisfied if there is to be an opportunity for doing the thing which is the content". Norms are **categorical** or **hypothetical** by it.
- Authorities are **personal** or **impersonal**, the latter "intimately connected with the concept of an office".
- **Heteronomous** prescriptions are "given by somebody to somebody else". Self-given ones are prescriptions "only in a secondary sense".
- Subjects can be **conjunctively or disjunctively general**: "Someone ought to leave the boat".
- Occasions likewise. "report to the police within a week" can be complied with "either to-day or to-morrow or…".

**Norm vs norm-proposition.**
- [P] ch. VII: confusing the two is behind the apparent Kant/Hume conflict over *ought implies can*; "the importance of keeping this distinction clear". The entailment holds "between (true or false) norm-propositions" and propositions about ability.
- [S] SEP Deontic Logic §6.1: "You may park here for one hour" can be used by an authority "to provide permission" ("norming"), or by a passer-by "to report on an already existing norm". "only the latter use allows for truth or falsity", though some blend the two via performatives. Lineage: Alchourrón & Bulygin, *Normative Systems* (1971) [M for details].
- [S] SEP Deontic Logic §5: standard deontic logic makes **normative gaps** impossible ("neither explicitly obligatory, impermissible, nor permissible"). Systems of *explicit* norms need them (von Wright 1968).

### 4.3 LegalRuleML (OASIS Standard, 2021)

**Source.** *LegalRuleML Core Specification Version 1.0*, OASIS Standard, 30 Aug 2021 (Palmirani, Governatori, Athan, Boley, Paschke, Wyner). **[P]** <https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/os/legalruleml-core-spec-v1.0-os.html>.

Definitions [P]:
- **Legal Norm**: "a binding directive from a Legal Authority to addressees (i.e. Bearers or Auxiliary Parties)".
- **Legal Status**: "a standing that can apply to a Legal Norm at a Time, e.g., 'is applicable', 'is in force', 'has efficacy', 'is valid'". A **Status Development** is an event that changes it.
- **Permission**:
  > "a Deontic Specification for a state, an act, or a course of action where the Bearer has no Obligation or Prohibition to the contrary. A weak Permission is the absence of the Obligation or Prohibition to the contrary; a strong Permission is an exception or derogation of the Obligation or Prohibition to the contrary."
- **Right**: a Permission to a Bearer that implies Obligations or Prohibitions on others (the AuxiliaryParty). This is Hohfeld's claim/duty correlation.
- **Obligation / Prohibition**: what, if not achieved / achieved, "results in a Violation".
- **Reparation**: links a PenaltyStatement to a PrescriptiveStatement.
- **Override**: "a Legal Rule takes precedence over another". **Strength** is strict / defeasible / defeater; **Defeater** is defined as blocking a conclusion without asserting its opposite. This is an undercutter.
- **§4.2.2**: norms are "constitutive norms and prescriptive norms … (also known as counts-as rules)". Constitutive norms "define and create so called institutional facts", citing Searle.
- **Multiple interpretations**: "A legal rule may have multiple semantic annotations, where these annotations represent different legal interpretations … with parameters that indicate provenance, applicable jurisdiction".

### 4.4 Fit for this family

- **Draft 2 §6.4's "deontic type: obligation / prohibition / permission / exemption / power"** mixes two theories:
  - obligation / prohibition / permission are deontic-logic *characters* (von Wright);
  - power is a Hohfeldian *second-order* position.

  The established vocabulary keeps them as two layers:
  1. **first-order**: claim–duty, privilege–no-right (≈ obligation, prohibition, permission);
  2. **second-order**: power–liability, immunity–disability.

  "Leadership can … make decisions without the SAG" is then, on my reading, a power held by Leadership **plus** Leadership's *immunity* from the SAG's control (equivalently, the SAG's *disability*). Two positions, both recordable, both currently invisible to a strength ladder.
- **"Exemption"** in draft 2 (open-source models exempt from obligations) is a **strong permission** in LegalRuleML's terms, or a Hohfeldian *privilege* created by derogation. It is **not** Hohfeld's "exemption", which means immunity. I'd avoid the word, or define it against both.
- **"Grant permissions ('benefits … outweigh the risks')"**: the frameworks' deployment conditions are mostly **strong permissions**, derogations from a default prohibition the same document sets up. The weak/strong distinction is what tells a framework that *permits* from one that merely *doesn't forbid*.
- **"Who holds the correlative?"** Hohfeld's correlatives force this question for every duty. For statutes there is usually an answer: the state, or a regulator with power to enforce. For voluntary commitments there often is not, and that absence is substantive. Draft 2's "enforcer" and "beneficiary" slots are approximations of it.
- **Roles conferred by instruments under conditions (§6.2).** The established parts:
  - the conditions are Hohfeld's **operative facts**;
  - the conferral is a **constitutive rule** (Searle; LegalRuleML constitutive norm), "X counts as Y in C";
  - the authority to confer is a **power**.

  Hohfeld's operative/evidential split is exactly the line between the *threshold* (SB 53's compute figure, an operative fact) and a company's *report* of its compute (an evidential fact about it). On my reading, that separation is what keeps the "developer" question tractable.
- **Von Wright's components ↔ §6.4** (my alignment):

  | von Wright | draft 2 §6.4 |
  |---|---|
  | authority | imposer / issuer |
  | subject(s) | bearer |
  | condition of application | applicability condition |
  | occasion, with "within a week" generality | trigger → time limit → act |
  | sanction | consequence |
  | promulgation | — (draft 2 has no slot) |
  | heteronomous vs autonomous | imposer ≠ / = bearer |

  Draft 2 reinvented most of it. Promulgation could matter: unpublished internal policies cited in public frameworks.
- **The compilation principle is the norm / norm-proposition distinction.**
  - The Code's "Signatories commit to…" is *norming*. Our record "the Code says signatories commit to…" is a *norm-proposition*, and it is true or false.
  - On the evidence plane, assertions about norms are norm-propositions: attributed, truth-apt, checkable. On the model plane, a norm record is the norm-kernel the norm-propositions are about.
  - It also explains why draft 2 needed "force is an attributed assertion": a statement of force is a norm-proposition, and it can be false.
- **Normative gaps** give an established name to draft 2's "declared but empty slot", "a limit left unstated", and to "deliberately unbound". In deontic logic a *gap* is neither obligatory, forbidden nor permitted, and standard deontic logic can't express it. So gaps want explicit representation, not inference.
- **LegalRuleML's legal status over time** (applicable / in force / efficacy / valid, with status-changing events) is the established form of draft 2 §2's "in force from, applies from, enforceable from, superseded by". Its *multiple interpretations with provenance* is draft 2 §5's "a resolution is always an attributed assertion".

### 4.5 Strains

- Hohfeld is **bipartite**: every relation is between two persons. Norms addressed to "the field" (GDM), or "unaddressed by design" (IAEA), resist it. So do commitments to the public. Each needs an explicit "no determinate correlative" value rather than a forced counterparty.
- **Duties without claimants.** Hohfeld's correlative can still be stated: the claimant is "no one". Some theorists hold there can be duties without correlative rights. SEP Rights covers this [M for the detail].
- Von Wright's theory is of **prescriptions**. Customs, technical norms and ideal rules lack authority and subject, as he notes. Corpus "norms" of the best-practice kind ("industry should…" from a think tank) are closer to *recommendations*: Searle's weak directives, or IG "shared strategies" (§9.3). They are not prescriptions.
- LegalRuleML is built for **executable** legal rules. Most of it (formula syntax, rule engines) is beside the point here. The glossary and metamodel concepts are the useful part.

---

## 5. Toulmin, Walton, AIF/IAT

### 5.1 Toulmin (1958)

**Source.** Toulmin, *The Uses of Argument* (CUP 1958; 2nd ed. 2003). [S] via Verheij, B. 2005, "Evaluating arguments based on Toulmin's scheme," *Argumentation* 19:347–371, <https://www.ai.rug.nl/~verheij/publications/pdf/toulmin2005.pdf>, which quotes with page numbers.

- **Claim and data** (p. 97): "the claim or conclusion whose merits we are seeking to establish (C) and the facts we appeal to as a foundation for the claim … our data (D)".
- **Warrant** (p. 98): "general, hypothetical statements, which can act as bridges, and authorize the sort of step to which our particular argument commits us".
- **Backing**: support for the warrant (pp. 103–105). In Verheij's reading, backings can be categorical statements of fact, while warrants are bridge-like.
- **Qualifier**: the force of the step, e.g. "presumably" (Verheij §2, Toulmin's Harry/Bermuda example).
- **Rebuttal** (p. 101): "conditions of exception". They "indicate circumstances in which the general authority of the warrant would have to be set aside", and are also "exceptional circumstances which might be capable of defeating or rebutting the warranted conclusion".

  Verheij: "Toulmin speaks of the defeat (or rebutting) of the conclusion, of the applicability of the warrant and of the authority of the warrant, in a rather loose manner, without further distinction." He separates five attackable statements.

**Fit.**
- *Warrant* is the right name for what draft 2 calls a load-bearing dependency, or "transfer by dominance". *Backing* is the right name for what supports a warrant: a source's methodology or epistemic policy (draft 2 §4 "About knowledge"). This links the project's **Methodology** column to the argument layer. A methodology is the *backing* for a family of warrants.
- **Qualifier.** In Toulmin it is the modal force of one inference. Draft 2's "qualifier" carries:
  - likelihood scales;
  - knowledge states;
  - conditions and scope;
  - perspective;
  - mitigation state;
  - measurement conditions.

  Most of those are Toulmin's *data* or *conditions of rebuttal*, or not argument parts at all. If the lexicon adopts "qualifier", I'd suggest it carry Toulmin's narrow sense. The broad bundle needs its own name, or should be dissolved into its parts. Joseph's rule cuts both ways here: the established word exists, but it means something narrower than draft 2's use.
- **Rebuttal** collides with Pollock's *rebutting* (§3). Toulmin's rebuttal is closer to an *exception condition*, which is often an undercutter. A lexicon note is warranted.
- **[M] Field-dependence.** Toulmin holds that warrants and backing differ by field (law, science, ethics) while the layout is invariant. That suits a corpus spanning statute, science and corporate policy. Not checked.

### 5.2 Walton's schemes; the Argument Interchange Format; Inference Anchoring Theory

**Sources.**
- SEP "Informal Logic" (Groarke, rev. Jan 2026) §4.4. [S]
- Walton, Reed & Macagno 2008, *Argumentation Schemes* (CUP). Per SEP "a compendium of 96 schemes". [S]
- Budzynska, Janier, Reed, Saint-Dizier, Stede & Yaskorska, "A model for processing illocutionary structures and argumentation in debates," LREC 2014. [P], abstract and §1–2, <https://aclanthology.org/L14-1599.pdf>.

**The expert-opinion scheme** as SEP gives it [S]. Premises: "A is an authority in domain D. / A says that T is true. / T is within D." Conclusion: "(Therefore) T is true." Critical questions:
1. How credible is A?
2. Is A an authority in domain D?
3. What did A assert that implies T?
4. Is A someone who can be trusted?
5. Is T consistent with what other experts assert?
6. Is A's assertion of T based on evidence?

[M] Walton's own labels for the six are expertise, field, opinion, trustworthiness, consistency, backup evidence. Prakken treats schemes as defeasible inference rules, and critical questions as pointers to undermining or undercutting attacks [S, SEP; detail M].

**[M] Argument from analogy** (Walton): a similarity premise, a base-case premise, a conclusion. Its critical questions ask about relevant differences, and about counter-analogies to cases that point the other way. Not checked.

**[M] *A fortiori*** (classical; Latin "from the stronger"): if the claim holds for the harder case, it holds for the easier. *A pari* (from parity) and *a contrario* (by contrast) are siblings, standard in legal reasoning. Not checked. Draft 2's "transfer by dominance" ("serve as an upper bound for the risks of this model as well") is an *a fortiori* argument, the "ancient word" case in Joseph's rule. The word is old enough that verifying its sense is low-stakes. But I did not find an authoritative source this session, so it is marked M.

**Inference Anchoring Theory** [P]:
> "Speech acts that form a part of argumentative discourse can be seen as anchors for the establishment of inferences between propositions"

IAT links locutions to their propositional contents by **illocutionary connections** (asserting, questioning, challenging, …). It treats *arguing* as anchored in **transitions** between locutions. It also discusses rhetorical questions with "only assertive illocution", which is indirect force again. [M] IAT extends the Argument Interchange Format (AIF): I-nodes for propositions, S-nodes for rule application (RA), conflict (CA) and preference (PA). AIF was proposed by Chesñevar, Reed et al. 2006.

**Fit.**
- Draft 2 §4's **analogy/transfer** kind ("respects claimed and denied", "Where Analogies Break") is Walton's analogy scheme with its critical questions answered *by the source itself*. Analogy is the most common argument form in lit-a. A scheme catalogue gives a typed slot per scheme. The source's own "where it breaks" becomes its answer to a critical question.
- IASR's appeals to "experts repeatedly highlighted" and the opinion-distribution claims (draft 2 §4) are expert-opinion and *popular-opinion* schemes [M for the latter scheme's name].
- **IAT is the architecture draft 2 drew as two planes.** It anchors the argument graph *in* the speech acts, keeping both. That is draft 2 §1's evidence plane (locutions) → resolution → propositions. If anything here is a precedent for the *whole* assertion layer, IAT/AIF is the closest. Next step if wanted: read Budzynska & Reed 2011 and the AIF ontology [not done].

**Strain.** Walton's CQ5 asks about consistency with other experts, but schemes have no notion of the *independence* of the experts. The project's "correlation is not corroboration" needs §9.4 for that.

---

## 6. Safety cases: CAE, GSN, SACM, eliminative argumentation, Assurance 2.0

**Sources.**
- **OMG SACM 2.2**, Structured Assurance Case Metamodel, formal/21-11-01, released April 2022. **[P]** <https://www.omg.org/spec/SACM/2.2/PDF>.
- **GSN Community Standard v3** (SCSC-141C, ACWG, May 2021). Element definitions [s], from a search summary of <https://scsc.uk/scsc-141c>. The v3 additions [P], from the ACWG summary "Changes from Version 2 to Version 3", <https://www.scsc.uk/file/gc/GSNv2-to-v3_changes-1092.pdf>.
- **Goodenough, Weinstock & Klein 2015**, *Eliminative Argumentation: A Basis for Arguing Confidence in System Properties*, CMU/SEI-2015-TR-005. **[P]** <https://www.sei.cmu.edu/documents/1248/2015_005_001_434813.pdf>.
- **Bloomfield & Rushby**, "Assurance 2.0: A Manifesto," arXiv:2004.10474 (v3, 2021). **[P]**
- **In corpus:** Buhl et al. 2024, *Safety cases for frontier AI* (relata `buhl-2024-safety`), §4.3 and fns. 16–17. **[P]**

### 6.1 Definitions

**SACM AssertionDeclaration** [P], §11.8:
- `asserted`: the default.
- `needsSupport`: "further argumentation has yet to be provided to support the Assertion".
- `assumed`: "declared by the author as being assumed to be true rather than being supported by further argumentation".
- `axiomatic`: "axiomatically true, so that no further argumentation is needed".
- `defeated`: "defeated by counter-evidence and/or argumentation".
- `asCited`: "because the Assertion is cited, the AssertionDeclaration should be transitively derived from the value of the AssertionDeclaration of the cited Assertion".

**SACM, further** [P]:
- *Assertion* (§11.10) records "the propositions of Argumentation (including both the Claims about the subject of the argument and the structure of the Argumentation being asserted)".
- *AssertedRelationship* (§11.13) has *Assertion* as its superclass. A support link is itself an assertion, with its own declaration. It carries `isCounter` for counter-evidence or counter-argument.
- An Assertion can carry **metaClaims**: "Claims concerning (i.e., about) the Assertion (e.g., regarding the confidence in the Assertion)".

**GSN.**
- Elements [s]:
  - Goal ("a claim forming part of the argument");
  - Strategy ("the nature of the inference that exists between a goal and its supporting goal(s)");
  - Solution (a reference to evidence);
  - Context;
  - Assumption ("an intentionally unsubstantiated statement");
  - Justification ("a statement of rationale").
- v3 change list [P]: "New notation for Dialectics. Allows Challenges to the argument to be recorded", "representing/recording counter-argument and counter-evidence". A **Defeated** decorator applies to any element *or any relationship*. Examples distinguish "Unresolved Challenge" from "Successful Challenge", and include a "Challenge by Argument to a Challenge".
- v3 also makes **Confidence Arguments** part of the main definition [P, change list].

**CAE** [S], via Bloomfield & Rushby:
- CAE has "five basic CAE Blocks: evidence incorporation, calculation, decomposition, substitution, and concretion", citing Bloomfield & Netkachova 2014.
- Their terminology note: "we say claim where GSN says goal, we say argument step where CAE says simply argument".
- Their **Indefeasibility Criterion** "requires a comprehensive search for defeaters".
- They name "undercutting defeat" and "rebutting defeater" in Pollock's senses.

**Eliminative argumentation** [P], SEI 2015, §4.3:
> "the defeaters in eliminative argumentation are taken from the three (and only three) kinds of defeaters in defeasible reasoning, which correspond to the three ways of attacking an argument: rebutting and undercutting defeaters [Pollock 1987] and undermining defeaters [Prakken 2010]."

Their definitions:
- rebutting defeaters are "doubts that contradict a claim";
- undermining defeaters are "doubts about evidence";
- undercutting defeaters target inference rules.

Two terminators: "Assumed OK" and "Is OK". And: "The GSN standard explicitly talks about 'undercutting' challenges to a strategy element."

**In corpus** [P], Buhl et al. fn. 16:
> "The term 'argument' is used in a number of different ways in the safety case literature. For example, in the Claims Arguments Evidence framework, it refers to the justification linking a specific claim to a specific piece of evidence …; and in propositional logic, an argument would include the evidence and conclusion … We follow the use of the term in the Goal Structuring Notation framework"

Fn. 17: evidence provides "some reason to think the claim is true, but these reasons may be overridden by defeaters (Bloomfield et al., 2021)".

### 6.2 Fit

- **SACM's AssertionDeclaration is a published, standardised stance enumeration** that overlaps draft 2's stance question 1:
  - `assumed` ≈ "adopted assumption";
  - `needsSupport` ≈ "a slot declared but empty", "we are studying…";
  - `axiomatic` ≈ ASPIC+ axioms;
  - `defeated` = a contest standing;
  - **`asCited` ≈ "relays" / "reports without endorsing"**: the declaration *inherits* from the cited source.

  `asCited` is also a precedent for draft 2 §3.3's scope-inherited qualifiers, as inheritance by citation. SACM was built so declarations can differ between the *author's* package and *cited* packages. That is a two-voice model, though not an n-voice one.
- **Relationships are assertions** (SACM; GSN v3's defeated *relationships*). This is what draft 2's argument layer needs. "A supports B" is itself something a source says, and something another source can challenge (undercutting). It also gives the established form of draft 2 §4's **"claim about a claim"**: SACM's *metaClaim*.
- **GSN v3 Dialectics** gives the logos "standing" an established notation: unresolved vs successful challenge, challenge to a challenge, defeated element vs defeated relationship.
- **Sources that *are* safety cases** (Buhl's sketch, AISI's safety-case sketches, Anthropic's risk reports, the STPA→CAE design pattern in lit-a) can be recorded *in* CAE/GSN terms on their own terms. For those families the notation is the source's own vocabulary.
- **The term "argument" collides** inside the corpus's own safety-case literature (Buhl fn. 16). The lexicon needs a note on it.

### 6.3 Strains

- Safety-case notations are **for constructing one's own case**. They have no author other than the case-maker, and no reported speech. "Defeated" there is the case-maker's or reviewer's *verdict*. In this project a defeat is always someone's attributed claim (§3.2).
- "Context" and "Strategy" in GSN collide with IG's *Context* and *shared strategy* (§9.3), and with draft 2's own uses.
- GSN's Assumption ("intentionally unsubstantiated statement") and Justification are *roles in an argument*, not stances. They line up with draft 2's stance question 3 "adopted assumption" only for the author's own working assumptions.

---

## 7. Two worked consequences for draft 2 (my reading, offered for checking)

### 7.1 Stance question 1 decomposes into established axes

Draft 2's ten values for "commitment to the content's truth" sort, under the vocabulary above, into four independent things:

| Draft 2 value | Established home |
|---|---|
| asserts / speculates | **one illocutionary point, different strength** (Searle feature 4; SEP's assert ≻ conjecture ≻ guess) |
| believes, with adjudication deferred | assertion (strength), plus a **directive or declaration about who decides**: a power assignment (Hohfeld) |
| reports without endorsing; relays | **nested source**: author `<U,u>` towards p, while asserting that S holds p (FactBank, §9.1; SACM `asCited`; Goffman: the author is *animator* only, §9.2) |
| explicitly abstains | author `<U,u>` (FactBank's "does not overtly commit") |
| holds insufficient but not false | **undercutting** (argument relation, §3) |
| rejects or rebuts | **rebutting** (argument relation) |
| discounts as a class | **undercutting a scheme or warrant** (§5) |
| rules out on evidence | rebutting or undermining argument made by the source |

What stays genuinely about commitment is strength plus factuality value relative to source. That is FactBank's `<CT/PR/PS/U, +/−/u>` per source, verified in §9.1.

Stance question 2 ("mode") has established names for most entries:
- *exhibited as a specimen* = **mention**, not use [M; standard philosophy-of-language distinction];
- *presupposed* = presupposition (PDTB "Ftv"/presupposed; Searle's expressives presuppose);
- *stipulated for this document* = **stipulative definition** (SEP "Definitions"), which in Searle is a linguistic declaration (§2.1);
- *hypothetical/scenario* = supposition. In von Wright's terms a scenario-conditioned "should" may be a hypothetical norm.

### 7.2 Norms (§6.4): adopt rather than coin

Suggested layering, each layer established:
1. **The speech act** (evidence plane): directive / commissive / declaration, with strength and mode of achievement (Searle).
2. **The institutional statement** (its grammar): IG 2.0 regulative (Attributes, Deontic, Aim, Object, Context = activation condition + execution constraint, Or else) or constitutive (Constituted Entity, Modal, Constitutive Function, Constituting Properties, Context, Or else).
3. **The normative positions created**: Hohfeld's eight, first and second order, with the correlative party stated or "none". Strong vs weak permission (LegalRuleML).
4. **Its legal status over time**: applicable / in force / efficacy / valid, with status-changing events (LegalRuleML).
5. **What we record about all of the above**: norm-propositions, attributed (von Wright).

Draft 2 §6.4 is very close to IG + Hohfeld already; the change is mostly renaming plus the second-order layer. Draft 2's "commitment" becomes: a commissive act (1), whose IG statement (2) has Attributes = the speaker, creating a duty (3) whose correlative claim-holder is recorded, possibly "none". It stops being "a norm where imposer = bearer".

### 7.3 The IASR conflict draft 2 flags dissolves into a recordable ambiguity

Draft 2 §3.3: "IASR declares no recommendations and still says 'should not release'". The sentence, verified in `ref/iasr-2026-full.md`:
> "To avoid catastrophic harm, developers of open-weight models should not release models without evaluating risks"

This has exactly von Wright's **technical-norm** form: wanted end, then must-not. A technical norm logically presupposes an **anankastic statement**: evaluating risks is a necessary condition of avoiding catastrophic harm. That statement is truth-apt and fits a report that declares itself descriptive. Whether IASR also *prescribes* (heteronomous prescription from an authority) is the open question.

The established vocabulary lets the record say "ambiguous among {technical norm presupposing anankastic claim, prescription}" with both candidates named. A flagged conflict becomes a typed ambiguity. My reading, not checked against how IASR uses the "Challenges for policymakers" section elsewhere.

---

## 8. Corrections and misrememberings

- **Two defeater kinds → three.** Rebutting, undercutting (Pollock), undermining (Prakken/ASPIC+). The SEI and Assurance 2.0 safety-case literature uses all three [P]. Draft 2's premise-attached `defeats` is undermining.
- **Searle's first class** is "Representatives" in the 1975/76 papers [P]. "Assertives" is the 1979 label [S, Kloosterhuis quoting Searle 1979].
- **Declarations do not all need an institution.** Searle exempts declarations "that concern language itself" (define, name, dub) [P]. My first draft of this file got this wrong and was corrected on re-reading.
- **Searle 1975 vs 1976.** Both exist. The *Language in Society* paper (1976) is a version of the Minnesota Studies chapter (1975); *Expression and Meaning* (1979) reprints it as "A taxonomy of illocutionary acts". Cite by edition read.
- **Toulmin's "qualifier"** is narrower than draft 2's. **Toulmin's "rebuttal"** is not Pollock's "rebutting". Both are [S].
- **Hohfeld's "exemption" = immunity** [P], not the derogation-from-obligation sense draft 2 uses.
- **Evidentiality** in the linguistic sense is grammatical. English lacks it; "reportedly" and "it is said that" are explicitly *excluded* as lexical or biclausal (WALS 77) [P]. For English text, the right frame is **evidential strategies** [M, Aikhenvald's term] or attribution/factuality annotation (§9.1). Evidentiality and **epistemic modality** are distinct: evidence for vs confidence in [P, WALS].
- **"Conjunctive / disjunctive / convergent"** (draft 2 §3.4): the established terms are **linked** (premises support "(only) when combined") vs **convergent** (independent reasons) [S, SEP Informal Logic]. [M] *Serial* and *divergent* complete the usual set. "Disjunctive" has no standard counterpart that I know of.
- Draft 2 §8 lists CAE/GSN as "training knowledge". It is now partly verified: SACM [P], SEI [P], GSN v3 change list [P], CAE blocks [S].

## 9. Better or complementary vocabulary not named in the brief

### 9.1 Factuality and attribution annotation: FactBank, PDTB

**FactBank** [P]: Saurí & Pustejovsky, "From structure to interpretation: A double-layered annotation for event factuality" (LREC 2008 workshop), <https://www.cs.brandeis.edu/~roser/pubs/sauriPustejovsky_lrec08_2.pdf>. Corpus: LDC2009T23. Journal version [s]: *LRE* 43(3):227–268, 2009.
- Values are `<modality, polarity>`, with modality certain (CT), probable (PR), possible (PS) or unknown (U). Six committed values, plus `<CT,u>` ("total certainty about the factual nature of the event but … not clear … what the output is") and `<U,u>`. `<U,u>` covers the source not knowing, not being aware, or not overtly committing.
- **Nested sources**: "By default, events mentioned in discourse always have an implicit source, viz., the author." Source-introducing predicates add sources. "Izvestiya is not a licit source of the factuality of event e2, but Izvestiya according to the author instead." The same event can be CT+ for one nested source, CT− for another, and Uu for the author.
- **Fit: very strong.** This *is* draft 2's "Nested voices stay nested … Stance is recorded per layer" and the "characterises-position-of" rule ("must never be attributed to B as a quotation"), with a worked value system and an annotated corpus.

**PDTB 2.0 attribution** [P]: Prasad et al. 2007, *The Penn Discourse Treebank 2.0 Annotation Manual* (IRCS report), ch. 5, <https://repository.upenn.edu/ircs_reports/203>.
- Attribution is "a relation of 'ownership' between abstract objects and individuals or agents".
- **Source**: writer (Wr) / other specific agent (Ot) / arbitrary (Arb) / inherited (Inh).
- **Type**:
  - assertion propositions, "Comm": verbs of communication;
  - belief propositions, "PAtt": propositional-attitude verbs;
  - facts, "Ftv": factive verbs, truth "taken for granted";
  - eventualities, "Ctrl": "an agent's intention/attitude towards a considered event", via verbs like persuade, permit, order.
- **Scopal polarity**: "didn't say", "don't think" reversing the content.
- **Determinacy**: "Indet" where the attribution itself is cancelled, e.g. conjectured.
- **Fit.** "Arb" is draft 2's "experts repeatedly highlighted" / "reports suggest". Ftv vs Comm vs PAtt separates "X found that" (presupposes) from "X claims" from "X believes". Determinacy catches attributions inside conditionals: "if developers believed…".

### 9.2 Goffman's production format: animator, author, principal

[S] Goffman, "Footing," *Semiotica* 25 (1979):1–29; reprinted in *Forms of Talk* (1981). Quoted with page numbers in Kišiček & Žagar (eds.), *What do we know about the world?*, Ljubljana 2013, p. 376, <https://pei.si/ISBN/978-961-270-170-3/files/basic-html/page376.html>:
- **animator**: "an individual active in the role of utterance production";
- **author**: "someone who has selected the sentiments that are being expressed and the words in which they are encoded";
- **principal**: "Someone whose position is established by the words that are spoken, someone whose beliefs have been told, someone who is committed to what the words say".

**Fit.** This is draft 2 §3.1's "writers / responsible party / endorsement status", named in 1979. The corpus pulls Goffman's *principal* apart further. IASR's Chair holds "ultimate responsibility" (the position established) while the report "does not necessarily represent the views of the Chair" (beliefs told, commitment). Recording principal as three sub-facts may be needed; that is my reading. A relayed quotation makes the relay the animator; Goffman's own example is reading a deposition.

### 9.3 Institutional Grammar: ADICO and IG 2.0

- Crawford, S. E. S. & Ostrom, E. 1995, "A grammar of institutions," *APSR* 89(3):582–600. [S] via Basurto et al. 2010, "A systematic approach to institutional analysis: applying Crawford and Ostrom's grammar," *Political Research Quarterly* 63:523ff, which applies the grammar to "two pieces of U.S. legislation". Hosted at <https://dukespace.lib.duke.edu/server/api/core/bitstreams/d0cc84f8-8b66-4ea9-8c35-228da83d3d49/content>.
- Frantz, C. K. & Siddiki, S. N., *Institutional Grammar 2.0 Codebook*, v1.4, 2024, arXiv:2008.08937. **[P]**

**ADICO** [S]. Crawford & Ostrom 1995: 583, quoted:
> "Institutional statement refers to the shared linguistic constraint or opportunity that prescribes, permits, or advises actions or outcomes for actors (both individual and corporate)."

Components: Attribute, Deontic, aIm, Condition, Or else. *Strategies* = AIC, *norms* = ADIC, *rules* = ADICO, i.e. with a sanction. "deontic operators can vary by prescriptive force; for example, must represents more force than should" (citing Crawford & Ostrom 2005: 142–49). With no explicit condition, the default is "at all times".

**IG 2.0** [P], codebook §1 and Tables 2–3:
- *Constitutive* statements "parameterize an institutional setting … introduce, modify or otherwise constitute features of an institutional system", including "actor positions and roles". *Regulative* statements "describe actors' duties and discretion".
- Regulative components: Attributes, Deontic, Aim, Object, **Context** and Or else. Context is split into an **"Activation Condition"** (settings in which the action applies) and an **"Execution Constraint"** (qualifies the action).
- Constitutive components: Constituted Entity, Modal, **Constitutive Function** ("defining, establishing, or modifying … including the conferral of status"), Constituting Properties, Context, Or else. A constitutive Or else can be "existential in kind (e.g., invalidating policy)".
- **Hybrid** statements mix both types.

**Fit: the strongest find for §6.4 and §6.2.**
- It is a coding grammar for exactly this kind of text, with a codebook and a literature of application to statutes and regulations.
- Its *regulative/constitutive* split is Searle's, operationalised.
- Activation condition vs execution constraint is draft 2's "applicability condition" vs "trigger → time limit → act".
- Its *Or else*, and the ADIC vs ADICO distinction, is the materiality question: a commitment without sanction is a *norm*, a statute with one a *rule*.

**Strains and hazards.**
- IG's **"norm" means ADIC specifically**, without sanction. That collides with "norm" as draft 2's umbrella and with von Wright's general sense. Pick one and gloss the others.
- "Shared strategy" and "Context" collide with GSN.
- IG codes *statements*. Draft 2's role-conferral-under-conditions needs Hohfeld's operative facts on top.

### 9.4 Source reliability × information credibility (Admiralty / NATO grading)

[S] Wikipedia, "Intelligence source and information reliability", citing US Army FM 2-22.3 Appendix B. The Army primary (ATP 2-22.9 on irp.fas.org) was not fetchable.
- Source reliability A–F: "Reliable" … "Unreliable", F = "cannot be judged".
- Information credibility 1–6, with 1 = "Confirmed by independent Sources: Logical, consistent with other relevant information, confirmed by independent sources", 2 = "Probably true … not confirmed", through 5 = "Improbable" and 6 = cannot be judged.

**Fit.** Two separate axes: who said it vs how well the content holds up. "Confirmed" is defined by *independent* confirmation, which is the project's "correlation is not corroboration" in an operational standard. It belongs beside "soft evidence stays in, marked". Our own grading of a source would be *our* attributed assertion, in keeping with compilation-not-adjudication. The risk-formalisms sibling may cover ICD 203 or IPCC calibrated language, which is adjacent.

### 9.5 Appraisal theory: ENGAGEMENT

[s] Martin, J. R. & White, P. R. R. 2005, *The Language of Evaluation: Appraisal in English* (Palgrave). Only search-summary and secondary-application level here; the book was not seen.
- **Monogloss**: a bare assertion, no alternative acknowledged.
- **Heterogloss**, which is either contractive or expansive:
  - contract → **disclaim** (deny, counter) and **proclaim** (concur, pronounce, endorse);
  - expand → **entertain** and **attribute** (acknowledge, distance).

**Fit, if the categories hold up on reading the primary:**

| ENGAGEMENT | draft 2 stance question 1 |
|---|---|
| attribute: acknowledge | "reports without endorsing" |
| attribute: distance | "relays", including scare-quoted relays |
| entertain | "speculates" |
| disclaim: deny | "rejects" |
| proclaim: endorse | presenting a source as warranting a claim |
| monogloss | flat assertion |

It is a linguistics framework for exactly how a text positions itself among voices, and is widely applied to news and academic prose. Worth reading the primary (Martin & White 2005 ch. 3) before adopting.

### 9.6 Others worth a look (not researched here)

- **[M] Hyland's hedges and boosters** (*Hedging in Scientific Research Articles*, 1998; *Metadiscourse*, 2005). The standard corpus-linguistic account of how academic and policy prose marks commitment. Probably the best source for "we believe" / "may" / "clearly" in English, given the evidentiality caveat above.
- **[M] Akoma Ntoso / OASIS LegalDocML** for document structure: recitals, articles, annexes; part-level force; versioning and point-in-time. Draft 2 §2's document parts.
- **[M] Provenance and citation standards**: W3C PROV-O (`wasQuotedFrom`, `wasRevisionOf`, `hadPrimarySource`), CiTO (citation typing), micropublications, nanopublications. These overlap draft 2 §3.4 lineage. The terminology/provenance sibling is covering this area, so I only flag the overlap.
- **[M] Brandom's commitment and entitlement**, and Hamblin/Walton **commitment stores** in dialogue theory. An established sense of "commitment" (what a speaker is answerable for) that collides with Searle's commissive and draft 2's stance question 1.
- **[M] Walton & Krabbe's dialogue types** (persuasion, inquiry, negotiation, …) [S that they exist: SEP Informal Logic §3.4]. A genre-level frame that might type documents (a consultation response vs a safety case vs a statute), in the spirit of the us-gov atlas's "genre determines the speech act".

## 10. Terminology collisions to put in the lexicon

1. **argument**:
   - CAE: claim–evidence justification;
   - GSN: the whole structure;
   - logic: premises + conclusion;
   - Bloomfield & Rushby: "argument step".

   Seen in corpus (Buhl fn. 16).
2. **rebuttal** (Toulmin: exception condition, loosely) vs **rebutting** (Pollock/ASPIC+: denies the conclusion).
3. **qualifier**: Toulmin, the force of an inference, vs draft 2's bundle of scope, conditions and measurement context.
4. **norm**: IG (ADIC, no sanction) vs von Wright (general, with prescriptions as one kind) vs draft 2 (umbrella) vs LegalRuleML ("binding directive from a Legal Authority").
5. **exemption**: Hohfeld (= immunity) vs draft 2 (derogation, ≈ strong permission / privilege).
6. **commitment**:
   - Searle: commissive point;
   - draft 2 stance question 1: commitment to truth, which is Searle's *representative* "commit … to something's being the case";
   - draft 2 §6.4: self-imposed norm;
   - dialogue theory: commitment store [M].

   Four senses in play.
7. **declaration**: Searle's class (makes its content true by being performed; institutional, or linguistic for definitions) vs ordinary "declares" (often just asserts). A "declared scope" in draft 2 may be either: "this report covers only X" can stipulate the document's scope (a linguistic declaration) or describe it (a representative).
8. **assertion**:
   - Searle: representative;
   - SACM: any proposition in the argument, *including relationships*;
   - PDTB: "Comm" attribution type;
   - draft 2: any speech act.
9. **context / strategy**: GSN vs IG vs ordinary use.
10. **defeated**: a verdict (SACM, GSN) vs an attack (ASPIC+) vs a source's claim of defeat (what this project would record).
11. **evidential**: linguistics (grammatical source-marking) vs Hohfeld's "evidential facts" vs ordinary "evidential breadth" (draft 2 §3.3).

## 11. Honest limits

- **Not read at primary:**
  - Searle 1979 (the 1975 chapter was read whole);
  - Austin 1962;
  - Pollock 1987;
  - Toulmin 1958;
  - Walton, Reed & Macagno 2008;
  - Crawford & Ostrom 1995 (IG 2.0 *is* [P]);
  - Martin & White 2005;
  - Goffman 1979;
  - GSN v3 full standard (only its change summary);
  - Bloomfield & Netkachova 2014;
  - FM 2-22.3.

  Where these are [S], the secondary quotes with page numbers. They are still one step removed.
- I checked no corpus counts. "Expressives are rare" and "analogy is the commonest form in lit-a" come from my impression and from draft 2 respectively.
- The fit judgements in §2.2, §4.4, §7 and §9 are mine. They are the parts most worth a second reader. In particular: the stance-question-1 decomposition (§7.1), the norm layering (§7.2) and the IASR technical-norm reading (§7.3).
- Not done: AIF ontology, Budzynska & Reed 2011, Walton's analogy scheme at source, Hyland, Akoma Ntoso, LegalDocML.

## Sources fetched this session

| Source | URL | Status |
|---|---|---|
| Searle 1975, "A taxonomy of illocutionary acts" (Minnesota Studies 7) | <https://conservancy.umn.edu/server/api/core/bitstreams/f1857cae-5ee1-453c-803e-4e11854b2bf6/content> | P (pp. 344–369, complete) |
| Review of Searle 1976 in *Lexis* 1(1), 1977 | <https://revistas.pucp.edu.pe/index.php/lexis/article/download/4648/4650> | S |
| Kloosterhuis 1998, ISSA Proceedings (Searle 1979; Hart; Austin) | <https://rozenbergquarterly.com/?p=14018> | S |
| SEP "Speech Acts" (Green) | <https://plato.stanford.edu/entries/speech-acts/> | S |
| SEP "John Langshaw Austin" (Longworth) | <https://plato.stanford.edu/entries/austin-jl/> | S |
| SEP "Social Ontology" (Epstein) | <https://plato.stanford.edu/entries/social-ontology/> | S |
| Hohfeld 1913 | <https://persweb.wabash.edu/facstaff/helmang/phi213-1314S/phi213-txtbrwsr/Hohfeld/Hohfeld1913.html> | P |
| SEP "Rights" (Wenar) | <https://plato.stanford.edu/entries/rights/> | S |
| von Wright 1963, *Norm and Action*, chs. I, V, VII | <https://giffordarchives.org/books/norm-and-action/i-norms-general> · <https://giffordarchives.org/node/1514> · <https://giffordarchives.org/books/norm-and-action/vii-norms-and-existence> | P |
| SEP "Deontic Logic" (McNamara & Van De Putte) | <https://plato.stanford.edu/entries/logic-deontic/> | S |
| LegalRuleML Core Spec 1.0 (OASIS Standard 2021) | <https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/os/legalruleml-core-spec-v1.0-os.html> | P |
| SEP "Defeasible Reasoning" (Koons) | <https://plato.stanford.edu/entries/reasoning-defeasible/> | S |
| Modgil & Prakken, ASPIC+ with preferences (arXiv:1804.06763) | <https://arxiv.org/pdf/1804.06763> | P |
| Verheij 2005 on Toulmin | <https://www.ai.rug.nl/~verheij/publications/pdf/toulmin2005.pdf> | S (for Toulmin) |
| SEP "Informal Logic" (Groarke) | <https://plato.stanford.edu/entries/logic-informal/> | S |
| SEP "Argument and Argumentation" | <https://plato.stanford.edu/entries/argument/> | S (context only) |
| Budzynska et al. 2014, IAT (LREC) | <https://aclanthology.org/L14-1599.pdf> | P (partial) |
| OMG SACM 2.2 | <https://www.omg.org/spec/SACM/2.2/PDF> | P |
| GSN v2→v3 changes (ACWG) | <https://www.scsc.uk/file/gc/GSNv2-to-v3_changes-1092.pdf> | P |
| GSN v3 standard page | <https://scsc.uk/scsc-141c> | s |
| Goodenough, Weinstock & Klein 2015 (SEI) | <https://www.sei.cmu.edu/documents/1248/2015_005_001_434813.pdf> | P |
| Khakzad Shahandashti et al. 2024 (arXiv:2401.17991) | <https://arxiv.org/pdf/2401.17991> | S (cross-check) |
| Bloomfield & Rushby, Assurance 2.0 (arXiv:2004.10474) | <https://arxiv.org/pdf/2004.10474> | P |
| Buhl et al. 2024 (corpus) | relata `buhl-2024-safety` | P |
| WALS ch. 77 (de Haan) | <https://wals.info/chapter/77> | P |
| Saurí & Pustejovsky 2008, FactBank | <https://www.cs.brandeis.edu/~roser/pubs/sauriPustejovsky_lrec08_2.pdf> | P |
| FactBank 1.0 readme (LDC2009T23) | <https://catalog.ldc.upenn.edu/docs/LDC2009T23/readme.pdf> | P |
| PDTB 2.0 Annotation Manual | <https://repository.upenn.edu/ircs_reports/203> | P (ch. 5) |
| Kišiček & Žagar (eds.) 2013, p. 376 (Goffman) | <https://pei.si/ISBN/978-961-270-170-3/files/basic-html/page376.html> | S |
| Basurto et al. 2010 (Crawford & Ostrom) | <https://dukespace.lib.duke.edu/server/api/core/bitstreams/d0cc84f8-8b66-4ea9-8c35-228da83d3d49/content> | S |
| Frantz & Siddiki, IG 2.0 Codebook v1.4 (arXiv:2008.08937) | <https://arxiv.org/pdf/2008.08937> | P |
| Wikipedia, intelligence source and information reliability | <https://en.wikipedia.org/wiki/Intelligence_source_and_information_reliability> | S |
| Martin & White, ENGAGEMENT | search summaries only | s |
| IASR 2026, the "should not release" sentence | `ref/iasr-2026-full.md` | P |
