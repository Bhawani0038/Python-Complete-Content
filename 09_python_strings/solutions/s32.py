registration = input("Enter vehicle registration: ")
registration = "".join(registration.split()).upper()
valid = (
    len(registration) == 10
    and registration[:2].isalpha()
    and registration[2:4].isdigit()
    and registration[4:6].isalpha()
    and registration[6:].isdigit()
)
print("Valid" if valid else "Invalid")
