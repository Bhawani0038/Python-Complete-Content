"""Question: Use age and monthly income to determine loan eligibility."""

age = 25
monthly_income = 28000

# Solution 1: nested conditions
if age < 21:
    print("Not eligible")
elif monthly_income < 30000:
    print("Eligible for a small loan")
else:
    print("Eligible for a regular loan")



# Solution 2: use a single ordered conditional expression
message = (
    "Not eligible" if age < 21
    else "Eligible for a small loan" if monthly_income < 30000
    else "Eligible for a regular loan"
)
print(message)