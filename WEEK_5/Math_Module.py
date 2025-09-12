import math # Importing the math module

# Math functions
print(math.sqrt(16))     # Square root → 4.0
print(math.factorial(5)) # Factorial → 120
print(math.pi)           # Value of π → 3.141592653589793
print(math.pow(2, 3))    # 8.0 (2^3)
print(math.exp(2))       # e^2
print(math.log(2))       # 10 (inclusive)

# Constants
print(math.pi)     # 3.14159...
print(math.e)      # 2.71828...
print(math.tau)    # 6.28318... (2π)
print(math.inf)    # Infinity
print(math.nan)    # Not a Number


# Example: Calculate area and circumference of a circle
radius = 7
area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius

print("Area:", area)
print("Circumference:", circumference)
