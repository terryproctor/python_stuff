fav_numbers = {
    'paul' : [4, 1],
    'jesus' : [42, 3, 1, 12],
    'judas' : [13, 666],
    'thiery' : [14, 49],
    'mike' : []
}

for people, numbers in fav_numbers.items():
    print (f"\n{people.title()} likes the")
    for number in numbers:
        print (f"{number}")
    
