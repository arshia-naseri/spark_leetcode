"""1873. Calculate Special Bonus.

https://leetcode.com/problems/calculate-special-bonus/

Calculate the bonus of each employee. The bonus is the full salary if the
employee_id is odd and the name does not start with 'M' or 'm'. Otherwise the
bonus is 0. Order the result by employee_id.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(employees: DataFrame) -> DataFrame:
    gets_bonus = (F.col("employee_id") % 2 == 1) & ~F.col("name").ilike("M%")
    return (
        employees
        .select(
            "employee_id",
            F.when(gets_bonus, F.col("salary")).otherwise(F.lit(0)).alias("bonus"),
        )
        .orderBy("employee_id")
    )


def solve_sql(spark: SparkSession, employees: DataFrame) -> DataFrame:
    employees.createOrReplaceTempView("Employees")
    return spark.sql(
        """
        SELECT
            employee_id,
            CASE
                WHEN employee_id % 2 = 1 AND name NOT ILIKE 'M%' THEN salary
                ELSE 0
            END AS bonus
        FROM Employees
        ORDER BY employee_id
        """
    )
