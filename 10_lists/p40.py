from copy import deepcopy

original = [[1, 2], [3, 4]]
duplicate = deepcopy(original)
duplicate[0].append(5)

print(original)
print(duplicate)
