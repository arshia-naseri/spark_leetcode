# 182. Duplicate Emails

Difficulty: Easy · <https://leetcode.com/problems/duplicate-emails/>

## Tables

**Person**

| Column Name | Type    |
| ----------- | ------- |
| id          | int     |
| email       | varchar |

`id` is the primary key (column with unique values) for this table. Each row of this table contains an email. The emails will not contain uppercase letters.

## Task

Write a solution to report all the duplicate emails. Note that it's guaranteed that the `email` field is not `NULL`.

Return the result table in **any order**.

## Example 1

**Input:**

Person table:

| id | email   |
| -- | ------- |
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |

**Output:**

| Email   |
| ------- |
| a@b.com |

**Explanation:**

`a@b.com` is repeated two times.

## Run

```bash
uv run pytest p0182
uv run python -m problems.easy.p0182_duplicate_emails._internal.main
```
