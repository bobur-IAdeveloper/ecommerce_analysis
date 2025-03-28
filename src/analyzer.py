from collections import Counter
from data_loader import load_csv

transactions = load_csv("data/transactions.csv")

def most_sold_products():
    """Eng ko‘p sotilgan mahsulotlarni topish"""
    product_count = Counter()
    
    for transaction in transactions:
        product_count[transaction["product_id"]] += int(transaction["quantity"])

    return product_count.most_common(5)

