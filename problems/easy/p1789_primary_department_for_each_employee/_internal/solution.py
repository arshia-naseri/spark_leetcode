"""1789. Primary Department for Each Employee.

https://leetcode.com/problems/primary-department-for-each-employee/

Report each employee with the primary department. If an employee is in only
one department, report that department.
"""

from pyspark.sql import DataFrame, SparkSession, Window
from pyspark.sql import functions as F


def solve(employee: DataFrame) -> DataFrame:
    w = Window.partitionBy("employee_id")
    return (
        employee
        .withColumn("cnt", F.count("*").over(w))
        .filter((F.col("primary_flag") == "Y") | (F.col("cnt") == 1))
        .select("employee_id", "department_id")
    )


def solve_sql(spark: SparkSession, employee: DataFrame) -> DataFrame:
    employee.createOrReplaceTempView("Employee")
    return spark.sql(
        """
        SELECT employee_id, department_id
        FROM (
            SELECT *, COUNT(*) OVER (PARTITION BY employee_id) AS cnt
            FROM Employee
        ) e
        WHERE primary_flag = 'Y' OR cnt = 1
        """
    )
