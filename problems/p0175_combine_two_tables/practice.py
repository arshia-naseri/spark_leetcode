"""175. Combine Two Tables. Write your practice solution here.

https://leetcode.com/problems/combine-two-tables/

Report the first name, last name, city, and state of each person in the
Person table. If the address of a personId is not in the Address table,
report null.

Person:  personId INT, lastName STRING, firstName STRING
Address: addressId INT, personId INT, city STRING, state STRING
Output:  firstName, lastName, city, state (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(person: DataFrame, address: DataFrame) -> DataFrame:
    # raise NotImplementedError
    return (
            person
            .join(address, on="personId", how="left")
            .select("firstName", "lastName", "city")
        )


def solve_sql(spark: SparkSession, person: DataFrame, address: DataFrame) -> DataFrame:
    # The tables are available as the views "Person" and "Address".
    person.createOrReplaceTempView("Person")
    address.createOrReplaceTempView("Address")
    raise NotImplementedError
