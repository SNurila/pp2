a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

if b > a:
  pass
