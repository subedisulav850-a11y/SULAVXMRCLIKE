"""
Vercel Serverless Webhook Handler — MRC x SULAV FF Bot
Receives Telegram updates and dispatches them through aiogram.
"""
from http.server import BaseHTTPRequestHandler
import json
import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aiogram.types import Update
from bot import dp, bot


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            data = json.loads(body)
            asyncio.run(self._dispatch(data))
        except Exception as e:
            print(f"[webhook] Error: {e}")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"ok":true}')

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"MRC x SULAV FF Bot - Webhook Active! v2.0")

    @staticmethod
    async def _dispatch(data: dict):
        update = Update.model_validate(data)
        await dp.process_update(update)

    def log_message(self, format, *args):
        pass
