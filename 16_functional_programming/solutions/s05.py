# 5. Login Check

def can_login(username, password):
    stored_username = "admin"
    stored_password = "1234"
    return username == stored_username and password == stored_password


print(can_login("admin", "1234"))
