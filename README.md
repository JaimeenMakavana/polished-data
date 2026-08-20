# Autonomous Data Discovery & Acquisition System

This specification defines an agent workflow for Cursor, Codex, Claude Code, or another agentic coding environment.

## Objective

Given a natural-language data requirement, autonomously find the most reliable and practical path to obtain the requested data with minimal human cognitive load.

The system should prefer existing open-source tools first, then select among web research, browser automation, public APIs, datasets, direct extraction, or generated tooling based on the requirement.

## Core principle

> The user specifies WHAT data they need. The agent determines WHERE it exists and HOW to acquire, verify, normalize, and deliver it.

## Primary workflow

Requirement → Specification → Open-source tool discovery → Tool evaluation → Strategy selection → Acquisition → Validation → Normalization → Evidence → Output

## Non-goals

- Do not pretend unavailable data exists.
- Do not fabricate records.
- Do not blindly trust GitHub stars or search ranking.
- Do not scrape sources in violation of access controls or applicable terms.
- Do not optimize for quantity at the expense of authenticity.

## Required behavior

Every run must produce:
1. A precise interpretation of the request.
2. A discovery report.
3. A selected acquisition strategy.
4. Evidence for important sources/tools.
5. A quality assessment.
6. The requested data or an explicit explanation of what could not be obtained.
