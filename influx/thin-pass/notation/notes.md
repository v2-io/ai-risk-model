# Notes on the notation trial: fit, strain, and what it couldn't say

*Claude (Opus 5.5), 2026-10-07, for Joseph. This rewrites the thin pass's SB 53 slice in the notation you sketched this evening, as the coordinator elaborated it. Disposable. All 22 of the thin pass's resolution records and all its frames are carried, as 43 entries (19 of ours in `arm:`, 24 in ten source namespaces, one with two scopes) and 25 resolution lines, in seven files. Every judgment here is one reader's; the coordinator's elaborations were proposals, and I changed several where the material pushed back.*

## 0. The short version

- **It works.** It carries the precise terms, and it keeps sources' words, our concepts and ambiguity visibly apart. The slice's hard case, OpenAI's "severe harm", becomes legible in five lines (`oai.ud`), where the thin pass needed a frame, a resolution record and a footnote.
- **Writing it found an error** that the thin pass and its verifier both made. The FCF's crime list doesn't "drop murder"; it widens a closed list of four into an open class, "serious crimes (such as …)". Naming the class and its closure made that visible. The thin-pass files are corrected.
- **Your sketch line survives in shape and loses two equalities.** The material corrects both: PF's severe harm *contains* two classes, one a dollar class; the FGF's is *open*, so 50 deaths is a member, not the whole (`oai.ud`, discussion).
- **The ambiguity mark had to work on four kinds of thing,** not one:
  - a use's referent (the expected case);
  - an attribute value (`:closure {open | closed}`);
  - a relation (`:{exact | narrower}`);
  - a whole member set.

  It held each time. The syntax got heavy in the last two.
- **Logic, sets and ambiguity are three different things.** A source's own "or" is not ambiguity. I kept source logic out of the marks entirely, in relation names (`:requires-all`, `:outcome-any`, `:excludes-any`). That kept `{a | b}` meaning only "one of these is meant; we don't know which".
- **For proposed change 2, my recommendation is "both, divided".** A source's precise definition lives *in the lexicon, under its own namespace*. `arm:` holds the points where sources meet. The translation layer shrinks to resolution records. (§5)

## 1. Where it fit

**Source namespaces.** Every source term sits as an entry beside its neighbours, and nothing collides:
- `sb53.bp:catastrophic-risk`, `sb53.lab:catastrophic-risk`, `ny-raise:catastrophic-risk`, `ant-rsp:catastrophic-risk`;
- `oai-pf:severe-harm`, `oai-fgf:severe-harm#own`.

This is the layout you asked for ("lay out openai:severe-harm and namespace nearby terms that are similar to but not identical"). Two cases show why it pays:
- SB 53's "foreseeable" (`-> ca-law:foreseeable ?`) and the AI Act's "reasonably foreseeable" (`-> eu-law:reasonably-foreseeable ?`) stay apart without anyone resolving either.
- SB 53's term minted in two chapters gets two entries, and its findings' unscoped use of the word resolves to `{bp | lab | ordinary}`. That is address theory's origin-relative resolution, readable at a glance.

