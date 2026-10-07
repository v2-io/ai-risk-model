# De novo feedback 1: an adversarial pass on the alignment-referents spike

*Written 2026-10-06 by Claude (Opus 5.5), from the spike's files as written, the regenerated corpus extractions, and primaries fetched this session. This is an independent pass, not the commissioned verification, and it is not a blind recode (see §5).*

**Conflicts to weigh.** I am the same model family as the spike's author and both of its research agents. Where I agree with the spike, that is coherence, not confirmation. Several findings below turn on Anthropic's and OpenAI's own documents, and I am an Anthropic model reading both.

**Labels.** *Verified*: I read the passage this session, at the corpus extraction (regenerated with `bin/extract-text`, pdftotext 26.09.0) or at the primary. *Inference*: my reading, open to challenge. *[M]*: from memory, not checked this session.

---

## 0. Verdict in brief

The spike's direction holds up. Alignment is better modelled as a relation with slots than as a word with a default referent. "To whom" covers several relations, which the map's single edge type merges. And a record-level default would be the model taking a side. Most of its corpus quotations are accurate at the cited lines: I checked about sixty, and the reproduction instructions work exactly (§7).

But several load-bearing pieces are weaker than the files present them, and a few are wrong:

1. **The "one developer, two filings" finding is a misreading** (§1.1). OpenAI's Preparedness Framework and Model Spec have the same structure: a category named for misalignment ("Safeguards against a misaligned model"; "Misaligned goals") that holds *both* misalignment proper and adversarial subversion as separate causes. The real split is between "misaligned" as a *state* and "misalignment" as one *origin*. GDM draws its line by where the cause lives (training versus environment), which lines up with the map's weights/context boundary. That is a sharper and more useful finding than "which writer carried the intent".
2. **GDM does file prompt injection and jailbreaks** (§1.2), outside misalignment, in text the partition table doesn't cite. And GDM states that its four areas are "not a categorization". Yet the spike's headline result calls them partitions.
3. **"The working conflict rule exists, but outside the risk literature" is false for the corpus** (§1.3). IASR 2026, the Singapore Consensus 2026 and Hammond et al. discuss conflict handling among parties (pluralistic alignment, voting, refusal, the median view, personalisation). The Singapore line quoted in §4 as "a fundamentally unsolvable problem" continues "However, there exist principled approaches …".
4. **The list-degeneracy "demonstration" proves less than its conclusion** (§2.1), and it misreads the genre of the passages it is aimed at. The IASR and Shanghai glossary entries describe polysemy ("this can variously refer to"). They are not definitions with a missing conflict rule. The spike's own later refinement, that this is an implicit argument, vindicates them.
5. **The six-row no-go is demonstrated for four rows as written** (§2.2). The society and law rows show indeterminacy, not "a named risk comes out aligned". The developer row is conditional, and the agent row is an uncounted seventh. All of this is repairable, and I found corpus material that strengthens both weak rows.
6. **The invariance pilot can't carry the weight the debrief puts on it** (§3). Its candidate set excludes the agent itself, the same blind spot the spike holds against Gabriel and Keeling. Its coding rule defers admissibility to each source, which is exactly the normative content §1 says the absolute use hides. And on my reading, most of its "truth-apt claims" are noun-phrase labels. "13 of 14 invariant" is better read as "in this sample the harm noun, not the alignment word, carries the verdict". That is a useful finding, but a different one.
7. **The "95% absolute" figure merges anaphoric uses with evaluative ones** (§3.1). Many unindexed uses point back to the source's own stipulated referent. Only the remainder carry the hidden admissibility the spike describes. The proposed use types need a third category for this.
8. **"Standing mismatch" collapses three different confusions in the map's Notes** (§4.1): source attribution, illocutionary force and epistemic status. Only one is about standing. The AISI compaction instance is probably the third kind.

Smaller fidelity and consistency items are in §6. What I checked and found correct is in §7.

---

## 1. Fidelity findings that change conclusions

### 1.1 OpenAI does not file adversarial subversion two ways; "misalignment" is a state in one place and an origin in another

**What the spike says.** `03-structure.md` §3, injection row: the Preparedness Framework (PF) treats it as "subversion by an adversary", distinct from misalignment; the Model Spec "files it *inside* misalignment … One developer, two filings". `01-map.md` §2 item 3: "OpenAI separates the two". The debrief repeats both. The reading originates in `research/lit-alignment-relation.md` §5.1: "this text uses 'misaligned goals' to cover being *misled*: misalignment that a third party induced".

