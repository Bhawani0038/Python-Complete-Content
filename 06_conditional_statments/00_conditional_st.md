# Python Conditional Statements

Conditional statements allow a program to make decisions based on certain conditions. They help your code run different actions depending on whether a condition is true or false.

## Why Use Conditional Statements?

Conditional statements are important because they allow programs to respond dynamically. For example:

- If a user is logged in, show the dashboard.
- If the number is even, print a message.
- If a score is greater than 50, mark it as pass.

## The `if` Statement

The `if` statement checks a condition. If the condition is `True`, the code inside the block runs.

```python
age = 18

if age >= 18:
    print("You are an adult.")
```

Output:

```python
You are an adult.
```

## The `else` Statement

The `else` statement runs when the `if` condition is `False`.

```python
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

Output:

```python
You are a minor.
```

## The `elif` Statement

The `elif` statement means "else if". It is used when you want to check multiple conditions.

```python
marks = 75

if marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: F")
```

Output:

```python
Grade: B
```

## Comparison Operators Used in Conditions

Conditional statements often use comparison operators:

- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

Example:

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

## Logical Operators in Conditions

You can combine conditions using logical operators:

- `and`
- `or`
- `not`

### Example with `and`

```python
age = 22
citizen = True

if age >= 18 and citizen:
    print("Eligible")
else:
    print("Not eligible")
```

### Example with `or`

```python
num = 3

if num == 1 or num == 3:
    print("Number is 1 or 3")
```

### Example with `not`

```python
is_raining = False

if not is_raining:
    print("It is not raining.")
```

## Nested `if` Statements

You can place one `if` inside another `if`.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can vote.")
    else:
        print("You need an ID.")
else:
    print("You are too young.")
```

Output:

```python
You can vote.
```

## Example Program: Voting Check

```python
age = 17

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
```

## Example Program: Even or Odd

```python
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

Output:

```python
Odd number
```

## Indentation in Python

Python uses indentation to show which statements belong to the `if` block.

```python
x = 5

if x > 0:
    print("Positive")
    print("This is inside the if block")
print("This is outside the if block")
```

## Summary

Conditional statements help a program make decisions. The main keywords are:

- `if`
- `else`
- `elif`

They allow code to run differently depending on conditions.

## Practice Exercise

1.	Write a program that checks if a given number is positive. If it is positive, print "Number is positive"; otherwise, print "Number is not positive."
2.	Write a program that checks if a given number is even. If it is even, print "Number is even"; otherwise, print "Number is odd.
3.	Write a program that checks if a given number is divisible by both 2 and 3. If it is, print "Number is divisible by 2 and 3"; otherwise, print "Number is not divisible by
both 2 and 3."
4.	Write a program that calculates the grade based on a student's score. If the score is above 90, print "Grade: A"; if it is between 80 and 90, print "Grade: B"; if it is between 70 and 80, print "Grade: C"; if it is between 60 and 70, print "Grade: D"; otherwise, print "Grade: F."
5.	Write a program that checks if a given character is a vowel. If it is a vowel, print "Character is a vowel"; otherwise, print "Character is not a vowel."
6.	Write a program that determines the largest of three given numbers. Print the largest number.
7.	Write a program that determines the number of days in a given month. The program should ask the user to input the month number (1 for January, 2 for February, etc.) and print the number of days in that month. If an invalid month number is entered, print "Invalid month number."
8.	Write a program that determines the cost of a movie ticket based on the age of the person. If the age is 12 or below, the ticket cost is $5; if the age is between 13 and 17 (inclusive), the ticket cost is $7; if the age is 18 or above, the ticket cost is $10.
9.	Write a program that determines the season based on a given month. If the month is December, January, or February, print "Winter"; if it is March, April, or May, print "Spring"; if it is June, July, or August, print "Summer"; if it is September, October, or November, print "Autumn."
10.	Write a program that determines the discount amount based on a customer's membership level. If the level is "Gold", apply a 20% discount; if it is "Silver", apply a 15% discount; if it is "Bronze", apply a 10% discount; otherwise, no discount is applied.
11.	Write a program that determines a person's BMI (Body Mass Index) category based on their weight and height. Ask the user to enter their weight in kilograms and their height in meters. Calculate their BMI using the formula: BMI = weight / (height * height). Display a message indicating their BMI category based on the following ranges: "Underweight" for BMI less than 18.5, "Normal weight" for BMI between 18.5 and 24.9, "Overweight" for BMI between 25 and 29.9, and "Obese" for BMI greater than or equal to 30.
12.	Write a program that assists a customer in selecting a suitable mobile phone plan. Ask the user to enter the number of minutes they anticipate using per month and display the plan options: "Basic," "Standard," and "Premium." If the user enters less than 200 minutes, recommend the "Basic" plan. For 200-500 minutes, recommend the "Standard" plan. For more than 500 minutes, recommend the "Premium" plan.
13.	Write a program that calculates the shipping cost based on the weight and destination of a package. Ask the user to enter the weight in kilograms and the destination: "Domestic" or "International." For domestic shipping, charge $2 per kilogram. For international shipping, charge $5 per kilogram. Display the total shipping cost.
14.	Write a program that determines the eligibility of a person to apply for a driver's license based on their age and the type of license. Ask the user to enter their age and the type of license they are applying for: "Car" or "Motorcycle." If the age is 18 or above for a car license or 16 or above for a motorcycle license, print "Eligible to apply for a [license type] license"; otherwise, print "Not eligible to apply for a [license type] license."
15.	Write a program that helps a user choose the right clothing for the weather. Ask the user to enter the current temperature in Celsius. Based on the temperature, provide suggestions for clothing: if the temperature is below 10 degrees, suggest "Winter jacket, hat, and gloves"; if it is between 10 and 20 degrees, suggest "Sweater or light jacket"; if it is above 20 degrees, suggest "T-shirt and shorts."
16.	Write a program that determines the discount amount for a customer's online purchase. Ask the user to enter the total order amount. If the order amount is above $100, apply a 20% discount; if it is between $50 and $100, apply a 10% discount; if it is below $50, apply a 5% discount. Print the discounted amount.
17.	Input age and monthly income:
●	If age < 21 → print "Not eligible"
●	If income < 30000 → print "Eligible for a small loan"
●	If income ≥ 30000 → print "Eligible for a regular loan"

18.	Ask for temperature in Celsius and classify it as:
●	Less than 10°C → "Cold"
●	Between 10°C and 25°C → "Moderate"
●	Greater than 25°C → "Hot"

19.	Input the total purchase amount.
●	If amount > ₹5000 → apply 20% discount
●	If amount is between ₹2000 and ₹5000 → apply 10% discount
●	Otherwise → no discount
 Print the final bill amount after applying the discount.

20.	Ask the user's age and print the ticket price:
●	Age < 5 → "Free"
●	Age between 5 and 18 → ₹100
●	Age between 19 and 60 → ₹200
●	Age > 60 → ₹150
21.	Ask the user:
●	If they have a loyalty card (yes/no)
●	Their total purchase amount Apply discount if:
○	They have a loyalty card
○	Or the purchase is over ₹200
 Print whether discount is applied.
