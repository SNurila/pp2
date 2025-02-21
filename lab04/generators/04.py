def gen(a,b):
    for i in range(a,b+1):
        yield i ** 2

for num in gen(4,19):
    print(num)