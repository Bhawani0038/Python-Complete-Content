"""Question: Recommend a mobile phone plan from monthly minutes."""

minutes = 350

# Solution 1: if/elif/else
if minutes < 200:
    plan = "Basic"
elif minutes <= 500:
    plan = "Standard"
else:
    plan = "Premium"
print(f"Recommended plan: {plan}")




# Solution 2: use a conditional expression
plan = "Basic" if minutes < 200 else "Standard" if minutes <= 500 else "Premium"
print(f"Recommended plan: {plan}")