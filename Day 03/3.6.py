print("Welcome to the RollerCoaster")
height = int(input("What is your height in cm?"))
age = int(input("Enter your age:"))
bill = 0
#  (Nested Statement)
if height >= 120:
    if age <12:
        bill = 5
        print("Please pay 5$.")
    elif age <=18:
        bill = 7
        print("Please pay 7$.")
    else:
        print("Please pay 12$.")

    print("you can ride the RollerCoaster")
    wants_photo = input("Do you want to take photo? Y, N")
    if wants_photo == "Y"
else:
    print(" Sorry you have to grow taller before you can ride "))