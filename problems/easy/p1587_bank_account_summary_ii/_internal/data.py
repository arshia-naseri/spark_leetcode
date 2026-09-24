import datetime

USERS_SCHEMA = "account INT, name STRING"
TRANSACTIONS_SCHEMA = "trans_id INT, account INT, amount INT, transacted_on DATE"
OUTPUT_SCHEMA = "name STRING, balance BIGINT"

d = datetime.date

EXAMPLE_USERS = [
    (900001, "Alice"),
    (900002, "Bob"),
    (900003, "Charlie"),
]
EXAMPLE_TRANSACTIONS = [
    (1, 900001, 7000, d(2020, 8, 1)),
    (2, 900001, 7000, d(2020, 9, 1)),
    (3, 900001, -3000, d(2020, 9, 2)),
    (4, 900002, 1000, d(2020, 9, 12)),
    (5, 900003, 6000, d(2020, 8, 7)),
    (6, 900003, 6000, d(2020, 9, 7)),
    (7, 900003, -4000, d(2020, 9, 11)),
]
EXAMPLE_OUTPUT = [
    ("Alice", 11000),
]

# Each case: (users rows, transactions rows, expected output rows).
CASES = [
    (EXAMPLE_USERS, EXAMPLE_TRANSACTIONS, EXAMPLE_OUTPUT),
    # No transactions: all balances are 0.
    (EXAMPLE_USERS, [], []),
    # No users.
    ([], EXAMPLE_TRANSACTIONS, []),
    # Balance equal to 10000 is not higher than 10000. 10001 is higher.
    (
        [(1, "Ann"), (2, "Ben")],
        [
            (1, 1, 6000, d(2020, 1, 1)),
            (2, 1, 4000, d(2020, 1, 2)),
            (3, 2, 10001, d(2020, 1, 3)),
        ],
        [("Ben", 10001)],
    ),
    # Many users over the limit. Negative amounts go down below the limit.
    (
        [(1, "Ann"), (2, "Ben"), (3, "Cid"), (4, "Dan")],
        [
            (1, 1, 20000, d(2020, 1, 1)),
            (2, 2, 15000, d(2020, 1, 2)),
            (3, 2, -2000, d(2020, 1, 3)),
            (4, 3, 12000, d(2020, 1, 4)),
            (5, 3, -5000, d(2020, 1, 5)),
        ],
        [("Ann", 20000), ("Ben", 13000)],
    ),
]
