students = ["Nagarjun", "Arjun", "Dhanya"]

try:
    file = open("f1.txt", "w")
    for student in students:
        file.write(f"{student}\n")
    file.close()
    print("f1.txt written successfully!")

except FileNotFoundError:
    print("Error: The folder path does not exist.")
except PermissionError:
    print("Error: You don't have permission to write to this file.")
except Exception as e:
    print("Unexpected error:", e)


# Writing to a CSV file with 'with' (auto closes file)
students = ["Nagarjun1", "Arjun1", "Dhanya1"]

try:
    with open("f2.csv", "w") as file:
        for student in students:
            file.write(f"{student}\n")
    print("f2.csv written successfully!")

except FileNotFoundError:
    print("Error: The folder path does not exist.")
except PermissionError:
    print("Error: You don't have permission to write to this file.")
except Exception as e:
    print("Unexpected error:", e)
