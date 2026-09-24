"""1965. Employees With Missing Information.

https://leetcode.com/problems/employees-with-missing-information/

Report the IDs of all the employees with a missing name or a missing
salary. Sort the result by employee_id in ascending order.
"""

from pyspark.sql import DataFrame, SparkSession


def solve(employees: DataFrame, salaries: DataFrame) -> DataFrame:
    return (
        employees
        .join(salaries, on="employee_id", how="full")
        .where("name IS NULL OR salary IS NULL")
        .select("employee_id")
        .orderBy("employee_id")
    )


def solve_sql(spark: SparkSession, employees: DataFrame, salaries: DataFrame) -> DataFrame:
    employees.createOrReplaceTempView("Employees")
    salaries.createOrReplaceTempView("Salaries")
    return spark.sql(
        """
        SELECT employee_id FROM Employees
        WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
        UNION
        SELECT employee_id FROM Salaries
        WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
        ORDER BY employee_id
        """
    )
