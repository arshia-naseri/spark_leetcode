EMPLOYEES_SCHEMA = "employee_id INT, name STRING, salary INT"
OUTPUT_SCHEMA = "employee_id INT, bonus INT"

EXAMPLE_EMPLOYEES = [
    (2, "Meir", 3000),
    (3, "Michael", 3800),
    (7, "Addilyn", 7400),
    (8, "Juan", 6100),
    (9, "Kannon", 7700),
]
EXAMPLE_OUTPUT = [
    (2, 0),
    (3, 0),
    (7, 7400),
    (8, 0),
    (9, 7700),
]

# Each case: (employees rows, expected output rows).
CASES = [
    (EXAMPLE_EMPLOYEES, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # All IDs are odd and no name starts with "M": each employee gets the full salary.
    (
        [(1, "Anna", 1000), (5, "Bob", 2000)],
        [(1, 1000), (5, 2000)],
    ),
    # All names start with "M": no employee gets a bonus.
    (
        [(1, "Mia", 1000), (3, "Max", 2000), (4, "Mo", 500)],
        [(1, 0), (3, 0), (4, 0)],
    ),
    # "M" in the name but not at the start: the bonus is the salary.
    (
        [(11, "Sam", 4000), (13, "Emma", 4500)],
        [(11, 4000), (13, 4500)],
    ),
    # A name that starts with a lowercase "m": no bonus. LeetCode uses MySQL,
    # and MySQL compares 'M' and 'm' as equal.
    (
        [(1, "mia", 1000), (3, "nina", 2000)],
        [(1, 0), (3, 2000)],
    ),
    # Salary 0 and a large odd ID.
    (
        [(1, "Zed", 0), (99999, "Lee", 123456)],
        [(1, 0), (99999, 123456)],
    ),
]
