word = input("Enter a word: ")

if len(word) <= 2:
    masked_word = word[0] + "*" * max(0, len(word) - 1) if word else ""
else:
    masked_word = word[0] + "*" * (len(word) - 2) + word[-1]

print(masked_word)
