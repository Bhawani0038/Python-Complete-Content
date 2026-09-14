pan = input("Enter PAN: ").strip().upper()
valid = (
    len(pan) == 10
    and pan[:5].isalpha()
    and pan[5:9].isdigit()
    and pan[9].isalpha()
)

if valid:
    print("Valid")
    print(f"Normalized PAN: {pan}")
else:
    print("Invalid")
