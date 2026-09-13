# Python Operators

Operators are special symbols in Python that perform operations on values and variables. They are used to do calculations, compare values, assign data, and make decisions.

## Why Operators Are Important

Operators help us:

- perform arithmetic
- compare values
- assign values to variables
- combine conditions
- manipulate data efficiently

## 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| + | Addition | `5 + 3` | `8` |
| - | Subtraction | `5 - 3` | `2` |
| * | Multiplication | `5 * 3` | `15` |
| / | Division | `10 / 2` | `5.0` |
| % | Modulus | `10 % 3` | `1` |
| ** | Exponentiation | `2 ** 3` | `8` |
| // | Floor Division | `11 // 3` | `2` |

### Example

```python
x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
```

Output:

```python
13
7
30
3.3333333333333335
1
1000
3
```

## 2. Comparison Operators

Comparison operators are used to compare two values. They return `True` or `False`.

| Operator | Meaning | Example |
|----------|---------|---------|
| == | Equal to | `5 == 5` |
| != | Not equal to | `5 != 3` |
| > | Greater than | `7 > 3` |
| < | Less than | `3 < 7` |
| >= | Greater than or equal to | `7 >= 7` |
| <= | Less than or equal to | `3 <= 5` |

### Example

```python
print(5 == 5)
print(5 != 3)
print(8 > 4)
print(2 < 6)
print(7 >= 7)
print(3 <= 5)
```

Output:

```python
True
True
True
True
True
True
```

## 3. Assignment Operators

Assignment operators are used to assign values to variables.

| Operator | Example | Meaning |
|----------|---------|---------|
| = | `x = 5` | Assign value |
| += | `x += 2` | Add and assign |
| -= | `x -= 2` | Subtract and assign |
| *= | `x *= 2` | Multiply and assign |
| /= | `x /= 2` | Divide and assign |
| %= | `x %= 3` | Modulus and assign |

### Example

```python
x = 10
x += 5
print(x)

x *= 2
print(x)
```

Output:

```python
15
30
```

## 4. Logical Operators

Logical operators are used to combine conditions.

| Operator | Meaning | Example |
|----------|---------|---------|
| and | Returns True if both are True | `a and b` |
| or | Returns True if at least one is True | `a or b` |
| not | Reverses the result | `not a` |

### Example

```python
age = 20
student = True

print(age >= 18 and student)
print(age < 18 or student)
print(not student)
```

Output:

```python
True
True
False
```

## 5. Identity Operators

Identity operators check whether two variables refer to the same object.

| Operator | Meaning |
|----------|---------|
| is | True if both are the same object |
| is not | True if they are not the same object |

### Example

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(id(a))
print(id(b))
print(id(c))

print(a is b)
print(a is c)
print(a is not c)
```

Output:

```python
True
False
True
```

## 6. Membership Operators

Membership operators test whether a value exists in a sequence such as a string, list, or tuple.

| Operator | Meaning |
|----------|---------|
| in | True if value is found |
| not in | True if value is not found |

### Example

```python
letters = ["a", "b", "c"]
print("a" in letters)
print("z" not in letters)
```

Output:

```python
True
True
```

## 7. Bitwise Operators

Bitwise operators work on binary numbers.

| Operator | Meaning |
|----------|---------|
| & | Bitwise AND |
| | | Bitwise OR |
| ^ | Bitwise XOR |
| ~ | Bitwise NOT |
| << | Left shift |
| >> | Right shift |

These are less common for beginners, but they are useful in advanced programming.

## Operator Precedence

Python follows an order of operations, similar to mathematics.

Example:

```python
result = 10 + 5 * 2
print(result)
```

Output:

```python
20
```

Because multiplication is done before addition.

## Summary

Python operators are symbols used to perform operations on values and variables. The main types are:

- arithmetic operators
- comparison operators
- assignment operators
- logical operators
- identity operators
- membership operators
- bitwise operators

Understanding operators is essential for writing effective Python programs.

## Practice Exercise

Try these examples:

```python
x = 15
y = 4

print(x + y)
print(x > y)
print(x % y)
print(x == y)
print(x >= 10 and y <= 5)
```

This will help you understand how operators work in real code.
