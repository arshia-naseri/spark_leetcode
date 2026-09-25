# Spark LeetCode

Practice LeetCode DB problems w/ PySpark. Each problem: reference answer + blank practice templates. User writes `practice_dataframe.py` (`solve()`) + `practice_sql.py` (`solve_sql()`), git-ignored copies of templates. Two files independent: error in one no stop other. Tests check both, show results LeetCode format.

## Setup

- `uv` for all package mgmt + commands. No `pip`.
- Python 3.10+, PySpark 4.2, jedi (web UI completions), pytest 9 (dev group).
- PySpark 4 needs Java 17+. Machine has Java 21.

## Commands

```bash
uv run pytest                                   # practice code only (default)
uv run pytest --solution                        # the reference answers only
uv run pytest --all                             # all tests
uv run pytest p0175                             # one problem (name prefix or number: 175)
uv run pytest p0175 --solution                  # one problem, reference answers
uv run pytest -k "practice and case1"           # one case (-k turns off the default filter)
uv run python -m problems.easy.p0175_combine_two_tables._internal.main            # print practice output
uv run python -m problems.easy.p0175_combine_two_tables._internal.main solution   # print reference output
uv run python reset.py p0175                    # reset practice files to templates (--all for all)
uv run python -m webui                          # web UI at http://127.0.0.1:8000
```

Full list w/ explanations: `docs/commands.md`. Keep it in sync when commands change.

Always run `main.py` as module w/ `-m` from project root. Relative imports fail if file run direct.

## Layout

```
conftest.py        # `spark` fixture; problem prefix args; --solution/--all filter; "Output" section
common/spark.py    # get_spark(): shared SparkSession builder; DEFAULTS + spark_config.json overrides
common/leetcode.py # check(): compares answers and makes LeetCode-style reports
common/practice.py # makes/resets practice files from templates; load(): lazy import of one method's module
reset.py           # CLI: reset practice files
webui/             # local web UI (stdlib http.server): problem list, 3 panels, runs pytest
  server.py        # API: list/get problems, save code, run tests (pytest --leetcode-json), reset, jedi completions, Spark settings
                   # solved methods per problem in progress.json (project root, git-ignored)
  cases.py         # reads CASES tables w/ fake Spark (no JVM) for Testcase tab
  static/          # index.html, app.js, style.css. CodeMirror + marked from CDN
problems/__init__.py  # sets sys.dont_write_bytecode; makes missing practice files
problems/<difficulty>/  # easy, medium, hard. NO __init__.py (namespace package)
  pNNNN_<slug>/    # NO __init__.py here (namespace package)
    practice_dataframe.py # the user's solve(); git-ignored; auto-made from template_dataframe.py
    practice_sql.py  # the user's solve_sql(); git-ignored; auto-made from template_sql.py
    question.md      # LeetCode problem statement, tables, example, run commands
    _internal/
      __init__.py
      template_dataframe.py # committed blank stub: solve()
      template_sql.py  # committed blank stub: solve_sql()
      solution.py      # the reference answer
      data.py          # schemas (DDL strings) and CASES
      test_cases.py    # parametrized tests: cases x {practice, solution} x {dataframe, sql}
      main.py          # runs the LeetCode example and calls .show()
```

## Rules

