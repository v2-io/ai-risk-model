-- The tokenizer census (README §1-§2): what Postgres's parser does to every passage,
-- and which words a reader can see that a search can't find.
--
--   createdb-18 airisk_tokspike && pg_dump-18 airisk_sources | psql-18 -q -d airisk_tokspike
--   psql-18 -d airisk_tokspike -f code/census.sql > runs/census.txt
--
-- tok.lex is today's tsv_exact, recomputed from the text (to_tsvector('simple', text), the
-- column's definition in search/schema.sql), so it doesn't matter which variant
-- code/apply-variant.sh last applied. Writes only schema tok. About two minutes.
\pset pager off
create extension if not exists unaccent;
create schema if not exists tok;
drop table if exists tok.tokens, tok.lex, tok.rw, tok.rwf, tok.compound, tok.cparts, tok.unfindable, tok.lex_w, tok.lex_h cascade;

-- every token, in order
create table tok.tokens as
  select p.id pid, p.doc_key, t.n, t.tokid, t.token
  from src.passages p, lateral ts_parse('default', p.text) with ordinality t(tokid, token, n);
create index on tok.tokens (tokid);
create index on tok.tokens (pid);

\echo '== 1. tokens by parser type (blank and tag/entity/protocol have no mapping in simple or english: never indexed)'
select a.alias, count(*) n, count(distinct t.pid) passages, count(distinct lower(token)) distinct_tokens
from tok.tokens t join ts_token_type('default') a on a.tokid = t.tokid group by a.alias order by n desc;

-- today's lexemes, and the reader's words (maximal runs of letters and digits)
create table tok.lex as select p.id pid, x.lexeme from src.passages p, unnest(to_tsvector('simple', p.text)) x;
create index on tok.lex (pid, lexeme);
create table tok.rw as
  select p.id pid, w word, count(*) n from src.passages p, regexp_split_to_table(lower(p.text), '[^[:alnum:]]+') w
  where w <> '' group by 1, 2;
create index on tok.rw (pid, word);
-- a word searched alone: today the query is text.fold(w) through the parser, which for a
-- run of letters and digits is unaccent(lower(w)); findable iff that is a lexeme of the passage
create table tok.rwf as select pid, word, unaccent(word) q, n from tok.rw;
create index on tok.rwf (pid, q);

-- shape classes for the parser's compound tokens
create or replace function tok.klass(tokid int, t text) returns text language sql immutable as $$
select case
 when tokid = 19 and t ~ '^[[:alpha:]]+(/[[:alpha:]]+)+$' then 'A slash-joined words'
 when tokid = 19 and t ~ '^[0-9]+(/[0-9]+)+$' then 'B slash-joined numbers'
 when tokid in (19,6) and t ~ '^([[:alpha:]]{1,3}\.)+[[:alpha:]]{1,3}$' and t !~* '\.(com|org|net|gov|edu|io|py|md|sh|js|uk|ai)$' and t !~ '^cs\.' then 'C dotted abbreviation'
 when tokid = 6 and t ~* '^(cs|stat|econ|math|eess|q-bio|physics|hep-th|quant-ph)\.[a-z]{2}$' then 'H arXiv category'
 when tokid = 6 and t ~* '\.(py|md|txt|json|pdf|html?|sh|csv|ya?ml|js|log|sgm|ts|ipynb|xml|tex|png|jpg)$' then 'G filename'
 when tokid = 6 and t ~* '\.(com|org|net|gov|edu|io|ai|uk|co|eu|int|dev|app|me|ca|fr|de|cn|tv|info|us|xyz|ac|quebec)$' and t ~ '^[[:alnum:]-]+(\.[[:alnum:]-]+)+$' then 'D domain or dotted brand name'
 when tokid = 6 and t ~ '^[[:alpha:]]{2,}\.[[:alpha:]]{2,}$' then 'E words joined by a period (no space)'
 when tokid in (19) and t ~ '^[[:alpha:]]{1,3}[0-9]*\.[0-9]+(\.[0-9]+)*$' then 'F labelled number (A.1, v3.4)'
 when tokid in (8) then 'I dotted section number (version)'
 when tokid in (20) then 'J decimal (float)'
 when tokid in (21) then 'K signed integer (hyphen before digits)'
 when tokid in (7) then 'L scientific notation'
 when tokid in (4,5,18,14) or tokid in (6,19) then 'M URL, email, path, other dotted/slashed'
 when tokid in (13,23) then 'N dropped: XML tag or entity'
 else 'other' end $$;
create or replace function tok.klass2(tokid int, t text) returns text language sql immutable as $$
select case
 when tokid in (6,19) and t ~ '^[[:alpha:]]{2,}\.[0-9]{1,4}$' and t !~ '^[vV][0-9]' then 'E2 word.footnote-number'
 when tokid in (6,19) and t ~ '^[[:alpha:]]*[[:lower:]]{2,}\.[[:upper:]][[:lower:]]+$' then 'E1 sentence join (word.Word)'
 when tokid in (6,19) and t ~ '^[[:alpha:]_]+\.[[:alpha:]_]+(\.[[:alpha:]_]+)*$' and tok.klass(tokid,t) like 'E%' then 'E3 code identifier / other word.word'
 when tokid in (5,6,19) and t ~ '^([[:alpha:]]+-)*[[:alpha:]]+[0-9]+\.[0-9]+(-[[:alnum:]]+)+$' then 'O model name with decimal (Qwen2.5-7B)'
 else tok.klass(tokid, t) end $$;
