numbers = [2, 5, 2, 6, 5, 2]
count = {}
for num in numbers:
    count[num] = count.get(num, 0) + 1
print(count)
