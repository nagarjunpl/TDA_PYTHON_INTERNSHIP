age = 21
print(type(age))  

pi = 3.14
print(type(pi)) 

name = "Nagarjun"
print(type(name))   

fruits = ["apple", "banana", "mango"]
print(type(fruits))   


# Problems

# Take two integers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)


# Area and circumference of a circle
radius = float(input("Enter radius of circle: "))

area = 3.14159 * radius * radius
circumference = 2 * 3.14159 * radius

print("Area:", area)
print("Circumference:", circumference)


# String operations
text = input("Enter a string: ")

print("Uppercase:", text.upper())
print("Length:", len(text))
print("Reversed:", text[::-1])


# String Manupulation
first_name = "nagarjun"
last_name = "pl"

print(first_name + " " + last_name)


# repititions

name = "Arjun \n"*5  # printing a 5 times
print(name)

# escape sequences

message = "i'm a 'nagarjun'" # using double quotes inside single quotes
print(message)


# formatted strings

first = "nagarjun"
last = "pl"

full = f"{first} {last}"
print(full)


# Dictionary operations
student = {"name": "Nagarjun", "age": 21, "marks": 75}

print("Student Name:", student["name"])

# Increase marks by 10
student["marks"] += 10
print("Updated Student Details:", student)


# List operations
numbers = [10, 25, 7, 42, 18]

print("Numbers:", numbers)
print("Largest:", max(numbers))
print("Smallest:", min(numbers))
print("Sum:", sum(numbers))
