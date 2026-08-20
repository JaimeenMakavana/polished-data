# Polished Data

You say **what data you need**. An AI coding agent (Cursor, Codex, Claude Code, and similar) figures out **where it lives**, **how to get it**, and **hands you a file you can use**.

You do not fill forms, pick scrapers, or stitch sources yourself.

---

## How to use it

1. Open this folder in your coding agent.
2. Ask for the data in plain English. Be specific about fields, place, and how many records.
3. Confirm the agent’s summary of your request before it starts collecting.
4. Take the files from `data-workspace/jobs/<job-id>/output/`.

That’s the whole loop.

### Example request

> Get at least 500 Ahmedabad startups with company name, website, city, sector, and lat/long. Prefer public sources. CSV and JSON.

The agent will restate that, wait for your OK, then run.

---

## What you get

Each job is a folder under `data-workspace/jobs/`. Open `output/` first.

| File | What it is |
|------|------------|
| `result.csv` / `result.json` | The dataset |
| `README.md` | Counts, schema, sources, gaps |
| `validation/quality-report.json` | Completeness and confidence |

If something could not be found honestly, you get an explanation — not invented rows.

A finished example: `data-workspace/jobs/job_2026_08_20_ahmedabad_startups/output/`.

---

## What it will not do

- Invent companies, emails, or other records
- Bypass logins, paywalls, or access controls
- Treat GitHub stars as proof a tool is good
- Pad volume at the cost of real, traceable data

---

## Writing a good request

Say these five things if you know them. Skip anything you don’t.

| Ask for | Example |
|---------|---------|
| **Who / what** | Ahmedabad startups, not “Indian companies” |
| **Fields you must have** | name, website, city |
| **Nice-to-have fields** | founder, email, funding stage |
| **How many** | at least 500 |
| **Format** | CSV and JSON |

The agent confirms this interpretation before any download or scrape.

---

## For the agent

Start with `AGENT.md`. Confirm the request using `MANDATORY_REQUIREMENT.md` before acquiring anything.

| File | When to open it |
|------|-----------------|
| `AGENT.md` | Full workflow |
| `DATA_REQUIREMENT.md` | Turn the ask into a data contract |
| `GITHUB_TOOL_DISCOVERY.md` | Prefer existing tools over custom scrapers |
| `STRATEGY_SELECTOR.md` | Choose how to acquire |
| `SECURITY_AND_ACCESS.md` | Legal / access limits |
| `VALIDATION.md` | Quality checks |
| `OUTPUT_CONTRACT.md` | How to present the result |
| `EXECUTION_LOOP.md` | Retry / fallback loop |
| `EXAMPLE_RUN.md` | Worked example |