**Two kinds of split, two marks.** The coordinator's proposal used `#` for "a sense". The material has two different things that need marking:
- **`ns.scope:term`, where the source mints the same word twice** (SB 53's two chapters). The source made the split.
- **`ns:term#sense`, where *we* distinguish a sense in a word the source leaves unbound** (`oai-fgf:severe-harm#own`, `ant-fcf:systemic-risk#sentence`). The split is ours and attributed to us.

A sense that is another source's binding doesn't get a `#` name at all; the candidate is that binding itself (`{@{oai-fgf:severe-harm#own} | @{oai-pf:severe-harm}}`). That kept the FGF/PF case honest: the PF sense is the PF's term, imported, not our paraphrase of it.

**Descriptive `arm:` names.** "Name by the distinguishing feature, not the judgment word" had a real effect. Once the PF's term had to be written as `:contains {thousands dead or gravely injured, hundreds of billions economic}`, it was plainly not equal to a casualty class. The judgment words ("catastrophic", "severe", "systemic") now appear only in source namespaces.

**`:contains` with closure, and what closure buys.** Closure is what turns *absence of a path* into *no*. Asking the entries the ex-ante form of Q1, "which source terms reach `arm:harm.over-50-deaths-one-incident`?", gives this (by hand, from the entries):

| Entry | Reaches it? | Why, from the rels |
|---|---|---|
| `sb53.bp:catastrophic-risk` | yes, on its other conditions | `:outcome-any` → either pooling reading → contains it |
| `sb53.lab:catastrophic-risk` | yes, likewise | `:broader` than bp |
| `ny-raise:catastrophic-risk` | yes, likewise | `:copies`; `{exact \| narrower}` doesn't change the outcome side |
| `xai-faif25:catastrophic-risk` | yes, as of 2025-12-30 | `:exact` bp |
| `ant-fcf:systemic-risk` | yes | contains bp; and `#sentence`'s example |
| `oai-fgf:systemic-risk` | yes | contains bp (both closure readings) |
| `oai-fgf:severe-harm#own` | yes | contains it |
| `oai-pf:severe-harm` | **no** | closed, and neither member contains it |
| `ant-fcf:large-scale-harm` (40 deaths, say) | **?** | open, so no path is not a no |
| `ant-rsp:catastrophic-risk` | **?** | deliberately unbound |
| `eu-act:systemic-risk` | **?** | no harm relation; its conditions are of another kind |
| `xai-rmf:catastrophic-malicious-use-events` | (can't say) | its bar is quoted text, not a relation (§2) |

This table is the thin pass's ex-ante answer, with no evaluator. The notation carries enough for the lookup to be mechanical.

**Delegation and "unresolved".**
- `-> ns:term ?` read cleanly as "the path goes into another namespace, and we didn't follow it". It kept the thin pass's *delegated* status distinct from *ambiguous*, which was the MIT "Other" lesson.
- `-> @{sb53.bp:…}` with no `?` is a followed import (xAI's incorporation).

## 2. Where it strained

1. **Ambiguity in four places.**

   | Where the ambiguity sits | Example |
   |---|---|
   | a referent | `=> {a \| b}` |
   | an attribute value | `:closure {open \| closed}` |
   | a relation | `:{exact \| narrower} @{sb53.bp:catastrophic-risk}`; `:{materializes-whole \| materializes-whole-or-part}` |
   | a whole set | `:contains {{a, b} \| {a, b, c}}` |

   One mark serves all four, which I'd keep. But a braced relation key is new syntax, and an ambiguity between two sets is hard to read. A set's membership that depends on another ambiguity (the umbrella's closure) has no lighter form that I found.
2. **Source logic versus our ambiguity.** SB 53's "or" in its conduct list, the AI Act's "due to … or due to …" and SB 53's "any of the following" are the sources' disjunctions. Putting them in relation names (`-any`, `-all`, `:excludes-any`) worked. It strained once: SB 53's pooling ambiguity has a candidate that is itself a disjunction (more than 50 dead *or* more than 50 injured). With no inline any-of inside an ambiguity, that reading needed its own named class, `arm:harm.over-50-dead-or-over-50-seriously-injured-one-incident`. Inline `any-of(…)` / `all-of(…)` would avoid inventing names for readings.
3. **Brackets, in udon.**
   - Braces already mean reference (`@{…}`) and cardinality (`{0,N}`), and the proposal adds sets (`{a, b}`) and ambiguity (`{a | b}`).
   - `def-resolution.ud` already writes `(@{admissibility} | @{preference})` in a `|rels` target, where `|` means a *type union* (the range admits either), not ambiguity.

   Readable by eye, fragile for a parser. One option is udon's own list brackets for sets (`[a b]`, as `:synonyms [x]` already does), `{a | b}` only for ambiguity, and parentheses never. The other is keywords: `one-of(a, b)` for ambiguity, `all-of`, `any-of`.

   Separately, the built udon parser (`udon/core`, pre-0.8) emits warnings on the existing `def/` files too, so I couldn't use it to validate these. They follow the house style by eye only.
4. **`?` does two jobs.** It means "unresolved" in a resolution, and "further unnamed members" in an open set (`:contains {…, ?}`). Both readings are natural. A separate mark for the second (`…`) would make the open set's tail distinct from an unresolved referent.
5. **`.` does two jobs.**
   - Before the colon it nests scopes (`sb53.bp:`).
   - After it, it sub-classes (`arm:harm.over-50-…`).
   - Facet values needed a third form (`arm:materiality=importance`).

   Position keeps them apart, but it is a lot for one character to carry.
6. **Descriptive names grow with every delimiting characteristic.** `arm:harm.over-50-dead-or-seriously-injured-one-incident` is at the edge of usable. The comparisons were done by the *numbers in the names*, not the names. The xAI RMF's bar (>100 deaths, no counting unit) is quoted text, so the Q1 lookup can't place it at all. **Better form:** harm classes carry facets (`:count deaths+serious-injuries :op > :n 50 :per incident`), and the descriptive name is a handle on that. Then a single-source bar like xAI's needs no name of its own, only facet values, and it still joins the lookup.
7. **Inheritance lives in prose.** "As @{sb53.bp:catastrophic-risk}, with 'foundation model' for 'frontier model'" appears three times (Labor Code, RAISE, the incident limbs). The thin pass's frames had `inherit` and `override`, and the notation needs them too: `:inherits @{…}` with `|overrides` rows.

## 3. What it couldn't say, except in prose

- **Who asserts a relation.** `ant-rsp:catastrophic-risk :not-to-be-confused-with sb53.bp:…` is Anthropic's statement. `oai-fgf:severe-harm#own :not-to-be-confused-with oai-pf:severe-harm` is ours. Every mapping relation is an assertion with an author (plan §3.7, after the micropublications model), so rows need a `:by` or a trailing attribution. I used comments.
- **Time.** The notation has no place for:
  - "in force from 2025-12-30, end undetermined" (xAI);
  - the moment a source's test is evaluated at (foreseeability is judged as of the conduct);
  - versions inside a namespace.

  I versioned by name (`xai-faif25:`, `xai-faif26:`) and left the FCF's v1/v2 unmarked. A namespace probably wants a `@version` part, and entries an `:in-force` attribute.
- **Namespaces for relation keys.** `:materializes` is defined as `arm:materializes` but used bare, as udon uses `:is-a`. That's fine while only `arm:` defines relations. It needs a rule if sources' own relations (the FCF's "AI Event → AI Incident" ladder) are ever carried.
- **Coverage, as against meaning.** RAISE's §1425 limits where the act applies, not what its terms mean. I put it on a `|namespace[ny-raise]` element. That works, but it's a new element.
- **Evaluation.** The entries say everything the thin pass's frames said except how to compute. Evaluating them would need an interpreter for the relation vocabulary (`-all`, `-any`, `:excludes-any`, the ambiguity marks), which is the same evaluator in a new syntax. The Q1 lookup in §1 shows the relational half is queryable as written.

## 4. Your worry about open and closed as "grammatical pedantry"

The slice has evidence at two of the three levels the coordinator proposed, and none at the third.

- **In a definition, closure is not pedantry.** "Means" against "includes … including but not limited to" is the source's own drafting choice between a floor and an example, with legal effect. In the thin pass's variants it changed results: for 40 deaths, SB 53's closed bar says no, while both companies' own sentences stay open. It is a property of the entry (`:closure`), and the source's word sets it.
- **Counting turned up inside definitions, not only in claims.** The coordinator put quantification (pooling, counting units) in claim records. In this slice both counting findings are inside SB 53's *definition*:
  - whether deaths and injuries pool toward "more than 50 people";
  - which arms "a single incident" governs.

  They are delimiting characteristics, so they sit in the entry, as facets, with the same ambiguity mark (`:incident-phrase-attaches {both | property-only}`). So the same mark works at every level. What differs is where it sits.
- **In claims, it may well be pedantry.** "When a developer does xyz" is open or closed only if the answer depends on it. The slice has no such claims, so it can't test this. Leaving the default unmarked, and marking only where an answer changes, matches everything seen here.

## 5. What this suggests for proposed change 2

The thin pass asked where a source definition's precision should live: in translation-layer frames, or as lexicon concepts. This trial suggests a third arrangement that keeps the best of both:

- **The source's precise term is a lexicon entry in the source's namespace** (`sb53.bp:catastrophic-risk`), with its delimiting characteristics as `|rels`. This is your "union of the most precise, scoped, bounded definitions", without our lexicon adopting anyone's model: the namespace says whose it is.
- **`arm:` holds the meeting points:** concepts several sources share or that our thinking needs, named descriptively, with numbers carried as facets.
- **Translation shrinks to resolution records.** Each use of a source's word resolves to an entry, ours or a source's, or to `{a | b}` among them.

My confidence in this is moderate. It fits everything in this slice. But the slice is definitions-heavy, and the actor vocabulary (your `oai-pf:developer#api-provider` example) and claims haven't been tried. On that example: I'd write the sense with `#` rather than a second `:`, since `oai-pf:developer:api-provider` would read as a namespace `oai-pf:developer`. `-unknown-` is `?`. And `arm:developer:org-c:*` is a pattern over senses, which in address theory is a *match*, not a name. That is worth its own mark if it's needed.

## 6. Small things found on the way

- The FCF's "serious crimes (such as …)" correction (§0) is applied to the thin-pass files.
- Art. 3(65)'s "or" is about the *cause* of the market impact ("due to their reach, or due to … negative effects"), not two alternative impacts. My first draft of `eu-act.ud` got that wrong; it's fixed.
- `arm:` rules used here, for you to keep or drop:
  - a term exists only where two sources meet, or where our thinking needs one;
  - no judgment words in names;
  - our umbrellas contain only our terms.

  The second rule is the one that did the most work.
