from shop.products import product_list
from shop.billing import total_price

products = product_list()
print(products)
print(total_price([1500, 50, 200]))
