# 27. Employee Salary Function

def net_salary(gross_salary, tax_percent=10):
    tax_amount = gross_salary * (tax_percent / 100)
    return gross_salary - tax_amount


print(net_salary(50000))
