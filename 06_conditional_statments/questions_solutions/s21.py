"""Question: Apply a discount for a loyalty card or a purchase over 200 rupees."""

has_loyalty_card = True
purchase_amount = 150

# Solution 1: combine conditions with or
if has_loyalty_card or purchase_amount > 200:
    print("Discount is applied")
else:
    print("Discount is not applied")



# Solution 2: store the result and use a conditional expression
discount_applied = has_loyalty_card or purchase_amount > 200
message = "Discount is applied" if discount_applied else "Discount is not applied"
print(message)