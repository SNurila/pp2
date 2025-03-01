class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'age')  #Get the value of the "age" property of the "Person" object:
print(x)
