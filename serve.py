"""Serve this folder locally when opening index.html directly is restricted."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser

root = Path(__file__).resolve().parent
server = ThreadingHTTPServer(('127.0.0.1', 8000), partial(SimpleHTTPRequestHandler, directory=str(root)))
webbrowser.open('http://127.0.0.1:8000/')
print('Explorer running at http://127.0.0.1:8000/ - press Ctrl+C to stop.')
server.serve_forever()
