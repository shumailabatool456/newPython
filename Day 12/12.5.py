def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    difference = abs(guess - answer)
    if guess > answer:
        print("Too high.")
        
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"🎉 You got it! The answer was {answer}.")
        return turns
    if difference <= 5:
            print("Your guess is too close.")
    elif difference >= 20:
            print("Your guess is far away.")
    return turns - 1