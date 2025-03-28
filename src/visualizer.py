import matplotlib.pyplot as plt
from analyzer import most_sold_products

top_products = most_sold_products()

if not top_products:
    print("Eng ko‘p sotilgan mahsulotlar haqida ma’lumot yo‘q.")
else:
    labels, values = zip(*top_products.items())

    def show_top_products():
        plt.figure(figsize=(10, 5))
        plt.bar(labels, values, color='skyblue')
        plt.xlabel("Mahsulotlar")
        plt.ylabel("Sotilgan soni")
        plt.title("Eng ko‘p sotilgan mahsulotlar")
        plt.xticks(rotation=45, ha="right")
        plt.savefig("top_products.png", dpi=300, bbox_inches="tight")
