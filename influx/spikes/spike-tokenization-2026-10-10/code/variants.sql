-- The index forms compared in this spike. Each is a function from a passage's (or a
-- query's) text to the text Postgres's parser is given. The same function is used on
-- both sides: the generated tsvector columns, and every to_tsvector / plainto_tsquery
-- the ranking code builds from a query (code/srcsearch/rank.py, patched).
--
-- Applied to the scratch database only (airisk_tokspike, a pg_dump copy of
-- airisk_sources), by code/apply-variant.sh VARIANT.
--
--   Q   identity: today's index, so only the query side's changes are measured
--   W   words:    a word is a run of letters and digits; every other character
--                separates. Accents and ligatures folded (unaccent), as the query
--                side's text.fold already does.
--   H   words + hyphen compounds: as W, except a hyphen between two letters is kept,
--                so the parser indexes "loss-of-control" whole and by its parts, as
--                it does today. A hyphen next to a digit separates ("COVID-19",
--                "2024-2025"), since the parser would read "-19" as a signed number.

create extension if not exists unaccent;

create or replace function src.index_form_q(t text) returns text
  language sql immutable parallel safe as $$ select t $$;

create or replace function src.index_form_w(t text) returns text
  language sql immutable parallel safe as
$$ select regexp_replace(public.unaccent('public.unaccent'::regdictionary, t), '[^[:alnum:]]+', ' ', 'g') $$;

create or replace function src.index_form_h(t text) returns text
  language sql immutable parallel safe as
$$ select regexp_replace(
            regexp_replace(public.unaccent('public.unaccent'::regdictionary, t), '[^[:alnum:]-]+', ' ', 'g'),
            '(?<![[:alpha:]])-|-(?![[:alpha:]])', ' ', 'g') $$;

-- A word count to match: the number of runs of letters and digits (BM25's length).
create or replace function src.n_words(t text) returns int
  language sql immutable parallel safe as
$$ select coalesce(array_length(regexp_split_to_array(btrim(src.index_form_w(t)), ' '), 1), 0) $$;
