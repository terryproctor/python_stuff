people_in_diner = input('How many people are in the diner? \n')
people_in_diner = int(people_in_diner)
if people_in_diner > 8:
    print('They\'ll have to wait for a new table')
else:
    print('Their table is ready')