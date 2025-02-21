n = int(input())

def gen(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

for num in gen(n):
    print(num)