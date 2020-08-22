number1 = int(input('First number?'))
number2 = int(input('Second number?'))
number3 = int(input('Third number?'))

largest_number = number1

if number2> largest_number:
    largest_number = number2

if number3>largest_number:
    largest_number = number3

print(largest_number)