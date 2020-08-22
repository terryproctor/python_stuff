
users = {
'terry' : {
    'name':'Terry',
    'age': 36,
    'height':'173cm',
    'city': 'edinburgh',
    },

'barry' : {
    'name':'Barry',
    'age': 36,
    'height':'172cm',
    'city': 'york',
    },

'george' : {
    'name':'George',
    'age': 5,
    'height':'110cm',
    'city': 'edinburgh',    
    },

'gordon' : {
    'name':'Gordon',
    'age': 56,
    'height':'176cm',
    'city': 'edinburgh', 
}
}


for user, user_info in sorted(users.items()):
    print(f"{user.title()}")
    # print(f"Age: {user_info['age']}")
    # print(f"City: {user_info['city'].title()}")
    # print(f"Height: {user_info['height']}\n")
    for key, value in user_info.items():
        if key != "name":
            print(f"\t{key.title()}: {str(value).title()}")
   



