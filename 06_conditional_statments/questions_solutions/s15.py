"""Question: Suggest clothing from the current temperature in Celsius."""

temperature = 15

# Solution 1: if/elif/else
if temperature < 10:
    suggestion = "Winter jacket, hat, and gloves"
elif temperature <= 20:
    suggestion = "Sweater or light jacket"
else:
    suggestion = "T-shirt and shorts"
print(suggestion)



# Solution 2: conditional expression
suggestion = (
    "Winter jacket, hat, and gloves"
    if temperature < 10
    else "Sweater or light jacket" if temperature <= 20
    else "T-shirt and shorts"
)
print(suggestion)