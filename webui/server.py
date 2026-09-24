"""Local web server for the practice UI. It uses only the Python standard library.

API:
    GET  /api/problems              list of problems
    GET  /api/problems/<name>       question, code, solution, and test cases
    PUT  /api/problems/<name>/code  save the code to practice.py
    POST /api/problems/<name>/run   save the code, run the tests, return the results
    POST /api/problems/<name>/reset reset practice.py to the template
"""

import json
import re
import subprocess
import sys
import tempfile
import threading
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from common.practice import PRACTICE, TEMPLATE, problem_dirs, reset

from .cases import load_cases

ROOT = Path(__file__).resolve().parent.parent
STATIC = Path(__file__).resolve().parent / "static"
STATIC_TYPES = {".html": "text/html", ".js": "text/javascript", ".css": "text/css"}
RUN_TIMEOUT_S = 300

# Only one test run at a time. Each run starts its own Spark JVM.
_run_lock = threading.Lock()


def _problems() -> dict[str, Path]:
    return {p.name: p for p in problem_dirs()}


def _title(problem: Path) -> str:
    first = (problem / "question.md").read_text().splitlines()[0]
    return first.lstrip("# ").strip()


def _summary(problem: Path) -> dict:
    practice, template = problem / PRACTICE, problem / TEMPLATE
    return {
        "name": problem.name,
        "number": int(problem.name[1:5]),
        "title": _title(problem),
        "difficulty": problem.parent.name,
        "attempted": practice.exists() and practice.read_text() != template.read_text(),
    }


def _details(problem: Path) -> dict:
    return {
        **_summary(problem),
        "question": (problem / "question.md").read_text(),
        "code": (problem / PRACTICE).read_text(),
        "solution": (problem / "_internal" / "solution.py").read_text(),
        "cases": load_cases(problem),
    }


def _run(problem: Path, method: str, count: int) -> dict:
    """Run the practice tests of one method with pytest. Return the case results."""
    test_file = (problem / "_internal" / "test_cases.py").relative_to(ROOT)
    node_ids = [f"{test_file}::test_case[case{i}-practice-{method}]" for i in range(1, count + 1)]
    with tempfile.TemporaryDirectory() as tmp:
        report = Path(tmp) / "report.json"
        cmd = [sys.executable, "-m", "pytest", *node_ids, "--color=no", "-p", "no:cacheprovider"]
        cmd += ["--leetcode-json", str(report)]
        try:
            proc = subprocess.run(
                cmd, cwd=ROOT, capture_output=True, text=True, timeout=RUN_TIMEOUT_S
            )
        except subprocess.TimeoutExpired:
            return {"results": [], "errors": [f"Time Limit Exceeded: more than {RUN_TIMEOUT_S} s"]}
        if not report.exists():
            return {"results": [], "errors": [proc.stdout + proc.stderr]}
        data = json.loads(report.read_text())
    if not data["results"] and not data["errors"]:
        data["errors"].append(proc.stdout + proc.stderr)
    return data


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):  # noqa: A002
        pass

    def _send(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, data, status: int = HTTPStatus.OK) -> None:
        self._send(status, json.dumps(data).encode(), "application/json")

    def _body(self) -> dict:
        length = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(length) or b"{}")

    def _problem(self, name: str) -> Path | None:
        problem = _problems().get(name)
        if problem is None:
            self._json({"error": f"No problem: {name}"}, HTTPStatus.NOT_FOUND)
        return problem

    def do_GET(self):  # noqa: N802
        path = self.path.split("?")[0]
        if path == "/api/problems":
            return self._json([_summary(p) for p in _problems().values()])
        if m := re.fullmatch(r"/api/problems/(\w+)", path):
            if problem := self._problem(m[1]):
                return self._json(_details(problem))
            return None
        if path.startswith("/static/"):
            file = STATIC / path.removeprefix("/static/")
            if file.parent == STATIC and file.suffix in STATIC_TYPES and file.is_file():
                return self._send(HTTPStatus.OK, file.read_bytes(), STATIC_TYPES[file.suffix])
            return self._json({"error": "Not found"}, HTTPStatus.NOT_FOUND)
        # All other paths are pages of the single-page app.
        return self._send(HTTPStatus.OK, (STATIC / "index.html").read_bytes(), "text/html")

    def do_PUT(self):  # noqa: N802
        m = re.fullmatch(r"/api/problems/(\w+)/code", self.path)
        if not m:
            return self._json({"error": "Not found"}, HTTPStatus.NOT_FOUND)
        if problem := self._problem(m[1]):
            (problem / PRACTICE).write_text(self._body()["code"])
            return self._json({"saved": True})
        return None

    def do_POST(self):  # noqa: N802
        m = re.fullmatch(r"/api/problems/(\w+)/(run|reset)", self.path)
        if not m:
            return self._json({"error": "Not found"}, HTTPStatus.NOT_FOUND)
        problem = self._problem(m[1])
        if problem is None:
            return None
        if m[2] == "reset":
            reset(problem)
            return self._json({"code": (problem / PRACTICE).read_text()})

        body = self._body()
        method = body.get("method", "dataframe")
        if method not in ("dataframe", "sql"):
            return self._json({"error": f"Bad method: {method}"}, HTTPStatus.BAD_REQUEST)
        (problem / PRACTICE).write_text(body["code"])
        with _run_lock:
            return self._json(_run(problem, method, len(load_cases(problem))))


def serve(host: str, port: int) -> None:
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"Spark LeetCode UI: http://{host}:{port}  (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
