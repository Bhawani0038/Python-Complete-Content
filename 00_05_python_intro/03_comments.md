# Python Comments

Comments are notes written in the source code that are ignored by Python when the program runs. They are useful for explaining what the code does, making programs easier to understand, and helping other developers read your work.

## Why Use Comments?

Comments are helpful because they:

- explain the purpose of code
- make programs easier to understand
- help with teamwork
- remind you what a block of code does later
- make debugging easier

## Single-Line Comments

Single-line comments start with `#`.

```python
# This is a comment
print("Hello, World!")
```

Python ignores everything after `#` on that line.

## Multi-Line Comments

Python does not have a special multi-line comment syntax like some other languages, but you can use multiple `#` lines:

```python
# This is line one of a comment
# This is line two of a comment
# This is line three of a comment
```

You can also use triple quotes for larger text blocks, but those are usually treated as strings, not comments:

```python
"""This is a multi-line string used as documentation."""
```

## Comments in Code

```python
# Calculate the total price
price = 100
quantity = 2

total = price * quantity
print(total)
```

## Good Commenting Practice

Use comments to explain why something is done, not just what it does.

### Bad example

```python
x = x + 1  # add one to x
```

### Better example

```python
# Increase the score when the user answers correctly
score = score + 1
```

## Commenting Out Code

Sometimes you may want to temporarily disable a line of code without deleting it.

```python
# print("This line is temporarily disabled")
```

This helps when debugging or testing alternative logic.

## Example Program with Comments

```python
# Program to calculate the area of a rectangle
length = 10
width = 5

area = length * width

# Print the result
print("Area:", area)
```

Output:

```python
Area: 50
```

## Summary

Comments are an important part of writing clean and understandable Python code. They help explain logic, improve readability, and make code easier to maintain.

## Practice

Write a short Python program with at least 3 comments explaining the different steps.

Example:

```python
# Ask the user for their name
name = "Alice"

# Print a greeting message
print("Hello, " + name)
```

Remember: comments do not affect how the program works; they only help the reader understand it.
