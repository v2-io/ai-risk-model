-- Schema `cache`'s tables besides the embeddings: things worked out once and kept
-- across `bin/source-index --rebuild`, which drops only schema `src`. Kept apart
-- from schema.sql so that adding a cache doesn't change schema.sql's sha256, which
-- would ask for a rebuild that a cache doesn't need. Every statement is idempotent:
-- bin/source-index and bin/source-search both run this file.

create schema if not exists cache;

-- bin/check-quote's verdict on an anchor whose page the canonical text alone can't
-- settle (DESIGN §5.1: "settled by bin/check-quote, which checks against the PDF,
-- and it is cached"). A verdict holds for one canonical text and one checker: the
-- key carries the sha256 of the canonical file and of bin/check-quote and
-- bin/canonicalize together, so a rebuilt text or a changed checker is checked
-- afresh, never served a stale verdict.
create table if not exists cache.quote_checks (
    doc_key      text not null,
    quote_sha    text not null,          -- sha256 of the quote
    page_cited   int  not null,          -- the page the anchor gave
    canon_sha    text not null,          -- sha256 of ref/canonical/KEY.md
    checker_sha  text not null,          -- sha256 of bin/check-quote + bin/canonicalize
    quote        text not null,
    status       text not null,          -- check-quote's: ok, unconfirmed, not-in-pdf, ambiguous, …
    page         int,                    -- the settled page
    page_from    text,                   -- pdf | canonical
    printed      text,
    record       jsonb not null,         -- check-quote's whole record for the anchor
    checked_at   timestamptz not null default now(),
    primary key (doc_key, quote_sha, page_cited, canon_sha, checker_sha)
);
