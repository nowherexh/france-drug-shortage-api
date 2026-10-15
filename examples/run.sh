#!/usr/bin/env bash
# Run France Drug Shortage API — ANSM Stock-outs & Alerts on Apify and print the results as JSON.
# export APIFY_TOKEN=your_token && bash run.sh
set -euo pipefail
curl -sS -X POST "https://api.apify.com/v2/acts/jet_mythology~france-drug-shortages/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"statuses": ["shortage", "supply-tension"]}'
