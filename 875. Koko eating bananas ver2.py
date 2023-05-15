def minEatingSpeed(piles: list[int], h: int) -> int:
    
    def binarySearch(binaryList):
        low = 0
        high = len(binaryList)
        intStore = 0
        res = -1

        while low <= high:
            intStore = 0
            mid = (low + high) // 2 
            print("low: ", low)
            print("high", high)
            print("mid: ", mid) 
            for idx in range(len(piles)):
                print("piles idx: ", piles[idx])
                intStore += piles[idx] // mid
                if piles[idx] % mid > 0:
                    intStore += 1
                print("intStore: ", intStore)



            if intStore > h:
                low = mid + 1
            elif intStore <= h:
                res = mid
                high = mid - 1

            if low == 0 and high == 0:
                return 1


        return res
    x = max(piles)
    return binarySearch(range(1, x+1))



# print(minEatingSpeed(piles = [3,6,7,11], h = 8))
# print(minEatingSpeed(piles = [30,11,23,4,20], h = 5))
# print(minEatingSpeed(piles = [312412412], h = 312412411))
print(minEatingSpeed(piles = [312884470], h = 968709470))






