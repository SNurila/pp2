fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

for x in [0, 1, 2]:
  pass