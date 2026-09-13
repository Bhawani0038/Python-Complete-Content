"""Question: Check whether a number is even or odd."""

number = 7

# Solution 1: if/else
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Solution 2: use the remainder in a conditional expression
result = "Number is even" if number % 2 == 0 else "Number is odd"
print(result)