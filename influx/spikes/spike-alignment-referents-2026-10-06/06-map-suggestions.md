# Suggestions for the "Aligned to whom?" map

*For Joseph, who is iterating on `alignment-model/alignment.md`. These are proposals with reasons. I have not edited the map. Each item points to the evidence in this spike, and each is offered for you to accept, change or drop.*

1. **Name two relations, not one.** The map's lines mean *writes into*, and the premise is about *to whom*. The literature and the developers' own documents keep apart:
   - *who writes into* the agent;
   - *whose instructions it should act on* (principals; the "chain of command");
   - *whose interests it should weigh* (third parties).

   A planted web page writes into the context but should direct nothing. An affected third party directs nothing and writes nothing, but is owed regard. (`03-structure.md` §6; `research/lit-alignment-relation.md` §5.1.)

   One low-ink way to show it: a column, *standing to direct*, with values such as *top* (the trainer's spec), *operator*, *user*, *delegated* (other agents, via an orchestrator), *none* (content, tools, the environment). The lines stay as they are. The column also separates the Notes' three confusions. Taking a tool description as an instruction is a confusion of *standing* (force). Taking a harness summary as the user's words is a confusion of *attribution*. Taking an earlier agent's note as fact is a confusion of *epistemic status*. The map's own word for all three, "provenance", is the right umbrella (`03-structure.md` §6.2).

2. **Consider extending the lead sentence.** The corpus supports a stronger version: "'Alignment' without saying to whom quietly picks one of them, *and how to settle it when they disagree*." The corpus's definitions name parties without a conflict rule. Its bodies discuss rules (refusal, the median view, voting), and the developers' documents state operative ones (`03-structure.md` §2).

3. **"Society, law, humanity" is three or four things.** The corpus separates:
   - the *general public* (NIST names it as an actor);
   - *the law*, which belongs to a jurisdiction. Jurisdictions conflict: one government's executive order says another's law forces models "to produce false results";
   - *norm authors* (standards bodies, civil society; NIST's "formal or quasi-formal norms or guidance").

   States also have a channel in: through mandated training content and through law (CAISI's "CCP alignment"; the US Action Plan). If one row is needed for space, keep it as an umbrella and footnote the split. (`04-actors.md`, the society row.)

4. **Split Control & Eval.** *Overseers* (monitors, approval gates) act on actions, as the map says. *Evaluators* also write into context, deliberately without marking it: "Evaluators can also edit or construct the model's context merely by editing text, for example in order to run an alignment honeypot" (AISI, *Loss of Oversight*). The evaluator then has a line into Context.

5. **Rows the references add** (first-pass, with evidence in `04-actors.md` §3):
   - **fine-tuner / downstream modifier**: writes into weights. In EU law it becomes a provider on a "significant change", with more than a third of the original training compute as an indicative criterion. AISI pools it with the scaffolding developer;
   - **human feedback providers** (raters, labellers): write into weights through reward, with their own judgment and biases;
   - **norm authors / the state**;
   - possibly **model hosts** (open-weight platforms), which were the harmed third party in the OpenAI–Hugging Face incident.

5a. **Two more candidates from the role-vocabulary report:**
   - **The counterparty**: the party the agent negotiates or transacts with for a principal. It is likely where "Agents embedded in applications" belongs, since that row is another principal's agent.
   - **Writers of authority**: identity providers, credential providers, verifiers. AP2's non-agentic "Trusted Surface" carries the user's consent past the agent's context. That is a deployed instance of "authority travels out of band", and possibly the best concrete example the floor could cite.

6. **The floor has one adversarial case worth stating.** "Generated is marked generated" conflicts with honeypot evaluation, which only works if the agent can't tell. AISI reports that evaluation awareness is already eroding honeypots. The floor might hold at the level of the regime (the agent is told that some contexts are evaluations) rather than per instance. That is a hypothesis, recorded in `03-structure.md` §6.3.

7. **Where the map is ahead of its sources, keep it marked as the map's own:**
   - the *inference provider* writing into ephemeral state and context: no corpus role is defined this way;
   - *the agent itself* as a party with interests: no corpus *role* definition treats it so, and the literature's most developed multi-party account assumes the agent has no moral standing. The corpus does raise AI welfare as a concern (MIT 7.5; Anthropic's model-welfare evaluations), so the map is ahead as a role, not as a concern;
   - *the user's lack of any obligation of truthfulness toward the agent*: no role definition I found says anything like it.

   These are contributions, not errors. The sources simply don't make these points.

8. **Words, if the map wants established ones:**
   - *end user* (NIST, ETSI) for The user;
   - *affected individuals and communities* (NIST) for Affected third parties;
   - *system operator* (ETSI), *scaffolding developer* (AISI), *operator* (Anthropic) and *developer* (OpenAI's Model Spec) all name the harness provider, and they collide. Keeping the map's own "application / harness provider" and listing these as synonyms is probably clearest.
