a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(id(a))
print(id(b))
print(id(c))

print(a is b)
print(a is c)
print(a is not c)
