from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, customer: DataFrame) -> DataFrame:
    # The table is available as the view "Customer".
    customer.createOrReplaceTempView("Customer")
    raise NotImplementedError
