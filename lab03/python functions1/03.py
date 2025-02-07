rabbits = 0
chickens = 0
def solve(numheads, numlegs):
    global rabbits, chickens
    chickens = int((numheads*4 - 94)/2)
    rabbits = numheads - chickens
    print(f"{rabbits} rabbits and {chickens} chickens")

solve(35,94)