"""1407. Top Travellers. Write your practice solution here.

Read question.md for the problem statement.

Users:  id INT, name STRING
Rides:  id INT, user_id INT, distance INT
Output: name, travelled_distance
        (order by travelled_distance descending, then name ascending)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(users: DataFrame, rides: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, users: DataFrame, rides: DataFrame) -> DataFrame:
    # The tables are available as the views "Users" and "Rides".
    users.createOrReplaceTempView("Users")
    rides.createOrReplaceTempView("Rides")
    raise NotImplementedError
