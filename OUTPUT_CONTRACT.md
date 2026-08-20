# OUTPUT CONTRACT

The final response should be useful without requiring the user to understand the internal process.

## Required sections

### 1. Result
Provide the requested structured data.

### 2. What was found
State:
- number of usable records
- scope
- major sources
- selected acquisition strategy

### 3. Quality
Report:
- completeness
- provenance
- freshness
- confidence
- known gaps

### 4. How it was obtained
Briefly explain:
- open-source tool discovered, if any
- other acquisition methods used
- whether multiple sources were combined

### 5. Limitations
Be explicit about:
- unavailable fields
- inaccessible sources
- stale data
- unresolved conflicts
- coverage limitations

## Example summary

```text
Requested: 500 Indian manufacturers with X, Y, Z fields

Usable records: 327
Required-field completeness: 91%
Primary sources: 4
Open-source tool used: <repo>
Secondary strategy: browser research
Overall confidence: Medium-High

Main limitation:
Phone numbers were unavailable for 38% of otherwise valid records.
```

Never hide the gap between requested quantity and achieved quantity.
