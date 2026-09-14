word = input("Enter a non-empty word: ").strip()

if word:
    print(f"First character: {word[0]}")
    print(f"Last character: {word[-1]}")
else:
    print("Please enter at least one character.")
