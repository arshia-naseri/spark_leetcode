CUSTOMER_SCHEMA = "id INT, name STRING, referee_id INT"
OUTPUT_SCHEMA = "name STRING"

EXAMPLE_CUSTOMER = [
    (1, "Will", None),
    (2, "Jane", None),
    (3, "Alex", 2),
    (4, "Bill", None),
    (5, "Zack", 1),
    (6, "Mark", 2),
]
EXAMPLE_OUTPUT = [
    ("Will",),
    ("Jane",),
    ("Bill",),
    ("Zack",),
]

# Each case: (customer rows, expected output rows).
CASES = [
    (EXAMPLE_CUSTOMER, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # All customers are referred by customer 2: no match.
    ([(1, "Ann", 2), (3, "Bob", 2)], []),
    # No customer has a referee: all names.
    ([(1, "Ann", None), (2, "Bob", None)], [("Ann",), ("Bob",)]),
    # Duplicate names: keep each row.
    (
        [(1, "Sam", None), (2, "Sam", 3), (3, "Sam", 2)],
        [("Sam",), ("Sam",)],
    ),
]
