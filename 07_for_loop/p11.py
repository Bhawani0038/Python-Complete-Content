student = {"name": "Mina", "age": 20, "course": "Python"}

print(student.items())
# for key, value in student.items():
# 	print(f"{key}: {value}")

for name, age in student.items():
    print(name, age)