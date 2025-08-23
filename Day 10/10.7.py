def add(n1, n2):
   return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = { "+" : add, 
             "-": subtract,
               "*": multiply,
                 "/": divide,
 }
def calculator():
   from art import logo
   num1 = float(input("What's the first number?:" ))
   for symbols in operations:
     print(symbols)
   should_continue = True
   while should_continue:

     operation_symbol = input("Pick a symbol :") 
     calculation_function = operations[operation_symbol]
     num2 = float(input("What's the next number?:" ))
     answer = calculation_function(num1, num2)
     print(f"{num1} {operation_symbol} {num2} = {answer}")
     if (input(f"Type  'y' to continue with calculating {answer}, or type 'n' to start new calculation:")) =="y":
      num1 = answer
     else:
      should_continue = False
      calculator()
calculator()




