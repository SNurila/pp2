thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")#Remove the first occurrence of "banana"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #Remove the second item
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist #Delete the entire list

thislist = ["apple", "banana", "cherry"]
thislist.clear() #Clear the list content
print(thislist)