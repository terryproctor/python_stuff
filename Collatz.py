#input must be positive integer
c0 = int(input('Enter a positive integer: '))
if c0 < 1:
    c0 = int(input('Enter a POSITIVE integer: '))
#steps taken to arrive at final number
steps = 0

#c0 is now a positive number
while c0 != 1:
    if (c0%2 == 0): #even
        c0 = c0 / 2
        steps = steps + 1
        print(int(c0))
    else:           #odd
        c0 = 3 * c0 + 1
        print(int(c0))
        steps = steps + 1

print(f'steps: {steps}')
