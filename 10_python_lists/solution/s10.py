first = [1, 2]
first.append([3, 4])

second = [1, 2]
second.extend([3, 4])

print("append:", first)
print("extend:", second)
print("append adds the whole list as one item.")
print("extend adds each item separately.")
