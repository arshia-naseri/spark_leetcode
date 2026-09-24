MY_NUMBERS_SCHEMA = "num INT"
OUTPUT_SCHEMA = "num INT"

EXAMPLE_MY_NUMBERS = [(8,), (8,), (3,), (3,), (1,), (4,), (5,), (6,)]
EXAMPLE_OUTPUT = [(6,)]

# Each case: (my_numbers rows, expected output rows).
CASES = [
    (EXAMPLE_MY_NUMBERS, EXAMPLE_OUTPUT),
    # LeetCode example 2: no single number gives one null row.
    ([(8,), (8,), (7,), (7,), (3,), (3,), (3,)], [(None,)]),
    # Empty table gives one null row.
    ([], [(None,)]),
    # One row only.
    ([(42,)], [(42,)]),
    # Negative numbers. The largest single number is -1.
    ([(-5,), (-1,), (2,), (2,), (-3,)], [(-1,)]),
    # The largest number is a duplicate. The next single number is the answer.
    ([(10,), (10,), (10,), (9,), (1,), (1,)], [(9,)]),
    # A null value is not a number. Ignore it.
    ([(None,), (None,), (None,), (2,)], [(2,)]),
    # Only null values give one null row.
    ([(None,)], [(None,)]),
]
