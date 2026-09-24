from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, users: DataFrame) -> DataFrame:
    # The table is available as the view "Users".
    users.createOrReplaceTempView("Users")
    raise NotImplementedError
