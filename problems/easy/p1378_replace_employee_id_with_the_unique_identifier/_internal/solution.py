"""1378. Replace Employee ID With The Unique Identifier.

https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

Show the unique ID and the name of each employee. If an employee does not
have a unique ID, show null.
"""

from pyspark.sql import DataFrame, SparkSession


def solve(employees: DataFrame, employee_uni: DataFrame) -> DataFrame:
    return (
        employees
        .join(employee_uni, on="id", how="left")
        .select("unique_id", "name")
    )


def solve_sql(spark: SparkSession, employees: DataFrame, employee_uni: DataFrame) -> DataFrame:
    employees.createOrReplaceTempView("Employees")
    employee_uni.createOrReplaceTempView("EmployeeUNI")
    return spark.sql(
        """
        SELECT u.unique_id, e.name
        FROM Employees e
        LEFT JOIN EmployeeUNI u ON e.id = u.id
        """
    )
