first_word = input("First word: ")
second_word = input("Second word: ")

first_clean = "".join(character.lower() for character in first_word if character.isalnum())
second_clean = "".join(character.lower() for character in second_word if character.isalnum())

if sorted(first_clean) == sorted(second_clean):
    print("Anagrams")
else:
    print("Not anagrams")
