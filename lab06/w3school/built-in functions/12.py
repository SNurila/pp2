ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)  #Filter the array, and return a new array with only the values equal to or above 18

for x in adults:
  print(x)


#The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not