QUERIES_SCHEMA = "query_name STRING, result STRING, position INT, rating INT"
OUTPUT_SCHEMA = "query_name STRING, quality DOUBLE, poor_query_percentage DOUBLE"

EXAMPLE_QUERIES = [
    ("Dog", "Golden Retriever", 1, 5),
    ("Dog", "German Shepherd", 2, 5),
    ("Dog", "Mule", 200, 1),
    ("Cat", "Shirazi", 5, 2),
    ("Cat", "Siamese", 3, 3),
    ("Cat", "Sphynx", 7, 4),
]
EXAMPLE_OUTPUT = [
    ("Dog", 2.50, 33.33),
    ("Cat", 0.66, 33.33),
]

# Each case: (queries rows, expected output rows).
CASES = [
    (EXAMPLE_QUERIES, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # All queries are poor.
    (
        [("A", "x", 1, 1), ("A", "y", 2, 2)],
        [("A", 1.0, 100.0)],
    ),
    # No poor queries. Rating 3 is not poor. Quality 0.875 rounds up to 0.88.
    (
        [("B", "x", 4, 3), ("B", "y", 5, 5)],
        [("B", 0.88, 0.0)],
    ),
    # Duplicate rows count each time.
    (
        [("C", "r", 2, 4), ("C", "r", 2, 4), ("C", "s", 4, 1)],
        [("C", 1.42, 33.33)],
    ),
    # One row for each query name.
    (
        [("D", "x", 500, 1), ("E", "y", 1, 5)],
        [("D", 0.0, 100.0), ("E", 5.0, 0.0)],
    ),
]
