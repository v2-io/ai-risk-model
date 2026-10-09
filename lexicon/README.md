# lexicon

Builds `lexicon.html`, a readable lexicon page, from the udon term groups in `../def/`. New files in `def/` appear on the next build, in a new namespace if their ids carry one.

```sh
bundle install        # once: slim, sass-embedded (bundles Dart Sass), kramdown, rake
./build               # ../def/*.ud -> lexicon.html (self-contained); `rake` does the same
./build --check       # parse only; report unresolved and approximate @{refs} and reading notes
./build --link        # links lexicon.css + lexicon.js instead of inlining (rebuild after editing Sass)
```

Ruby is pinned in `mise.toml` (run `mise trust` once), as in `alignment-model/`. `build` runs from any directory.

## Reading other directories as if they were in def/

```sh
./build ../influx/thin-pass/notation                          # def/ + notation -> lexicon+thin-pass-notation.html
./build ../influx/thin-pass/notation ../influx/model-beta/terms
./build --only ../influx/model-beta/terms                     # without def/
./build ../influx/thin-pass/notation -o ~/Desktop/notation.html
rake DIRS="../influx/thin-pass/notation"                      # the same through rake
```

Each argument is a directory (its `*.ud`), a file, or a glob. The files are read into the same page as `def/`: their terms join the index, references between them resolve both ways, and each namespace gets a section in the sidebar. A view from outside `def/` carries a tag naming where it came from, and the home page lists what was read in. Without `-o`, the page is written next to `lexicon.html` as `lexicon+<dirs>.html`, which git ignores, so `lexicon.html` stays the page for `def/` alone.

`config.yml`'s `collections:` gives a directory a title, a note and a reading order (the thin-pass notation follows its README's order). A directory not listed there still builds, in alphabetical order.

## Files

| File | What to change there |
|---|---|
| `config.yml` | Title and lede; which files, in what order; namespace titles, descriptions and colour family; collections (other directories); namespaces defined elsewhere (`external:`, such as `addr:`); headwords that differ from their ids; each block's label, treatment, order and whether it starts folded |
| `templates/page.slim` | Page structure: the home view, then one view per term group or other top-level element |
| `templates/home.slim` | The home view: title, tally, what was read, index, what needs attention, colophon |
| `templates/nav.slim` | The sidebar: filter box and contents, one section per namespace |
| `templates/group.slim` | One term group's view: a quiet header with the comments above it in the file and the text that introduces its terms, a card per term, a notes card for the group's own blocks |
| `templates/extra.slim` | Any other top-level element (`|resolutions`, `|namespace`, …): a view of its own; resolution lines are set as a table |
| `templates/term.slim` | One term's card: headword, definition, source, synonyms, avoided words, other attributes, relations, blocks, backlinks |
| `templates/block.slim`, `block_body.slim` | One `|invariants`, `|discussion`, … block, and any blocks inside it |
| `templates/facts.slim`, `crumbs.slim`, `lead.slim`, `pager.slim` | Attributes as label/value lines; a view's top line; a file's comments; previous and next |
| `styles/palette.sass` | All colour: paper, ink, the ten families, the dark set, chips, callouts, the notation's marks |
| `styles/style.sass` | Layout and type |
| `lexicon.js` | Filtering, the entry-in-view mark, the arrow keys, the theme switch |
| `build` | The udon reader (`Udon`), the model (`Book`, `Group`, `Term`, `Extra`), the notation in values (`Notation`) and rendering helpers |

## What is read

Udon is read as udon 0.10.0's `CORE.md` describes it (`~/src/arch/firmatum/udon/v2/spec-0.10.00/`), as far as these files need it. That covers:

- Elements: a name, stacked `[ids]`, `.traits`, suffix flags (`? ! * +`), anonymous elements (`|[id]`, `|.trait`), and several on one line (`|a :x 1 |b`).
- Attributes:
  - several on a line (`:a 1 :b 2`);
  - values that end at the next framed ` :label`, ` |name`, ` ; ` or ` \ `, outside quotes and brackets;
  - a label with nothing after it, whose value is then the deeper lines.
- Comments: whole-line `;` comments, which own the deeper lines under them, and sameline ` ; ` comments.
- Verbatim and directives: fences, `!:kind:` verbatim blocks, and `!name` directives, which are carried but never run.
- Escapes at the start of a line: `\|`, `\:`, `\;`, `\\`, and `\ `.
- Text: markdown owned by the element above it. A line deeper than an element's first text line is text, even when it starts with a marker.
- Inline forms in prose: `|{em …}`, `;{…}`, `!{{…}}` and `!{:kind: …}`.

