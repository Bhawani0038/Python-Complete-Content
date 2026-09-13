v = ord('a')
for r in range(1, 6):
    for c in range(1, r + 1):
        print(chr(v), end = "")
    v = v + 1
    print()