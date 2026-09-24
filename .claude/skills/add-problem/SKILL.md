---
name: add-problem
description: Add a LeetCode database problem to this repo from a LeetCode URL or slug. Gets the problem statement and example data, makes a placeholder problem folder, then fills question.md, data.py (with edge cases), solution.py, practice_template.py, test_cases.py and main.py like problems/p0175_combine_two_tables. Use when the user gives a leetcode.com/problems/... URL or asks to add a new problem.
argument-hint: <leetcode-url-or-slug>
allowed-tools: Bash(uv run python .claude/skills/add-problem/scripts/*) Bash(uv run pytest *)
---

# Add a LeetCode problem

Input: `$ARGUMENTS` (a LeetCode URL, for example `https://leetcode.com/problems/second-highest-salary/`, or a slug).

The reference problem is `problems/p0175_combine_two_tables/`. Read all of its files before you write the new files. Follow the rules in `CLAUDE.md`.

## Step 1: Get the problem

```bash
uv run python .claude/skills/add-problem/scripts/fetch.py "$ARGUMENTS"
```

The script prints JSON: `id`, `title`, `slug`, `difficulty`, `category`, `paid`, `url`, `folder`, `schema`, `examples`, `content`.

Stop and tell the user when:

- `category` is not `Database`. This repo only has SQL / DataFrame problems.
- `paid` is `true` and `content` is `null`. The API does not give premium content. Ask the user to paste the problem statement.
- the script fails (network error, no problem found). Show the error.

## Step 2: Make placeholders

```bash
uv run python .claude/skills/add-problem/scripts/scaffold.py <folder>
```

Use `folder` from the JSON. The script makes the folder with one placeholder file for each required file. If the folder exists, the script stops. Then ask the user before you change the existing folder.

## Step 3: Fill the files

Replace each placeholder. Keep the structure and style of the p0175 files. Write comments and docstrings in ASD-STE100 Simplified Technical English.

### Types

Use `schema` from the JSON for column names and types. Map SQL types to Spark DDL types:

| SQL type                  | Spark DDL      | Python value in data.py            |
| ------------------------- | -------------- | ---------------------------------- |
| `INT`, `INTEGER`          | `INT`          | `int`                              |
| `BIGINT`                  | `BIGINT`       | `int`                              |
| `VARCHAR(n)`, `CHAR`, `TEXT`, `ENUM(...)` | `STRING` | `str`                   |
| `DECIMAL(p,s)`            | `DECIMAL(p,s)` | `decimal.Decimal("1.50")`          |
| `FLOAT`, `DOUBLE`         | `DOUBLE`       | `float`                            |
| `DATE`                    | `DATE`         | `datetime.date(2020, 1, 1)`        |
| `DATETIME`, `TIMESTAMP`   | `TIMESTAMP`    | `datetime.datetime(2020, 1, 1, 9, 0)` |
| `BOOL`, `TINYINT(1)`      | `BOOLEAN`      | `bool`                             |

LeetCode shows `null` or `Null` in example tables. Use `None`.

The output schema is not in the JSON. Get the output column names from the example output in `content`. Select the output types from the task and the input types (for example `COUNT` gives `BIGINT`, `AVG` / `ROUND` gives `DOUBLE`). `check()` compares values, so the solution types must give equal values.

### Files

1. `question.md`: same sections as p0175. Title `# <id>. <title>`, `Difficulty: <difficulty> · <<url>>`, `## Tables` (one markdown table for each input table and the description text), `## Task`, `## Example N` for each example (Input tables, Output table, Explanation if present), `## Run` with the two commands for this folder (`uv run pytest pNNNN` and the `main` module command). Convert the ASCII `+---+` tables in `content` to markdown tables. Put column and table names in backticks. Remove HTML tags. Do not include the "result format is in the following example" line.
2. `_internal/data.py`: `<TABLE>_SCHEMA` for each input table, `OUTPUT_SCHEMA`, `EXAMPLE_<TABLE>` and `EXAMPLE_OUTPUT` from example 1, and `CASES`. Put a comment above `CASES` that tells the tuple order. Case 1 is the LeetCode example. Add the other LeetCode examples as next cases (input rows from `examples`, output from `content`). Then add edge cases: empty tables, no matches, nulls, duplicates, ties. Add only edge cases that apply to this problem. Calculate each expected output by hand from the task text. Do not calculate it with the solution.
3. `_internal/solution.py`: docstring (title, URL, short task text). `solve(<tables>)` with the DataFrame API and `solve_sql(spark, <tables>)` with Spark SQL. In `solve_sql`, register each input as a temp view with its LeetCode table name.
4. `_internal/practice_template.py`: docstring with title, "Read question.md for the problem statement.", input schemas, output columns and order rule. Stubs `raise NotImplementedError`. `solve_sql` registers the temp views before `raise`. No answer in this file.
5. `_internal/test_cases.py`: copy p0175. Change the parameter names, schemas and the `inputs` dict for `check()` (LeetCode table name to DataFrame). One parameter for each input table plus `expected_rows`.
6. `_internal/main.py`: copy p0175. Change the imports and tables to use the `EXAMPLE_*` data.

Argument names: snake_case of the table name (`Person` gives `person`, `MyNumbers` gives `my_numbers`). Use the same argument order as the tables in the problem.

## Step 4: Verify

```bash
uv run pytest problems/<folder> --all
```

All `solution` tests must pass. All `practice` tests must skip. If a solution test fails, look at the report. Find if the solution or the expected rows are wrong. Fix the incorrect one. Do not change the expected rows only to make the test pass.

Then run the example:

```bash
uv run python -m problems.<folder>._internal.main solution
```

## Step 5: Report

Tell the user the folder name, the number of cases, and the edge cases that you added. Do not commit.
