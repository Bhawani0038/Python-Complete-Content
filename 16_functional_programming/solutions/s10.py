# 10. Sales Report Function

def sales_report(sales_list):
    total = sum(sales_list)
    count = len(sales_list)
    average = total / count if count else 0
    return {
        "total_sales": total,
        "count": count,
        "average_sale": average,
    }


print(sales_report([200, 500, 350]))
