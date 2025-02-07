str = ''
def reverse():
    global str
    str = input()
    words = list(str.split(" "))
    print(" ".join(words[::-1]))

reverse()