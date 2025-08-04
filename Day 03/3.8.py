print("Welcome to the RollerCoaster")
height = int(input("What is your height in cm? "))
age = int(input("Enter your age: "))
bill = 0

if height >= 120:
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age < 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55: 
        print("Every one is having free ride on RollerCoaster by us")
    else:
        bill = 12
        print("Please pay $12.")

    print("You can ride the RollerCoaster.")
    wants_photo = input("Do you want to take a photo? Y or N: ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")