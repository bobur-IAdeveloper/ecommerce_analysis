from collections import Counter
from data_loader import load_csv

transactions = load_csv("data/transactions.csv")
products = load_csv("data/products.csv")

product_dict = {p["id"]: p["name"] for p in products}

def most_sold_products():
    product_count = Counter()
    top_5_products = {}

    for transaction in transactions:
        product_count[transaction["product_id"]] += int(transaction["quantity"])

    top_products = product_count.most_common(5)
    for id, count in top_products:
        product_name = product_dict.get(id, "Noma'lum")
        top_5_products[product_name] = count
    return top_5_products