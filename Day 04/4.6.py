
import random
user_choice = input("What will you choose? choice 0 for Rock, choice1 for Paper, choice2 for Scissors " )
computer_choice = random.randint(0, 1)
print(f"computer choose {computer_choice}")
if user_choice == 0 and computer_choice ==2:
    print("You Win")
elif computer_choice > user_choice:
    print("You lose")
else:
    print("You typed invalid number. You lose.")