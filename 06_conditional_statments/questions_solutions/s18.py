"""Question: Classify a temperature as Cold, Moderate, or Hot."""

temperature = 22

# Solution 1: if/elif/else
if temperature < 10:
    classification = "Cold"
elif temperature <= 25:
    classification = "Moderate"
else:
    classification = "Hot"
print(classification)



# Solution 2: conditional expression
classification = "Cold" if temperature < 10 else "Moderate" if temperature <= 25 else "Hot"
print(classification)