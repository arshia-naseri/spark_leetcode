"""596. Classes With at Least 5 Students.

https://leetcode.com/problems/classes-with-at-least-5-students/

Find all the classes that have at least five students.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(courses: DataFrame) -> DataFrame:
    return (
        courses
        .groupBy("class")
        .agg(F.count("student").alias("cnt"))
        .where(F.col("cnt") >= 5)
        .select("class")
    )


def solve_sql(spark: SparkSession, courses: DataFrame) -> DataFrame:
    courses.createOrReplaceTempView("Courses")
    return spark.sql(
        """
        SELECT `class`
        FROM Courses
        GROUP BY `class`
        HAVING COUNT(student) >= 5
        """
    )
