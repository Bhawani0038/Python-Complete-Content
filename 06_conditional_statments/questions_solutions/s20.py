"""Question: Determine a ticket price from the user's age."""

age = 62

# Solution 1: if/elif/else
if age < 5:
    ticket_price = "Free"
elif age <= 18:
    ticket_price = 100
elif age <= 60:
    ticket_price = 200
else:
    ticket_price = 150
print(f"Ticket price: {ticket_price}" if ticket_price == "Free" else f"Ticket price: Rs. {ticket_price}")




# Solution 2: use age boundaries in a conditional expression
ticket_price = "Free" if age < 5 else 100 if age <= 18 else 200 if age <= 60 else 150
print(f"Ticket price: {ticket_price}" if ticket_price == "Free" else f"Ticket price: Rs. {ticket_price}")