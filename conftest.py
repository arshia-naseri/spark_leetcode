import pytest

from common import leetcode
from common.spark import get_spark


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
