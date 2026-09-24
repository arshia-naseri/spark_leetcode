"""Make an empty problem folder with placeholder files.

Usage: uv run python .claude/skills/add-problem/scripts/scaffold.py <difficulty> <folder>

Example: scaffold.py Medium p0176_second_highest_salary

<difficulty> is easy, medium, or hard (any case).
The script does not change a folder that exists. It stops if the problem
exists in a different difficulty folder. It makes:
  problems/<difficulty>/<folder>/question.md
  problems/<difficulty>/<folder>/_internal/__init__.py            (empty)
  problems/<difficulty>/<folder>/_internal/solution.py
  problems/<difficulty>/<folder>/_internal/data.py
  problems/<difficulty>/<folder>/_internal/test_cases.py
  problems/<difficulty>/<folder>/_internal/main.py
Each placeholder has a TODO line. Replace all TODO lines with the problem data.
It does not make practice_template.py or practice.py. Write
_internal/practice_template.py when the stubs are complete.
problems/__init__.py copies each template to a missing practice.py when a
test run starts. A placeholder template would give a practice.py without
stubs, and the practice tests would fail.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PROBLEMS = ROOT / "problems"
DIFFICULTIES = ("easy", "medium", "hard")

PLACEHOLDERS = {
    "question.md": "# TODO: question title\n",
    "_internal/__init__.py": "",
    "_internal/solution.py": '"""TODO: reference solution."""\n',
    "_internal/data.py": "# TODO: schemas and CASES.\n",
    "_internal/test_cases.py": "# TODO: parametrized tests.\n",
    "_internal/main.py": "# TODO: run the LeetCode example.\n",
}


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    difficulty, name = sys.argv[1].lower(), sys.argv[2]
    if difficulty not in DIFFICULTIES:
        sys.exit(f"Bad difficulty {sys.argv[1]!r}. Use one of: {', '.join(DIFFICULTIES)}.")
    if not re.fullmatch(r"p\d{4}_[a-z0-9_]+", name) or not name.isidentifier():
        sys.exit(f"Bad folder name {name!r}. Use p + 4 digits + _ + snake_case slug.")
    existing = [PROBLEMS / d / name for d in DIFFICULTIES if (PROBLEMS / d / name).exists()]
    if existing:
        sys.exit(f"{existing[0].relative_to(ROOT)} exists. Nothing changed.")
    folder = PROBLEMS / difficulty / name
    for rel, text in PLACEHOLDERS.items():
        path = folder / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
