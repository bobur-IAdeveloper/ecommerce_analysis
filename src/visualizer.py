import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from analyzer import most_sold_products
from data_loader import load_csv

products = load_csv("data/products.csv")
product_dict = {p["id"]: p["name"] for p in products}

top_products = most_sold_products()

labels = [product_dict[prod_id] for prod_id, _ in top_products]
values = [count for _, count in top_products]

plt.bar(labels, values, color='skyblue')
plt.xlabel("Mahsulotlar")
plt.ylabel("Sotilgan soni")
plt.title("Eng ko‘p sotilgan mahsulotlar")
plt.xticks(rotation=45)