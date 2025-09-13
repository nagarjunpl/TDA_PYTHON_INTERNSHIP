import pandas as pd

# Create DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [85, 90, 88]
}
df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# Filter
print("People older than 28:")
print(df[df["Age"] > 28])

# Average score
print("Average Score:", df["Score"].mean())
