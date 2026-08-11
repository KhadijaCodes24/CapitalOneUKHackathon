import sqlite3
import os
import pytest

BACKEND_DIR  = os.path.join(os.path.dirname(__file__), "..")
SCHEMA_PATH  = os.path.join(BACKEND_DIR, "schema.sql")


# ── Self-contained database helpers ────────────────────────────────────────────
# These mirror the SQLite functions you can implement in app.py — they exist
# here only to demonstrate how to write and test database code.

def get_db(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def find_user(conn, username, password):
    return conn.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password),
    ).fetchone()


def find_user_by_id(conn, user_id):
    return conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()


def get_budgets_for_user(conn, user_id):
    return conn.execute("SELECT * FROM budgets WHERE user_id = ?", (user_id,)).fetchall()


def get_budget_by_id(conn, budget_id):
    return conn.execute("SELECT * FROM budgets WHERE id = ?", (budget_id,)).fetchone()


def get_categories_for_budget(conn, budget_id):
    return conn.execute(
        "SELECT * FROM categories WHERE budget_id = ?", (budget_id,)
    ).fetchall()


def save_budget(conn, user_id, monthly_income, carryover, categories):
    cur = conn.execute(
        "INSERT INTO budgets (user_id, month, year, monthly_income, carryover, date_created, date_edited) "
        "VALUES (?, 1, 2026, ?, ?, '2026-01-01', '2026-01-01')",
        (user_id, monthly_income, carryover),
    )
    budget_id = cur.lastrowid
    for c in categories:
        conn.execute(
            "INSERT INTO categories (budget_id, category, expected_amount, actual_amount) "
            "VALUES (?, ?, ?, ?)",
            (budget_id, c["category"], c["expected_amount"], c["actual_amount"]),
        )
    conn.commit()
    return budget_id


def delete_budget(conn, budget_id):
    conn.execute("DELETE FROM categories WHERE budget_id = ?", (budget_id,))
    conn.execute("DELETE FROM budgets WHERE id = ?", (budget_id,))
    conn.commit()


def register_user(conn, username, password, name, email):
    existing = conn.execute(
        "SELECT 1 FROM users WHERE username = ?", (username,)
    ).fetchone()
    if existing:
        return False
    conn.execute(
        "INSERT INTO users (username, password, name, email) VALUES (?, ?, ?, ?)",
        (username, password, name, email),
    )
    conn.commit()
    return True


# ── Fixture ─────────────────────────────────────────────────────────────────────
# Each test gets a fresh temporary, seeded database — never the real app data.

@pytest.fixture
def db(tmp_path):
    db_path = str(tmp_path / "test.db")
    conn = get_db(db_path)
    with open(SCHEMA_PATH) as f:
        conn.executescript(f.read())

    conn.execute("INSERT INTO users (id, username, password, name, email) VALUES (1,'alice','pass123','Alice','alice@test.com')")
    conn.execute("INSERT INTO users (id, username, password, name, email) VALUES (2,'bob','pass123','Bob','bob@test.com')")
    conn.execute("INSERT INTO budgets (id, user_id, month, year, monthly_income, carryover, date_created, date_edited) VALUES (1,1,7,2026,2800,150,'2026-07-01','2026-07-01')")
    conn.execute("INSERT INTO budgets (id, user_id, month, year, monthly_income, carryover, date_created, date_edited) VALUES (2,2,7,2026,3500,0,'2026-07-01','2026-07-01')")
    conn.execute("INSERT INTO categories (id, budget_id, category, expected_amount, actual_amount) VALUES (1,1,'rent',900,900)")
    conn.execute("INSERT INTO categories (id, budget_id, category, expected_amount, actual_amount) VALUES (2,1,'food',300,320)")
    conn.execute("INSERT INTO categories (id, budget_id, category, expected_amount, actual_amount) VALUES (3,2,'rent',1200,1200)")
    conn.commit()

    yield conn
    conn.close()


# ── find_user ─────────────────────────────────────────────────────────────────

class TestFindUser:
    def test_valid_credentials(self, db):
        result = find_user(db, "alice", "pass123")
        assert result is not None
        assert result["username"] == "alice"

    def test_wrong_password(self, db):
        result = find_user(db, "alice", "wrongpassword")
        assert result is None

    def test_unknown_user(self, db):
        result = find_user(db, "nobody", "pass123")
        assert result is None


# ── find_user_by_id ───────────────────────────────────────────────────────────

class TestFindUserById:
    def test_existing_user(self, db):
        result = find_user_by_id(db, 1)
        assert result["name"] == "Alice"

    def test_nonexistent_user(self, db):
        result = find_user_by_id(db, 999)
        assert result is None


# ── get_budgets_for_user ──────────────────────────────────────────────────────

class TestGetBudgetsForUser:
    def test_returns_only_user_budgets(self, db):
        result = get_budgets_for_user(db, 1)
        assert len(result) == 1
        assert result[0]["user_id"] == 1

    def test_no_budgets(self, db):
        result = get_budgets_for_user(db, 999)
        assert result == []


# ── get_budget_by_id ──────────────────────────────────────────────────────────

class TestGetBudgetById:
    def test_existing_budget(self, db):
        result = get_budget_by_id(db, 1)
        assert result is not None
        assert result["monthly_income"] == pytest.approx(2800.0)

    def test_nonexistent_budget(self, db):
        result = get_budget_by_id(db, 999)
        assert result is None


# ── get_categories_for_budget ─────────────────────────────────────────────────

class TestGetCategoriesForBudget:
    def test_returns_correct_categories(self, db):
        result = get_categories_for_budget(db, 1)
        assert len(result) == 2
        names = [r["category"] for r in result]
        assert "rent" in names
        assert "food" in names

    def test_no_categories(self, db):
        result = get_categories_for_budget(db, 999)
        assert result == []


# ── save_budget ───────────────────────────────────────────────────────────────

class TestSaveBudget:
    def test_saves_and_returns_id(self, db):
        cats = [{"category": "rent", "expected_amount": 800, "actual_amount": 800}]
        new_id = save_budget(db, 1, 3000, 100, cats)
        assert new_id is not None
        budget = get_budget_by_id(db, new_id)
        assert budget["monthly_income"] == pytest.approx(3000.0)

    def test_categories_saved(self, db):
        cats = [{"category": "food", "expected_amount": 200, "actual_amount": 180}]
        new_id = save_budget(db, 1, 3000, 0, cats)
        saved_cats = get_categories_for_budget(db, new_id)
        assert len(saved_cats) == 1
        assert saved_cats[0]["category"] == "food"


# ── delete_budget ─────────────────────────────────────────────────────────────

class TestDeleteBudget:
    def test_budget_removed(self, db):
        delete_budget(db, 1)
        assert get_budget_by_id(db, 1) is None

    def test_categories_also_removed(self, db):
        delete_budget(db, 1)
        assert get_categories_for_budget(db, 1) == []


# ── register_user ─────────────────────────────────────────────────────────────

class TestRegisterUser:
    def test_creates_new_user(self, db):
        result = register_user(db, "charlie", "pass", "Charlie", "c@test.com")
        assert result is True
        user = find_user(db, "charlie", "pass")
        assert user is not None

    def test_duplicate_username_rejected(self, db):
        result = register_user(db, "alice", "newpass", "Alice2", "a2@test.com")
        assert result is False
