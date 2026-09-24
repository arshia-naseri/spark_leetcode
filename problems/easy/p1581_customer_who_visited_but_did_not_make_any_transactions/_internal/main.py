import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import EXAMPLE_TRANSACTIONS, EXAMPLE_VISITS, TRANSACTIONS_SCHEMA, VISITS_SCHEMA

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    visits = spark.createDataFrame(EXAMPLE_VISITS, VISITS_SCHEMA)
    transactions = spark.createDataFrame(EXAMPLE_TRANSACTIONS, TRANSACTIONS_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(visits, transactions)),
        ("SQL", lambda: module.solve_sql(spark, visits, transactions)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()
