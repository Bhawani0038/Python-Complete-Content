
import random
secret_number = random.randint(1, 100)
attempts = 0
guess = int(input("Guess the number: "))

while guess != secret_number:
	attempts += 1

	if guess < secret_number:
		print("Too low")
	else:
		print("Too high")

	guess = int(input("Try again: "))

attempts += 1
print(f"Correct! You guessed it in {attempts} attempts.")
