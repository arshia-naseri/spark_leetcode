"""Make an empty problem folder with placeholder files.

Usage: uv run python .claude/skills/add-problem/scripts/scaffold.py <folder>

Example: scaffold.py p0176_second_highest_salary

The script does not change a folder that exists. It makes:
  problems/<folder>/question.md
  problems/<folder>/_internal/__init__.py            (empty)
  problems/<folder>/_internal/practice_template.py
  problems/<folder>/_internal/solution.py
  problems/<folder>/_internal/data.py
  problems/<folder>/_internal/test_cases.py
  problems/<folder>/_internal/main.py
Each placeholder has a TODO line. Replace all TODO lines with the problem data.
It does not make practice.py. problems/__init__.py makes it from the template.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PROBLEMS = ROOT / "problems"

PLACEHOLDERS = {
    "question.md": "# TODO: question title\n",
    "_internal/__init__.py": "",
    "_internal/practice_template.py": '"""TODO: practice stubs."""\n',
    "_internal/solution.py": '"""TODO: reference solution."""\n',
    "_internal/data.py": "# TODO: schemas and CASES.\n",
    "_internal/test_cases.py": "# TODO: parametrized tests.\n",
    "_internal/main.py": "# TODO: run the LeetCode example.\n",
}


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    name = sys.argv[1]
    if not re.fullmatch(r"p\d{4}_[a-z0-9_]+", name) or not name.isidentifier():
        sys.exit(f"Bad folder name {name!r}. Use p + 4 digits + _ + snake_case slug.")
    folder = PROBLEMS / name
    if folder.exists():
        sys.exit(f"{folder.relative_to(ROOT)} exists. Nothing changed.")
    for rel, text in PLACEHOLDERS.items():
        path = folder / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
