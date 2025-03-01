f = open("w3school/demofile3.txt", "w")  #Open the file "demofile3.txt" and overwrite the content
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("w3school/demofile3.txt", "r")
print(f.read())