number = int(input("Enter a positive integer: "))

if number == 0:
    digit_count = 1
else:
    digit_count = 0
    while number > 0:
        digit_count += 1
        number //= 10

print(digit_count)
