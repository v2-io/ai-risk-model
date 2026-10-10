#!/bin/sh
# Run the three instruments against the scratch database, for one variant.
#   code/evals.sh LABEL [python launcher]
# LABEL names the output files in runs/. With the launcher (code/patched.py), the
# eval scripts run with this spike's patched srcsearch in place of search/'s.
# Run from the repository root. AIRISK_SOURCES_DB defaults to airisk_tokspike.
set -e
L=$1; shift
S=influx/spikes/spike-tokenization-2026-10-10
export AIRISK_SOURCES_DB=${AIRISK_SOURCES_DB:-airisk_tokspike}
L1=${1:-}
$( [ -n "$L1" ] && echo "python3 $L1" ) search/eval/pilot-check --per-query > $S/runs/$L-pilot-check.txt 2>&1
$( [ -n "$L1" ] && echo "python3 $L1" ) search/eval/outline-check --judgments search/eval/outline-judgments --per-query > $S/runs/$L-outline-judges.txt 2>&1
$( [ -n "$L1" ] && echo "python3 $L1" ) search/eval/outline-check --judgments search/eval/expert-judgments --per-query > $S/runs/$L-outline-experts.txt 2>&1
grep -h "mean nDCG" $S/runs/$L-pilot-check.txt
for f in judges experts; do echo "== $f"; sed -n '/^pooled:/,/^$/p' $S/runs/$L-outline-$f.txt; done
