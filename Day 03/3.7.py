
print("Welcome to the Pizza Deliveries")

size = input("What size of Pizza do you want? S, M, L: ")
add_pepperoni = input("Do you want to add pepperoni on it? Y, N: ")
extra_cheese = input("Do you want extra cheese? Y, N: ")

bill = 0

if size == "S":
    bill += 1000
elif size == "M":
    bill += 1500
elif size == "L":
    bill += 2000
else:
    print("Invalid pizza size selected.")

if add_pepperoni == "Y":
    if size == "S":
        bill += 200
    else:
        bill += 300

if extra_cheese == "Y":
    bill += 100

print(f"Your final bill is Rs. {bill}")
