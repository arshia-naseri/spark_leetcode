"""Start the web UI.

Usage:
    uv run python -m webui               # http://127.0.0.1:8000, opens the browser
    uv run python -m webui --port 8080   # other port
    uv run python -m webui --no-browser  # do not open the browser
"""

import argparse
import threading
import webbrowser

from .server import serve


def main() -> None:
    parser = argparse.ArgumentParser(prog="python -m webui", description="Spark LeetCode web UI")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--no-browser", action="store_true", help="Do not open the browser.")
    args = parser.parse_args()
    if not args.no_browser:
        url = f"http://{args.host}:{args.port}/"
        threading.Timer(0.5, webbrowser.open, [url]).start()
    serve(args.host, args.port)


if __name__ == "__main__":
    main()
