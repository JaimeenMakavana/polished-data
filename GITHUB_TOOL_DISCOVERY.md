# OPEN-SOURCE TOOL DISCOVERY

This is the first discovery stage.

## Goal

Find existing open-source software that can materially reduce the work required to acquire the requested data.

## Search strategy

Run several targeted searches instead of one generic query.

### Search dimensions

1. Exact domain
2. Entity + scraper
3. Entity + crawler
4. Entity + API
5. Entity + dataset
6. Entity + extractor
7. Entity + browser automation
8. Entity + GitHub
9. Source domain + open source
10. Technical implementation terms

## Candidate ranking

Use this conceptual score:

ToolScore =
0.30 Relevance +
0.15 Coverage +
0.15 Executability +
0.10 Maintenance +
0.10 Documentation +
0.10 OutputQuality +
0.05 Reproducibility +
0.05 CommunityEvidence

Adjust weights when the user has explicit priorities.

## Minimum candidate inspection

For each serious candidate inspect:
- README
- repository structure
- package/dependency files
- recent commits
- releases if available
- issues
- examples
- output schema
- authentication requirements
- source URLs
- known limitations

## Strong signals

Increase confidence when:
- the repository directly targets the required source
- code is executable
- recent commits exist
- examples show real output
- tests exist
- issues demonstrate real usage
- output matches the requested schema

## Weak signals

Do not treat these as proof:
- star count
- forks
- SEO ranking
- README claims
- old blog posts

## Output

Produce an internal candidate table:

| Tool | Relevance | Coverage | Maintained | Runnable | Output Fit | Risk | Decision |
|---|---:|---:|---:|---:|---:|---:|---|
| candidate A |  |  |  |  |  |  |  |
| candidate B |  |  |  |  |  |  |  |

Choose the best tool only after inspection.
