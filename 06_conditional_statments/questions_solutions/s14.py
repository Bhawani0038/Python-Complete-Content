"""Question: Check driver's-license eligibility by age and license type."""

age = 17
license_type = "Motorcycle"

# Solution 1: explicit conditions
if license_type == "Car":
    eligible = age >= 18
elif license_type == "Motorcycle":
    eligible = age >= 16
else:
    eligible = False
if eligible:
    print(f"Eligible to apply for a {license_type} license")
else:
    print(f"Not eligible to apply for a {license_type} license")


