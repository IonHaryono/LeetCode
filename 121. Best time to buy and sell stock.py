def maxProfit(prices: list[int]) -> int:
    
    pointer = 1
    memo = [0 for _ in range(len(prices))]
    maxDiff = 0
    #initialisation
    lowestNumber = prices[0]
 

    while pointer < len(prices):
        if prices[pointer] < lowestNumber:
            lowestNumber = prices[pointer]
        
        maxDiff = prices[pointer] - lowestNumber
        if maxDiff > 0:
            memo[pointer] =  max(memo[pointer], maxDiff)
        
        print(memo)
        
        pointer += 1

        # print(memo)
    return max(memo)

    


print(maxProfit(prices = [7,6,3,9,2,9,4,3,1,5]))
# print(maxProfit(prices = [3]))