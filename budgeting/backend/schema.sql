CREATE TABLE IF NOT EXISTS users (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name     TEXT NOT NULL,
    email    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS budgets (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id        INTEGER NOT NULL,
    month          INTEGER NOT NULL,
    year           INTEGER NOT NULL,
    monthly_income REAL NOT NULL,
    carryover      REAL NOT NULL DEFAULT 0,
    date_created   TEXT NOT NULL,
    date_edited    TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS categories (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    budget_id       INTEGER NOT NULL,
    category        TEXT NOT NULL,
    expected_amount REAL NOT NULL,
    actual_amount   REAL NOT NULL,
    FOREIGN KEY (budget_id) REFERENCES budgets(id)
);
