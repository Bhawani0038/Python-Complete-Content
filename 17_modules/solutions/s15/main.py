from school.student import student_info
from school.marks import total_marks
from school.report import generate_report

student = student_info("Ayesha", "10-A")
marks = [80, 90, 95]
report = generate_report(student, marks)
print(student)
print(total_marks(*marks))
print(report)
