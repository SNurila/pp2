from itertools import permutations
str = ''
def permutation():
    global str 
    str = input()
    perm_str = permutations(str)
    for i in perm_str:
        print("".join(i))
permutation()