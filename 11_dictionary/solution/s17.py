word = input("Enter a word: ")
count = {}
for ch in word:
    count[ch] = count.get(ch, 0) + 1
print(count)
