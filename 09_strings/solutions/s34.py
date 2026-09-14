text = input("Enter a string: ")
normalized_text = text.lower()
unique_character = None

for index, character in enumerate(normalized_text):
    if normalized_text.count(character) == 1:
        unique_character = text[index]
        break

if unique_character is None:
    print("No unique character")
else:
    print(unique_character)
