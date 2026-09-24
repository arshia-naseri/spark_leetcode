# 1527. Patients With a Condition

Difficulty: Easy · <https://leetcode.com/problems/patients-with-a-condition/>

## Tables

**Patients**

> | Column Name  | Type    |
> | ------------ | ------- |
> | patient_id   | int     |
> | patient_name | varchar |
> | conditions   | varchar |
>
> `patient_id` is the primary key (column with unique values) for this table. `conditions` contains 0 or more code separated by spaces. This table contains information of the patients in the hospital.

## Task

Write a solution to find the `patient_id`, `patient_name`, and `conditions` of the patients who have Type I Diabetes. Type I Diabetes always starts with `DIAB1` prefix.

Return the result table in **any order**.

## Example 1

> **Input:**
>
> Patients table:
>
> | patient_id | patient_name | conditions   |
> | ---------- | ------------ | ------------ |
> | 1          | Daniel       | YFEV COUGH   |
> | 2          | Alice        |              |
> | 3          | Bob          | DIAB100 MYOP |
> | 4          | George       | ACNE DIAB100 |
> | 5          | Alain        | DIAB201      |
>
> **Output:**
>
> | patient_id | patient_name | conditions   |
> | ---------- | ------------ | ------------ |
> | 3          | Bob          | DIAB100 MYOP |
> | 4          | George       | ACNE DIAB100 |
>
> **Explanation:**
>
> Bob and George both have a condition that starts with `DIAB1`.

## Run

```bash
uv run pytest p1527
uv run python -m problems.easy.p1527_patients_with_a_condition._internal.main
```
