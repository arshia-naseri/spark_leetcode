import json
from pathlib import Path

import pytest

from common import leetcode
from common.practice import problem_dirs
from common.spark import get_spark


def pytest_addoption(parser):
    group = parser.getgroup("leetcode")
    group.addoption(
        "--solution",
        action="store_true",
        help="Run only the reference answers. Default: only the practice files.",
    )
    group.addoption(
        "--all",
        action="store_true",
        dest="all_modules",
        help="Run the practice files and the reference answers.",
    )
    group.addoption(
        "--leetcode-json",
        metavar="PATH",
        help="Write the result of each test case as JSON to PATH. The web UI uses this.",
    )


def _expand(arg: str) -> list[str]:
    """Change a problem name prefix (p0181 or 181) to the problem folder path."""
    if arg.startswith("-") or Path(arg.split("::")[0]).exists():
        return [arg]
    prefix = f"p{int(arg):04d}" if arg.isdigit() else arg
    matches = [str(p) for p in problem_dirs() if p.name.startswith(prefix)]
    return matches or [arg]


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Let "uv run pytest p0181" select the folder of problem 181.
    config.args = [path for arg in config.args for path in _expand(arg)]


def pytest_collection_modifyitems(config, items):
    """Keep only practice tests, or only solution tests with --solution.

    Do not filter when -k or --all is given.
    """
    if config.getoption("keyword") or config.getoption("all_modules"):
        return
    keep = "solution" if config.getoption("solution") else "practice"
    selected, deselected = [], []
    for item in items:
        callspec = getattr(item, "callspec", None)
        module_name = callspec.params.get("module_name") if callspec else None
        (deselected if module_name not in (None, keep) else selected).append(item)
    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = selected


def pytest_sessionstart(session):
    # Use the same color setting as pytest (--color, NO_COLOR, FORCE_COLOR).
    # A check of isatty() does not work, because pytest captures stdout.
    leetcode.set_color(session.config.get_terminal_writer().hasmarkup)


@pytest.fixture(scope="session")
def spark():
    session = get_spark("leetcode-tests")
    yield session
    session.stop()


def pytest_terminal_summary(terminalreporter):
    """Show the output of each accepted answer."""
    outputs = [
        value
        for report in terminalreporter.stats.get("passed", [])
        for name, value in report.user_properties
        if name == "leetcode_output"
    ]
    if outputs:
        terminalreporter.section("Output")
        for text in outputs:
            terminalreporter.write_line(text)



# Data for --leetcode-json: the case results and the errors that stop collection.
_json_results: list[dict] = []
_json_errors: list[str] = []


def pytest_collectreport(report):
    if report.failed:
        _json_errors.append(str(report.longrepr))


def pytest_runtest_logreport(report):
    for name, value in report.user_properties:
        if name == "leetcode_result" and report.when == "call":
            _json_results.append({"nodeid": report.nodeid, **value})
    if report.failed and report.when != "call":
        _json_errors.append(str(report.longrepr))


def pytest_sessionfinish(session):
    path = session.config.getoption("leetcode_json")
    if path:
        data = {"results": _json_results, "errors": _json_errors}
        Path(path).write_text(json.dumps(data))
