from pyspark.sql import SparkSession


def get_spark(app_name: str = "spark-leetcode") -> SparkSession:
    spark = (
        SparkSession.builder
        .master("local[1]")
        .appName(app_name)
        # The default of 200 shuffle partitions is slow on small data.
        .config("spark.sql.shuffle.partitions", "1")
        .config("spark.ui.enabled", "false")
        .config("spark.sql.session.timeZone", "UTC")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("ERROR")
    return spark
