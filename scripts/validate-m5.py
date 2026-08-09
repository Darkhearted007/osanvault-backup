"""Validate M5 staging artifacts without touching a database or production data."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MIGRATION = ROOT / "services" / "database" / "migrations" / "001_canonical_foundation.sql"

REQUIRED_TABLES = {
    "organizations",
    "users",
    "assets",
    "documents",
    "verification_cases",
    "offerings",
    "investments",
    "treasury_accounts",
    "ledger_entries",
    "tokenization_records",
    "audit_events",
}


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    sql = MIGRATION.read_text(encoding="utf-8")
    missing = [table for table in sorted(REQUIRED_TABLES) if f"CREATE TABLE IF NOT EXISTS osanvault.{table}" not in sql]
    if missing:
        raise SystemExit(f"Missing canonical tables: {', '.join(missing)}")

    legacy = {
        "properties": load_json(ROOT / "api/properties/data.json"),
        "users": load_json(ROOT / "api/users/data.json"),
        "referrals": load_json(ROOT / "api/referrals/data.json"),
    }

    for name, records in legacy.items():
        if not isinstance(records, list):
            raise SystemExit(f"Legacy {name} source is not an array")

    print("M5 staging validation: PASS")
    print(f"Canonical tables: {len(REQUIRED_TABLES)}")
    print(f"Legacy properties records: {len(legacy['properties'])}")
    print(f"Legacy users records: {len(legacy['users'])}")
    print(f"Legacy referral records: {len(legacy['referrals'])}")
    print("Production database: untouched")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
