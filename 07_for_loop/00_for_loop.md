# Python `for` Loops

A `for` loop repeats a block of code for every item in a sequence. It is useful when you know what collection of values you want to visit or how many times an action should repeat.

## Why Use a `for` Loop?

For loops help avoid writing the same code many times. For example, instead of writing three `print()` statements, a loop can print three values:

```python
for number in (1, 2, 3):
	print(number)
```

Output:

```text
1
2
3
```

## Basic Syntax

```python
for variable in sequence:
	# code to repeat
```

- `for` starts the loop.
- `variable` temporarily stores the current item.
- `in` selects the sequence to visit.
- The indented block runs once for each item.

```python
names = ["Asha", "Bilal", "Chen"]

for name in names:
	print(f"Hello, {name}!")
```

Output:

```text
Hello, Asha!
Hello, Bilal!
Hello, Chen!
```

## Using `range()`

The `range()` function generates a sequence of numbers. The ending value is not included.

### `range(stop)`

```python
for number in range(5):
	print(number)
```

Output:

```text
0
1
2
3
4
```

### `range(start, stop)`

```python
for number in range(1, 6):
	print(number)
```

Output:

```text
1
2
3
4
5
```

### `range(start, stop, step)`

```python
for number in range(2, 11, 2):
	print(number)
```

Output:

```text
2
4
6
8
10
```

Use a negative step to count backward:

```python
for number in range(5, 0, -1):
	print(number)
```

## Looping Through Strings

A string is a sequence of characters, so a `for` loop can visit each character.

```python
word = "Python"

for character in word:
	print(character)
```

Output:

```text
P
y
t
h
o
n
```

## Looping Through Lists and Tuples

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
	print(fruit)
```

The same pattern works with tuples:

```python
colors = ("red", "green", "blue")

for color in colors:
	print(color)
```

## Looping Through a Dictionary

By default, a loop visits dictionary keys.

```python
student = {"name": "Mina", "age": 20, "course": "Python"}

for key in student:
	print(key, student[key])
```

Use `.items()` to receive both the key and value:

```python
for key, value in student.items():
	print(f"{key}: {value}")
```

## Using `enumerate()`

`enumerate()` provides both the position and the item. The starting position can be changed.

```python
fruits = ["apple", "banana", "mango"]

for position, fruit in enumerate(fruits, start=1):
	print(position, fruit)
```

Output:

```text
1 apple
2 banana
3 mango
```

## `break`

The `break` statement stops the loop immediately.

```python
for number in range(1, 11):
	if number == 6:
		break
	print(number)
```

Output:

```text
1
2
3
4
5
```

## `continue`

The `continue` statement skips the current iteration and moves to the next one.

```python
for number in range(1, 6):
	if number == 3:
		continue
	print(number)
```

Output:

```text
1
2
4
5
```

## The `else` Block

The `else` block runs after a loop finishes normally. It does not run when the loop is stopped with `break`.

```python
for number in range(3):
	print(number)
else:
	print("Loop completed")
```

Output:

```text
0
1
2
Loop completed
```

## Nested `for` Loops

A loop inside another loop is called a nested loop.

```python
for row in range(1, 4):
	for column in range(1, 4):
		print(f"row {row}, column {column}")
```

Nested loops are useful for grids, tables, and multiplication tables.

```python
for number in range(1, 4):
	for multiplier in range(1, 4):
		print(number * multiplier, end=" ")
	print()
```

Output:

```text
1 2 3
2 4 6
3 6 9
```

## Calculating a Total with a Loop

```python
prices = [10, 25, 15]
total = 0

for price in prices:
	total += price

print(total)
```

Output:

```text
50
```

Python also provides the built-in `sum()` function for this common task:

```python
prices = [10, 25, 15]
print(sum(prices))
```

## Summary

- Use a `for` loop to repeat code for every item in a sequence.
- Use `range()` to generate numbers.
- Use `break` to stop a loop.
- Use `continue` to skip one iteration.
- Use `enumerate()` when you need an index and an item.
- Use nested loops for repeated rows and columns.
- Indentation defines the body of the loop.

## Practice Exercises


name | age | salary
20 | 30 |40