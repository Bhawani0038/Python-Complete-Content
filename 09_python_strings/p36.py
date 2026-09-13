text = "Python programming"
vowel_count = 0

for character in text.lower():
	if character in "aeiou":
		vowel_count += 1

print(vowel_count)
