fruits = ["apple", "banana", "mango", "orange"]
fruit = input("Enter a fruit: ").strip().lower()

if fruit in fruits:
    fruits.remove(fruit)
    print(fruits)
else:
    print("Fruit not found")
