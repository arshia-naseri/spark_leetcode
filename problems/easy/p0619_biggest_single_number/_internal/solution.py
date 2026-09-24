"""619. Biggest Single Number.

https://leetcode.com/problems/biggest-single-number/

A single number is a number that appears only once in the MyNumbers table.
Report the largest single number. If there is no single number, report null.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(my_numbers: DataFrame) -> DataFrame:
    # A global aggregate always gives one row. MAX of no rows is null.
    return (
        my_numbers
        .groupBy("num")
        .agg(F.count("*").alias("cnt"))
        .filter(F.col("cnt") == 1)
        .agg(F.max("num").alias("num"))
    )


def solve_sql(spark: SparkSession, my_numbers: DataFrame) -> DataFrame:
    my_numbers.createOrReplaceTempView("MyNumbers")
    return spark.sql(
        """
        SELECT MAX(num) AS num
        FROM (
            SELECT num
            FROM MyNumbers
            GROUP BY num
            HAVING COUNT(*) = 1
        ) t
        """
    )
