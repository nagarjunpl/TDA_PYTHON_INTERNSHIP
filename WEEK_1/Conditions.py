# if-else statement
b=20
if b % 2 == 0: # Check if b is even
    print("b is even")
else:
    print("b is odd")


# if-elif-else statement

c = 15
if c <20:
    print(f"{c} is less than 20")
elif c == 20:
    print(f"{c} is equal to 20")
else:
    print("c is greater than 20")


# input from user

d = int(input("Enter a number: "))
if d < 0:
    print("d is negative")  
elif d == 0:
    print("d is zero")
else:
    print("d is positive")


# logical operators

e = 5
f = 10

# if-else with logical operators

if e < 10 and f > 5:
    print("Both conditions are true")
else:
    print("At least one condition is false")

gender = input("Enter your Gender : ")
age = int(input("Enter your Age : "))

if gender == "Female" or gender == "female:":
    print("Ticket is Free!!!")
else :
    if age > 18 and age < 60:
        print("Ticket is 20")
    elif age >= 60:
        print("Ticket is 15 (Senior Citizen)")
    elif age <= 18 and age > 12:
        print("Ticket is 10 (50% discount)")
    elif age <= 12:
        print("Ticket is Free!!!")   


# For loop

city=["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
for i in city:
    print(i)  # Prints each city without index

name ="nagarjun"
for index, letter in enumerate(name): # Enumerate gives both index and letter
    print(letter*(index+1)) # Prints each letter multiplied by its index+1

a= [1, 2, 3, 4, 5]
for index,num in enumerate(a):
    print(f"{num} is in {index}th index ")  # Prints index and number from the list


pers_details = {"name": "Nagarjun", "age": 20, "city": "Mandya"}
print(pers_details.items()) # Prints key-value pairs of the dictionary

for key, value in pers_details.items():
    print(f"{key} : {value}")  # Prints each key-value pair in the dictionary


# While Condition

while 2>1: 
    print("2 is greater than 1")

    break  # This will prevent an infinite loop


i=1
while i <= 10:
    print(f"This is loop {i}")
    i = i+1


is_failed = True
i=1
while is_failed :
    print(f"Attempt {i}")
    i = i+1
    if i > 10:
        break  # Stop after 10 attempts
print("I gave up after 10 attempts")
