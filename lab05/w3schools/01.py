import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)  #Search the string to see if it starts with "The" and ends with "Spain":
if x:
  print("YES! We have a match!")
else:
  print("No match")
