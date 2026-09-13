"""Question: Check whether a number is positive or not positive."""

number = 8

# Solution 1: if/else
if number > 0:
    print("Number is positive")
else:
    print("Number is not positive")

# Solution 2: conditional expression
message = "Number is positive" if number > 0 else "Number is not positive"
print(message)