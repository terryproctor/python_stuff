sandwich_orders = [
    'tuna mayo', 
    'cheese and pickle', 
    'prawn mayo',
    'BLT',
    'cheese and tomato'
    ]

finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print(f"Finished sandwiches: \n{finished_sandwiches}")
