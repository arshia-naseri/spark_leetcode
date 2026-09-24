from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, users: DataFrame, transactions: DataFrame) -> DataFrame:
    # The tables are available as the views "Users" and "Transactions".
    users.createOrReplaceTempView("Users")
    transactions.createOrReplaceTempView("Transactions")
    raise NotImplementedError
