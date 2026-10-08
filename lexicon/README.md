# lexicon

Builds `lexicon.html`, a readable lexicon page, from the udon term groups in `../def/`. New files in `def/` appear on the next build, in a new namespace if their ids carry one.

```sh
bundle install        # once: slim, sass-embedded (bundles Dart Sass), kramdown, rake
rake                  # ../def/*.ud -> lexicon.html (self-contained)
rake check            # parse only; list unresolved @{refs} (exit 1 if any)
rake link             # links lexicon.css + lexicon.js instead of inlining (rebuild after editing Sass)

ruby build.rb ../influx/model-beta/terms/*.ud -o beta.html   # any other term files
```

Ruby is pinned in `mise.toml` (run `mise trust` once), as in `alignment-model/`.

| File | What to change there |
|---|---|
| `config.yml` | Title and lede; which files, in what order; namespace titles, descriptions and colour family; namespaces defined elsewhere (`external:`, such as `addr:`); headwords that differ from their ids; each block's label, treatment, order and whether it starts folded |
| `templates/page.slim` | Page structure: the home view, then one view per term group |
| `templates/home.slim` | The home view: title, tally, index, unresolved references, colophon |
| `templates/nav.slim` | The sidebar: filter box and contents |
| `templates/group.slim` | One term group's view: a quiet header with the text that introduces its terms, a card per term, a notes card for the group's own blocks, previous and next group |
| `templates/term.slim` | One term's card: headword, definition, source, synonyms, avoided words, relations, blocks, backlinks |
| `templates/block.slim`, `block_body.slim` | One `|invariants`, `|discussion`, … block |
| `styles/palette.sass` | All colour: paper, ink and the ten families (alignment-model's), the dark set, chips and callouts |
| `styles/style.sass` | Layout and type |
| `lexicon.js` | Filtering, the entry-in-view mark, the theme switch |
| `build.rb` | The udon reader, the model (`Book`, `Group`, `Term`) and rendering helpers |

**What is read.** `build.rb` reads the udon that `def/` uses, not all of udon: elements with `[ids]`, inline text or inline attributes; `:key value ; comment` attributes (strings, `[lists]`, or raw values); whole-line `;` comments; and markdown text owned by the element above it by indentation (so `| a | b |` lines are tables). Each file's `|term-group` gives a group; a file of bare `|term` elements becomes a group too.

**How it reads.** The page shows one view at a time. The home view holds the title and the index. A link to a term opens its group's view with that term's card in view and outlined. A link to a group (its label in the sidebar) opens the view at the top. The ← and → keys step between groups. The switching is CSS (`:target`); `lexicon.js` only adds the filter, the sidebar mark, the arrow keys and the theme switch. Printing shows every view.

**What is shown.**
- Each term's `:source` gets a chip. *Verbatim* means the text ends "— verbatim". *Modified* means ISO 704's `[SOURCE: …, modified — …]`, with the note shown. *Cited* is anything else.
- `@{id}` becomes a link when the id is a term here, or links out when its namespace is listed under `external:`. Otherwise it is marked and listed under "Unresolved references", and `rake check` fails.
- In a group's opening, `**BOUNDED-CONTEXT**` links to its term.
- Every term lists what refers to it.
- The index interleaves the terms with their `:synonyms` and `:avoid` words.

**Adding a block type.** Write it in udon. It renders as plain text under a label made from its name. To label, order, fold it, or set it as a list, callout or wide table, give it a line under `blocks:` in `config.yml`.

**Markdown and the sources' characters.** kramdown is set to keep straight quotes, `...` and `--` as typed, so quoted passages copied from the page still match the sources character for character.
