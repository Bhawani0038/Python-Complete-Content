def is_valid_username(username):
    return len(username) >= 5 and username.isalnum()
