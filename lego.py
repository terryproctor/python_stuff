age=input("age?")
age=int(age)
if (age >= 4) and (age <= 99):
    print('You can play with lego')
elif age<4:
    print('you are too young to paly with lego. Choking hazard!')
elif age>99: 
    print('You are too old to play with lego. Nobody knows why!')
else:
    print("uh-oh spaghettios")