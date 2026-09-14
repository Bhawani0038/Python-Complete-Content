email = input("Enter an email address: ").strip()
parts = email.split("@")

valid = (
    len(parts) == 2
    and bool(parts[0])
    and bool(parts[1])
    and " " not in email
    and "." in parts[1]
    and not parts[1].startswith(".")
    and not parts[1].endswith(".")
)
print("Valid" if valid else "Invalid")
