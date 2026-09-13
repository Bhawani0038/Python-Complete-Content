"""Question: Calculate the discounted amount for an online purchase."""

order_amount = 80

# Solution 1: choose the discount rate
if order_amount > 100:
    discount_rate = 0.20
elif order_amount >= 50:
    discount_rate = 0.10
else:
    discount_rate = 0.05
discounted_amount = order_amount * (1 - discount_rate)
print(f"Discounted amount: ${discounted_amount:.2f}")



# Solution 2: calculate the discount separately
discount = (
    order_amount * 0.20 if order_amount > 100
    else order_amount * 0.10 if order_amount >= 50
    else order_amount * 0.05
)
print(f"Discounted amount: ${order_amount - discount:.2f}")