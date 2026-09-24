# Commands

Run all commands from project root.

## Tests

Test only your code (default):

```bash
uv run pytest
```

Test only reference answers:

```bash
uv run pytest --solution
```

Run all tests (your code and reference answers):

```bash
uv run pytest --all
```

Run tests for one problem. Give the folder name, a prefix of it, or the problem number:

```bash
uv run pytest p0175
uv run pytest 175
uv run pytest p0175 --solution
```

Run one case. When you give `-k`, the default practice filter is off:

```bash
uv run pytest -k "practice and case1"
```

New problem: run its tests. All `solution` tests must pass, all `practice` tests must skip:

```bash
uv run pytest pNNNN --all
```

## Add a problem

In Claude Code, add a problem from a LeetCode URL:

```text
/add-problem https://leetcode.com/problems/second-highest-salary/
```

The skill uses these scripts. You can also run them yourself:

```bash
uv run python .claude/skills/add-problem/scripts/fetch.py <url-or-slug>  # print the problem as JSON
uv run python .claude/skills/add-problem/scripts/scaffold.py pNNNN_<slug> # make placeholder files
```

## Colors

Reports use same color setting as pytest.

```bash
uv run pytest --color=yes   # always show colors
uv run pytest --color=no    # never show colors
NO_COLOR=1 uv run pytest    # never show colors
FORCE_COLOR=1 uv run pytest # always show colors
```

## Show the output of the example

Show your code output for LeetCode example:

```bash
uv run python -m problems.p0175_combine_two_tables._internal.main
```

Show reference answer output:

```bash
uv run python -m problems.p0175_combine_two_tables._internal.main solution
```

Always use `-m`, run from project root. Run `main.py` directly → relative imports fail.

## Reset your practice file

Replace `practice.py` with blank template copy. Deletes your code in that file.

```bash
uv run python reset.py p0175          # one problem (a name prefix is sufficient)
uv run python reset.py p0175 p0181    # more than one problem
uv run python reset.py --all          # all problems
```
