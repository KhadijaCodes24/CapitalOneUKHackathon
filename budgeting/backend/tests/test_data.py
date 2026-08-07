import pytest
import sys, os, sqlite3

# Point imports at the backend folder
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# ── Test fixtures ─────────────────────────────────────────────────────────────
# Each test gets a fresh temporary database so tests don't interfere with each other.

@pytest.fixture
def tmp_db(monkeypatch, tmp_path):
    """Create a temporary seeded database and point the app at it."""
    import app as backend

    db_path = str(tmp_path / "test.db")
    monkeypatch.setattr(backend, "DB_PATH", db_path)

    schema = os.path.join(os.path.dirname(os.path.dirname(__file__)), "schema.sql")
    conn = sqlite3.connect(db_path)
    with open(schema) as f:
        conn.executescript(f.read())

    conn.execute("INSERT INTO users (id, username, password, name, email) VALUES (1,'alice','pass123','Alice','alice@test.com')")
    conn.execute("INSERT INTO users (id, username, password, name, email) VALUES (2,'bob','pass123','Bob','bob@test.com')")
    conn.execute("INSERT INTO budgets (id, user_id, month, year, monthly_income, carryover, date_created, date_edited) VALUES (1,1,7,2026,2800,150,'2026-07-01','2026-07-01')")
    conn.execute("INSERT INTO budgets (id, user_id, month, year, monthly_income, carryover, date_created, date_edited) VALUES (2,2,7,2026,3500,0,'2026-07-01','2026-07-01')")
    conn.execute("INSERT INTO categories (id, budget_id, category, expected_amount, actual_amount) VALUES (1,1,'rent',900,900)")
    conn.execute("INSERT INTO categories (id, budget_id, category, expected_amount, actual_amount) VALUES (2,1,'food',300,320)")
    conn.execute("INSERT INTO categories (id, budget_id, category, expected_amount, actual_amount) VALUES (3,2,'rent',1200,1200)")
    conn.commit()
    conn.close()

    return db_path


# ── find_user ─────────────────────────────────────────────────────────────────

class TestFindUser:
    def test_valid_credentials(self, tmp_db):
        import app as backend
        result = backend.find_user("alice", "pass123")
        assert result is not None
        assert result["username"] == "alice"

    def test_wrong_password(self, tmp_db):
        import app as backend
        result = backend.find_user("alice", "wrongpassword")
        assert result is None

    def test_unknown_user(self, tmp_db):
        import app as backend
        result = backend.find_user("nobody", "pass123")
        assert result is None


# ── find_user_by_id ───────────────────────────────────────────────────────────

class TestFindUserById:
    def test_existing_user(self, tmp_db):
        import app as backend
        result = backend.find_user_by_id(1)
        assert result["name"] == "Alice"

    def test_nonexistent_user(self, tmp_db):
        import app as backend
        result = backend.find_user_by_id(999)
        assert result is None


# ── get_budgets_for_user ──────────────────────────────────────────────────────

class TestGetBudgetsForUser:
    def test_returns_only_user_budgets(self, tmp_db):
        import app as backend
        result = backend.get_budgets_for_user(1)
        assert len(result) == 1
        assert str(result[0]["user_id"]) == "1"

    def test_no_budgets(self, tmp_db):
        import app as backend
        result = backend.get_budgets_for_user(999)
        assert result == []


# ── get_budget_by_id ──────────────────────────────────────────────────────────

class TestGetBudgetById:
    def test_existing_budget(self, tmp_db):
        import app as backend
        result = backend.get_budget_by_id(1)
        assert result is not None
        assert float(result["monthly_income"]) == 2800.0

    def test_nonexistent_budget(self, tmp_db):
        import app as backend
        result = backend.get_budget_by_id(999)
        assert result is None


# ── get_categories_for_budget ─────────────────────────────────────────────────

class TestGetCategoriesForBudget:
    def test_returns_correct_categories(self, tmp_db):
        import app as backend
        result = backend.get_categories_for_budget(1)
        assert len(result) == 2
        names = [r["category"] for r in result]
        assert "rent" in names
        assert "food" in names

    def test_no_categories(self, tmp_db):
        import app as backend
        result = backend.get_categories_for_budget(999)
        assert result == []


# ── save_budget ───────────────────────────────────────────────────────────────

class TestSaveBudget:
    def test_saves_and_returns_id(self, tmp_db):
        import app as backend
        cats = [{"category": "rent", "expected_amount": 800, "actual_amount": 800}]
        new_id = backend.save_budget(1, 3000, 100, cats)
        assert new_id is not None
        budget = backend.get_budget_by_id(new_id)
        assert float(budget["monthly_income"]) == 3000.0

    def test_categories_saved(self, tmp_db):
        import app as backend
        cats = [{"category": "food", "expected_amount": 200, "actual_amount": 180}]
        new_id = backend.save_budget(1, 3000, 0, cats)
        saved_cats = backend.get_categories_for_budget(new_id)
        assert len(saved_cats) == 1
        assert saved_cats[0]["category"] == "food"


# ── delete_budget ─────────────────────────────────────────────────────────────

class TestDeleteBudget:
    def test_budget_removed(self, tmp_db):
        import app as backend
        backend.delete_budget(1)
        assert backend.get_budget_by_id(1) is None

    def test_categories_also_removed(self, tmp_db):
        import app as backend
        backend.delete_budget(1)
        assert backend.get_categories_for_budget(1) == []


# ── register_user ─────────────────────────────────────────────────────────────

class TestRegisterUser:
    def test_creates_new_user(self, tmp_db):
        import app as backend
        result = backend.register_user("charlie", "pass", "Charlie", "c@test.com")
        assert result is True
        user = backend.find_user("charlie", "pass")
        assert user is not None

    def test_duplicate_username_rejected(self, tmp_db):
        import app as backend
        result = backend.register_user("alice", "newpass", "Alice2", "a2@test.com")
        assert result is False
