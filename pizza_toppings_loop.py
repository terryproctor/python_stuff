toppings=[]
active = True
while active:
    topping = input('What  toppings do you want? else type quit\n\t')

    if topping == 'quit':
        break
    if len(toppings) == 7: 
        print("that's enough toppings!")
        break
    if topping.lower() == 'pineapple':
        print("that's disgusting I'm not putting pineapple on pizza!")
        active = False
    else:
        toppings.append(topping)


print(toppings)
