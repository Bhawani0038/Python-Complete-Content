# 20. Real App Function Challenge

def create_customer_record(name, email, **extra_info):
    record = {
        "name": name,
        "email": email,
    }
    record.update(extra_info)
    return record


print(create_customer_record("Hassan", "hassan@example.com", city="Lahore", phone="0300-1234567"))
