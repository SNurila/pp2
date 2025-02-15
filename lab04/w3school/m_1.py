import mymodule as mx  #Create an alias for mymodule called mx

a = mx.person1["age"]
print(a)


import platform  #Import and use the platform module (it is a built in module)

x = platform.system()
print(x)

x = dir(platform)  #List all the defined names belonging to the platform module
print(x)


from mymodule import person1 #Import only the person1 dictionary from the module

print (person1["age"])

