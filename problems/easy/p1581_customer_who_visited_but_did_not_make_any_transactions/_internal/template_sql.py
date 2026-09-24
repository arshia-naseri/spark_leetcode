from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, visits: DataFrame, transactions: DataFrame) -> DataFrame:
    # The tables are available as the views "Visits" and "Transactions".
    visits.createOrReplaceTempView("Visits")
    transactions.createOrReplaceTempView("Transactions")
    raise NotImplementedError
