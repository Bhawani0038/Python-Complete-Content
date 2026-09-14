words = {
    "apple": "a round fruit",
    "book": "a set of written pages",
    "cat": "a small animal",
    "dog": "a domestic animal",
    "python": "a programming language"
}
word = input("Enter a word: ")
if word in words:
    print(words[word])
else:
    print("Word not found")
