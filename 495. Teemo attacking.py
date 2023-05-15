def findPoisonedDuration(timeSeries: list[int], duration: int) -> int:


    i = 0
    res = 0
    while i < len(timeSeries):
        if timeSeries[i]+duration < timeSeries[i+1]:
            res += timeSeries[i]+ (duration - 1)

            return res


print(findPoisonedDuration(timeSeries = [1,4], duration = 2))
print(findPoisonedDuration(timeSeries = [1,2,3,4,5,6,7,8,9], duration = 100000))

