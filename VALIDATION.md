# DATA VALIDATION & TRUST

Acquisition is not success. The output must be evaluated.

## Record-level checks

For every record:
- required fields present?
- source identified?
- duplicate?
- values plausible?
- source current enough?
- conflicts with another source?

## Dataset-level checks

Calculate or estimate:
- record count
- unique record count
- required-field completeness
- source coverage
- duplicate percentage
- freshness
- conflict percentage
- verification percentage

## Provenance

Every important field should be traceable where practical.

Preferred provenance model:

```yaml
record:
  source_url: ""
  source_name: ""
  retrieved_at: ""
  source_type: ""
  verification_status: "verified|partially_verified|unverified"
```

## Confidence

Use confidence as a transparent assessment, not fake mathematical precision.

Example:
- High: directly supported by a credible primary/public source
- Medium: supported by credible secondary evidence
- Low: inferred, stale, weakly sourced, or conflicting

## Never

- fabricate missing values
- convert inference into fact
- hide conflicting sources
- claim exhaustive coverage without evidence
- claim 100% authenticity merely because data came from a website
