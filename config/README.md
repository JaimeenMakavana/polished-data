# Configuration

This project is prompt-and-agent driven. You do not need a config file to request a dataset.

When an agent *does* fetch or geocode, it should follow this optional overlay:

1. **`config/default.yaml`** — committed defaults (timeouts, user-agent, workspace path).
2. **`config/local.yaml`** — your machine-only overrides (gitignored).
3. **Environment variables** — secrets and one-off overrides. Copy `.env.example` to `.env`.

Priority: environment variable > `local.yaml` > `default.yaml`.

Do not put API keys, tokens, or cookies in YAML. Use `.env` or the host secret store.
