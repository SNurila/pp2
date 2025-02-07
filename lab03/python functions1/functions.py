def isPalindrome (str):
    rev_str = ''
    for i in range(len(str)-1, -1, -1):
        rev_str += str[i]

    return str == rev_str



def unique(items):
    unique_list = []
    for i in items:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)



items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def filtered (items):
        items = list(filter(lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)), items))
        print(items)
