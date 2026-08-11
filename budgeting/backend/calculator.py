import math


def calculate_budget_summary(income: float, carryover: float, categories: list) -> dict:
# TODO: Calculate total_expected, total_actual, remaining_expected, remaining_actual
# and a per-category breakdown. Return as a dict.
    pass


def validate_budget(monthly_income: float, carryover: float, categories: list) -> dict:
    if income is None or carryover is None:
        return {"valid": False, "message": "Income and carryover are required."}

    try:
       income = float(income)
       carryover = float(carryover)
    except (TypeError, ValueError):
       return {"valid": False, "message": "Income and carryover must be numbers."}

    if income < 0 or carryover < 0:
        return {"valid": False, "message": "Income and carryover cannot be negative."}

    if not categories:
        return {"valid": False, "message": "Add at least one budget category."}

    total_outgoings = 0.0
    for cat in categories:
        name = cat.get("name") or "Unnamed category"
        try:
            amount = float(cat.get("amount", 0))
        except (TypeError, ValueError):
            return {"valid": False, "message": f"'{name}' has an invalid amount."}
        if amount < 0:
            return {"valid": False, "message": f"'{name}' cannot be negative."}
        total_outgoings += amount

    available = income + carryover
    if total_outgoings > available:
        over = total_outgoings - available
    return {
        "valid": False,
        "message": f"Outgoings (£{total_outgoings:.2f}) exceed available funds (£{available:.2f}) by £{over:.2f}.",
        }

    return {"valid": True}

def generate_suggestions(income: float, categories: list) -> list:
# TODO: Return a list of suggestion strings based on the spending figures
# e.g. flag categories where spending is high, or savings are low
    pass