from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, products: DataFrame, orders: DataFrame) -> DataFrame:
    # The tables are available as the views "Products" and "Orders".
    products.createOrReplaceTempView("Products")
    orders.createOrReplaceTempView("Orders")
    raise NotImplementedError
