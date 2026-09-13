full_name = input("Enter your full name: ")
clean_name = full_name.strip().lower()
username = clean_name.replace(" ", ".")

print(f"Your username is: {username}")
