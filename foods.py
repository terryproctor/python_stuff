my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
friend_foods[0]='icecream'
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

print('My foods:')
for food in my_foods:
    print('\t'+food)
print('\n')

print("Friend\'s foods:")
for food in friend_foods:
    print('\t'+food)