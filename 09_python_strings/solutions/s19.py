username = input("Enter a username: ").strip()
valid = (
    5 <= len(username) <= 15
    and username.replace("_", "").isalnum()
    and not username[0].isdigit()
    and " " not in username
)
print("Valid" if valid else "Invalid")
