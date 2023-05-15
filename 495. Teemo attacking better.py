def findPoisonedDuration(timeSeries: list[int], duration: int) -> int:


    i = 0
    res = 0
    while i < len(timeSeries) -1 :
        if timeSeries[i]+duration-1 < timeSeries[i+1]:
            res += duration 
        elif timeSeries[i]+duration-1 >= timeSeries[i+1]:
            res += timeSeries[i+1] - timeSeries[i]
        i += 1
    # res += duration
    return res + duration


print(findPoisonedDuration(timeSeries = [1,4], duration = 2))
print(findPoisonedDuration(timeSeries = [1,3,4], duration = 2))
print(findPoisonedDuration(timeSeries = [1,2,3,4,5,6,7,8,9], duration = 100000))

print(findPoisonedDuration(timeSeries = [1,2,3,4,5,6,7,8,9], duration = 1))
print(findPoisonedDuration(timeSeries = [1,4], duration = 2))