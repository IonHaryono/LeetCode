from re import I


def maxProfit(prices: list[int]) -> int:
    

    memo = [0 for _ in range(len(prices))]
    pointer = 1
    maxDiff = 0
    res = 0
    #initalisation:
    lowestPrice = prices[0]

    while pointer < len(prices):
        if prices[pointer] < lowestPrice:
            lowestPrice = prices[pointer]
        if prices[pointer] <= prices[pointer -1]:
            lowestPrice = prices[pointer]
        
        maxDiff = prices[pointer] - lowestPrice
        if maxDiff > 0:
            if maxDiff > memo[pointer - 1]:
                memo[pointer] =  max(memo[pointer], maxDiff)
                memo[pointer - 1] = 0


        pointer += 1
        print(memo)
    

    trans1 = 0
    trans2 = 0
    for i in memo:
        if trans1 < i:
            trans2 = trans1
            trans1 = i
        elif trans2 <= i:
            trans2 = i
    res = trans1 + trans2

    return res


# print(maxProfit([7,1,5,3,6,4]))
# print(maxProfit([1,2,3,4,5]))
# print(maxProfit([7,6,4,3,1]))
# print(maxProfit([7,1,5,3,6,4,1,2,3,4,5]))
# print(maxProfit([5]))
# print(maxProfit([8,3,6,2,8,8,8,4,2,0,7,2,9,4,9]))

# print(maxProfit([3,2,6,5,0,3]))
print(maxProfit([1,2,4,2,5,7,2,4,9,0]))

"""
    while pointer < len(prices):
        if prices[pointer] < lowestPrice:
            lowestPrice = prices[pointer]
        if prices[pointer] < prices[pointer -1]:
            lowestPrice = prices[pointer]
        
        
        maxDiff = prices[pointer] - lowestPrice
        if maxDiff > 0:
            if maxDiff > memo[pointer - 1]:
                memo[pointer] =  max(memo[pointer], maxDiff)


        pointer += 1


        print(memo)
"""