# Even-Odd Checker (Medium Version)

print("===== EVEN-ODD CHECKER =====")

count = int(input("How many numbers do you want to check? "))

numbers = []
even = []
odd = []

for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("\n===== RESULTS =====")
print("Numbers Entered:", numbers)
print("Even Numbers:", even)
print("Odd Numbers:", odd)
print("Total Even:", len(even))
print("Total Odd:", len(odd))
