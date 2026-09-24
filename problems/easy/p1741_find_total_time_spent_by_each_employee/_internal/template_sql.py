from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, employees: DataFrame) -> DataFrame:
    # The table is available as the view "Employees".
    employees.createOrReplaceTempView("Employees")
    raise NotImplementedError
