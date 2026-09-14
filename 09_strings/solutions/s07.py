text = input("Enter a string: ")
uppercase_count = 0
lowercase_count = 0
digit_count = 0
space_count = 0
special_count = 0

for character in text:
    if character.isupper():
        uppercase_count += 1
    elif character.islower():
        lowercase_count += 1
    elif character.isdigit():
        digit_count += 1
    elif character.isspace():
        space_count += 1
    else:
        special_count += 1

print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Spaces: {space_count}")
print(f"Special characters: {special_count}")
