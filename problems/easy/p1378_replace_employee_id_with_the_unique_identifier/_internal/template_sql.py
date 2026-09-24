from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, employees: DataFrame, employee_uni: DataFrame) -> DataFrame:
    # The tables are available as the views "Employees" and "EmployeeUNI".
    employees.createOrReplaceTempView("Employees")
    employee_uni.createOrReplaceTempView("EmployeeUNI")
    raise NotImplementedError
