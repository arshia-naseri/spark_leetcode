"""1527. Patients With a Condition.

https://leetcode.com/problems/patients-with-a-condition/

Find the patient_id, patient_name, and conditions of the patients who have
Type I Diabetes. A Type I Diabetes code starts with the prefix DIAB1. The
codes in conditions are separated by spaces.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F

# A code starts at the start of the string or after a space.
PATTERN = r"(^| )DIAB1"


def solve(patients: DataFrame) -> DataFrame:
    return (
        patients
        .filter(F.col("conditions").rlike(PATTERN))
        .select("patient_id", "patient_name", "conditions")
    )


def solve_sql(spark: SparkSession, patients: DataFrame) -> DataFrame:
    patients.createOrReplaceTempView("Patients")
    return spark.sql(
        """
        SELECT patient_id, patient_name, conditions
        FROM Patients
        WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'
        """
    )
