EMPLOYEES_SCHEMA = "employee_id INT, name STRING, manager_id INT, salary INT"
OUTPUT_SCHEMA = "employee_id INT"

EXAMPLE_EMPLOYEES = [
    (3, "Mila", 9, 60301),
    (12, "Antonella", None, 31000),
    (13, "Emery", None, 67084),
    (1, "Kalel", 11, 21241),
    (9, "Mikaela", None, 50937),
    (11, "Joziah", 6, 28485),
]
EXAMPLE_OUTPUT = [(11,)]

# Each case: (employees rows, expected output rows).
CASES = [
    (EXAMPLE_EMPLOYEES, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # Low salary, but no manager (manager_id is null). The manager did not leave.
    ([(1, "Ann", None, 1000), (2, "Bob", None, 20000)], []),
    # Manager left. Salary 30000 is not strictly less than 30000; 29999 is.
    ([(1, "Ann", 7, 30000), (2, "Bob", 7, 29999)], [(2,)]),
    # All managers are still in the company.
    ([(1, "Ann", None, 50000), (2, "Bob", 1, 10000), (3, "Cy", 2, 5000)], []),
    # Many employees with the same manager that left, and one with a manager that stays.
    (
        [
            (5, "Eve", 100, 10000),
            (2, "Bob", 100, 20000),
            (8, "Hal", 200, 25000),
            (3, "Cy", 5, 15000),
            (4, "Dan", 100, 40000),
        ],
        [(2,), (5,), (8,)],
    ),
]
