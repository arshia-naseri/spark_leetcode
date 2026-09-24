# Spark LeetCode

Practice LeetCode DB problems w/ PySpark. Each problem: reference answer + blank practice template. User writes `practice.py`, git-ignored copy of template. Tests check both, show results LeetCode format.

## Setup

- `uv` for all package mgmt + commands. No `pip`.
- Python 3.10+, PySpark 4.2, pytest 9 (dev group).
- PySpark 4 needs Java 17+. Machine has Java 21.

## Commands

```bash
uv run pytest                                   # all tests
uv run pytest -k practice                       # the user's practice code only
uv run pytest -k solution                       # the reference answers only
uv run pytest problems/p0175_combine_two_tables # one problem
uv run pytest -k "practice and case1"           # one case
uv run python -m problems.p0175_combine_two_tables._internal.main            # print practice output
uv run python -m problems.p0175_combine_two_tables._internal.main solution   # print reference output
uv run python reset.py p0175                    # reset practice.py to template (--all for all)
```

Full list w/ explanations: `docs/commands.md`. Keep it in sync when commands change.

Always run `main.py` as module w/ `-m` from project root. Relative imports fail if file run direct.

## Layout

```
conftest.py        # session `spark` fixture; prints the "Output" section for passed tests
common/spark.py    # get_spark(): shared SparkSession builder
common/leetcode.py # check(): compares answers and makes LeetCode-style reports
common/practice.py # makes/resets practice.py from practice_template.py
reset.py           # CLI: reset practice.py files
problems/__init__.py  # sets sys.dont_write_bytecode; makes missing practice.py files
problems/pNNNN_<slug>/  # NO __init__.py here (namespace package)
  practice.py      # the user's code; git-ignored; auto-made from template
  question.md      # LeetCode problem statement, tables, example, run commands
  _internal/
    __init__.py
    practice_template.py # committed blank stubs: solve() and solve_sql()
    solution.py      # the reference answer
    data.py          # schemas (DDL strings) and CASES
    test_cases.py    # parametrized tests: cases x {practice, solution} x {dataframe, sql}
    main.py          # runs the LeetCode example and calls .show()
```

## Rules

- Problem folder name: `p` + 4-digit LeetCode number + `_` + snake_case slug. Ex: `p0175_combine_two_tables`. Must be valid Python identifier.
- Problem folder top level: only `practice.py`, `question.md`, `_internal/`. Rest in `_internal/`.
- Problem folder no `__init__.py` (namespace pkg); `_internal/` has one. pytest config `pythonpath = ["."]` + `consider_namespace_packages = true` → each test module unique full name, same-named `_internal` modules no collide.
- Relative imports in `_internal/`: `from .. import practice`, `from . import solution`.
- Test file not `test_solution.py` — "solution" in name makes `-k solution` select all tests. Use `test_cases.py`.
- No answer in `practice.py` or `practice_template.py`. Template stubs `raise NotImplementedError`. Stub = skipped, not failed.
- `practice.py` in `.gitignore`. Never commit. Never edit template to hold user code.
- `problems/__init__.py` copies template → `practice.py` if missing, before any problem import.
- No show/change user code in `practice.py` unless asked.
- Each module two funcs: `solve(<tables>)` DataFrame API, `solve_sql(spark, <tables>)` Spark SQL. User do one or both.
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

## Spark config

`common/spark.py` sets: `local[1]`, `spark.sql.shuffle.partitions=1`, UI off, session tz UTC, log level ERROR. Driver mem default 1g. Most test time (~6 s) = JVM startup.

## Add a new problem

Use `/add-problem <leetcode-url>` skill (`.claude/skills/add-problem/`). It fetches problem, makes placeholders, fills files. Manual steps:

1. Make `problems/pNNNN_<slug>/_internal/` w/ empty `_internal/__init__.py`. No `__init__.py` in problem folder.
2. Copy `data.py`, `test_cases.py`, `main.py` from `p0175_combine_two_tables/_internal/`. Change schemas, `CASES`, table names.
3. Write `_internal/solution.py` w/ answer, `_internal/practice_template.py` w/ stubs (docstring: title, "Read question.md", schemas).
4. Write `question.md` LeetCode format: title, difficulty + URL, tables, task, examples, run commands.
5. Run `uv run pytest problems/pNNNN_<slug>`. All `solution` tests pass, all `practice` tests skipped.

## Style

- Code comments, docstrings, docs in ASD-STE100 Simplified Technical English.