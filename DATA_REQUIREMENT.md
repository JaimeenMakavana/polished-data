# DATA REQUIREMENT SPECIFICATION

Before acquisition, construct this internal specification.

## Required schema

```yaml
request:
  natural_language: ""
  objective: ""

target:
  entity_type: ""
  geography: ""
  time_range: ""

fields:
  required: []
  preferred: []
  optional: []

constraints:
  minimum_records: null
  maximum_records: null
  freshness: ""
  completeness_target: ""
  authenticity_requirement: ""
  acceptable_sources: []
  excluded_sources: []

output:
  format: ""
  schema: {}

quality:
  minimum_confidence: ""
  provenance_required: true
```

## Interpretation rules

### Required vs preferred
A required field must be present for a record to count as complete.

A preferred field improves usefulness but should not block acquisition.

### Authenticity
Authenticity means the record can be traced to a credible source. It does not mean every field is independently verified.

### Completeness
Report completeness separately from quantity.

Example:
- 1,000 records with 50% required-field coverage is not equivalent to
- 500 records with 95% required-field coverage.

### Freshness
If the user requests current/recent information, source timestamps must be considered.

## Ambiguity handling

If the user says "all", interpret it as:
> all discoverable records within the defined scope, not literally every record on the internet.

If the user says "authentic", require provenance and distinguish source-published information from agent inference.
