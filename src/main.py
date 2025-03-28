from analyzer import most_sold_products
from visualizer import show_top_products  # Import function, not plt

def main():
    while True:
        print("\n1 - Most sold products")
        print("2 - View sales statistics")
        print("3 - Exit")

        choice = input(">>> ")

        if choice == '1':
            top_products = most_sold_products()
            if not top_products:
                print("No data available!")
            else:    
                print("\nMost sold products:")
                for name, count in top_products.items():
                    print(f"  {name}: {count} sold")
        elif choice == '2':
            show_top_products()
            print("Chart saved!")
        elif choice == '3':
            break
        else:
            print("Invalid choice! Please try again!")

if __name__ == "__main__":
    main()
