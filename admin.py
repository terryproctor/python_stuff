usernames = ['admin','colonel mustard', 'reverend green', 'mrs peacock', 'mrs white', 'professor plum', 'miss scarlett']
#usernames = []
if len(usernames) == 0:
    print('we need to find some more users!')

for username in usernames:
    if username != 'admin':
        print(f'Hello {username.title()}, thank you for logging in again.')
    elif username == 'admin':
        print('Hello admin, would you like to see a status report?')

