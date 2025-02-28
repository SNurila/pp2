import re

pattern = r"ab*"

test_strings = ["a", "ab", "abb", "abbb", "b", "ba", "aaa", "aabb"]

for string in test_strings:
    match = re.fullmatch(pattern, string)  
    if match:
        print(f"Match: {string}")
    else:
        print(f"No match: {string}")