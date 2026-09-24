EMPLOYEE_SCHEMA = "id INT, name STRING, salary INT, managerId INT"
OUTPUT_SCHEMA = "Employee STRING"

EXAMPLE_EMPLOYEE = [
    (1, "Joe", 70000, 3),
    (2, "Henry", 80000, 4),
    (3, "Sam", 60000, None),
    (4, "Max", 90000, None),
]
EXAMPLE_OUTPUT = [
    ("Joe",),
]

# Each case: (employee rows, expected output rows).
CASES = [
    (EXAMPLE_EMPLOYEE, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # No employee has a manager.
    ([(1, "Ann", 100, None), (2, "Bob", 200, None)], []),
    # Equal salary is not "more than".
    ([(1, "Ann", 100, 2), (2, "Bob", 100, None)], []),
    # The managerId is not in the table.
    ([(1, "Ann", 100, 9)], []),
    # Chain of managers and two employees with the same name.
    (
        [
            (1, "Ann", 300, 2),
            (2, "Bob", 200, 3),
            (3, "Cid", 100, None),
            (4, "Ann", 250, 2),
        ],
        [("Ann",), ("Bob",), ("Ann",)],
    ),
]
