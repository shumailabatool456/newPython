print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First decision
choice1 = input("Do you want to go left or right? ").lower()

if choice1 == "right":
    print("Game Over.")
elif choice1 == "left":
    # Second decision
    choice2 = input("Do you want to swim or wait? ").lower()
    if choice2 == "swim":
        print("Game Over.")
    elif choice2 == "wait":
        # Third decision
        choice3 = input("Which door? Red, Blue, or Yellow? ").lower()
        if choice3 == "red":
            print("Game Over.")
        elif choice3 == "blue":
            print("Game Over.")
        elif choice3 == "yellow":
            print("You Win!")
        else:
            print("Invalid door choice. Game Over.")
    else:
        print("Invalid action. Game Over.")
else:
    print("Invalid direction. Game Over.")
