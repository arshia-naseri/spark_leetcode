from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, daily_sales: DataFrame) -> DataFrame:
    # The table is available as the view "DailySales".
    daily_sales.createOrReplaceTempView("DailySales")
    raise NotImplementedError
