# 23. Password Validator

def is_valid_password(password):
    has_letter = any(ch.isalpha() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    valid_length = len(password) >= 8
    return valid_length and has_letter and has_digit


print(is_valid_password("hello123"))
