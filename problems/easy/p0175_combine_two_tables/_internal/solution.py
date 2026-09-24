"""175. Combine Two Tables.

https://leetcode.com/problems/combine-two-tables/

Report the first name, last name, city, and state of each person in the
Person table. If the address of a personId is not in the Address table,
report null.
"""

from pyspark.sql import DataFrame, SparkSession


def solve(person: DataFrame, address: DataFrame) -> DataFrame:
    return (
        person
        .join(address, on="personId", how="left")
        .select("firstName", "lastName", "city", "state")
    )


def solve_sql(spark: SparkSession, person: DataFrame, address: DataFrame) -> DataFrame:
    person.createOrReplaceTempView("Person")
    address.createOrReplaceTempView("Address")
    return spark.sql(
        """
        SELECT p.firstName, p.lastName, a.city, a.state
        FROM Person p
        LEFT JOIN Address a ON p.personId = a.personId
        """
    )
