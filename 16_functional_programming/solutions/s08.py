# 8. User Registration

def register_user(name, email, role="customer"):
    return {
        "name": name,
        "email": email,
        "role": role,
    }


user = register_user("Mina", "mina@example.com")
print(user)
