# 12. Build a Profile

def create_profile(name, age, city, hobby="reading"):
    return {
        "name": name,
        "age": age,
        "city": city,
        "hobby": hobby,
    }


print(create_profile("Nadia", 21, "Karachi"))
