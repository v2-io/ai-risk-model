-- The source index's database (search/DESIGN.md §3–§4).
--
-- Everything in schema `src` is derived from the inputs (the catalog, bib/refs.bib,
-- ref/canonical/) and can be dropped and rebuilt: `bin/source-index --rebuild`.
-- Schema changes are made that way, not by migrations. Nothing here is entered by
-- hand; the ranking weights live in the repo (search/weights.toml).
--
-- Schema `cache` holds the embeddings, keyed by model and the sha256 of the text
-- embedded, so a rebuild, or a re-chunk that leaves a passage's text unchanged,
-- never embeds anything twice. `--rebuild` leaves it alone.

create extension if not exists vector;
create extension if not exists pg_trgm;

create schema if not exists cache;

create table if not exists cache.embeddings (
    model       text not null,
    input_sha   text not null,           -- sha256 of the exact text sent to the model
    dims        int  not null,
    vec         halfvec not null,        -- halfvec: half the size of vector, ample precision for cosine ranking
    created     timestamptz not null default now(),
    primary key (model, input_sha)
);

create schema src;

-- What built this database: schema_sha is sha256 of this file, so a changed schema
-- is noticed and answered with --rebuild rather than silently half-applied.
create table src.meta (
    name        text primary key,
    value       text not null
);

-- One row per run of bin/source-index: what it changed, and what it warned about.
create table src.runs (
    id          bigserial primary key,
    started     timestamptz not null default now(),
    finished    timestamptz,
    chunker_sha text not null,           -- sha256 of the chunker's source files
    counts      jsonb,
    warnings    text[]
);

-- One row per catalog key, indexed or not: a key with no text (no-canon, subsumed-by,
-- or not yet converted) still answers "what is this source" and "is it in the corpus".
create table src.documents (
    key             text primary key,
    status          text not null check (status in ('active', 'superseded', 'subsumed')),
    active_key      text,                -- for a superseded key, the version its chain ends at
    subsumed_by     text,
    no_canon        text,                -- the reason, when the catalog gives one
    has_text        boolean not null,
    section         text,                -- the catalog section it is first listed under
    code            text,                -- the main table's Code
    group_label     text,                -- its bold group label under "The rest of the corpus"
    influence       text,                -- anchor | major | supporting | context | corpus
    cat_date        text,
    cat_kind        text,
    cat_document    text,
    title           text,
    authors         text,
    org             text,                -- recency is measured within it (DESIGN §6.2)
    year            int,
    url             text,
    bib_type        text,
    fidelity_mark   text,                -- trusted | check-pages | check-all (pages.json)
    pages_to_check  int[],
    text_fp         text,                -- sha256 of the canonical file + the chunker's source
    meta_fp         text,                -- sha256 of its bib entry and catalog row
    fidelity_fp     text,                -- sha256 of pages.json's fidelity section
    n_passages      int not null default 0,
    indexed_at      timestamptz
);

-- Headings, so `--all` can count a term in headings apart from body text (the pilot
-- found 6 of the NRR's 79 "hazard" forms in headings only).
create table src.headings (
    doc_key     text not null references src.documents (key) on delete cascade,
    ord         int  not null,
    start_off   int  not null,
    end_off     int  not null,
    level       int  not null,
    text        text not null,
    title       text,                    -- a label heading's title ("Article 3" — "Definitions")
    path        text[] not null,
    page        int,
    printed     text,
    tsv         tsvector generated always as (to_tsvector('simple', text || ' ' || coalesce(title, ''))) stored,
    primary key (doc_key, ord)
);

create table src.passages (
    id          bigserial primary key,
    doc_key     text not null references src.documents (key) on delete cascade,
    layer       text not null default 'canonical',   -- room for translated editions (DESIGN §9)
    ord         int  not null,
    start_off   int  not null,           -- [start_off, end_off) in ref/canonical/KEY.md
    end_off     int  not null,
    page        int,                     -- physical PDF page where it starts, and ends
    printed     text,
    page_last   int,
    printed_last text,
    pages       int[],                   -- every page it touches, in text order (can run backwards)
    not_in_pdf  boolean not null default false,
    path        text[] not null,
    heading     text not null,           -- path joined with ' › ' (a generated column can't use array_to_string)
    section     text not null,           -- body | glossary | toc | references | abbreviations | index | annex | restored
    kinds       text[] not null,         -- the block kinds it holds; 'cut' if it is a piece of a longer block
    text        text not null,           -- indexed text: links, tags, images and emphasis removed
    norm_sha    text not null,           -- sha256 of its words, for collapsing duplicates (DESIGN §6.3)
    embed_sha   text not null,           -- sha256 of its embedding input; joins cache.embeddings
    tsv_exact   tsvector generated always as (to_tsvector('simple', text)) stored,
    tsv_stem    tsvector generated always as (to_tsvector('english', text)) stored,
    tsv_head    tsvector generated always as (to_tsvector('simple', heading)) stored,
    unique (doc_key, layer, ord)
);
create index on src.passages using gin (tsv_exact);
create index on src.passages using gin (tsv_stem);
create index on src.passages using gin (tsv_head);
create index on src.passages (norm_sha);
create index on src.passages (embed_sha);

-- A term a passage defines (DESIGN §5.3). Detection errs toward recall; conf and
-- evidence say how sure, so a false positive is visible in --defs.
create table src.definitions (
    id          bigserial primary key,
    passage_id  bigint not null references src.passages (id) on delete cascade,
    doc_key     text not null references src.documents (key) on delete cascade,
    term        text not null,           -- as written
    norm        text not null,           -- text.norm_term: folded, singular, without quotes or parentheticals
    kind        text not null,
    conf        real not null,
    evidence    text,
    at_off      int  not null,           -- where the defining words start in the canonical file
    page        int,
    printed     text
);
create index on src.definitions (norm);
create index on src.definitions using gin (norm gin_trgm_ops);
create index on src.definitions (doc_key);
