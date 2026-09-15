# 11. Friend List Filter

def filter_friends(names, letter):
    return [name for name in names if name.startswith(letter)]


print(filter_friends(["Ali", "Ayesha", "Bilal", "Anas"], "A"))
