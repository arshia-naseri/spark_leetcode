"""1179. Reformat Department Table.

https://leetcode.com/problems/reformat-department-table/

Reformat the table so that there is a department id column and a revenue
column for each month.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def solve(department: DataFrame) -> DataFrame:
    return (
        department
        .groupBy("id")
        .agg(*[
            F.max(F.when(F.col("month") == m, F.col("revenue"))).alias(f"{m}_Revenue")
            for m in MONTHS
        ])
    )


def solve_sql(spark: SparkSession, department: DataFrame) -> DataFrame:
    department.createOrReplaceTempView("Department")
    columns = ",\n".join(
        f"MAX(CASE WHEN month = '{m}' THEN revenue END) AS {m}_Revenue" for m in MONTHS
    )
    return spark.sql(
        f"""
        SELECT id,
        {columns}
        FROM Department
        GROUP BY id
        """
    )