create table tok.compound as
  select pid, doc_key, n, tokid, token, tok.klass2(tokid, token) k2 from tok.tokens
  where tokid in (4,5,6,7,8,13,14,18,19,20,21,23);

\echo '== 2. compound tokens by shape class'
select k2, count(*) tokens, count(distinct pid) passages, count(distinct doc_key) docs, count(distinct lower(token)) distinct_tokens
from tok.compound group by 1 order by 1;

\echo '== 3. most frequent tokens per class'
select k2, string_agg(token || ' ×' || c, '  ' order by c desc) top from (
  select k2, token, count(*) c, row_number() over (partition by k2 order by count(*) desc) r from tok.compound group by 1, 2) x
where r <= 25 group by k2 order by k2;

-- each unfindable (passage, word) attributed to the compound token that holds it
create table tok.cparts as
  select distinct on (c.pid, w) c.pid, w part, c.k2
  from tok.compound c, regexp_split_to_table(lower(c.token), '[^[:alnum:]]+') w where w <> '' order by c.pid, w, c.k2;
create index on tok.cparts (pid, part);
create table tok.unfindable as
  select r.pid, r.word, r.n,
         coalesce(c.k2, case when r.q <> r.word then 'P accent or ligature (query folded, index not)' else '(no compound token)' end) k2
  from tok.rwf r left join tok.cparts c on c.pid = r.pid and c.part = r.word
  where not exists (select 1 from tok.lex l where l.pid = r.pid and l.lexeme = r.q);

\echo '== 4. unfindable (passage, word) pairs today, by class and kind of word'
select k2,
  count(*) filter (where word ~ '^[[:alpha:]]{3,}$') "letters 3+",
  count(distinct pid) filter (where word ~ '^[[:alpha:]]{3,}$') "passages (3+)",
  count(*) filter (where word ~ '^[[:alpha:]]{1,2}$') "letters 1-2",
  count(*) filter (where word ~ '^[0-9]+$') digits,
  count(*) filter (where word !~ '^[[:alpha:]]+$' and word !~ '^[0-9]+$') mixed,
  count(*) pairs, count(distinct pid) passages
from tok.unfindable group by rollup (1) order by 1 nulls last;

\echo '== 5. the most often hidden words of 3+ letters, per class'
select k2, string_agg(word || ' ' || np, ', ' order by np desc) top from (
  select k2, word, count(distinct pid) np, row_number() over (partition by k2 order by count(distinct pid) desc) r
  from tok.unfindable where word ~ '^[[:alpha:]]{3,}$' group by 1, 2) x where r <= 30 group by k2 order by k2;

\echo '== 6. glyph-level damage (canonicalizer territory)'
select 'ligature' what, count(*) passages, count(distinct doc_key) docs from src.passages where text ~ '[ﬀ-ﬆ]'
union all select 'superscript digits', count(*), count(distinct doc_key) from src.passages where text ~ '[⁰¹²³⁴-⁹]'
union all select 'caret exponent 10^n', count(*), count(distinct doc_key) from src.passages where text ~ '[0-9]\^[0-9]'
union all select 'combining marks', count(*), count(distinct doc_key) from src.passages where text ~ E'[̀-ͯ]'
union all select 'Cyrillic word that looks Latin (Туре)', count(distinct pid), count(distinct doc_key) from tok.tokens where token in ('Туре')
union all select 'U+FFFD', count(*), count(distinct doc_key) from src.passages where text ~ E'�'
union all select 'non-ASCII hyphen U+2010/2011', count(*), count(distinct doc_key) from src.passages where text ~ E'[‐‑]'
union all select 'literal <sup> left in indexed text', count(*), count(distinct doc_key) from src.passages where text ~ '<sup>|</sup>'
union all select 'no letter or digit at all', count(*), count(distinct doc_key) from src.passages where text !~ '[[:alnum:]]';

\echo '== 7. a footnote digit glued to a word (one run of letters and digits: no index form splits it)'
create temp table v as select lexeme from tok.lex where lexeme ~ '^[a-z]{4,}$' group by 1 having count(distinct pid) >= 5;
select case when token ~ '^[0-9]' then 'digits+word (14After)' else 'word+digits (harms1)' end k, count(*) occ, count(distinct pid) passages, count(distinct doc_key) docs
from tok.tokens t join v on v.lexeme = lower(coalesce(substring(t.token from '^[0-9]{1,3}([A-Za-z]{4,})$'), substring(t.token from '^([A-Za-z]{4,})[0-9]{1,3}$')))
where t.tokid = 3 group by 1;
