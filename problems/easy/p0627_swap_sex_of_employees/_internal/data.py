SALARY_SCHEMA = "id INT, name STRING, sex STRING, salary INT"
OUTPUT_SCHEMA = "id INT, name STRING, sex STRING, salary INT"

EXAMPLE_SALARY = [
    (1, "A", "m", 2500),
    (2, "B", "f", 1500),
    (3, "C", "m", 5500),
    (4, "D", "f", 500),
]
EXAMPLE_OUTPUT = [
    (1, "A", "f", 2500),
    (2, "B", "m", 1500),
    (3, "C", "f", 5500),
    (4, "D", "m", 500),
]

# Each case: (salary rows, expected output rows).
CASES = [
    (EXAMPLE_SALARY, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # All rows are 'm'.
    (
        [(1, "A", "m", 100), (2, "B", "m", 200)],
        [(1, "A", "f", 100), (2, "B", "f", 200)],
    ),
    # All rows are 'f'.
    (
        [(1, "A", "f", 100), (2, "B", "f", 200)],
        [(1, "A", "m", 100), (2, "B", "m", 200)],
    ),
    # One row.
    ([(7, "Z", "f", 0)], [(7, "Z", "m", 0)]),
    # Two rows with the same name and salary.
    (
        [(1, "A", "m", 300), (2, "A", "f", 300)],
        [(1, "A", "f", 300), (2, "A", "m", 300)],
    ),
]
