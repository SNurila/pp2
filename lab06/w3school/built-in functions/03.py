mylist = [False, True, False]
x = any(mylist)  #Check if any of the items in a list are True
print(x)
#If the iterable object is empty, the any() function will return False



mydict = {0 : "Apple", 1 : "Orange"}
x = any(mydict)
print(x)

# Returns True because the second key is True.

# For dictionaries the any() function checks the keys, not the values.