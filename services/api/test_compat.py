from __future__ import annotations

import json
import threading
import unittest
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path

from compat import snapshot, validate_collection
from server import ApiHandler

ROOT = Path(__file__).resolve().parents[2]


class CompatibilityDataTests(unittest.TestCase):
    def test_legacy_collections_match_v1_contracts(self) -> None:
        data = snapshot()
        self.assertGreaterEqual(len(data["properties"]), 1)
        self.assertGreaterEqual(len(data["users"]), 1)
        self.assertGreaterEqual(len(data["referrals"]), 1)

    def test_invalid_collection_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            validate_collection("properties", [{"id": 1}])

    def test_contract_files_are_valid_json(self) -> None:
        contracts = ROOT / "services" / "api" / "contracts"
        for path in contracts.glob("*.v1.json"):
            with path.open(encoding="utf-8") as handle:
                payload = json.load(handle)
            self.assertEqual(payload.get("type"), "array")


class ApiRuntimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), ApiHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.port = cls.server.server_address[1]

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def request(self, path: str):
        connection = HTTPConnection("127.0.0.1", self.port, timeout=3)
        connection.request("GET", path)
        response = connection.getresponse()
        body = response.read()
        content_type = response.getheader("Content-Type")
        connection.close()
        return response.status, content_type, body

    def test_health(self) -> None:
        status, content_type, body = self.request("/health")
        self.assertEqual(status, 200)
        self.assertIn("application/json", content_type)
        self.assertIn(b'"status": "ok"', body)

    def test_properties_endpoint(self) -> None:
        status, _, body = self.request("/api/v1/properties")
        self.assertEqual(status, 200)
        self.assertTrue(json.loads(body))

    def test_users_endpoint(self) -> None:
        status, _, body = self.request("/api/v1/users")
        self.assertEqual(status, 200)
        self.assertTrue(json.loads(body))

    def test_referrals_endpoint(self) -> None:
        status, _, body = self.request("/api/v1/referrals")
        self.assertEqual(status, 200)
        self.assertTrue(json.loads(body))

    def test_unknown_route(self) -> None:
        status, _, _ = self.request("/api/v1/unknown")
        self.assertEqual(status, 404)


if __name__ == "__main__":
    unittest.main()
