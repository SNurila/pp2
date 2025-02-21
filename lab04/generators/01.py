def gen(N):
    for i in range(1,N+1):
        yield i ** 2

for num in gen(10):
    print(num)