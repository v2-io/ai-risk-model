"""The source index: a semantic and lexical index over the catalog's sources.

The design is search/DESIGN.md. The modules:
- text:    cleaning a canonical text for indexing while keeping each character's
           offset in the canonical file, and normalising terms and words;
- catalog: the documents to index, from source-catalog.md, bib/refs.bib and
           ref/canonical/, with their fingerprints;
- chunk:   a canonical text cut into blocks, then passages;
- defs:    where a block defines a term;
- db:      the database: reconcile it with the inputs.
"""
import os, sys

sys.dont_write_bytecode = True   # importing bin/corpus.py would otherwise leave bin/__pycache__ behind

SEARCH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(SEARCH)
if os.path.join(REPO, 'bin') not in sys.path:
    sys.path.insert(0, os.path.join(REPO, 'bin'))
CANON = os.path.join(REPO, 'ref', 'canonical')
