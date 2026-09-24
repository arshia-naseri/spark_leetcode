# 1378. Replace Employee ID With The Unique Identifier

Difficulty: Easy · <https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/>

## Tables

**Employees**

> | Column Name | Type    |
> | ----------- | ------- |
> | id          | int     |
> | name        | varchar |
>
> `id` is the primary key (column with unique values) for this table. Each row of this table contains the id and the name of an employee in a company.

**EmployeeUNI**

> | Column Name | Type |
> | ----------- | ---- |
> | id          | int  |
> | unique_id   | int  |
>
> (`id`, `unique_id`) is the primary key (combination of columns with unique values) for this table. Each row of this table contains the id and the corresponding unique id of an employee in the company.

## Task

Write a solution to show the **unique ID** of each user. If a user does not have a unique ID, show `null`.

Return the result table in **any** order.

## Example 1

> **Input:**
>
> Employees table:
>
> | id | name     |
> | -- | -------- |
> | 1  | Alice    |
> | 7  | Bob      |
> | 11 | Meir     |
> | 90 | Winston  |
> | 3  | Jonathan |
>
> EmployeeUNI table:
>
> | id | unique_id |
> | -- | --------- |
> | 3  | 1         |
> | 11 | 2         |
> | 90 | 3         |
>
> **Output:**
>
> | unique_id | name     |
> | --------- | -------- |
> | null      | Alice    |
> | null      | Bob      |
> | 2         | Meir     |
> | 3         | Winston  |
> | 1         | Jonathan |
>
> **Explanation:**
>
> Alice and Bob do not have a unique ID. We show `null` instead.
>
> The unique ID of Meir is 2.
>
> The unique ID of Winston is 3.
>
> The unique ID of Jonathan is 1.

## Run

```bash
uv run pytest p1378
uv run python -m problems.easy.p1378_replace_employee_id_with_the_unique_identifier._internal.main
```
