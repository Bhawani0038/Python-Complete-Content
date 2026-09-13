sentence = "My car broke down near the railway station."

sentence = sentence.lower()

vowels = 0
for char in sentence:
    if char in "aeiou":
        vowels += 1

print("vowels=", vowels)