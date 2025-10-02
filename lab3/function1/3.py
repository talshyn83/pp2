def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None, None 

heads = 35
legs = 94
chickens, rabbits = solve(heads, legs)
if chickens is not None and rabbits is not None:
    print(chickens)
    print(rabbits)
else:
    print("error")