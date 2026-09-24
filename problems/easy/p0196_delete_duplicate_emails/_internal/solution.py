"""196. Delete Duplicate Emails.

https://leetcode.com/problems/delete-duplicate-emails/

Delete all duplicate emails. For each email, keep only the row with the
smallest id. Spark DataFrames are immutable, thus return the Person table
after the delete as a new DataFrame.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(person: DataFrame) -> DataFrame:
    return person.groupBy("email").agg(F.min("id").alias("id")).select("id", "email")


def solve_sql(spark: SparkSession, person: DataFrame) -> DataFrame:
    person.createOrReplaceTempView("Person")
    # LeetCode wants a DELETE statement. Spark temp views do not support
    # DELETE, thus SELECT the rows that stay after the delete.
    return spark.sql(
        """
        SELECT p.id, p.email
        FROM Person p
        WHERE NOT EXISTS (
            SELECT 1
            FROM Person q
            WHERE q.email = p.email AND q.id < p.id
        )
        """
    )
