date_text = input("Enter a date (DD-MM-YYYY): ").strip()
parts = date_text.split("-")
valid = (
    len(parts) == 3
    and len(parts[0]) == 2
    and len(parts[1]) == 2
    and len(parts[2]) == 4
    and all(part.isdigit() for part in parts)
)
print("Valid format" if valid else "Invalid format")
