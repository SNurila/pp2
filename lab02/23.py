thisset = {"apple", "banana", "cherry"}

thisset.remove("banana") #f the item to remove does not exist, remove() will raise an error.

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.discard("banana") #If the item to remove does not exist, discard() will NOT raise an error.

print(thisset)


thisset = {"apple", "banana", "cherry"}

x = thisset.pop() #Remove a random item by using the pop() method

print(x)

print(thisset)



thisset = {"apple", "banana", "cherry"}

thisset.clear() #The clear() method empties the set

print(thisset)


thisset = {"apple", "banana", "cherry"}

del thisset  #The del keyword will delete the set completely

print(thisset)