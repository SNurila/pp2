string = "Hello World"
upper = sum(1 for c in string if c.isupper())
lower = sum(1 for c in string if c.islower())
print(upper)
print(lower)