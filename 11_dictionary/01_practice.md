# Python Dictionaries Practice Sheet

Use the concepts from `00_dictionary.md` to solve these exercises. Try to write your own code for each question without copying from any existing program.

## Part 1: Dictionary Basics

### 1. Create a Student Dictionary

Create a dictionary for a student with the following keys:

- `name`
- `age`
- `course`

Print the whole dictionary.

### 2. Access Values by Key

Create a dictionary:

```python
student = {"name": "Aisha", "age": 20, "city": "Karachi"}
```

Print:

- the value of `name`
- the value of `city`

### 3. Missing Key Handling

Create a dictionary with 3 keys and print the value of a key that exists. Then try to access a key that does not exist and print a safe message using `get()`.

### 4. Dictionary Length

Create a dictionary with 5 key-value pairs and print the number of items in it using `len()`.

### 5. Data Type Check

Create a dictionary storing these values:

- name (string)
- age (integer)
- is_student (boolean)
- marks (float)

Print each value and its data type.

## Part 2: Adding and Updating Data

### 6. Add New Information

Start with:

```python
student = {"name": "Ali"}
```

Add:

- `age`: 21
- `city`: "Lahore"

Print the final dictionary.

### 7. Update Existing Value

Create a dictionary:

```python
book = {"title": "Python", "pages": 250}
```

Update the page count to 300 and print the dictionary.

### 8. Change Multiple Values

Create a dictionary with keys like `name`, `score`, and `grade`. Change at least two values and print the updated dictionary.

## Part 3: Removing Data

### 9. Remove a Key Using `pop()`

Create a dictionary with 4 items and remove one key using `pop()`. Print the removed value and the updated dictionary.

### 10. Remove a Key Using `del`

Create a dictionary and delete one item using `del`. Print the dictionary after deletion.

### 11. Clear the Dictionary

Create a dictionary and then clear it using `clear()`. Print the result.

### 12. `popitem()` Practice

Create a dictionary with at least 3 items. Use `popitem()` to remove the last inserted item and print the dictionary after removal.

## Part 4: Keys, Values, and Items

### 13. Print Keys

Create a dictionary and print all its keys.

### 14. Print Values

Create a dictionary and print all its values.

### 15. Loop Through Items

Create a dictionary and print each key and value in the format:

```text
name: Aisha
age: 20
```

### 16. Check if a Key Exists

Create a dictionary and ask the user for a key. Print whether that key exists in the dictionary.

## Part 5: Loops and Dictionaries

### 17. Count Characters in a Word

Ask the user for a word and count how many times each character appears in the word using a dictionary.

Example:

```text
Input: banana
Output: {'b': 1, 'a': 3, 'n': 2}
```

### 18. Find Frequency of Numbers

Create a list of numbers and count how many times each number appears using a dictionary.

Example:

```python
numbers = [2, 5, 2, 6, 5, 2]
```

### 19. Add Product Prices

Create a dictionary of products and their prices:

```python
products = {"apple": 50, "banana": 30, "mango": 80}
```

Print each product and price on a separate line.

### 20. Total Price

Use the dictionary below and calculate the total cost of all products.

```python
products = {"book": 250, "pen": 40, "notebook": 120}
```

### 21. Student Marks Summary

Create a dictionary of students and their marks:

```python
marks = {"Aisha": 90, "Bilal": 85, "Sara": 78}
```

Print the student name with the highest score.

### 22. Average Marks

Create a dictionary of marks and calculate the average score.

Example:

```python
scores = {"math": 90, "science": 80, "english": 85}
```

## Part 6: Nested Dictionaries

### 23. Student Records

Create a nested dictionary with 2 students, where each student has:

- `name`
- `age`
- `marks`

Print the details of one student.

### 24. Access Nested Data

Create the following dictionary:

```python
students = {
    "student1": {"name": "Aisha", "age": 20},
    "student2": {"name": "Bilal", "age": 22}
}
```

Print the age of `student2`.

### 25. Add a New Student

Given a dictionary of students, add another student with a name, age, and marks.

## Part 7: Dictionary Comprehension

### 26. Square Values

Create a dictionary where the keys are numbers from 1 to 5 and the values are their squares.

### 27. Name Lengths

Create a list of names and build a dictionary that stores each name as a key and its length as the value.

### 28. Even Numbers

Create a dictionary for numbers 1 to 10 where each key is a number and the value is `True` if the number is even, otherwise `False`.

## Part 8: Real-Life Practice

### 29. User Profile

Ask the user for their name, age, email, and city. Store them in a dictionary and print the final profile.

### 30. Shopping Cart

Create a dictionary for a shopping cart with product names and quantities.

Example:

```python
cart = {"apple": 3, "milk": 2, "bread": 1}
```

Then:

- print the total number of items
- add one more product
- update the quantity of one product
- print the final cart

### 31. Password Validation Using Dictionary

Create a dictionary of usernames and passwords.

Example:

```python
users = {
    "admin": "admin123",
    "student": "python123"
}
```

Ask the user for a username and password. Check whether the login is valid and print `Login successful` or `Invalid username or password`.

### 32. Word Meaning Dictionary

Create a dictionary of at least 5 words and their meanings. Ask the user to enter a word and print its meaning if it exists; otherwise print `Word not found`.

## Challenge Questions

### 33. Merge Two Dictionaries

Create two dictionaries and merge them into one dictionary. Print the result.

### 34. Remove Duplicate Values

Create a dictionary where some values repeat. Print the dictionary after removing duplicate values while keeping the first occurrence of each value.

#