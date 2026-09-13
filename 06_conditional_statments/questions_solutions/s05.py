"""Question: Check whether a given character is a vowel."""

character = "e"

# Solution 1: membership test
if character.lower() in "aeiou":
    print("Character is a vowel")
else:
    print("Character is not a vowel")



# Solution 2: explicit comparisons
is_vowel = (
    character == "a"
    or character == "e"
    or character == "i"
    or character == "o"
    or character == "u"
)
print("Character is a vowel" if is_vowel else "Character is not a vowel")