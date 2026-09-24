# 584. Find Customer Referee

Difficulty: Easy · <https://leetcode.com/problems/find-customer-referee/>

## Tables

**Customer**

| Column Name | Type    |
| ----------- | ------- |
| id          | int     |
| name        | varchar |
| referee_id  | int     |

In SQL, `id` is the primary key column for this table. Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

## Task

Find the names of the customer that are either:

1. **referred by** any customer with `id != 2`.
2. **not referred by** any customer.

Return the result table in **any order**.

## Example 1

**Input:**

Customer table:

| id | name | referee_id |
| -- | ---- | ---------- |
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |

**Output:**

| name |
| ---- |
| Will |
| Jane |
| Bill |
| Zack |

## Run

```bash
uv run pytest p0584
uv run python -m problems.easy.p0584_find_customer_referee._internal.main
```
