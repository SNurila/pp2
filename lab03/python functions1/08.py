def spy_game(nums):
    it = [0, 0, 7]
    index = 0
    for i in nums:
        if i == it[index]:  
            index += 1
        if index == len(it): 
            return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,7,2,0,4,5,0]))
print(spy_game([1,0,2,4,0,5,7]))