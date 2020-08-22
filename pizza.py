pizzas=['mushroom', 'seafood', 'deep-fried']
for pizza in pizzas:
    print('I like',pizza,'pizzas.')

print('\nI really love pizzas!')

friends_pizzas=pizzas[:]
pizzas.append('fruit')
friends_pizzas.append('haggis')

print("My freind likes:") 
for pizza in friends_pizzas:
    print("\t\t"+pizza+",")