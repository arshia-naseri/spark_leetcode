"""1517. Find Users With Valid E-Mails.

https://leetcode.com/problems/find-users-with-valid-e-mails/

Find the users who have a valid mail. The prefix must start with a letter
and can contain letters, digits, "_", "." and "-". The domain must be
exactly "@leetcode.com" in lowercase.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F

# Spark regular expressions are case-sensitive. Thus "@LeetCode.com" does not match.
VALID_MAIL = r"^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$"


def solve(users: DataFrame) -> DataFrame:
    return users.filter(F.col("mail").rlike(VALID_MAIL))


def solve_sql(spark: SparkSession, users: DataFrame) -> DataFrame:
    users.createOrReplaceTempView("Users")
    return spark.sql(
        r"""
        SELECT user_id, name, mail
        FROM Users
        WHERE mail RLIKE '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'
        """
    )
