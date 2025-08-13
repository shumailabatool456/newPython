
vegies = ['potato', 'peas', 'spinach', 'brinjal']
print(vegies)
vegies.append('ladyfinger')
print(vegies)

import random
namesAsCSV = input("Enter names, splitting by commas. ")
names = namesAsCSV.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items-1)
person_who_pays = names[random_choice]
print(person_who_pays + " is going to pay the bill")

#17.	Create a list called fruits with "apple", "banana", and "cherry". Then add "orange" to it.
fruits = ['apple', 'banana', 'cherry'] 
print(fruits)
fruits.append('orange')  
print(fruits)        
#18.Write a small function that uses input() to take a user’s choice of "rock", "paper", or
#  "scissors" and prints a random choice by the computer
import random
user_choice = int(input("Enter your choice. Type 0 for rock, type 1 for paper, type 2 for scissors"))
computer_choice = random.randint(0, 2)
print(f"computer chooses{computer_choice}")
if user_choice == 0 and computer_choice == 2:
    print("You wins")
elif computer_choice > user_choice:
    print("You Lose")
else:
    print("Draw")
my_list = [1, 2, 3] 
print(my_list[2])
# 20.Create a 3x3 nested list (list of lists) representing a treasure map and 
# place an "X" at a user-specified location.
row1 = ["⬜","⬜", "⬜" ]
row2 = ["⬜","⬜", "⬜" ]
row3 = ["⬜","⬜", "⬜" ]
map = [row1, row2, row3]  

position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[vertical-1]
selected_row[horizontal-1] = "X"
print(f"{row1}\n{row2}\n{row3}")

zeros =['0', '0', '0', '0', '0']
print(zeros)
