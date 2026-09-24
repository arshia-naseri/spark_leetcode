EMPLOYEES_SCHEMA = "employee_id INT, name STRING, reports_to INT, age INT"
OUTPUT_SCHEMA = "employee_id INT, name STRING, reports_count BIGINT, average_age INT"

EXAMPLE_EMPLOYEES = [
    (9, "Hercy", None, 43),
    (6, "Alice", 9, 41),
    (4, "Bob", 9, 36),
    (2, "Winston", None, 37),
]
EXAMPLE_OUTPUT = [
    (9, "Hercy", 2, 39),
]

# Each case: (employees rows, expected output rows).
CASES = [
    (EXAMPLE_EMPLOYEES, EXAMPLE_OUTPUT),
    # LeetCode example 2: a manager can also report to a different manager.
    (
        [
            (1, "Michael", None, 45),
            (2, "Alice", 1, 38),
            (3, "Bob", 1, 42),
            (4, "Charlie", 2, 34),
            (5, "David", 2, 40),
            (6, "Eve", 3, 37),
            (7, "Frank", None, 50),
            (8, "Grace", None, 48),
        ],
        [
            (1, "Michael", 2, 40),
            (2, "Alice", 2, 37),
            (3, "Bob", 1, 37),
        ],
    ),
    # Empty table.
    ([], []),
    # No employee reports to anyone, so there are no managers.
    (
        [(1, "Ann", None, 30), (2, "Ben", None, 40)],
        [],
    ),
    # reports_to has an id that is not in the table. That id is not a manager.
    (
        [(1, "Ann", None, 50), (2, "Ben", 1, 25), (3, "Cid", 99, 30)],
        [(1, "Ann", 1, 25)],
    ),
    # Rounding: 30.5 rounds up to 31, and 62 / 3 = 20.67 rounds to 21.
    (
        [
            (1, "Max", None, 60),
            (2, "Xia", 1, 30),
            (3, "Yan", 1, 31),
            (4, "Nia", None, 50),
            (5, "Pat", 4, 20),
            (6, "Quinn", 4, 21),
            (7, "Rae", 4, 21),
        ],
        [(1, "Max", 2, 31), (4, "Nia", 3, 21)],
    ),
]
