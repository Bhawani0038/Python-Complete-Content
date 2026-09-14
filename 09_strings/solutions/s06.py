text = input("Enter a sentence: ")
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for character in text.lower():
    if character in vowels:
        vowel_count += 1
    elif character.isalpha():
        consonant_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
