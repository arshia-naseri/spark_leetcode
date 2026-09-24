# 610. Triangle Judgement

Difficulty: Easy · <https://leetcode.com/problems/triangle-judgement/>

## Tables

**Triangle**

| Column Name | Type |
| ----------- | ---- |
| x           | int  |
| y           | int  |
| z           | int  |

In SQL, (`x`, `y`, `z`) is the primary key column for this table. Each row of this table contains the lengths of three line segments.

## Task

Report for every three line segments whether they can form a triangle.

Return the result table in **any order**.

## Example 1

**Input:**

Triangle table:

| x  | y  | z  |
| -- | -- | -- |
| 13 | 15 | 30 |
| 10 | 20 | 15 |

**Output:**

| x  | y  | z  | triangle |
| -- | -- | -- | -------- |
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |

## Run

```bash
uv run pytest p0610
uv run python -m problems.easy.p0610_triangle_judgement._internal.main
```