Nothing is dropped. What the builder reads differently from plain udon, carries without running, or finds inconsistent is listed by `--check` and under "Reading notes" on the home page.

Where these files go beyond udon 0.10.0, the builder follows the files. It reads these forms so that drafts can be read; reading a form is not endorsing it. The thin-pass notation's syntax is still open (plan §5, decision 14), and what is decided there goes to the udon team as a needs list, not into this builder by default.

- `:{exact | narrower} @{…}`, a braced label, is read as one label: the notation's ambiguous relation (one of these relations holds; which is undetermined). Udon ends a label at the first space; the valid udon spellings are quoted, `:'exact | narrower'` or `:'{exact | narrower}'`, and all three read and render alike. The braced form gets a reading note.
- A list, set or string left open at the end of a line continues onto the next. Udon leaves this unspecified.
- A line that starts with `|` and ends with `|` is a markdown table row, not an element.
- `@{id}` in prose and values is a reference. In udon 0.10.0 the brace form appears only in key brackets; the house style uses it everywhere.

## What is shown

- **Files.** A file can hold several `|term-group`s; each becomes a view, labelled `file k/n`. A run of bare `|term`s becomes a group. A `|term-group` nested in another becomes a group after it. Any other top-level element gets a view of its own. Comments above a group in its file (a file header, a section rule) show at the top of its view, as written.
- **Terms.**
  - **Definition and body.** A term's definition is its sameline text, or else its first paragraph. Any other text it holds is shown as its body.
  - **Extra ids.** More `[ids]` on a term are aliases, and references to them resolve.
  - **Source.** Each term's `:source` gets a chip:
    - *verbatim* means the text ends "— verbatim";
    - *modified* means ISO 704's `[SOURCE: …, modified — …]`, with the note shown;
    - *cited* is anything else.
  - **Other attributes.** These (`:binding`, `:closure`, `:values`, …) are listed under the header.
- **Headwords.** A dotted id (`arm:harm.over-50-deaths-one-incident`) shows its parent segment muted. A `#sense` shows as a tag. A scoped namespace (`sb53.bp`) shows its scope.
- **References.** Where two terms on the page share a headword, a link to either names its namespace.
- **The notation in values.** Relation targets and attribute values set the notation apart:
  - `{a | b}` (one of these is meant, undetermined) is highlighted like a declared ambiguity;
  - `{a, b}` is a set;
  - `(a | b)` is a union;
  - `{1,N}` is a cardinality;
  - `"words"` are the source's words;
  - `-> ns:x ?` is a path out of the lexicon, not followed;
  - `?` means unresolved;
  - `lean x` is our preference.
- **Relations.** An ambiguous relation (`:'exact | narrower'`, `:'{exact | narrower}'` or `:{exact | narrower}`) is highlighted like an ambiguous value. Comments between relation rows stay where they were written.
- **Resolving `@{id}`.** The rules, in order:
  - Exact ids and aliases link.
  - `@{ns:facet=value}` links to the facet's term. If the value isn't among the term's `:values`, the link is listed as approximate.
  - `@{ns:term#sense}` with no such sense links to the term, and is listed as approximate.
  - A plural or singular form (`@{writers}` for `writer`, `@{referent}` for `referents`) links quietly; `--check` lists these.
  - A namespace listed under `external:` links out.
  - Anything else is marked, listed under "Unresolved references", and makes `--check` exit 1.
- **Group ids.** A group's `[ids]` are checked against the terms it holds.
- **Linking and the index.** In a group's opening, `**BOUNDED-CONTEXT**` (also `**REFERENT**s`) links to its term. Every term lists what refers to it. The index interleaves the terms with their `:synonyms` and `:avoid` words.

**Adding a block type.** Write it in udon. It renders as plain text under a label made from its name, with any blocks inside it nested below. To label, order, fold it, or set it as a list, callout or wide table, give it a line under `blocks:` in `config.yml`. A block set as a table that holds a list is set as a list.

**Markdown and the sources' characters.** kramdown is set to keep straight quotes, `...` and `--` as typed, so quoted passages copied from the page still match the sources character for character.
