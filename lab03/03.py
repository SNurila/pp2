x = lambda a : a + 10  #lambda func can have many arguments, but only one expression
print(x(5))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def myfunc(n):   #this function doubles the unknown number
  return lambda a : a * n

mydoubler = myfunc(2) #n = 2

print(mydoubler(11)) # a = 11


def myfunc(n): 
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


