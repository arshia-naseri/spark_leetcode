"""1075. Project Employees I.

https://leetcode.com/problems/project-employees-i/

Report the average experience years of all the employees for each project,
rounded to 2 digits.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(project: DataFrame, employee: DataFrame) -> DataFrame:
    return (
        project
        .join(employee, on="employee_id", how="inner")
        .groupBy("project_id")
        .agg(F.round(F.avg("experience_years"), 2).alias("average_years"))
    )


def solve_sql(spark: SparkSession, project: DataFrame, employee: DataFrame) -> DataFrame:
    project.createOrReplaceTempView("Project")
    employee.createOrReplaceTempView("Employee")
    return spark.sql(
        """
        SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_years
        FROM Project p
        JOIN Employee e ON p.employee_id = e.employee_id
        GROUP BY p.project_id
        """
    )
