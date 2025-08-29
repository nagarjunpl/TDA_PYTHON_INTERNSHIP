# Using readlines() → reads all lines into a list

file = open("manually_created2.txt", "r")   # Open file again

contents = file.readlines()                # Read all lines into a list

print("\nOutput using readlines():")
print(contents)                            # Print the list of lines

file.close()                               # Close the file