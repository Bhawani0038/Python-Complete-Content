# Python Sets

A set is an unordered collection of unique items. It is used to store values without duplicates and to perform mathematical set operations like union, intersection, and difference.

```python
numbers = {1, 2, 3, 4}
fruits = {"apple", "banana", "mango"}
```

Sets are mutable, meaning you can add or remove items after creation. However, they do not keep order, and duplicate values are automatically removed.

## Creating Sets

Use curly braces `{}` to create a set.

```python
empty_set = set()
colors = {"red", "green", "blue"}

print(empty_set)
print(colors)
```

Output:

```text
set()
{'red', 'green', 'blue'}
```

Important: an empty pair of curly braces `{}` creates an empty dictionary, not a set. Use `set()` instead.

You can also create a set from any iterable using `set()`.

```python
letters = set("Python")
numbers = set(range(1, 6))

print(letters)
print(numbers)
```

Output:

```text
{'P', 'y', 't', 'h', 'o', 'n'}
{1, 2, 3, 4, 5}
```

## Set Characteristics

A set has these important properties:

- unordered
- does not allow duplicate values
- mutable
- supports membership testing
- supports mathematical set operations

```python
values = {10, 20, 20, 30, 30}
print(values)
```

Output:

```text
{10, 20, 30}
```

Duplicates are removed automatically.

## Length of a Set

Use `len()` to know how many items are in a set.

```python
numbers = {1, 2, 3, 4}
print(len(numbers))
```

Output:

```text
4
```

## Accessing Items

Sets are unordered, so you cannot access items by index.

```python
colors = {"red", "green", "blue"}

# This will raise an error
# print(colors[0])
```

Instead, use membership tests with `in`.

```python
print("green" in colors)
print("yellow" in colors)
```

Output:

```text
True
False
```

## Adding Items

Use `add()` to insert one item.

```python
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)
```

Output:

```text
{1, 2, 3, 4}
```

Use `update()` to add multiple items.

```python
numbers = {1, 2, 3}
numbers.update([3, 4, 5, 6])
print(numbers)
```

Output:

```text
{1, 2, 3, 4, 5, 6}
```

## Removing Items

### `remove()`

`remove()` deletes a specific item. It raises an error if the item is not found.

```python
numbers = {1, 2, 3, 4}
numbers.remove(3)
print(numbers)
```

### `discard()`

`discard()` also removes an item, but it does not raise an error if the item is missing.

```python
numbers = {1, 2, 3}
numbers.discard(10)
print(numbers)
```

### `pop()`

`pop()` removes and returns a random item from the set.

```python
numbers = {10, 20, 30, 40}
print(numbers.pop())
print(numbers)
```

Because sets are unordered, the removed item is unpredictable.

### `clear()`

`clear()` removes all items from the set.

```python
numbers = {1, 2, 3}
numbers.clear()
print(numbers)
```

Output:

```text
set()
```

## Set Operations

### Union

`union()` combines two sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)
print(result)
```

Output:

```text
{1, 2, 3, 4, 5}
```

### Intersection

`intersection()` keeps only common elements.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.intersection(set2)
print(result)
```

Output:

```text
{3, 4}
```

### Difference

`difference()` keeps items that are in the first set but not in the second.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

result = set1.difference(set2)
print(result)
```

Output:

```text
{1, 2}
```

### Symmetric Difference

`symmetric_difference()` keeps items that are in either set, but not both.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)
print(result)
```

Output:

```text
{1, 2, 5, 6}
```

## Membership and Comparison

```python
A = {1, 2, 3}
B = {2, 3}

print(B.issubset(A))
print(A.issuperset(B))
print(A.isdisjoint({4, 5}))
```

Output:

```text
True
True
True
```

## Looping Through a Set

You can iterate through a set using a loop.

```python
numbers = {10, 20, 30}

for item in numbers:
    print(item)
```

Output may vary because sets are unordered.

```text
10
20
30
```

## Set vs List vs Tuple

- List: ordered, mutable, allows duplicates
- Tuple: ordered, immutable, allows duplicates
- Set: unordered, mutable, no duplicates

```python
list_values = [1, 2, 2, 3]
tuple_values = (1, 2, 2, 3)
set_values = {1, 2, 2, 3}

print(list_values)
print(tuple_values)
print(set_values)
```

Output:

```text
[1, 2, 2, 3]
(1, 2, 2, 3)
{1, 2, 3}
```

## Summary

A set is a collection of unique values. It is useful when:

- you need to remove duplicates
- you want fast membership checks
- you need mathematical set operations

```python
students = {"Ali", "Aisha", "Zain"}
students.add("Ali")
print(students)
```

Output:

```text
{'Ali', 'Aisha', 'Zain'}
```

## Practice

Try these exercises:

1. Create a set of 5 numbers.
2. Add a number that already exists and observe the result.
3. Remove one item using `remove()`.
4. Find the union of two sets.
5. Check whether one set is a subset of another.

Example:

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
print(A.intersection(B))
```

This shows how sets are useful for grouping and comparing data.
