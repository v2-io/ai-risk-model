#!/bin/sh
# Recreate code/srcsearch/ (git-ignored): search/srcsearch/ with experimental-srcsearch.patch,
# the query-side variant the Q, W, H and Wn runs used. Run from the repository root.
set -e
S=influx/spikes/spike-tokenization-2026-10-10
rm -rf $S/code/srcsearch && mkdir -p $S/code/srcsearch
cp search/srcsearch/*.py $S/code/srcsearch/
patch -s -p3 -d $S/code/srcsearch < $S/code/experimental-srcsearch.patch
echo "made $S/code/srcsearch"
