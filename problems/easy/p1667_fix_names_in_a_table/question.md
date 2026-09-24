# 1667. Fix Names in a Table

Difficulty: Easy · <https://leetcode.com/problems/fix-names-in-a-table/>

## Tables

**Users**

| Column Name | Type    |
| ----------- | ------- |
| user_id     | int     |
| name        | varchar |

`user_id` is the primary key (column with unique values) for this table. This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.

## Task

Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by `user_id`.

## Example 1

**Input:**

Users table:

| user_id | name  |
| ------- | ----- |
| 1       | aLice |
| 2       | bOB   |

**Output:**

| user_id | name  |
| ------- | ----- |
| 1       | Alice |
| 2       | Bob   |

## Run

```bash
uv run pytest p1667
uv run python -m problems.easy.p1667_fix_names_in_a_table._internal.main
```
