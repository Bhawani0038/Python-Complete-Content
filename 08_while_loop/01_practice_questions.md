## 1. What is the output of the following code?
```
i = 1
while True:
    if i % 3 == 0:
        break
    print(i)
    i += 1
```

Options:
- a) 1 2
- b) 1 2 3
- c) Error
- d) None of the mentioned

Correct Answer: a) 1 2

### Explanation:
It prints it as long as i % 3 != 0. When i reaches 3, the loop breaks before printing it.

## 2. What is the output of the following code?
```
i = 2
while True:
    if i % 3 == 0:
        break
    print(i)
    i += 2
```

Options:
- a) 2 4
- b) 2 4 6 8 10 …
- c) 2 3
- d) 1 2 3 4 5 6

Correct Answer: a) 2 4

### Explanation:
Loop begins at i = 2, prints 2 and then 4.
Next i = 6, and 6 % 3 == 0, so the loop breaks.
Only 2 and 4 are printed.


## 3. What is the output of the following code?
```
i = 1
while False:
    if i % 2 == 0:
        break
    print(i)
    i += 2
```

Options:
- a) 1
- b) 1 3 5 7 …
- c) 1 2 3 4 …
- d) No Output
- Correct Answer: No Output


## 4. What is the output of the following code?
```
True = False
while True:
    print(True)
    break
```

Options:
- a) True
- b) False
- c) None
- d) Error

Correct Answer: d) Error

### Explanation:
You cannot assign a value to True (or False) in Python because they are reserved keywords. Doing so causes a SyntaxError.


## 5. What is the output of the following code?
```
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)
```

Options:
- a) 0 1 2 3 0
- b) 0 1 2 0
- c) 0 1 2
- d) None of the mentioned

Correct Answer: b) 0 1 2 0

### Explanation:
The loop runs while i < 3 → prints 0, 1, 2.
Then the else block runs because the loop finished normally (not via break).

## 6. What is the output of the following code?
```
x = "abcdef"
while i in x:
    print(i, end=" ")
```

Options:
- a) a b c d e f
- b) abcdef
- c) 0 1 2
- d) i i i i i i … (infinite)
- e) Error
- f) None of the mentioned

Correct Answer: e) Error

### Explanation:
i is undefined before being used in while i in x, which leads to a NameError.

## 7. What is the output of the following code?
```
x = "abcdef"
i = "i"
while i in x:
    print(i, end=" ")
```

Options:
- a) No output
- b) i
- c) i i i i i … (infinite)
- d) Error

Correct Answer: a) No output

### Explanation:
 i = "i" and "i" is not present in "abcdef".
 So while i in x is False, the loop never runs.


## 8. What is the output of the following code?
```
x = "abcdef"
i = "a"
while i in x:
    print(i, end=" ")
``` 

Options:
- a) No output
- b) a a a a a a … (infinite)
- c) abcdef
- d) Error

Correct Answer: b) a a a a a a … (infinite)

### Explanation:
Since i = "a" and "a" is in "abcdef", the loop condition is always True, and since i is never updated, it causes an infinite loop.

## 9. What is the output of the following code?
```
x = "abcdef"
i = "a"
while i in x:
    x = x[:-1]
    print(i, end=" ")
```

Options:
- a) i i i i i i
- b) a a a a a a
- c) a a a a a
- d) None of the mentioned

Correct Answer: b) a a a a a 

### Explanation:
 Initially, "a" is in x. On each iteration, the last character is removed from x using x = x[:-1].
The loop continues until 'a' is no longer in x. So, 6 iterations print 'a'.

## 10. What is the output of the following code?
```
x = "abcdef"
i = "a"
while i in x[:-1]:
    print(i, end=" ")
```

Options:
- a) a a a a a
- b) a a a a a a
- c) Infinite loop
- d) No output
# While Loop Practice Questions

## Output Questions

### 1. What is the output?

```python
number = 1

while number <= 4:
    print(number, end=" ")
    number += 1
```

- a) `0 1 2 3`
- b) `1 2 3 4`
- c) `1 2 3`
- d) Infinite loop

### 2. What is the output?

```python
number = 5

while number > 0:
    print(number, end=" ")
    number -= 2
```

- a) `5 4 3 2 1`
- b) `5 3 1`
- c) `5 3`
- d) `4 2`

### 3. What is the output?

```python
number = 1

total = 0
while number <= 3:
    total += number
    number += 1

print(total)
```

- a) `3`
- b) `5`
- c) `6`
- d) `123`

### 4. What is the output?

```python
number = 0

while number < 5:
    number += 1
    if number == 3:
        continue
    print(number, end=" ")
```

- a) `0 1 2 4`
- b) `1 2 4 5`
- c) `1 2 3 4 5`
- d) Infinite loop

### 5. What is the output?

```python
number = 1

while number <= 5:
    if number == 4:
        break
    print(number, end=" ")
    number += 1
else:
    print("Finished")
```

- a) `1 2 3 Finished`
- b) `1 2 3 4`
- c) `1 2 3`
- d) `Finished`

### 6. What happens when this code runs?

```python
number = 1

while number <= 3:
    print(number)
```

- a) It prints `1 2 3`.
- b) It prints `0 1 2`.
- c) It causes an infinite loop.
- d) It causes a syntax error.

### 7. What is the output?

```python
word = "cat"
index = 0

while index < len(word):
    print(word[index], end=" ")
    index += 1
```

- a) `c a t`
- b) `0 1 2`
- c) `cat`
- d) `c a`

### 8. What is the output?

```python
number = 1

while number <= 2:
    print(number)
    number += 1
else:
    print("Done")
```

- a) `1 2`
- b) `1 2 Done`
- c) `Done`
- d) Infinite loop

## Write Programs

### 9. Print Numbers

Write a `while` loop that prints the numbers from 1 through 10.

### 10. Print Even Numbers

Write a `while` loop that prints all even numbers from 2 through 20.

Expected output:

```text
2 4 6 8 10 12 14 16 18 20
```

### 11. Countdown

Write a program that prints a countdown from 10 to 1 and then prints `Blast off!`.

### 12. Sum of Numbers

Use a `while` loop to calculate the sum of the numbers from 1 through 100.

Expected output:

```text
5050
```

### 13. Multiplication Table

Ask the user for a number and use a `while` loop to print its multiplication table from 1 through 10.

Example for input `5`:

```text
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

### 14. Count Digits

Ask the user for a positive integer and use a `while` loop to count how many digits it contains.

Example:

```text
Input: 48291
Output: 5
```

### 15. Reverse a Number

Ask the user for a positive integer and use a `while` loop to print its digits in reverse order.

Example:

```text
Input: 1234
Output: 4321
```

### 16. Password Validation

Keep asking the user for a password until they enter `python123`. Print `Access granted` after the correct password is entered.

### 17. Guessing Game

Set `secret_number = 7`. Keep asking the user to guess the number until they guess correctly. Print whether each guess is too high or too low.

### 18. Menu Loop

Display a menu with these choices:

```text
1. Say hello
2. Say goodbye
q. Quit
```

Use `while True` and `break` to keep displaying the menu until the user enters `q`.

## Challenge Questions

### 19. FizzBuzz with `while`

Use a `while` loop to print numbers from 1 through 30. Print `Fizz` for multiples of 3, `Buzz` for multiples of 5, and `FizzBuzz` for multiples of both.

