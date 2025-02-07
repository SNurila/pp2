my_list = []
def has_33():
    global my_list
    len_list = int(input("number of elements = "))
    for i in range(len_list):
        a = int(input())
        my_list.append(a)

    for i in range(len_list+1):
        if i < len_list -1  and (my_list[i] == 3 and my_list[i+1] == 3):
            return True
    return False
        
print(has_33())