from analyzer import most_sold_products
from visualizer import plt

def main():
    while True:
        print("\n1 - Eng ko'p sotilgan mahsulotlar")
        print("2 - Sotuv statistikasini ko'rish")
        print("3 - chiqish")

        choice = input(">>> ")

        if choice == '1':
            print(most_sold_products())
        elif choice == '2':
            plt.show()
        elif choice == '3':
            break
        else:
            print("Noto'g'ri tanlov! Qayta urinib ko'ring!")

if __name__ == "__main__":
    main()