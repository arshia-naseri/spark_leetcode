USERS_SCHEMA = "user_id INT, name STRING, mail STRING"
OUTPUT_SCHEMA = "user_id INT, name STRING, mail STRING"

EXAMPLE_USERS = [
    (1, "Winston", "winston@leetcode.com"),
    (2, "Jonathan", "jonathanisgreat"),
    (3, "Annabelle", "bella-@leetcode.com"),
    (4, "Sally", "sally.come@leetcode.com"),
    (5, "Marwan", "quarz#2020@leetcode.com"),
    (6, "David", "david69@gmail.com"),
    (7, "Shapiro", ".shapo@leetcode.com"),
]
EXAMPLE_OUTPUT = [
    (1, "Winston", "winston@leetcode.com"),
    (3, "Annabelle", "bella-@leetcode.com"),
    (4, "Sally", "sally.come@leetcode.com"),
]

# Each case: (users rows, expected output rows).
CASES = [
    (EXAMPLE_USERS, EXAMPLE_OUTPUT),
    # Empty table.
    ([], []),
    # No valid mail.
    (
        [
            (1, "Ann", "1ann@leetcode.com"),
            (2, "Bob", "_bob@leetcode.com"),
            (3, "Cid", "@leetcode.com"),
        ],
        [],
    ),
    # Domain must be exact and lowercase. The period must not match any character.
    (
        [
            (1, "Ann", "ann@LeetCode.com"),
            (2, "Bob", "bob@leetcode.com.fake"),
            (3, "Cid", "cid@leetcodeXcom"),
            (4, "Dan", "dan@leetcode.co"),
            (5, "Eve", "eve@@leetcode.com"),
            (6, "Fay", "fay@sub.leetcode.com"),
        ],
        [],
    ),
    # Prefix can start with an uppercase letter and have one letter only.
    # Prefix can contain letters, digits, "_", "." and "-". A space is not permitted.
    (
        [
            (1, "Ann", "Ann@leetcode.com"),
            (2, "Bob", "b@leetcode.com"),
            (3, "Cid", "c_i.d-9@leetcode.com"),
            (4, "Dan", "dan smith@leetcode.com"),
            (5, "Eve", "Z9__..--@leetcode.com"),
        ],
        [
            (1, "Ann", "Ann@leetcode.com"),
            (2, "Bob", "b@leetcode.com"),
            (3, "Cid", "c_i.d-9@leetcode.com"),
            (5, "Eve", "Z9__..--@leetcode.com"),
        ],
    ),
    # Null mail is not valid. Null name does not change the result.
    (
        [
            (1, "Ann", None),
            (2, None, "bob@leetcode.com"),
        ],
        [(2, None, "bob@leetcode.com")],
    ),
]
