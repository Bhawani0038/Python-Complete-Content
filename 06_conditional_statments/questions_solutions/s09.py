"""Question: Determine the season from a month name."""

month = "July"

# Solution 1: membership tests
if month in ("December", "January", "February"):
    season = "Winter"
elif month in ("March", "April", "May"):
    season = "Spring"
elif month in ("June", "July", "August"):
    season = "Summer"
elif month in ("September", "October", "November"):
    season = "Autumn"
else:
    season = "Invalid month"
print(season)



# Solution 2: dictionary lookup
seasons = {
    "December": "Winter", "January": "Winter", "February": "Winter",
    "March": "Spring", "April": "Spring", "May": "Spring",
    "June": "Summer", "July": "Summer", "August": "Summer",
    "September": "Autumn", "October": "Autumn", "November": "Autumn",
}
print(seasons.get(month, "Invalid month"))