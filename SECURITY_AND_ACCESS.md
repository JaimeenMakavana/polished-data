# SECURITY, ACCESS & ETHICAL BOUNDARIES

The agent may use public web resources and open-source software, but must operate within reasonable access boundaries.

## Prefer

- official APIs
- public datasets
- public pages
- documented interfaces
- open-source software with clear licensing

## Do not

- bypass authentication
- defeat CAPTCHAs
- circumvent paywalls
- steal credentials
- evade technical access controls
- access private/non-public information
- fabricate authorization

## Secrets

Never commit or expose:
- API keys
- passwords
- session cookies
- access tokens
- private credentials

Use environment variables or the platform's secret-management facilities.
See `.env.example` and `config/README.md`. Vulnerability reports: `SECURITY.md`.

## Repository safety

Treat third-party repositories as untrusted code.

Before executing:
- inspect install scripts
- inspect dependency files
- inspect obvious network/file-system behavior
- avoid unnecessary privileges
- prefer isolated execution when available

## Licensing

Check repository license before incorporating code into a distributed product.

License compatibility is part of tool selection.
