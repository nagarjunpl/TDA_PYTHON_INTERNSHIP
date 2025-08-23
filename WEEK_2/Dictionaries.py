# Dictionary with string keys
student = {
    "name": "Nagarjun",
    "age": 20,
    "course": "Computer Science"
}
print(student)

print(student.keys()) # prints the keys of the dictionary

print(student.values()) # prints the values of the dictionary

print(student.items()) # prints the key-value pairs of the dictionary

print(student["name"]) # prints the value of the key "name"


# Dictionary with integer keys
info = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    "active": True,
    "marks": [90, 85, 92]
}
print(info)


# Updating and adding key-value pairs
student = {"name": "Nagarjun", "age": 20}

print(student)

student["age"] = 21   # Update value
student["college"] = "PESCE"  # Add new key-value pair

print(student)


# Removing key-value pairs
student = {"name": "Nagarjun", "age": 20, "course": "CSE"}

student.pop("age")         # Removes key "age"
del student["course"]      # Another way to remove

print(student)

student.clear()            # Clears all items

print(student)

# Looping through dictionaries
student = {"name": "Nagarjun", "age": 20}

# Loop through keys
for key in student.keys():
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(key, ":", value)


# Nested dictionaries
students = {
    "101": {"name": "Alice", "age": 21},
    "102": {"name": "Bob", "age": 22},
}

print(students["101"]["name"])  # Alice
