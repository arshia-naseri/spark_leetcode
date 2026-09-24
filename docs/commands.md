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

## Web UI

Start the local web UI. It opens <http://127.0.0.1:8000> in the browser:

```bash
uv run python -m webui
uv run python -m webui --port 8080   # use a different port
uv run python -m webui --no-browser  # do not open the browser
```

The home page shows all problems. Click a problem to open it in three panels:

- Left: the question (`question.md`). The Solution tab shows the reference answer.
- Top right: the editor for the practice file of the selected method. The UI saves your code automatically.
  The editor shows completions for Python and PySpark (from `jedi`) when you type a name or `.`.
  Press Ctrl + Space to show them manually. The panel next to the list shows the signature and the docstring.
- Bottom right: the test cases and the test results.

Select `solve()` (DataFrame API, `practice_dataframe.py`) or `solve_sql()` (Spark SQL, `practice_sql.py`).
The editor shows the file of the selected method. Then click **Run** (Ctrl/⌘ + Enter).
Each run starts pytest, so a run takes approximately 6 s.
The ↺ button resets the practice file of the selected method to its template. This deletes your code in that file.

The UI runs pytest with `--leetcode-json PATH`. This option writes the result of each case as JSON:

```bash
uv run pytest p0175 --leetcode-json results.json
```

## Add a problem

In Claude Code, add a problem from a LeetCode URL:

```text
/add-problem https://leetcode.com/problems/second-highest-salary/
```

The skill uses these scripts. You can also run them yourself:

```bash
uv run python .claude/skills/add-problem/scripts/fetch.py <url-or-slug>  # print the problem as JSON
uv run python .claude/skills/add-problem/scripts/scaffold.py <difficulty> pNNNN_<slug> # make placeholder files
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
uv run python -m problems.easy.p0175_combine_two_tables._internal.main
```

Show reference answer output:

```bash
uv run python -m problems.easy.p0175_combine_two_tables._internal.main solution
```

Always use `-m`, run from project root. Run `main.py` directly → relative imports fail.

## Reset your practice files

Replace `practice_dataframe.py` and `practice_sql.py` with blank template copies. Deletes your code in these files.

```bash
uv run python reset.py p0175          # one problem (a name prefix is sufficient)
uv run python reset.py p0175 p0181    # more than one problem
uv run python reset.py --all          # all problems
```
