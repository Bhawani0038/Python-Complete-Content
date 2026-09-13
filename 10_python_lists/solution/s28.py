numbers = [3, 5, 3, 2, 5, 7, 2, 8]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)
