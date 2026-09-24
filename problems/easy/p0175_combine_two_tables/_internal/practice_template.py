"""175. Combine Two Tables. Write your practice solution here.

Read question.md for the problem statement.

Person:  personId INT, lastName STRING, firstName STRING
Address: addressId INT, personId INT, city STRING, state STRING
Output:  firstName, lastName, city, state (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(person: DataFrame, address: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, person: DataFrame, address: DataFrame) -> DataFrame:
    # The tables are available as the views "Person" and "Address".
    person.createOrReplaceTempView("Person")
    address.createOrReplaceTempView("Address")
    raise NotImplementedError
