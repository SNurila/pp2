class Person:  #a parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


class Student(Person): #a child class
  pass

x = Student("Andrew", "Garfield")  #Use the Student class to create an object, and then execute the printname method
x.printname()


#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

#To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Any", "Student")
x.printname()


#Python also has a super() function that will make the child class inherit all the methods and properties from its parent
#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
class Student(Person): 
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Git", "Hub")
x.printname()

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019  #add property

x = Student("Lionel", "Messi")
print(x.graduationyear)


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019) #Add a year parameter, and pass the correct year when creating objects
print(x.graduationyear)




class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self): #Add a method called welcome to the Student class
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()

