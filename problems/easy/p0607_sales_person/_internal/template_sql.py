from pyspark.sql import DataFrame, SparkSession


def solve_sql(
    spark: SparkSession, sales_person: DataFrame, company: DataFrame, orders: DataFrame
) -> DataFrame:
    # The tables are available as the views "SalesPerson", "Company" and "Orders".
    sales_person.createOrReplaceTempView("SalesPerson")
    company.createOrReplaceTempView("Company")
    orders.createOrReplaceTempView("Orders")
    raise NotImplementedError
