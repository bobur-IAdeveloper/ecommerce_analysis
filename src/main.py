from analyzer import most_sold_products
from visualizer import show_top_products

def main():
    while True:
        print("\n1 - Eng ko'p sotilgan mahsulotlar")
        print("2 - Grafikni Ko'rish")
        print("3 - Chiqish")

        choice = input(">>> ")
        if choice == '1':
            p = most_sold_products()
            if not p:
                print("Ma'lumotlar yuq")
            else:
                print("Eng ko'p sotilgan mahsulotlar: ")
                for pr, cn in p.items():
                    print(f"{pr} {cn}ta sotilgan")
        elif choice == '2':
            show_top_products()
            print("Diagramma fayllarga saqlandi!")
        elif choice == '3':
            print("Dastur Tugadi...")
            break
        else:
            print("Notug'ri tanlov! qayta urinib ko'ring")

if __name__ == "__main__":
    main()
