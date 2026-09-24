"""1527. Patients With a Condition. Write your practice solution here.

Read question.md for the problem statement.

Patients: patient_id INT, patient_name STRING, conditions STRING
Output:   patient_id, patient_name, conditions (any order)
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F  # noqa: F401


def solve(patients: DataFrame) -> DataFrame:
    raise NotImplementedError


def solve_sql(spark: SparkSession, patients: DataFrame) -> DataFrame:
    # The table is available as the view "Patients".
    patients.createOrReplaceTempView("Patients")
    raise NotImplementedError
