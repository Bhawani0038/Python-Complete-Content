# Python Strings

A string is a sequence of characters used to represent text. Strings can contain letters, numbers, spaces, punctuation, and special characters.

```python
name = "Asha"
message = 'Welcome to Python'
```

## Creating Strings

Python supports single quotes and double quotes. Choose the type that makes the text easiest to read.

```python
single_quoted = 'Python'
double_quoted = "Python"

print(single_quoted)
print(double_quoted)
```

Use different quote types when the string itself contains a quote:

```python
sentence = "It's a beautiful day."
title = 'The book is called "Python Basics".'
```

You can also escape a quote with a backslash:

```python
sentence = 'It\'s a beautiful day.'
title = "The book is called \"Python Basics\"."
```

## Multiline Strings

Triple quotes create a string that can span several lines.

```python
message = """Hello!
Welcome to Python.
Have a great day."""

print(message)
```

## Special Characters

An escape sequence begins with a backslash and represents a special character.

| Escape sequence | Meaning |
| --- | --- |
| `\n` | New line |
| `\t` | Tab space |
| `\'` | Single quote |
| `\"` | Double quote |
| `\\` | Backslash |

```python
print("Name:\tAsha")
print("Line one\nLine two")
```

Use a raw string when backslashes should be treated as ordinary characters:

```python
path = r"C:\Users\Acer\Desktop\Python"
print(path)
```

## Length and Indexing

Use `len()` to count characters. Spaces and punctuation are included.

```python
word = "Python"
print(len(word))
```

Python uses zero-based indexing, so the first character has index `0`.

```python
word = "Python"

print(word[0])
print(word[1])
print(word[-1])
print(word[-2])
```

Output:

```text
P
y
n
o
```

An index outside the string raises an `IndexError`.

## Slicing

Slicing extracts part of a string. The ending index is not included.

```python
word = "Python"

print(word[0:2])
print(word[2:6])
print(word[:4])
print(word[2:])
```

The general syntax is `text[start:stop:step]`.

```python
text = "abcdef"

print(text[::2])
print(text[1::2])
print(text[::-1])
```

Output:

```text
ace
bdf
fedcba
```

`text[::-1]` is a common way to reverse a string.

## Strings Are Immutable

Strings are immutable. This means that individual characters cannot be changed after the string is created.

```python
word = "cat"
# word[0] = "b"  # TypeError
```

Create a new string instead:

```python
word = "cat"
word = "b" + word[1:]
print(word)
```

String methods also return new strings. They do not change the original string.

```python
word = "python"
upper_word = word.upper()

print(word)
print(upper_word)
```

## Combining Strings

The `+` operator joins strings, and `*` repeats a string.

```python
first_name = "Asha"
last_name = "Khan"
full_name = first_name + " " + last_name

print(full_name)
print("Hi! " * 3)
```

Both operands of `+` must be strings. Convert other types before joining them:

```python
age = 20
print("Age: " + str(age))
```

## Membership and Comparison

Use `in` and `not in` to search for text. Membership checks are case-sensitive.

```python
email = "asha@example.com"

print("@" in email)
print("gmail" not in email)
print("python" in "Python")
```

Strings can be compared with `==`, `!=`, `<`, `>`, `<=`, and `>=`.

```python
print("cat" == "cat")
print("cat" != "dog")
print("apple" < "banana")
```

For a case-insensitive comparison, normalize both strings first:

```python
answer = "YES"

if answer.lower() == "yes":
	print("Accepted")
```

## Changing Letter Case

These methods return new strings:

```python
text = "Python Programming"

print(text.lower())
print(text.upper())
print(text.title())
print(text.capitalize())
print(text.swapcase())
```

- `lower()` converts letters to lowercase.
- `upper()` converts letters to uppercase.
- `title()` capitalizes each word.
- `capitalize()` capitalizes only the first character.
- `swapcase()` changes uppercase letters to lowercase and vice versa.

## Removing Whitespace

Use `strip()` to remove whitespace from both ends, `lstrip()` from the left, and `rstrip()` from the right.

```python
text = "   Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())
```

These methods do not remove spaces between words.

## Replacing Text

Use `replace(old, new)` to create a string with matching text replaced.

```python
sentence = "I like Java"
updated_sentence = sentence.replace("Java", "Python")

print(updated_sentence)
```

Limit the number of replacements with a third argument:

```python
text = "one one one"
print(text.replace("one", "two", 2))
```

## Splitting and Joining

`split()` divides a string into a list. By default, it splits at whitespace.

