import json
from pathlib import Path

from pyspark.sql import SparkSession

# Local Spark settings. The web UI writes this file. It is git-ignored.
CONFIG_FILE = Path(__file__).resolve().parent.parent / "spark_config.json"

DEFAULTS = {
    "spark.master": "local[1]",
    # The default of 200 shuffle partitions is slow on small data.
    "spark.sql.shuffle.partitions": "1",
    "spark.ui.enabled": "false",
    "spark.sql.session.timeZone": "UTC",
}


def load_config() -> dict[str, str]:
    """Return the settings in CONFIG_FILE, or DEFAULTS if the file does not exist."""
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text())
    return dict(DEFAULTS)


def save_config(config: dict[str, str]) -> None:
    """Write the settings to CONFIG_FILE. Remove the file if the settings are DEFAULTS."""
    if config == DEFAULTS:
        CONFIG_FILE.unlink(missing_ok=True)
    else:
        CONFIG_FILE.write_text(json.dumps(config, indent=2) + "\n")


def get_spark(app_name: str = "spark-leetcode") -> SparkSession:
    builder = SparkSession.builder.appName(app_name)
    for key, value in load_config().items():
        builder = builder.config(key, value)
    spark = builder.getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    return spark
