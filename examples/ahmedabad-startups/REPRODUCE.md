# Reproduce the Ahmedabad startups example

This is not a pinned dump of 870 rows. Public pages change. A new run should follow the same contract and honesty rules, not match yesterday’s count.

## Prompt (paste into your coding agent)

> Get at least 500 Ahmedabad startups with company name, website, city, sector, and lat/long. Prefer public sources. CSV and JSON.

## What the agent must do

1. Restate the request as a data contract (`requirement/data-contract.yaml`).
2. Wait for your confirmation (`MANDATORY_REQUIREMENT.md`).
3. Discover existing tools before writing a scraper.
4. Use public incubator/directory pages and datasets only. No login bypass.
5. Write a new job folder:

```text
data-workspace/jobs/job_<date>_ahmedabad_startups/
  output/result.csv
  output/result.json
  output/README.md
  validation/quality-report.json
  manifest.json
```

6. Report gaps (for example: websites missing on many incubator listings) instead of inventing values.

## Expected schema

See `schema.json`. Required fields for a **complete** row: `company_name`, `website`, `city`, `sector`, `latitude`, `longitude`, `verification_status`.

The original run reached 870 named startups with coordinates but only 331 with a website. Your numbers will differ.

## Optional config

Copy `.env.example` to `.env` if you want a GitHub token (tool discovery rate limits) or a self-hosted Photon URL. Not required.

## After the run

Keep live artifacts in `data-workspace/` (ignored). If you want to share a sample, copy ≤20 rows here and strip email, phone, founder, and local paths — same as `sample.csv`.
