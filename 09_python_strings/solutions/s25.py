aadhaar = input("Enter Aadhaar number: ").replace(" ", "")
valid = len(aadhaar) == 12 and aadhaar.isdigit() and aadhaar[0] not in "01"

if valid:
    print("Valid")
    print(f"{aadhaar[:4]} {aadhaar[4:8]} {aadhaar[8:]}")
else:
    print("Invalid")
