"""Question: Check whether a number is divisible by both 2 and 3."""

number = 12

# Solution 1: combine conditions with and
if number % 2 == 0 and number % 3 == 0:
    print("Number is divisible by 2 and 3")
else:
    print("Number is not divisible by 2 and 3")


# Solution 2: divisibility by the product
message = (
    "Number is divisible by 2 and 3"
    if number % 6 == 0
    else "Number is not divisible by 2 and 3"
)
print(message)