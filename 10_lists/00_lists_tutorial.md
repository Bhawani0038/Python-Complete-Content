# Python Lists

A list is an ordered collection of values. Lists can store multiple items in one variable, and they can contain values of different data types.

```python
numbers = [10, 20, 30]
names = ["Asha", "Bilal", "Chen"]
mixed_values = ["Python", 42, 3.14, True]
```

Lists are ordered, changeable, and allow duplicate values.

## Creating Lists

Use square brackets to create a list. An empty list contains no items.

```python
empty_list = []
fruits = ["apple", "banana", "mango"]

print(empty_list)
print(fruits)
```

You can create a list from another iterable with `list()`:

```python
letters = list("Python")
numbers = list(range(1, 6))

print(letters)
print(numbers)
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n']
[1, 2, 3, 4, 5]
```

## List Length

Use `len()` to find the number of items in a list.

```python
fruits = ["apple", "banana", "mango"]
print(len(fruits))
```

The length counts items, not the number of characters inside each item.

## Indexing

List indexes start at `0`.

```python
colors = ["red", "green", "blue"]

print(colors[0])
print(colors[1])
print(colors[-1])
```

Output:

```text
red
green
blue
```

An index outside the list raises an `IndexError`.

## Slicing

Slicing extracts part of a list. The ending index is not included.

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])
print(numbers[::-1])
```

Output:

```text
[1, 2, 3]
[0, 1, 2]
[3, 4, 5]
[0, 2, 4]
[5, 4, 3, 2, 1, 0]
```

## Changing Items

Lists are mutable, so an item can be replaced using its index.

```python
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"

print(fruits)
```

Output:

```text
['apple', 'orange', 'mango']
```

Change several items with a slice:

```python
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [20, 30]
print(numbers)
```

## Adding Items

### `append()`

`append()` adds one item to the end of a list.

```python
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)
```

### `insert()`

`insert(index, item)` adds an item at a specific position.

```python
fruits = ["apple", "mango"]
fruits.insert(1, "banana")
print(fruits)
```

### `extend()`

`extend()` adds every item from another iterable.

```python
numbers = [1, 2]
numbers.extend([3, 4, 5])
print(numbers)
```

Do not confuse `append()` and `extend()`:

```python
first = [1, 2]
first.append([3, 4])
print(first)

second = [1, 2]
second.extend([3, 4])
print(second)
```

Output:

```text
[1, 2, [3, 4]]
[1, 2, 3, 4]
```

## Removing Items

### `remove()`

`remove(value)` removes the first matching value. It raises a `ValueError` if the value is not present.

```python
fruits = ["apple", "banana", "banana"]
fruits.remove("banana")
print(fruits)
```

### `pop()`

`pop()` removes and returns the last item. Give it an index to remove a specific item.

```python
fruits = ["apple", "banana", "mango"]
last_fruit = fruits.pop()
first_fruit = fruits.pop(0)

print(last_fruit)
print(first_fruit)
print(fruits)
```

### `del`

Use `del` to remove an item or a slice.

```python
numbers = [10, 20, 30, 40, 50]
del numbers[1]
del numbers[1:3]
print(numbers)
```

### `clear()`

`clear()` removes all items but keeps the list itself.

```python
items = [1, 2, 3]
items.clear()
print(items)
```

## Searching and Counting

Use `in` and `not in` to test membership.

```python
fruits = ["apple", "banana", "mango"]

print("banana" in fruits)
print("orange" not in fruits)
```

Use `index()` to find the position of the first matching item and `count()` to count matches.

```python
numbers = [2, 4, 2, 6, 2]

print(numbers.index(6))
print(numbers.count(2))
```

## Sorting and Reversing

`sort()` changes the original list.

```python
numbers = [4, 1, 3, 2]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)
```

`reverse()` reverses the original list.

```python
letters = ["a", "b", "c"]
letters.reverse()
print(letters)
```

`sorted()` returns a new sorted list and keeps the original unchanged.

```python
numbers = [4, 1, 3, 2]
sorted_numbers = sorted(numbers)

