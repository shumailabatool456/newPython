import random
import string

print("Welcome to the Password Generator!")

# Input: Convert to integers
letters_count = int(input("How many letters do you want in your password?\n"))
symbols_count = int(input("How many symbols do you want?\n"))
numbers_count = int(input("How many numbers do you want?\n"))

# Define character pools
letters = string.ascii_letters  # a-z + A-Z
symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?/'
numbers = string.digits         # 0-9

# Generate password characters
password = []

for _ in range(letters_count):
    password.append(random.choice(letters))

for _ in range(symbols_count):
    password.append(random.choice(symbols))

for _ in range(numbers_count):
    password.append(random.choice(numbers))

# Shuffle the characters
random.shuffle(password)

# Join list into string
final_password = ''.join(password)
print(f"Your generated password is: {final_password}")
