sentence = input("Enter a sentence: ")
words = sentence.split()

if words:
    longest_word = max(words, key=len)
    print(f"Longest word: {longest_word}")
    print(f"Length: {len(longest_word)}")
else:
    print("No words entered.")
