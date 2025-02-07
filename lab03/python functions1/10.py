def unique(items):
    unique_list = []
    for i in items:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)

unique([2,3,45,6,7,7,7,8,4,3,2,2])