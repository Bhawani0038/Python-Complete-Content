v = ord('a')
for r in range(1, 5):
    for c in range(1, r + 1):
        print(chr(v), end = "")
        v = v + 1
    print()