# Python Strings Practice

## Guidelines

- Read input using `input()` unless values are already provided.
- Remove unnecessary leading and trailing spaces with `strip()`.
- Decide whether validation should be case-sensitive. Normalize text with `lower()` or `upper()` when appropriate.
- Print a clear result such as `Valid` or `Invalid`.

## Part 1: String Basics

### 1. Personal Greeting

Ask the user for their name and print:

```text
Hello, Asha! Welcome to Python.
```

The name should be displayed with the first letter capitalized.

### 2. Character Count

Ask the user for a sentence and print:

- The sentence including spaces
- The sentence without leading or trailing spaces
- The number of characters after trimming

### 3. First and Last Character

Ask for a non-empty word and print its first and last character.

Example:

```text
Input: Python
First character: P
Last character: n
```

### 4. Reverse a String

Ask the user for text and print it in reverse order.

Example:

```text
Input: hello
Output: olleh
```

### 5. Palindrome Check

Ask for a word and check whether it reads the same forward and backward.

Treat uppercase and lowercase letters as equal.

Examples:

```text
madam -> Palindrome
Python -> Not a palindrome
```

### 6. Count Vowels and Consonants

Ask for a sentence and count its vowels and consonants. Ignore spaces, digits, and punctuation.

Example:

```text
Input: Python is fun!
Vowels: 3
Consonants: 9
```

### 7. Count Character Types

Ask for a string and count how many characters are:

- Uppercase letters
- Lowercase letters
- Digits
- Spaces
- Special characters

### 8. Replace a Word

Ask for a sentence, an old word, and a new word. Replace every occurrence of the old word with the new word and print the result.

### 9. Word Count

Ask for a sentence and count the number of words. Multiple spaces between words should not create empty words.

### 10. Longest Word

Ask for a sentence and print its longest word and its length.

If multiple words have the same length, print the first one.

## Part 2: String Methods and Formatting

### 11. Username Generator

Ask for a full name and create a username by:

- Removing extra spaces at the beginning and end
- Converting the name to lowercase
- Replacing spaces with dots

Example:

```text
Input:  Asha Khan
Output: asha.khan
```

### 12. Initials

Ask for a person's full name and print their initials.

Example:

```text
Input: Asha Fatima Khan
Output: AFK
```

### 13. Title Formatter

Ask for a sentence in any case and print it in title case. Also print the lowercase and uppercase versions.

### 14. Remove Duplicate Spaces

Ask for a sentence that may contain multiple spaces between words. Print the sentence with exactly one space between each word.

Example:

```text
Input: Python   is    easy
Output: Python is easy
```

### 15. Extract File Information

Ask for a filename such as `report.pdf`. Print:

- The filename without the extension
- The extension
- Whether the file is a PDF

Also handle a filename that has no extension.

### 16. Extract a Domain

Ask for an email address and print the domain after `@`.

Example:

```text
Input: asha@example.com
Output: example.com
```

### 17. Mask a String

Ask for a word and replace every character except the first and last with `*`.

Example:

```text
Input: Python
Output: P****n
```

Handle one-character and two-character words without producing an incorrect result.

### 18. Format a Bill

Given a product name, quantity, and price, print a formatted bill using an f-string.

Example:

```text
Product: Notebook
Quantity: 3
Price per item: $4.50
Total: $13.50
```

## Part 3: General Validation

For each question, print `Valid` or `Invalid` and explain the rule in your code with clear variable names.

### 19. Username Validation

Validate a username using these rules:

- Length is between 5 and 15 characters
- Contains only letters, digits, and underscores
- Does not start with a digit
- Does not contain spaces

Test values:

```text
asha_20    -> Valid
20_asha    -> Invalid
asha khan  -> Invalid
ab         -> Invalid
```

### 20. Password Validation

Validate a password using these rules:

- At least 8 characters
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character
- Contains no spaces

Print which rule failed when the password is invalid.

### 21. Confirm Password

Ask the user to enter a password twice. Print `Passwords match` only when both entries are identical; otherwise print `Passwords do not match`.

### 22. Email Validation

Create a basic email validator using string methods. Require that:

- There is exactly one `@`
- The local part before `@` is not empty
- The domain contains a dot
- There are no spaces
- The domain does not start or end with a dot

Test values:

```text
asha@example.com       -> Valid
asha@@example.com      -> Invalid
asha example.com       -> Invalid
@example.com           -> Invalid
asha@example           -> Invalid
```

This is a beginner exercise, not a complete email standard validator.

### 23. URL Validation

Create a basic URL validator. Accept URLs that:

- Start with `http://` or `https://`
- Contain a non-empty domain
- Do not contain spaces

