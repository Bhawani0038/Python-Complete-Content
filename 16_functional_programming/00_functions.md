# Python Functions

A function is a reusable block of code that performs a specific task. Instead of writing the same logic again and again, you define it once and call it whenever needed.

Functions are one of the most important ideas in Python because they help keep code organized, readable, and reusable.

## Why Use Functions?

Imagine you are building a small app that:

- signs in a user
- saves a report
- sends a confirmation email
- calculates a total bill

All of these tasks can be written as separate functions. Then your main program becomes easy to read.

```python
print("Welcome to the system")
print("Processing order...")
print("Order saved successfully")
```

This code works, but it becomes difficult to manage if the program grows. Functions make it easier.

## Defining a Function

Use the `def` keyword.

```python
def greet():
    print("Hello, welcome!")
```

This function does not take any input and does not return any value. It just prints a message.

### Calling a function

```python
def greet():
    print("Hello, welcome!")

# Call the function
greet()
```

Output:

```text
Hello, welcome!
```

## A Practical Example: Welcome Message for a User

```python
def welcome_user(name):
    print(f"Welcome, {name}!")

welcome_user("Aisha")
welcome_user("Bilal")
```

Output:

```text
Welcome, Aisha!
Welcome, Bilal!
```

This is a real use case because apps often greet different users by name.

## Function Parameters

Parameters are variables that receive values when a function is called.

```python
def show_message(name, city):
    print(f"{name} lives in {city}.")

show_message("Hassan", "Karachi")
```

Output:

```text
Hassan lives in Karachi.
```

This is a practical pattern in programs that work with user data.

## Return Values

A function can return data to the caller using `return`.

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 25)
print(result)
```

Output:

```text
35
```

Return values are useful when you want to use the result later in your program.

## Function Signature

A function signature is the definition of a function, including:

- function name
- parameters
- default values
- return type (optional in Python)

```python
def send_email(recipient, subject="Welcome", body="Hello!"):
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Message: {body}")
```

This function signature tells us:

- the function name is `send_email`
- it takes `recipient`, `subject`, and `body`
- `subject` and `body` have default values

A function signature is useful because it tells you what kind of information the function expects.

```python
send_email("student@example.com")
send_email("student@example.com", "Your report", "Your report is ready.")
```

## `*args` (Variable Number of Positional Arguments)

`*args` allows a function to accept any number of positional arguments.

```python
def display_items(*items):
    for item in items:
        print(item)


display_items("Tea", "Coffee", "Water")
display_items("Pen", "Notebook")
```

Output:

```text
Tea
Coffee
Water
Pen
Notebook
```

This is practical when you do not know in advance how many values will be passed.

### Real-world example: building a shopping cart summary

```python
def cart_summary(*products):
    print("Your cart contains:")
    for product in products:
        print("-", product)

cart_summary("Rice", "Milk", "Bread")
cart_summary("Phone", "Charger")
```

This is useful in apps where a user may buy different numbers of products.

## `**kwargs` (Variable Number of Keyword Arguments)

`**kwargs` allows a function to accept any number of keyword arguments.

```python
def customer_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

customer_profile(name="Ayesha", city="Lahore", age=24)
```

Output:

```text
name: Ayesha
city: Lahore
age: 24
```

This is very practical when you receive a dictionary-like set of data from a form or API.

### Real-world example: user registration data

```python
def register_user(**user_data):
    print("User registered successfully")
    for key, value in user_data.items():
        print(f"{key}: {value}")

