"""Fail CI if community files, config, or the example dataset are missing or malformed."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENT.md",
    "ARCHITECTURE.md",
    "CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "SECURITY_AND_ACCESS.md",
    ".env.example",
    "config/default.yaml",
    "config/README.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/bug.yml",
    ".github/ISSUE_TEMPLATE/feature.yml",
    ".github/ISSUE_TEMPLATE/data-quality.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/validate.yml",
    "examples/ahmedabad-startups/README.md",
    "examples/ahmedabad-startups/REPRODUCE.md",
    "examples/ahmedabad-startups/sample.csv",
    "examples/ahmedabad-startups/sample.json",
    "examples/ahmedabad-startups/schema.json",
    "examples/ahmedabad-startups/data-contract.yaml",
    "examples/ahmedabad-startups/quality-report.json",
]

SAMPLE_COLUMNS = [
    "company_name",
    "website",
    "city",
    "sector",
    "latitude",
    "longitude",
    "verification_status",
    "description",
    "funding_stage",
    "founding_year",
    "source_url",
    "source_name",
    "geocode_status",
]

FORBIDDEN_SAMPLE_COLUMNS = {"email", "phone", "founder"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    missing = [rel for rel in REQUIRED_FILES if not (ROOT / rel).is_file()]
    if missing:
        fail("missing required files:\n  " + "\n  ".join(missing))

    env_example = (ROOT / ".env.example").read_text(encoding="utf-8")
    if "GITHUB_TOKEN=" in env_example and "ghp_" in env_example:
        fail(".env.example must not contain a real token")

    default_yaml = (ROOT / "config/default.yaml").read_text(encoding="utf-8")
    for key in ("workspace:", "acquisition:", "geocoding:", "output:"):
        if key not in default_yaml:
            fail(f"config/default.yaml missing section {key}")

    schema = json.loads((ROOT / "examples/ahmedabad-startups/schema.json").read_text(encoding="utf-8"))
    required_fields = schema["required_for_complete_row"]

    sample_path = ROOT / "examples/ahmedabad-startups/sample.json"
    records = json.loads(sample_path.read_text(encoding="utf-8"))
    if not isinstance(records, list) or len(records) < 10 or len(records) > 50:
        fail("sample.json must contain 10–50 records")

    for i, row in enumerate(records):
        if not isinstance(row, dict):
            fail(f"sample.json[{i}] is not an object")
        leak = FORBIDDEN_SAMPLE_COLUMNS.intersection(row)
        if leak:
            fail(f"sample.json[{i}] includes sanitized-out fields: {sorted(leak)}")
        if "D:\\\\" in json.dumps(row) or "/Users/" in json.dumps(row):
            fail(f"sample.json[{i}] looks like it contains a local filesystem path")
        for field in ("company_name", "city", "source_url"):
            if not row.get(field):
                fail(f"sample.json[{i}] missing {field}")

    with (ROOT / "examples/ahmedabad-startups/sample.csv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != SAMPLE_COLUMNS:
            fail(f"sample.csv columns mismatch: {reader.fieldnames}")
        csv_rows = list(reader)
    if len(csv_rows) != len(records):
        fail("sample.csv and sample.json row counts differ")

    quality = json.loads(
        (ROOT / "examples/ahmedabad-startups/quality-report.json").read_text(encoding="utf-8")
    )
    for key in ("records_total", "records_with_website", "job_id"):
        if key not in quality:
            fail(f"quality-report.json missing {key}")

    print("validate_repo: ok")
    print(f"  files: {len(REQUIRED_FILES)}")
    print(f"  sample rows: {len(records)}")
    print(f"  required complete-row fields: {len(required_fields)}")


if __name__ == "__main__":
    main()
