VISITS_SCHEMA = "visit_id INT, customer_id INT"
TRANSACTIONS_SCHEMA = "transaction_id INT, visit_id INT, amount INT"
OUTPUT_SCHEMA = "customer_id INT, count_no_trans BIGINT"

EXAMPLE_VISITS = [
    (1, 23),
    (2, 9),
    (4, 30),
    (5, 54),
    (6, 96),
    (7, 54),
    (8, 54),
]
EXAMPLE_TRANSACTIONS = [
    (2, 5, 310),
    (3, 5, 300),
    (9, 5, 200),
    (12, 1, 910),
    (13, 2, 970),
]
EXAMPLE_OUTPUT = [
    (54, 2),
    (30, 1),
    (96, 1),
]

# Each case: (visits rows, transactions rows, expected output rows).
CASES = [
    (EXAMPLE_VISITS, EXAMPLE_TRANSACTIONS, EXAMPLE_OUTPUT),
    # No transactions: each visit counts.
    (
        EXAMPLE_VISITS,
        [],
        [(23, 1), (9, 1), (30, 1), (54, 3), (96, 1)],
    ),
    # No visits: empty output.
    ([], EXAMPLE_TRANSACTIONS, []),
    # Each visit has a transaction: empty output.
    (
        [(1, 10), (2, 20)],
        [(1, 1, 100), (2, 2, 200), (3, 2, 50)],
        [],
    ),
    # A transaction for a visit that is not in Visits does not change the result.
    (
        [(1, 10), (2, 10), (3, 20)],
        [(1, 99, 100), (2, 3, 40)],
        [(10, 2)],
    ),
]
