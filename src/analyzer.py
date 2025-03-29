from collections import Counter
from data_loader import load_csv

products = load_csv("data/data.csv")
products_dict = {p["StockCode"]: p["Description"] for p in products}

def most_sold_products():
    product_count = Counter()
    product = {}

    for i in products:
        product_id = i["StockCode"]
        quantity = int(i["Quantity"])
        product_count[product_id] += quantity

    top_5_products = product_count.most_common(5)
    for stockcode, count in top_5_products:
        product_name = products_dict.get(stockcode, "Noma'lum")
        product[product_name] = count
    return product


