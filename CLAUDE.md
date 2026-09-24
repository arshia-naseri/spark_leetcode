# Spark LeetCode

Practice LeetCode database problems with PySpark. Each problem: reference answer + empty practice file. User writes practice file. Tests check both, show results in LeetCode format.

## Setup

- Use `uv` for all package mgmt + commands. No `pip`.
- Python 3.10+, PySpark 4.2, pytest 9 (dev group).
- PySpark 4 needs Java 17+. Machine has Java 21.

## Commands

```bash
uv run pytest                                   # all tests
uv run pytest -k practice                       # the user's practice code only
uv run pytest -k solution                       # the reference answers only
uv run pytest problems/p0175_combine_two_tables # one problem
uv run pytest -k "practice and case1"           # one case
uv run python -m problems.p0175_combine_two_tables.main            # print practice output
uv run python -m problems.p0175_combine_two_tables.main solution   # print reference output
```

Always run `main.py` as module with `-m` from project root. Relative imports fail if file run directly.

## Layout

```
conftest.py        # session `spark` fixture; prints the "Output" section for passed tests
common/spark.py    # get_spark(): shared SparkSession builder
common/leetcode.py # check(): compares answers and makes LeetCode-style reports
problems/pNNNN_<slug>/
  __init__.py      # makes the folder a package (necessary, see below)
  practice.py      # the user's code: solve() and solve_sql() stubs
  solution.py      # the reference answer
  data.py          # schemas (DDL strings) and CASES
  test_cases.py    # parametrized tests: cases x {practice, solution} x {dataframe, sql}
  main.py          # runs the LeetCode example and calls .show()
```

## Rules

- Problem folder name: `p` + 4-digit LeetCode number + `_` + snake_case slug. Example: `p0175_combine_two_tables`. Must be valid Python identifier.
- Every problem folder needs `__init__.py`. Without it, all `solution` modules share name → pytest imports wrong one.
- Relative imports in problem folder, e.g. `from .solution import solve`.
- Test file not `test_solution.py` — "solution" in name makes `-k solution` select all tests. Use `test_cases.py`.
- No answer in `practice.py`. File is for user. New problem gets stubs that `raise NotImplementedError`. Stub shows skipped, not failed.
- No show/change user code in `practice.py` unless user asks.
- Each module has two functions: `solve(<tables>)` for DataFrame API, `solve_sql(spark, <tables>)` for Spark SQL. User can do one or both.
- In `solve_sql`, register inputs as temp views with LeetCode table names (e.g. `Person`) before `raise NotImplementedError`.
- Always pass explicit DDL schema string to `createDataFrame`. Type inference fails on empty lists + all-`None` columns.
- Test cases in `data.py` as `CASES`: list of tuples (input rows..., expected rows). Case 1 = LeetCode example. Add edge cases: empty tables, no matches, nulls.
- Tests use `common.leetcode.check(request, inputs, run, expected)`. No plain `assert`.

## How `check()` works

- Ignores row order + column order. Column names + values must match.
- Wrong answer → `pytest.fail(..., pytrace=False)` with Input, Output, Expected tables. No traceback.
- Exception → `Runtime Error` with first line of error.
- `NotImplementedError` → skip test.
- Correct answer → saves output table in `user_properties`. `conftest.py` prints these in "Output" section.

## Spark config

`common/spark.py` sets: `local[1]`, `spark.sql.shuffle.partitions=1`, UI off, session timezone UTC, log level ERROR. Driver memory default 1g. Most test time (~6 s) = JVM startup.

## Add a new problem

1. Make `problems/pNNNN_<slug>/` with empty `__init__.py`.
2. Copy `data.py`, `test_cases.py`, `main.py` from `p0175_combine_two_tables`. Change schemas, `CASES`, table names.
3. Write `solution.py` with answer, `practice.py` with stubs. Problem statement + schemas in docstring of both.
4. Run `uv run pytest problems/pNNNN_<slug>`. All `solution` tests pass, all `practice` tests skipped.

## Style

- Code comments, docstrings, docs in ASD-STE100 Simplified Technical English.