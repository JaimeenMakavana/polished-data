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

A finished, sanitized sample (20 rows, no emails/phones/founders): [`examples/ahmedabad-startups/`](examples/ahmedabad-startups/). How to re-run it: [`examples/ahmedabad-startups/REPRODUCE.md`](examples/ahmedabad-startups/REPRODUCE.md).

Live job folders under `data-workspace/` are local only (gitignored).

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

## Configuration (optional)

You can run jobs with no config. If you want defaults or secrets:

| File | Purpose |
|------|---------|
| [`config/default.yaml`](config/default.yaml) | Timeouts, user-agent, workspace path, geocoder URL |
| [`config/local.yaml`](config/README.md) | Machine-only overrides (gitignored) |
| [`.env.example`](.env.example) | Copy to `.env` for tokens and env overrides |

Details: [`config/README.md`](config/README.md). Never commit `.env` or API keys.

---

## How it is put together

[`ARCHITECTURE.md`](ARCHITECTURE.md) is the single overview of the pipeline, job folders, and decision gates. Agent playbooks (`AGENT.md` and the rest) are the detailed procedures.

---

## Contributing

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to change docs, examples, and CI
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
- [`SECURITY.md`](SECURITY.md) — private vulnerability reports
- [`CHANGELOG.md`](CHANGELOG.md)

Issues and pull requests use the templates under `.github/`. CI runs `python scripts/validate_repo.py` on every push.

---

## For the agent

Start with `AGENT.md`. Confirm the request using `MANDATORY_REQUIREMENT.md` before acquiring anything.

| File | When to open it |
|------|-----------------|
| `ARCHITECTURE.md` | Pipeline overview |
| `AGENT.md` | Full workflow |
| `DATA_REQUIREMENT.md` | Turn the ask into a data contract |
| `GITHUB_TOOL_DISCOVERY.md` | Prefer existing tools over custom scrapers |
| `STRATEGY_SELECTOR.md` | Choose how to acquire |
| `SECURITY_AND_ACCESS.md` | Legal / access limits |
| `VALIDATION.md` | Quality checks |
| `OUTPUT_CONTRACT.md` | How to present the result |
| `EXECUTION_LOOP.md` | Retry / fallback loop |
| `EXAMPLE_RUN.md` | Worked example |
