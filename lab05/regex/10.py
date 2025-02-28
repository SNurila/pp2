import re
txt = "helloWorldMyNameIsNurila"
def toLower(match):
    return '_' + match.group(0).lower()  
x = re.sub(r'[A-Z]', toLower, txt)
print(x)