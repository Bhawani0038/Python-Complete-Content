# 9. Product Availability Check

def is_available(stock, requested):
    return requested <= stock


print(is_available(10, 4))
