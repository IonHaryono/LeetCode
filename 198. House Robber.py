def rob(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    memo = [0 for _ in range(len(nums))]
    #initalisation
    memo[0] = nums[0]
    memo[1] = nums[1]


    idx = 0 
    while idx < len(nums):
        print("memo -1:", memo[idx-1])
        print("memo -2:", memo[idx-2])
        print("nums idx:", nums[idx])
        memo[idx] = max(memo[idx-1], memo[idx-2]+ nums[idx])
        print(memo)
        idx += 1

    return memo[-1]

# print(rob([1,2,3,1]))
# print(rob([2,1,1,2]))
# print(rob([1,2,1,1,1,2]))
print(rob([2,1,1,2]))
