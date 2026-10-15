# France Drug Shortage API — ANSM Stock-outs & Alerts

**Which medicines are out of stock or under supply tension in France right now — and which ones you stock?** Paste your CIP13 codes or schedule a daily run to be alerted when a status changes.

> 🇫🇷 Ruptures et tensions d'approvisionnement de médicaments (ANSM) : API et alertes par code CIP13. Les exemples ci-dessous sont en anglais ; les données restent en français.

**[▶ Run it on Apify](https://apify.com/jet_mythology/france-drug-shortages)** — no installation, no scraping, official data only.

## Use it without code

1. Open the [Actor page](https://apify.com/jet_mythology/france-drug-shortages) and click **Try for free**.
2. Paste one of the inputs below (or use the form).
3. Click **Start**, then **Export** the results as **Excel, CSV or JSON**, or send them to Google Sheets, Make, Zapier or n8n.

Schedule it (daily or weekly) to get only what changed since the last run.

## Sample output

```json
{
  "statusLabel": "Rupture de stock",
  "drugName": "LARIAM 250 mg, comprimé sécable",
  "holders": [
    "CHEPLAPHARM ARZNEIMITTEL (ALLEMAGNE)"
  ],
  "startDate": "2026-06-25",
  "updatedAt": "2026-10-08",
  "availableAgainDate": null,
  "majorTherapeuticInterest": true,
  "ansmUrl": "https://ansm.sante.fr/disponibilites-des-produits-de-sante/medicaments/lariam-250-mg-comprime-secable-mefloquine"
}
```

*Real result from 8 October 2026 (abridged).* Full field list below.

## Use it from code

Get your API token in [Apify Console → Settings → API & Integrations](https://console.apify.com/settings/integrations).

**Python** (`pip install apify-client`) — see [`examples/run.py`](examples/run.py)

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("jet_mythology/france-drug-shortages").call(run_input={"statuses": ["shortage", "supply-tension"]})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

**JavaScript** (`npm install apify-client`) — see [`examples/run.mjs`](examples/run.mjs)

```js
import { ApifyClient } from "apify-client";

const client = new ApifyClient({ token: "YOUR_APIFY_TOKEN" });
const run = await client.actor("jet_mythology/france-drug-shortages").call({"statuses": ["shortage", "supply-tension"]});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

**curl** — one call, results returned directly — see [`examples/run.sh`](examples/run.sh)

```bash
curl -X POST "https://api.apify.com/v2/acts/jet_mythology~france-drug-shortages/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"statuses": ["shortage", "supply-tension"]}'
```

## Example inputs

**All current stock-outs and tensions**
```json
{"statuses": ["shortage", "supply-tension"]}
```

**Check a pharmacy's product list**
```json
{"codes": ["3400930000011", "3400930000028"], "statuses": ["shortage", "supply-tension", "discontinued", "available-again"]}
```

**Daily alert on antibiotics (ATC J01), including "back in stock"**
```json
{"atcPrefixes": ["J01"], "monitorChanges": true, "monitorKey": "antibiotics"}
```

## Who uses it

- **Pharmacies and pharmacy groups**: check your product list by CIP13 and get an alert when a drug runs out or comes back.
- **Wholesalers, hospital pharmacies and procurement**: anticipate substitutions.
- **Healthtech and pharmacy software vendors**: show availability warnings in your product.
- **Journalists and researchers**: track shortages over time by laboratory or therapeutic class.

## What you get

| Field | Description |
|---|---|
| `status`, `statusLabel` | `shortage`, `supply-tension`, `discontinued`, `available-again` |
| `drugName`, `form`, `routes` | Medicine name, pharmaceutical form, routes |
| `cis`, `cip13`, `cip7`, `presentation`, `scope` | Identifiers; `scope` = one presentation or all presentations |
| `holders` | Marketing authorisation holder(s) |
| `startDate`, `updatedAt`, `availableAgainDate` | Dates of the status |
| `majorTherapeuticInterest`, `atcCode` | MITM flag and ATC code |
| `ansmUrl` | Official ANSM notice |
| `changeType`, `previousStatus` | Monitor mode: `new`, `status-changed`, `updated`, `no-longer-listed` |

## Pricing

Pay per result on Apify: you only pay for the items returned, nothing for what is filtered out. In monitor mode you only pay for new or changed items. Current prices are on the [Actor page](https://apify.com/jet_mythology/france-drug-shortages).

## Good to know

- Source files are those of the Base de Données Publique des Médicaments, which mirrors the ANSM availability information.
- ATC codes come from the list of medicines of major therapeutic interest, so the ATC filter only returns MITM medicines.
- In monitor mode every status is tracked, so a medicine going from "shortage" to "back in stock" is reported as a change.

## Source and licence

ANSM / Base de Données Publique des Médicaments (base-donnees-publique.medicaments.gouv.fr), reused under the Licence Ouverte (Etalab). Each record carries its official update date. This Actor is independent and not affiliated with the ANSM or the French administration. It provides information, not medical or pharmaceutical advice.

The code examples in this repository are under the MIT licence. This repository contains usage examples only; the Actor itself runs on [Apify](https://apify.com/jet_mythology/france-drug-shortages).

---

More French public data Actors by the same author: [apify.com/jet_mythology](https://apify.com/jet_mythology)
