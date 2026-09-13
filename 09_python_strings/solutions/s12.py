full_name = input("Enter your full name: ").strip()
initials = "".join(word[0].upper() for word in full_name.split())
print(f"Initials: {initials}")
