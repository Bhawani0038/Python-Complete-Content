# 13. Billing with Tax

def final_bill(amount, tax_rate=0.05):
    return amount + (amount * tax_rate)


print(final_bill(1000))
