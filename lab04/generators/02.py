n = int(input())

def gen(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

print(*gen(n), sep = ',')