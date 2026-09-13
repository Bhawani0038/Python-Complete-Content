"""Question: Determine a movie ticket cost from the person's age."""

age = 16

# Solution 1: if/elif/else
if age <= 12:
    price = 5
elif age <= 17:
    price = 7
else:
    price = 10
print(f"Ticket cost: ${price}")



# Solution 2: choose from age boundaries
price = 5 if age <= 12 else 7 if age <= 17 else 10
print(f"Ticket cost: ${price}")