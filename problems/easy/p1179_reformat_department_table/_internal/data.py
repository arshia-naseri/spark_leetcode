MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

DEPARTMENT_SCHEMA = "id INT, revenue INT, month STRING"
OUTPUT_SCHEMA = "id INT, " + ", ".join(f"{m}_Revenue INT" for m in MONTHS)


def _row(dept_id, **revenue):
    """Make one output row. Give the revenue for each month as a keyword (Jan=8000)."""
    return (dept_id, *(revenue.get(m) for m in MONTHS))


EXAMPLE_DEPARTMENT = [
    (1, 8000, "Jan"),
    (2, 9000, "Jan"),
    (3, 10000, "Feb"),
    (1, 7000, "Feb"),
    (1, 6000, "Mar"),
]
EXAMPLE_OUTPUT = [
    _row(1, Jan=8000, Feb=7000, Mar=6000),
    _row(2, Jan=9000),
    _row(3, Feb=10000),
]

# Each case: (department rows, expected output rows).
CASES = [
    (EXAMPLE_DEPARTMENT, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # One department with revenue in all 12 months.
    (
        [(7, (i + 1) * 100, m) for i, m in enumerate(MONTHS)],
        [(7, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200)],
    ),
    # Only the last month. All other columns are null.
    ([(4, 500, "Dec")], [_row(4, Dec=500)]),
    # Null revenue and zero revenue stay as they are.
    (
        [(1, None, "Jan"), (1, 0, "Feb"), (2, 300, "Jan")],
        [_row(1, Feb=0), _row(2, Jan=300)],
    ),
]
