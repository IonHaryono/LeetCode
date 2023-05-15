def minEatingSpeed( piles: list[int], h: int) -> int:
    k = 1
    
    idx = 0
    hCounter = 0
    storePiles = []
    for i in piles:
        storePiles.append(i)


    while idx < len(piles):
        piles[idx] -= k
        hCounter += 1
        if piles[idx] <= 0:
            idx += 1



        if hCounter > h:
            hCounter = 0
            idx = 0
            k += 1

            piles = []
            for i in storePiles:
                piles.append(i)

    return k







# print(minEatingSpeed(piles = [3,6,7,11], h = 8))
print(minEatingSpeed(piles = [30,11,23,4,20], h = 5))




