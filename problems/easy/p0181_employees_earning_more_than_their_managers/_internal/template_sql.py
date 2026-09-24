from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, employee: DataFrame) -> DataFrame:
    # The table is available as the view "Employee".
    employee.createOrReplaceTempView("Employee")
    raise NotImplementedError
