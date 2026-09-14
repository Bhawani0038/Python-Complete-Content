ifsc = input("Enter IFSC code: ").strip().upper()
valid = (
    len(ifsc) == 11
    and ifsc[:4].isalpha()
    and ifsc[4] == "0"
    and ifsc[5:].isalnum()
)
print("Valid" if valid else "Invalid")
