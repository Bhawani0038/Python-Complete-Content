while True:
    print("1. Say hello")
    print("2. Say goodbye")
    print("q. Quit")
    choice = input("Choose an option: ").strip().lower()

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
    elif choice == "q":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
