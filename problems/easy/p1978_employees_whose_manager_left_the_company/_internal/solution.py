"""1978. Employees Whose Manager Left the Company.

https://leetcode.com/problems/employees-whose-manager-left-the-company/

Find the IDs of the employees whose salary is strictly less than 30000 and
whose manager left the company. A manager that left has no row in the
Employees table, but manager_id of the reports still has the manager ID.
Order the result by employee_id.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(employees: DataFrame) -> DataFrame:
    managers = employees.select(F.col("employee_id").alias("manager_id"))
    return (
        employees
        .filter((F.col("salary") < 30000) & F.col("manager_id").isNotNull())
        .join(managers, on="manager_id", how="left_anti")
        .select("employee_id")
        .orderBy("employee_id")
    )


def solve_sql(spark: SparkSession, employees: DataFrame) -> DataFrame:
    employees.createOrReplaceTempView("Employees")
    return spark.sql(
        """
        SELECT employee_id
        FROM Employees
        WHERE salary < 30000
          AND manager_id IS NOT NULL
          AND manager_id NOT IN (SELECT employee_id FROM Employees)
        ORDER BY employee_id
        """
    )
