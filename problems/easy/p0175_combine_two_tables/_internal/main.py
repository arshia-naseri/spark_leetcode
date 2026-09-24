import sys

from common.spark import get_spark

from .. import practice
from . import solution
from .data import ADDRESS_SCHEMA, EXAMPLE_ADDRESS, EXAMPLE_PERSON, PERSON_SCHEMA

if __name__ == "__main__":
    # Default: run practice.py. Give "solution" as an argument to run solution.py.
    module = solution if sys.argv[1:] == ["solution"] else practice
    spark = get_spark()
    person = spark.createDataFrame(EXAMPLE_PERSON, PERSON_SCHEMA)
    address = spark.createDataFrame(EXAMPLE_ADDRESS, ADDRESS_SCHEMA)

    for name, run in [
        ("DataFrame API", lambda: module.solve(person, address)),
        ("SQL", lambda: module.solve_sql(spark, person, address)),
    ]:
        print(f"{name}:")
        try:
            run().show()
        except NotImplementedError:
            print("  not implemented yet\n")

    spark.stop()
