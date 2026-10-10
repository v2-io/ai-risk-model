-- The invariant the fix is for: every word a reader can see in a passage (a maximal
-- run of letters and digits) is findable by searching for that word alone.
--
--   psql-18 -d airisk_tokspike -f code/invariant.sql
--
-- Needs tok.rwf and tok.lex from code/census.sql. Counts unfindable (passage, word)
-- pairs for today (tok.lex) and for the W and H index forms (code/variants.sql),
-- computed here from the text, whatever the passages' columns currently hold.
\pset pager off
\i influx/spikes/spike-tokenization-2026-10-10/code/variants.sql
create table if not exists tok.lex_w as select p.id pid, x.lexeme from src.passages p, unnest(to_tsvector('simple', src.index_form_w(p.text))) x;
create table if not exists tok.lex_h as select p.id pid, x.lexeme from src.passages p, unnest(to_tsvector('simple', src.index_form_h(p.text))) x;
create index if not exists lex_w_i on tok.lex_w (pid, lexeme);
create index if not exists lex_h_i on tok.lex_h (pid, lexeme);
select v, count(*) pairs, count(distinct pid) passages,
  count(*) filter (where word ~ '^[[:alpha:]]{3,}$') "letters 3+",
  count(*) filter (where word ~ '^[[:alpha:]]{1,2}$') "letters 1-2",
  count(*) filter (where word ~ '^[0-9]+$') digits,
  count(*) filter (where word !~ '^[[:alpha:]]+$' and word !~ '^[0-9]+$') mixed
from (
  select 'today' v, r.* from tok.rwf r where not exists (select 1 from tok.lex l where l.pid = r.pid and l.lexeme = r.q)
  union all select 'W', r.* from tok.rwf r where not exists (select 1 from tok.lex_w l where l.pid = r.pid and l.lexeme = r.q)
  union all select 'H', r.* from tok.rwf r where not exists (select 1 from tok.lex_h l where l.pid = r.pid and l.lexeme = r.q)
) x group by v order by pairs desc;
\echo 'what W leaves (math notation such as pˆ, hex hashes, a few split names):'
select r.word, count(*) from tok.rwf r
where not exists (select 1 from tok.lex_w l where l.pid = r.pid and l.lexeme = r.q)
group by 1 order by 2 desc limit 25;
