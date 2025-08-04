height = float(input("enter your height in m:"))
weight = float(input("enter your weight in kg:"))
BMI = weight /height**2
print(BMI)
if BMI < 18.5: 
    print("Your are Under weight.")
elif BMI <25:
    print("You have Normal weight.")
elif BMI <30:
    print("You are Over weight.")
else:
    print("You are Obese")