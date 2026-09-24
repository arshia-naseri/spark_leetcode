"""627. Swap Sex of Employees.

https://leetcode.com/problems/swap-sex-of-employees/

Change all 'f' values to 'm' and all 'm' values to 'f' in the sex column of
the Salary table. Spark DataFrames are immutable, thus return the Salary table
after the update as a new DataFrame.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(salary: DataFrame) -> DataFrame:
    return salary.withColumn(
        "sex", F.when(F.col("sex") == "m", "f").otherwise("m")
    )


def solve_sql(spark: SparkSession, salary: DataFrame) -> DataFrame:
    salary.createOrReplaceTempView("Salary")
    return spark.sql(
        """
        SELECT id, name, CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END AS sex, salary
        FROM Salary
        """
    )
