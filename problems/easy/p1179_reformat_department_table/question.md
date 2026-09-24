# 1179. Reformat Department Table

Difficulty: Easy · <https://leetcode.com/problems/reformat-department-table/>

## Tables

**Department**

| Column Name | Type    |
| ----------- | ------- |
| id          | int     |
| revenue     | int     |
| month       | varchar |

In SQL, (`id`, `month`) is the primary key of this table. The table has information about the revenue of each department per month. The `month` has values in `["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]`.

## Task

Reformat the table such that there is a department `id` column and a revenue column **for each month**.

Return the result table in **any order**.

## Example 1

**Input:**

Department table:

| id  | revenue | month |
| --- | ------- | ----- |
| 1   | 8000    | Jan   |
| 2   | 9000    | Jan   |
| 3   | 10000   | Feb   |
| 1   | 7000    | Feb   |
| 1   | 6000    | Mar   |

**Output:**

| id  | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
| --- | ----------- | ----------- | ----------- | --- | ----------- |
| 1   | 8000        | 7000        | 6000        | ... | null        |
| 2   | 9000        | null        | null        | ... | null        |
| 3   | null        | 10000       | null        | ... | null        |

**Explanation:**

The revenue from Apr to Dec is null.

Note that the result table has 13 columns (1 for the department `id` + 12 for the months).

## Run

```bash
uv run pytest p1179
uv run python -m problems.easy.p1179_reformat_department_table._internal.main
```
