C = 0
def FarToCel (F):
    global C
    C = (5 / 9) * (F - 32)
    print(f"{C:.2f}")

FarToCel(190)