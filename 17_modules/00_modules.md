# Python Modules

A module is simply a Python file that contains reusable code. Modules help you organize your program by separating functions, variables, and classes into different files.

Instead of writing everything in one file, you can place related code in a module and import it whenever needed.

## Why Use Modules?

Modules are useful when you want to:

- reuse code across multiple programs
- organize large projects
- keep files smaller and easier to read
- separate logic into different sections

For example, you might create one module for user functions, another for calculations, and another for file operations.

## Creating a Module

A module is just a `.py` file.

For example, create a file named `greetings.py`:

```python
# greetings.py

def greet(name):
    print(f"Hello, {name}!")


def farewell(name):
    print(f"Goodbye, {name}!")
```

Now this file is a module named `greetings`.

## Importing a Module

To use a module, import it in another Python file.

```python
import greetings

greetings.greet("Aisha")
greetings.farewell("Aisha")
```

Output:

```text
Hello, Aisha!
Goodbye, Aisha!
```

This is the most common way to access functions from a module.

## Different Ways to Access Module Content

### 1. Import the module

```python
import greetings

greetings.greet("Ali")
```

This keeps the module name as a namespace.

### 2. Import a specific function from a module

```python
from greetings import greet

greet("Sara")
```

This is cleaner when you only need one or two functions.

### 3. Import everything from a module

```python
from greetings import *

greet("Bilal")
farewell("Bilal")
```

This imports all public names. It is possible, but not always recommended because it can cause name conflicts.

### 4. Import with an alias

```python
import greetings as g

g.greet("Nadia")
```

This is useful when the module name is long or when you want shorter code.

### 5. Import a specific item with an alias

```python
from greetings import greet as welcome

welcome("Zain")
```

This is useful when you want a more readable name.

## Module Example with a Calculator

Create a file named `calculator.py`:

```python
# calculator.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b
```

Now use it in another file:

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
```

Output:

```text
15
5
50
```

## Module Variables and Constants

A module can also contain variables.

```python
# config.py

app_name = "My App"
version = 1.0
```

Use it in another file:

```python
import config

print(config.app_name)
print(config.version)
```

## `__name__` and Main Module

Python sets `__name__` to `"__main__"` when a file is run directly.

```python
# demo.py

def show():
    print("This is a module function")


if __name__ == "__main__":
    print("This file is being run directly")
    show()
```

This is a very important pattern in Python. It prevents code from running when the file is imported as a module.

## Built-in Modules

Python already includes many useful modules.

Examples:

```python
import math
import random
import datetime

print(math.sqrt(25))
print(random.randint(1, 10))
print(datetime.datetime.now())
```

Output will vary depending on values and time.

## Creating Your Own Module Directory

You can place related modules into a folder. That folder becomes a package if it contains an `__init__.py` file.

## What is a Package?

A package is a folder that contains Python modules. It helps organize multiple modules together.

Example structure:

```text
project/
    myapp/
        __init__.py
        math_tools.py
        user_tools.py
        main.py
```

### Example: `math_tools.py`

```python
# math_tools.py

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b
```

### Example: `user_tools.py`

```python
# user_tools.py

def greet(name):
    return f"Hello, {name}!"
```

### Example: `__init__.py`

```python
# __init__.py
# This file can be empty or can contain package-level code
```

## Importing a Package

If the project folder is in the same directory, you can import the package like this:

```python
import myapp.math_tools

print(myapp.math_tools.add(5, 3))
```

You can also import specific items:

```python
from myapp.math_tools import add

print(add(5, 3))
```

Or from the package root:

```python
from myapp import user_tools

print(user_tools.greet("Ayesha"))
```

## Using Nested Packages

You can create subfolders inside a package.

Example structure:

```text
project/
    myapp/
        __init__.py
        helpers/
            __init__.py
            strings.py
```

### `strings.py`

```python
# strings.py

def uppercase(text):
    return text.upper()
```

### Importing nested package content

```python
from myapp.helpers.strings import uppercase

print(uppercase("python"))
```

This is how larger real applications organize their code.

## Relative Imports

Relative imports are used inside a package.

Example:

```python
# myapp/user_tools.py
from .math_tools import add

print(add(3, 4))
```

This means: import `add` from the same package.

Relative imports are especially useful when your modules belong to the same package.

## Absolute vs Relative Imports

### Absolute import

```python
import myapp.math_tools
```

### Relative import

```python
from .math_tools import add
```

Absolute imports are clearer for beginners, while relative imports are commonly used inside packages.


## Practical Example: Real Project Structure

```text
school_project/
    students/
        __init__.py
        profile.py
        marks.py
    app.py
```

### `profile.py`

```python
def student_profile(name, class_name):
    return {
        "name": name,
        "class": class_name
    }
```

### `marks.py`

```python
def total_marks(*marks):
    return sum(marks)
```

### `app.py`

```python
from students.profile import student_profile
from students.marks import total_marks

student = student_profile("Ayesha", "10-A")
print(student)
print(total_marks(80, 90, 95))
```

This is a realistic example of how a project uses modules and packages together.

## Important Points

- A module is a single Python file.
- A package is a folder with modules.
- Use `import module_name` to access the module.
- Use `from module import function` to access specific things.
- Use `__init__.py` to make a folder into a package.
- Packages help organize larger Python projects.

## Summary

Python modules are a clean way to break code into smaller reusable files. Packages let you group modules into a structured project. This makes programs easier to maintain and scale.
