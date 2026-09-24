"""Make practice.py files from practice_template.py files.

Layout: problems/<problem>/practice.py and problems/<problem>/_internal/practice_template.py.
"""

import shutil
from pathlib import Path

PROBLEMS_DIR = Path(__file__).resolve().parent.parent / "problems"
TEMPLATE = "_internal/practice_template.py"
PRACTICE = "practice.py"


def problem_dirs() -> list[Path]:
    return sorted(p.parent.parent for p in PROBLEMS_DIR.glob(f"*/{TEMPLATE}"))


def ensure_practice_files() -> None:
    """Copy the template to practice.py in each problem that has no practice.py."""
    for problem in problem_dirs():
        if not (problem / PRACTICE).exists():
            shutil.copyfile(problem / TEMPLATE, problem / PRACTICE)


def reset(problem: Path) -> None:
    """Replace practice.py with a blank copy of the template."""
    shutil.copyfile(problem / TEMPLATE, problem / PRACTICE)
