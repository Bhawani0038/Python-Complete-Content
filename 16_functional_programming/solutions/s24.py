# 24. Monthly Budget Checker

def budget_status(income, expenses):
    if income > expenses:
        return "safe"
    elif income == expenses:
        return "break-even"
    else:
        return "over-budget"


print(budget_status(5000, 4500))
