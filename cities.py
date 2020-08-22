cities = {
    'London' : {
        'country' : 'England',
        'population' : 9E7, 
        'fact' : 'Only six people died in the Fire of London', 
    },

    'Venice' : {
        'country' : 'Italy',
        'population' : 3E6, 
        'fact' : 'Venice is sinking', 
    },

    'Paris' : {
        'country' : 'France',
        'population' : 2E7, 
        'fact' : 'The Eiffel Tower was only supposed to be a temporary installation', 
    }
}

for city, info in cities.items():
    print(city)
    for key, value in info.items():
        print(f"{key.title()}: {value}")
    print('\n')