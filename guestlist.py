guest_list=["Arsene Wenger","AOC","Rachel Stevens"]
#print(guest_list)
#print("Dear",guest_list[0],"I would love for you to attend my dinner party.")
#print("Dear",guest_list[1],"I would love for you to attend my dinner party.")
#print("Dear",guest_list[2],"I would love for you to attend my dinner party.")
print("Unfortuantley",guest_list[0],"cannot make the dinner!")

guest_list[0]="Frankie Boyle"
#print("Dear",guest_list[0],"I would love for you to attend my new dinner party.")
#print("Dear",guest_list[1],"I would love for you to attend my new dinner party.")
#print("Dear",guest_list[2],"I would love for you to attend my new dinner party.")

print("We have now upgraded our table to a bigger one!")
guest_list.insert(0,"Nelson Mandela")
guest_list.insert(2,"Andy Bolton")
guest_list.append("Greta Thunberg")
#print(guest_list)

#print("Dear",guest_list[0],"I would love for you to attend my bigger dinner party.")
#print("Dear",guest_list[1],"I would love for you to attend my bigger dinner party.")
#print("Dear",guest_list[2],"I would love for you to attend my bigger dinner party.")
#print("Dear",guest_list[3],"I would love for you to attend my bigger dinner party.")
#print("Dear",guest_list[4],"I would love for you to attend my bigger dinner party.")
#print("Dear",guest_list[5],"I would love for you to attend my bigger dinner party.")
#print(guest_list)

print("Uh-oh spaghettios! The new table won't arrive in-time. I have only enough room for two guests")

print(guest_list.pop(),"you've been cut!")
print(guest_list.pop(),"you've been cut!")
print(guest_list.pop(),"you've been cut!")
print(guest_list.pop(),"you've been cut!")

print(guest_list[0], "your,re still going to the dinner party!")
print(guest_list[1], "your,re still going to the dinner party!")

del guest_list[0]
print(guest_list)
del guest_list[-1]
#print(guest_list[1]) #testing error