# Python Data Types Overview

In Python, data types tell us what kind of value a variable holds. Understanding data types is important because different values are used in different ways in a program.

## What is a Data Type?

A data type is a category for a value. For example:

- `10` is an integer
- `3.14` is a float
- `"Hello"` is a string
- `True` is a boolean

Python automatically identifies the type of a value when you assign it to a variable.

## Common Data Types in Python

### 1. Integer (`int`)

Integers are whole numbers without decimals.

```python
age = 25
count = 100
```

Examples:

```python
5
-10
0
```

### 2. Float (`float`)

Floats are numbers with decimal points.

```python
price = 19.99
height = 5.8
```

Examples:

```python
3.14
2.0
-8.5
```

### 3. String (`str`)

Strings are sequences of characters used to represent text.

```python
name = "Alice"
message = 'Hello, World!'
```

Strings can be enclosed in single quotes or double quotes.

### 4. Boolean (`bool`)

Booleans represent truth values: `True` or `False`.

```python
is_active = True
is_logged_in = False
```

### 5. List (`list`)

A list is an ordered collection of items. Lists are mutable, which means their values can be changed.

```python
numbers = [1, 2, 3, 4]
names = ["Alice", "Bob", "Charlie"]
```

### 6. Tuple (`tuple`)

A tuple is similar to a list, but it is immutable. Once created, it cannot be changed.

```python
point = (10, 20)
```

### 7. Dictionary (`dict`)

A dictionary stores data in key-value pairs.

```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
```

### 8. Set (`set`)

A set is an unordered collection of unique items.

```python
numbers = {1, 2, 3, 3, 4}
print(numbers)
```

Output:

```python
{1, 2, 3, 4}
```

## Type Checking

You can check the type of a variable using the `type()` function.

```python
x = 10
print(type(x))

name = "Python"
print(type(name))
```

Output:

```python
<class 'int'>
<class 'str'>
```

## Example Program

```python
age = 21
price = 12.50
name = "Sam"
active = True

print(type(age))
print(type(price))
print(type(name))
print(type(active))
```

Output:

```python
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

## Why Data Types Matter

Data types help Python understand how to process values correctly. For example:

- You can add integers and floats together
- You can concatenate strings with other strings
- You must be careful when mixing types

```python
print("5" + "3") # "53"
print(5 + 3)        # 8
print("Hello " + "World")  # Hello World
```

## Summary

Python has many built-in data types, including:

- `int` for integers
- `float` for decimal numbers
- `str` for text
- `bool` for True/False
- `list` for ordered collections
- `tuple` for fixed collections
- `dict` for key-value pairs
- `set` for unique values

Understanding data types is a key step in learning Python.
