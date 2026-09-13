"""Question: Determine the number of days in a month number."""

month_number = 4

# Solution 1: group months with the same number of days
if month_number == 2:
    days = 28
elif month_number in (4, 6, 9, 11):
    days = 30
elif month_number in (1, 3, 5, 7, 8, 10, 12):
    days = 31
else:
    days = None
print("Invalid month number" if days is None else f"{days} days")




# Solution 2: use a list of month lengths
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 1 <= month_number <= 12:
    print(f"{month_days[month_number - 1]} days")
else:
    print("Invalid month number")