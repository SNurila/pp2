import re

txt = "hello_world_my_name_is_nurila"
def toUpper(match):
    return match.group(0)[1].upper()  
x = re.sub(r'_[a-z]', toUpper, txt)
print(x)