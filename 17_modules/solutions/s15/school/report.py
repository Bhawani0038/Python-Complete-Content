def generate_report(student_data, marks):
    return {
        "student": student_data,
        "total_marks": sum(marks),
    }
