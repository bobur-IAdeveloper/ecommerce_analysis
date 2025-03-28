🛒 E-Commerce Data Analysis
This project analyzes e-commerce sales data, identifying the most sold products and visualizing sales statistics.

📌 Features
✅ Load data from CSV files
✅ Identify the most sold products
✅ Generate visual sales reports

📂 Project Structure
bash
Копировать
Редактировать
ecommerce_analysis/
│── data/
│   ├── products.csv          # List of products
│   ├── transactions.csv      # Sales transactions
│── src/
│   ├── data_loader.py        # Loads data from CSV
│   ├── analyzer.py           # Analyzes sales data
│   ├── visualizer.py         # Generates graphs
│── main.py                   # Runs the program
│── README.md                 # Project description
│── requirements.txt          # Required dependencies
⚙ Installation & Usage
1️⃣ Ensure Python 3 is installed.
2️⃣ Install dependencies:

sh
Копировать
Редактировать
pip install -r requirements.txt
3️⃣ Run the project:

sh
Копировать
Редактировать
python main.py
📊 Output
The list of top-selling products will be displayed in the terminal. A bar chart is saved as top_products.png and shown automatically.

Example Chart:


🔧 Troubleshooting
If the chart shows "Unknown" as a product name, check the products.csv file.

Ensure transactions.csv contains valid product IDs.
