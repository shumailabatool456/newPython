
def prime_checker(number):
    for i in range(2, number-1):
        number % i == 0
        print("It's not a prime nuber")
print("it's not a prime number")       
n= int(input("Check the number: "))
prime_checker(number=n)