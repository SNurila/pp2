n = int(input())
def gen(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in gen(n):
    print(num)