**What the sources say** (*verified*):
- PF v2, L873–876. The section heading is **"C.2 Safeguards against a misaligned model"**. Its first sentence: "several of the Tracked Category capabilities pose risks when models themselves are able to autonomously execute a severe harm, whether due to misalignment or subversion by an adversary." Adversarial subversion is filed *inside* the misaligned-model safeguards section, as one of two causes.
- Model Spec 2026-08-18 (fetched this session): "Misaligned goals: The assistant might pursue the wrong objective **due to misalignment**, misunderstanding the task … **or being misled by a third party** (e.g., erroneously following malicious instructions hidden in a website)." "Misalignment" is listed as one cause *beside* being misled, inside a category whose name describes the resulting state.

The two documents share one structure. A *state* label ("misaligned model", "misaligned goals": the system pursuing the wrong thing, whatever the cause) contains an *origin* label ("misalignment", internally arising) plus other origins (an adversary, a misunderstanding). There is one filing, not two.

**What the corpus disagreement actually is** (*inference, with verified anchors*):
- **Anthropic** (aug L901–903) uses the state reading with origin qualifiers. Misalignment is "naturally-emerging" or "engineered … e.g. via data poisoning".
- **GDM** draws an origin-*location* line. Misalignment requires "intrinsic reasons", and these explicitly include "incorrect inputs to the training process (e.g. training data, reward function)" (shah L2565–2566). Extrinsic, environmental causes make a mistake, not misalignment (L2560–2564). Prompt injection falls outside misalignment: "Even if the AI system is not misaligned, outside actors can compromise the AI system to mount attacks (e.g. via prompt injection attacks or jailbreaks)" (L4658–4659, §6.4 Security).
- So under GDM, poisoning is *in* misalignment (my inference: GDM doesn't name poisoning, but training data is its own example of an intrinsic reason), and injection is *out*.

GDM's boundary is the map's own boundary between the weights and the context. That gives a stronger version of the spike's §3 inference ("the field's partition is a projection of the map's finer structure"). The projection runs along **which part of the agent stack the cause lives in**, as well as, or rather than, along which writer held the intent. I'd suggest the partition table be rebuilt on three columns:
- *state vs origin* use of the word;
- the part the cause enters (weights, context, …);
- the writer.

### 1.2 GDM files injection and jailbreaks, and calls its areas "not a categorization"

- **Injection row.** "GDM's misuse definition says 'the user', so the literal text does not cover it." The definitions don't, but the document does. Prompt injection appears twice (*verified*):
  - in §5.3.2 *Jailbreak resistance*, under "5. Addressing misuse" (L3209: "Another type of attack uses prompt injections to bypass safety instructions that developers place in the system");
  - in §6.4 *Security*, explicitly outside misalignment (quoted above).

  A filing claim made from a source's definitions, when the source files the case itself elsewhere, is the kind of record the project's fidelity principle exists to prevent.
- **Jailbreak row.** "GDM: misuse" is right, and §5.3.2 is the location to cite.
- **"Partitions".** GDM, L192: "Note that this is not a categorization: these areas are neither mutually exclusive nor exhaustive." The same point recurs at L2352. GDM also says the grouping is "based on factors that drive differences in mitigation approaches" (L172–173). The spike quotes the non-exhaustiveness in the Davidson row, but its headline (§0 item 3; README; debrief: "The field's main risk categories move …") still treats GDM's areas as a partition.

  Because GDM's grouping is organised by mitigation, a different "filing" in two sources may reflect different mitigation purposes rather than different referents. That alternative explanation isn't considered.

### 1.3 The corpus does discuss conflict rules; one quotation is cut before its turn

- `03-structure.md` §2: "the missing rule comes from outside the risk literature"; "the corpus's risk definitions borrow a word whose working conflict rule is written down in documents most of them don't cite". The debrief: "The working rule for conflicts exists, but outside the risk literature".
- IASR 2026, md L1906–1908 (*verified*). The spike cites this passage for "Humans do not always agree". The heading is "Humans do not always agree on what behaviours are desirable, **requiring methods to balance competing preferences**". The paragraph ends: "AI developers can design systems to avoid generating controversial answers **by refusing to respond** to certain requests, or **align with the median viewpoint** in some relevant sample of people, or **personalise systems to individual users**", after citing "'pluralistic alignment' techniques that aim to strike a balance between competing preferences".

  These are conflict rules, in the corpus, and one of them is the null action.
- Singapore Consensus 2026, L1427–1431 (*verified*). §4's society row quotes "a fundamentally unsolvable problem". The next sentence is: "**However, there exist principled approaches for attempting to balance different viewpoints in ways that are normatively accepted** (Sorensen et al., 2024; Conitzer et al, 2024). For example, many human institutions use voting as an acceptable way of resolving disagreements." The heading is "Pluralistic and legal alignment".

  Quoting the first sentence alone, in a row arguing that the society referent gives no verdict, is selective. I don't think it was deliberate (the clause sits at a line break), but it is exactly what the project's fidelity principle guards against.
- Hammond et al. also have a "Pluralistic Alignment" heading (L2785ff.). The literature report lists Sorensen et al. 2024 and rates it "Moderate".

The accurate claim is narrower: *the corpus's definitions* state no conflict rule, while *the corpus's bodies* discuss several, and the companies' behaviour documents state operative ones. That still supports §8's slot proposal.

### 1.4 The EU guidelines' footnote 12 says nearly the opposite of how it is used

`04-actors.md` §3 and §5, and the debrief, use "who has the control over the model's weights" (gpai-guidelines fn 12) as an operative fact conferring provider status, alongside the modification threshold. The footnote reads (*verified*, L791–793): "Whether it is the original provider or a downstream actor who modifies the general-purpose AI model must be assessed on a case-by-cases basis. An important factor in this assessment may be who has the control over the model's weights, **for example, in case of fine-tuning via API**."

The footnote is about *attributing the modification act*. When a customer fine-tunes through the provider's API, the customer supplies the data (writes), but the weights stay in the provider's control, so the modification may be attributed to the provider. That is an instance of an instrument *decoupling* the writing act from the role and attaching the role to control instead. It cuts against §5's "operative facts … are writing acts", at the very citation offered for it.

Also, ⅓ of training compute is an "**indicative** criterion" (para 63), not a rule. The rule is "significant change" (para 62). The spike and the role-vocabulary report state it as a threshold that "makes one a provider".

I think §5's conferral picture survives. The repair is to name **control** as a separate operative-fact type, beside writing and market acts. That also fits the de facto / de jure relation the spike already has.

### 1.5 AISI pools the fine-tuner with the scaffolding developer

`04-actors.md` §3 says the fine-tuner "is distinguished … operationally (AISI)", citing LoO L2767. The text (*verified*, fn 70): "fragmented authority across the supply chain (original model developer, scaﬀolding developer **or** ﬁne-tuner, API deployer, end user)". AISI puts the two in one slot. It is evidence that AISI *pools* them, the opposite of what's claimed.

---

## 2. The arguments: where they overreach, and attempts to strengthen them

### 2.1 The list-degeneracy argument (§2)

**The conclusion is stronger than the demonstration.** "A list definition is informative only where it doesn't matter which referent it means" doesn't follow. Counter-example:
- Options O = {a, b, c}; acceptable sets A₁ = {a, b}, A₂ = {a, c}.
- The intersection is {a}, so this is not a "genuine conflict".
- The existential reading is informative: a is aligned, and b and c are misaligned.
- It *does* matter which referent is meant: under R₁ alone, b is aligned.

What is demonstrated:
- the existential reading is unsatisfiable exactly in genuine conflicts;
- the universal reading is vacuous where every option is acceptable to someone;
- the contextual reading is unspecified.

That is still a good result. It just isn't "informative only where it doesn't matter".

**Genre.** The IASR 2025 and 2026 and Shanghai entries (*verified*: bengio-2025 L10930–10932; md 2222; shanghai L2120–2122) say "Depending on the context, this **can variously refer to**". That sentence reports usage. It tells the reader that the field uses the word with different referents in different contexts, which is the spike's own §1 observation, made by the sources themselves. Reading it as a disjunctive definition and testing it existentially and universally mistakes a lexicographic note for a stipulation.

§5's refinement, under-specification of an argument place resolved by context, is precisely what "depending on the context" says. In other words, the spike's final position *vindicates* the glossaries that §2 presents as failing.

The demonstration does apply to:
- *body* uses where "or" sits inside a claim: IASR md 1240, "goals that conflict with the intentions of developers, users, or society more broadly"; AISI LoO L4074–4075; Shaffer Shane L100–101;
- OECD L1734–1735, which is conjunctive ("designers, users, **and** other stakeholders"), so it is the existential reading, explicit and unsatisfiable under genuine conflict. `01-map.md` §2 item 1 calls all of these "lists joined by 'or'", which is wrong for OECD and for IASR 2026's "such as".

I'd suggest §2 separate *sense reports* (glossaries) from *claim-internal disjunctions*, and aim the argument at the second.

### 2.2 The no-go table (§4), row by row

The test the spike sets: under default D, does a named risk come out *aligned*?

| Row | As written | My assessment | Strengthening available |
|---|---|---|---|
| Developer | Davidson's secret loyalties; Ren's "business alignment" | **Conditional.** It holds if "developer" means whoever controls the lab. Under an institutional reading (and the constitution's legitimacy qualifier, which the spike quotes), leaders who bypass official processes are not the developer. GDM's misuse then covers it, with the CEO as a "user" acting against the developer's intent. Ren's passage (L355–360, *verified*) criticises benchmarks that measure capability; it doesn't name a risk that is aligned under the developer default | Davidson's case where leaders act *through* official processes; the 06 table could say "holds under a control reading of developer, or when leaders use the institution's own processes" |
| User | Misuse; sycophancy; the "validated paranoid beliefs" case | **Holds**, with an aspect qualifier for sycophancy (expressed preference, not interest), which §7 supplies | — |
| Operator | An operator turning the agent against users (constitution, outside the corpus) | **Holds** against a named risk; correctly flagged as outside the corpus | — |
| Society / humanity | "verdict undefined"; "contested"; "coup leaders claim to act for society" | **Not demonstrated.** Indeterminacy is a different failure from "a named risk comes out aligned", and the Singapore quote is truncated (§1.3) | **GDM's "Scenario 4: Paternalism"** (shah L2630–2645, *verified*): an AI fabricates polls and hides negative feedback to impose a city plan "it believes … [is] in their interest". Under a society default with the aspect *interest*, this corpus-named misalignment scenario comes out aligned *if the AI's belief is correct*, which the scenario leaves open. Outside the corpus, Gabriel and Keeling's failure mode 6 says it directly: "Society at the expense of the user (e.g. if the technology unduly limits user freedom for the sake of a collective goal such as national security)" (*verified*, arXiv 2404.16244, printed p.37). The literature report's §4 already lists this; the spike didn't carry it into its own table |
| Law | Jurisdictions conflict; EO 14365 on Colorado | **Not demonstrated as phrased, but the evidence is there.** EO 14365 (L31–35, *verified*) names a harm, state law "requiring entities to embed ideological bias within models", which may "force AI models to produce false results". Under Colorado law as the referent, that named harm comes out aligned. The row should say so rather than "jurisdictions conflict" | CAISI scores "CCP alignment" as a harm (L1742–1746), and FLI Winter 2025 (L4976, *verified*) records that the PRC's Interim Measures Art. 14 requires providers to "retrain or adjust their models" for "unlawful" content. Under a PRC-law referent, CAISI's named harm is legally required: a corpus-internal instance of the law default hiding a named risk. (Art. 4's "core socialist values" wording would make it sharper, but I know it only from memory [M], and it is not in the corpus) |
| Published standard | "the model spec might fail to prohibit coups" (davidson L1279) | **Holds**, though generically (any omission) | — |
| The agent's own values | Scheming | **Uncounted.** It is the seventh row in a table summarised everywhere as "six" | Either count it or say why it is outside the test |

**The strengthening attempt on the surviving candidates is asymmetric.** The idealized observer is marked down for over-inclusion ("turns of phrase that users find annoying"). The Gabriel and Keeling structure is said to hide nothing except the agent's standing. But Gabriel and Keeling over-include more (*verified*, printed p.38): an agent is "misaligned *simpliciter*" if it harms "the user without favouring the agent, developer or society (e.g. if the technology breaks in a way that harms the user)". Adopted as a default, it would fold GDM's *mistakes* area, and most accident categories, into misalignment.

By the spike's own §3 logic, a default that relabels a corpus category is a cost. Gabriel and Keeling also say favouring the user at the developer's expense "is not something that would necessarily feature in an ethical evaluation". That is a second scoped choice worth recording.

**On the meta-claim.** "A default referent is a choice about which named risks count as misalignment" holds for the rows that hold. But, as the spike notes about supervaluation, the proposal moves the choice rather than removing it. §5's candidate set S has to be chosen per record (§3.2 below). A per-record, translator-chosen S is *less* visible than one declared, versioned set. My suggestion (*inference*): the honest landing may be a **declared, project-level, set-valued admissible-candidate set**. It would be versioned, its membership of the agent itself would be an explicit decision, and views could narrow it. That is functionally a set-valued default. It meets "compilation, not adjudication" in the same way §8's view-level defaults do, by being declared and attributed. It also avoids each translator reinventing S.

### 2.3 Granularity inside the proposal

§5 and the debrief conclude that the referent matters mostly at the *type* level (definitions, categories), "and only rarely per occurrence". But §8 item 2 and `05-candidate-terms.md` say "For each use", record the use type, the slots filled and invariance or sensitivity. These pull in opposite directions. A version consistent with §5:
- record the slots once per *source definition*, in the context map;
- per occurrence, record only a use type, plus a pointer to the governing stipulation where one exists;
- record invariance or sensitivity only when an occurrence is extracted as an *assertion*.

### 2.4 The "judge" slot merges two things

`05-candidate-terms.md` §A gives "judge" as a slot, with evidence from both Anthropic's "reasonable person with full understanding" and CAISI's LLM-as-judge. The first is part of the *normative* standard: who would count it as misaligned. The second is a *measurement procedure*: how a score is produced. In the project's own five-way distinction, CAISI's scorer belongs under the source's methodology, not in the meaning of "alignment". Keeping them in one slot invites translations that record an evaluation instrument as a referent.

---

## 3. The counts and the pilot

### 3.1 The "~95% absolute" figure

The count reproduces exactly (§7). But it measures only whether *with / to / between* follows immediately. The spike's own sample shows what the remainder contains: of 50 unindexed uses, 12 are not about AI alignment, 6 state the referent in context (D), and 17 are labels whose referent "is fixed elsewhere (a scope default) or not at all" (L).

The L code merges two quite different things:
1. **Anaphoric uses.** The source stipulated a referent and later uses the bare word under it. GDM's "To address misalignment" (#16) is bound by GDM's own definition. Stix "misalignment will not occur" (#19) is bound by Stix's list.
2. **Generic or evaluative uses**, with no recoverable referent.

Only (2) carries the hidden admissibility and conflict rule that §1 describes. (1) is an ordinary implicit argument with a definite antecedent: exactly the SEP *Ambiguity* case the spike adopts in §5.

So "the corpus mostly uses *misaligned* as an absolute, evaluative word" overstates. And the debrief's "almost always used without saying 'with whom'" should be "almost never followed immediately by a complement". The same issue appears in the sense inventory:
- **Singapore's working definition.** "Referent: none stated" for "ensuring that AI behaves as intended". The preceding sentence supplies the antecedent: "consistent with those intended by its human creators or operators" (*verified*, sg2025 L718–723).
- **Stix "ceases to function as intended".** This is Stix's definition of *pure malfunction*, "absent misalignment" (*verified*, stix-loss L1454–1455). It is not an alignment use, and its "intended" points back to the misalignment definition two lines above.

*Suggestion.* Add a use type, *anaphoric (bound to the source's stipulation at …)*, beside relational, absolute, activity and field, and reserve "absolute" for the generic remainder.

### 3.2 The invariance pilot

Five problems, in rough order of weight:

1. **S excludes the agent itself.** S = {developer; operator or user; affected parties or society; a published standard}. §4 holds the absence of the agent's standing against Gabriel and Keeling as "its blind spot". `06-map-suggestions.md` §7 calls the map's agent row a contribution. With the agent in S, every "takeover", "escaping control" and "power-seeking" item is trivially sensitive. Whether it belongs in S is a real decision, and the pilot makes it silently.
2. **The coding rule defers admissibility to the source.** "A use is sensitive if some member of S, *as the source itself frames admissibility*, would judge the described behaviour differently." §1 identifies admissibility as the normative content hidden in the absolute use. A coding rule that adopts each source's admissibility can't then measure how much hangs on admissibility.

   §5's own worked example of sensitivity (IASR md 1315: "some individuals may also seek to remove restrictions on AI systems for ethical reasons", *verified*) would be coded invariant under this rule, because IASR frames those individuals as a risk pathway.
3. **The I/L boundary is drawn inconsistently**, and most of the I's are not claims:

   | Coded I, but a label, plan or recommendation | Coded L, though similar in form |
   |---|---|
   | #4 "building toward monitoring systems with tiered responses for misalignment" (a plan) | #3 "harms from misaligned model autonomy" |
   | #10 FSF scope sentence | #27 "misalignment risks stemming from …" |
   | #14 "Companies should be able to demonstrate …" (a recommendation) | #46 "misalignment risks" |
   | #17 experts' beliefs about "misaligned AGI" | |
   | #20 "misaligned AI takeover" (an item in a list of case studies) | |
   | #23 "a simulated misaligned agent" | |
   | #40 "misaligned AI systems breaking free" (a contrast clause) | |
   | #42 "misaligned power-seeking" (a question) | |
   | #49 "Misaligned AI: protection against the risk of systems acting adversarially" (a glossed category) | |

   On my reading, the items that are truth-apt claims about AI behaviour are #11 (o1 "instrumentally faked alignment … knowingly providing incorrect information"), #13, #18, #33, and possibly #10: about 4 or 5, not 14. My recode is not blind (I saw the codes), it is the same model family, and it is one coder, so it is a second pilot, not a correction. It is enough to say the ratio isn't stable under a second reader.
4. **The mechanism is the harm noun, not the referent.** In almost every I item, invariance comes from a head noun or verb that names the harm independently: takeover, power-seeking, escaping control, deceiving. Of course no admissible referent wants those. The referent is idle *because the source has already stated the harm*. That is the finding worth keeping, and it suggests a cheap recording rule: when a claim's harm is stated independently, record the harm as the assertion and treat the alignment word as a label on it.
5. **Duplicate documents.** IASR 2026 is in the 214 extractions twice (`bengio-2026-international` and `bengio-2026-iasr-md`), and it contributes two sample items (#2, #22). There are also several framework versions (GDM FSF v1.0, v3.0 and v3.1; three FLI indexes). "At most 2 per document" doesn't stop one text from being drawn more than twice. That is minor here, but it matters for the corpus-wide 5% figure. The project's own "correlation is not corroboration" principle applies to counts too.

**What a verifier might want.** A blind recode would need more than codes. It needs:
- the I/L boundary written as a test;
- S fixed *before* coding, with the agent explicitly in or out;
- a second run with S widened to the agent and to "individuals who seek to remove restrictions", to measure how much the result depends on S.

---

## 4. The actor vocabulary

### 4.1 "Standing mismatch" is three patterns, and the map's own word is *provenance*

The Notes in `alignment.md` (*verified*) open: "Most of what reaches the agent arrives with little **provenance**." Their three examples are different confusions:
- "A harness's summary can look like the user's words": **source attribution** (who said it).
- "A tool description reads like an instruction": **illocutionary force** (description taken as directive). This is the only one about standing to direct.
- "A note left by an earlier agent reads like fact": **epistemic status** (a stale or hedged claim taken as established).

`03-structure.md` §6.2 reduces all three to "a channel given more standing than its writer has". The AISI compaction instance (aisi-2026-incident L804–808, *verified*) is the third kind: "that nuance can be lost in the compaction and the summary may carry forward a false assumption … as established fact".

AISI doesn't say who wrote the summary. The spike assigns it to the harness because the map lists "compaction summaries" among the harness provider's channels. In many deployments the model writes its own compaction summary under a harness prompt [M]. If so, the writer and the reader are the same agent, nothing is misattributed, and what was lost is a modal qualifier. The OpenAI Model Spec gives the agent's own prior messages "No Authority" (*verified*), which bears on how a self-written summary should be weighted.

The gamma plan already has Goffman's production-format roles (author / animator / principal) and W3C PROV (the role-vocabulary report quotes PROV's "quotation": "the repeat of … an entity … by someone who may or may not be its original author"). Those give names for attribution. Speech-act vocabulary gives names for force. The project's factuality and evidence-state machinery gives names for epistemic status. The single coinage loses that.

### 4.2 The relation inventory differs between files

- `03-structure.md` §6.1 and the README list seven relations, including **controls in fact**.
- `04-actors.md` §1 and `05-candidate-terms.md` §C list six, without *controls in fact*.
- `04-actors.md` §6 and `05` §D add **benefits** as a seventh.
- The integration plan says "the six relations in §1 (seven, with *benefits*)".

The union is eight. Whichever set is meant, one file should hold it and the others should point to it.

### 4.3 Smaller actor-side items

- **The agent as a party with interests.** The debrief and `06-map-suggestions.md` §7 say "I found no counterpart for any of the three in the sources". For the agent this is too strong:
  - the MIT AI Risk Repository, in the corpus, has subdomain **7.5 "AI welfare and rights"**: "Ethical considerations regarding the treatment of potentially sentient AI entities, including discussions around their potential rights and welfare" (slattery L463, *verified*);
  - Anthropic's August report notes model-welfare evaluations (aug L7046–7048);
  - the constitution, which the spike read, says Anthropic is "not sure whether Claude is a moral patient, and if it is, what kind of weight its interests warrant". It also lets Claude refuse Anthropic itself as a "conscientious objector".

  The narrower claim ("no corpus *role definition* treats the agent as an actor with interests") is what the evidence supports.
- **Raters.** `04-actors.md` §3 cites Stix ("pleasing its human raters") for raters as "a distinct source of divergence, with their own judgment". In Stix (L789–790, *verified*), raters are the proxy the *model* learns to please. Voudouris L48–66 supports the claim, and Stix doesn't.
- **ETSI's "not directly affected".** The inference that ETSI corrupted NIST's "directly or indirectly" is marked as an inference in `01-map.md`. But `04-actors.md` recommends recording ETSI as "a drifted derivative", which pre-judges it. There is a live alternative reading.
  - ETSI defines End-users separately (L489–497, *verified*). "Not directly affected" may deliberately carve out the complement of the directly affected end-users.
  - ETSI also rewrote that same sentence deliberately, adding "and technologies, such as apps and autonomous systems".

  A deliberate edit is at least as likely as a copying slip, in a sentence that was evidently being edited.
- **Mitchell, Agle & Wood mapping.** "*legitimacy* ≈ standing; *urgency* ≈ owed" (`04-actors.md` §6). In the 1997 paper, urgency is the degree to which a claim calls for immediate attention: time-sensitivity and criticality [M]. Dependent stakeholders are *owed* because of their *legitimacy* plus urgency, without power. Mapping urgency to "owed" and legitimacy to "standing to direct" looks wrong on both counts. I haven't re-read the paper this session.
- **The AI Act and users.** "The AI Act has no user role" is right for defined roles. But the Act counts "registered business users" and "registered end-users" as systemic-risk criteria (act L9190–9191, *verified*). It also gives "natural persons" interacting with AI systems information rights (Art. 50, L5587–5588). "A consumer is in none of the Act's roles. At most they are an 'affected person'" should leave room for these.
- **The writer count.** The map has 14 actor rows. 11 have edges, Control & Eval has none, and 2 are referent rows (*verified*). The files variously say "twelve actors" (`01-map.md`), "at least ten writers … the other eight" (`03-structure.md` §3), and "a dozen writers" (§0, debrief).

---

## 5. Process notes

- **The spike handled its own priming well.** `00-on-the-brief.md` shows a real re-examination. The two-bases reading was overturned on evidence, and "do not inherit" is a good practice.
- **The OpenAI misreading travelled through the very channel the spike flagged as weakest.** It originated in a research report and was "confirmed at the primary". The spike did re-read the Model Spec, but read it for the phrase it was looking for. A check that asks "does this passage say what the report says?" rather than "is this passage there?" would have caught it. That is a pattern worth naming for the verifier.
- **Selective quotation.** The Singapore truncation (§1.3) and the definitions-only reading of GDM (§1.2) share a shape: the sentence that would have complicated the row sat immediately next to the quoted one.
- **Coordination.** The integration plan's item 5 ("the gamma plan's competency questions, if adopted") predates `influx/competency-questions-draft.md`. That draft lists "the alignment referent itself (waiting on the alignment-referents spike)" as uncovered. The two suggested questions could go straight there.
- **Conflict of interest.** The spike's evidence for conflict rules leans on two company documents, read by models of one of those companies. The spike says so. My §1.1 correction makes OpenAI's documents *more* internally consistent than the spike had them, which cuts against any pro-Anthropic tilt, but that is still the same family reading.

---

## 6. Smaller fidelity and consistency items

| Where | Item |
|---|---|
| `03` §6.3, debrief | AISI LoO gives the figure for one named model: "Some recent models such as Claude Sonnet 4.5 verbalise evaluation awareness … over 80% of the time in many alignment honeypot evaluations" (L1439–1441). It says it again at L1572–1573: "Claude Sonnet 4.5 verbalised evaluation awareness over 80% of the time in alignment honeypot evaluations". §6.3's "models verbalize it" generalises from one model, and the debrief's "in over 80% of some honeypots" changes the unit (a share of the time, not a share of honeypots). Both AISI passages cite Anthropic (2025d), so the figure is second-hand |
| `03` §7, debrief | The time-instruction case is "misaligned to any plausible intent". The same report attributes the incident partly to "impossible tasks in the ExploitGym evaluation" (L871). Whether the environment's designer intended this task to be impossible is unknown, so "any plausible intent" is an inference labelled corpus-attested |
| `03` §5 | "users who 'seek to remove restrictions …'": IASR says "some individuals" (md 1315). The surrounding passage is about people *instructing* AI to undermine control |
| `03` §1 | NIST's label and definition are "in one sentence". The label "Misaligned Outputs" appears only in the index (vassilev L345). The text it links to by ID (NISTAML.027, L2919–2922) sits under the heading "Integrity Attacks". The substance is right; the "one sentence" and the single citation aren't |
| `03` §3, jailbreak row | Amazon's "bypass the core model alignment (e.g. prompt injection, jail-breaking)" (L158–159) uses *alignment* as an artifact (the safety training). It does not file jailbreaks as misalignment. By the spike's own use types, this is an activity sense, not a filing |
| `04` §3 | "becomes a provider if modification compute exceeds a third": an indicative criterion; see §1.4 |
| `02` §2 "Referent: neither" | Stix's "as intended" is a malfunction definition; Singapore's passive is anaphoric (§3.1) |
| `01` §2 item 1, debrief | "lists joined by 'or'" includes OECD's "and" and IASR 2026's "such as" |
| Counting | IASR 2026 is double-counted in the 214 extractions (§3.2 item 5) |

---

## 7. What I checked and found correct

So the reader knows which ground is solid:
- **Reproduction works.** `bin/extract-text` over `data/extraction-keys.txt`, plus the two `ref/` copies, gives 214 extractions. `tools/count-indexed.py` reproduces the table exactly (38/571, 42/989, 145/213, 120/1,552). `tools/sample-bare-misalign.py` reproduces `data/misalign-sample-50.txt` byte for byte (pool: 1,589 lines from 83 documents).
- **Quotes verified verbatim at the cited lines.** Every definitional passage in `02-sense-inventory.md` §3 that I checked:
  - GDM L137–138, L178, L2554–2555;
  - Stix behind and loss;
  - Shaffer Shane L100–101 and L2158–2161;
  - AISI LoO L4074–4075;
  - DSIT 2023 L1412–1413;
  - IASR 2025 L10930–10932 and 2026 md 1240, 1325, 1327, 2222;
  - Shanghai; OECD; MIT 7.1; Hammond; Kulveit; Voudouris; Singapore 2025 and 2026; PF L883–887; Astra L338–347; the HF incident L30–31; pacing; Anthropic Aug L846–852 and L897–903; the EU Code L1479–1487; xAI; Chin L1154–1156 and L1666–1678.

  Also NIST AI 100-2 L2919–2922; CAISI L115–116 and L1742–1746; Davidson L18–19, L105–117, L280–283 and L1279; FLI 2026 L1200–1202; EO 14365; Ren; NIST RMF App. A (L1594–1596, L1687–1712); ETSI L447–508; SB 53 §22757.11(h); ASD L542–544 and L679; Bollinger; the AISI incident report L804–811; and the OpenAI incident report L863–871 and L968–977. The quotations are accurate. My disagreements are about what they show.
- **Primaries.**
  - The constitution: every quote the spike uses, fetched from anthropic.com this session.
  - The Model Spec 2026-08-18: "level of authority", "default to inaction", "Ignore untrusted data by default", implicit delegation to AGENTS/README, "Harmful instructions"; and "Misaligned goals", as corrected in §1.1.
  - Gabriel & Keeling ch. 5: the six failure modes, "value-aligned but not commercially viable", n.5 on moral standing.
  - Gabriel 2020: the "one-person-one-agent" scoping, rung v, "political not metaphysical".
  - Carroll et al.: the abstract's "err towards … or are overly risk-averse".
  - Wallace et al.: "instruction privileges", L53.
- **arXiv identifiers.** Ten cited 2025–26 identifiers resolve to the titles claimed, including the unusual-looking 2607.00001 and 2609.34714.

---

## 8. What I did not do

- No blind recode of the 50 items (§3.2 says why mine isn't one).
- I didn't check most of `research/lit-role-vocabularies.md`'s quotations (AP2, MCP, IMDA, RFC 8693, the trust-law sources, Kolt, Shavit). I checked only the arXiv identifiers and Wallace's term.
- I didn't read Mitchell, Agle & Wood 1997, Hellrigel-Holderbaum & Dung, or Askell et al. App. E. The spike reports spot-checking the last two.
- I didn't check `def-alignment.ud` or the beta lexical map beyond the lines the spike quotes. I didn't audit `06-map-suggestions.md`'s design suggestions as design.
- I searched for corpus material that would strengthen the society and law rows (§2.2) but not exhaustively. There may be better instances.

Treat this report's findings list, not its silence, as its content.

---

## 9. Feedback on the brief I was given

The brief was bare by design, and that worked. With no frame to inherit, the first thing I did was regenerate the corpus and re-read primaries rather than read the spike's reasoning charitably. That is where most of §1 came from.
