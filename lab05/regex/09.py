import re
txt = "HelloWorldThisIsPython"
x = re.sub(r'(?<!^)(?=[A-Z])', ' ', txt)
print(x)