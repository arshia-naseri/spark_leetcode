"""577. Employee Bonus.

https://leetcode.com/problems/employee-bonus/

Report the name and bonus of each employee who has a bonus less than 1000
or who has no bonus.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(employee: DataFrame, bonus: DataFrame) -> DataFrame:
    return (
        employee
        .join(bonus, on="empId", how="left")
        .where(F.col("bonus").isNull() | (F.col("bonus") < 1000))
        .select("name", "bonus")
    )


def solve_sql(spark: SparkSession, employee: DataFrame, bonus: DataFrame) -> DataFrame:
    employee.createOrReplaceTempView("Employee")
    bonus.createOrReplaceTempView("Bonus")
    return spark.sql(
        """
        SELECT e.name, b.bonus
        FROM Employee e
        LEFT JOIN Bonus b ON e.empId = b.empId
        WHERE b.bonus IS NULL OR b.bonus < 1000
        """
    )
