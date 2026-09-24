"""1731. The Number of Employees Which Report to Each Employee.

https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/

A manager is an employee with at least 1 direct report. Report the id and the
name of each manager, the number of direct reports, and the average age of
the reports rounded to the nearest integer. Order by employee_id.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(employees: DataFrame) -> DataFrame:
    reports = employees.alias("e")
    managers = employees.alias("m")
    return (
        managers
        .join(reports, F.col("e.reports_to") == F.col("m.employee_id"), "inner")
        .groupBy(F.col("m.employee_id"), F.col("m.name"))
        .agg(
            F.count("e.employee_id").alias("reports_count"),
            F.round(F.avg("e.age")).cast("int").alias("average_age"),
        )
        .orderBy("employee_id")
    )


def solve_sql(spark: SparkSession, employees: DataFrame) -> DataFrame:
    employees.createOrReplaceTempView("Employees")
    return spark.sql(
        """
        SELECT m.employee_id,
               m.name,
               COUNT(e.employee_id) AS reports_count,
               CAST(ROUND(AVG(e.age)) AS INT) AS average_age
        FROM Employees m
        JOIN Employees e ON e.reports_to = m.employee_id
        GROUP BY m.employee_id, m.name
        ORDER BY m.employee_id
        """
    )
