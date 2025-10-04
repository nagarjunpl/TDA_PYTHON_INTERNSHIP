import csv
import datetime

CSV_FILE = "expenses.csv"

def initialize_csv():
    try:
        with open(CSV_FILE, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])
    except FileExistsError:
        pass  # File already exists

def add_expense(category, description, amount):
    date = datetime.date.today().strftime("%Y-%m-%d")
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print(f"✅ Expense added: {description} - ₹{amount}")

def view_expenses():
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def summary():
    totals = {}
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            totals[category] = totals.get(category, 0) + amount
    
    print("\n📊 Expense Summary:")
    for category, total in totals.items():
        print(f"{category}: ₹{total}")

def main():
    initialize_csv()
    
    while True:
        print("\n==== Daily Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            category = input("Enter category (Food, Travel, Shopping, etc.): ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            add_expense(category, description, amount)
        
        elif choice == "2":
            view_expenses()
        
        elif choice == "3":
            summary()
        
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice, try again.")

main()