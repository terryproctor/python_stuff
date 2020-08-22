rivers = {
    'nile': 'africa',
    'amazon': 'south america',
    'thames': 'europe',
    'mississippi': 'north america',
    'rheine': 'europe',
}

for river, continent in rivers.items():
    print(f'The {river.title()} runs through {continent.title()}.')
print('')

print('Rivers:')
for river in rivers.keys():
    print(f'\t{river.title()}')
print('')

print('Continents:')
for continent in rivers.values():
    print(f'\t{continent.title()}')