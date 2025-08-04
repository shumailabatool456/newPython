print("Welcome to the tip_calculator")
bill = int(input("What is the bill?"))
tip = int(input("How much tip you want to give? 10, 12,15? "))
people = int(input("How many people split the bill?"))
tip_as_percent = tip/100
tip_amount = bill*tip_as_percent
total_bill = tip_amount + bill
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay {final_amount} dollars")