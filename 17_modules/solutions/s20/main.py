from bank_app.users.login import login
from bank_app.users.profile import user_profile
from bank_app.accounts.balance import check_balance

print(login("admin", "1234"))
print(user_profile("Ali", "123456"))
print(check_balance(5000))
