import json
import random

def email_exists(email):
    database = load_data()
    for user in database:
        if user["email"]  == email:
            return True
        
    return False

def account_exists(account):
    database = load_data()
    for user in database:
        if user["acc_no"]  == account:
            return True
        
    return False

def generate_account_no():
    account_no = "bob" + str(random.randint(100, 999))
    if account_exists(account_no):
        print("account alread exists")
        generate_account_no()

    else:
        return account_no

def load_data():
    with open(r"Bank_Management_System\database.json", "r") as f:
        db = json.load(f)
        return db

def create_user(user_data):
    database = load_data()
    database.append(user_data)

    with open(r"Bank_Management_System\database.json", "w") as f:
        json.dump(database, f)
    
def signup():
    user_data =     {"name" : input("name :"), 
       "email" : input("email: "), 
       "acc_no" : generate_account_no(), 
       "balance" : 0,
       "password" : input("password: ")
    }

    if not email_exists(user_data["email"]):
        create_user(user_data)
        print(f"account created succesfully. account no = {user_data["acc_no"]} and password = {user_data["password"]} with 0 balance")

    else:
        print("email already exists...")


def login():
    login_time_email = input("email:")
    login_time_password = input("password:")

    if not email_exists(login_time_email):
        print("no such account exists . retry with different email....")

    


def main():
    user_choice = input("""
        1 : Login
        2 : SignUp
        3 : Exit
        """)

    if user_choice == "1":
        login()

    elif user_choice == "2":
        signup()

    elif user_choice == "3":
        exit()

    else:
        print("invalid choice...")
    


main()