"""584. Find Customer Referee.

https://leetcode.com/problems/find-customer-referee/

Find the names of the customers that are not referred by the customer with
id = 2. This includes the customers with no referee (referee_id is null).
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(customer: DataFrame) -> DataFrame:
    return (
        customer
        .where(F.col("referee_id").isNull() | (F.col("referee_id") != 2))
        .select("name")
    )


def solve_sql(spark: SparkSession, customer: DataFrame) -> DataFrame:
    customer.createOrReplaceTempView("Customer")
    return spark.sql(
        """
        SELECT name
        FROM Customer
        WHERE referee_id IS NULL OR referee_id != 2
        """
    )
