from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, users: DataFrame, rides: DataFrame) -> DataFrame:
    # The tables are available as the views "Users" and "Rides".
    users.createOrReplaceTempView("Users")
    rides.createOrReplaceTempView("Rides")
    raise NotImplementedError
