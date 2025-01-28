x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y) #Convert the tuple into a list to be able to change it

print(x)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)