def isPalindrome (str):
    rev_str = ''
    for i in range(len(str)-1, -1, -1):
        rev_str += str[i]

    if str == rev_str:
        return True
    return False

print(isPalindrome("madam"))
