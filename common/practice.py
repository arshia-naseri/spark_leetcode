"""Make practice files from their templates, and import the code of one method.

Layout: each problem has two practice files, one for each method:
problems/<difficulty>/<problem>/practice_dataframe.py has solve() (DataFrame API).
problems/<difficulty>/<problem>/practice_sql.py has solve_sql() (Spark SQL).
The templates are problems/<difficulty>/<problem>/_internal/template_<method>.py.
The difficulty folder is easy, medium, or hard.
"""

import shutil
from importlib import import_module
from pathlib import Path
from types import ModuleType

PROBLEMS_DIR = Path(__file__).resolve().parent.parent / "problems"
METHODS = ("dataframe", "sql")
PRACTICE = {m: f"practice_{m}.py" for m in METHODS}
TEMPLATE = {m: f"_internal/template_{m}.py" for m in METHODS}


def problem_dirs() -> list[Path]:
    """Return the problem folders of all difficulty folders, sorted by name."""
    return sorted(
        (p.parent.parent for p in PROBLEMS_DIR.glob(f"*/*/{TEMPLATE['dataframe']}")),
        key=lambda p: p.name,
    )


def ensure_practice_files() -> None:
    """Copy each template to its practice file if the practice file does not exist."""
    for problem in problem_dirs():
        for method in METHODS:
            if not (problem / PRACTICE[method]).exists():
                shutil.copyfile(problem / TEMPLATE[method], problem / PRACTICE[method])


def reset(problem: Path, methods: tuple[str, ...] = METHODS) -> None:
    """Replace the practice files of the methods with blank copies of the templates."""
    for method in methods:
        shutil.copyfile(problem / TEMPLATE[method], problem / PRACTICE[method])


def load(package: str, module_name: str, method: str) -> ModuleType:
    """Import the module that has the code of one method.

    package is the _internal package of the problem. module_name is "practice" or
    "solution". method is "dataframe" or "sql". Tests import the module only when
    they run it. Thus an error in one practice file does not stop the other method.
    """
    if module_name == "solution":
        return import_module(".solution", package)
    return import_module(f"..{Path(PRACTICE[method]).stem}", package)
