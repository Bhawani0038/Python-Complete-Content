frequency = {}
for char in "banana":
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)
