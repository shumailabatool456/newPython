print("Welcome to the RollerCoaster")
height = int(input("What is your height in cm?"))
age = int(input("Enter your age:"))
#  (Nested Statement)
if height >= 120:
    if age <12:
        print("Please pay 5$.")
    elif age <=18:
        print("Please pay 7$.")
    else:
        print("Please pay 12$.")

    print("you can ride the RollerCoaster")
else:
    print(" Sorry you have to grow taller before you can ride ")