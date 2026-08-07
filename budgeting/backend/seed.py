import sqlite3, os

DB_PATH     = os.path.join(os.path.dirname(__file__), "data.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")


def seed():
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH) as f:
        conn.executescript(f.read())

    conn.executemany(
        "INSERT OR IGNORE INTO users (id, username, password, name, email) VALUES (?, ?, ?, ?, ?)",
        [
            (1, "alice", "password123", "Alice Johnson", "alice@example.com"),
            (2, "bob",   "password123", "Bob Smith",     "bob@example.com"),
        ]
    )

    conn.executemany(
        "INSERT OR IGNORE INTO budgets (id, user_id, month, year, monthly_income, carryover, date_created, date_edited) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (1, 1, 7, 2026, 2800.00, 150.00, "2026-07-01", "2026-07-01"),
            (2, 2, 7, 2026, 3500.00,   0.00, "2026-07-01", "2026-07-01"),
        ]
    )

    conn.executemany(
        "INSERT OR IGNORE INTO categories (id, budget_id, category, expected_amount, actual_amount) "
        "VALUES (?, ?, ?, ?, ?)",
        [
            (1,  1, "rent",        900.00,  900.00),
            (2,  1, "food",        300.00,  320.00),
            (3,  1, "bills",       150.00,  145.00),
            (4,  1, "hobbies",     100.00,   80.00),
            (5,  1, "socialising", 150.00,  200.00),
            (6,  1, "savings",     200.00,  200.00),
            (7,  1, "transport",   100.00,   95.00),
            (8,  2, "rent",       1200.00, 1200.00),
            (9,  2, "food",        400.00,  380.00),
            (10, 2, "bills",       200.00,  210.00),
            (11, 2, "hobbies",     150.00,  170.00),
            (12, 2, "socialising", 200.00,  190.00),
            (13, 2, "savings",     300.00,  300.00),
            (14, 2, "transport",   120.00,  115.00),
        ]
    )

    conn.commit()
    conn.close()
    print("Database seeded. Demo: alice / password123  |  bob / password123")


if __name__ == "__main__":
    seed()
