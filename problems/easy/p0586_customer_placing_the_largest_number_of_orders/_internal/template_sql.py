from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, orders: DataFrame) -> DataFrame:
    # The table is available as the view "Orders".
    orders.createOrReplaceTempView("Orders")
    raise NotImplementedError
