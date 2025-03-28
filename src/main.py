from analyzer import most_sold_products
from visualizer import show_top_products  # plt emas, funksiya import qilamiz

def main():
    while True:
        print("\n1 - Eng ko'p sotilgan mahsulotlar")
        print("2 - Sotuv statistikasini ko'rish")
        print("3 - Chiqish")

        choice = input(">>> ")

        if choice == '1':
            top_products = most_sold_products()
            if not top_products:
                print("Ma'lumotlar yuq!")
            else:    
                print("\n Eng ko‘p sotilgan mahsulotlar:")
                for name, count in top_products.items():
                  print(f"  {name}: {count} ta sotilgan")
        elif choice == '2':
            show_top_products()
            print("Diagramma saqlandi!")
        elif choice == '3':
            break
        else:
            print("Noto'g'ri tanlov! Qayta urinib ko'ring!")

if __name__ == "__main__":
    main()
