# Python File Handling

File handling allows a Python program to read data from files and write data to files. This is very useful for saving user data, logs, reports, and configuration information.

In Python, we use the built-in `open()` function to work with files.

```python
file = open("example.txt", "r")
print(file.read())
file.close()
```

## Opening a File

The syntax for opening a file is:

```python
open(filename, mode)
```

The `mode` tells Python how to open the file.

### Common file modes

- `"r"` - read mode (default)
- `"w"` - write mode
- `"a"` - append mode
- `"rb"` - read in binary mode
- `"wb"` - write in binary mode

## Reading a File

### Example file

A sample file named `sample.txt` is used in this lesson.

```text
Hello, Python!
This is a sample file.
File handling is useful for reading and writing data.
```

### Read the whole file

```python
file = open("sample.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()
```

You can also use the ready-made example script in [p01.py](p01.py):

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

### Read a certain number of characters

```python
file = open("example.txt", "r")
print(file.read(10))
file.close()
```

This reads only the first 10 characters.

### Read line by line

```python
file = open("example.txt", "r")
print(file.readline())
print(file.readline())
file.close()
```

### Read all lines as a list

```python
file = open("example.txt", "r")
lines = file.readlines()
print(lines)
file.close()
```

## Writing to a File

Use `"w"` mode to write to a file.

```python
file = open("example.txt", "w")
file.write("Hello, Python!\n")
file.write("This is file handling.")
file.close()
```

This creates a new file if it does not exist. If the file already exists, it overwrites the old content.

### Writing multiple lines

```python
file = open("example.txt", "w")
file.writelines(["First line\n", "Second line\n", "Third line\n"])
file.close()
```

## Appending to a File

Use `"a"` mode to add content to the end of a file without deleting the existing content.

```python
file = open("example.txt", "a")
file.write("\nThis line is appended.")
file.close()
```

## Using `with` Statement

It is best practice to use `with` when working with files. It automatically closes the file after the block ends.

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

This is cleaner and safer than manually calling `close()`.

## File Modes Example

```python
with open("sample.txt", "w") as file:
    file.write("Welcome to Python file handling\n")

with open("sample.txt", "r") as file:
    print(file.read())
```

## Checking if a File Exists

Use `os.path.exists()` to check whether a file exists.

```python
import os

if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File does not exist")
```

## Reading and Writing Binary Files

Binary files store data in bytes rather than text.

```python
with open("image.bin", "wb") as file:
    file.write(b"\x00\x01\x02\x03")

with open("image.bin", "rb") as file:
    data = file.read()
    print(data)
```

## File Handling Best Practices

- Always close the file after use
- Use `with open(...)` whenever possible
- Be careful with `"w"` mode because it overwrites files
- Use `"a"` when you want to add new content instead of replacing old content

## Common Errors

### FileNotFoundError

This happens when you try to open a file that does not exist in read mode.

```python
# file = open("missing.txt", "r")
# This will raise FileNotFoundError
```

### PermissionError

This happens when the file cannot be opened because of permission restrictions.

## Example Program

```python
with open("notes.txt", "w") as file:
    file.write("Python is fun\n")
    file.write("File handling is important\n")

with open("notes.txt", "r") as file:
    print(file.read())
```

Output:

```text
Python is fun
File handling is important
```

## Summary

File handling in Python lets us:

- read data from files
- write new content to files
- append additional data to existing files
- manage text and binary files

The most common functions are:

- `open()`
- `read()`
- `write()`
- `readline()`
- `readlines()`
- `close()`

## Practice

Try these exercises:

1. Create a file named `students.txt` and write 3 names in it.
2. Read the file and print its content.
3. Append a new name to the file.
4. Open the file in read mode and print each line separately.

Example:

```python
with open("students.txt", "w") as file:
    file.write("Ali\n")
    file.write("Aisha\n")
    file.write("Zain\n")

with open("students.txt", "r") as file:
    print(file.read())
```

This gives you the basic foundation for working with files in Python.
