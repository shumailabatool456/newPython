import random
from game_data import data
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_account():
    """Return random account from data"""
    return random.choice(data)
random_account()
def format_account(account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a{desc} from {country}"
def check_answer(guess, follower_A, follower_B):
    
    if follower_A > follower_B:
        return guess == 'A'
    else:
        return guess == 'B'
    
score = 0
game_continue = True
account_A = random_account()
while game_continue:
    account_B = random_account()
    while account_A == account_B:
        account_B = random_account()
    clear()
    print(f"Compare A: {format_account(account_A)}") 
    print("VS") 
    print(f"Against B: {format_account(account_B)}")

    guess = input("Which account has more followers? 'A' or 'B'.") 
    A_follower_count = account_A['follower_count']
    B_follower_count = account_B['follower_count']
    is_correct = check_answer(guess, A_follower_count, B_follower_count)
    if is_correct:
       score += 1
       print(f" Correct ✔ Your final score is {score}.")
    else:
        print(f"❌ your final score is {score}")
    game_continue = False

          

    
        

    

