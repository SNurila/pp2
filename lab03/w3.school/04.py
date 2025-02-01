class MyClass:  #Create a class named MyClass, with a property named x
  x = 5
p1 = MyClass()  #Create an object named p1, and print the value of x
print(p1.x) 


class Person:  #Create a class named Person
  def __init__(self, name, age):  #use the __init__() function to assign values for name and age
    self.name = name 
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):  #The string representation of an object WITH the __str__() function
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


class Person:  #Insert a function that prints a greeting, and execute it on the p1 object
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


class Person:
  def __init__(mysillyobject, name, age):  #Use the words mysillyobject and abc instead of self
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
 
p1.age = 40 #modifying objects

print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age #delete an object

print(p1.age) #this will rise an error, since object property! does not exist (attribute error)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1 #deleting an object

print(p1)# this will raise an error, (name error)



class Person:
  pass
# having an empty class definition like this, would raise an error without the pass statement