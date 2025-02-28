import re

pattern = r"\ba.*b\b"

test_strings = ["Wedef", "abdwqfb", "a!@Dwrbb", "Dabbwokfpb", "abwdewb", "ba", "aEa-a_dadb", "aabb", 'ab']

for string in test_strings:
    match = re.fullmatch(pattern, string)  
    if match:
        print(f"Match: {string}")
    else:
        print(f"No match: {string}")