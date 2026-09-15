## JSON Module in Python

JSON stands for JavaScript Object Notation. It is a lightweight format used to store and exchange data.

JSON is widely used in:

- APIs
- web applications
- configuration files
- data storage
- mobile apps

Python has a built-in module called `json` to work with JSON data.

```python
import json
```

## Why JSON is Important?

Many websites and apps send and receive data in JSON format.

Example of JSON data:

```json
{
  "name": "Ali",
  "age": 25,
  "city": "Lahore"
}
```

This is a very common format for transferring structured information.

## JSON in Python

The `json` module allows us to:

- convert Python objects into JSON strings
- write JSON to files
- read JSON from files
- convert JSON into Python dictionaries and lists

## 1. `json.dumps()`

`dumps()` converts a Python object into a JSON string.

```python
import json

person = {
	"name": "Ayesha",
	"age": 22,
	"city": "Karachi"
}

json_string = json.dumps(person)
print(json_string)
print(type(json_string))
```

Output:

```python
{"name": "Ayesha", "age": 22, "city": "Karachi"}
<class 'str'>
```

This means the Python dictionary is now converted into a JSON string.

## 2. `json.loads()`

`loads()` converts a JSON string into a Python object.

```python
import json

data = '{"name": "Ali", "age": 30, "city": "Islamabad"}'

person = json.loads(data)
print(person)
print(type(person))
```

Output:

```python
{'name': 'Ali', 'age': 30, 'city': 'Islamabad'}
<class 'dict'>
```

Here, the JSON string is converted into a Python dictionary.

## 3. `json.dump()`

`dump()` writes JSON data to a file.

```python
import json

student = {
	"name": "Hamza",
	"roll_no": 12,
	"marks": 89
}

with open("student.json", "w") as file:
	json.dump(student, file)

print("JSON data saved to file.")
```

This creates a file named `student.json` and stores the dictionary in JSON form.

## 4. `json.load()`

`load()` reads JSON data from a file and converts it into Python objects.

```python
import json

with open("student.json", "r") as file:
	data = json.load(file)

print(data)
print(data["name"])
```

Output:

```python
{'name': 'Hamza', 'roll_no': 12, 'marks': 89}
Hamza
```

## JSON and Python Data Types

JSON supports data types similar to Python:

- object -> dictionary
- array -> list
- string -> string
- number -> int or float
- true -> True
- false -> False
- null -> None

Example:

```python
import json

data = {
	"name": "Zain",
	"active": True,
	"score": 95.5,
	"skills": ["Python", "SQL"],
	"address": None
}

json_data = json.dumps(data)
print(json_data)
```

Output:

```python
{"name": "Zain", "active": true, "score": 95.5, "skills": ["Python", "SQL"], "address": null}
```

## Practical Example 1: Reading User Data from JSON

```python
import json

user_data = '{"username": "ali123", "email": "ali@gmail.com", "password": "secret123"}'

user = json.loads(user_data)
print("Username:", user["username"])
print("Email:", user["email"])
```

This is a real-world example because many apps receive JSON data from a server.

## Practical Example 2: Save Product Information

```python
import json

product = {
	"name": "Laptop",
	"brand": "Dell",
	"price": 75000,
	"in_stock": True
}

with open("product.json", "w") as file:
	json.dump(product, file)

print("Product saved successfully.")
```

When a shop app saves product details, it often stores them in JSON format.

## Practical Example 3: Read Student Records

```python
import json

students = [
	{"name": "Sara", "marks": 90},
	{"name": "Usman", "marks": 85},
	{"name": "Hira", "marks": 92}
]

with open("students.json", "w") as file:
	json.dump(students, file)

with open("students.json", "r") as file:
	data = json.load(file)

print(data)
print(data[0]["name"])
```

This is useful in school management or attendance systems.

## Practical Example 4: Login Data in JSON

```python
import json

user = {
	"username": "admin",
	"roles": ["admin", "editor"],
	"is_active": True
}

json_string = json.dumps(user, indent=4)
print(json_string)
```

The `indent=4` parameter makes the JSON output neat and readable.

## Practical Example 5: API Response Simulation

```python
import json

response = {
	"status": "success",
	"message": "User logged in",
	"data": {
		"id": 101,
		"name": "Aisha"
	}
}

print(json.dumps(response, indent=2))
```

This kind of structure is common in API responses.

## `indent` Parameter

The `indent` parameter makes JSON more readable when printed.

```python
import json

person = {"name": "Bilal", "age": 28, "city": "Multan"}

print(json.dumps(person, indent=4))
```

Output:

```python
{
	"name": "Bilal",
	"age": 28,
	"city": "Multan"
}
```

## `sort_keys` Parameter

This sorts keys alphabetically in JSON output.

```python
import json

person = {"city": "Lahore", "name": "Nimra", "age": 24}

print(json.dumps(person, sort_keys=True, indent=4))
```

## JSON and Files

JSON is often used to save app settings and user data.

Example:

```python
import json

settings = {
	"theme": "dark",
	"notifications": True,
	"language": "en"
}

with open("settings.json", "w") as file:
	json.dump(settings, file, indent=4)

with open("settings.json", "r") as file:
	loaded = json.load(file)

print(loaded)
```

This is exactly how many applications store their configuration.

## Common JSON Functions

Here are the main ones you should remember:

- `json.dumps(obj)` -> convert Python object to JSON string
- `json.loads(str)` -> convert JSON string to Python object
- `json.dump(obj, file)` -> write JSON to a file
- `json.load(file)` -> read JSON from a file

## Comparing Python and JSON

| Python | JSON |
|---|---|
| dict | object |
| list | array |
| tuple | array |
| str | string |
| int | number |
| float | number |
| True | true |
| False | false |
| None | null |

## Summary

The `json` module helps us work with structured data in a standard format.

It is used when:

- saving application data
- reading API responses
- storing settings
- exchanging data between systems

It is one of the most important modules in Python because JSON is used everywhere on the web and in software applications.
