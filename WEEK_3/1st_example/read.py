# Using read() → reads the entire file as one string

file = open("manually_created.txt", "r")   # Open file in read mode

contents = file.read()                     # Read the whole file

print("Output using read():")
print(contents)                            # Print as a single string

file.close()                               # Close the file