# MANDATORY REQUIREMENT CONFIRMATION GATE

This is a **hard gate**.

The agent MUST NOT begin data discovery, GitHub searching, browser research, scraping, API calls, tool installation, or data acquisition until the user has explicitly confirmed the interpreted requirement.

---

## 1. REQUIREMENT → INTERPRETATION

When the user gives a data request:

1. Do NOT immediately execute it.
2. Parse the request.
3. Construct the internal Data Contract.
4. Convert the Data Contract into a concise human-readable requirement summary.
5. Present the interpretation to the user.
6. Ask the user to confirm whether the interpretation is correct.
7. Wait for explicit confirmation.

The agent must treat this confirmation as a hard dependency.

---

# 2. WHAT MUST BE CONFIRMED

The confirmation summary should cover the dimensions that materially affect the result.

### Objective

What exactly is the user trying to obtain?

### Target

What entities/items/data are being requested?

### Scope

Geography, industry, category, time period, etc.

### Fields

Which fields are:

* required
* preferred
* optional

### Quantity

* target quantity
* minimum acceptable quantity

### Quality

* authenticity
* completeness
* freshness
* confidence

### Sources

Preferred or prohibited sources.

### Processing

Whether the user wants:

* deduplication
* enrichment
* classification
* ranking
* scoring
* filtering
* aggregation

### Output

Format and schema.

### Destination

Where the result should be stored/delivered.

---

# 3. CONFIRMATION FORMAT

Use a short confirmation summary.

Example:

```text
Before I start, this is my understanding:

Objective:
Find potential industrial buyers for Product X.

Scope:
India.

Required fields:
- Company name
- Website
- City
- Contact information

Quantity:
Target: 500
Minimum acceptable: 300

Quality:
- Publicly verifiable
- Deduplicated
- Prefer recent information

Sources:
Public web + GitHub/open-source tools + public APIs.
No paid databases.

Processing:
Rank buyers by estimated purchase likelihood.

Output:
JSON.

Storage:
Create a separate acquisition workspace without modifying the existing application architecture.

Please confirm:
"Yes, this is correct."
```

---

# 4. DO NOT START WORK BEFORE CONFIRMATION

Until confirmation:

### DO NOT

* search GitHub
* search websites
* launch browser agents
* install repositories
* call APIs
* scrape pages
* create scrapers
* download datasets
* modify project files
* create acquisition tooling
* create large folders
* begin data collection

The only work allowed before confirmation is **requirement interpretation**.

---

# 5. HANDLING USER CORRECTIONS

If the user says:

> "No, I need 1,000 companies."

Update the Data Contract.

Then show the updated requirement again.

Do NOT begin execution until the revised requirement is confirmed.

Example:

```text
Updated requirement:

Quantity:
Target: 1,000
Minimum: 700

Everything else remains unchanged.

Please confirm.
```

---

# 6. PARTIAL CONFIRMATION

If the user confirms only some aspects:

> "Everything is correct except I don't need email."

Update the contract.

Then ask for confirmation of the complete revised requirement.

Do not interpret partial agreement as authorization to begin.

---

# 7. AMBIGUITY

If the request is ambiguous, do not make assumptions about high-impact variables.

Examples:

* "all companies"
* "latest data"
* "large dataset"
* "authentic companies"
* "potential buyers"
* "good quality"
* "recent startups"

Clarify only the ambiguity that materially affects execution.

Avoid asking unnecessary questions.

---

# 8. LOW-IMPACT DEFAULTS

The agent may automatically choose reasonable defaults for low-impact decisions.

For example:

* JSON vs CSV when the user has not specified a format
* temporary file naming
* job ID
* internal workspace structure
* intermediate processing format

These defaults should be stated in the confirmation summary if they materially affect the result.

---

# 9. EXPLICIT CONFIRMATION SIGNALS

Accept confirmation such as:

* "yes"
* "confirmed"
* "correct"
* "go ahead"
* "that's right"
* "proceed"
* "start"
* "do it"

Do NOT require the exact phrase:

> "Yes, I confirm."

Natural confirmation is sufficient.

---

# 10. AFTER CONFIRMATION

Only after confirmation:

```text
CONFIRMED
   ↓
Create isolated job workspace
   ↓
Save data-contract.yaml
   ↓
Search open-source tools FIRST
   ↓
Evaluate candidates
   ↓
Select acquisition strategy
   ↓
Run small sample
   ↓
Validate
   ↓
Scale
   ↓
Transform
   ↓
Generate requested output
   ↓
Generate quality report
   ↓
Update manifest
   ↓
Return result
```

---

# 11. ARCHITECTURAL PRINCIPLE

The entire system should behave as two separate phases:

```text
PHASE 0
REQUIREMENT NEGOTIATION
        ↓
USER CONFIRMATION
        ↓
PHASE 1
AUTONOMOUS EXECUTION
```

The boundary between these phases is explicit.

**No execution before confirmation.**

---

# 12. FINAL RULE

The agent's first responsibility is not to find data.

Its first responsibility is to ensure:

> **"I understand exactly what data the user wants."**

Only after the user confirms:

> **"Yes, that's exactly what I need."**

does the agent receive permission to begin autonomous data acquisition.
