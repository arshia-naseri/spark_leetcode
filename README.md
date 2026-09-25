# Spark LeetCode

Practice LeetCode database problems with PySpark.

Each problem has a reference answer and two blank practice files:

- `practice_dataframe.py`: write `solve()` with the DataFrame API.
- `practice_sql.py`: write `solve_sql()` with Spark SQL.

You can do one method or both. The two files are independent. An error in one file does not stop the tests of the other file.
The tests compare your output with the expected output and show the result in LeetCode format.

## Requirements

- Python 3.10 or later
- Java 17 or later (PySpark 4 needs it)
- [uv](https://docs.astral.sh/uv/)

## Install

```bash
git clone https://github.com/arshia-naseri/spark_leetcode.git
cd spark_leetcode
uv sync
```

Use `uv` for all packages and commands. Do not use `pip`.

## Web UI

The web UI is the main way to practice. Start it:

```bash
uv run python -m webui
```

The web UI opens at <http://127.0.0.1:8000>. It shows the list of problems and marks the solved methods.
Each problem opens in three panels: the question, a code editor with PySpark completions, and the test results.
Select `solve()` (DataFrame API) or `solve_sql()` (Spark SQL), write your code, and click **Run** (Ctrl/⌘ + Enter).
The editor saves your code automatically. A run takes approximately 6 seconds, because each run starts a new JVM.

## Quick start without the web UI

To write code in your own editor and run the tests from the terminal:

1. Open a problem folder, for example `problems/easy/p0175_combine_two_tables/`.
2. Read `question.md`.
3. Write your answer in `practice_dataframe.py`, `practice_sql.py`, or both.
4. Run the tests:

   ```bash
   uv run pytest p0175
   ```

The first run makes the practice files from the templates. Git ignores the practice files.
A method that still raises `NotImplementedError` is skipped, not failed.

## Common commands

```bash
uv run pytest                   # test your practice code (default)
uv run pytest --solution        # test the reference answers
uv run pytest --all             # run all tests
uv run pytest 175               # test one problem (number or folder name prefix)
uv run python reset.py p0175    # reset the practice files of one problem to the templates
```

Show the output of the LeetCode example:

```bash
uv run python -m problems.easy.p0175_combine_two_tables._internal.main            # your code
uv run python -m problems.easy.p0175_combine_two_tables._internal.main solution   # reference answer
```

Always run `main.py` as a module (`-m`) from the project root.

For the full list of commands, see [docs/commands.md](docs/commands.md).

## Test reports

The tests ignore the order of rows and columns. The column names and the values must be the same.

- **Wrong Answer**: the report shows the Input, Output and Expected tables. Red shows extra columns or rows. Green shows missing columns or rows.
- **Runtime Error**: the report shows the first line of the error.
- **Correct**: pytest shows your output table in the "Output" section.

## Spark settings

The default settings are in `common/spark.py` (`local[1]`, 1 shuffle partition, UI off, time zone UTC, 1g driver memory).
To change them, click the gear button in the web UI. The web UI writes `spark_config.json` in the project root.
The new settings apply to the next run.

## Project layout

```
common/          # shared code: Spark session, answer check, practice file helpers
problems/
  easy/ medium/ hard/
    pNNNN_<slug>/
      question.md            # problem statement
      practice_dataframe.py  # your solve() (git-ignored)
      practice_sql.py        # your solve_sql() (git-ignored)
      _internal/             # templates, reference answer, data, tests
webui/           # local web UI
reset.py         # resets practice files
docs/            # documentation
```

## Add a problem

In [Claude Code](https://claude.com/claude-code), run:

```text
/add-problem https://leetcode.com/problems/<slug>/
```

For the manual steps, see `CLAUDE.md`.