Test values:

```text
https://example.com    -> Valid
http://python.org      -> Valid
example.com            -> Invalid
https://               -> Invalid
```

### 24. Date Format Validation

Validate a date written in the format `DD-MM-YYYY`.

For this exercise, check only that:

- The date has exactly three parts
- The day has two digits
- The month has two digits
- The year has four digits
- All parts contain digits

Example:

```text
25-12-2025 -> Valid format
25/12/2025 -> Invalid format
```

Do not worry about checking whether February has 28 or 29 days yet.

## Part 4: Indian Identity and Contact Validation

These exercises validate format only. They do not verify whether an identifier is real, active, or issued by a government authority. Use fictional values for testing.

### 25. Aadhaar Number Format

Ask the user for an Aadhaar number and validate this beginner-level format:

- Exactly 12 digits after removing spaces
- Contains digits only
- Does not begin with `0` or `1`

Accept both of these input styles:

```text
2345 6789 0123
234567890123
```

Print the number in grouped form as `XXXX XXXX XXXX` when it is valid.

Example fictional test values:

```text
2345 6789 0123 -> Valid format
1234 5678 9012 -> Invalid format
2345 6789 012  -> Invalid format
```

Note: This exercise checks formatting rules only. It does not implement Aadhaar verification or the official checksum algorithm.

### 26. Aadhaar Masking

Ask for a valid-format 12-digit Aadhaar number and display only the last four digits. Mask the first eight digits with `X`.

Example:

```text
Input: 2345 6789 0123
Output: XXXX XXXX 0123
```

Never print the complete identifier in the output.

### 27. PAN Format

Validate an Indian PAN format using these rules:

- Exactly 10 characters
- First five characters are uppercase letters
- Next four characters are digits
- Last character is an uppercase letter
- Ignore leading and trailing spaces
- Accept lowercase input by converting it to uppercase before validation

Example fictional test values:

```text
abcde1234f -> Valid format after normalization
ABCDE1234F -> Valid format
ABC1234EFG -> Invalid format
ABCDE12345 -> Invalid format
```

Print the normalized PAN only when it is valid.

### 28. PAN Category Character

For a valid-format PAN, inspect the fourth character and print its category:

- `P` for individual
- `C` for company
- `H` for Hindu Undivided Family
- `F` for firm or partnership
- `A` for association of persons
- `T` for trust
- `B` for body of individuals
- `L` for local authority
- `J` for artificial juridical person
- `G` for government

Print `Unknown category` for other letters.

### 29. Indian Phone Number

Validate an Indian mobile number using these rules:

- After removing spaces and hyphens, it has 10 digits
- It starts with a digit from 6 to 9
- It may optionally begin with `+91` or `91`

Normalize a valid number to the format `+91 XXXXX XXXXX`.

Test values:

```text
9876543210       -> Valid
+91 9876543210   -> Valid
91-9876543210    -> Valid
5123456789       -> Invalid
98765 4321       -> Invalid
```

This checks format only and does not confirm whether the number is active.

### 30. Phone Number Masking

Ask for a valid-format Indian phone number and display it with only the last four digits visible.

Example:

```text
Input: +91 9876543210
Output: +91 XXXXXX3210
```

### 31. IFSC Code Format

Validate an Indian bank IFSC code using these beginner-level rules:

- Exactly 11 characters
- First four characters are uppercase letters
- Fifth character is `0`
- Last six characters are uppercase letters or digits
- Ignore surrounding spaces and accept lowercase input by normalizing it

Example fictional test values:

```text
SBIN0001234 -> Valid format
sbin0001234 -> Valid after normalization
SB1N0001234 -> Invalid format
SBIN1001234 -> Invalid format
```

### 32. Vehicle Registration Format

Create a basic validator for a vehicle registration string such as `MH12AB1234`.

Require:

- Two uppercase letters for the state code
- Two digits for the district code
- Two uppercase letters
- Four digits

Allow optional spaces between parts after trimming the input.

This is a format exercise and does not cover every regional registration pattern.

## Part 5: Challenge Programs

### 33. Text Frequency

Ask for a sentence and a character. Count how many times the character appears, ignoring letter case.

Example:

```text
Sentence: Python Programming
Character: p
Output: 2
```

### 34. First Non-Repeating Character

Ask for a string and print the first character that appears only once. Ignore case while counting, but preserve the original character when displaying it.

Print `No unique character` when every character repeats.

### 35. Anagram Check

Ask for two words and determine whether they are anagrams. Ignore spaces, punctuation, and letter case.

Examples:

```text
listen / silent -> Anagrams
hello / world   -> Not anagrams
```
