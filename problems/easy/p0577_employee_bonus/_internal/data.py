EMPLOYEE_SCHEMA = "empId INT, name STRING, supervisor INT, salary INT"
BONUS_SCHEMA = "empId INT, bonus INT"
OUTPUT_SCHEMA = "name STRING, bonus INT"

EXAMPLE_EMPLOYEE = [
    (3, "Brad", None, 4000),
    (1, "John", 3, 1000),
    (2, "Dan", 3, 2000),
    (4, "Thomas", 3, 4000),
]
EXAMPLE_BONUS = [
    (2, 500),
    (4, 2000),
]
EXAMPLE_OUTPUT = [
    ("Brad", None),
    ("John", None),
    ("Dan", 500),
]

# Each case: (employee rows, bonus rows, expected output rows).
CASES = [
    (EXAMPLE_EMPLOYEE, EXAMPLE_BONUS, EXAMPLE_OUTPUT),
    # No bonus rows: all employees are in the output with a null bonus.
    (
        EXAMPLE_EMPLOYEE,
        [],
        [("Brad", None), ("John", None), ("Dan", None), ("Thomas", None)],
    ),
    # No employees: the output is empty.
    ([], [], []),
    # Boundary: 1000 is not less than 1000. 999 and 0 are less than 1000.
    (
        [(1, "Ann", None, 100), (2, "Ben", 1, 200), (3, "Cal", 1, 300)],
        [(1, 1000), (2, 999), (3, 0)],
        [("Ben", 999), ("Cal", 0)],
    ),
    # All employees have a bonus of 1000 or more: the output is empty.
    (
        [(1, "Ann", None, 100), (2, "Ben", 1, 200)],
        [(1, 1000), (2, 5000)],
        [],
    ),
    # Two employees have the same name: keep both rows.
    (
        [(1, "Sam", None, 100), (2, "Sam", 1, 200), (3, "Sam", 1, 300)],
        [(1, 100)],
        [("Sam", 100), ("Sam", None), ("Sam", None)],
    ),
]
