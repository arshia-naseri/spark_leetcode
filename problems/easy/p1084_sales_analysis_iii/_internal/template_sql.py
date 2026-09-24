from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, product: DataFrame, sales: DataFrame) -> DataFrame:
    # The tables are available as the views "Product" and "Sales".
    product.createOrReplaceTempView("Product")
    sales.createOrReplaceTempView("Sales")
    raise NotImplementedError
