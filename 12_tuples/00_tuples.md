# Python Tuples

A tuple is an ordered collection of values. Tuples are similar to lists, but they are immutable, which means you cannot change, add, or remove items after the tuple is created.

```python
numbers = (10, 20, 30)
names = ("Asha", "Bilal", "Chen")
mixed_values = ("Python", 42, 3.14, True)
```

Tuples are ordered, allow duplicate values, and support indexing and slicing just like lists.

## Creating Tuples

Use parentheses to create a tuple.

```python
empty_tuple = ()
fruits = ("apple", "banana", "mango")

print(empty_tuple)
print(fruits)
```

Output:

```text
()
('apple', 'banana', 'mango')
```

You can also create a tuple from another iterable using `tuple()`.

```python
letters = tuple("Python")
numbers = tuple(range(1, 6))

print(letters)
print(numbers)
```

Output:

```text
('P', 'y', 't', 'h', 'o', 'n')
(1, 2, 3, 4, 5)
```

### Single Element Tuple

A tuple with only one item must include a trailing comma.

```python
single = (42,)
print(single)
```

Without the comma, Python treats it as a normal value in parentheses, not a tuple.

## Tuple Length

Use `len()` to know how many items are in a tuple.

```python
fruits = ("apple", "banana", "mango")
print(len(fruits))
```

Output:

```text
3
```

## Indexing

Tuple indexes start at `0`.

```python
colors = ("red", "green", "blue")

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

An index outside the tuple raises an `IndexError`.

## Slicing

Slicing works the same way as with lists. The ending index is excluded.

```python
numbers = (0, 1, 2, 3, 4, 5)

print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])
print(numbers[::-1])
```

Output:

```text
(1, 2, 3)
(0, 1, 2)
(3, 4, 5)
(0, 2, 4)
(5, 4, 3, 2, 1, 0)
```

## Immutable Nature

Tuples cannot be changed once created.

```python
numbers = (10, 20, 30)

# This will raise an error
# numbers[0] = 15
```

This is the biggest difference between a list and a tuple.

- List: mutable (can be changed)
- Tuple: immutable (cannot be changed)

## Tuple Operations

### Concatenation

You can join two tuples using `+`.

```python
first = (1, 2)
second = (3, 4)

result = first + second
print(result)
```

Output:

```text
(1, 2, 3, 4)
```

### Repetition

Use `*` to repeat a tuple.

```python
letters = ("A",)
print(letters * 5)
```

Output:

```text
('A', 'A', 'A', 'A', 'A')
```

## Membership

Use `in` and `not in` to check whether an item exists in a tuple.

```python
fruits = ("apple", "banana", "mango")

print("banana" in fruits)
print("orange" not in fruits)
```

Output:

```text
True
True
```

## Searching and Counting

Use `index()` to find the position of an item and `count()` to count how many times it appears.

```python
numbers = (2, 4, 2, 6, 2)

print(numbers.index(6))
print(numbers.count(2))
```

Output:

```text
3
3
```

## Tuple Methods

Tuples have only a few built-in methods because they are immutable.

### `count()`

Counts how many times a value appears.

```python
numbers = (1, 2, 2, 3, 2)
print(numbers.count(2))
```

### `index()`

Returns the index of the first matching value.

```python
numbers = (10, 20, 30, 40)
print(numbers.index(30))
```

Output:

```text
2
```

## Packing and Unpacking

A tuple can be created by packing multiple values into one tuple.

```python
student = ("Ali", 21, "A")
print(student)
```

Unpacking allows you to assign each item to a separate variable.

```python
student = ("Ali", 21, "A")
name, age, grade = student

print(name)
print(age)
print(grade)
```

Output:

```text
Ali
21
A
```

This is a very common and useful pattern in Python.

## Swapping Values

Tuples also make swapping values easy.

```python
a = 10
b = 20

(a, b) = (b, a)

print(a)
print(b)
```

Output:

```text
20
10
```

## Converting to and from Lists

You can convert a tuple to a list and vice versa.

```python
numbers = (1, 2, 3)
list_numbers = list(numbers)
print(list_numbers)

letters = ["a", "b", "c"]
tuple_letters = tuple(letters)
print(tuple_letters)
```

Output:

```text
[1, 2, 3]
('a', 'b', 'c')
```

## When to Use Tuples?

Use tuples when:

- You want data that should not be changed
- You want fixed values such as coordinates, dates, or settings
- You want to protect data from accidental modification

```python
point = (10, 20)
print(point[0], point[1])
```

Tuples are often used for fixed data structures because they are safe and efficient.

## Summary

A tuple is:

- ordered
- immutable
- indexed
- able to contain duplicate values
- useful for fixed data

```python
person = ("Sara", 18, "student")
print(person)
print(person[1])
```

Tuples are simple, reliable, and useful in many Python programs.

## Practice

Try these exercises:

1. Create a tuple of your favorite three colors.
2. Print the second item using indexing.
3. Use `len()` to find the number of items.
4. Try to change one element and observe the error.
5. Unpack a tuple into variables.

Example:

```python
colors = ("red", "green", "blue")
print(colors[1])
print(len(colors))
```

## Key Difference: List vs Tuple

```python
list_example = [1, 2, 3]
tuple_example = (1, 2, 3)

list_example[0] = 10
# tuple_example[0] = 10  # This would raise TypeError

print(list_example)
print(tuple_example)
```

Output:

```text
[10, 2, 3]
(1, 2, 3)
```

This shows why tuples are useful when you need a stable, non-changeable collection of values.
