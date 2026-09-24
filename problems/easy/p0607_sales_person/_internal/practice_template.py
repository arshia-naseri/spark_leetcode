"""607. Sales Person. Write your practice solution here.

Read question.md for the problem statement.

SalesPerson: sales_id INT, name STRING, salary INT, commission_rate INT, hire_date DATE
Company:     com_id INT, name STRING, city STRING
Orders:      order_id INT, order_date DATE, com_id INT, sales_id INT, amount INT
Output:      name (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(sales_person: DataFrame, company: DataFrame, orders: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(
    spark: SparkSession, sales_person: DataFrame, company: DataFrame, orders: DataFrame
) -> DataFrame:
    # The tables are available as the views "SalesPerson", "Company" and "Orders".
    sales_person.createOrReplaceTempView("SalesPerson")
    company.createOrReplaceTempView("Company")
    orders.createOrReplaceTempView("Orders")
    raise NotImplementedError
