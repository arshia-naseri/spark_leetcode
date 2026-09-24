from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, customers: DataFrame, orders: DataFrame) -> DataFrame:
    # The tables are available as the views "Customers" and "Orders".
    customers.createOrReplaceTempView("Customers")
    orders.createOrReplaceTempView("Orders")
    raise NotImplementedError
