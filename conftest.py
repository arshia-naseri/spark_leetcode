import pytest

from common.spark import get_spark


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
