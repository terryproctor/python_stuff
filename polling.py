favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

should_take_the_poll = ('terry', 'simon', 'dave', 'phil')

for person in should_take_the_poll:
    if person in favorite_languages.keys():
        print(f'Thanks for responding to the poll, {person.title()}.') 
    else:
        print(f'{person.title()}, you should take this poll.')
