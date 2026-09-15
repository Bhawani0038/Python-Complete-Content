## Date and Time Module in Python

Python provides the built-in `datetime` module for working with dates and times.

It is useful for:

- showing the current date and time
- creating reminders and schedules
- calculating age or duration
- checking deadlines and expiry dates
- recording when an order was created
- formatting dates for users

Import the module like this:

```python
import datetime
```

## Getting the Current Date and Time

### `datetime.now()`

`datetime.now()` returns the current local date and time.

```python
from datetime import datetime

current_time = datetime.now()
print(current_time)
```

Example output:

```text
2026-09-15 14:30:45.123456
```

The exact output depends on the computer's clock.

### Getting Individual Parts

```python
from datetime import datetime

current_time = datetime.now()

print("Year:", current_time.year)
print("Month:", current_time.month)
print("Day:", current_time.day)
print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)
```

## Getting Today's Date

Use `date.today()` when you only need the date and not the current time.

```python
from datetime import date

today = date.today()
print(today)
```

Output:

```text
2026-09-15
```

## Creating a Specific Date

```python
from datetime import date

launch_date = date(2026, 12, 25)
print(launch_date)
print(launch_date.year)
```

The order is always:

```python
date(year, month, day)
```

## Creating a Specific Date and Time

```python
from datetime import datetime

meeting = datetime(2026, 10, 5, 15, 30)
print(meeting)
```

The order is:

```python
datetime(year, month, day, hour, minute, second)
```

## Formatting Dates with `strftime()`

The default date format is useful for programs, but users often need a more readable format. Use `strftime()` to convert a date or time into a formatted string.

```python
from datetime import datetime

current_time = datetime.now()

print(current_time.strftime("%d-%m-%Y"))
print(current_time.strftime("%B %d, %Y"))
print(current_time.strftime("%I:%M %p"))
```

Example output:

```text
15-09-2026
September 15, 2026
02:30 PM
```

### Common Formatting Codes

| Code | Meaning | Example |
|---|---|---|
| `%Y` | four-digit year | `2026` |
| `%y` | two-digit year | `26` |
| `%m` | month number | `09` |
| `%B` | full month name | `September` |
| `%b` | short month name | `Sep` |
| `%d` | day of month | `15` |
| `%A` | full weekday name | `Tuesday` |
| `%a` | short weekday name | `Tue` |
| `%H` | hour in 24-hour format | `14` |
| `%I` | hour in 12-hour format | `02` |
| `%M` | minute | `30` |
| `%S` | second | `45` |
| `%p` | AM or PM | `PM` |

## Converting Text into a Date with `strptime()`

`strptime()` converts a string into a `datetime` object. The format must match the string.

```python
from datetime import datetime

date_text = "15-09-2026"
converted_date = datetime.strptime(date_text, "%d-%m-%Y")

print(converted_date)
print(converted_date.year)
```

This is useful when a user enters a date in a form or when a date is read from a file.

## Date Arithmetic with `timedelta`

Use `timedelta` to add or subtract days, hours, and minutes.

```python
from datetime import date, timedelta

today = date.today()
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
previous_day = today - timedelta(days=1)

print("Today:", today)
print("Tomorrow:", tomorrow)
print("Next week:", next_week)
print("Previous day:", previous_day)
```

## Finding the Difference Between Dates

Subtracting two dates returns a `timedelta` object.

```python
from datetime import date

start_date = date(2026, 9, 1)
end_date = date(2026, 9, 15)

difference = end_date - start_date
print("Days passed:", difference.days)
```

Output:

```text
Days passed: 14
```

## Practical Example 1: Calculate Age

```python
from datetime import date

birth_year = int(input("Enter your birth year: "))
current_year = date.today().year

age = current_year - birth_year
print("Your approximate age is:", age)
```

For an exact age, compare the person's birthday with today's month and day as well.

## Practical Example 2: Calculate an Order Delivery Date

```python
from datetime import date, timedelta

order_date = date.today()
delivery_date = order_date + timedelta(days=5)

print("Order date:", order_date.strftime("%d %B %Y"))
print("Expected delivery:", delivery_date.strftime("%d %B %Y"))
```

This is useful in shopping and delivery applications.

## Practical Example 3: Check Whether a Subscription Has Expired

```python
from datetime import date

expiry_date = date(2026, 12, 31)
today = date.today()

if today > expiry_date:
	print("Subscription expired")
else:
	remaining_days = (expiry_date - today).days
	print(f"Subscription is active for {remaining_days} more days")
```

## Practical Example 4: Meeting Reminder

```python
from datetime import datetime

meeting_text = input("Enter meeting date and time (DD-MM-YYYY HH:MM): ")
meeting_time = datetime.strptime(meeting_text, "%d-%m-%Y %H:%M")
current_time = datetime.now()

if meeting_time > current_time:
	print("Your meeting is scheduled for", meeting_time.strftime("%d %B at %I:%M %p"))
else:
	print("This meeting time has already passed.")
```

## Practical Example 5: Create a Timestamp for an Order

```python
from datetime import datetime

order_id = "ORD-1001"
created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("Order:", order_id)
print("Created at:", created_at)
```

Timestamps help applications record when an event occurred.

## Working with `time`

The `time` class represents a time without a date.

```python
from datetime import time

office_opening = time(9, 0)
office_closing = time(17, 30)

print("Opening:", office_opening)
print("Closing:", office_closing)
```

## Comparing Dates and Times

Dates and times can be compared using operators such as `<`, `>`, and `==`.

```python
from datetime import date

today = date.today()
deadline = date(2026, 12, 31)

if today < deadline:
	print("The deadline has not arrived.")
elif today == deadline:
	print("The deadline is today.")
else:
	print("The deadline has passed.")
```

## Handling Invalid Date Input

`strptime()` raises `ValueError` when the input does not match the expected format.

```python
from datetime import datetime

date_text = input("Enter a date (DD-MM-YYYY): ")

try:
	selected_date = datetime.strptime(date_text, "%d-%m-%Y")
	print("Valid date:", selected_date.date())
except ValueError:
	print("Invalid date. Use the format DD-MM-YYYY.")
```

## Important Notes

- Months and days must be valid, such as month `1` through `12`.
- `strftime()` converts a date into text.
- `strptime()` converts text into a date.
- Use `timedelta` for date calculations.
- Use `date` when time is not needed.
- Use `datetime` when both date and time are needed.
- A naive `datetime` does not contain timezone information.

## Common Imports

```python
from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
```

You can also import several names together:

```python
from datetime import date, datetime, timedelta
```

## Summary

The `datetime` module makes it possible to work with real dates and times in Python.

The most important tools are:

- `date.today()` - get today's date
- `datetime.now()` - get the current date and time
- `strftime()` - format a date as text
- `strptime()` - parse text into a date
- `timedelta` - add or subtract time
- date subtraction - find the duration between dates
