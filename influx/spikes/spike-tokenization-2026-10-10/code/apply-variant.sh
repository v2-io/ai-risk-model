#!/bin/sh
# Rebuild the scratch database's tsvector columns with one index form.
#   code/apply-variant.sh q|w|h  [orig-nwords]
# Run from the repository root. Touches only airisk_tokspike (never airisk_sources):
# src.index_form becomes the chosen variant, and tsv_exact, tsv_stem, tsv_head and
# src.headings.tsv are regenerated through it. nwords becomes src.n_words(text)
# (runs of letters and digits), or with orig-nwords, text.words()'s count as today.
set -e
V=$1
DB=airisk_tokspike
[ "$(psql-18 -At -d $DB -c 'select current_database()')" = "$DB" ] || exit 1
psql-18 -q -d $DB -f influx/spikes/spike-tokenization-2026-10-10/code/variants.sql
psql-18 -q -d $DB <<SQL
\set ON_ERROR_STOP on
create table if not exists tok.nwords_orig as select id, nwords from src.passages;
create or replace function src.index_form(t text) returns text
  language sql immutable parallel safe as \$\$ select src.index_form_$V(t) \$\$;
alter table src.passages drop column tsv_exact, drop column tsv_stem, drop column tsv_head;
alter table src.passages
  add column tsv_exact tsvector generated always as (to_tsvector('simple', src.index_form(text))) stored,
  add column tsv_stem  tsvector generated always as (to_tsvector('english', src.index_form(text))) stored,
  add column tsv_head  tsvector generated always as (to_tsvector('simple', src.index_form(heading))) stored;
create index on src.passages using gin (tsv_exact);
create index on src.passages using gin (tsv_stem);
create index on src.passages using gin (tsv_head);
alter table src.headings drop column tsv;
alter table src.headings add column tsv tsvector generated always as
  (to_tsvector('simple', src.index_form(text || ' ' || coalesce(title, '')))) stored;
SQL
if [ "$2" = orig-nwords ]; then
  psql-18 -q -d $DB -c "update src.passages p set nwords = o.nwords from tok.nwords_orig o where o.id = p.id"
else
  psql-18 -q -d $DB -c "update src.passages set nwords = src.n_words(text)"
fi
psql-18 -q -d $DB -c "vacuum analyze src.passages"
echo "applied $V ($([ "$2" = orig-nwords ] && echo 'nwords as today' || echo 'nwords = runs of letters and digits'))"
