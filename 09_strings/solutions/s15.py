filename = input("Enter a filename: ").strip()

if "." in filename and not filename.startswith("."):
    name, extension = filename.rsplit(".", 1)
    print(f"Name: {name}")
    print(f"Extension: {extension}")
    print(f"Is PDF: {extension.lower() == 'pdf'}")
else:
    print(f"Name: {filename}")
    print("Extension: None")
    print("Is PDF: False")
