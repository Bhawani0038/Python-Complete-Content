# Practice Questions
## 1. What is the output of the following code?
```
x = ['ab', 'cd']
for i in x:
    i.upper()
print(x)
```
- a) ['ab', 'cd']
- b) ['AB', 'CD']
- c) [None, None]
- d) None of the mentioned
Correct Answer:
a) ['ab', 'cd']

### Explanation:
The i.upper() creates a new uppercase string but does not modify the original list x. Strings are immutable in Python. Since there is no reassignment (i = i.upper()), the original list remains unchanged.


## 2. What is the output of the following code?
```
x = ['ab', 'cd']
for i in x:
    x.append(i.upper())
print(x)
```

Options:
- a) ['AB', 'CD']
- b) ['ab', 'cd', 'AB', 'CD']
- c) ['ab', 'cd']
- d) None of the mentioned

Correct Answer: d) None of the mentioned

### Explanation:
 This results in an infinite loop or unexpected behavior because you're modifying the list (x.append()) while iterating over it. The loop keeps growing the list during iteration.
Example of actual output (if it doesn't hang):
['ab', 'cd', 'AB', 'CD']
But this is not safe or reliable — hence option d is the most correct.



## 3. What is the output of the following code?
```
x = 'abcd'
for i in x:
    print(i)
    x.upper()
```

Options:
- a) a B C D
- b) a b c d
- c) A B C D
- d) Error
- e) None of the mentioned

Correct Answer: b) a b c d

### Explanation:
●	x.upper() is called but its result is ignored because str.upper() returns a new string, it does not change x in-place.

●	So loop prints original characters: 'a', 'b', 'c', 'd'.

 
## 4. Write a program to print the following patterns:
i)
```
*
**
***
****
*****
```

ii)
```
*****
****
***
**
*
```

iii)
```
1
12
123
1234
12345
```

iv)
```
1
23
456
78910
```

v)
```
1
22
333
4444
55555
```

vi)
```
    *
   ***
  *****
 *******
*********
```

vii)
```
*******
 *****
  ***
   *
```

viii)
```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

ix)
```
a
bc
def
ghij
```


x)
```
a
bb
ccc
dddd
eeeee
```

xi)
```
*****
*****
*****
*****
*****
```

xii)
```
******
*    *
*    *
*    *
*    *
******
```

## 5. You are given a list of product prices. Write a for loop that prints "High" if the price is more than ₹300, otherwise print "Low".
prices = [120, 340, 560, 290]
```
    Expected output:
    Low
    High
    High
    Low
```

## 6. You had multiple meals today. Each meal had a certain number of calories. Write a program using a for loop to calculate and print the total calories consumed.
```
meals = [400, 600, 300, 500]
Expected Output: Total calories consumed = 1800
```

## 7. Using a for loop and range(), print all even-numbered buses in the range 101 to 120 (inclusive).
```
Expected Output: 102 104 106 108 110 112 114 116 118 120
```

## 8. Write a for loop to count how many vowels (a, e, i, o, u) are present in the given sentence.
```
sentence = "My car broke down near the railway station."
# Expected Output: Total vowels = 14
```
## 9. You are given a dictionary of fruit prices. Use a for loop to print each fruit and its price in the format: fruit -> ₹price.
```
fruit_prices = {'apple': 100, 'banana': 50, 'grapes': 60}
# Expected Output:
# apple -> ₹100
# banana -> ₹50
# grapes -> ₹60
```
 
## 10. Use a for loop to display the multiplication table of 5 up to 10.

```
Expected Output:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```
