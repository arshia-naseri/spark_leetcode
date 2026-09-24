EMPLOYEES_SCHEMA = "employee_id INT, name STRING"
SALARIES_SCHEMA = "employee_id INT, salary INT"
OUTPUT_SCHEMA = "employee_id INT"

EXAMPLE_EMPLOYEES = [
    (2, "Crew"),
    (4, "Haven"),
    (5, "Kristian"),
]
EXAMPLE_SALARIES = [
    (5, 76071),
    (1, 22517),
    (4, 63539),
]
EXAMPLE_OUTPUT = [
    (1,),
    (2,),
]

# Each case: (employees rows, salaries rows, expected output rows).
CASES = [
    (EXAMPLE_EMPLOYEES, EXAMPLE_SALARIES, EXAMPLE_OUTPUT),
    # No salaries: all employees have a missing salary.
    (EXAMPLE_EMPLOYEES, [], [(2,), (4,), (5,)]),
    # No employees: all salary rows have a missing name.
    ([], EXAMPLE_SALARIES, [(1,), (4,), (5,)]),
    # Both tables empty.
    ([], [], []),
    # All information is present: no rows.
    (
        [(1, "Ann"), (2, "Bob")],
        [(2, 500), (1, 400)],
        [],
    ),
    # No shared IDs: all IDs from the two tables.
    (
        [(3, "Cat"), (1, "Ann")],
        [(2, 500), (4, 700)],
        [(1,), (2,), (3,), (4,)],
    ),
]
