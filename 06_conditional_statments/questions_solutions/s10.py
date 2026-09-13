"""Question: Determine the discount rate from a membership level."""

membership_level = "Gold"

# Solution 1: if/elif/else
if membership_level == "Gold":
    discount_rate = 0.20
elif membership_level == "Silver":
    discount_rate = 0.15
elif membership_level == "Bronze":
    discount_rate = 0.10
else:
    discount_rate = 0
print(f"Discount: {discount_rate:.0%}")




# Solution 2: dictionary lookup
discounts = {"Gold": 0.20, "Silver": 0.15, "Bronze": 0.10}
discount_rate = discounts.get(membership_level, 0)
print(f"Discount: {discount_rate:.0%}")