- Problem folder location: `problems/<difficulty>/`, difficulty = LeetCode difficulty in lowercase (`easy`, `medium`, `hard`). Ex: `problems/easy/p0175_combine_two_tables`.
- Problem folder name: `p` + 4-digit LeetCode number + `_` + snake_case slug. Ex: `p0175_combine_two_tables`. Must be valid Python identifier.
- Problem folder top level: only `practice_dataframe.py`, `practice_sql.py`, `question.md`, `_internal/`. Rest in `_internal/`.
- Difficulty folder + problem folder no `__init__.py` (namespace pkg); `_internal/` has one. pytest config `pythonpath = ["."]` + `consider_namespace_packages = true` → each test module unique full name, same-named `_internal` modules no collide.
- `test_cases.py` + `main.py` import practice/solution code via `common.practice.load(__package__, module_name, method)`, lazy inside `run`. No top-level import of practice files: syntax error in one file must not break other method. Error shows as `Runtime Error`.
- Test file not `test_solution.py` — "solution" in name makes `-k solution` select all tests. Use `test_cases.py`.
- No answer in practice files or templates. No docstring/header comment in them. Template stubs `raise NotImplementedError`. Stub = skipped, not failed.
- Practice files in `.gitignore`. Never commit. Never edit template to hold user code.
- `problems/__init__.py` copies each template → practice file if missing, before any problem import.
- No show/change user code in practice files unless asked.
- `solution.py` has both funcs: `solve(<tables>)` DataFrame API, `solve_sql(spark, <tables>)` Spark SQL. Practice: `solve` only in `practice_dataframe.py`, `solve_sql` only in `practice_sql.py`. User do one or both.
- In `solve_sql`, register inputs as temp views w/ LeetCode table names (e.g. `Person`) before `raise NotImplementedError`.
- Always pass explicit DDL schema string to `createDataFrame`. Type inference fails on empty lists + all-`None` cols.
- Test cases in `data.py` as `CASES`: list of tuples (input rows..., expected rows). Case 1 = LeetCode example. Add edge cases: empty tables, no matches, nulls.
- Tests use `common.leetcode.check(request, inputs, run, expected)`. No plain `assert`.

## How `check()` works

- Ignores row + col order. Col names + values must match.
- Wrong answer → `pytest.fail(..., pytrace=False)` w/ Input, Output, Expected tables. No traceback.
- Col diff line (extra/missing, case-only hint). Red in Output = extra cols/rows; green in Expected = missing cols/rows. Rows matched on shared cols.
- Colors follow pytest setting (`--color`, `NO_COLOR`, `FORCE_COLOR`) via `pytest_sessionstart` + `set_color()`. No `isatty()`: pytest capture breaks it.
- Exception → `Runtime Error` w/ first line of error.
- `NotImplementedError` → skip.
- Correct → saves output table in `user_properties`. `conftest.py` prints in "Output" section.
- Every case also saves `leetcode_result` dict (status, inputs, output, expected, marks). `--leetcode-json PATH` writes them as JSON. Web UI reads this.

## Spark config

`common/spark.py` `DEFAULTS`: `spark.master=local[1]`, `spark.sql.shuffle.partitions=1`, UI off, session tz UTC. Log level ERROR (fixed). Driver mem default 1g. Most test time (~6 s) = JVM startup.

`spark_config.json` (project root, git-ignored) replaces `DEFAULTS` when it exists. Web UI gear button edits it (`GET`/`PUT /api/spark-config`). Save of `DEFAULTS` deletes file. Applies to next run + `uv run pytest` + `main.py`: each run = new JVM.

## Add a new problem

Use `/add-problem <leetcode-url>` skill (`.claude/skills/add-problem/`). It fetches problem, makes placeholders, fills files. Manual steps:

1. Make `problems/<difficulty>/pNNNN_<slug>/_internal/` w/ empty `_internal/__init__.py`. No `__init__.py` in problem folder.
2. Copy `data.py`, `test_cases.py`, `main.py` from `easy/p0175_combine_two_tables/_internal/`. Change schemas, `CASES`, table names.
3. Write `_internal/solution.py` w/ answer, `_internal/template_dataframe.py` + `_internal/template_sql.py` w/ stubs (copy p0175, no docstring).
4. Write `question.md` LeetCode format: title, difficulty + URL, tables, task, examples, run commands.
5. Run `uv run pytest pNNNN --all`. All `solution` tests pass, all `practice` tests skipped.

## Style

- Code comments, docstrings, docs in ASD-STE100 Simplified Technical English.