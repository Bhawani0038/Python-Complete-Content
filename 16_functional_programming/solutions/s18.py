# 18. Flexible User Details

def display_user_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


display_user_details(name="Ali", city="Lahore", age=20)
