# Contributing

Thanks for helping improve polished-data. This repo is mostly **agent instructions** plus a small validation/example layer. Most useful contributions are clearer docs, safer acquisition rules, and better examples.

Please read the [Code of Conduct](CODE_OF_CONDUCT.md) first.

## What to change where

| You want to… | Edit |
|--------------|------|
| How the agent runs a job | `AGENT.md`, `EXECUTION_LOOP.md` |
| Requirement / confirmation gate | `MANDATORY_REQUIREMENT.md`, `DATA_REQUIREMENT.md` |
| Tool / strategy choice | `GITHUB_TOOL_DISCOVERY.md`, `STRATEGY_SELECTOR.md` |
| Legal / access limits | `SECURITY_AND_ACCESS.md`, `SECURITY.md` |
| Output shape and quality | `OUTPUT_CONTRACT.md`, `VALIDATION.md` |
| Pipeline overview | `ARCHITECTURE.md` |
| Defaults (timeouts, workspace path) | `config/default.yaml`, `.env.example` |
| Worked sample | `examples/ahmedabad-startups/` |

Do not commit `data-workspace/` (live job artifacts, raw HTML, local paths). Ship sanitized samples under `examples/` instead.

## Development setup

1. Clone the repo.
2. Optional: copy `.env.example` to `.env` and fill only what you need.
3. Optional: use `config/local.yaml` for machine overrides (gitignored).
4. Run the repo check:

```bash
python scripts/validate_repo.py
```

You do not need a Python package install for the docs themselves.

## Pull requests

1. Open an issue first for behavior or policy changes (not required for typos).
2. Keep the PR focused: one concern per PR.
3. Use the pull request template.
4. If you change agent rules, say how an agent should behave differently.
5. If you add an example dataset, sanitize it (no emails, phones, secrets, or absolute local paths) and document how to reproduce it.

## Issues

Use the issue templates:

- **Bug** — agent did the wrong thing, docs contradict each other, validation failed
- **Data quality** — example or documented output is incomplete or misleading
- **Feature** — new instruction, strategy, or output format

Security issues go to [SECURITY.md](SECURITY.md), not the public tracker.
