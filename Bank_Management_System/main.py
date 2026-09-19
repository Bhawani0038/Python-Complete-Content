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

def find_user_by_email(email):
    db =load_data()
    for user in db:
        if user["email"] == email:
            return user
        
def check_balance(user):
    return user["balance"]

def deposit_money(user):
    amount = float(input("amount to deposit:"))
    balance = check_balance(user)
    if amount <= 0:
        print("invalid amount to depoasit")

    else:
        new_balance = balance + amount
        user["balance"] = new_balance

        db = load_data()

        for index, db_user in enumerate(db):
            if db_user["email"] == user["email"]:
                db_user["balance"] = new_balance
                db[index] = db_user
    
        with open(r"Bank_Management_System\database.json", "w") as f:
            json.dump(db, f)

        print(f"{amount} deposited succefully. new balance =  {new_balance}")

def withdraw_money(user):
    amount = float(input("amount to withdraw:"))
    balance = check_balance(user)
    if amount <= 0:
        print("invalid amount to depoasit")

    elif amount > balance:
        print("insufficient balance")

    else:
        new_balance = balance - amount
        user["balance"] = new_balance

        db = load_data()

        for index, db_user in enumerate(db):
            if db_user["email"] == user["email"]:
                db_user["balance"] = new_balance
                db[index] = db_user
    
        with open(r"Bank_Management_System\database.json", "w") as f:
            json.dump(db, f)

        print(f"{amount} withdrawn succefully. new balance =  {new_balance}")

def change_password(user):
    print("change password")
      
def user_access_panel(user):
    while True:
        choice = input("""
        1 : Chcek Balance
        2 : Deposit
        3 : Withdraw
        4 : Change Password
        5 : Exit
        """)

        if choice == "1":
            print("user balance = ", check_balance(user))

        elif choice == "2":
            deposit_money(user)

        elif choice == "3":
            withdraw_money(user)

        elif choice == "4":
            change_password(user)

        elif choice == "5":
            exit()

        else:
            print("invalid choice try again....")

def login():
    login_time_email = input("email:")
    login_time_password = input("password:")

    if not email_exists(login_time_email):
        print("no such account exists . retry with different email....")

    else:
        user = find_user_by_email(login_time_email)

        if user["password"] == login_time_password:
            user_access_panel(user)

        else:
            print("password is incorrect...")
    
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