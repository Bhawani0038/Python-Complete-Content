contacts = []

while True:
    print("\n1. Add contact")
    print("2. Search contacts")
    print("3. View contacts")
    print("q. Quit")
    choice = input("Choose an option: ").strip().lower()

    if choice == "q":
        break
    if choice == "1":
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        contacts.append([name, phone])
    elif choice == "2":
        search = input("Search name: ").strip().lower()
        matches = [contact for contact in contacts if search in contact[0].lower()]
        if matches:
            for name, phone in matches:
                print(f"{name}: {phone}")
        else:
            print("No contacts found")
    elif choice == "3":
        for name, phone in contacts:
            print(f"{name}: {phone}")
    else:
        print("Invalid option")
