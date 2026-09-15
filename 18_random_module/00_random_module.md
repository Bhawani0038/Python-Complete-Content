# Python Random Module

The `random` module in Python is used to generate random numbers and make random choices. It is very useful in games, simulations, password generation, testing, and many real-world programs.

To use it, first import the module:

```python
import random
```

## Why Use the Random Module?

The `random` module helps you create:

- random numbers
- random choices from a list
- random shuffling of data
- lottery-style programs
- game logic

For example, a dice game, a quiz selector, or a password generator all use random values.

## Generating Random Numbers

### `random()`

This returns a random floating-point number between `0.0` and `1.0`.

```python
import random

print(random.random())
print(random.random())
print(random.random())
```

Example output:

```text
0.234567890123
0.987654321456
0.112233445566
```

The values are random and will change every time the program runs.

### `randint(a, b)`

This returns a random integer between `a` and `b`, including both endpoints.

```python
import random

print(random.randint(1, 10))
```

Example output:

```text
7
```

This is very useful for dice rolls and random number games.

### `randrange(start, stop, step)`

This returns a random integer from a range.

```python
import random

print(random.randrange(1, 10))
print(random.randrange(0, 20, 2))
```

Example output:

```text
4
12
```

### `uniform(a, b)`

This returns a random floating-point number between `a` and `b`.

```python
import random

print(random.uniform(1.5, 5.5))
```

Example output:

```text
3.842331234
```

## Random Choices from a List

### `choice()`

This picks one random item from a sequence like a list.

```python
import random

fruits = ["apple", "banana", "mango", "orange"]
print(random.choice(fruits))
```

Example output:

```text
banana
```

This is used in random quiz selection, prize selection, and game reward systems.

### `choices()`

This returns multiple random elements from a list.

```python
import random

colors = ["red", "green", "blue", "yellow"]
print(random.choices(colors, k=3))
```

Example output:

```text
['green', 'blue', 'red']
```

## Shuffling a List

### `shuffle()`

This randomizes the order of items in a list.

```python
import random

cards = ["A", "K", "Q", "J"]
random.shuffle(cards)
print(cards)
```

Example output:

```text
['Q', 'A', 'J', 'K']
```

This is used in card games and randomizing questions.

## Randomizing a Sequence

### `sample()`

This picks unique random items from a list without repetition.

```python
import random

numbers = [1, 2, 3, 4, 5, 6, 7]
print(random.sample(numbers, 3))
```

Example output:

```text
[2, 5, 7]
```

This is useful when selecting winners or random teams without duplicates.

## Setting a Random Seed

The random module can be made predictable by setting a seed.

```python
import random

random.seed(10)
print(random.randint(1, 10))
print(random.randint(1, 10))
```

This produces the same random values every time the same seed is used.

Seeds are useful for debugging and testing programs.

## Practical Example 1: Dice Roll

```python
import random

roll = random.randint(1, 6)
print(f"You rolled a {roll}")
```

Example output:

```text
You rolled a 4
```

This is a classic real-world example of the random module.

## Practical Example 2: Lucky Draw

```python
import random

participants = ["Ali", "Aisha", "Zain", "Sara", "Hassan"]
winner = random.choice(participants)
print(f"Winner is: {winner}")
```

Example output:

```text
Winner is: Sara
```

## Practical Example 3: Random Quiz Question

```python
import random

questions = [
    "What is the capital of Pakistan?",
    "What is 2 + 2?",
    "Who created Python?",
    "Which language is used for web pages?"
]

question = random.choice(questions)
print(question)
```

This is a practical use because quiz apps often show questions in random order.

## Practical Example 4: Password Generator

```python
import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(10))
print(password)
```

Example output:

```text
mK7!pQ2@vL
```

This is a common real-world use of the random module.

## Practical Example 5: Random Team Selection

```python
import random

students = ["Ali", "Ayesha", "Bilal", "Maira", "Hassan", "Noor"]
random.shuffle(students)
print("Team 1:", students[:3])
print("Team 2:", students[3:])
```

This is used to divide students into teams for group activities.

## Practical Example 6: Simulating Coin Toss

```python
import random

outcomes = ["Heads", "Tails"]
print(random.choice(outcomes))
```

Example output:

```text
Heads
```

## Common Methods in the Random Module

Here are the most common methods:

- `random()` - random float between 0 and 1
- `randint(a, b)` - random int in range
- `randrange(start, stop, step)` - random value from range
- `uniform(a, b)` - random float in a range
- `choice(seq)` - choose one item
- `choices(seq, k=n)` - choose multiple items
- `shuffle(seq)` - randomize order
- `sample(seq, k)` - choose unique random items without replacement

## Difference Between `random.choice()` and `random.sample()`

```python
import random

items = ["A", "B", "C", "D", "E"]

print(random.choice(items))
print(random.sample(items, 3))
```

- `choice()` picks a single item
- `sample()` picks multiple unique items

## Best Practices

- Use `random.seed()` only when you want repeatable output
- For random unique values, prefer `sample()`
- For list order randomization, use `shuffle()`
- For user-facing randomness, `choice()` and `randint()` are simple and effective

## Summary

The `random` module helps us create unpredictable values and make programs more dynamic.

It is commonly used for:

- games
- random picks and winners
- testing
- simulations
- password generation
- shuffling data

## Practice Questions

1. Use `random.randint()` to simulate a dice roll.
2. Pick a random fruit from a list using `random.choice()`.
3. Shuffle a list of names and print the new order.
4. Use `random.sample()` to select 3 numbers from 1 to 10.
5. Generate a random password using letters, digits, and symbols.

## Example Practice Code

```python
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.sample(numbers, 3))
```

This shows a simple real-world use of randomization without duplicates.
