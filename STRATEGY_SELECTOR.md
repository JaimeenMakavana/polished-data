# ACQUISITION STRATEGY SELECTOR

Once open-source discovery is complete, select the acquisition method.

## Strategy hierarchy

### Strategy A — Existing open-source tool
Use when a credible tool directly solves most of the requirement.

Best when:
- source is known
- extraction logic already exists
- output can be adapted
- tool is runnable

### Strategy B — Public API
Prefer when an official/public API provides the required data.

Best when:
- structured data is available
- API access is stable
- rate limits are acceptable

### Strategy C — Browser/Web Agent
Use when data is publicly visible but not conveniently exposed through an API/tool.

Best when:
- pages are dynamic
- user-visible information matters
- browser interaction is required

### Strategy D — Direct extraction
Use for simple public pages/files when a browser agent or existing scraper is unnecessary.

### Strategy E — Multi-source acquisition
Use when no single source provides adequate coverage.

Example:
Source A → company identity
Source B → contact/site
Source C → location
Source D → recent activity

### Strategy F — Generate purpose-built tooling
Use only when existing tools are insufficient.

The generated tool should be small, reproducible, and narrowly scoped.

## Decision function

Conceptually:

ExpectedValue(strategy) =
P(success) × DataUtility
− Cost
− Time
− AccessRisk
− MaintenanceBurden

Do not select the strategy with the highest theoretical capability. Select the strategy with the highest expected practical value.

## Fallback

If the selected strategy fails, move to the next strategy rather than stopping immediately.
