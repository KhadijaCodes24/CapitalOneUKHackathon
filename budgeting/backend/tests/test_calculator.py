import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from calculator import calculate_budget_summary, validate_budget, generate_suggestions

CATEGORIES = [
    {"category": "rent",       "expected_amount": 900,  "actual_amount": 900},
    {"category": "food",       "expected_amount": 300,  "actual_amount": 320},
    {"category": "bills",      "expected_amount": 150,  "actual_amount": 145},
    {"category": "savings",    "expected_amount": 200,  "actual_amount": 200},
    {"category": "socialising","expected_amount": 150,  "actual_amount": 200},
]


class TestCalculateBudgetSummary:
    def test_totals_correct(self):
        result = calculate_budget_summary(2800, 150, CATEGORIES)
        # TODO: assert total_expected and total_actual are correct

    def test_remaining_expected(self):
        result = calculate_budget_summary(2800, 150, CATEGORIES)
        # TODO: assert remaining_expected is income + carryover - total_expected

    def test_remaining_actual(self):
        result = calculate_budget_summary(2800, 150, CATEGORIES)
        # TODO: assert remaining_actual is income + carryover - total_actual

    def test_by_category_keys(self):
        result = calculate_budget_summary(2800, 150, CATEGORIES)
        # TODO: assert "rent" and "food" are keys in by_category

    def test_empty_categories(self):
        result = calculate_budget_summary(2800, 0, [])
        # TODO: assert totals are 0 and remaining equals income


class TestValidateBudget:
    def test_valid_budget(self):
        result = validate_budget(2800, 150, CATEGORIES)
        # TODO: assert valid is True

    def test_over_budget(self):
        big = [{"category": "rent", "expected_amount": 3000, "actual_amount": 0}]
        result = validate_budget(2800, 0, big)
        # TODO: assert valid is False and message is present

    def test_zero_income(self):
        result = validate_budget(0, 0, CATEGORIES)
        # TODO: assert valid is False

    def test_carryover_helps(self):
        cats = [{"category": "rent", "expected_amount": 2900, "actual_amount": 0}]
        result = validate_budget(2800, 200, cats)
        # TODO: assert valid is True (carryover covers the difference)


class TestGenerateSuggestions:
    def test_returns_list(self):
        result = generate_suggestions(2800, CATEGORIES)
        # TODO: assert result is a list

    def test_no_savings_flagged(self):
        no_savings = [{"category": "savings", "actual_amount": 0, "expected_amount": 0}]
        result = generate_suggestions(2800, no_savings)
        # TODO: assert a suggestion mentions savings

    def test_no_issues_message(self):
        good = [
            {"category": "food",    "actual_amount": 100, "expected_amount": 100},
            {"category": "savings", "actual_amount": 500, "expected_amount": 500},
        ]
        result = generate_suggestions(2000, good)
        # TODO: assert a suggestion contains "Great" when there are no issues
