number = input('Please enter a number: \n')
number = int(number)
if number %10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print("Number is not a multiple of 10")