names = ["Asha", "Bilal", "Chen"]
marks = [
    [80, 75, 90],
    [35, 42, 38],
    [92, 88, 95],
]

for name, student_marks in zip(names, marks):
    total = sum(student_marks)
    average = total / len(student_marks)
    result = "Pass" if average >= 40 else "Fail"

    print(f"Name: {name}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Result: {result}")
    print()
