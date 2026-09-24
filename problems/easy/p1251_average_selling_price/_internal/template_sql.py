from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, prices: DataFrame, units_sold: DataFrame) -> DataFrame:
    # The tables are available as the views "Prices" and "UnitsSold".
    prices.createOrReplaceTempView("Prices")
    units_sold.createOrReplaceTempView("UnitsSold")
    raise NotImplementedError
