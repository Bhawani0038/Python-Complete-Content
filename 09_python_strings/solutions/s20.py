password = input("Enter a password: ")
errors = []

if len(password) < 8:
    errors.append("at least 8 characters")
if not any(character.isupper() for character in password):
    errors.append("one uppercase letter")
if not any(character.islower() for character in password):
    errors.append("one lowercase letter")
if not any(character.isdigit() for character in password):
    errors.append("one digit")
if not any(not character.isalnum() and not character.isspace() for character in password):
    errors.append("one special character")
if any(character.isspace() for character in password):
    errors.append("no spaces")

if errors:
    print("Invalid")
    print("Missing or incorrect rules:")
    for error in errors:
        print(f"- {error}")
else:
    print("Valid")
