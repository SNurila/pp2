f = open("w3school/demofile2.txt", "a")  #Open the file "demofile2.txt" and append content to the file
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("w3school/demofile2.txt", "r")
print(f.read())