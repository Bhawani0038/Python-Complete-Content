# Read a text file and print its contents

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
