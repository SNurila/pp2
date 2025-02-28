import re

pattern = r"\b[a-z]+_[a-z]+\b"

test_strings = ["a_a", "ab", "a_wrbb", "abbwokfpb_", "bw", "b_a", "aa_a_", "aa_bb"]

for string in test_strings:
    match = re.fullmatch(pattern, string)  
    if match:
        print(f"Match: {string}")
    else:
        print(f"No match: {string}")