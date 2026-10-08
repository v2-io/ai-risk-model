# notation/: the SB 53 slice, written in the namespaced notation

*For Joseph. A trial of the notation you sketched on 2026-10-07: source-namespaced terms, descriptive terms of our own, explicit ambiguity, and set-valued relations. The coordinator elaborated it, and this applies it to the thin pass's SB 53 slice. Claude (Opus 5.5), 2026-10-07. **Disposable**, like everything in `influx/thin-pass/`. Nothing here is adopted into `def/`.*

## Read in this order

1. **`oai.ud`**: OpenAI's "severe harm", the slice's one decisive ambiguity. Your sketch line is re-expressed in its discussion.
2. **`sb53.ud`**: SB 53's two scopes, its catastrophic-risk and critical-safety-incident entries, and its resolution records.
3. **`notes.md`**: where the notation fit, where it strained, what it couldn't say, and what it suggests for proposed change 2.
4. The rest as reference:
   - `arm.ud` (our terms);
   - `ant.ud` (FCF v2, RSP v3.4);
   - `ny-raise.ud`;
   - `xai.ud`;
   - `eu-act.ud`.

## The marks, as used here

| Mark | Means | Example |
|---|---|---|
| `ns:term` | a source's word, in that source's namespace | `oai-pf:severe-harm` |
| `ns.scope:term` | the *source* mints the same word in two scopes | `sb53.bp:catastrophic-risk`, `sb53.lab:catastrophic-risk` |
| `ns:term#sense` | a sense *we* distinguish in a word the source leaves unbound (ours, attributed) | `oai-fgf:severe-harm#own` |
| `arm:name` | our term, named by its distinguishing feature, never by a judgment word | `arm:harm.over-50-deaths-one-incident` |
| `arm:facet=value` | a value of one of our facets | `arm:materiality=importance` |
| `{a \| b}` | one of these is meant; undetermined (ambiguity) | `{@{oai-fgf:severe-harm#own} \| @{oai-pf:severe-harm}}` |
| `{a, b}` | a set: all of these, as members or targets | `:contains {@{…}, @{…}}` |
| `?` | unresolved; inside a set, further unnamed members | `-> ca-law:foreseeable ?` |
| `-> ns:term` | the path goes into another namespace (an import or incorporation); with `?`, not followed | `-> ca-law:materially-contribute ?` |
| `lean x` | our preference among candidates, attributed to us; the candidates stay | `lean #own, low-moderate` |

A source's own "and"/"or"/"not" goes in the **relation name**, never in a mark: `:requires-all`, `:requires-any`, `:outcome-any`, `:excludes-any`. So `{a | b}` always means *we don't know which*, never *either will do*.

## Relations used

- **Structural:**
  - `:contains` (with the entry's `:closure open | closed`);
  - `:is-a`;
  - `:broader`, `:narrower`, `:exact` (SKOS direction: the entry is the subject);
  - `:not-to-be-confused-with`.
- **Domain:** `:materializes`, `:evidences-increase-in` (an occurrence to a risk), `:outcome-any`, `:bearer`, `:contribution`, `:knowledge`, `:materiality`, `:model-conduct-any`, `:excludes-any`.
- **Lineage:** `:copies`, `:quotes`, `:restates`, `:shares-template-with`.

`notes.md` §2–3 records where these strained: ambiguity over a relation itself, inheritance, who asserts a relation, and time.

## Ties to the thin pass

Every entry's `:source` gives the passage ids (`P-…`) in `../records/passages.yaml`. Every resolution line starts with its record id (`R-…`) in `../records/resolutions.yaml`, and all 22 records appear. The thin pass's computed results (`../answer.md`) are cited, not recomputed: the notation is declarative, and evaluating it would need an interpreter (`notes.md` §3).

The files follow the `def/` house style (udon term groups, `|rels`, `|discussion`) by eye. The built udon parser (pre-0.8) warns on the existing `def/` files too, so it couldn't be used to validate these.
