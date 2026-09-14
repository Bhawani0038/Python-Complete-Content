# Python Dictionaries

A dictionary is a collection of key-value pairs. Each key is unique and maps to a value. Dictionaries are useful when you want to store data by meaningful names instead of only by index.

```python
student = {
    "name": "Aisha",
    "age": 20,
    "course": "Python"
}

print(student)
```

Output:

```text
{'name': 'Aisha', 'age': 20, 'course': 'Python'}
```

Dictionaries are unordered in older Python versions, but in modern Python they preserve insertion order.

## Creating a Dictionary

Use curly braces `{}` to create a dictionary.

```python
empty_dict = {}
student = {"name": "Aisha", "age": 20}

print(empty_dict)
print(student)
```

You can also create a dictionary using the `dict()` function.

```python
student = dict(name="Aisha", age=20, course="Python")
print(student)
```

Output:

```text
{'name': 'Aisha', 'age': 20, 'course': 'Python'}
```

## Key-Value Pairs

A dictionary stores values using keys.

```python
person = {
    "name": "Ali",
    "city": "Karachi",
    "is_student": True
}
```

Here:

- `"name"` is the key
- `"Ali"` is the value
- `"city"` is another key
- `"Karachi"` is its value

## Accessing Values

Use the key inside square brackets to access a value.

```python
student = {"name": "Aisha", "age": 20, "course": "Python"}

print(student["name"])
print(student["age"])
```

Output:

```text
Aisha
20
```

If the key does not exist, Python raises a `KeyError`.

```python
# print(student["marks"])  # KeyError
```

Use `get()` to avoid errors when a key may not exist.

```python
student = {"name": "Aisha", "age": 20}

print(student.get("name"))
print(student.get("marks", "Not available"))
```

Output:

```text
Aisha
Not available
```

## Adding and Updating Values

You can add a new key-value pair by assigning to a new key.

```python
student = {"name": "Aisha"}
student["age"] = 20
student["course"] = "Python"

print(student)
```

Output:

```text
{'name': 'Aisha', 'age': 20, 'course': 'Python'}
```

To update an existing value, assign a new value to the key.

```python
student["age"] = 21
print(student)
```

## Removing Items

### `pop()`

`pop()` removes a key and returns its value.

```python
student = {"name": "Aisha", "age": 20, "course": "Python"}

age = student.pop("age")
print(age)
print(student)
```

Output:

```text
20
{'name': 'Aisha', 'course': 'Python'}
```

### `popitem()`

`popitem()` removes the last inserted key-value pair.

```python
student = {"name": "Aisha", "age": 20}
student.popitem()
print(student)
```

### `del`

Use `del` to delete a specific key.

```python
student = {"name": "Aisha", "age": 20}
del student["age"]
print(student)
```

### `clear()`

`clear()` removes all items from the dictionary.

```python
student = {"name": "Aisha", "age": 20}
student.clear()
print(student)
```

Output:

```text
{}
```

## Dictionary Length

Use `len()` to count the number of key-value pairs.

```python
student = {"name": "Aisha", "age": 20, "course": "Python"}
print(len(student))
```

Output:

```text
3
```

## Checking Keys and Values

Use `in` to check whether a key exists.

```python
student = {"name": "Aisha", "age": 20}

print("name" in student)
print("city" in student)
```

Output:

```text
True
False
```

You can also get all keys and values separately.

```python
student = {"name": "Aisha", "age": 20, "course": "Python"}

print(student.keys())
print(student.values())
print(student.items())
```

Output:

```text
dict_keys(['name', 'age', 'course'])
dict_values(['Aisha', 20, 'Python'])
dict_items([('name', 'Aisha'), ('age', 20), ('course', 'Python')])
```

## Looping Through a Dictionary

### Loop through keys

```python
student = {"name": "Aisha", "age": 20, "course": "Python"}

for key in student:
    print(key)
```

### Loop through values

```python
for value in student.values():
    print(value)
```

### Loop through key-value pairs

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Aisha
age 20
course Python
```

## Nested Dictionaries

A dictionary can contain another dictionary as a value.

```python
students = {
    "student1": {"name": "Aisha", "marks": 90},
    "student2": {"name": "Bilal", "marks": 85}
}

print(students["student1"]["name"])
```

Output:

```text
Aisha
```

This is useful for storing structured data like user profiles or records.

## Copying a Dictionary

Use `copy()` to create a duplicate dictionary.

```python
student = {"name": "Aisha", "age": 20}
new_student = student.copy()

new_student["age"] = 21

print(student)
print(new_student)
```

Output:

```text
{'name': 'Aisha', 'age': 20}
{'name': 'Aisha', 'age': 21}
```

This prevents changes in the copied dictionary from affecting the original.

## Dictionary Comprehension

Dictionary comprehension lets you create dictionaries in a compact way.

```python
squares = {x: x * x for x in range(1, 6)}
print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

You can also create a dictionary from a list of names.

```python
names = ["Aisha", "Bilal", "Chen"]
lengths = {name: len(name) for name in names}
print(lengths)
```

## Real-Life Use Cases

Dictionaries are ideal for:

- Storing student records
- Saving settings and preferences
- Mapping words to meanings
- Representing JSON data
- Counting frequency of items

Example:

```python
frequency = {}
for char in "banana":
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)
```

Output:

```text
{'b': 1, 'a': 3, 'n': 2}
```

## Summary

A dictionary stores data as key-value pairs. Keys are unique and are used to access values quickly.

Common dictionary operations:

- Create: `{}` or `dict()`
- Access: `dict[key]` or `dict.get(key)`
- Add: `dict[key] = value`
- Update: `dict[key] = new_value`
- Remove: `pop()`, `del`, `clear()`
- Loop: `for key, value in dict.items()`

Dictionaries are one of the most important data structures in Python because they are fast, flexible, and widely used in real-world programs.

## Practice Questions

1. Create a dictionary with your name, age, and city.
2. Print the value of the `city` key.
3. Add a new key called `country` with a value.
4. Update the age.
5. Remove one key from the dictionary.
6. Print all items using `items()`.

```python
# Example solution
student = {"name": "Aisha", "age": 20, "city": "Karachi"}
print(student["city"])
student["country"] = "Pakistan"
student["age"] = 21
student.pop("city")
print(student.items())
```
