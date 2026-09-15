# 7. Order Summary Function

def order_summary(item_name, quantity, price):
    subtotal = quantity * price
    if subtotal > 1000:
        discount = subtotal * 0.10
    else:
        discount = 0
    final_total = subtotal - discount
    return {
        "item_name": item_name,
        "quantity": quantity,
        "subtotal": subtotal,
        "discount": discount,
        "final_total": final_total,
    }


print(order_summary("Laptop", 2, 500))
