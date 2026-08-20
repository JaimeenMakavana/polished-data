# Ahmedabad startups — example (sanitized)

This is a **small public sample** so you can see output shape without cloning a live job folder.

The full 2026-08-20 run lived in `data-workspace/jobs/job_2026_08_20_ahmedabad_startups/` on the machine that acquired it. That directory is gitignored (raw HTML, local paths, complete dump). Do not commit it.

## What is in this folder

| File | Role |
|------|------|
| `sample.csv` / `sample.json` | 20 rows, emails/phones/founders omitted |
| `schema.json` | Field definitions |
| `data-contract.yaml` | Contract the agent confirmed before fetch |
| `quality-report.json` | Stats from the **full** local run (context only) |
| `REPRODUCE.md` | Exact prompt and expected artifacts |

## Sanitize rules used

- Cap at 20 records
- Drop `email`, `phone`, `founder`
- Drop absolute filesystem paths
- Keep company name, website, city, sector, coordinates, source URL (all from public incubator/directory pages)

## Reproduce

See [REPRODUCE.md](REPRODUCE.md). Short version: open this repo in a coding agent and paste the prompt there. You will get a **new** job under `data-workspace/`, not a byte-identical copy of the original 870-row file.
