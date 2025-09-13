import random
import string

def generate_password(length=12, use_symbols=True):
    # Define character sets
    letters = string.ascii_letters   # a-z, A-Z
    digits = string.digits           # 0-9
    symbols = string.punctuation     # !@#$%^&* etc.

    # Base pool
    pool = letters + digits
    if use_symbols:
        pool += symbols

    # Generate password
    password = ''.join(random.choice(pool) for _ in range(length))
    return password


# --- Interactive program ---
print("Password Generator")

# Ask user for length
length = int(input("Enter password length: "))

# Ask user for symbol choice
choice = input("Include symbols? (yes/no): ").lower()
use_symbols = True if choice == "yes" else False

# Generate and show password
password = generate_password(length, use_symbols)
print("\nYour Generated Password:", password)
