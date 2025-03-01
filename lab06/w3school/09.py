'''
"x" - Create - will create a file, returns an error if the file exists

"a" - Append - will create a file if the specified file does not exists

"w" - Write - will create a file if the specified file does not exists
'''


f = open("w3school/myfile.txt", "x") #Create a file called "myfile.txt"
#f = open("w3school/myfile.txt", "w") Create a new file if it does not exist
