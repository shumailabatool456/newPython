# What will be the output of the following code, and why? 
# print("123" + 123)
#Ans: Output: This will not print , it gives type error because this line of code is trying to print a string and an integer which is not possible.
a = 13 
b = 14.5
result=a+b
print(result)
print(type(result))
#Q.
print("123")
print(type(123))
 
#    f strings are very useful when we does not  want to concatenate string s ,using a lot of + signs and converting data types of each variable.
score = 95 
age = 20
rank = "A"
print(f"Your score is {score}%, age is {age}, and rank is {rank}. ")
#Output: Your score is 95%, age is 20, and rank is A. 

print(3 * (3 + 3) / 3 - 3)
#Ans: Result:  3.0
#Because, firstly it solves the part inside parenthesis and then it multiply as according to PEMDAS rule,
#But also the left sign is prioritized so multiplication and division goes equally important, and addition and subtraction also, the sign which is on left side will be calculated first.

age = input("Enter your age: ") 
print("Your age is " + age + " years old. Type: " + str(type(age)))




height = 1.75  
weight = 68  
print(f"Your BMI is {weight / height ** 2}")

 #Q9.(In the Day 2 project, you built a Tip Calculator.
 #Write a Python snippet that:
 #Takes a bill amount
 #Takes a tip percentage (e.g., 10, 12, 15)
 #Splits the total bill (including tip) between 3 people
 #Prints the amount each person should pay (rounded to 2 decimal places))###
Bill = int(input("Enter the bill amount?\n"))
Tip_percent = int(input("Enter the tip percent you want to give? 10, 12, 15?\n"))
Tip_as_percent =Tip_percent/100 
Tip_amount = Bill*Tip_as_percent
Bill_amount = Bill + Tip_amount
people = 3
Bill_per_person = round(Bill_amount/3, 2)
print(f"Each  person should pay {Bill_per_person}")