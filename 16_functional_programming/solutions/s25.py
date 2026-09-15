# 25. Library Book Issue System

def issue_book(book_name, days_issued, fine_rate=5):
    fine = days_issued * fine_rate
    return {
        "book_name": book_name,
        "days_issued": days_issued,
        "fine": fine,
    }


print(issue_book("Python Basics", 10))
