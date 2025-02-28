import re

pattern = r"[A-Z][a-z]+"

test_strings = ["Wedef", "abdwqf", "Dwrbb", "Dabbwokfp", "bwdew", "ba", "Eaadad", "aabb"]

for string in test_strings:
    match = re.fullmatch(pattern, string)  
    if match:
        print(f"Match: {string}")
    else:
        print(f"No match: {string}")