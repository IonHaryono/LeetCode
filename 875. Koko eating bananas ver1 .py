def minEatingSpeed( piles: list[int], h: int) -> int:

  
    k = 1
    idx = 0
    intStore = 0

    while idx < len(piles):
        intStore += piles[idx] // k 
        idx += 1

        if piles[idx] % k > 0:
            intStore += 1

        if intStore > h:
            intStore = 0
            idx = 0
            k += 1
    return k






print(minEatingSpeed(piles = [3,6,7,11], h = 8))
print(minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(minEatingSpeed(piles = [312412412], h = 312412411))




