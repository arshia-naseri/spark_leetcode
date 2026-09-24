"""Make practice.py files from practice_template.py files.

Layout: problems/<difficulty>/<problem>/practice.py and
problems/<difficulty>/<problem>/_internal/practice_template.py.
The difficulty folder is easy, medium, or hard.
"""

import shutil
from pathlib import Path

PROBLEMS_DIR = Path(__file__).resolve().parent.parent / "problems"
TEMPLATE = "_internal/practice_template.py"
PRACTICE = "practice.py"


def problem_dirs() -> list[Path]:
    """Return the problem folders of all difficulty folders, sorted by name."""
    return sorted(
        (p.parent.parent for p in PROBLEMS_DIR.glob(f"*/*/{TEMPLATE}")),
        key=lambda p: p.name,
    )


def ensure_practice_files() -> None:
    """Copy the template to practice.py in each problem that has no practice.py."""
    for problem in problem_dirs():
        if not (problem / PRACTICE).exists():
            shutil.copyfile(problem / TEMPLATE, problem / PRACTICE)


def reset(problem: Path) -> None:
    """Replace practice.py with a blank copy of the template."""
    shutil.copyfile(problem / TEMPLATE, problem / PRACTICE)
