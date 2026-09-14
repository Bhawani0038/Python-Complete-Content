word = input("Enter a word: ").strip().lower()

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
