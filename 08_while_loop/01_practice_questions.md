## 3. What is the output of the following code?
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

## 4. What is the output of the following code?
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


## 5. What is the output of the following code?
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


## 6. What is the output of the following code?
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


## 7. What is the output of the following code?
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

## 8. What is the output of the following code?
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

## 9. What is the output of the following code?
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


## 10. What is the output of the following code?
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

## 11. What is the output of the following code?
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

## 12. What is the output of the following code?
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
Correct Answer: c) Infinite loop

### Explanation:
This will be an infinite loop because:
●	x[:-1] returns a new string ('abcde'), but doesn't change x.

●	'a' is always in 'abcde', and x is never updated.
So the loop never ends unless interrupted.

## 13. What is the output of the following code?
```
x = "abcdef"
i = "a"
while i in x:
    x = x[1:]
    print(i, end=" ")
```

Options:
- a) a a a a a a
- b) a
- c) a a a a a
- d) a a a a a a … (infinite loop)
- e) No output

Correct Answer: b) a
### Explanation:
●	First check: 'a' in "abcdef" → True → print 'a'

●	Then: x = x[1:] → becomes "bcdef"

●	Now 'a' not in x, so loop ends

Only one iteration happens

## 14. What is the output of the following code?
```
x = "abcdef"
i = "a"
while i in x[1:]:
    print(i, end=" ")
```

Options:
- a) a a a a a a
- b) a
- c) No output
- d) Error
Correct Answer: c) No output

### Explanation:
 x[1:] = "bcdef"
 Since 'a' is not in "bcdef", the loop never runs.