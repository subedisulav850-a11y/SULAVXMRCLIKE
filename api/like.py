"""
Like API Endpoint
GET /like?uid={uid}&region={region}

Sends Free Fire likes to the target UID using the like engine.
"""
from http.server import BaseHTTPRequestHandler
import json
import asyncio
import sys
import os
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bot import run_global_like_engine, REGION_CONFIGS


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = dict(urllib.parse.parse_qsl(parsed.query))

        uid = params.get("uid", "").strip()
        region = params.get("region", "BD").upper().strip()

        # --- Validation ---
        if not uid or not uid.isdigit():
            self._respond(400, {"error": "Missing or invalid 'uid'. Must be numeric.", "status": "error"})
            return

        if region not in REGION_CONFIGS:
            self._respond(400, {
                "error": f"Invalid region '{region}'. Supported: BD, SG, IND, EU",
                "status": "error"
            })
            return

        # --- Run like engine ---
        try:
            result = asyncio.run(run_global_like_engine(uid, region))
            self._respond(200, result)
        except Exception as e:
            self._respond(500, {"error": str(e), "status": "error", "uid": uid, "region": region})

    def _respond(self, code: int, body: dict):
        data = json.dumps(body, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format, *args):
        pass
