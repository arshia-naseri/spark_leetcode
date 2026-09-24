"""610. Triangle Judgement.

https://leetcode.com/problems/triangle-judgement/

Report for every three line segments whether they can form a triangle.
Three segments form a triangle when the sum of each two sides is more
than the third side.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(triangle: DataFrame) -> DataFrame:
    x, y, z = F.col("x"), F.col("y"), F.col("z")
    is_triangle = (x + y > z) & (x + z > y) & (y + z > x)
    return triangle.select(
        "x", "y", "z",
        F.when(is_triangle, "Yes").otherwise("No").alias("triangle"),
    )


def solve_sql(spark: SparkSession, triangle: DataFrame) -> DataFrame:
    triangle.createOrReplaceTempView("Triangle")
    return spark.sql(
        """
        SELECT x, y, z,
               CASE WHEN x + y > z AND x + z > y AND y + z > x
                    THEN 'Yes' ELSE 'No' END AS triangle
        FROM Triangle
        """
    )
