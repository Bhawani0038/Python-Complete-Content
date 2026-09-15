# Functions Practice Questions

Practice these questions to build confidence using Python functions in real-world situations.

## Beginner Level

### 1. Greeting Function
Write a function called `greet_user` that takes a name and prints a welcome message.

Example:

```python
greet_user("Ayesha")
```

Expected output:

```text
Welcome, Ayesha!
```

---

### 2. Student Record Function
Write a function called `student_info` that takes a student's name and age and returns a formatted string.

Example:

```python
print(student_info("Ali", 18))
```

Expected output:

```text
Ali is 18 years old.
```

---

### 3. Calculate Total Price
Write a function `calculate_total(price, quantity)` that returns the total cost.

Example:

```python
print(calculate_total(120, 3))
```

Expected output:

```text
360
```

---

### 4. Discount Calculator
Write a function `discounted_price(price, discount_percent)` that returns the price after applying a discount.

Example:

```python
print(discounted_price(500, 10))
```

Expected output:

```text
450.0
```

---

### 5. Login Check
Write a function `can_login(username, password)` that checks whether the username and password match stored values.

Example:

```python
print(can_login("admin", "1234"))
```

Expected output:

```text
True
```

---

### 6. Email Formatter
Write a function `format_email(name, domain)` that returns an email address in the format `name@domain.com`.

Example:

```python
print(format_email("sara", "gmail"))
```

Expected output:

```text
sara@gmail.com
```

---

## Intermediate Level

### 7. Order Summary Function
Write a function `order_summary(item_name, quantity, price)` that calculates:

- subtotal
- discount if subtotal is above 1000
- final total

Return all values in a dictionary or tuple.

Example:

```python
print(order_summary("Laptop", 2, 500))
```

Hint: if subtotal is more than 1000, apply a 10% discount.

---

### 8. User Registration
Write a function `register_user(name, email, role="customer")` that returns a dictionary containing user details.

Example:

```python
user = register_user("Mina", "mina@example.com")
print(user)
```

Expected structure:

```python
{
    "name": "Mina",
    "email": "mina@example.com",
    "role": "customer"
}
```

---

### 9. Product Availability Check
Write a function `is_available(stock, requested)` that returns `True` if the requested quantity is available, otherwise `False`.

Example:

```python
print(is_available(10, 4))
```

Expected output:

```text
True
```

---

### 10. Sales Report Function
Write a function `sales_report(sales_list)` that calculates:

- total sales
- number of sales entries
- average sale

Example:

```python
print(sales_report([200, 500, 350]))
```

---

### 11. Friend List Filter
Write a function `filter_friends(names, letter)` that returns only those names that start with the given letter.

Example:

```python
print(filter_friends(["Ali", "Ayesha", "Bilal", "Anas"], "A"))
```

Expected output:

```text
['Ali', 'Ayesha', 'Anas']
```

---

### 12. Build a Profile
Write a function `create_profile(name, age, city, hobby="reading")` that returns a dictionary with the provided information.

Example:

```python
print(create_profile("Nadia", 21, "Karachi"))
```

---

## Practical Real-World Problems

### 13. Billing with Tax
Write a function `final_bill(amount, tax_rate=0.05)` that calculates the final bill including tax.

Example:

```python
print(final_bill(1000))
```

Expected output:

```text
1050.0
```

---

### 14. Attendance Summary
Write a function `attendance_summary(present, total_students)` that returns the attendance percentage.

Example:

```python
print(attendance_summary(42, 50))
```

Expected output:

```text
84.0
```

---

### 15. Simple Calculator
Write a function `calculator(a, b, operation)` that performs addition, subtraction, multiplication, or division based on the `operation` string.

Example:

```python
print(calculator(10, 5, "add"))
print(calculator(10, 5, "divide"))
```

Expected output:

```text
15
2.0
```

---

### 16. User Access Control
Write a function `has_access(user_role)` that returns `True` if the role is one of `['admin', 'manager', 'editor']`, otherwise `False`.

Example:

```python
print(has_access("admin"))
print(has_access("guest"))
```

Expected output:

```text
True
False
```

---

## Advanced Function Practice

### 17. Flexible Product List
Write a function `show_products(*products)` that prints each product from the list passed to it.

Example:

```python
show_products("Laptop", "Mouse", "Keyboard")
```

---

### 18. Flexible User Details
Write a function `display_user_details(**details)` that prints all key-value pairs passed to it.

Example:

```python
display_user_details(name="Ali", city="Lahore", age=20)
```

---

### 19. Mix Both Patterns
Write a function `show_order(order_id, *items, **details)` that prints:

- order ID
- all items
- all additional details

Example:

```python
show_order(101, "Book", "Pen", customer="Sara", city="Karachi")
```

---

### 20. Real App Function Challenge
Write a function `create_customer_record(name, email, **extra_info)` that returns a dictionary containing:

- name
- email
- any extra information passed as keyword arguments

Example:

```python
print(create_customer_record("Hassan", "hassan@example.com", city="Lahore", phone="0300-1234567"))
```

---

## Mini Project Style Questions

### 21. Grocery Store Basket
Write a function `basket_total(*prices)` that adds all item prices and returns the total.

Example:

```python
print(basket_total(50, 30, 20, 15))
```

Expected output:

```text
115
```

---

### 22. Save Student Record
Write a function `save_student(name, age, grade)` that returns a dictionary like:

```python
{"name": "Sara", "age": 18, "grade": "A"}
```

---

### 23. Password Validator
Write a function `is_valid_password(password)` that checks:

- length is at least 8
- contains at least one digit
- contains at least one letter

Return `True` or `False`.

Example:

```python
print(is_valid_password("hello123"))
```

---

### 24. Monthly Budget Checker
Write a function `budget_status(income, expenses)` that returns:

- `"safe"` if income > expenses
- `"break-even"` if equal
- `"over-budget"` if expenses are greater

Example:

```python
print(budget_status(5000, 4500))
```

Expected output:

```text
safe
```

---

## Bonus Challenge Questions

### 25. Library Book Issue System
Write a function `issue_book(book_name, days_issued, fine_rate=5)` that calculates the fine if the book is returned late.

Example:

```python
print(issue_book("Python Basics", 10))
```

---

### 26. Fitness Goal Tracker
Write a function `goal_status(target, completed)` that returns a percentage of completion.

Example:

```python
print(goal_status(100, 75))
```

Expected output:

```text
75.0
```

---

### 27. Employee Salary Function
Write a function `net_salary(gross_salary, tax_percent=10)` that calculates salary after tax.

Example:

```python
print(net_salary(50000))
```

---

### 28. Event Registration Function
Write a function `register_event(name, event_type, **details)` that returns a dictionary containing the event information.

Example:

```python
print(register_event("Seminar", "Workshop", venue="Hall A", seats=40))
```

---

## Suggested Practice Order

If you want to practice step by step, do them in this order:

1. Greeting, total price, discount, login
2. Student record, email format, order summary
3. Sales report, attendance summary, budget checker
4. `*args`, `**kwargs`, mixed-pattern functions
5. Bonus challenge tasks

## Tips for Solving These Questions

- Start by writing the function signature.
- Decide what the function should return.
- Use simple prints first to test your logic.
- Then improve the function to make it cleaner and reusable.
- Check edge cases like empty values, zero, or invalid input.
