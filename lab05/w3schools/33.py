import re

#The search() function returns a Match object:

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)



#Search for an upper case "S" character in the beginning of a word, and print its position:

y = re.search(r"\bS\w+", txt)
print(y.span())



#The string property returns the search string:

z = re.search(r"\bS\w+", txt)
print(z.string)



#Search for an upper case "S" character in the beginning of a word, and print the word:
t = re.search(r"\bS\w+", txt)
print(t.group())
