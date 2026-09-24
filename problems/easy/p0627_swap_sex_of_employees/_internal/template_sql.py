from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, salary: DataFrame) -> DataFrame:
    # The table is available as the view "Salary".
    # Spark views do not support UPDATE. Use SELECT to get the updated rows.
    salary.createOrReplaceTempView("Salary")
    raise NotImplementedError
