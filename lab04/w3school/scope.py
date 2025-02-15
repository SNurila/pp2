def myfunc():
  x = 300  #variable x in the local scope
  print(x)

myfunc()


def myfunc():
  x = 300  #The local variable can be accessed from a function within the function
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()



x = 300  #A variable created outside of a function is global and can be used by anyone

def myfunc():
  print(x)

myfunc()

print(x)




x = 300  #The function will print the local x, and then the code will print the global x

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)


def myfunc(): #If you use the global keyword, the variable belongs to the global scope
  global x
  x = 300

myfunc()

print(x)



x = 300  #To change the value of a global variable inside a function, refer to the variable by using the global keyword

def myfunc():
  global x
  x = 200  #the value of x will be changed

myfunc()

print(x)



def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x   #If you use the nonlocal keyword, the variable will belong to the outer function
    x = "hello"
  myfunc2()
  return x

print(myfunc1())




