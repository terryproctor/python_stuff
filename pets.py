pets = []

pet = {
    'type': 'dog',
    'name': 'rover',
    'legs': 4,
    'tail': 'yes',
    'food': 'dogfood',
    }

pets.append(pet)

pet = {
    'type': 'snake',
    'name': 'sid',
    'legs': 'none',
    'tail': 'yes',
    'food': 'mice',
    }

pets.append(pet)

pet = {
    'type': 'cat',
    'name': 'henry',
    'legs': 4,
    'tail': 'yes',
    'food': 'catfood',
    }

pets.append(pet)

for animal in pets:
    print(f"{animal['name'].title()}")
    for attributes, value in animal.items():
        print(f"\t{attributes}: {value}")
    print('\n')

    