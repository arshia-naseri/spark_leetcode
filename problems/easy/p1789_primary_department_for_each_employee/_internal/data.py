EMPLOYEE_SCHEMA = "employee_id INT, department_id INT, primary_flag STRING"
OUTPUT_SCHEMA = "employee_id INT, department_id INT"

EXAMPLE_EMPLOYEE = [
    (1, 1, "N"),
    (2, 1, "Y"),
    (2, 2, "N"),
    (3, 3, "N"),
    (4, 2, "N"),
    (4, 3, "Y"),
    (4, 4, "N"),
]
EXAMPLE_OUTPUT = [
    (1, 1),
    (2, 1),
    (3, 3),
    (4, 3),
]

# Each case: (employee rows, expected output rows).
CASES = [
    (EXAMPLE_EMPLOYEE, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # All employees have only one department.
    (
        [(1, 10, "N"), (2, 20, "N"), (3, 10, "N")],
        [(1, 10), (2, 20), (3, 10)],
    ),
    # All employees have many departments. The primary is not the first row.
    (
        [(1, 5, "N"), (1, 6, "N"), (1, 7, "Y"), (2, 5, "Y"), (2, 6, "N")],
        [(1, 7), (2, 5)],
    ),
    # One employee with one department.
    ([(7, 3, "N")], [(7, 3)]),
]
