# Python Lists Practice Questions

Use the concepts from `00_lists_tutorial.md` to solve these exercises. Write each solution in the matching file: `p01.py` for Question 1, `p02.py` for Question 2, and so on.

## Part 1: List Basics

### 1. Create and Print a List

Create a list containing five of your favorite foods and print the list.

### 2. List Length

Given the list below, print the number of items in the list.

```python
colors = ["red", "green", "blue", "yellow"]
```

### 3. Access List Items

Given a list of cities, print the first item, the third item, and the last item.

```python
cities = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Jaipur"]
```

### 4. List Slicing

Given the list below, print:

- The first three items
- The last three items
- Every second item
- The list in reverse order

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
```

### 5. Change an Item

Change `"banana"` to `"orange"` in the following list and print the result.

```python
fruits = ["apple", "banana", "mango"]
```

### 6. Replace a Slice

Replace the middle three items with `"X"`, `"Y"`, and `"Z"`.

```python
items = [1, 2, 3, 4, 5, 6]
```

### 7. Append Items

Start with an empty list. Ask the user for five numbers and append each number to the list. Print the final list.

### 8. Insert an Item

Insert `"Python"` at index 1 in the following list.

```python
languages = ["C", "Java", "JavaScript"]
```

### 9. Extend a List

Combine these two lists using `extend()` and print the result.

```python
first = [1, 2, 3]
second = [4, 5, 6]
```

### 10. Append versus Extend

Predict and then run the following code. Explain why the two lists are different.

```python
first = [1, 2]
first.append([3, 4])

second = [1, 2]
second.extend([3, 4])
```

## Part 2: Removing, Searching, and Sorting

### 11. Remove an Item

Remove the first occurrence of `20` from the list.

```python
numbers = [10, 20, 30, 20, 40]
```

### 12. Remove Safely

Ask the user for a fruit. Remove it from the list only if it exists. Otherwise print `Fruit not found`.

```python
fruits = ["apple", "banana", "mango", "orange"]
```

### 13. Pop Items

Use `pop()` to remove and print the last item. Then remove and print the item at index 1.

```python
items = ["A", "B", "C", "D"]
```

### 14. Delete a Range

Delete the items from index 1 through index 3 from the list.

```python
numbers = [10, 20, 30, 40, 50, 60]
```

### 15. Clear a List

Remove all items from the list using `clear()` and print the empty list.

```python
data = ["Python", 10, True, 3.5]
```

### 16. Membership Check

Ask the user for a subject and print whether it exists in the following list.

```python
subjects = ["math", "science", "english", "computer"]
```

### 17. Find an Index

Print the index of the first occurrence of `"mango"`.

```python
fruits = ["apple", "mango", "banana", "mango"]
```

### 18. Count Occurrences

Count how many times `5` appears in the list.

```python
numbers = [5, 2, 5, 8, 5, 1, 5]
```

### 19. Sort Numbers

Sort the list in ascending order and then in descending order.

```python
numbers = [45, 12, 78, 3, 29, 10]
```

### 20. Sort Names

Sort the following names alphabetically and print the sorted list.

```python
names = ["Zara", "Asha", "Chen", "Bilal", "Diya"]
```

## Part 3: Lists and Loops

### 21. Print Every Item

Use a `for` loop to print every item in this list on a separate line.

```python
animals = ["cat", "dog", "rabbit", "parrot"]
```

### 22. Numbered List

Use `enumerate()` to print each item with a number beginning at 1.

```python
tasks = ["study", "exercise", "read", "sleep"]
```

Expected format:

```text
1. study
2. exercise
```

### 23. Sum of List Items

Calculate and print the total of all numbers in the list without using a manually written total.

```python
prices = [120, 250, 75, 300]
```

### 24. Average Score

Calculate the average score of the students.

```python
scores = [72, 85, 91, 68, 94]
```

### 25. Highest and Lowest

Print the highest and lowest temperature from the list.

```python
temperatures = [32, 28, 35, 31, 29, 36]
```

### 26. Count Even and Odd Numbers

Count how many numbers are even and how many are odd.

```python
numbers = [12, 7, 5, 18, 20, 9, 14, 3]
```

### 27. Create a New List

Create a new list containing only the numbers greater than 50.

```python
numbers = [25, 60, 42, 89, 51, 10, 73]
```

### 28. Remove Duplicates

Create a new list containing each value only once while preserving the original order.

```python
numbers = [3, 5, 3, 2, 5, 7, 2, 8]
```

### 29. Combine Two Lists

Combine the two lists and sort the result.

```python
class_a = ["Asha", "Bilal", "Chen"]
class_b = ["Diya", "Evan", "Farah"]
```

### 30. Common Items

Find and print the items that appear in both lists, without duplicates.

```python
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
```

## Part 4: List Comprehensions and Copies

### 31. Squares with a Comprehension

Create a list containing the squares of numbers from 1 through 10 using a list comprehension.

### 32. Even Numbers with a Comprehension

Create a list of even numbers from 1 through 50 using a list comprehension.

### 33. Transform Strings

Create a new list containing the uppercase version of every name.

```python
names = ["asha", "bilal", "chen", "diya"]
```

### 34. Filter Words

Create a list containing only words with more than five characters.

```python
words = ["Python", "is", "powerful", "and", "easy", "useful"]
```

### 35. Conditional Values

Create a list containing `"Pass"` for scores of 40 or more and `"Fail"` for lower scores.

```python
scores = [35, 62, 48, 29, 90, 40]
```

### 36. Independent Copy

Create a copy of the list, add `4` to the copy, and show that the original list is unchanged.

```python
original = [1, 2, 3]
```

### 37. Predict Aliasing

Predict the output, run the code, and explain why changing `second` also changes `first`.

```python
first = [10, 20]
second = first
second.append(30)
```

### 38. Join List Items

Join the list into one sentence with a single space between words.

```python
words = ["Lists", "are", "useful", "in", "Python"]
```

## Part 5: Nested Lists and Projects

### 39. Matrix Values

Given the matrix below, print the value at row 2, column 3, and print every value using nested loops.

```python
matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]
```

### 40. Student Marks Project

Create a program that stores student names and their marks in lists. For each student, print:

- Their name
- Their total marks
- Their average marks
- `Pass` if the average is at least 40, otherwise `Fail`

Use these sample lists:

```python
names = ["Asha", "Bilal", "Chen"]
marks = [
	[80, 75, 90],
	[35, 42, 38],
	[92, 88, 95],
]
```

## Challenge Ideas

After completing the 40 questions, try building these projects:

- A shopping cart that adds, removes, and totals products
- A contact list that searches for names and phone numbers
- A to-do list with add, complete, and delete operations

