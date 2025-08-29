# List of student names
students = ["Nagarjun", "Arjun", "Dhanya"]

# Write to a text file using normal open/close
file = open("s1.txt", "w")

for student in students:
    file.write(f"{student}\n")   # Write each student on a new line

file.close()   # Close the file



# Another list of student names
students = ["Nagarjun1", "Arjun1", "Dhanya1"]

# Write to a CSV file using 'with' (auto close after block)
with open("s2.csv", "w") as file:
    for student in students:
        file.write(f"{student}\n")   # Write each student on a new line