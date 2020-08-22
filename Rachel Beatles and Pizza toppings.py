# pizza_topping = 'haggis'
# print(pizza_topping == 'haggis')
# print(pizza_topping == 'mushrooms')

# rachel_stevens = 'hot'
# print(rachel_stevens != 'hot')
# print(rachel_stevens == 'hot')
# print(rachel_stevens == 'uggers')
# print(rachel_stevens != 'uggers')

# rachel_stevens_age = 38
# if rachel_stevens_age >= 18:
#     print('Ain\'t no party, like an s-club party!')
# print(rachel_stevens_age>=18)

beatles = ['Ringo', 'Paul', 'George', 'John']
beatles.append('Terry')
band_member='Ringo'
beatles.remove('George')
beatles.pop(1)
if band_member in beatles:
    print('I\'m in the band!')
else: 
    print("You're not in the band!")

if (len(beatles) == 4):
    print('The fab four!')
else: 
    print('huh?')
print(beatles)

if 'Terry' in beatles:
    print('Imposter alert!') 

if 'John' or 'Ringo' in beatles:
    print('yeah baby yeah!')

if 'George' not in beatles:
    print('uh-oh spaghetios!')