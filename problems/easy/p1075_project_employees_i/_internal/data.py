PROJECT_SCHEMA = "project_id INT, employee_id INT"
EMPLOYEE_SCHEMA = "employee_id INT, name STRING, experience_years INT"
OUTPUT_SCHEMA = "project_id INT, average_years DOUBLE"

EXAMPLE_PROJECT = [
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 4),
]
EXAMPLE_EMPLOYEE = [
    (1, "Khaled", 3),
    (2, "Ali", 2),
    (3, "John", 1),
    (4, "Doe", 2),
]
EXAMPLE_OUTPUT = [
    (1, 2.0),
    (2, 2.5),
]

# Each case: (project rows, employee rows, expected output rows).
CASES = [
    (EXAMPLE_PROJECT, EXAMPLE_EMPLOYEE, EXAMPLE_OUTPUT),
    # No projects: empty output.
    ([], EXAMPLE_EMPLOYEE, []),
    # Both tables empty.
    ([], [], []),
    # One employee on each project. Employee 3 is on no project.
    (
        [(1, 1), (2, 2)],
        [(1, "A", 7), (2, "B", 0), (3, "C", 5)],
        [(1, 7.0), (2, 0.0)],
    ),
    # Average with repeating decimals: 5 / 3 = 1.666... gives 1.67, 1 / 3 gives 0.33.
    (
        [(1, 1), (1, 2), (1, 3), (2, 1), (2, 4), (2, 5)],
        [(1, "A", 1), (2, "B", 2), (3, "C", 2), (4, "D", 0), (5, "E", 0)],
        [(1, 1.67), (2, 0.33)],
    ),
    # Half rounds up: 1 / 8 = 0.125 gives 0.13.
    (
        [(1, i) for i in range(1, 9)],
        [(i, f"E{i}", 1 if i == 1 else 0) for i in range(1, 9)],
        [(1, 0.13)],
    ),
]
