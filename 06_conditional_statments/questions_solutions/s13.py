"""Question: Calculate shipping cost from weight and destination."""

weight = 3
destination = "International"

# Solution 1: choose the price per kilogram
if destination == "Domestic":
    rate = 2
elif destination == "International":
    rate = 5
else:
    rate = 0
cost = weight * rate
print("Shipping cost:", cost if rate else "Invalid destination")





# Solution 2: dictionary lookup
rates = {"Domestic": 2, "International": 5}
rate = rates.get(destination)
print("Shipping cost:", weight * rate if rate is not None else "Invalid destination")