# Defining a function
def greet():
    print("Hello, welcome to Python!")

# Calling the function
greet()


# Function with parameters
def greet_user(name):
    print("Hello,", name)

greet_user("Nagarjun")
greet_user("Arjun")


# Function with return value
def add(a, b):
    return a + b
    
result = add(5, 3)
print("Sum is:", result)


# Function with default parameter
def greet(name="Guest"):
    print("Hello,", name)

greet("Nagarjun")
greet()   # No argument, uses default


# Function with multiple return values
def calculate(a, b):
    sum_ = a + b
    diff = a - b
    return sum_, diff

x, y = calculate(10, 4)
print("Sum:", x)
print("Difference:", y)


# Function with variable number of arguments
def add_numbers(*args): # *args is a tuple of arguments
    return sum(args) # sum is a built-in function that returns the sum of the arguments

print(add_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55


# Function with variable number of keyword arguments
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Nagarjun", age=20, course="CSE")


# Function with multiple return values
def calculate(a, b):
    return a+b, a-b, a*b

sum_, diff, prod = calculate(10, 5)
print(f"Sum: {sum_}")
print(f"Difference: {diff}")
print(f"Product: {prod}")


# Lambda function
square = lambda x: x*x
print(square(5))  # 25


# Map function
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x*x, nums))
print(squares)  # [1, 4, 9, 16, 25]


# Global and local variables
x = 10  # global

def func():
    x = 5  # local
    print("Inside:", x)

func()
print("Outside:", x)


# Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120


# Decorator function
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

