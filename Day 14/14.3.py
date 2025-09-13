import random
from game_data import data
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_account():
    """Return random account from data"""
    return random.choice(data)

def format_account(account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a {desc}, from {country}"

def check_answer(guess, follower_A, follower_B):
    if follower_A > follower_B:
        return guess == 'a'
    else:
        return guess == 'b'

score = 0
game_continue = True
account_A = random_account()

while game_continue:
    account_B = random_account()
    while account_A == account_B:
        account_B = random_account()

   
    print(f"Compare A: {format_account(account_A)}") 
    print("VS") 
    print(f"Against B: {format_account(account_B)}")

    guess = input("Which account has more followers? Type 'A' or 'B': ").lower()

    A_follower_count = account_A['follower_count']
    B_follower_count = account_B['follower_count']
    is_correct = check_answer(guess, A_follower_count, B_follower_count)
    clear()
    if is_correct:
        score += 1
        print(f"✅ Correct! Current score: {score}.")
        account_A = account_B   # winner ko next round me carry forward karna
    else:   
        print(f"❌ Wrong! Final score: {score}")
        game_continue = False
