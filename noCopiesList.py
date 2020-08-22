myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for i in myList:
    while i not in new_list:
        new_list.append(i)

print("The list with unique elements only:")
print(new_list)