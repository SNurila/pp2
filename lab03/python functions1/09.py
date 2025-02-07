import math
def SphereVolume(radius):
    vol = 4/3 * radius**3 * math.pi
    print(f"{vol:.3f}")
SphereVolume(4)