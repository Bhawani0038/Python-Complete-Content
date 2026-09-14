phone = input("Enter an Indian phone number: ").strip()
phone = phone.replace(" ", "").replace("-", "")

if phone.startswith("+91"):
    local_number = phone[3:]
elif phone.startswith("91") and len(phone) == 12:
    local_number = phone[2:]
else:
    local_number = phone

valid = len(local_number) == 10 and local_number.isdigit() and local_number[0] in "6789"

if valid:
    print(f"+91 XXXXXX{local_number[-4:]}")
else:
    print("Invalid phone format")