print(sorted_numbers)
print(numbers)
```

Sort strings alphabetically:

```python
names = ["Chen", "Asha", "Bilal"]
names.sort()
print(names)
```

## Copying Lists

Assigning one list to another variable does not create a separate list. Both names refer to the same list.

```python
first = [1, 2, 3]
second = first
second.append(4)

print(first)
print(second)
```

Use `copy()` or a full slice to create a shallow copy.

```python
first = [1, 2, 3]
second = first.copy()
second.append(4)

print(first)
print(second)
```

The `list()` constructor also creates a shallow copy:

```python
second = list(first)
```

## Joining Lists

Use `join()` to combine a list of strings into one string.

```python
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)
```

All items must be strings. Convert numeric items before joining them:

```python
numbers = [1, 2, 3]
text = ", ".join(str(number) for number in numbers)
print(text)
```

## Iterating Through a List

Use a `for` loop to visit every item.

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
	print(fruit)
```

Use `enumerate()` when you need both the index and the item.

```python
names = ["Asha", "Bilal", "Chen"]

for index, name in enumerate(names, start=1):
	print(f"{index}. {name}")
```

## Calculating with Lists

For a list of numbers, use `sum()`, `min()`, `max()`, and `len()`.

```python
scores = [72, 85, 91, 68]

print(sum(scores))
print(min(scores))
print(max(scores))
print(sum(scores) / len(scores))
```

## List Comprehensions

A list comprehension creates a list using a compact loop syntax.

```python
squares = [number ** 2 for number in range(1, 6)]
print(squares)
```

Add a condition to select items:

```python
even_numbers = [number for number in range(1, 11) if number % 2 == 0]
print(even_numbers)
```

Use an expression to transform each item:

```python
names = ["asha", "bilal", "chen"]
capitalized_names = [name.capitalize() for name in names]
print(capitalized_names)
```

For complex logic, a regular `for` loop may be easier to read.

## Nested Lists

A list can contain other lists. This is useful for tables and grids.

```python
matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]

print(matrix[0][1])
print(matrix[2][2])
```

Use nested loops to visit every item:

```python
for row in matrix:
	for value in row:
		print(value, end=" ")
	print()
```

## Unpacking Lists

Unpacking assigns list items to separate variables.

```python
colors = ["red", "green", "blue"]
first, second, third = colors

print(first)
print(second)
print(third)
```

Use `*` to collect several items:

```python
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

The number of variables must match the number of values unless a starred variable collects the remaining items.

## List of Different Data Types

Lists can contain different types, although lists with one clear purpose are usually easier to work with.

```python
student = ["Asha", 20, 92.5, True]

print(student[0])
print(student[1])
```

## Useful Built-in Functions

```python
numbers = [5, 2, 8, 1]

print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(sorted(numbers))
```

Use `all()` and `any()` for conditions over every item or at least one item.

```python
scores = [75, 82, 91]

print(all(score >= 50 for score in scores))
print(any(score == 100 for score in scores))
```

## Common Mistakes

### Confusing `append()` and `extend()`

`append()` adds one item, while `extend()` adds each item from another iterable.

### Changing a List While Iterating

Removing items from a list while looping over it can skip values. Build a new list instead:

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
```

### Copying by Assignment

Use `copy()` when you need an independent list. Assignment creates another reference to the same list.

### Aliasing Nested Lists

For nested lists, `copy()` is shallow. Changes to inner lists may still be shared. Use `deepcopy()` when a fully independent nested structure is required:

```python
from copy import deepcopy

original = [[1, 2], [3, 4]]
duplicate = deepcopy(original)
duplicate[0].append(5)

print(original)
print(duplicate)
```

## Summary

- Lists are ordered, mutable collections written with square brackets.
- Use indexes and slices to read parts of a list.
- Use `append()`, `insert()`, and `extend()` to add items.
- Use `remove()`, `pop()`, `del`, and `clear()` to remove items.
- Use `sort()` to change a list and `sorted()` to create a sorted copy.
- Use `copy()` when assigning an independent list is required.
- Use loops and `enumerate()` to process list items.
- Use list comprehensions for concise transformations and filtering.
- Nested lists can represent tables and grids.
