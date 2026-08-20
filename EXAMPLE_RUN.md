# EXAMPLE

A committed, sanitized sample (not a live job dump) is in `examples/ahmedabad-startups/`.
The narrative below is the general method. For that dataset’s exact prompt, see `examples/ahmedabad-startups/REPRODUCE.md`.

## User request

"Find 300 Indian manufacturers of industrial X with company name, website, city, phone and email."

## Step 1 — Requirement

Required:
- company name
- website
- city
- phone
- email

Minimum:
- 300 records

Quality:
- authentic public business information
- source provenance
- deduplicated

## Step 2 — Open-source discovery

Search GitHub for:
- industrial X scraper
- Indian manufacturer scraper
- B2B directory scraper
- company website extractor
- email extraction
- business directory crawler

Inspect the strongest repositories.

## Step 3 — Small test

Run the best candidate against a small sample.

If output contains:
- correct companies
- usable URLs
- acceptable field coverage

continue.

If not, test another tool.

## Step 4 — Multi-source fallback

Suppose no single tool provides all fields.

Use:
- directory source → company + city
- company website → website + contact information
- another public source → missing fields

Merge using domain/company identity.

## Step 5 — Validation

Deduplicate by:
1. canonical domain
2. normalized company name
3. secondary identifiers

Do not merge two companies solely because names look similar.

## Step 6 — Output

Return the dataset plus:
- source provenance
- field completeness
- number of records
- confidence
- limitations

The user should not need to manually coordinate the research process.
