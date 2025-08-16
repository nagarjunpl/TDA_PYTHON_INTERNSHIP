# Multiplication Table Generator

num = int(input("Enter a number for multiplication table: "))
limit = int(input("Enter the limit (e.g., 10): "))

print(f"\nMultiplication Table of {num}")
print("=" * 30)

for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")
