# Python `while` Loops

A `while` loop repeats a block of code as long as a condition is `True`. It is useful when you do not know in advance how many times the loop needs to run.

## Basic Syntax

```python
while condition:
	# code to repeat
	pass
```

- `while` starts the loop.
- The condition is checked before every iteration.
- The indented block runs only when the condition is `True`.
- The loop stops when the condition becomes `False`.

```python
count = 1

while count <= 5:
	print(count)
	count += 1
```

Output:

```text
1
2
3
4
5
```

## How a `while` Loop Works

Each iteration follows the same order:

1. Check the condition.
2. Run the indented block if the condition is `True`.
3. Update one or more values used by the condition.
4. Check the condition again.

The update is important. Without it, the condition may never become `False`.

```python
number = 3

while number > 0:
	print(number)
	number -= 1

print("Go!")
```

Output:

```text
3
2
1
Go!
```

## Counting with a `while` Loop

Use an initial value, a condition, and an update to count upward or downward.

```python
number = 2

while number <= 10:
	print(number)
	number += 2
```

This prints the even numbers from 2 through 10.

To count backward, use a negative update:

```python
number = 5

while number >= 1:
	print(number)
	number -= 1
```

## Accumulating a Total

A `while` loop can process values one at a time and keep a running total.

```python
number = 1
total = 0

while number <= 5:
	total += number
	number += 1

print(total)
```

Output:

```text
15
```

## Looping Through a String with an Index

Use an index to visit each character in a string. The index must be increased on every iteration.

```python
word = "Python"
index = 0

while index < len(word):
	print(word[index])
	index += 1
```

## `break`

The `break` statement stops the loop immediately, even if the condition is still `True`.

```python
number = 1

while number <= 10:
	if number == 6:
		break
	print(number)
	number += 1
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

The `continue` statement skips the rest of the current iteration and starts the next condition check.

```python
number = 0

while number < 5:
	number += 1
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

When using `continue`, update the loop variable before reaching it. Otherwise, the loop may never progress.

## The `else` Block

A `while` loop can have an `else` block. The `else` block runs when the condition becomes `False`. It does not run if the loop stops with `break`.

```python
number = 1

while number <= 3:
	print(number)
	number += 1
else:
	print("Loop completed")
```

Output:

```text
1
2
3
Loop completed
```

## Input Validation

`while` loops are useful when a program should keep asking until the user enters an acceptable value.

```python
password = input("Enter the password: ")

while password != "python123":
	print("Incorrect password")
	password = input("Try again: ")

print("Access granted")
```

## Infinite Loops

An infinite loop never ends because its condition remains `True`.

```python
number = 1

while number <= 5:
	print(number)
```

This loop is missing `number += 1`, so `number` always remains 1. Add an update or use `break` when an intentional exit condition is reached.

An intentional infinite loop is often written with `while True`:

```python
while True:
	command = input("Enter a command, or q to quit: ")
	if command == "q":
		break
	print(f"You entered: {command}")
```

## `while` Compared with `for`

- Use a `for` loop when iterating through a sequence or a known range of values.
- Use a `while` loop when repetition depends on a changing condition or user input.

## Summary

- A `while` loop repeats while its condition is `True`.
- Initialize the values used by the condition before the loop.
- Update those values inside the loop so the loop can finish.
- Use `break` to stop immediately.
- Use `continue` to skip the rest of one iteration.
- A loop `else` block runs only when the loop ends normally.
- Be careful with conditions that can remain `True` forever.
