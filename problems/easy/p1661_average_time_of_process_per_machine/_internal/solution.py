"""1661. Average Time of Process per Machine.

https://leetcode.com/problems/average-time-of-process-per-machine/

For each machine, find the average time to complete a process. The time of a
process is the "end" timestamp minus the "start" timestamp. Round the average
to 3 decimal places.
"""

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def solve(activity: DataFrame) -> DataFrame:
    # Give "end" a positive sign and "start" a negative sign. The sum for one
    # machine is then the total time of all its processes.
    signed = F.when(F.col("activity_type") == "end", F.col("timestamp")).otherwise(
        -F.col("timestamp")
    )
    return activity.groupBy("machine_id").agg(
        F.round(F.sum(signed) / F.countDistinct("process_id"), 3).alias("processing_time")
    )


def solve_sql(spark: SparkSession, activity: DataFrame) -> DataFrame:
    activity.createOrReplaceTempView("Activity")
    return spark.sql(
        """
        SELECT s.machine_id,
               ROUND(AVG(e.timestamp - s.timestamp), 3) AS processing_time
        FROM Activity s
        JOIN Activity e
          ON s.machine_id = e.machine_id
         AND s.process_id = e.process_id
         AND s.activity_type = 'start'
         AND e.activity_type = 'end'
        GROUP BY s.machine_id
        """
    )
