"""Run a search/eval script (or bin/source-search) with this spike's patched srcsearch.

    python3 influx/spikes/spike-tokenization-2026-10-10/code/patched.py search/eval/pilot-check [args]

The patched package (code/srcsearch/, a copy of search/srcsearch/ with rank.py's query
side sending every query through src.index_form) is imported first, so the script's own
`sys.path.insert(0, REPO/search)` finds it already in sys.modules. Point it at the
scratch database with AIRISK_SOURCES_DB=airisk_tokspike; src.index_form exists only there.
"""
import os, runpy, sys

sys.dont_write_bytecode = True
# SRCSEARCH_PARENT: a directory holding another srcsearch package to test instead
# (e.g. search/ of a tree with proposed.patch applied); default, this spike's code/
sys.path.insert(0, os.environ.get('SRCSEARCH_PARENT') or os.path.dirname(os.path.abspath(__file__)))
import srcsearch  # noqa: E402,F401  (the patched copy)
print(f'# srcsearch from {os.path.dirname(srcsearch.__file__)}', file=sys.stderr)

assert os.environ.get('AIRISK_SOURCES_DB', 'airisk_sources') != 'airisk_sources', \
    'the patched code needs src.index_form, which only the scratch database has'
script = sys.argv[1]
sys.argv = sys.argv[1:]
runpy.run_path(script, run_name='__main__')
