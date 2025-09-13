# Debugging Exercise
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()
from random import randint
dice_img = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"] 
dice_num =  randint(0, 5)
print(dice_img[dice_num])

year = int(input("What's your year of birth."))
if year >= 1980 and year < 1994:
    print("You are millenial.")
elif year >= 1994:
    print("You are Gen Z.")
age = int(input("What is your age?"))
if age > 18:
    print(f"You can drive at age {age}.")

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words: "))
total_words = pages * word_per_page
print(total_words)
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
mutate([1,2,3,5,8,13])


year = int(input("What's your year of birth."))
if year > 1980 and year < 1994:
    print("You are millenial.")
elif year >= 1994:
    print("You are Gen Z.")
age = int(input("What is your age?"))
if age > 18:
    print(f"You can drive at age {age}.") 

for number in range (1 , 101):
    if  number  %  3  ==  0  and  number  %  5  ==  0:
        print (" FizzBuzz")
    elif  number  %  3  ==  0:
        print (" Fizz") 
    elif number % 5 == 0:
        print (" Buzz") 
    else :
         print ( number)
 

