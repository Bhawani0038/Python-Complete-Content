# 19. Mix Both Patterns

def show_order(order_id, *items, **details):
    print("Order ID:", order_id)
    print("Items:")
    for item in items:
        print("-", item)
    print("Details:")
    for key, value in details.items():
        print(f"{key}: {value}")


show_order(101, "Book", "Pen", customer="Sara", city="Karachi")
