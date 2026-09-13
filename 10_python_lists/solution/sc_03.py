tasks = []

while True:
    print("\n1. Add task")
    print("2. Complete task")
    print("3. Delete task")
    print("4. View tasks")
    print("q. Quit")
    choice = input("Choose an option: ").strip().lower()

    if choice == "q":
        break
    if choice == "1":
        tasks.append({"text": input("Task: ").strip(), "done": False})
    elif choice == "2":
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task['text']}")
        index = int(input("Task number to complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
    elif choice == "3":
        index = int(input("Task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
    elif choice == "4":
        for number, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{number}. {task['text']} - {status}")
    else:
        print("Invalid option")