register_user(name="Hina", email="hina@example.com", department="IT")
```

This is similar to collecting form input where the user may provide different fields.

## Combining `*args` and `**kwargs`

A function can accept both positional and keyword arguments together.

```python
def show_order(order_id, *items, **details):
    print("Order ID:", order_id)
    print("Items:")
    for item in items:
        print("-", item)
    print("Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

show_order(
    101,
    "Laptop",
    "Mouse",
    customer="Ali",
    city="Islamabad",
    payment="Cash"
)
```

This pattern is common in real application code where one function handles flexible input.

## Practical Example: Function Signature in a Real App

```python
def create_user(username, email, role="customer", active=True):
    return {
        "username": username,
        "email": email,
        "role": role,
        "active": active
    }

user1 = create_user("maria", "maria@example.com")
user2 = create_user("ahmed", "ahmed@example.com", role="admin", active=False)

print(user1)
print(user2)
```

Output:

```text
{'username': 'maria', 'email': 'maria@example.com', 'role': 'customer', 'active': True}
{'username': 'ahmed', 'email': 'ahmed@example.com', 'role': 'admin', 'active': False}
```

This is a realistic function signature because it clearly defines the expected input and optional values.

## Real-World Example: Building a Billing Function

```python
def total_bill(amount, tax_rate):
    tax_amount = amount * tax_rate
    total = amount + tax_amount
    return total

bill = total_bill(500, 0.10)
print(f"Total bill: {bill}")
```

Output:

```text
Total bill: 550.0
```

This is a practical example because shops and apps often calculate totals with tax.

## Real-World Example: Checking User Access

```python
def can_access(user_role):
    allowed_roles = ["admin", "manager", "editor"]
    if user_role in allowed_roles:
        return True
    return False

print(can_access("admin"))
print(can_access("guest"))
```

Output:

```text
True
False
```

This is the kind of logic used in apps and websites for permissions.

## Real-World Example: Saving a Student Record

```python
def save_student(name, age, grade):
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    return student

student1 = save_student("Sara", 18, "A")
print(student1)
```

Output:

```text
{'name': 'Sara', 'age': 18, 'grade': 'A'}
```

This is practical because apps often collect data and store it in a structured form.

## Default Parameters

You can give parameters default values.

```python
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()
greet_user("Maryam")
```

Output:

```text
Hello, Guest!
Hello, Maryam!
```

This is useful when your program has common values that usually do not change.

## Multiple Return Values

A function can return more than one value.

```python
def get_user_info():
    name = "Ali"
    age = 22
    city = "Lahore"
    return name, age, city

result = get_user_info()
print(result)
```

Output:

```text
('Ali', 22, 'Lahore')
```

This is especially useful when one function supplies multiple pieces of related data.

## Function with a Practical Task: Order Summary

```python
def order_summary(item_name, quantity, price):
    subtotal = quantity * price
    if subtotal > 1000:
        discount = subtotal * 0.10
    else:
        discount = 0
    total = subtotal - discount
    return item_name, quantity, subtotal, discount, total

item, qty, sub, discount, final_total = order_summary("Laptop", 2, 500)
print(f"Item: {item}")
print(f"Quantity: {qty}")
print(f"Subtotal: {sub}")
print(f"Discount: {discount}")
print(f"Final total: {final_total}")
```

Output:

```text
Item: Laptop
Quantity: 2
Subtotal: 1000
Discount: 100.0
Final total: 900.0
```

This is a realistic business example and demonstrates why functions are so useful.

## Function Scope

Variables created inside a function are local to that function.

```python
def add_tax(price):
    tax = price * 0.05
    return price + tax

print(add_tax(200))
# print(tax)  # This would cause an error because tax is local to the function
```

This helps reduce accidental changes to variables in other parts of the program.

## Best Practices for Functions

- Give functions clear names
- Keep each function focused on one task
- Use return values when needed
- Use default parameters when a value is commonly reused
- Use `*args` and `**kwargs` only when you truly need flexible inputs
- Avoid writing very long functions
- Reuse functions instead of repeating code

## Example: A Real App Workflow

```python
def register_user(name, email):
    return {
        "name": name,
        "email": email,
        "status": "registered"
    }


def send_welcome_email(email):
    return f"Welcome email sent to {email}"


def main():
    new_user = register_user("Nadia", "nadia@example.com")
    print(new_user)
    print(send_welcome_email(new_user["email"]))


main()
```

Output:

```text
{'name': 'Nadia', 'email': 'nadia@example.com', 'status': 'registered'}
Welcome email sent to nadia@example.com
```

This is a practical application of functions in a small software workflow.

## Summary

Functions help you:

- organize code
- reduce repetition
- make code easier to understand
- reuse logic in different parts of a program

A function is a small reusable unit that can take input, process it, and return a result.

