import os 
if os.path.exists("w3school/demofile.txt"):     #Check if file exists, then delete it
  os.remove("w3school/demofile.txt")
else:
  print("The file does not exist")