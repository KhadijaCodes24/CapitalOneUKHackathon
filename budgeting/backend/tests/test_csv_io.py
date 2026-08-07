import csv
import os
import pytest

BACKEND_DIR = os.path.join(os.path.dirname(__file__), "..")


def read_csv(filename):
    path = os.path.join(BACKEND_DIR, filename)
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


class TestReadUsers:
    def test_two_users(self):
        users = read_csv("users.csv")
        assert len(users) == 2

    def test_usernames(self):
        users = read_csv("users.csv")
        usernames = [u["username"] for u in users]
        assert "alice" in usernames
        assert "bob" in usernames


class TestReadBudgets:
    def test_two_budgets(self):
        budgets = read_csv("budgets.csv")
        assert len(budgets) == 2

    def test_incomes(self):
        budgets = read_csv("budgets.csv")
        by_user = {b["user_id"]: float(b["monthly_income"]) for b in budgets}
        assert by_user["1"] == pytest.approx(2800.0)
        assert by_user["2"] == pytest.approx(3500.0)


class TestReadCategories:
    def test_fourteen_rows(self):
        categories = read_csv("categories.csv")
        assert len(categories) == 14

    def test_amounts_are_numeric(self):
        for cat in read_csv("categories.csv"):
            float(cat["expected_amount"])
            float(cat["actual_amount"])

    def test_alice_rent(self):
        categories = read_csv("categories.csv")
        rent = next(c for c in categories if c["budget_id"] == "1" and c["category"] == "rent")
        assert float(rent["expected_amount"]) == pytest.approx(900.0)
        assert float(rent["actual_amount"]) == pytest.approx(900.0)


class TestWriteAndReadBack:
    def test_budget_roundtrip(self, tmp_path):
        path = tmp_path / "budgets.csv"
        fieldnames = ["id", "user_id", "monthly_income", "carryover"]
        row = {"id": "99", "user_id": "3", "monthly_income": "4000.00", "carryover": "50.00"}
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(row)
        with open(path, newline="") as f:
            rows = list(csv.DictReader(f))
        assert len(rows) == 1
        assert rows[0]["user_id"] == "3"
        assert float(rows[0]["monthly_income"]) == pytest.approx(4000.0)

    def test_category_roundtrip(self, tmp_path):
        path = tmp_path / "categories.csv"
        fieldnames = ["id", "budget_id", "category", "expected_amount", "actual_amount"]
        row = {"id": "50", "budget_id": "99", "category": "gym",
               "expected_amount": "60.00", "actual_amount": "55.00"}
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(row)
        with open(path, newline="") as f:
            rows = list(csv.DictReader(f))
        assert rows[0]["category"] == "gym"
        assert float(rows[0]["actual_amount"]) == pytest.approx(55.0)
