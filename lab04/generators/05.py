n = int(input())
gen_exp = (x for x in range(n, -1, -1))
print(*gen_exp)