import random

print("Welcome to the Password Generator")
for number in range(1, 5):
     print(number, end=" ")
for number in range(1, 6):
     if number % 3 == 0:
       print("Fizz")
else:
        print(number)
#Ans:        1
#             2
#             Fizz
#             4
#             5

# print highest score 
scores = [87, 45, 92, 100, 76]

high_score = 0
for score in scores: 
    if score > high_score:
      high_score = score
print(high_score)
# Password generator 
import random
import string

print("Welcome to the Password Generator!")

# Input: Convert to integers
letters_count = int(input("How many letters do you want in your password?\n"))
symbols_count = int(input("How many symbols do you want?\n"))
numbers_count = int(input("How many numbers do you want?\n"))

# Define character pools
letters = string.ascii_letters  
symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?/'
numbers = string.digits         

# Generate password characters
password = []

for _ in range(letters_count):
    password.append(random.choice(letters))

for _ in range(symbols_count):
    password.append(random.choice(symbols))

for _ in range(numbers_count):
    password.append(random.choice(numbers))

final_password = ''.join(password)
random.shuffle(password)
print(f"Your generated password is: {final_password}")

random.shuffle(password)
# 
#10.Explain how randomness is achieved in the password generator.
#Ans: By using Python’s random module functions like random.choice() and
#  random.shuffle() 
#random.choice() is used to choose random characters in the password generator.
#  It gives the password in the sequence — for example, if we choose 4 letters,
#  2 symbols, and 2 numbers, it chooses all characters randomly and the password
#  may look like fgsQ%&97. However, random.shuffle() shuffles all the characters 
# so the password may look like this g8k*o3!m.