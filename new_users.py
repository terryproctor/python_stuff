current_users = ['Barneythedino', 'sWeetpea88', 'goonersaurus', 'TerryTibbs', 'uptheBlades76']
new_users = ['bigbertha', 'Sweetpea88', 'GeorgeGeorgeGeorgeoftheJungle', 'originalNuttah', 'TerryTibbs']

#list comprehension #current_user_lower = [user.lower() for user in current_users]
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'{new_user} username allready exists!\nPlease enter a new username')
    else:
        print(f'{new_user} username is available')