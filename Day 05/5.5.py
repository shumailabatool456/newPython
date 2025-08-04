total = 0
for number in range(1, 100):
    total += number
    if number % 3 == 0:
     print("Fizz")
    elif number % 5 == 0:
     print("Buzz")
    elif number % 5 == 0 and number % 3 == 0:
     print("FizzBuzz")
    else:
        print(number)
