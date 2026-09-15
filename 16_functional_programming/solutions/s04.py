# 4. Discount Calculator

def discounted_price(price, discount_percent):
    discount = price * (discount_percent / 100)
    return price - discount


print(discounted_price(500, 10))
