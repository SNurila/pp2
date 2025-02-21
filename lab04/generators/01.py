def gen(N):
    for i in range(1,N+1):
        yield i ** 2

Gen = gen(10)
print(next(Gen))
print(next(Gen))
print(next(Gen))
print(next(Gen))
print(next(Gen))
print(next(Gen))
print(next(Gen))
print(next(Gen))
print(next(Gen))
print(next(Gen))