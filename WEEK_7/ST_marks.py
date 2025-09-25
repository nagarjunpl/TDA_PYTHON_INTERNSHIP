import os
import pandas as pd

CSV_PATH = "data/student_marks.csv"

def main(path=CSV_PATH):
    df = pd.read_csv(path)
    print("--- HEAD ---")
    print(df.head())

    print('\n--- DESCRIBE ---')
    print(df[['math', 'science', 'english']].describe())

    # Add total and percentage
    df['total'] = df[['math', 'science', 'english']].sum(axis=1)
    df['percentage'] = df['total'] / 3

    # Pass/fail (pass if percentage >= 40)
    df['pass'] = df['percentage'] >= 40

    print('\n--- SUMMARY ---')
    print(f"Average percentage: {df['percentage'].mean():.2f}")
    print(f"Pass rate: {(df['pass'].mean() * 100):.1f}%")

    # Groupby class
    grp = df.groupby('class').agg(
        students=('student_id', 'count'),
        avg_percentage=('percentage', 'mean'),
        pass_rate=('pass', lambda x: x.mean() * 100),
    )
    print('\n--- GROUP BY CLASS ---')
    print(grp)

    # Ensure output folder exists
    os.makedirs("data", exist_ok=True)

    # Save cleaned CSV for further use
    df.to_csv("data/student_marks.csv", index=False)


main()
