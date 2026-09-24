"""181. Employees Earning More Than Their Managers.

https://leetcode.com/problems/employees-earning-more-than-their-managers/

Find the employees who earn more than their managers.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(employee: DataFrame) -> DataFrame:
    e = employee.alias("e")
    m = employee.alias("m")
    return (
        e
        .join(m, F.col("e.managerId") == F.col("m.id"), how="inner")
        .where(F.col("e.salary") > F.col("m.salary"))
        .select(F.col("e.name").alias("Employee"))
    )


def solve_sql(spark: SparkSession, employee: DataFrame) -> DataFrame:
    employee.createOrReplaceTempView("Employee")
    return spark.sql(
        """
        SELECT e.name AS Employee
        FROM Employee e
        JOIN Employee m ON e.managerId = m.id
        WHERE e.salary > m.salary
        """
    )
