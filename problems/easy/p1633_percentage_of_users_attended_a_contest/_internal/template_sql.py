from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, users: DataFrame, register: DataFrame) -> DataFrame:
    # The tables are available as the views "Users" and "Register".
    users.createOrReplaceTempView("Users")
    register.createOrReplaceTempView("Register")
    raise NotImplementedError
