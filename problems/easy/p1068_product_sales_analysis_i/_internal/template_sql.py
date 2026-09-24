from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, sales: DataFrame, product: DataFrame) -> DataFrame:
    # The tables are available as the views "Sales" and "Product".
    sales.createOrReplaceTempView("Sales")
    product.createOrReplaceTempView("Product")
    raise NotImplementedError
