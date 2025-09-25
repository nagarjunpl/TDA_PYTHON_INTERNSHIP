import os
import pandas as pd

CSV_PATH = "data/expenses.csv"

def main(path=CSV_PATH):
    df = pd.read_csv(path)
    print("--- HEAD ---")
    print(df.head())

    print("\n--- DESCRIBE ---")
    print(df[['amount']].describe())

    # Total expenses
    total_spent = df['amount'].sum()
    print(f"\nTotal Expenses: {total_spent}")

    # Expenses by category
    by_category = df.groupby('category')['amount'].sum()
    print("\n--- EXPENSES BY CATEGORY ---")
    print(by_category)

    # Expenses by payment mode
    by_payment = df.groupby('payment_mode')['amount'].sum()
    print("\n--- EXPENSES BY PAYMENT MODE ---")
    print(by_payment)

    # Average spend per day
    avg_per_day = df.groupby('date')['amount'].sum().mean()
    print(f"\nAverage Daily Spend: {avg_per_day:.2f}")

    # Ensure output folder exists
    os.makedirs("data", exist_ok=True)

    # Save processed data
    df.to_csv("data/expenses_processed.csv", index=False)


main()
