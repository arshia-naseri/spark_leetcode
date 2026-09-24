"""Reset practice.py to the blank template.

Usage:
    uv run python reset.py p0175          # one problem (name or prefix)
    uv run python reset.py p0175 p0181    # more than one problem
    uv run python reset.py --all          # all problems
"""

import sys

from common.practice import problem_dirs, reset


def main(args: list[str]) -> int:
    if not args:
        print(__doc__)
        return 1

    problems = problem_dirs()
    if args != ["--all"]:
        selected = [p for p in problems if any(p.name.startswith(a) for a in args)]
        unknown = [a for a in args if not any(p.name.startswith(a) for p in problems)]
        if unknown:
            print(f"No problem found for: {', '.join(unknown)}")
            return 1
        problems = selected

    for problem in problems:
        reset(problem)
        print(f"Reset {problem.name}/practice.py")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
