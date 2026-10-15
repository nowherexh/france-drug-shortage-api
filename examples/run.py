"""Run France Drug Shortage API — ANSM Stock-outs & Alerts on Apify and save the results to results.csv.

pip install apify-client
set APIFY_TOKEN=your_token   (Windows)  |  export APIFY_TOKEN=your_token   (macOS/Linux)
python run.py
"""
import csv
import json
import os

from apify_client import ApifyClient

RUN_INPUT = {
    "statuses": [
        "shortage",
        "supply-tension"
    ]
}

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("jet_mythology/france-drug-shortages").call(run_input=RUN_INPUT)
items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
print(f"{len(items)} items")

if items:
    keys = sorted({k for item in items for k in item})
    with open("results.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for item in items:
            writer.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v
                             for k, v in item.items()})
    print("Saved to results.csv (opens in Excel)")
