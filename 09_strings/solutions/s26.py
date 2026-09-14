aadhaar = input("Enter Aadhaar number: ").replace(" ", "")
valid = len(aadhaar) == 12 and aadhaar.isdigit() and aadhaar[0] not in "01"

if valid:
    print(f"XXXX XXXX {aadhaar[-4:]}")
else:
    print("Invalid Aadhaar format")
