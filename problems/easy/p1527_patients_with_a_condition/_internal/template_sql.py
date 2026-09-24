from pyspark.sql import DataFrame, SparkSession


def solve_sql(spark: SparkSession, patients: DataFrame) -> DataFrame:
    # The table is available as the view "Patients".
    patients.createOrReplaceTempView("Patients")
    raise NotImplementedError
