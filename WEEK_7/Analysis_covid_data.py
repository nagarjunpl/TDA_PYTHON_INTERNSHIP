import os
import pandas as pd

CSV_PATH = "data/covid_sample.csv"

def main(path=CSV_PATH):
    df = pd.read_csv(path)
    print("--- HEAD ---")
    print(df.head())

    print("\n--- DESCRIBE ---")
    print(df[['new_cases', 'total_cases', 'new_deaths', 'total_deaths']].describe())

    # Calculate Case Fatality Rate (CFR) per row
    df['cfr'] = (df['total_deaths'] / df['total_cases']) * 100

    # Summary stats
    print("\n--- SUMMARY ---")
    print(f"Overall average CFR: {df['cfr'].mean():.2f}%")
    print(f"Total new cases: {df['new_cases'].sum()}")
    print(f"Total new deaths: {df['new_deaths'].sum()}")

    # Group by country
    grp = df.groupby('country').agg(
        days_reported=('date', 'count'),
        total_cases=('total_cases', 'max'),
        total_deaths=('total_deaths', 'max'),
        avg_new_cases=('new_cases', 'mean'),
        avg_new_deaths=('new_deaths', 'mean'),
        avg_cfr=('cfr', 'mean'),
    )

    print("\n--- GROUP BY COUNTRY ---")
    print(grp)

    # Ensure output folder exists
    os.makedirs("data", exist_ok=True)

    # Save processed data
    df.to_csv("data/covid_sample_processed.csv", index=False)


main()
