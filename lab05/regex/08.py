import re
txt = "HelloWorldThisIsPython"

x = list(filter(None,re.split(r'(?=[A-Z])', txt)))
print(x)