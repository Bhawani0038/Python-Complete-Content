users = {"admin": "admin123", "student": "python123"}
username = input("Enter username: ")
password = input("Enter password: ")
if username in users and users[username] == password:
    print("Login successful")
else:
    print("Invalid username or password")
