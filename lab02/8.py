thislist = ["apple", "banana", "cherry"]
for x in thislist: #Print all items in the list, one by one:
    print(x)

thislist = ["Ford", "Tesla", "BMW"]
for i in range(len(thislist)): #Print all items by referring to their index number:
    print(thislist[i])

thislist = ["Tokyo", "Paris", "Rome"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


thislist = ["bread", "meat", "burger"]
[print(x) for x in thislist]