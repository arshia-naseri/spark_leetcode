from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, person: DataFrame) -> DataFrame:
    # The table is available as the view "Person".
    # Spark views do not support DELETE. Use SELECT to get the rows that stay.
    person.createOrReplaceTempView("Person")
    raise NotImplementedError
