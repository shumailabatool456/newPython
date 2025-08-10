number = int(input("Enter a number: "))

if number == 0:
    print("zero")
elif number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("Invalid number")    
    #14.	Write a program that asks for a user's age and prints:

  # “Child” if age < 13
  #“Teenager” if age is 13–19   “Adult” if age is 20 or more
age = int(input("Enter your age: "))

if age < 13:
   print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20:
   print("Adult")
else: 
    print("Invalid")
#15.	Write a program using nested if to check if a number is even and greater than 10.
number = int(input("Enter anumber: "))
if number % 2 == 0:
    if number >10:
        print(" even number is greater than 10")
    else:
        print("even number not greater than 10")
else:    
 print("Invalid")
