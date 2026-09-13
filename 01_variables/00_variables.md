# Python Variables

Variables are containers used to store data in a Python program. They help us save values so we can use them later in the program.

## What is a Variable?

A variable is like a box with a name. You can put a value inside it and then use that value whenever needed.

```python
name = "Alice"
print(name)
```

Output:

```python
Alice
```

## Declaring a Variable

In Python, you do not need to specify the type of a variable explicitly.

```python
age = 20
price = 15.75
is_student = True
```

Here:

- `age` stores an integer
- `price` stores a float
- `is_student` stores a boolean

## Rules for Naming Variables

Variable names must follow these rules:

- Must start with a letter or underscore
- Cannot start with a number
- Can contain letters, numbers, and underscores
- Cannot use spaces
- Cannot use Python keywords like `if`, `for`, `class`, etc.

Examples of valid variable names:

```python
name
_age
student1
```

Examples of invalid variable names:

```python
2name
my name
for
```

## Assigning Values to Variables

You can assign values using the `=` sign.

```python
x = 10
y = 20
```

You can also assign multiple variables in one line:

```python
a, b, c = 1, 2, 3
print(a, b, c)
```

## Reassigning Variables

Variables can be changed later.

```python
score = 10
score = 15
print(score)
```

Output:

```python
15
```

## Variable Types

Python supports different data types, and variables can store them.

### Integer

```python
count = 5
```

### Float

```python
height = 5.9
```

### String

```python
message = "Hello, Python!"
```

### Boolean

```python
is_active = True
```

## Example Program

```python
name = "John"
age = 18
city = "New York"

print("Name:", name)
print("Age:", age)
print("City:", city)
```

Output:

```python
Name: John
Age: 18
City: New York
```

## Important Notes

- Python variables are case-sensitive.
- `Name` and `name` are different variables.

```python
Name = "Alice"
name = "Bob"

print(Name)
print(name)
```

Output:

```python
Alice
Bob
```

## Summary

Variables are used to store data in Python. They make programs flexible and easier to work with. You can assign values, change them, and use them throughout your code.

## Practice Questions

1. Create a variable called `fruit` and assign it a value.
2. Print the variable.
3. Change the value of the variable and print it again.
4. Create variables for `name`, `age`, and `city` and print them together.

```python
fruit = "apple"
print(fruit)

fruit = "banana"
print(fruit)
```