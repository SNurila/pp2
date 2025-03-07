def isPalindrome(s):
    return s.lower() == s.lower()[::-1]

string = "Madam"
print(isPalindrome(string))