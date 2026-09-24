import sys

from common.practice import load
from common.spark import get_spark

from .data import EXAMPLE_TRANSACTIONS, EXAMPLE_USERS, TRANSACTIONS_SCHEMA, USERS_SCHEMA

if __name__ == "__main__":
    # Default: run the practice files. Give "solution" as an argument to run solution.py.
    module_name = "solution" if sys.argv[1:] == ["solution"] else "practice"
    module = lambda method: load(__package__, module_name, method)  # noqa: E731
    spark = get_spark()
    users = spark.createDataFrame(EXAMPLE_USERS, USERS_SCHEMA)
    transactions = spark.createDataFrame(EXAMPLE_TRANSACTIONS, TRANSACTIONS_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module("dataframe").solve(users, transactions)),
        ("SQL", lambda: module("sql").solve_sql(spark, users, transactions)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()
