"""Deterministic M5 source-to-target reconciliation preflight.

This does not connect to PostgreSQL and does not mutate production or staging.
It validates that the legacy compatibility collections contain enough
information to construct the canonical staging entities and reports the
expected source-to-target cardinalities.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str) -> list[dict]:
    path = ROOT / "api" / name / "data.json"
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, list):
        raise SystemExit(f"{name}: expected JSON array")
    if not all(isinstance(item, dict) for item in value):
        raise SystemExit(f"{name}: every record must be an object")
    return value


def require(records: list[dict], fields: set[str], name: str) -> None:
    for index, record in enumerate(records):
        missing = fields.difference(record)
        if missing:
            raise SystemExit(f"{name}[{index}] missing: {sorted(missing)}")


def main() -> int:
    properties = load("properties")
    users = load("users")
    referrals = load("referrals")

    require(properties, {"id", "name", "location", "price", "rentYield", "tokenized"}, "properties")
    require(users, {"userId", "name", "properties", "netBalance"}, "users")
    require(referrals, {"userId", "referrals", "netEarned"}, "referrals")

    property_names = {record["name"] for record in properties}
    user_ids = {record["userId"] for record in users}
    referral_ids = {record["userId"] for record in referrals}

    for record in users:
        unknown = set(record["properties"]) - property_names
        if unknown:
            raise SystemExit(f"users/{record['userId']}: unknown properties {sorted(unknown)}")

    if referral_ids - user_ids:
        raise SystemExit(f"referrals reference unknown users: {sorted(referral_ids - user_ids)}")

    print("M5 reconciliation preflight: PASS")
    print(f"legacy properties -> canonical assets: {len(properties)}")
    print(f"legacy users -> canonical users: {len(users)}")
    print(f"legacy properties -> canonical offerings candidates: {len(properties)}")
    print(f"legacy referrals -> canonical audit/reconciliation subjects: {len(referrals)}")
    print("PostgreSQL: not connected")
    print("Production data: untouched")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
