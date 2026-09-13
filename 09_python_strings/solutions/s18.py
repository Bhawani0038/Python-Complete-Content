product = input("Product: ")
quantity = int(input("Quantity: "))
price = float(input("Price per item: "))
total = quantity * price

print(f"Product: {product}")
print(f"Quantity: {quantity}")
print(f"Price per item: ${price:.2f}")
print(f"Total: ${total:.2f}")