```python
sentence = "Python is easy to learn"
words = sentence.split()
print(words)
```

Pass a separator to split at a particular character:

```python
colors = "red,green,blue"
print(colors.split(","))
```

`join()` combines a sequence of strings with a separator.

```python
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)
```

The separator is placed between items, not after the final item.

## Searching Within a String

`find()` returns the index of the first match. It returns `-1` when the text is not found.

```python
text = "banana"

print(text.find("an"))
print(text.find("x"))
```

`index()` is similar, but raises a `ValueError` when the text is not found.

```python
text = "banana"
print(text.index("na"))
```

Use `count()` to count non-overlapping occurrences:

```python
text = "banana"
print(text.count("a"))
print(text.count("na"))
```

Use `startswith()` and `endswith()` for prefix and suffix checks:

```python
filename = "report.pdf"

print(filename.startswith("report"))
print(filename.endswith(".pdf"))
```

## Useful Validation Methods

Validation methods return `True` or `False`.

```python
print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("   ".isspace())
print("python".islower())
print("PYTHON".isupper())
```

Common methods include:

- `isalpha()` checks for letters only.
- `isdigit()` checks for digits only.
- `isalnum()` checks for letters and digits only.
- `isspace()` checks for whitespace only.
- `islower()` checks whether all cased letters are lowercase.
- `isupper()` checks whether all cased letters are uppercase.

## Formatting with f-Strings

An f-string lets you place variables and expressions inside a string. Add `f` before the opening quote and put expressions inside `{}`.

```python
name = "Asha"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

Expressions can be placed inside the braces:

```python
price = 49.5
quantity = 2

print(f"Total: {price * quantity}")
```

Format numbers with a format specifier:

```python
price = 12.5
print(f"Price: ${price:.2f}")
```

Output:

```text
Price: $12.50
```

Use a comma for thousands separators:

```python
population = 1500000
print(f"Population: {population:,}")
```

## Older Formatting Styles

The `.format()` method is another way to insert values.

```python
name = "Asha"
score = 95

print("{} scored {} marks.".format(name, score))
```

The `%` operator is an older style. It is still found in existing code, but f-strings are usually easier to read.

```python
name = "Asha"
print("Hello, %s!" % name)
```

## Iterating Through a String

A string is iterable, so a `for` loop can visit each character.

```python
word = "Python"

for character in word:
	print(character)
```

Count vowels with a loop:

```python
text = "Python programming"
vowel_count = 0

for character in text.lower():
	if character in "aeiou":
		vowel_count += 1

print(vowel_count)
```

## Converting Values to Strings

Use `str()` to convert a value to a string.

```python
number = 42
number_text = str(number)

print(number_text)
print(type(number_text))
```

To convert numeric text into a number, use `int()` or `float()` when the text has a valid numeric format.

```python
age_text = "20"
age = int(age_text)

print(age + 1)
```

Invalid text causes a `ValueError`:

```python
# int("twenty")  # ValueError
```

## Practical Example

This program cleans a name and creates a username.

```python
full_name = input("Enter your full name: ")
clean_name = full_name.strip().lower()
username = clean_name.replace(" ", ".")

print(f"Your username is: {username}")
```

For input `Asha Khan`, the output is:

```text
Your username is: asha.khan
```

## Common Mistakes

### Forgetting That Indexes Start at Zero

```python
word = "Python"
print(word[0])  # P, not y
```

### Trying to Modify a Character

Strings are immutable. Build a new string or use a string method instead.

```python
word = "cat"
word = "b" + word[1:]
```

### Mixing Strings and Numbers

Convert the number before concatenating:

```python
items = 3
print("Items: " + str(items))
print(f"Items: {items}")
```

### Forgetting That Methods Return New Strings

```python
text = "python"
text.upper()
print(text)  # python
```

Save the returned value if you need it:

```python
text = text.upper()
print(text)  # PYTHON
```

## Summary

- Strings store text and can use single, double, or triple quotes.
- Strings use zero-based indexes and support slicing.
- Strings are immutable, so string operations return new strings.
- Use `+` to concatenate and `*` to repeat strings.
- Use `in`, `find()`, `count()`, `startswith()`, and `endswith()` to search.
- Use `strip()`, `replace()`, `split()`, and `join()` to clean and reorganize text.
- Use case-conversion and validation methods to inspect or normalize text.
- Use f-strings to format variables and expressions clearly.
- Use `str()`, `int()`, and `float()` to convert between text and numbers.
