# Practice Questions: Modules and Packages

These exercises will help you understand how modules and packages work in real Python projects.

## Basic Module Questions

### 1. Create a module
Create a file named `math_tools.py` with functions:

- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`

Then import this module in another Python file and print the results.

---

### 2. Import by function
Create a module named `greetings.py` with a function `welcome(name)`.

Then write code using:

```python
from greetings import welcome
```

and call the function with your name.

---

### 3. Alias import
Create a module named `string_tools.py` with a function `uppercase(text)`.

Use an alias while importing:

```python
import string_tools as st
```

Then call the function using the alias.

---

### 4. Module variable access
Create a module named `config.py` containing:

```python
app_name = "Student Portal"
version = 1.0
```

Write a program that prints both values by importing the module.

---

### 5. `__name__` usage
Create a file `demo.py` with a function `show_message()` and add:

```python
if __name__ == "__main__":
    show_message()
```

Explain what happens when the file is imported versus when it is run directly.

---

## Import Style Questions

### 6. Different ways to import
Create a module named `operations.py` with the functions `sum_values()` and `multiply_values()`.

Practice all of these imports:

```python
import operations
from operations import sum_values
from operations import *
```

Then call the functions using each method.

---

### 7. Import with alias
Create a module named `user_tools.py` with a function `display_user(name, city)`.

Import it using:

```python
import user_tools as ut
```

and call the function.

---

### 8. Module from built-in library
Use the built-in `math` module to:

- find the square root of 49
- calculate `pow(2, 5)`
- print the value of `pi`

---

## Package Questions

### 9. Create a package
Create a package named `shop` with these files:

- `shop/__init__.py`
- `shop/products.py`
- `shop/billing.py`

In `products.py`, create a function `product_list()` that returns a list of product names.

In `billing.py`, create a function `total_price(prices)` that returns the sum of the list.

Then import them from another file and print the results.

---

### 10. Package import using absolute path
Create a package called `student_app` with:

- `student_app/__init__.py`
- `student_app/profile.py`
- `student_app/grades.py`

In `profile.py`, write a function `student_profile(name, grade)`.

In `grades.py`, write a function `average_marks(marks)`.

Import them as:

```python
from student_app.profile import student_profile
from student_app.grades import average_marks
```

and use them in a program.

---

### 11. Relative import inside package
Create a package `library` with:

- `library/__init__.py`
- `library/books.py`
- `library/utility.py`

In `books.py` write a function `book_info(title)`.

In `utility.py`, use a relative import to access the function from the same package and print the result.

---

### 12. Nested package
Create the following structure:

```text
project/
    myapp/
        __init__.py
        helpers/
            __init__.py
            strings.py
```

In `strings.py`, write a function `uppercase_text(text)`.

Then import and use it from another file using:

```python
from myapp.helpers.strings import uppercase_text
```

---

## Practical Real-World Questions

### 13. Create a module for user data
Create a module `user_data.py` with a function `create_user(name, email, role)` that returns a dictionary with user information.

Then import it and print a user record.

---

### 14. Create a billing module
Create a module `billing.py` with a function `final_bill(amount, tax_rate)` that calculates the total bill.

Then import it into another file and print the final bill for a customer.

---

### 15. Create a package for a school app
Create a package `school` with modules:

- `student.py`
- `marks.py`
- `report.py`

Functions:

- `student.py`: `student_info(name, class_name)`
- `marks.py`: `total_marks(*marks)`
- `report.py`: `generate_report(student_data, marks)`

Use the package in a small program that prints a student report.

---

### 16. Create a package for an online store
Create a package `store` with:

- `store/__init__.py`
- `store/products.py`
- `store/cart.py`

In `products.py`, store product names and prices in a list or dictionary.

In `cart.py`, write a function `cart_total(items)` that calculates total cost.

Then import and use them in another file.

---

## Challenge Questions

### 17. Create a calculator package
Create a package `calculator_pkg` with modules:

- `basic.py`
- `advanced.py`

`basic.py` should contain `add()` and `subtract()`.

`advanced.py` should contain `power()` and `square_root()`.

Then import and use both modules in a main program.

---

### 18. Build a small project structure
Create a project with the following structure:

```text
project/
    app.py
    utilities/
        __init__.py
        formatters.py
        validators.py
```

`formatters.py` contains a function to format a customer name.

`validators.py` contains a function to check whether a username is valid.

Then import both modules in `app.py` and use them.

---

### 19. Explain import behavior
Write a short note explaining the difference between:

```python
import module_name
from module_name import function_name
from module_name import *
```

Also explain when each one is useful.

---

### 20. Package design question
Imagine you are creating a project for a bank app. Explain how you would organize it using modules and packages.

Suggested structure:

```text
bank_app/
    __init__.py
    users/
        __init__.py
        login.py
        profile.py
    accounts/
        __init__.py
        balance.py
        transactions.py
```

Explain what each module would contain.

---

## Tips for Solving These Questions

- Start by creating a small module and testing it in isolation.
- Use `import` when you want the whole module.
- Use `from module import function` when you only need one part.
- Use packages to organize related modules in larger projects.
- Remember that `__init__.py` makes a folder a package.

