# EXECUTION LOOP

Use this loop for every data request.

```text
INPUT
  ↓
PARSE REQUIREMENT
  ↓
DEFINE ACCEPTANCE CRITERIA
  ↓
SEARCH OPEN-SOURCE TOOLS
  ↓
EVALUATE CANDIDATES
  ↓
SELECT BEST TOOL
  ↓
TEST SMALL SAMPLE
  ↓
PASS QUALITY CHECK?
  ├─ YES → SCALE ACQUISITION
  └─ NO  → SELECT NEXT STRATEGY
              ↓
        API / WEB / BROWSER / MULTI-SOURCE
              ↓
           VALIDATE
              ↓
           NORMALIZE
              ↓
            OUTPUT
```

## Small-sample rule

Before running an expensive acquisition process, test a small sample.

The test should answer:
- Does the tool actually work?
- Does it reach the intended source?
- Does it return the right entities?
- Are required fields available?
- Is the data quality acceptable?

Only scale after the sample passes.

## Adaptive stopping

Stop when:
- requested quantity is reached, OR
- quality target is reached and additional records have sharply diminishing value, OR
- remaining sources are unlikely to improve the result materially.

Do not keep collecting low-quality records merely to increase the count.
