# Python Exception Handling

In real programs, errors can happen while the code is running. These errors are called exceptions.

Examples include:

- dividing a number by zero
- trying to open a missing file
- converting a text value into an integer
- using an index that is out of range

Instead of crashing the whole program, Python allows us to handle these errors using `try`, `except`, `else`, and `finally`.

## Why Exception Handling Is Important

Imagine a program asks a user for a number, but the user types text instead. Without exception handling, the program may stop working completely.

```python
number = int(input("Enter a number: "))
print("You entered:", number)
```

If the user enters `abc`, Python raises a `ValueError`.

With exception handling, we can show a friendly message instead of crashing:

```python
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Please enter a valid integer.")
```

## Basic Syntax

```python
try:
    # Code that may raise an error
except SomeError:
    # Code to handle the error
```

The code inside `try` is checked first. If an exception happens, Python jumps to the matching `except` block.

## Example: Division by Zero

```python
try:
    a = 10
    b = 0
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output:

```text
Cannot divide by zero.
```

## Example: Reading a Missing File

```python
try:
    with open("missing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file was not found.")
```

Output:

```text
The file was not found.
```

## Catching Multiple Exceptions

You can handle different errors separately.

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

### Example input/output

```text
Enter a number: abc
Please enter a valid number.
```

```text
Enter a number: 0
You cannot divide by zero.
```

## Using `else`

The `else` block runs only if no exception occurs in the `try` block.

```python
try:
    value = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", value)
```

Example:

```text
Enter an integer: 25
You entered: 25
```

## Using `finally`

The `finally` block always runs, whether an error happens or not. It is often used to close files or clean up resources.

```python
try:
    value = int(input("Enter a number: "))
    print(10 / value)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Program finished.")
```

Output:

```text
Enter a number: 0
Cannot divide by zero.
Program finished.
```

## Practical Example: Safe Calculator

```python
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
        print("Result:", result)
        break
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("Second number cannot be zero.")
```

This is a practical example because it keeps the program running until the user enters valid input.

## Practical Example: File Reading Safely

```python
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist. Please check the filename.")
```

This is useful in real programs where the file may not always exist.

## Catching All Exceptions

You can also catch a general exception, though it is not always recommended because it hides details.

```python
try:
    number = int("abc")
except Exception as e:
    print("Something went wrong:", e)
```

Output:

```text
Something went wrong: invalid literal for int() with base 10: 'abc'
```

It is better to catch specific exceptions when possible.

## Common Built-in Exceptions

Here are some common exceptions in Python:

- `ValueError` - wrong value type or format
- `TypeError` - wrong type used in an operation
- `ZeroDivisionError` - division by zero
- `IndexError` - index is out of range
- `KeyError` - missing dictionary key
- `FileNotFoundError` - file does not exist
- `SyntaxError` - invalid Python syntax

## Example: Handling Different Errors

```python
data = [10, 20, 30]

try:
    print(data[5])
except IndexError:
    print("Index is out of range.")
```

Output:

```text
Index is out of range.
```

## Real-Life Use Case: User Input Validation

```python
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        print("Your age is:", age)
        break
    except ValueError:
        print("Please enter a valid positive age.")
```

This is useful in forms, apps, and login systems.

## Raising Your Own Exceptions

Sometimes you want to create your own error condition using `raise`.

```python
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Valid age:", age)
except ValueError as e:
    print("Error:", e)
```

## Summary

Exception handling helps us:

- prevent programs from crashing
- show user-friendly messages
- handle invalid input safely
- manage file and resource errors

The main structure is:

```python
try:
    # risky code
except ErrorType:
    # handle error
else:
    # runs when no error occurs
finally:
    # always runs
```

## Practice

Try these exercises:

1. Write a program that asks the user for a number and handles `ValueError`.
2. Divide two numbers and catch `ZeroDivisionError`.
3. Try to open a file that does not exist and catch `FileNotFoundError`.
4. Use `finally` to print a message after the operation.

### Example practice solution

```python
try:
    num = int(input("Enter a number: "))
    print("Square:", num * num)
except ValueError:
    print("That is not a valid integer.")
finally:
    print("Thanks for using the program.")
```

This will help you build programs that are more stable and user-friendly.
