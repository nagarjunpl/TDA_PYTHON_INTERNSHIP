# Using readline() → reads only one line at a time

file = open("manually_created1.csv", "r")  # Open file again

contents = file.readline()                 # Read the first line

print("\nOutput using readline():")
print(contents)                            # Print the first line

file.close()                               # Close the file