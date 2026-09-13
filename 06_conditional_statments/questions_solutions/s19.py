"""Question: Apply a purchase discount and print the final bill amount."""

purchase_amount = 4500

# Solution 1: if/elif/else
if purchase_amount > 5000:
    discount_rate = 0.20
elif purchase_amount >= 2000:
    discount_rate = 0.10
else:
    discount_rate = 0
final_bill = purchase_amount * (1 - discount_rate)
print(f"Final bill: {final_bill:.2f}")



# Solution 2: calculate the discount with a conditional expression
discount_rate = 0.20 if purchase_amount > 5000 else 0.10 if purchase_amount >= 2000 else 0
print(f"Final bill: {purchase_amount * (1 - discount_rate):.2f}")