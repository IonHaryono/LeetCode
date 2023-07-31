def minEatingSpeed(piles: list[int], h: int) -> int:
    l, r = 1, max(piles)
    while l <= r:
        hourCounter = 0
        k = (l+r)// 2
        for i in range(len(piles)):
            hourCounter += piles[i] // k
            if piles[i] % k > 0:
                hourCounter += 1
            if hourCounter > h:
                l = k + 1
                break
        if hourCounter <= h:    
            r = k - 1
    return l

print(
    minEatingSpeed(piles = [30,11,23,4,20], h = 6)
)


# print(
#     minEatingSpeed(piles = [30,11,23,4,20], h = 5)
# )