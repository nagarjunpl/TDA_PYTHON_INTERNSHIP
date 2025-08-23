# Class and objects with init method
class Student:
    def __init__(self, name, age):
        self.name = name  # assign values to object
        self.age = age

# Creating objects
s1 = Student("Nagarjun", 20)
s2 = Student("Arjun", 19)

print(s1.name, s1.age)  # Nagarjun 20
print(s2.name, s2.age)  # Arjun 19


# Class and objects with init method and methods
class Student:
    def __init__(self, name, age):   # constructor
        self.name = name
        self.age = age

    def display(self):               # method
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects
s1 = Student("Nagarjun", 20)
s2 = Student("Arjun", 19)

s1.display()
s2.display()


# Class and objects with init method and methods
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

rect = Rectangle(10, 5)
print("Area:", rect.area())  # 50


# Class and objects with class and instance variables
class Student:
    college = "PESCE"   # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

s1 = Student("Nagarjun")

print(s1.college, s1.name)  # PESCE Nagarjun


# OOPs concepts

# Class with Methods
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(10, 5)
print("Area:", rect.area())           # 50
print("Perimeter:", rect.perimeter()) # 30


# Class with Instance, Class and Static Methods
class Demo:
    def instance_method(self):
        print("This is an instance method")

    @classmethod
    def class_method(cls):
        print("This is a class method")

    @staticmethod
    def static_method():
        print("This is a static method")

obj = Demo()
obj.instance_method()
Demo.class_method()
Demo.static_method()


# Inheritance (Reusing Classes)
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):   # Dog inherits from Animal
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()  # Dog barks


# Encapsulation (Data Protection)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500


# Polymorphism
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

for animal in (Cat(), Dog()):
    animal.sound()
