import random # Importing the random module

print(random.random()) # Print a random float between 0.0 to 1.0
print(random.randint(1, 10)) # Print a random integer between 1 and


fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))   # Example: banana

cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)   # Example: [3, 5, 1, 2, 4]
