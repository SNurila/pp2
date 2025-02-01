def my_function():
  print("Hello from a function")

my_function()


def my_function(fname): #fname - argument
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(*kids): #If the number of arguments is unknown, add a * before the parameter name
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")



def my_function(child3, child2, child1): #keyword arguments (kwargs)
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



def my_function(**kid):  #If the number of keyword arguments is unknown, add a double ** before the parameter name
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")




def my_function(country = "Norway"): #Norway is default parameter if we call func without parameter
  print("I am from " + country)

my_function("Sweden")
my_function()






def my_function(food): #passing a list as an argument 
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



def my_function(x): #return values
  return 5 * x

print(my_function(3))
print(my_function(5))




def myfunction():  #pass statement
  pass
  

def my_function(x, /): #positional only arguments
  print(x)

my_function(3)



def my_function(x):  #Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments
  print(x)

my_function(x = 3)


def my_function(*, x): #keyword-only arguments
  print(x)

my_function(x = 3)




def my_function(x):  #Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments
  print(x)

my_function(3)


def my_function(a, b, /, *, c, d): #combine pos-only and keyw-only arguments
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)