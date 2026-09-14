cart = []

while True:
    print("\n1. Add product")
    print("2. Remove product")
    print("3. View cart")
    print("4. Show total")
    print("q. Quit")
    choice = input("Choose an option: ").strip().lower()

    if choice == "q":
        break
    if choice == "1":
        name = input("Product name: ").strip()
        price = float(input("Product price: "))
        cart.append([name, price])
    elif choice == "2":
        name = input("Product to remove: ").strip().lower()
        for product in cart:
            if product[0].lower() == name:
                cart.remove(product)
                print("Product removed")
                break
        else:
            print("Product not found")
    elif choice == "3":
        for name, price in cart:
            print(f"{name}: ${price:.2f}")
    elif choice == "4":
        print(f"Total: ${sum(product[1] for product in cart):.2f}")
    else:
        print("Invalid option")
