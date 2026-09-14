email = input("Enter an email address: ").strip()

if "@" in email:
    domain = email.split("@", 1)[1]
    print(f"Domain: {domain}")
else:
    print("Invalid email address")
