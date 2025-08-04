import random
import string

print("Welcome to the PyPassword Generator!")

# Step 1: Ask the user how many letters, symbols, and numbers they want
letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))

# Step 2: Define possible characters

letters = list(string.ascii_letters)  # a-z + A-Z
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = list(string.digits) 

# Step 3: Randomly choose from each category
password_list = []

password_list += random.choices(letters, k=letters_count)
password_list += random.choices(symbols, k=symbols_count)
password_list += random.choices(numbers, k=numbers_count)

# Step 4: Shuffle the list so it’s not in order
random.shuffle(password_list)

# Step 5: Join list into a string
password = ''.join(password_list)

# Step 6: Display the result
print(f"Here is your password: {password}")

