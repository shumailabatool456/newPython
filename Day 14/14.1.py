import random
from game_data import data   # list of celebrities with followers

def get_random_account():
    """Return a random account from data"""
    return random.choice(data)

def format_account(account):
    """Format account info into readable string"""
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return f"{name}, a {desc}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Check user guess and return True if correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Main Game
score = 0
game_continue = True
account_a = get_random_account()

while game_continue:
    account_b = get_random_account()
    while account_a == account_b:
        account_b = get_random_account()

    print(f"Compare A: {format_account(account_a)}")
    print("VS")
    print(f"Against B: {format_account(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"✅ Correct! Your score is: {score}.")
        account_a = account_b
    else:
        print(f"❌ Wrong! Final score: {score}")
        game_continue = False
