subjects = ["math", "science", "english", "computer"]
subject = input("Enter a subject: ").strip().lower()

if subject in subjects:
    print("Subject found")
else:
    print("Subject not found")
