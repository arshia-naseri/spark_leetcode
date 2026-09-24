from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, products: DataFrame) -> DataFrame:
    # The table is available as the view "Products".
    products.createOrReplaceTempView("Products")
    raise NotImplementedError
