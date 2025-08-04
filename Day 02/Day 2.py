# Get user input
two_digit_number = input("Type a two-digit number: ")

# Check input type
print(type(two_digit_number))  # This will show <class 'str'>

# Get the individual digits
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the digits
result = first_digit + second_digit

# Show result
print("The sum of the digits is:", result)
