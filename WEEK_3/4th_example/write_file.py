# Open file in write mode ("w")
# If the file doesn't exist, it will be created.
# If it already exists, its content will be overwritten.
file = open("student.txt", "w")

file.write("Nagarjun\n")   # Write first line

file.write("Arjun")        # Write second line

file.close()               # Always close the file


# Append mode ("a")
# Opens the same file, but instead of overwriting, it adds content at the end.

file = open("student.txt", "a")

file.write("\nDhanya")     # Add a new line with "Dhanya"

file.close()
