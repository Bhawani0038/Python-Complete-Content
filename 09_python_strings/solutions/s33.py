sentence = input("Sentence: ")
character = input("Character: ")

if len(character) != 1:
    print("Enter exactly one character.")
else:
    print(f"Output: {sentence.lower().count(character.lower())}")
