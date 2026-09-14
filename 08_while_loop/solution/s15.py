number = int(input("Enter a positive integer: "))
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print(reversed_number)
