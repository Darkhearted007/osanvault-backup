"""Minimal M4 canonical API boundary.

Read-only compatibility service. It does not replace existing authentication,
legacy handlers, or production persistence. It is intended for local/staging
validation while the authoritative database is built.
"""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import urlparse

from compat import snapshot


ROUTES = {
    "/api/v1/properties": "properties",
    "/api/v1/users": "users",
    "/api/v1/referrals": "referrals",
}


class ApiHandler(BaseHTTPRequestHandler):
    server_version = "OsanVaultCanonicalAPI/0.1"

    def _send(self, status: int, payload: Any) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        path = urlparse(self.path).path

        if path == "/health":
            self._send(200, {"status": "ok", "service": "osanvault-api", "mode": "legacy-read-only"})
            return

        resource = ROUTES.get(path)
        if resource is None:
            self._send(404, {"error": {"code": "not_found", "message": "Route not found"}})
            return

        try:
            records = snapshot()[resource]
        except (OSError, ValueError, KeyError) as exc:
            self._send(500, {"error": {"code": "data_validation_failed", "message": str(exc)}})
            return

        self._send(200, records)

    def do_POST(self) -> None:  # noqa: N802
        self._send(405, {"error": {"code": "read_only", "message": "M4 compatibility API is read-only"}})

    def do_PUT(self) -> None:  # noqa: N802
        self._send(405, {"error": {"code": "read_only", "message": "M4 compatibility API is read-only"}})

    def do_DELETE(self) -> None:  # noqa: N802
        self._send(405, {"error": {"code": "read_only", "message": "M4 compatibility API is read-only"}})

    def log_message(self, format: str, *args: Any) -> None:
        # Keep the transitional service quiet by default; deployment logging can
        # be provided by the process supervisor.
        return


def run(host: str = "127.0.0.1", port: int = 8080) -> None:
    server = ThreadingHTTPServer((host, port), ApiHandler)
    print(f"ÒsánVault API listening on http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    run()
