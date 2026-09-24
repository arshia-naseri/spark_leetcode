PERSON_SCHEMA = "personId INT, lastName STRING, firstName STRING"
ADDRESS_SCHEMA = "addressId INT, personId INT, city STRING, state STRING"
OUTPUT_SCHEMA = "firstName STRING, lastName STRING, city STRING, state STRING"

EXAMPLE_PERSON = [
    (1, "Wang", "Allen"),
    (2, "Alice", "Bob"),
]
EXAMPLE_ADDRESS = [
    (1, 2, "New York City", "New York"),
    (2, 3, "Leetcode", "California"),
]
EXAMPLE_OUTPUT = [
    ("Allen", "Wang", None, None),
    ("Bob", "Alice", "New York City", "New York"),
]

# Each case: (person rows, address rows, expected output rows).
CASES = [
    (EXAMPLE_PERSON, EXAMPLE_ADDRESS, EXAMPLE_OUTPUT),
    (
        EXAMPLE_PERSON,
        [],
        [("Allen", "Wang", None, None), ("Bob", "Alice", None, None)],
    ),
    ([], EXAMPLE_ADDRESS, []),
    (
        [(1, "Wang", "Allen"), (2, "Alice", "Bob")],
        [(10, 1, "Boston", "MA"), (11, 2, "Austin", "TX")],
        [("Allen", "Wang", "Boston", "MA"), ("Bob", "Alice", "Austin", "TX")],
    ),
]
