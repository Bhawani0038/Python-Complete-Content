numbers = [12, 7, 5, 18, 20, 9, 14, 3]
even_count = sum(number % 2 == 0 for number in numbers)
odd_count = sum(number % 2 != 0 for number in numbers)

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
