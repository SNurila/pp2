fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist_1 = [x for x in fruits if "n" in x]
newlist_2 = [x for x in fruits if x != "apple"]
newlist_3 = [x if x != "banana" else "orange" for x in fruits]

print(newlist_1)
print(newlist_2)
print(newlist_3)
