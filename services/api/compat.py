"""Read-only compatibility adapter for the legacy JSON data surface.

This module intentionally performs no writes. It provides the M4 transition
boundary while the canonical database is developed in staging.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
LEGACY_API = ROOT / "api"


def _load(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def properties() -> list[dict[str, Any]]:
    return _load(LEGACY_API / "properties" / "data.json")


def users() -> list[dict[str, Any]]:
    return _load(LEGACY_API / "users" / "data.json")


def referrals() -> list[dict[str, Any]]:
    return _load(LEGACY_API / "referrals" / "data.json")


def validate_collection(name: str, records: Any) -> None:
    if not isinstance(records, list):
        raise ValueError(f"{name} must be an array")

    required = {
        "properties": {"id", "name", "location", "price", "rentYield", "image", "tokenized"},
        "users": {"userId", "name", "properties", "netBalance"},
        "referrals": {"userId", "referrals", "netEarned"},
    }[name]

    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"{name}[{index}] must be an object")
        missing = required.difference(record)
        if missing:
            raise ValueError(f"{name}[{index}] missing: {sorted(missing)}")


def snapshot() -> dict[str, list[dict[str, Any]]]:
    data = {
        "properties": properties(),
        "users": users(),
        "referrals": referrals(),
    }
    for name, records in data.items():
        validate_collection(name, records)
    return data
