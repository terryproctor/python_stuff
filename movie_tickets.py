

while True:
    user_age = input('How old are you?\nType quit to quit\n')
    if user_age == 'quit':
        break
    user_age = int(user_age)

    if user_age < 3:
        print('  You get in free!')
    elif user_age < 13:
        print('  Your ticket is $10.')
    else:
        print('  Your ticket is $15.')    

