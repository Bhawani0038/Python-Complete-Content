# 16. User Access Control

def has_access(user_role):
    allowed_roles = ["admin", "manager", "editor"]
    return user_role in allowed_roles


print(has_access("admin"))
print(has_access("guest"))
