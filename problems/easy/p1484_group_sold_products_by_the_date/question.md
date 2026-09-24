# 1484. Group Sold Products By The Date

Difficulty: Easy · <https://leetcode.com/problems/group-sold-products-by-the-date/>

## Tables

**Activities**

> | Column Name | Type    |
> | ----------- | ------- |
> | sell_date   | date    |
> | product     | varchar |
>
> There is no primary key (column with unique values) for this table. It may contain duplicates.
>
> Each row of this table contains the product name and the date it was sold in a market.

## Task

Write a solution to find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by `sell_date`.

## Example 1

> **Input:**
>
> Activities table:
>
> | sell_date  | product    |
> | ---------- | ---------- |
> | 2020-05-30 | Headphone  |
> | 2020-06-01 | Pencil     |
> | 2020-06-02 | Mask       |
> | 2020-05-30 | Basketball |
> | 2020-06-01 | Bible      |
> | 2020-06-02 | Mask       |
> | 2020-05-30 | T-Shirt    |
>
> **Output:**
>
> | sell_date  | num_sold | products                     |
> | ---------- | -------- | ---------------------------- |
> | 2020-05-30 | 3        | Basketball,Headphone,T-Shirt |
> | 2020-06-01 | 2        | Bible,Pencil                 |
> | 2020-06-02 | 1        | Mask                         |
>
> **Explanation:**
>
> For 2020-05-30, Sold items were (Headphone, Basketball, T-Shirt), we sort them lexicographically and separate them by a comma.
>
> For 2020-06-01, Sold items were (Pencil, Bible), we sort them lexicographically and separate them by a comma.
>
> For 2020-06-02, the Sold item is (Mask), we just return it.
>
> Note: the LeetCode page shows `T-shirt` in the output, but the input has `T-Shirt`. The tests use `T-Shirt`.

## Run

```bash
uv run pytest p1484
uv run python -m problems.easy.p1484_group_sold_products_by_the_date._internal.main
```
