def longestConsecutive(nums: list[int]) -> int:
    nSet = set(nums)
    output = 0
    longest = 0 
    for i in range(len(nums)):
        # print("numsi: ", str(nums[i]))
        if (nums[i] - 1) not in nSet:
            longest = 0
            while nums[i] + longest in nSet:
                # print("numsi + longest: " + str(nums[i] + longest))
                longest += 1
            output = max(output, longest)
    return output


print(
    longestConsecutive(nums = [9,1,4,7,3,-1,0,5,8,-1,6])
)