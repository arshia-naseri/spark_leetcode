"""182. Duplicate Emails.

https://leetcode.com/problems/duplicate-emails/

Report all the emails that occur more than one time in the Person table.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(person: DataFrame) -> DataFrame:
    return (
        person
        .groupBy("email")
        .agg(F.count("*").alias("cnt"))
        .where(F.col("cnt") > 1)
        .select(F.col("email").alias("Email"))
    )


def solve_sql(spark: SparkSession, person: DataFrame) -> DataFrame:
    person.createOrReplaceTempView("Person")
    return spark.sql(
        """
        SELECT email AS Email
        FROM Person
        GROUP BY email
        HAVING COUNT(*) > 1
        """
    )
