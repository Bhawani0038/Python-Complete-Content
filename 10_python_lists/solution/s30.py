list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common_items = []

for item in list_a:
    if item in list_b and item not in common_items:
        common_items.append(item)

print(common_items)
