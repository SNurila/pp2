import math
n = int(input())
l = int(input())
area = (l*l*n)/ (4 * math.tan(math.pi/n))
print(f"{area:.0f}")