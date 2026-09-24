"""1741. Find Total Time Spent by Each Employee.

https://leetcode.com/problems/find-total-time-spent-by-each-employee/

Calculate the total time in minutes that each employee spends in the office
on each day. The time for one entry is out_time - in_time.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(employees: DataFrame) -> DataFrame:
    return (
        employees
        .groupBy(F.col("event_day").alias("day"), "emp_id")
        .agg(F.sum(F.col("out_time") - F.col("in_time")).alias("total_time"))
    )


def solve_sql(spark: SparkSession, employees: DataFrame) -> DataFrame:
    employees.createOrReplaceTempView("Employees")
    return spark.sql(
        """
        SELECT event_day AS day, emp_id, SUM(out_time - in_time) AS total_time
        FROM Employees
        GROUP BY event_day, emp_id
        """
    )
