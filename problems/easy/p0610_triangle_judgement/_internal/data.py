TRIANGLE_SCHEMA = "x INT, y INT, z INT"
OUTPUT_SCHEMA = "x INT, y INT, z INT, triangle STRING"

EXAMPLE_TRIANGLE = [
    (13, 15, 30),
    (10, 20, 15),
]
EXAMPLE_OUTPUT = [
    (13, 15, 30, "No"),
    (10, 20, 15, "Yes"),
]

# Each case: (triangle rows, expected output rows).
CASES = [
    (EXAMPLE_TRIANGLE, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # Sum of two sides equals the third side: no triangle.
    # The longest side is in each column once.
    (
        [(1, 2, 3), (3, 1, 2), (2, 3, 1)],
        [(1, 2, 3, "No"), (3, 1, 2, "No"), (2, 3, 1, "No")],
    ),
    # Equilateral, isosceles and scalene triangles, and one long side in each column.
    (
        [(5, 5, 5), (2, 2, 3), (3, 4, 5), (10, 1, 1), (1, 10, 1), (1, 1, 10)],
        [
            (5, 5, 5, "Yes"),
            (2, 2, 3, "Yes"),
            (3, 4, 5, "Yes"),
            (10, 1, 1, "No"),
            (1, 10, 1, "No"),
            (1, 1, 10, "No"),
        ],
    ),
]
