"""Question: Calculate BMI and display its category."""

weight = 70
height = 1.75
bmi = weight / (height * height)

# Solution 1: if/elif/else
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print(f"BMI: {bmi:.1f} ({category})")




