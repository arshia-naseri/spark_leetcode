EMPLOYEES_SCHEMA = "id INT, name STRING"
EMPLOYEE_UNI_SCHEMA = "id INT, unique_id INT"
OUTPUT_SCHEMA = "unique_id INT, name STRING"

EXAMPLE_EMPLOYEES = [
    (1, "Alice"),
    (7, "Bob"),
    (11, "Meir"),
    (90, "Winston"),
    (3, "Jonathan"),
]
EXAMPLE_EMPLOYEE_UNI = [
    (3, 1),
    (11, 2),
    (90, 3),
]
EXAMPLE_OUTPUT = [
    (None, "Alice"),
    (None, "Bob"),
    (2, "Meir"),
    (3, "Winston"),
    (1, "Jonathan"),
]

# Each case: (employees rows, employee_uni rows, expected output rows).
CASES = [
    (EXAMPLE_EMPLOYEES, EXAMPLE_EMPLOYEE_UNI, EXAMPLE_OUTPUT),
    # EmployeeUNI is empty: all unique IDs are null.
    (
        [(1, "Alice"), (2, "Bob")],
        [],
        [(None, "Alice"), (None, "Bob")],
    ),
    # Employees is empty: the result is empty.
    ([], EXAMPLE_EMPLOYEE_UNI, []),
    # No matches: EmployeeUNI ids are not in Employees.
    (
        [(1, "Alice"), (2, "Bob")],
        [(5, 10), (6, 20)],
        [(None, "Alice"), (None, "Bob")],
    ),
    # Duplicate names with different ids stay as separate rows.
    (
        [(1, "Alice"), (2, "Alice"), (3, "Bob")],
        [(1, 100), (3, 300)],
        [(100, "Alice"), (None, "Alice"), (300, "Bob")],
    ),
    # One id with two unique IDs gives two rows.
    (
        [(1, "Alice"), (2, "Bob")],
        [(1, 10), (1, 11)],
        [(10, "Alice"), (11, "Alice"), (None, "Bob")],
    ),
]
