from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, employees: DataFrame, salaries: DataFrame) -> DataFrame:
    # The tables are available as the views "Employees" and "Salaries".
    employees.createOrReplaceTempView("Employees")
    salaries.createOrReplaceTempView("Salaries")
    raise NotImplementedError
