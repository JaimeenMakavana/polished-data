# Architecture

Polished Data is not a hosted scraper. It is a **repeatable agent workflow**: the user states a data need; the agent compiles a contract, acquires from public sources, validates, and writes files into an isolated job folder.

```text
User request
    → requirement compiler (data contract)
    → confirmation gate (user must OK)
    → open-source tool discovery
    → strategy selection
    → acquisition (public APIs, datasets, pages)
    → transform / dedupe / enrich
    → validation + quality report
    → output adapter (CSV / JSON / …)
    → data-workspace/jobs/<job-id>/
```

## Documents vs runtime

| Layer | Lives in | Role |
|-------|----------|------|
| Instructions | `AGENT.md` and sibling `*.md` | What the agent must do |
| Defaults | `config/default.yaml`, `.env` | Optional timeouts, UA, geocoder URL |
| Job state | `data-workspace/jobs/<job-id>/` (gitignored) | One run, isolated |
| Examples | `examples/` | Sanitized samples you can clone and inspect |

The application (if any) around this repo is left untouched. Jobs never write into source trees unless the user asks for integration.

## One job, one workspace

```text
data-workspace/jobs/<job-id>/
  requirement/data-contract.yaml
  discovery/
  tools/
  acquisition/raw/
  processing/
  validation/quality-report.json
  output/result.csv | result.json | README.md
  manifest.json
```

`job-id` is unique (for example `job_2026_08_20_ahmedabad_startups`). Do not overwrite another job.

## Decision gates

1. **Confirmation** — `MANDATORY_REQUIREMENT.md`. No fetch until the user confirms the interpreted contract.
2. **Tool discovery first** — `GITHUB_TOOL_DISCOVERY.md`. Prefer an existing tool over a new scraper.
3. **Strategy** — `STRATEGY_SELECTOR.md`. Highest expected practical value, not most stars.
4. **Access** — `SECURITY_AND_ACCESS.md`. Public sources only; no login bypass.
5. **Honesty** — `VALIDATION.md` / `OUTPUT_CONTRACT.md`. Report gaps; never invent rows.

## Configuration

See `config/README.md`. Secrets stay in environment variables. YAML holds non-secret defaults.

## Where to read next

- Operator loop: `README.md`
- Full agent procedure: `AGENT.md`
- Worked sample: `examples/ahmedabad-startups/README.md`
