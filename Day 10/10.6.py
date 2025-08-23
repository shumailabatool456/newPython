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
num1 = int(input("What's the first number?:" ))
for symbols in operations:
    print(symbols)
operation_symbol = input("Pick a symbol from the above line:") 
calculation_function = operations[operation_symbol]
num2 = int(input("What's the second number?:" ))
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick a symbol from the above line:") 
calculation_function = operations[operation_symbol]
num3 = int(input("What's the second number?:" ))
second_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {second_answer}")
