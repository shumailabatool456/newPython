import random
print("Welcome to the Number Guessing Game.")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
number = random.randint(1, 100)
if difficulty == 'easy':
    attempts = 10
else:
   attempts = 5
while attempts != 0:
    Guess = int(input("Make a guess."))
    print(f"You have {attempts} attemps.")
    if Guess > number:
       print("too high")
    elif Guess < number:
       print("too low")
    else:
       print(f"You have got the right number {number}")
    
    attempts -= 1
    print(f"You have {attempts} attempts remaining.")  
    if attempts == 0:
       print("You have run out guesses. You lose.") 

